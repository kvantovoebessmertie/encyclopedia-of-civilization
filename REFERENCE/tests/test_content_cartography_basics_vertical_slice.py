from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"cartography-basics"/"records"
EXPECTED_SOURCES={"SRC-CARTOGRAPHY","SRC-CARTOGRAPHY-TOPO"}
def test_cartography_basics_vertical_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(SLICE.glob("*.json"))]
    types=[r["record_type"] for r in records]
    assert types.count("source")==2 and types.count("claim")==3 and types.count("evidence_use")==3
    assert types.count("context")==1 and types.count("scope")==1
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert sources==EXPECTED_SOURCES
    source="SRC-CARTOGRAPHY"
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    evidence_by_claim={e["content"]["claim_ref"]["record_id"]:e for e in evidence}
    assert set(evidence_by_claim)=={c["record_id"] for c in claims}
    assert all(e["content"]["source_ref"]["record_id"] in EXPECTED_SOURCES for e in evidence)
    assert all(evidence_by_claim[c["record_id"]]["content"]["source_ref"]["record_id"] in {p["record_id"] for p in c["provenance"]["created_from"]} for c in claims)
