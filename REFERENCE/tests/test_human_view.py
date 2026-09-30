from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.human_view import build_human_view
from encyclopedia_reference.query import QueryInterface
from encyclopedia_reference.storage import FileStorage

ROOT = Path(__file__).resolve().parents[2]


def _load_records():
    records = []
    for path in sorted((ROOT / "CONTENT" / "vertical-slices").glob("*/*.json")):
        records.append(json.loads(path.read_text(encoding="utf-8")))
    for path in sorted((ROOT / "CONTENT" / "vertical-slices").glob("*/records/*.json")):
        records.append(json.loads(path.read_text(encoding="utf-8")))
    return records


def _query(tmp_path):
    storage = FileStorage(tmp_path)
    for record in _load_records():
        storage.create(record)
    return QueryInterface(storage)


def test_human_view_preserves_traceability_and_unknown(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "INF-WATER-FILTER-NOT-UNIVERSAL")
    assert view["status"] == "ok"
    assert view["inferred"][0]["status"] == "inferred"
    assert view["traceability"]
    assert view["unknown"]


def test_human_view_exposes_action_applicability(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "ACT-EARTHQUAKE-DROP-COVER-HOLD", mode="ACT")
    assert view["status"] == "ok"
    assert view["applicability"]
    assert view["traceability"]


def test_human_view_never_promotes_historical_record_to_truth(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "DEC-EARTHQUAKE-PROTECT")
    assert not any("true" in str(x).lower() for x in view["known"] + view["basis"])


def test_human_view_unknown_record_is_explicit(tmp_path):
    q = _query(tmp_path)
    view = build_human_view(q, "MISSING-RECORD")
    assert view["status"] == "not_found"
