from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "generator-carbon-monoxide-safety" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records() -> list[dict]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CONTENT.glob("*.json"))
    ]


def test_generator_carbon_monoxide_safety_records_validate():
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


def test_generator_carbon_monoxide_safety_semantic_dataset_is_clean():
    assert validate_semantic_dataset(_records()) == []


def test_generator_carbon_monoxide_safety_claims_have_direct_evidence():
    records = _records()
    claims = {r["record_id"] for r in records if r["record_type"] == "claim"}
    evidence_claims = {
        r["content"]["claim_ref"]["record_id"]
        for r in records
        if r["record_type"] == "evidence_use"
    }
    assert claims == evidence_claims


def test_generator_carbon_monoxide_safety_scope_is_explicit():
    records = _records()
    scope = next(record for record in records if record["record_type"] == "scope")
    assert scope["content"]["scope_content"]["domain"] == "безопасность при аварийном электроснабжении"
