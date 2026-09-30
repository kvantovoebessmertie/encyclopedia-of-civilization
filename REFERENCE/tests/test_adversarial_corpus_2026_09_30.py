from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]


def test_adversarial_full_corpus_is_schema_and_semantically_clean():
    rs = records()
    assert len(rs) == 558
    assert len({r["record_id"] for r in rs}) == 558
    validator = Validator(SCHEMA)
    for r in rs:
        result = validator.validate(r)
        assert result.passed, (r["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(rs) == []


def test_adversarial_every_claim_has_source_and_evidence_path():
    rs = records()
    by_id = {r["record_id"]: r for r in rs}
    claims = [r for r in rs if r["record_type"] == "claim"]
    evidence = [r for r in rs if r["record_type"] == "evidence_use"]
    for claim in claims:
        assert claim.get("provenance", {}).get("created_from"), claim["record_id"]
        links = [e for e in evidence if e.get("content", {}).get("claim_ref", {}).get("record_id") == claim["record_id"]]
        assert links, claim["record_id"]
        for e in links:
            source_id = e["content"]["source_ref"]["record_id"]
            assert by_id[source_id]["record_type"] == "source"


def test_adversarial_cross_slice_relations_do_not_reference_relations_as_participants():
    rs = records()
    relation_ids = {r["record_id"] for r in rs if r["record_type"] == "relation"}
    for relation in (r for r in rs if r["record_id"].startswith("REL-CROSS-")):
        assert all(p["record_id"] not in relation_ids for p in relation["content"]["participants"])


def test_adversarial_new_slices_use_existing_types_only():
    allowed = {"record","claim","source","evidence_use","assessment","inference","decision","action","event","result","state","process","relation","identity","context","scope","provenance","authorship_contribution","trust_reputation"}
    for slug in ("infrastructure-basics","chronology-methods","archaeology-basics","early-agriculture","urbanization","writing-systems","trade-networks","state-formation","fire","flood"):
        files = list((CONTENT / slug / "records").glob("*.json"))
        assert len(files) == 9
        assert {json.loads(p.read_text(encoding="utf-8"))["record_type"] for p in files} <= allowed


def test_adversarial_core_reference_targets_resolve():
    rs = records()
    ids = {r["record_id"] for r in rs}
    for r in rs:
        content = r.get("content", {})
        for key in ("claim_ref","source_ref","target_ref","context_ref","scope_ref","decision_ref"):
            ref = content.get(key)
            if isinstance(ref, dict) and "record_id" in ref:
                assert ref["record_id"] in ids, (r["record_id"], key, ref)
