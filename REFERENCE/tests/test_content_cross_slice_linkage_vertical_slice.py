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


def test_alert_cross_slice_relations_resolve_exact_red_cross_versions():
    rs = records()
    by_id = {r["record_id"]: r for r in rs}

    wildfire = by_id["REL-CROSS-ALERTS-WILDFIRE-SMOKE"]
    wildfire_context = by_id["CTX-REL-CROSS-ALERTS-WILDFIRE-SMOKE"]
    home_fire = by_id["REL-CROSS-HOME-FIRE-ALERTS"]
    home_fire_context = by_id["CTX-REL-CROSS-HOME-FIRE-ALERTS"]

    assert wildfire["record_version"] == "3"
    assert wildfire["provenance"]["created_from"] == [
        {"record_id": "SRC-RED-CROSS-ALERTS-2026", "version": "2"},
        {"record_id": "SRC-CDC-WILDFIRE-SMOKE-2026", "version": "1"},
    ]
    assert wildfire["content"]["participants"] == [
        {"record_id": "CLM-ALERTS-ENABLE-RESPOND", "version": "2"},
        {"record_id": "CLM-WILDFIRE-AIR-QUALITY", "version": "1"},
    ]
    assert wildfire["content"]["relation_type"] == "public_alerts_and_wildfire_smoke_response"
    assert wildfire["content"]["roles"] == ["linked_record", "linked_record"]
    assert wildfire["content"]["direction"] == "undirected"
    assert wildfire["content"]["frame_ref"] == {
        "record_id": "CTX-REL-CROSS-ALERTS-WILDFIRE-SMOKE", "version": "2"
    }

    assert wildfire_context["record_version"] == "2"
    assert wildfire_context["provenance"]["created_from"] == [
        {"record_id": "SRC-RED-CROSS-ALERTS-2026", "version": "2"},
        {"record_id": "SRC-CDC-WILDFIRE-SMOKE-2026", "version": "1"},
    ]
    assert wildfire_context["content"]["target_ref"] == {
        "record_id": "REL-CROSS-ALERTS-WILDFIRE-SMOKE", "version": "3"
    }
    assert wildfire_context["content"]["context_content"]["condition"] == (
        "связь между участниками фиксируется только в пределах явно указанного типа Relation "
        "и не заменяет исходные Claim, Scope или Evidence Use"
    )
    assert wildfire_context["content"]["epistemic_status"] == "known"

    assert home_fire["record_version"] == "3"
    assert home_fire["provenance"]["created_from"] == [
        {"record_id": "SRC-NFPA-HOME-FIRE-2026", "version": "1"},
        {"record_id": "SRC-RED-CROSS-ALERTS-2026", "version": "2"},
    ]
    assert home_fire["content"]["participants"] == [
        {"record_id": "CLM-HOME-FIRE-LEAVE-STAY-OUT", "version": "1"},
        {"record_id": "CLM-ALERTS-ENABLE-RESPOND", "version": "2"},
    ]
    assert home_fire["content"]["relation_type"] == "emergency_warning_and_home_fire_response"
    assert home_fire["content"]["roles"] == ["linked_record", "linked_record"]
    assert home_fire["content"]["direction"] == "undirected"
    assert home_fire["content"]["frame_ref"] == {
        "record_id": "CTX-REL-CROSS-HOME-FIRE-ALERTS", "version": "2"
    }

    assert home_fire_context["record_version"] == "2"
    assert home_fire_context["provenance"]["created_from"] == [
        {"record_id": "SRC-NFPA-HOME-FIRE-2026", "version": "1"},
        {"record_id": "SRC-RED-CROSS-ALERTS-2026", "version": "2"},
    ]
    assert home_fire_context["content"]["target_ref"] == {
        "record_id": "REL-CROSS-HOME-FIRE-ALERTS", "version": "3"
    }
    assert home_fire_context["content"]["context_content"]["condition"] == (
        "связь между участниками фиксируется только в пределах явно указанного типа Relation "
        "и не заменяет исходные Claim, Scope или Evidence Use"
    )
    assert home_fire_context["content"]["epistemic_status"] == "known"
