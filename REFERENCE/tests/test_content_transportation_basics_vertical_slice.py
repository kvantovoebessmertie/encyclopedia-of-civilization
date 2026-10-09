from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "transportation-basics" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def test_transportation_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 15
    types = [r["record_type"] for r in records]
    assert types.count("source") == 2
    assert types.count("claim") == 4
    assert types.count("evidence_use") == 7
    assert types.count("context") == 1
    assert types.count("scope") == 1

    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(sources) == 2
    by_claim = {}
    for item in evidence:
        claim_id = item["content"]["claim_ref"]["record_id"]
        source_id = item["content"]["source_ref"]["record_id"]
        assert source_id in sources
        by_claim.setdefault(claim_id, set()).add(source_id)
    assert set(by_claim) == set(claims)
    assert all(sources <= by_claim[claim_id] for claim_id in ["CLM-TRANSPORTATION_BASICS-A", "CLM-TRANSPORTATION_BASICS-B", "CLM-TRANSPORTATION_BASICS-C"])
    assert by_claim["CLM-M5-TRANSPORT-RESILIENCE-D"] == {"SRC-M5-WORLD-BANK-TRANSPORT"}

    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []
