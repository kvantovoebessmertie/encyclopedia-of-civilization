from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"learning-basics"/"records"
def test_learning_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==9
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==1
    for claim in [r for r in records if r["record_type"]=="claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"]=="evidence_use")


def test_learning_basics_nimh_evidence_is_pinned_to_program_scope():
    records = {r["record_id"]: r for r in
               (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    evidence = records["EU-LEARNING_BASICS-A"]
    assert evidence["record_version"] == "2"
    assert evidence["content"]["claim_ref"] == {
        "record_id": "CLM-LEARNING_BASICS-A", "version": "1"
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": "SRC-LEARNING_BASICS", "version": "1"
    }
    assert evidence["provenance"]["created_from"] == [
        {"record_id": "SRC-LEARNING_BASICS", "version": "1"}
    ]
    assert evidence["content"]["material"]["locator"] == (
        "NIMH, Learning and Memory Program, program-overview passage listing "
        "encoding, consolidation, retrieval and working memory among the cognitive processes studied."
    )
    description = evidence["content"]["material"]["description"]
    assert "encoding, consolidation, retrieval and working memory" in description
    assert "not an exhaustive taxonomy or universal theory of learning" in description
