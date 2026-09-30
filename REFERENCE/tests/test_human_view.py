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


def test_human_view_supports_all_normative_modes(tmp_path):
    q = _query(tmp_path)
    for mode in ("FIND", "UNDERSTAND", "VERIFY", "APPLY", "DECIDE", "ACT", "CHECK", "RECOVER"):
        view = build_human_view(q, "ACT-EARTHQUAKE-DROP-COVER-HOLD", mode=mode)
        assert view["status"] == "ok"
        assert view["mode"] == mode


def test_human_view_rejects_unknown_mode(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "ACT-EARTHQUAKE-DROP-COVER-HOLD", mode="MAKE_IT_UP")
    assert view["status"] == "invalid_mode"


def test_human_view_preserves_traceability_and_inference_status(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "INF-WATER-FILTER-NOT-UNIVERSAL", mode="VERIFY")
    assert view["status"] == "ok"
    assert view["inferred"][0]["status"] == "inferred"
    assert view["traceability"]
    assert view["safety"]["verification_required"] is True


def test_human_view_action_is_not_current_instruction_without_user_context(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "ACT-EARTHQUAKE-DROP-COVER-HOLD", mode="ACT")
    assert view["status"] == "ok"
    assert view["applicability"]["status"] == "not_established"
    assert view["applicability"]["context"]
    assert view["applicability"]["scope"]
    assert view["safety"]["action_gate"] == "not_established_without_current_context"
    assert view["traceability"]


def test_human_view_keeps_unresolved_applicability_visible(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "CLM-BURN-EMERGENCY", mode="APPLY")
    assert view["status"] == "ok"
    assert view["applicability"]["status"] == "not_established"
    assert "ПРИМЕНИМОСТЬ НЕ УСТАНОВЛЕНА" in view["applicability"]["label"]


def test_human_view_never_promotes_historical_record_to_truth(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "DEC-EARTHQUAKE-PROTECT")
    rendered = json.dumps(view, ensure_ascii=False).lower()
    assert "истин" not in rendered
    assert "универсальную рекомендацию" in rendered


def test_human_view_preserves_result_non_causality(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "RES-EARTHQUAKE-PROTECTIVE", mode="CHECK")
    assert view["safety"]["temporal_sequence_is_not_causality"] is True
    assert any("Причинная связь" in str(x) or "причин" in str(x).lower() for x in view["constraints"])


def test_human_view_exposes_unknowns_and_does_not_fill_them(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "ASM-WATER-FILTER-APPLICABILITY")
    assert view["unknown"]
    assert all(item["status"] in {"unknown", "unresolved", "not_applicable"} for item in view["unknown"])


def test_human_view_corpus_has_explicit_safety_shape(tmp_path):
    q = _query(tmp_path)
    records = _load_records()
    assert records
    for record in records:
        view = build_human_view(q, record["record_id"], str(record["record_version"]))
        assert view["status"] == "ok"
        assert set(view["safety"]) >= {
            "historical_action_is_not_current_instruction",
            "source_is_not_truth",
            "inference_is_not_observation",
            "temporal_sequence_is_not_causality",
        }
        assert "traceability" in view
        assert "unknown" in view


def test_human_view_does_not_mutate_canonical_record(tmp_path):
    records = _load_records()
    original = copy.deepcopy(records[0])
    q = _query(tmp_path)
    build_human_view(q, original["record_id"])
    assert original == records[0]


def test_human_view_unknown_record_is_explicit(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "MISSING-RECORD")
    assert view["status"] == "not_found"
