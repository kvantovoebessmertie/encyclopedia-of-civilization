from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "water-treatment-basics" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def test_water_treatment_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    types = [r["record_type"] for r in records]
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]

    assert len(records) == 17
    assert types.count("source") == 3
    assert types.count("claim") == 4
    assert types.count("evidence_use") == 8
    assert types.count("context") == 1
    assert types.count("scope") == 1
    assert len({r["record_id"] for r in records}) == 17

    by_id = {r["record_id"]: r for r in records}
    by_claim = {}
    for link in evidence:
        claim_id = link["content"]["claim_ref"]["record_id"]
        source_id = link["content"]["source_ref"]["record_id"]
        assert by_id[source_id]["record_type"] == "source"
        by_claim.setdefault(claim_id, set()).add(source_id)

    assert set(by_claim) == set(claims)
    assert by_claim["CLM-WATER_TREATMENT_BASICS-A"] == {"SRC-WATER_TREATMENT_BASICS", "SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES"}
    assert by_claim["CLM-WATER_TREATMENT_BASICS-B"] == {"SRC-WATER_TREATMENT_BASICS", "SRC-EPA-WATER-TREATMENT-2026", "SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES"}
    assert by_claim["CLM-WATER_TREATMENT_BASICS-C"] == {"SRC-WATER_TREATMENT_BASICS", "SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES"}
    assert by_claim["CLM-M5-WATER-EMERGENCY-DISINFECTION-D"] == {"SRC-EPA-WATER-TREATMENT-2026"}

    emergency = claims["CLM-M5-WATER-EMERGENCY-DISINFECTION-D"]
    assert emergency["provenance"]["created_from"][0]["record_id"] == "SRC-EPA-WATER-TREATMENT-2026"

    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(records) == []
