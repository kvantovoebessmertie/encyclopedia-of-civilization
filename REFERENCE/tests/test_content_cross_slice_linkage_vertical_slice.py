from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "cross-slice-linkage"


def records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("records/*.json")]


def test_cross_slice_relation_set_is_complete():
    rs = records()
    relations = [r for r in rs if r["record_type"] == "relation"]
    by_identity = {(r["record_id"], str(r["record_version"])): r for r in rs}
    contexts = [r for r in rs if r["record_type"] == "context"]
    assert relations
    assert len(contexts) == len(relations)
    assert all(len(r["content"]["participants"]) >= 2 for r in relations)
    assert all(r["content"]["direction"] in {"directed", "undirected", "unknown"} for r in relations)
    relation_ids = {r["record_id"] for r in relations}
    participant_ids = {ref["record_id"] for r in relations for ref in r["content"]["participants"]}
    assert not (participant_ids & relation_ids)
    for relation in relations:
        frame = relation["content"]["frame_ref"]
        context = by_identity[(frame["record_id"], str(frame["version"]))]
        assert context["record_type"] == "context"
        assert context["content"]["target_ref"] == {
            "record_id": relation["record_id"],
            "version": str(relation["record_version"]),
        }


def test_cross_slice_audit_artifact_matches_current_corpus():
    audit = json.loads((ROOT / "RELEASE" / "CONTENT-CROSS-SLICE-AUDIT.json").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "RELEASE" / "CONTENT-COVERAGE.json").read_text(encoding="utf-8"))
    relations = [r for r in records() if r["record_type"] == "relation"]
    assert audit["corpus"]["vertical_slices"] == manifest["vertical_slices"]
    assert audit["corpus"]["records"] == manifest["total_records"]
    assert audit["corpus"]["relation_records_in_cross_slice_linkage"] == len(relations)
    assert audit["conclusion"]["blocking_findings"] == 0
    assert audit["conclusion"]["critical_contradictions"] == 0
    assert audit["conclusion"]["exact_duplicate_clusters"] == 0
    assert audit["conclusion"]["status"] == "CURRENT LINKAGE BASELINE VALID"


def test_cross_slice_relations_resolve_to_explicit_context():
    rs = records()
    by_identity = {(r["record_id"], str(r["record_version"])): r for r in rs}
    relation_ids = {r["record_id"] for r in rs if r["record_type"] == "relation"}
    for relation_id in relation_ids:
        relation = next(r for r in rs if r["record_id"] == relation_id and r["record_type"] == "relation")
        frame = relation["content"]["frame_ref"]
        context = by_identity[(frame["record_id"], str(frame["version"]))]
        assert context["record_type"] == "context"
        assert context["content"]["target_ref"] == {
            "record_id": relation_id,
            "version": str(relation["record_version"]),
        }
