from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "cross-slice-linkage"
EXPECTED_RELATIONS = {
    "REL-CROSS-WATER-CHEMICAL",
    "REL-CROSS-WATER-FILTER",
        "REL-CROSS-EARTHQUAKE-AFTERSHOCK",
    "REL-CROSS-SANITATION-HYGIENE",
    "REL-CROSS-FLOOD-SAFETY",
    "REL-CROSS-CO-PREVENTION",
}
EXPECTED_CONTEXT = "CTX-CROSS-SLICE-LINKAGE"

def test_cross_slice_relation_set_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("records/*.json")]
    assert {r["record_id"] for r in records if r["record_type"] == "relation"} == EXPECTED_RELATIONS
    assert {r["record_id"] for r in records if r["record_type"] == "context"} == {EXPECTED_CONTEXT}
    assert sum(r["record_type"] == "relation" for r in records) == 5
    relations = [r for r in records if r["record_type"] == "relation"]
    assert all(len(r["content"]["participants"]) >= 2 for r in relations)
    assert all(r["content"]["direction"] in {"directed", "undirected", "unknown"} for r in relations)
    participant_ids = {ref["record_id"] for r in relations for ref in r["content"]["participants"]}
    assert all(not pid.startswith("REL-CROSS-") for pid in participant_ids)


def test_cross_slice_audit_artifact_matches_current_corpus():
    audit = json.loads((ROOT / "RELEASE" / "CONTENT-CROSS-SLICE-AUDIT.json").read_text(encoding="utf-8"))
    assert audit["corpus"] == {"vertical_slices": 24, "records": 181}
    assert len(audit["findings"]) == 6
    assert audit["conclusion"]["critical_contradictions"] == 0
    assert audit["conclusion"]["exact_duplicate_clusters"] == 0
    assert audit["conclusion"]["cross_slice_context"] == EXPECTED_CONTEXT


def test_cross_slice_relations_resolve_to_explicit_context():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("records/*.json")]
    by_id = {r["record_id"]: r for r in records}
    context = by_id[EXPECTED_CONTEXT]
    target = context["content"]["target_ref"]["record_id"]
    assert target in EXPECTED_RELATIONS
    assert by_id[target]["record_type"] == "relation"
    for relation_id in EXPECTED_RELATIONS:
        relation = by_id[relation_id]
        frame = relation["content"].get("frame_ref")
        assert frame == {"record_id": EXPECTED_CONTEXT, "version": "1"}
