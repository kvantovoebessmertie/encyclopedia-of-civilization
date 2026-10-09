from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"demography-basics"/"records"
def test_demography_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==12
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert "SRC-DEMOGRAPHY_BASICS-WPP-METHODOLOGY-2024" in sources
    assert any(r["record_id"]=="EU-DEMOGRAPHY_BASICS-B-WPP-METHOD" and r["content"]["claim_ref"]["record_id"]=="CLM-DEMOGRAPHY_BASICS-B" and r["content"]["source_ref"]["record_id"]=="SRC-DEMOGRAPHY_BASICS-WPP-METHODOLOGY-2024" for r in records)
    assert any(r["record_id"]=="EU-DEMOGRAPHY_BASICS-C-WPP-METHOD" and r["content"]["claim_ref"]["record_id"]=="CLM-DEMOGRAPHY_BASICS-C" and r["content"]["source_ref"]["record_id"]=="SRC-DEMOGRAPHY_BASICS-WPP-METHODOLOGY-2024" for r in records)
    assert len(sources)==2
    for claim in [r for r in records if r["record_type"]=="claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"]=="evidence_use")
