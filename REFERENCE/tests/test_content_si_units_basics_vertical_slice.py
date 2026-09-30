from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"si-units-basics"/"records"
def test_si_units_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==7
    assert {r["record_type"] for r in records}=={"source","claim","evidence_use","context","scope"}
    ids={r["record_id"] for r in records}
    assert {"CLM-SI-SEVEN-BASE","CLM-SI-DERIVED"}<=ids
    assert all(r["record_type"]!="claim" or r["provenance"]["created_from"] for r in records)
