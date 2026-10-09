from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "sanitation-basics"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((SLICE / "records").glob("*.json"))]


def test_vertical_slice_has_m5_matured_shape():
    records = _records()
    assert len(records) == 14
    types = [x["record_type"] for x in records]
    assert types.count("source") == 3
    assert types.count("claim") == 4
    assert types.count("evidence_use") == 5
    assert types.count("context") == 1
    assert types.count("scope") == 1
    assert len({x["record_id"] for x in records}) == 14


def test_vertical_slice_is_schema_and_semantically_clean():
    records = _records()
    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []


def test_vertical_slice_claims_have_provenance_and_evidence_paths():
    records = _records()
    by_id = {x["record_id"]: x for x in records}
    evidence = [x for x in records if x["record_type"] == "evidence_use"]
    claims = [x for x in records if x["record_type"] == "claim"]
    assert len(claims) == 4
    assert len(evidence) == 5
    for claim in claims:
        assert claim.get("provenance", {}).get("created_from")
        links = [e for e in evidence if e.get("content", {}).get("claim_ref", {}).get("record_id") == claim["record_id"]]
        assert links
        for item in links:
            assert by_id[item["content"]["source_ref"]["record_id"]]["record_type"] == "source"
