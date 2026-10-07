import json
from pathlib import Path
SLICE=Path(__file__).resolve().parents[2]/"CONTENT"/"vertical-slices"/"labor-economics-basics"/"records"
def test_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==13
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
