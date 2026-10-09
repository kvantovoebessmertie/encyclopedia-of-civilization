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

    by_id = {r["record_id"]: r for r in records}
    claim_c = by_id["CLM-ERGONOMICS_BASICS-C"]["content"]["statement"]
    assert "выявления, анализа и контроля факторов риска" in claim_c
    assert "оценку их эффективности" not in claim_c
    descriptions = {r["record_id"]: r["content"]["material"]["description"] for r in records if r["record_type"] == "evidence_use"}
    assert len(set(descriptions.values())) == 3
    assert "возможностей работников" in descriptions["EU-ERGONOMICS_BASICS-A"]
    assert "повторяемые движения" in descriptions["EU-ERGONOMICS_BASICS-B"]
    assert "выявления, анализа и контроля" in descriptions["EU-ERGONOMICS_BASICS-C"]
    readme = (ROOT / "CONTENT" / "vertical-slices" / "ergonomics-basics" / "README.md").read_text(encoding="utf-8")
    assert "Эргономика рассматривает" in readme
    assert "иллюстрация подхода" in readme
    assert "не заменяет индивидуальную медицинскую оценку" in readme
    for suffix in ("A", "B", "C"):
        assert f"records/CLM-ERGONOMICS_BASICS-{suffix}.json" in readme
        assert f"records/EU-ERGONOMICS_BASICS-{suffix}.json" in readme
    assert "records/SRC-ERGONOMICS_BASICS.json" in readme
