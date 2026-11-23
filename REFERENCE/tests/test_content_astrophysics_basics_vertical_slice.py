from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "astrophysics-basics" / "records"

def test_astrophysics_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 1
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"] == "evidence_use")

def test_astrophysics_a_and_b_have_claim_specific_nasa_stars_pinpoints():
    records = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    expected = {
        "EU-ASTROPHYSICS_BASICS-A": ("CLM-ASTROPHYSICS_BASICS-A", "opening definition"),
        "EU-ASTROPHYSICS_BASICS-B": ("CLM-ASTROPHYSICS_BASICS-B", "Life"),
    }
    for eu_id, (claim_id, marker) in expected.items():
        eu = records[eu_id]
        assert eu["record_version"] == "2"
        assert eu["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert eu["content"]["source_ref"] == {"record_id": "SRC-ASTROPHYSICS_BASICS", "version": "1"}
        description = eu["content"]["material"]["description"]
        assert marker in description
        assert "science.nasa.gov/universe/stars/" in description
    assert records["CLM-ASTROPHYSICS_BASICS-A"]["content"]["statement"] == "Звёзды представляют собой горячие газовые объекты, состоящие преимущественно из водорода и гелия с примесью других элементов."
    assert records["CLM-ASTROPHYSICS_BASICS-B"]["content"]["statement"] == "Звёзды проходят жизненные циклы, а их свойства изменяются по мере эволюции."
    assert records["CLM-ASTROPHYSICS_BASICS-C"]["record_version"] == "1"
    assert records["EU-ASTROPHYSICS_BASICS-C"]["record_version"] == "1"
