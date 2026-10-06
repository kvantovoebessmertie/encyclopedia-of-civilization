import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator
ROOT=Path(__file__).resolve().parents[2]
CONTENT=ROOT/"CONTENT"/"vertical-slices"/"septic-system-emergency"/"records"
SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def _records() -> list[dict]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(CONTENT.glob("*.json"))]
def test_septic_system_emergency_slice_records_validate():
    validator = Validator(SCHEMA)
    records = _records()
    assert len(records) == 10
    assert {"source","claim","evidence_use","context","scope"} <= {record["record_type"] for record in records}
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"],[(f.code, f.message) for f in result.findings])
def test_septic_system_emergency_semantic_dataset_is_clean():
    assert validate_semantic_dataset(_records()) == []
