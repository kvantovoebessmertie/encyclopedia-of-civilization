from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "power-outage-food" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_power_outage_food_slice_validates():
    records = _records()
    assert len(records) == 20
    validator = Validator(SCHEMA)
    assert all(validator.validate(record).passed for record in records)
    assert validate_semantic_dataset(records) == []


def test_power_outage_food_publication_preserves_evidence(tmp_path):
    records = _records()
    report = build_content_package(
        records,
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="power-outage-food-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
    publication = json.loads((tmp_path / "package" / "publication.json").read_text(encoding="utf-8"))
    claims = [entry for entry in publication["entries"] if entry["record_type"] == "claim"]
    assert len(claims) == 4
    assert all(entry["evidence"] for entry in claims)
    assert publication["citations_preserved"] is True
