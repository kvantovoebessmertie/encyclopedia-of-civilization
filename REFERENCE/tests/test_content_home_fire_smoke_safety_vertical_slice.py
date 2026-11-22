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
    assert len(records)==16
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

def test_home_fire_escape_claims_have_direct_dedicated_sources():
    records = _records()
    by_id = {r["record_id"]: r for r in records}
    usfa = by_id["SRC-USFA-HOME-FIRE-ESCAPE-PLANS-2026"]
    usfa_eu = by_id["EU-HOME-FIRE-ESCAPE-PLAN-USFA-DIRECT-2026"]
    nfpa = by_id["SRC-NFPA-ESCAPE-PLANNING-2026"]
    nfpa_eu = by_id["EU-HOME-FIRE-TWO-WAYS-NFPA-ESCAPE-2026"]
    assert usfa["content"]["external_ref"]["uri"] == "https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/"
    assert usfa["content"]["external_ref"]["locator"] == "Making and practicing your fire escape plan"
    assert usfa_eu["content"]["claim_ref"] == {"record_id": "CLM-HOME-FIRE-ESCAPE-PLAN", "version": "1"}
    assert usfa_eu["content"]["source_ref"] == {"record_id": "SRC-USFA-HOME-FIRE-ESCAPE-PLANS-2026", "version": "1"}
    assert nfpa["content"]["external_ref"]["uri"] == "https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning"
    assert nfpa_eu["content"]["claim_ref"] == {"record_id": "CLM-HOME-FIRE-TWO-WAYS-NFPA", "version": "1"}
    assert nfpa_eu["content"]["source_ref"] == {"record_id": "SRC-NFPA-ESCAPE-PLANNING-2026", "version": "1"}
