#!/usr/bin/env python3
"""Deterministic content preflight executed before the full CI / Release Gate."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "REFERENCE" / "src"))

from encyclopedia_reference.validator import Validator  # noqa: E402


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    schema_path = ROOT / "IMPLEMENTATION/005-RECORD-SCHEMA.json"
    records_root = ROOT / "CONTENT/vertical-slices"
    coverage_path = ROOT / "RELEASE/CONTENT-COVERAGE.json"

    if not schema_path.is_file():
        fail(f"missing schema: {schema_path}")
    if not records_root.is_dir():
        fail(f"missing content root: {records_root}")
    if not coverage_path.is_file():
        fail(f"missing coverage manifest: {coverage_path}")

    validator = Validator(schema_path)
    findings: list[str] = []
    seen: defaultdict[tuple[str, str], list[str]] = defaultdict(list)
    record_paths = sorted(records_root.glob("*/records/*.json"))

    for path in record_paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            findings.append(f"{path}: invalid JSON: {exc}")
            continue

        if not isinstance(record, dict):
            findings.append(f"{path}: top-level value must be an object")
            continue

        record_id = record.get("record_id")
        record_version = record.get("record_version")
        if record_id is not None and record_version is not None:
            seen[(str(record_id), str(record_version))].append(str(path))

        result = validator.validate(record)
        for item in result.findings:
            if item.severity == "error":
                findings.append(
                    f"{path}: {item.code}: {item.message}"
                )

    for key, paths in sorted(seen.items()):
        if len(paths) > 1:
            findings.append(
                f"duplicate record identity {key[0]} @ version {key[1]}: "
                + ", ".join(paths)
            )

    slice_dirs = sorted(p for p in records_root.iterdir() if p.is_dir())
    for slice_dir in slice_dirs:
        slug = slice_dir.name
        if not (slice_dir / "README.md").is_file():
            findings.append(f"{slug}: missing README.md")
        record_dir = slice_dir / "records"
        if not record_dir.is_dir() or not list(record_dir.glob("*.json")):
            findings.append(f"{slug}: missing records")
        test_path = ROOT / "REFERENCE/tests" / (
            "test_content_" + slug.replace("-", "_") + "_vertical_slice.py"
        )
        legacy_test = (
            ROOT / "REFERENCE/tests/test_content_power_outage_vertical_slice.py"
            if slug == "power-outage-food" else None
        )
        if not test_path.is_file() and not (legacy_test and legacy_test.is_file()):
            findings.append(f"{slug}: missing regression test")

    try:
        coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
        expected_records = coverage["total_records"]
        expected_slices = coverage["vertical_slices"]
        actual_records = len(record_paths)
        actual_slices = len(slice_dirs)
        if actual_records != expected_records:
            findings.append(
                f"coverage record count mismatch: actual={actual_records}, "
                f"manifest={expected_records}"
            )
        if actual_slices != expected_slices:
            findings.append(
                f"coverage slice count mismatch: actual={actual_slices}, "
                f"manifest={expected_slices}"
            )
    except Exception as exc:
        findings.append(f"invalid coverage manifest: {exc}")

    if findings:
        print(f"PREFLIGHT FAILED: {len(findings)} finding(s)")
        for finding in findings:
            print(f" - {finding}")
        return 1

    print(
        "PREFLIGHT PASS: "
        f"{len(record_paths)} records, {len(slice_dirs)} slices, "
        f"{len(seen)} unique record identities."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
