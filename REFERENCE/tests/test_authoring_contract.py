from __future__ import annotations

import copy
import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]


def test_authoring_definition_of_done_is_structurally_and_semantically_met(tmp_path):
    rs = records()
    validator = Validator(SCHEMA)
    assert rs
    for r in rs:
        result = validator.validate(r)
        assert result.passed, (r["record_id"], [(f.code, f.message) for f in result.findings])
        assert r.get("record_id")
        assert r.get("record_version")
        assert r.get("type_version")
        assert r.get("completion_status")
        assert r.get("publication_status")
        assert r.get("provenance")
    assert validate_semantic_dataset(rs) == []


def test_authoring_contract_source_claim_evidence_roles_are_distinct():
    rs = records()
    ids = {r["record_id"]: r for r in rs}
    for claim in (r for r in rs if r["record_type"] == "claim"):
        assert claim.get("provenance", {}).get("created_from"), claim["record_id"]
        links = [r for r in rs if r["record_type"] == "evidence_use" and r.get("content", {}).get("claim_ref", {}).get("record_id") == claim["record_id"]]
        assert links, claim["record_id"]
        for link in links:
            source_id = link.get("content", {}).get("source_ref", {}).get("record_id")
            assert source_id in ids and ids[source_id]["record_type"] == "source"
            assert link["record_type"] != "claim"
            assert ids[source_id]["record_type"] != "claim"


def test_authoring_contract_does_not_mutate_canonical_records_during_validation(tmp_path):
    rs = records()
    before = copy.deepcopy(rs)
    validator = Validator(SCHEMA)
    for r in rs:
        assert validator.validate(r).passed
    assert validate_semantic_dataset(rs) == []
    assert rs == before


def test_authoring_contract_package_is_recoverable_and_publication_is_present(tmp_path):
    rs = records()
    report = build_content_package(rs, package_dir=tmp_path / "package", schema_path=SCHEMA, package_id="authoring-contract-202-v1")
    assert report["integrity_and_validation"] == "PASS"
    assert report["publication_present"] is True
    assert report["offline_schema_present"] is True
    assert report["recovered_record_count"] == len(rs)
    assert report["expected_record_count"] == len(rs)
    assert report["findings"] == []


def test_authoring_contract_publication_status_does_not_define_truth():
    rs = records()
    for r in rs:
        assert r.get("publication_status") in {"draft", "published", "archived"}
        assert r.get("completion_status") in {"complete", "incomplete", "partial"}
    # Publication/completion are lifecycle states, not epistemic truth values.
    assert any(r["publication_status"] == "published" for r in rs)
    assert any(r["completion_status"] == "complete" for r in rs)


def test_authoring_contract_cross_slice_and_history_boundaries_remain_explicit():
    rs = records()
    relation_ids = {r["record_id"] for r in rs if r["record_type"] == "relation"}
    for r in rs:
        if r["record_id"].startswith("REL-CROSS-"):
            assert r["content"].get("frame_ref") == {"record_id": "CTX-CROSS-SLICE-LINKAGE", "version": "1"}
            assert all(p["record_id"] not in relation_ids for p in r["content"]["participants"])
    # Canonical records retain explicit versions; no validation step may rewrite them.
    assert all("record_version" in r for r in rs)
