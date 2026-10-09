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
    assert len(records) == 12
    types = [r["record_type"] for r in records]
    assert set(types) == {"source", "claim", "evidence_use", "context", "scope"}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(sources) == 2 and len(claims) == 4 and len(evidence) == 4

    by_id = {r["record_id"]: r for r in records}
    for claim in claims:
        source_id = claim["provenance"]["created_from"][0]["record_id"]
        assert source_id in sources
        links = [e for e in evidence if e["content"]["claim_ref"]["record_id"] == claim["record_id"]]
        assert len(links) == 1
        assert links[0]["content"]["source_ref"]["record_id"] == source_id
        assert by_id[links[0]["content"]["source_ref"]["record_id"]]["record_type"] == "source"

    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []
