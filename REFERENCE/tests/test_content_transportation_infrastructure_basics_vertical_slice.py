from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "transportation-infrastructure-basics" / "records"

def test_transportation_infrastructure_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
