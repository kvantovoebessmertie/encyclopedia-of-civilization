from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT / "CONTENT" / "vertical-slices" / "food-security-basics" / "records"
def test_food_security_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==9
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    assert len([r for r in records if r["record_type"]=="claim"])==3
    assert len([r for r in records if r["record_type"]=="evidence_use"])==3
