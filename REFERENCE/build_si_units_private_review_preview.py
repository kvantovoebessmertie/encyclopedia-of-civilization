from __future__ import annotations

import argparse
import json
from pathlib import Path

from encyclopedia_reference.public_reader import build_public_preview


ROOT = Path(__file__).resolve().parents[1]
RECORDS_DIR = ROOT / "CONTENT" / "vertical-slices" / "si-units-basics" / "records"
MANIFEST_PATH = ROOT / "REFERENCE" / "fixtures" / "si-units-private-review-manifest.json"

EXPECTED = {
    "CLM-SI-SEVEN-BASE": ("1", "claim"),
    "EU-SI-SEVEN-BASE": ("2", "evidence_use"),
    "CLM-SI-DERIVED": ("1", "claim"),
    "EU-SI-DERIVED": ("2", "evidence_use"),
    "SRC-NIST-SI-UNITS": ("1", "source"),
    "CTX-SI": ("1", "context"),
    "SCP-SI": ("1", "scope"),
}


def load_exact_records() -> list[dict]:
    records = []
    for record_id, (version, record_type) in EXPECTED.items():
        path = RECORDS_DIR / f"{record_id}.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("record_id") != record_id:
            raise ValueError(f"Record ID mismatch in {path}")
        if record.get("record_version") != version:
            raise ValueError(
                f"Unexpected version for {record_id}: "
                f"{record.get('record_version')} != {version}"
            )
        if record.get("record_type") != record_type:
            raise ValueError(f"Unexpected record type for {record_id}")
        records.append(record)

    by_id = {record["record_id"]: record for record in records}
    for evidence_id, claim_id in (
        ("EU-SI-SEVEN-BASE", "CLM-SI-SEVEN-BASE"),
        ("EU-SI-DERIVED", "CLM-SI-DERIVED"),
    ):
        evidence = by_id[evidence_id]
        if evidence["content"]["claim_ref"] != {"record_id": claim_id, "version": "1"}:
            raise ValueError(f"Unexpected Claim reference in {evidence_id}")
        if evidence["content"]["source_ref"] != {
            "record_id": "SRC-NIST-SI-UNITS",
            "version": "1",
        }:
            raise ValueError(f"Unexpected Source reference in {evidence_id}")

    if by_id["CTX-SI"]["content"]["target_ref"] != {
        "record_id": "CLM-SI-SEVEN-BASE",
        "version": "1",
    }:
        raise ValueError("CTX-SI target must remain Claim A v1")
    if by_id["SCP-SI"]["content"]["target_ref"] != {
        "record_id": "CLM-SI-SEVEN-BASE",
        "version": "1",
    }:
        raise ValueError("SCP-SI target must remain Claim A v1")

    seven_base_description = by_id["EU-SI-SEVEN-BASE"]["content"]["material"]["description"]
    if "Defining Constants" not in seven_base_description or "Base and Derived Units" not in seven_base_description:
        raise ValueError("Seven-base-unit Evidence Use is missing its NIST section pinpoints")
    derived_description = by_id["EU-SI-DERIVED"]["content"]["material"]["description"]
    if "Base and Derived Units" not in derived_description or "22 is not the total number" not in derived_description:
        raise ValueError("Derived-unit Evidence Use is missing its NIST pinpoint or the 22-unit boundary")

    source_uri = by_id["SRC-NIST-SI-UNITS"]["content"]["external_ref"]["uri"]
    if source_uri != "https://www.nist.gov/pml/owm/metric-si/si-units":
        raise ValueError("Unexpected NIST Source URI")

    return records


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a private, non-release preview of two SI Claims."
    )
    parser.add_argument("--source-revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manifest["source_revision"] = args.source_revision
    expected_selections = {
        (record_id, version) for record_id, (version, _) in EXPECTED.items()
    }
    actual_selections = {
        (item.get("record_id"), item.get("record_version"))
        for item in manifest.get("records", [])
    }
    if actual_selections != expected_selections:
        raise ValueError("Private preview manifest does not match the exact authorized ID/version set")

    records = load_exact_records()
    result = build_public_preview(records, manifest, args.output)
    if result["record_count"] != len(EXPECTED):
        raise AssertionError("Private preview record count changed")
    if result["redistribution_allowed"] is not False or result["network_required"] is not False:
        raise AssertionError("Private preview must remain non-redistributable and offline")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
