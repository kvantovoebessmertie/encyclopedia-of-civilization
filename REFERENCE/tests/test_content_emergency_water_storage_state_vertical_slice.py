from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "emergency-water-storage-state" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_water_storage_state_relation_identity_slice_validates():
    records = _records()
    assert len(records) == 10
    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )
    assert validate_semantic_dataset(records) == []

    by_id = {r["record_id"]: r for r in records}
    subject = by_id["OBJ-WATER-CONTAINER"]
    state_a = by_id["ST-WATER-CONTAINER-SANITIZED"]
    state_b = by_id["ST-WATER-CONTAINER-STORED"]
    relation = by_id["REL-CONTAINER-WATER-STORAGE"]
    identity = by_id["ID-WATER-CONTAINER-CONTINUITY"]

    assert subject["record_type"] == "record"
    assert state_a["content"]["subject_ref"]["record_id"] == subject["record_id"]
    assert state_b["content"]["subject_ref"]["record_id"] == subject["record_id"]
    assert len(relation["content"]["participants"]) == 2
    assert {x["record_id"] for x in identity["content"]["targets"]} == {
        state_a["record_id"], state_b["record_id"]
    }
    assert identity["content"]["identity_status"] == "resolved_same"
    assert identity["content"]["uncertainty"]


def test_water_storage_package_preserves_epistemic_layers(tmp_path):
    report = build_content_package(
        _records(),
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="emergency-water-storage-state-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
    publication = json.loads((tmp_path / "package" / "publication.json").read_text(encoding="utf-8"))
    assert publication["citations_preserved"] is True
    assert any(e["record_type"] == "claim" and e["evidence"] for e in publication["entries"])
