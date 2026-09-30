from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "cross-slice-linkage"
EXPECTED_RELATIONS = {
    "REL-CROSS-WATER-CHEMICAL",
    "REL-CROSS-WATER-FILTER",
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
    assert all(len(r["content"]["participants"]) >= 2 for r in records)
    assert all(r["content"]["direction"] in {"directed", "undirected", "unknown"} for r in records)
    participant_ids = {ref["record_id"] for r in records for ref in r["content"]["participants"]}
    assert all(not pid.startswith("REL-CROSS-") for pid in participant_ids)
