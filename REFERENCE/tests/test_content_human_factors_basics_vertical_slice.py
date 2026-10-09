from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT / "CONTENT" / "vertical-slices" / "human-factors-basics" / "records"
def test_human_factors_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==9
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(sources)==1 and len(claims)==3 and len(evidence)==3
    assert all(r["provenance"]["created_from"][0]["record_id"] in sources for r in claims)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)

def test_human_factors_evidence_and_human_view_are_explanatory():
    by_id = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    descriptions = [by_id[f"EU-HUMAN_FACTORS_BASICS-{letter}"]["content"]["material"]["description"] for letter in "ABC"]
    assert len(set(descriptions)) == 3
    assert "взаимодействия человека и элементов системы" in descriptions[0]
    assert "человеческих возможностей и ограничений" in descriptions[1]
    assert "системный подход к проектированию" in descriptions[2]
    assert "не является универсальным отраслевым стандартом" in descriptions[2]
    readme = (SLICE.parent / "README.md").read_text(encoding="utf-8")
    assert "Пример:" in readme
    assert "не являются автоматически применимыми требованиями для всех отраслей" in readme
