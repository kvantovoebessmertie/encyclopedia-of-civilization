from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"materials-basics"/"records"
def test_materials_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==12
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==2
    for claim in [r for r in records if r["record_type"]=="claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"]=="evidence_use")
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert any(e["content"]["claim_ref"]["record_id"]=="CLM-MATERIALS_BASICS-A" and e["content"]["source_ref"]["record_id"]=="SRC-NIST-MATERIALS-SCIENCE-ENGINEERING-DIVISION" for e in evidence)
    mechanical=next(e for e in evidence if e["record_id"]=="EU-MATERIALS_BASICS-C-NIST-MECHANICAL-PERFORMANCE")
    canonical_source_path=ROOT/"CONTENT"/"vertical-slices"/"materials-science-basics"/"records"/"SRC-NIST-MECHANICAL-PERFORMANCE.json"
    canonical_source=json.loads(canonical_source_path.read_text(encoding="utf-8"))
    assert mechanical["record_version"]=="2"
    assert mechanical["content"]["claim_ref"]=={"record_id":"CLM-MATERIALS_BASICS-C","version":"1"}
    assert mechanical["content"]["source_ref"]=={"record_id":"SRC-NIST-MECHANICAL-PERFORMANCE","version":"1"}
    assert mechanical["provenance"]["created_from"]==[{"record_id":"SRC-NIST-MECHANICAL-PERFORMANCE","version":"1"}]
    assert canonical_source["record_type"]=="source"
    assert canonical_source["content"]["external_ref"]["uri"]=="https://www.nist.gov/mml/materials-science-and-engineering-division/mechanical-performance-group"
