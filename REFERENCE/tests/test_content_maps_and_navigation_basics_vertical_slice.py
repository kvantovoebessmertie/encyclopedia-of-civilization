from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"maps-and-navigation-basics"/"records"
def test_maps_and_navigation_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==13
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(sources)==3 and len(claims)==3 and len(evidence)==5
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)
    map_c=[e for e in evidence if e["content"]["claim_ref"]["record_id"]=="CLM-MAPS_AND_NAVIGATION_BASICS-C"]
    assert {e["content"]["source_ref"]["record_id"] for e in map_c} >= {
        "SRC-USGS-US-TOPO-ACCURACY","SRC-USGS-US-TOPO-CURRENCY"
    }
    accuracy=next(e for e in map_c if e["content"]["source_ref"]["record_id"]=="SRC-USGS-US-TOPO-ACCURACY")
    currency=next(e for e in map_c if e["content"]["source_ref"]["record_id"]=="SRC-USGS-US-TOPO-CURRENCY")
    assert "not authoritative or official for navigation" in accuracy["content"]["material"]["description"]
    assert "not a global rule" in currency["content"]["material"]["description"]
