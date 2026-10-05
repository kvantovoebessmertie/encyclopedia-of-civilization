from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "emergency-hand-hygiene" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_emergency_hand_hygiene_slice_validates():
    records = _records()
    assert len(records) == 11
    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )
    assert validate_semantic_dataset(records) == []

    by_id = {record["record_id"]: record for record in records}
    process = by_id["PRC-HANDWASH-SOAP-WATER"]
    action = by_id["ACT-HANDWASH-SCRUB-20SEC"]
    result = by_id["RES-HANDWASH-CLEANING"]

    action_refs = {ref["record_id"] for ref in process["content"]["process_content"]["action_refs"]}
    assert action["record_id"] in action_refs
    frame_refs = {ref["record_id"] for ref in result["content"]["reference_frame"]["refs"]}
    assert process["record_id"] in frame_refs
    assert action["record_id"] in frame_refs


def test_emergency_hand_hygiene_publication_preserves_evidence(tmp_path):
    records = _records()
    report = build_content_package(
        records,
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="emergency-hand-hygiene-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
    publication = json.loads((tmp_path / "package" / "publication.json").read_text(encoding="utf-8"))
    claims = [entry for entry in publication["entries"] if entry["record_type"] == "claim"]
    assert len(claims) == 1
    assert claims[0]["evidence"]
    assert publication["citations_preserved"] is True
