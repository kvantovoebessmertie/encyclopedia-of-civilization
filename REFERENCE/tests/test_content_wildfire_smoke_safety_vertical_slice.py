from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "wildfire-smoke-safety" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"

def _records() -> list[dict]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(CONTENT.glob("*.json"))]

def test_wildfire_smoke_safety_records_validate():
    records = _records()
    assert len(records) == 12
    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []

def test_wildfire_smoke_safety_claims_have_direct_evidence():
    records = _records()
    claims = {r["record_id"] for r in records if r["record_type"] == "claim"}
    evidence_claims = {r["content"]["claim_ref"]["record_id"] for r in records if r["record_type"] == "evidence_use"}
    assert claims == evidence_claims

def test_wildfire_smoke_safety_scope_is_explicit():
    scope = next(r for r in _records() if r["record_type"] == "scope")
    assert scope["content"]["scope_content"]["domain"] == "безопасность при задымлении"
