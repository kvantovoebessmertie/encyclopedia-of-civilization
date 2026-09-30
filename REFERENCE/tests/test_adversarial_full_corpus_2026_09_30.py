from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.human_view import build_human_view
from encyclopedia_reference.query import QueryInterface
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.storage import FileStorage
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"
EXPECTED_SLICES = 77
EXPECTED_RECORDS = 648
EXPECTED_TYPES = 19


def load_records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]


def test_full_corpus_has_no_duplicate_ids_and_expected_shape():
    records = load_records()
    assert len(records) == EXPECTED_RECORDS
    assert len({r["record_id"] for r in records}) == EXPECTED_RECORDS
    assert len({p.parent.parent.name for p in CONTENT.glob("*/records/*.json")}) == EXPECTED_SLICES
    assert len({r["record_type"] for r in records}) == EXPECTED_TYPES


def test_full_corpus_schema_and_semantics_are_clean():
    records = load_records()
    validator = Validator(SCHEMA)
    failures = []
    for record in records:
        result = validator.validate(record)
        if not result.passed:
            failures.append((record["record_id"], [(f.code, f.message) for f in result.findings]))
    assert failures == []
    assert validate_semantic_dataset(records) == []


def test_every_claim_has_provenance_and_evidence_to_a_source():
    records = load_records()
    by_id = {r["record_id"]: r for r in records}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    for claim in (r for r in records if r["record_type"] == "claim"):
        assert claim.get("provenance", {}).get("created_from"), claim["record_id"]
        links = [e for e in evidence if e.get("content", {}).get("claim_ref", {}).get("record_id") == claim["record_id"]]
        assert links, claim["record_id"]
        for link in links:
            source_id = link.get("content", {}).get("source_ref", {}).get("record_id")
            assert source_id in by_id and by_id[source_id]["record_type"] == "source"


def test_cross_slice_relations_have_explicit_frame_and_no_relation_participants():
    records = load_records()
    relation_ids = {r["record_id"] for r in records if r["record_type"] == "relation"}
    cross = [r for r in records if r["record_id"].startswith("REL-CROSS-")]
    assert len(cross) == 6
    for relation in cross:
        content = relation["content"]
        assert content.get("frame_ref") == {"record_id": "CTX-CROSS-SLICE-LINKAGE", "version": "1"}
        assert all(p["record_id"] not in relation_ids for p in content["participants"])


def test_human_view_all_records_preserves_unknown_and_safety_boundaries(tmp_path):
    storage = FileStorage(tmp_path / "storage")
    records = load_records()
    for record in records:
        storage.create(record)
    query = QueryInterface(storage)
    for record in records:
        view = build_human_view(query, record["record_id"], mode="UNDERSTAND")
        assert view["status"] == "ok"
        assert "unknown" in view
        assert view["safety"]["source_is_not_truth"] is True
        assert view["safety"]["temporal_sequence_is_not_causality"] is True
