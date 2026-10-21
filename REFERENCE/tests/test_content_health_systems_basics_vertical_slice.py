from __future__ import annotations

import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "health-systems-basics"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"

def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((SLICE / "records").glob("*.json"))]

def test_vertical_slice_has_canonical_thirteen_record_shape():
    records = _records()
    assert len(records) == 13
    assert {r["record_type"] for r in records} == {"source", "claim", "evidence_use", "context", "scope"}
    assert len({r["record_id"] for r in records}) == 13

def test_vertical_slice_is_schema_and_semantically_clean():
    records = _records()
    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []

def test_vertical_slice_claims_have_provenance_and_evidence_paths():
    records = _records()
    by_id = {r["record_id"]: r for r in records}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    claims = [r for r in records if r["record_type"] == "claim"]
    assert len(claims) == 4
    assert len(evidence) == 5
    for claim in claims:
        assert claim.get("provenance", {}).get("created_from")
        links = [e for e in evidence if e.get("content", {}).get("claim_ref", {}).get("record_id") == claim["record_id"]]
        assert links
        for link in links:
            source_id = link["content"]["source_ref"]["record_id"]
            assert by_id[source_id]["record_type"] == "source"


def test_health_resilience_evidence_use_targets_the_resilience_claim():
    records = _records()
    by_id = {r["record_id"]: r for r in records}
    evidence = by_id["EU-M4-HEALTH-RESILIENCE-WHO"]
    assert evidence["record_version"] == "2"
    assert evidence["content"]["claim_ref"] == {
        "record_id": "CLM-M4-HEALTH-RESILIENCE-A",
        "version": "1",
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": "SRC-M4-HEALTH-RESILIENCE-WHO",
        "version": "1",
    }
    assert by_id[evidence["content"]["claim_ref"]["record_id"]]["record_type"] == "claim"
    assert by_id[evidence["content"]["source_ref"]["record_id"]]["record_type"] == "source"
