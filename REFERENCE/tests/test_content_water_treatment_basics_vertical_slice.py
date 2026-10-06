from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SLICE=ROOT/"CONTENT"/"vertical-slices"/"water-treatment-basics"/"records"
def test_water_treatment_basics_slice_is_complete():
 records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]; types={r["record_type"] for r in records}; sources={r["record_id"] for r in records if r["record_type"]=="source"}; claims=[r for r in records if r["record_type"]=="claim"]; evidence=[r for r in records if r["record_type"]=="evidence_use"]
 assert len(records)==11; assert {"source","claim","evidence_use","context","scope"}<=types; assert len(sources)==2; assert len(claims)==3; assert len(evidence)==4
 for claim in claims:
  links=[e for e in evidence if e["content"]["claim_ref"]["record_id"]==claim["record_id"]]; assert links; assert all(e["content"]["source_ref"]["record_id"] in sources for e in links)
 assert {e["content"]["claim_ref"]["record_id"] for e in evidence}>={c["record_id"] for c in claims}