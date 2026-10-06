import json
from pathlib import Path
SLICE=Path("CONTENT/vertical-slices/disaster-recovery-basics")
def test_content_disaster_recovery_basics_vertical_slice():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    assert len(records)==12
    types=[r["record_type"] for r in records]
    assert types.count("source")==2 and types.count("claim")==4 and types.count("evidence_use")==4 and types.count("context")==1 and types.count("scope")==1
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]; evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert all(r["provenance"]["created_from"][0]["record_id"] in sources for r in claims)
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}
    assert len({r["content"]["source_ref"]["record_id"] for r in evidence})==2
