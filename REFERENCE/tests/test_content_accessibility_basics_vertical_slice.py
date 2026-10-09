from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT / "CONTENT" / "vertical-slices" / "accessibility-basics" / "records"
def test_accessibility_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==9
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==1
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(claims)==3 and len(evidence)==3
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)

def test_accessibility_claim_and_evidence_limits_are_explanatory():
    by_id = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    claim_c = by_id["CLM-ACCESSIBILITY_BASICS-C"]["content"]["statement"]
    assert "международную рамку доступности" in claim_c
    assert "применимым нормам" in claim_c
    descriptions = [by_id[f"EU-ACCESSIBILITY_BASICS-{letter}"]["content"]["material"]["description"] for letter in "ABC"]
    assert len(set(descriptions)) == 3
    assert "равное участие" in descriptions[0]
    assert "Статья 9" in descriptions[1]
    assert "минимальные стандарты" in descriptions[2]
    readme = (SLICE.parent / "README.md").read_text(encoding="utf-8")
    assert "Пример:" in readme
    assert "юридический тест" in readme
    assert "применимым нормам" in readme
