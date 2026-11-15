from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"materials-basics"/"records"
def test_materials_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==13
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==3
    for claim in [r for r in records if r["record_type"]=="claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"]=="evidence_use")
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert any(e["content"]["claim_ref"]["record_id"]=="CLM-MATERIALS_BASICS-A" and e["content"]["source_ref"]["record_id"]=="SRC-NIST-MATERIALS-SCIENCE-ENGINEERING-DIVISION" for e in evidence)
    assert any(e["content"]["claim_ref"]["record_id"]=="CLM-MATERIALS_BASICS-C" and e["content"]["source_ref"]["record_id"]=="SRC-NIST-MECHANICAL-PERFORMANCE-GROUP" for e in evidence)
