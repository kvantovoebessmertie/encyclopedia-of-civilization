import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator
ROOT=Path(__file__).resolve().parents[2]
CONTENT=ROOT/"CONTENT"/"vertical-slices"/"home-fire-smoke-safety"/"records"
SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]
def test_home_fire_smoke_safety_records_validate():
    records=_records()
    assert len(records)==12
    validator=Validator(SCHEMA)
    for record in records:
        result=validator.validate(record)
        assert result.passed,(record["record_id"],[(f.code,f.message) for f in result.findings])
    assert validate_semantic_dataset(records)==[]
def test_home_fire_claims_have_direct_evidence():
    records=_records()
    claims={r["record_id"] for r in records if r["record_type"]=="claim"}
    evidence={r["content"]["claim_ref"]["record_id"] for r in records if r["record_type"]=="evidence_use"}
    assert claims==evidence
def test_home_fire_scope_is_explicit():
    scope=next(r for r in _records() if r["record_type"]=="scope")
    assert scope["content"]["scope_content"]["domain"]=="базовая противопожарная безопасность и эвакуация"
def test_home_fire_contains_immediate_escape_boundary():
    ids={r["record_id"] for r in _records()}
    assert "CLM-HOME-FIRE-LEAVE-STAY-OUT" in ids
