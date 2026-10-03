from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"settlement-geography-basics"/"records"
def test_settlement_geography_basics_vertical_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(SLICE.glob("*.json"))]
    assert len(records)==9
    types=[r["record_type"] for r in records]
    assert types.count("source")==1 and types.count("claim")==3 and types.count("evidence_use")==3
    assert types.count("context")==1 and types.count("scope")==1
    source=next(r for r in records if r["record_type"]=="source")["record_id"]
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert all(r["provenance"]["created_from"][0]["record_id"]==source for r in claims)
    assert {e["content"]["claim_ref"]["record_id"] for e in evidence}=={c["record_id"] for c in claims}
    assert all(e["content"]["source_ref"]["record_id"]==source for e in evidence)
