#!/usr/bin/env python3
"""Deterministic content preflight executed before CI / Release Gate."""

from __future__ import annotations

import json
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "REFERENCE" / "src"))

from encyclopedia_reference.content_package import build_content_package  # noqa: E402
from encyclopedia_reference.semantic_rules import validate_semantic_dataset  # noqa: E402
from encyclopedia_reference.validator import Validator  # noqa: E402


def main() -> int:
    schema_path = ROOT / "IMPLEMENTATION/005-RECORD-SCHEMA.json"
    records_root = ROOT / "CONTENT/vertical-slices"
    coverage_path = ROOT / "RELEASE/CONTENT-COVERAGE.json"
    findings: list[str] = []

    for required in (schema_path, coverage_path):
        if not required.is_file():
            findings.append(f"missing required file: {required}")
    if not records_root.is_dir():
        findings.append(f"missing content root: {records_root}")
    if findings:
        print(f"PREFLIGHT FAILED: {len(findings)} finding(s)")
        for item in findings:
            print(f" - {item}")
        return 1

    validator = Validator(schema_path)
    record_paths = sorted(records_root.glob("*/records/*.json"))
    all_records: list[dict] = []
    seen: defaultdict[tuple[str, str], list[str]] = defaultdict(list)

    for path in record_paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            findings.append(f"{path}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            findings.append(f"{path}: top-level value must be an object")
            continue

        all_records.append(record)
        record_id = record.get("record_id")
        record_version = record.get("record_version")
        if record_id is not None and record_version is not None:
            seen[(str(record_id), str(record_version))].append(str(path))

        result = validator.validate(record)
        for item in result.findings:
            if item.severity == "error":
                findings.append(f"{path}: {item.code}: {item.message}")

    for key, paths in sorted(seen.items()):
        if len(paths) > 1:
            findings.append(
                f"duplicate record identity {key[0]} @ version {key[1]}: "
                + ", ".join(paths)
            )

    # Dataset-level semantic rules are deterministic release prerequisites.
    for item in validate_semantic_dataset(all_records):
        findings.append(f"semantic dataset: {item}")

    type_counts = Counter(
        r.get("record_type") for r in all_records
        if isinstance(r.get("record_type"), str)
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

    coverage = None
    try:
        coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
        if len(record_paths) != coverage["total_records"]:
            findings.append(
                f"coverage record count mismatch: actual={len(record_paths)}, "
                f"manifest={coverage['total_records']}"
            )
        if len(slice_dirs) != coverage["vertical_slices"]:
            findings.append(
                f"coverage slice count mismatch: actual={len(slice_dirs)}, "
                f"manifest={coverage['vertical_slices']}"
            )
        manifest_types = coverage.get("types", {})
        if not isinstance(manifest_types, dict):
            findings.append("coverage manifest: 'types' must be an object")
        else:
            for record_type, spec in sorted(manifest_types.items()):
                expected = spec.get("count") if isinstance(spec, dict) else None
                actual = type_counts.get(record_type, 0)
                if actual != expected:
                    findings.append(
                        f"coverage type count mismatch for {record_type}: "
                        f"actual={actual}, manifest={expected}"
                    )
            if set(manifest_types) != set(type_counts):
                findings.append(
                    "coverage type registry mismatch: "
                    f"actual={sorted(type_counts)}, manifest={sorted(manifest_types)}"
                )
    except Exception as exc:
        findings.append(f"invalid coverage manifest: {exc}")

    # Public registration and executable regression must remain one-to-one.
    content_readme = ROOT / "CONTENT/README.md"
    roadmap = ROOT / "ROADMAP.md"
    test_dir = ROOT / "REFERENCE/tests"
    if content_readme.is_file() and roadmap.is_file():
        readme_text = content_readme.read_text(encoding="utf-8")
        roadmap_text = roadmap.read_text(encoding="utf-8")
        regression_tests = {
            path.name for path in test_dir.glob("test_content_*_vertical_slice.py")
        }
        for slice_dir in slice_dirs:
            slug = slice_dir.name
            if f"vertical-slices/{slug}" not in readme_text:
                findings.append(f"{slug}: missing CONTENT/README.md registration")
            if f"vertical-slices/{slug}" not in roadmap_text:
                findings.append(f"{slug}: missing ROADMAP.md registration")
            expected = f"test_content_{slug.replace('-', '_')}_vertical_slice.py"
            if expected not in regression_tests and not (
                slug == "power-outage-food"
                and "test_content_power_outage_vertical_slice.py" in regression_tests
            ):
                findings.append(f"{slug}: missing dedicated regression test")
        if len(regression_tests) != len(slice_dirs):
            findings.append(
                f"regression test count mismatch: tests={len(regression_tests)}, "
                f"slices={len(slice_dirs)}"
            )

    # The same package/recovery path used by corpus coverage is exercised here.
    # It also runs dataset integrity and ReferenceResolver checks.
    if all_records:
        with tempfile.TemporaryDirectory(prefix="encyclopedia-preflight-") as temp_dir:
            report = build_content_package(
                all_records,
                package_dir=Path(temp_dir) / "package",
                schema_path=schema_path,
                package_id="preflight-content",
            )
            if report["integrity_and_validation"] != "PASS" or report["findings"]:
                findings.append(
                    "content package/recovery preflight failed: "
                    + json.dumps(report["findings"], ensure_ascii=False)
                )

    if findings:
        print(f"PREFLIGHT FAILED: {len(findings)} finding(s)")
        for finding in findings:
            print(f" - {finding}")
        return 1

    print(
        "PREFLIGHT PASS: "
        f"{len(record_paths)} records, {len(slice_dirs)} slices, "
        f"{len(seen)} unique record identities, {len(type_counts)} record types."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
