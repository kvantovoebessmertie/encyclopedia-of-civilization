from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "food-safety-basics" / "records"

def test_food_safety_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) >= 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) >= 1
    claims = [r for r in records if r["record_type"] == "claim"]
    assert len(claims) >= 3
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(evidence) >= 3
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)

def test_food_safety_basics_cdc_evidence_is_explicitly_separate():
    evidence = json.loads((SLICE / "EU-FOOD_SAFETY_CDC-A.json").read_text(encoding="utf-8"))
    assert evidence["content"]["claim_ref"]["record_id"] == "CLM_FOOD_SAFETY_CDC_A"
    assert evidence["content"]["source_ref"]["record_id"] == "SRC_FOOD_SAFETY_CDC"
    assert "not represented as independent corroboration" in evidence["content"]["material"]["description"]

def test_food_safety_basics_fda_baseline_stays_on_fda_evidence():
    evidence = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json") if p.name.startswith("EU-")]
    baseline = {"CLM-FOOD_SAFETY_BASICS-A", "CLM-FOOD_SAFETY_BASICS-B", "CLM-FOOD_SAFETY_BASICS-C"}
    for claim_ref in baseline:
        matching = [e for e in evidence if e["content"]["claim_ref"]["record_id"] == claim_ref]
        assert matching
        assert all(e["content"]["source_ref"]["record_id"] == "SRC-FOOD_SAFETY_BASICS" for e in matching)
