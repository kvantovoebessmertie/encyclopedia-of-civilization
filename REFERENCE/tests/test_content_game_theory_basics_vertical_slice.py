from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
DIR=ROOT/"CONTENT"/"vertical-slices"/"game-theory-basics"/"records"
def test_slice_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in DIR.glob("*.json")]
    assert len(records)==9
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==1
    for r in records:
        if r["record_type"]=="claim":
            assert r["provenance"]["created_from"][0]["record_id"] in sources
