from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"time-standard-basics"/"records"
def test_time_standard_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==7
    assert {r["record_type"] for r in records}=={"source","claim","evidence_use","context","scope"}
    assert {r["record_id"] for r in records}>={"CLM-UTC-INTERNATIONAL","CLM-UTC-NIST"}
    assert all(r["record_type"]!="claim" or r["provenance"]["created_from"] for r in records)
