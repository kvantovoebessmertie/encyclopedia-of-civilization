from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "cross-slice-linkage"
EXPECTED_CONTEXT = "CTX-CROSS-SLICE-LINKAGE"

def records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("records/*.json")]

def test_cross_slice_relation_set_is_complete():
    rs = records()
    relations = [r for r in rs if r["record_type"] == "relation"]
    contexts = [r for r in rs if r["record_type"] == "context"]
    assert relations
    assert {r["record_id"] for r in contexts} == {EXPECTED_CONTEXT}
    assert all(len(r["content"]["participants"]) >= 2 for r in relations)
    assert all(r["content"]["direction"] in {"directed", "undirected", "unknown"} for r in relations)
    participant_ids = {ref["record_id"] for r in relations for ref in r["content"]["participants"]}
    relation_ids = {r["record_id"] for r in relations}
    assert not (participant_ids & relation_ids)

def test_cross_slice_audit_artifact_matches_current_corpus():
    audit = json.loads((ROOT / "RELEASE" / "CONTENT-CROSS-SLICE-AUDIT.json").read_text(encoding="utf-8"))
    assert audit["corpus"] == {"vertical_slices": 27, "records": 202}
    assert len(audit["findings"]) == 6
    assert audit["conclusion"]["critical_contradictions"] == 0
    assert audit["conclusion"]["exact_duplicate_clusters"] == 0
    assert audit["conclusion"]["cross_slice_context"] == EXPECTED_CONTEXT

def test_cross_slice_relations_resolve_to_explicit_context():
    rs = records()
    by_id = {r["record_id"]: r for r in rs}
    context = by_id[EXPECTED_CONTEXT]
    target = context["content"]["target_ref"]["record_id"]
    relation_ids = {r["record_id"] for r in rs if r["record_type"] == "relation"}
    assert target in relation_ids
    for relation_id in relation_ids:
        relation = by_id[relation_id]
        assert relation["content"].get("frame_ref") == {"record_id": EXPECTED_CONTEXT, "version": "1"}
