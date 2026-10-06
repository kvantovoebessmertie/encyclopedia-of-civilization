from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT / "CONTENT" / "vertical-slices" / "disaster-response-basics" / "records"
def _records(): return [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
def test_disaster_response_basics_slice_is_complete():
    records=_records()
    assert len(records)==12
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources=[r for r in records if r["record_type"]=="source"]
    assert len(sources)==2
    urls=[r["content"].get("external_ref",{}).get("uri") for r in sources]
    assert len(urls)==len(set(urls))
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(claims)==4 and len(evidence)==4
    source_ids={r["record_id"] for r in sources}
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in source_ids
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in source_ids for e in evidence)
