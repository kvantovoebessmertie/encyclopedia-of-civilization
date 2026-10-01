from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"epistemology-basics"/"records"
def test_epistemology_basics_slice_is_complete():
 r=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
 assert len(r)==9
 assert {"source","claim","evidence_use","context","scope"} <= {x["record_type"] for x in r}
 s={x["record_id"] for x in r if x["record_type"]=="source"}
 assert len(s)==1
 for c in [x for x in r if x["record_type"]=="claim"]:
  assert c["provenance"]["created_from"][0]["record_id"] in s
  assert any(e["content"]["claim_ref"]["record_id"]==c["record_id"] for e in r if e["record_type"]=="evidence_use")
