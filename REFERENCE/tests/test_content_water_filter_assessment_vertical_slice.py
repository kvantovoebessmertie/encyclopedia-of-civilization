from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "water-filter-assessment" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_water_filter_assessment_inference_slice_validates():
    records = _records()
    assert len(records) == 8
    validator = Validator(SCHEMA)
    assert all(validator.validate(record).passed for record in records)
    assert validate_semantic_dataset(records) == []

    by_id = {r["record_id"]: r for r in records}
    assessment = by_id["ASM-WATER-FILTER-APPLICABILITY"]["content"]["target"]
    inference = by_id["INF-WATER-FILTER-NOT-UNIVERSAL"]["content"]

    assert assessment["record_id"] == "CLM-WATER-FILTER-LIMITS"
    assert {p["record_id"] for p in inference["premises"]} == {
        "CLM-WATER-FILTER-LIMITS",
        "ASM-WATER-FILTER-APPLICABILITY",
    }
    assert inference["attribution"]["mode"] == "known"
    assert inference["limitations"]


def test_water_filter_assessment_package_preserves_epistemic_layers(tmp_path):
    report = build_content_package(
        _records(),
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="water-filter-assessment-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
    publication = json.loads((tmp_path / "package" / "publication.json").read_text(encoding="utf-8"))
    assert publication["citations_preserved"] is True
    assert any(e["record_type"] == "claim" and e["evidence"] for e in publication["entries"])
