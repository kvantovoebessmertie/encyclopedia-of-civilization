import json
from pathlib import Path
from encyclopedia_reference.validator import Validator
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
ROOT=Path(__file__).resolve().parents[2]; CONTENT=ROOT/"CONTENT"/"vertical-slices"/"carbon-monoxide-heating-safety"/"records"; SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def test_records_validate():
 rs=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]; assert len(rs) == 13; v=Validator(SCHEMA)
 for r in rs:
  x=v.validate(r); assert x.passed,(r["record_id"],[(z.code,z.message) for z in x.findings])
 assert validate_semantic_dataset(rs)==[]
