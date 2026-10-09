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

    readme = (ROOT / "CONTENT" / "vertical-slices" / "accessibility-basics" / "README.md").read_text(encoding="utf-8")
    assert "Доступность означает" in readme
    assert "иллюстративный пример" in readme
    assert "не сертифицирует конкретное здание" in readme
    assert "применимые требования" in readme
    for suffix in ("A", "B", "C"):
        assert f"records/CLM-ACCESSIBILITY_BASICS-{suffix}.json" in readme
        assert f"records/EU-ACCESSIBILITY_BASICS-{suffix}.json" in readme
    assert "records/SRC-ACCESSIBILITY_BASICS.json" in readme
    descriptions = {r["record_id"]: r["content"]["material"]["description"] for r in evidence}
    assert len(set(descriptions.values())) == 3
    assert "наравне с другими" in descriptions["EU-ACCESSIBILITY_BASICS-A"]
    assert "Статья 9" in descriptions["EU-ACCESSIBILITY_BASICS-B"]
    assert "не сертифицирует конкретный местный проект" in descriptions["EU-ACCESSIBILITY_BASICS-C"]
