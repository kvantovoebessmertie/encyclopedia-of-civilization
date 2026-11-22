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

    assert len(records) == 14
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

def test_generator_refuelling_has_direct_cpsc_source():
    records = _records()
    by_id = {r["record_id"]: r for r in records}
    source = by_id["SRC-CPSC-WINTER-SAFETY-2026"]
    evidence = by_id["EU-GENERATOR-REFUEL-COOL-CPSC-2026"]
    assert source["content"]["external_ref"]["uri"] == "https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters"
    assert source["content"]["external_ref"]["locator"] == "Generators; Use Flashlights Instead of Candles"
    assert evidence["content"]["claim_ref"] == {"record_id": "CLM-GENERATOR-REFUEL-COOL", "version": "1"}
    assert evidence["content"]["source_ref"] == {"record_id": "SRC-CPSC-WINTER-SAFETY-2026", "version": "1"}
    assert "Generators" in evidence["content"]["material"]["description"]
