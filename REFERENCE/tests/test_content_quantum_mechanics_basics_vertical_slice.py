from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT / "CONTENT" / "vertical-slices" / "quantum-mechanics-basics" / "records"
def test_quantum_mechanics_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==9
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(sources)==1 and len(claims)==3 and len(evidence)==3
    assert all(r["provenance"]["created_from"][0]["record_id"] in sources for r in claims)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)
