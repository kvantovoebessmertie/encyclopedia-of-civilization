from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator
ROOT=Path(__file__).resolve().parents[2]
CONTENT=ROOT/"CONTENT"/"vertical-slices"/"carbon-monoxide-heating-safety"/"records"
SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def _records(): return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]
def test_records_validate():
 records=_records(); assert len(records)==7; v=Validator(SCHEMA)
 for r in records:
  x=v.validate(r); assert x.passed,(r["record_id"],[(f.code,f.message) for f in x.findings])
 assert validate_semantic_dataset(records)==[]
def test_claims_have_evidence():
 rs=_records(); assert {r["record_id"] for r in rs if r["record_type"]=="claim"}=={r["content"]["claim_ref"]["record_id"] for r in rs if r["record_type"]=="evidence_use"}
def test_scope_exists(): assert any(r["record_type"]=="scope" for r in _records())
