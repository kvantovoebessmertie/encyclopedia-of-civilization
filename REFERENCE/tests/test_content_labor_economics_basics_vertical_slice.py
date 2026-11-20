import json
from pathlib import Path
SLICE=Path(__file__).resolve().parents[2]/"CONTENT"/"vertical-slices"/"labor-economics-basics"/"records"
def test_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    record_ids={r["record_id"] for r in records}
    assert len(records)==14
    assert "EU-LABOR_ECONOMICS_BASICS-C-ILO-GUIDE" in record_ids
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
