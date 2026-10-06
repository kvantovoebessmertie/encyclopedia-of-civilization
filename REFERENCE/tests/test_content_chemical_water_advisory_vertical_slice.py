import json
from pathlib import Path
from encyclopedia_reference.validator import Validator
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
ROOT=Path(__file__).resolve().parents[2]; CONTENT=ROOT/"CONTENT"/"vertical-slices"/"chemical-water-advisory"/"records"; SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def _records(): return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]
def test_records_validate():
 rs=_records(); assert len(rs)==9; v=Validator(SCHEMA)
 for r in rs:
  x=v.validate(r); assert x.passed,(r["record_id"],[(z.code,z.message) for z in x.findings])
 assert validate_semantic_dataset(rs)==[]
def test_claims_have_evidence():
 rs=_records(); sources={r["record_id"] for r in rs if r["record_type"]=="source"}; claims=[r for r in rs if r["record_type"]=="claim"]; evidence=[r for r in rs if r["record_type"]=="evidence_use"]
 assert len(sources)==2 and len(claims)==2 and len(evidence)==3
 for claim in claims:
  links=[e for e in evidence if e["content"]["claim_ref"]["record_id"]==claim["record_id"]]
  assert links
  assert all(e["content"]["source_ref"]["record_id"] in sources for e in links)
 assert {e["content"]["claim_ref"]["record_id"] for e in evidence} >= {c["record_id"] for c in claims}