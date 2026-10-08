from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"fire-safety-basics"
SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def _records(): return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((SLICE/"records").glob("*.json"))]
def test_vertical_slice_has_canonical_nine_record_shape():
 r=_records(); assert len(r)==12; assert {x["record_type"] for x in r}=={"source","claim","evidence_use","context","scope","relation"}; assert len({x["record_id"] for x in r})==12
def test_vertical_slice_is_schema_and_semantically_clean():
 r=_records(); v=Validator(SCHEMA)
 for x in r:
  z=v.validate(x); assert z.passed,(x["record_id"],[(f.code,f.message) for f in z.findings])
 assert validate_semantic_dataset(r)==[]
def test_vertical_slice_claims_have_provenance_and_evidence_paths():
 r=_records(); by={x["record_id"]:x for x in r}; es=[x for x in r if x["record_type"]=="evidence_use"]; cs=[x for x in r if x["record_type"]=="claim"]; assert len(cs)==3; assert len(es)==4
 for c in cs:
  assert c.get("provenance",{}).get("created_from"); links=[e for e in es if e.get("content",{}).get("claim_ref",{}).get("record_id")==c["record_id"]]; assert links
  for e in links: assert by[e["content"]["source_ref"]["record_id"]]["record_type"]=="source"
