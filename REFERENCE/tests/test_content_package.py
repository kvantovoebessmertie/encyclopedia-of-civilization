from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package


ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "water" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_water_package_is_complete_and_offline(tmp_path):
    records = _records()
    first = tmp_path / "package-1"
    report = build_content_package(
        records,
        package_dir=first,
        schema_path=SCHEMA,
        package_id="water-emergency-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["network_required"] is False
    assert report["recovered_record_count"] == len(records)
    assert report["findings"] == []
    assert (first / "manifest.json").is_file()
    assert (first / "schemas/005-RECORD-SCHEMA.json").is_file()
    assert (first / "publication.json").is_file()
    assert (first / "recovery-report.json").is_file()


def test_water_package_is_reproducible(tmp_path):
    records = _records()
    a = tmp_path / "a"
    b = tmp_path / "b"
    for target in (a, b):
        build_content_package(
            records,
            package_dir=target,
            schema_path=SCHEMA,
            package_id="water-emergency-v1",
        )

    # Compare canonical package components; recovery reports are generated from
    # the same deterministic inputs and therefore must also be byte-equivalent.
    for rel in (
        "manifest.json",
        "publication.json",
        "recovery-report.json",
    ):
        assert (a / rel).read_bytes() == (b / rel).read_bytes(), rel
