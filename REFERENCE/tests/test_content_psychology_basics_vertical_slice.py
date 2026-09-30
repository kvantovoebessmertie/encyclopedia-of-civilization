import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/psychology-basics")
def test_content_psychology_basics_vertical_slice():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    assert len(records)==9
    types=[r["record_type"] for r in records]
    assert types.count("source")==1
    assert types.count("claim")==3
    assert types.count("evidence_use")==3
    assert types.count("context")==1
    assert types.count("scope")==1
    source=next(r for r in records if r["record_type"]=="source")["record_id"]
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert all(r["provenance"]["created_from"][0]["record_id"]==source for r in claims)
    assert all(r["content"]["source_ref"]["record_id"]==source for r in evidence)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}
