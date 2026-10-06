from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"disaster-behavioral-health-basics"/"records"
def test_disaster_behavioral_health_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==12
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]; evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(sources)==2 and len(claims)==4 and len(evidence)==4
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)
    assert any(e["content"]["source_ref"]["record_id"]=="SRC-WHO-MENTAL-HEALTH-EMERGENCIES-2025" for e in evidence)