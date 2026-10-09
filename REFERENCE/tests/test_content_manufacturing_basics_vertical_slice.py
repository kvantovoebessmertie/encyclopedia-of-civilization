from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "manufacturing-basics" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def test_manufacturing_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 15
    types = [r["record_type"] for r in records]
    assert types.count("source") == 2
    assert types.count("claim") == 4
    assert types.count("evidence_use") == 7
    assert types.count("context") == 1
    assert types.count("scope") == 1
    assert len({r["record_id"] for r in records}) == 15

    by_id = {r["record_id"]: r for r in records}
    sources = {"SRC-MANUFACTURING_BASICS", "SRC-M5-UNIDO-SMART-MANUFACTURING"}
    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    by_claim = {}
    for item in evidence:
        claim_id = item["content"]["claim_ref"]["record_id"]
        source_id = item["content"]["source_ref"]["record_id"]
        assert by_id[source_id]["record_type"] == "source"
        by_claim.setdefault(claim_id, set()).add(source_id)

    assert set(by_claim) == set(claims)
    assert by_claim["CLM-MANUFACTURING_BASICS-A"] == sources
    assert by_claim["CLM-MANUFACTURING_BASICS-B"] == sources
    assert by_claim["CLM-MANUFACTURING_BASICS-C"] == sources
    assert by_claim["CLM-M5-MANUFACTURING-FUNCTIONS-D"] == {"SRC-M5-UNIDO-SMART-MANUFACTURING"}

    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []
