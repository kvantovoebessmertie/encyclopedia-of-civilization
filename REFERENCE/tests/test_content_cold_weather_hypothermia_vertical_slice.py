from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "cold-weather-hypothermia" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records() -> list[dict]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CONTENT.glob("*.json"))
    ]


def test_cold_weather_hypothermia_slice_records_validate():
    validator = Validator(SCHEMA)
    records = _records()

    assert len(records) == 7
    assert {record["record_type"] for record in records} == {
        "source", "claim", "evidence_use", "context", "scope"
    }
    for record in records:
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )


def test_cold_weather_hypothermia_semantic_dataset_is_clean():
    assert validate_semantic_dataset(_records()) == []


def test_cold_weather_hypothermia_scope_is_explicit():
    records = _records()
    scope = next(record for record in records if record["record_type"] == "scope")
    assert scope["content"]["target_ref"]["record_id"] == "CLM-COLD-HYPOTHERMIA-SIGNS"
    assert scope["content"]["scope_content"]["population"] == "взрослые в общем населении"
