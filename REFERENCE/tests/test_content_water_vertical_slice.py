from __future__ import annotations
import json
from pathlib import Path
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator
ROOT=Path(__file__).resolve().parents[2]
CONTENT=ROOT / "CONTENT" / "vertical-slices" / "water" / "records"
SCHEMA=ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"
def _records():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(CONTENT.glob("*.json"))]
def test_water_vertical_slice_records_validate():
    validator=Validator(SCHEMA); records=_records(); assert len(records)==12
    for record in records:
        result=validator.validate(record); assert result.passed, (record["record_id"],[(f.code,f.message) for f in result.findings])
def test_water_vertical_slice_has_independent_source():
    records=_records(); sources={r["record_id"] for r in records if r["record_type"]=="source"}; assert len(sources)==2
    assert sum(r["record_type"]=="context" for r in records)==1
    assert sum(r["record_type"]=="scope" for r in records)==1
    context=next(r for r in records if r["record_type"]=="context")
    scope=next(r for r in records if r["record_type"]=="scope")
    assert context["record_id"]=="CTX-WATER-EMERGENCY"
    assert context["content"]["target_ref"]["record_id"]=="CLM-WATER-BOILING-EFFECTIVE"
    assert "не удаляет" in context["content"]["context_content"]
    assert scope["record_id"]=="SCP-WATER-EMERGENCY"
    assert scope["content"]["target_ref"]["record_id"]=="CLM-WATER-BOILING-EFFECTIVE"
    assert "радиоактивно загрязнённую воду" in scope["content"]["scope_content"]
    claim_ids={r["record_id"] for r in records if r["record_type"]=="claim"}
    assert {"CLM-WATER-BOILING-EFFECTIVE","CLM-WATER-BOILING-TIME","CLM-WATER-CHEMICAL-LIMIT"} <= claim_ids
    assert any(e["content"].get("source_ref",{}).get("record_id")=="SRC-EPA-EMERGENCY-WATER-2026" for e in records if e["record_type"]=="evidence_use")
def test_water_vertical_slice_semantic_dataset_is_clean():
    assert validate_semantic_dataset(_records())==[]