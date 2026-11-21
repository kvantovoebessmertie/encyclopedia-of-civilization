from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"risk-management-basics"/"records"
def test_risk_management_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==12
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==3
    for claim in [r for r in records if r["record_type"]=="claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"]=="evidence_use")


def test_risk_management_claim_b_uses_limited_rights_compatible_gao_source():
    source=json.loads((SLICE/"SRC-GAO-GREEN-BOOK-2025.json").read_text(encoding="utf-8"))
    evidence=json.loads((SLICE/"EU-RISK_MANAGEMENT_BASICS-B.json").read_text(encoding="utf-8"))
    claim=json.loads((SLICE/"CLM-RISK_MANAGEMENT_BASICS-B.json").read_text(encoding="utf-8"))
    assert source["record_version"]=="1"
    assert source["content"]["external_ref"]["uri"]=="https://www.gao.gov/assets/gao-25-107721.pdf"
    assert evidence["record_version"]=="3"
    assert evidence["content"]["claim_ref"]=={"record_id":claim["record_id"],"version":"1"}
    assert evidence["content"]["source_ref"]=={"record_id":"SRC-GAO-GREEN-BOOK-2025","version":"1"}
    assert evidence["provenance"]["created_from"]==[{"record_id":"SRC-GAO-GREEN-BOOK-2025","version":"1"}]
    assert evidence["content"]["evidence_role"]=="supports"
    description=evidence["content"]["material"]["description"].casefold()
    assert "paragraph 7.02" in description
    assert "adverse-event" in description
    assert "does not establish the broader positive-and-negative uncertainty framing" in description
