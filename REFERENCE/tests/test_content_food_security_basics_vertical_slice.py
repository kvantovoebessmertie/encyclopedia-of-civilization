from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT / "CONTENT" / "vertical-slices" / "food-security-basics" / "records"
def test_food_security_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==12
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==2
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(claims)==4 and len(evidence)==4
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)


def test_food_security_fao_evidence_use_is_pinned_to_section_1_4():
    records = {r["record_id"]: r for r in
               (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    evidence = records["EU-FOOD_SECURITY_BASICS-A"]
    assert evidence["record_version"] == "2"
    assert evidence["content"]["claim_ref"] == {
        "record_id": "CLM-FOOD_SECURITY_BASICS-A", "version": "1"
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": "SRC-FOOD_SECURITY_BASICS", "version": "1"
    }
    assert evidence["provenance"]["created_from"] == [
        {"record_id": "SRC-FOOD_SECURITY_BASICS", "version": "1"}
    ]
    assert evidence["content"]["material"]["locator"] == (
        "FAO, Food Security Information and Early Warning System Handbook, "
        "§1.4 “Definition of Food Security”."
    )
    description = evidence["content"]["material"]["description"]
    assert "physical and economic access" in description
    assert "availability, stability, access and biological utilization" in description
    assert "does not establish individual dietary or medical advice" in description
