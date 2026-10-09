from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "ergonomics-basics" / "records"
def test_ergonomics_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 1
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"] == "evidence_use")

def test_ergonomics_claim_and_evidence_limits_are_explanatory():
    by_id = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    claim_c = by_id["CLM-ERGONOMICS_BASICS-C"]["content"]["statement"]
    assert "выявление, анализ и контроль" in claim_c
    descriptions = [by_id[f"EU-ERGONOMICS_BASICS-{letter}"]["content"]["material"]["description"] for letter in "ABC"]
    assert len(set(descriptions)) == 3
    assert "возможностей работников" in descriptions[0]
    assert "повторяемость" in descriptions[1]
    assert "выявление, анализ и контроль" in descriptions[2]
    assert "не задаёт универсальную меру контроля" in descriptions[2]
    readme = (SLICE.parent / "README.md").read_text(encoding="utf-8")
    assert "Пример:" in readme
    assert "не является индивидуальной медицинской оценкой" in readme
