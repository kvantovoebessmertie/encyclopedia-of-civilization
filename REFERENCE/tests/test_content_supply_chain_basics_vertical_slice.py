from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "supply-chain-basics" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def test_supply_chain_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 16
    types = [r["record_type"] for r in records]
    assert set(types) == {"source", "claim", "evidence_use", "context", "scope"}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(sources) == 3 and len(claims) == 4 and len(evidence) == 7

    by_id = {r["record_id"]: r for r in records}
    by_claim = {}
    for link in evidence:
        claim_id = link["content"]["claim_ref"]["record_id"]
        source_id = link["content"]["source_ref"]["record_id"]
        assert by_id[source_id]["record_type"] == "source"
        by_claim.setdefault(claim_id, set()).add(source_id)

    nist = "SRC-SUPPLY_CHAIN_BASICS"
    cisa = "SRC-M5-CISA-ICT-SUPPLY-CHAIN"
    oecd = "SRC-M5-OECD-SUPPLY-CHAIN-VISIBILITY"
    assert by_claim["CLM-SUPPLY_CHAIN_BASICS-A"] == {nist, cisa}
    assert by_claim["CLM-SUPPLY_CHAIN_BASICS-B"] == {nist, cisa}
    assert by_claim["CLM-SUPPLY_CHAIN_BASICS-C"] == {nist, cisa}
    assert by_claim["CLM-M5-SUPPLY-CHAIN-VISIBILITY-D"] == {oecd}

    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []
