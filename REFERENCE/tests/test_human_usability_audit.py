from __future__ import annotations

import copy
import json
from pathlib import Path

from encyclopedia_reference.human_view import build_human_view
from encyclopedia_reference.query import QueryInterface
from encyclopedia_reference.storage import FileStorage

ROOT = Path(__file__).resolve().parents[2]


def _load_records():
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((ROOT / "CONTENT" / "vertical-slices").glob("*/records/*.json"))
    ]


def _query(tmp_path):
    storage = FileStorage(tmp_path)
    for record in _load_records():
        storage.create(record)
    return QueryInterface(storage)


def _view(q, record_id, mode):
    view = build_human_view(q, record_id, mode=mode)
    assert view["status"] == "ok"
    return view


def test_hua_01_accident_keeps_safety_boundary(tmp_path):
    view = _view(_query(tmp_path), "EVT-EARTHQUAKE-SHAKING", "UNDERSTAND")
    assert view["safety"]["source_is_not_truth"] is True
    assert view["safety"]["temporal_sequence_is_not_causality"] is True


def test_hua_02_known_unknown_are_separate(tmp_path):
    view = _view(_query(tmp_path), "ASM-WATER-FILTER-APPLICABILITY", "UNDERSTAND")
    assert "known" in view and "unknown" in view
    assert view["unknown"]


def test_hua_03_action_is_not_current_instruction(tmp_path):
    view = _view(_query(tmp_path), "ACT-EARTHQUAKE-DROP-COVER-HOLD", "ACT")
    assert view["act"]["allowed_as_current_instruction"] is False
    assert view["applicability"]["status"] == "not_established"
    assert view["safety"]["action_gate"] == "not_established_without_current_context"


def test_hua_04_trust_does_not_become_truth(tmp_path):
    view = _view(_query(tmp_path), "TRUST-SOURCE-NOT-ASSESSED", "VERIFY")
    rendered = json.dumps(view, ensure_ascii=False).lower()
    assert "истинность" not in rendered or "не устанавливает истинность" in rendered
    assert view["verification"]["available"] is True


def test_hua_05_conflict_state_remains_visible(tmp_path):
    q = _query(tmp_path)
    records = _load_records()
    synthetic = copy.deepcopy(records[0])
    synthetic["record_id"] = "HUA-CONFLICT-SYNTHETIC"
    synthetic["content"] = {"statement": "Пример", "status": "disputed", "disputed": True}
    q.storage.create(synthetic)
    view = _view(q, "HUA-CONFLICT-SYNTHETIC", "UNDERSTAND")
    assert view["conflicts"]


def test_hua_06_applicability_is_not_assumed(tmp_path):
    view = _view(_query(tmp_path), "CLM-BURN-EMERGENCY", "APPLY")
    assert view["apply"]["required_user_context"] is True
    assert view["applicability"]["status"] == "not_established"


def test_hua_07_history_does_not_become_present_instruction(tmp_path):
    view = _view(_query(tmp_path), "DEC-EARTHQUAKE-PROTECT", "DECIDE")
    assert any("универсальную рекомендацию" in str(x) for x in view["constraints"])


def test_hua_08_causality_is_not_inferred_from_result(tmp_path):
    view = _view(_query(tmp_path), "RES-EARTHQUAKE-PROTECTIVE", "CHECK")
    assert view["safety"]["temporal_sequence_is_not_causality"] is True
    assert view["safety"]["result_requires_observation"] is True
    assert any("Причинная связь" in str(x) for x in view["constraints"])


def test_hua_09_change_and_state_remain_traceable(tmp_path):
    q = _query(tmp_path)
    state = _view(q, "ST-WATER-CONTAINER-STORED", "UNDERSTAND")
    event = _view(q, "EVT-EARTHQUAKE-SHAKING", "UNDERSTAND")
    assert state["traceability"]
    assert event["traceability"]
    assert state["record"]["type"] == "state"
    assert event["record"]["type"] == "event"


def test_hua_10_after_action_result_is_checkable(tmp_path):
    view = _view(_query(tmp_path), "RES-EARTHQUAKE-PROTECTIVE", "CHECK")
    assert view["check"]["requires_observation"] is True
    assert "unknown" in view["check"]
    assert "constraints" in view["check"]


def test_hua_all_eight_modes_expose_mode_specific_contract(tmp_path):
    q = _query(tmp_path)
    expected = {
        "FIND": "find",
        "UNDERSTAND": "understand",
        "VERIFY": "verify",
        "APPLY": "apply",
        "DECIDE": "decide",
        "ACT": "act",
        "CHECK": "check",
        "RECOVER": "recover",
    }
    for mode, key in expected.items():
        view = _view(q, "ACT-EARTHQUAKE-DROP-COVER-HOLD", mode)
        assert key in view


def test_hua_full_corpus_has_traceability_and_safety_shape(tmp_path):
    q = _query(tmp_path)
    records = _load_records()
    assert len(records) == 1782
    for record in records:
        view = build_human_view(q, record["record_id"], str(record["record_version"]))
        assert view["status"] == "ok"
        provenance = record.get("provenance") or {}
        content = record.get("content") or {}
        has_basis_path = bool(provenance.get("created_from")) or any(
            content.get(key) for key in ("target_ref", "claim_ref", "source_ref", "basis_ref", "basis_refs", "context_ref", "scope_ref", "decision_ref", "premises", "refs")
        )
        if has_basis_path:
            assert view["traceability"]
        assert set(view["safety"]) >= {
            "historical_action_is_not_current_instruction",
            "source_is_not_truth",
            "inference_is_not_observation",
            "temporal_sequence_is_not_causality",
        }
        assert "verification" in view
        assert "unknown" in view


def test_hua_human_view_does_not_mutate_canonical_records(tmp_path):
    records = _load_records()
    original = copy.deepcopy(records)
    q = _query(tmp_path)
    for record in records:
        build_human_view(q, record["record_id"], str(record["record_version"]))
    assert original == records
