from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "astronomy-basics" / "records"
def test_astronomy_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 1
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"] == "evidence_use")

def test_astronomy_a_and_c_have_claim_specific_nasa_pinpoints():
    records = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    expected = {
        "EU-ASTRONOMY_BASICS-A": ("CLM-ASTRONOMY_BASICS-A", "Knowledge of the Solar System", "Mass"),
        "EU-ASTRONOMY_BASICS-C": ("CLM-ASTRONOMY_BASICS-C", "Distances Within the Solar System", "Light Time"),
    }
    for eu_id, (claim_id, marker_a, marker_b) in expected.items():
        eu = records[eu_id]
        assert eu["record_version"] == "2"
        assert eu["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert eu["content"]["source_ref"] == {"record_id": "SRC-ASTRONOMY_BASICS", "version": "1"}
        description = eu["content"]["material"]["description"]
        assert marker_a in description
        assert marker_b in description
        assert "science.nasa.gov/learn/basics-of-space-flight/chapter1-1/" in description
    assert records["CLM-ASTRONOMY_BASICS-A"]["content"]["statement"] == "Солнечная система включает Солнце и множество объектов, движущихся под его гравитационным влиянием."
    assert records["CLM-ASTRONOMY_BASICS-C"]["content"]["statement"] == "Астрономические расстояния часто выражаются через астрономическую единицу и световой год, соответствующие разным масштабам космических систем."
    assert records["CLM-ASTRONOMY_BASICS-B"]["record_version"] == "1"
    assert records["EU-ASTRONOMY_BASICS-B"]["record_version"] == "1"
