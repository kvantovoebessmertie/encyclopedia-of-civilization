from __future__ import annotations

import copy
from pathlib import Path

from encyclopedia_reference.publication import build_publication
from encyclopedia_reference.storage import FileStorage
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def base(record_id: str, record_type: str, content: dict, **envelope) -> dict:
    return {
        "record_id": record_id,
        "record_type": record_type,
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "completion_status": "complete",
        "schema": "record/0.1",
        "provenance": {"method": "semantic-conformance-test"},
        "content": content,
        **envelope,
    }


def test_storage_preserves_semantic_record_without_inventing_relations(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "REL-NO-INVERSE",
        "relation",
        {
            "relation_type": "precedes",
            "participants": [
                {"record_id": "A", "version": "1"},
                {"record_id": "B", "version": "1"},
            ],
            "frame_ref": {"record_id": "FRAME", "version": "1"},
        },
    )
    before = copy.deepcopy(record)
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    assert storage.read_version("REL-NO-INVERSE", "1") == before
    assert "inverse" not in storage.read_version("REL-NO-INVERSE", "1")["content"]


def test_storage_does_not_turn_state_change_into_event(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "STATE-NO-EVENT",
        "state",
        {
            "state_content": {"value": "destroyed"},
            "subject_ref": {"record_id": "OBJ", "version": "1"},
            "time": {"start": "2026-01-01T00:00:00Z"},
        },
    )
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("STATE-NO-EVENT", "1")
    assert stored["record_type"] == "state"
    assert "event" not in stored
    assert "event_ref" not in stored["content"]


def test_storage_does_not_turn_process_into_cause_or_goal(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "PROCESS-NO-INFERENCE",
        "process",
        {
            "process_content": {"name": "heating"},
            "participants": [{"record_id": "OBJ", "version": "1"}],
            "time": {"start": "2026-01-01T00:00:00Z"},
        },
    )
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("PROCESS-NO-INFERENCE", "1")
    assert stored["record_type"] == "process"
    assert "cause" not in stored["content"]
    assert "goal" not in stored["content"]
    assert "purpose" not in stored["content"]


def test_storage_does_not_turn_context_into_participant_or_frame(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "CTX-NO-INFERENCE",
        "context",
        {
            "context_content": {"condition": "laboratory"},
            "target_ref": {"record_id": "CLAIM", "version": "1"},
            "epistemic_status": "known",
        },
    )
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("CTX-NO-INFERENCE", "1")
    assert stored["record_type"] == "context"
    assert stored["content"]["target_ref"] == record["content"]["target_ref"]
    assert "participant_refs" not in stored["content"]
    assert "frame_ref" not in stored["content"]


def test_storage_does_not_expand_scope_into_universe_or_members(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "SCOPE-NO-EXPANSION",
        "scope",
        {
            "target_ref": {"record_id": "CLAIM", "version": "1"},
            "scope_content": {"population": "adults_over_65"},
        },
    )
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("SCOPE-NO-EXPANSION", "1")
    assert stored["record_type"] == "scope"
    assert stored["content"]["scope_content"] == record["content"]["scope_content"]
    assert "universe" not in stored["content"]
    assert "member_refs" not in stored["content"]


def test_storage_does_not_turn_provenance_into_authorship(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "PROV-NO-AUTHORSHIP",
        "provenance",
        {
            "target_ref": {"record_id": "DOC", "version": "1"},
            "relation": "derived_from",
            "inputs": [{"record_id": "SRC", "version": "1"}],
        },
    )
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("PROV-NO-AUTHORSHIP", "1")
    assert stored["record_type"] == "provenance"
    assert "author_ref" not in stored["content"]
    assert "contributor_ref" not in stored["content"]


def test_storage_does_not_turn_authorship_into_provenance(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "AUTHOR-NO-PROVENANCE",
        "authorship_contribution",
        {
            "target_ref": {"record_id": "DOC", "version": "1"},
            "contributor_ref": {"record_id": "PERSON", "version": "1"},
            "contribution": "author",
        },
    )
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("AUTHOR-NO-PROVENANCE", "1")
    assert stored["record_type"] == "authorship_contribution"
    assert stored["content"]["contributor_ref"] == record["content"]["contributor_ref"]
    assert "provenance_relation" not in stored["content"]
    assert "derived_from" not in stored["content"]


def test_storage_does_not_turn_trust_into_truth(tmp_path):
    validator = Validator(SCHEMA)
    storage = FileStorage(tmp_path)
    record = base(
        "TRUST-NO-TRUTH",
        "trust_reputation",
        {
            "target_ref": {"record_id": "CLAIM", "version": "1"},
            "assessment_type": "trust",
            "basis_refs": [{"record_id": "EVIDENCE", "version": "1"}],
            "subject_ref": {"record_id": "CLAIM", "version": "1"},
            "goal_ref": {"record_id": "GOAL", "version": "1"},
        },
    )
    record["type_version"] = "1.1"
    result = validator.validate(record)
    storage.create(record)

    assert result.passed
    stored = storage.read_version("TRUST-NO-TRUTH", "1")
    assert stored["record_type"] == "trust_reputation"
    assert stored["content"] == record["content"]
    assert stored["content"].get("truth") is not True


def test_unknown_identity_survives_publication_without_resolution(tmp_path):
    validator = Validator(SCHEMA)
    record = base(
        "IDENTITY-UNKNOWN-PUBLISH",
        "identity",
        {
            "identity_level": "referent",
            "targets": [
                {"record_id": "A", "version": "1"},
                {"record_id": "B", "version": "1"},
            ],
            "criterion": "same referent",
            "identity_status": "unknown",
            "frame_ref": {"record_id": "FRAME", "version": "1"},
        },
    )
    created = validator.validate(record)
    assert created.passed

    publication = build_publication([record])
    assert publication["source_records_unchanged"] is True
    assert record["content"]["identity_status"] == "unknown"


def test_publication_does_not_invent_semantic_roles():
    records = [
        base(
            "STATE-PUB",
            "state",
            {
                "state_content": {"value": "active"},
                "subject_ref": {"record_id": "OBJ", "version": "1"},
                "time": {"start": "2026-01-01T00:00:00Z"},
            },
        ),
        base(
            "REL-PUB",
            "relation",
            {
                "relation_type": "associated_with",
                "participants": [
                    {"record_id": "A", "version": "1"},
                    {"record_id": "B", "version": "1"},
                ],
                "frame_ref": {"record_id": "FRAME", "version": "1"},
            },
        ),
    ]
    before = copy.deepcopy(records)

    publication = build_publication(records)

    assert publication["source_records_unchanged"] is True
    assert records == before
    assert all("truth" not in record["content"] for record in records)


def test_storage_roundtrip_does_not_change_record_semantics(tmp_path):
    storage = FileStorage(tmp_path)
    record = base(
        "ROUNDTRIP-SEMANTICS",
        "claim",
        {"statement": "пример", "claim_type": "descriptive"},
    )

    storage.create(record)

    assert storage.read_version("ROUNDTRIP-SEMANTICS", "1") == record


def _semantic_fixture_records():
    return [
        base(
            "SEM-STATE",
            "state",
            {
                "state_content": {"value": "active"},
                "subject_ref": {"record_id": "OBJ", "version": "1"},
                "time": {"start": "2026-01-01T00:00:00Z"},
            },
        ),
        base(
            "SEM-PROCESS",
            "process",
            {
                "process_content": {"name": "heating"},
                "participants": [{"record_id": "OBJ", "version": "1"}],
                "context_ref": {"record_id": "CTX", "version": "1"},
                "time": {"start": "2026-01-01T00:00:00Z", "end": {"status": "unknown"}},
                "start_ref": {"record_id": "START", "version": "1"},
                "end_ref": {"record_id": "END", "version": "1"},
                "phase_refs": [{"record_id": "PHASE", "version": "1"}],
            },
            scope={"record_id": "SCOPE", "version": "1"},
            context={"record_id": "CTX", "version": "1"},
        ),
        base(
            "SEM-RELATION",
            "relation",
            {
                "relation_type": "precedes",
                "participants": [
                    {"record_id": "A", "version": "1"},
                    {"record_id": "B", "version": "1"},
                ],
                "frame_ref": {"record_id": "FRAME", "version": "1"},
            },
        ),
        base(
            "SEM-CONTEXT",
            "context",
            {
                "context_content": {"condition": "laboratory"},
                "target_ref": {"record_id": "CLAIM", "version": "1"},
                "epistemic_status": "known",
            },
        ),
        base(
            "SEM-SCOPE",
            "scope",
            {
                "target_ref": {"record_id": "CLAIM", "version": "1"},
                "scope_content": {"population": "adults_over_65"},
            },
        ),
    ]


def test_publication_preserves_semantic_payload_for_all_core_families():
    records = _semantic_fixture_records()
    before = copy.deepcopy(records)
    publication = build_publication(records)

    assert records == before
    assert publication["source_records_unchanged"] is True
    by_id = {entry["record_id"]: entry for entry in publication["entries"]}
    for record in before:
        assert by_id[record["record_id"]]["record_type"] == record["record_type"]
        assert by_id[record["record_id"]]["content"] == record["content"]


def test_package_recovery_preserves_semantic_payload(tmp_path):
    records = _semantic_fixture_records()
    package = tmp_path / "package"
    from encyclopedia_reference.recovery import make_package, recover_package

    referents = [
        base(rid, "record", {"note": "referent"})
        for rid in ["OBJ", "A", "B", "FRAME", "START", "END", "PHASE"]
    ]
    referents.extend([
        base("CLAIM", "claim", {"statement": "fixture claim", "claim_type": "descriptive"}),
        base(
            "CTX",
            "context",
            {"context_content": {"condition": "laboratory"}, "target_ref": {"record_id": "CLAIM", "version": "1"}},
        ),
        base(
            "SCOPE",
            "scope",
            {"target_ref": {"record_id": "CLAIM", "version": "1"}, "scope_content": {"population": "fixture"}},
        ),
    ])
    make_package(records + referents, package)
    recovered, findings = recover_package(package, SCHEMA)

    assert findings == []
    recovered_by_id = {r["record_id"]: r for r in recovered.export_all()}
    for record in records:
        assert recovered_by_id[record["record_id"]] == record


def test_query_is_read_only_and_does_not_reclassify_records(tmp_path):
    from encyclopedia_reference.query import QueryInterface

    storage = FileStorage(tmp_path)
    records = _semantic_fixture_records()
    for record in records:
        storage.create(record)

    before = copy.deepcopy(storage.export_all())
    result = QueryInterface(storage).query(record_type="relation")

    assert [r["record_id"] for r in result] == ["SEM-RELATION"]
    assert storage.export_all() == before


def test_edit_preserves_prior_version_and_does_not_change_identity_by_content(tmp_path):
    from encyclopedia_reference.pipeline import ReferencePipeline

    pipeline = ReferencePipeline(SCHEMA, tmp_path)
    referenced = base("OBJ", "record", {"note": "referent"})
    assert pipeline.create(referenced).passed
    first = base(
        "HISTORY-STATE",
        "state",
        {
            "state_content": {"value": "active"},
            "subject_ref": {"record_id": "OBJ", "version": "1"},
            "time": {"start": "2026-01-01T00:00:00Z"},
        },
    )
    assert pipeline.create(first).passed

    second = copy.deepcopy(first)
    second["record_version"] = "2"
    second["content"]["state_content"]["value"] = "inactive"
    assert pipeline.edit(second, expected_version="1").passed

    assert pipeline.storage.read_version("HISTORY-STATE", "1") == first
    assert pipeline.storage.read_version("HISTORY-STATE", "2") == second
    assert pipeline.storage.list_versions("HISTORY-STATE") == ["1", "2"]


def test_unknown_values_are_preserved_across_package_boundary(tmp_path):
    from encyclopedia_reference.recovery import make_package, recover_package

    record = base(
        "UNKNOWN-PRESERVED",
        "state",
        {
            "state_content": {"value": {"status": "unknown", "note": "not observed"}},
            "subject_ref": {"record_id": "OBJ", "version": "1"},
            "time": {"start": {"status": "unknown"}},
        },
    )
    package = tmp_path / "unknown-package"
    referent = base("OBJ", "record", {"note": "referent"})
    make_package([record, referent], package)
    recovered, findings = recover_package(package, SCHEMA)

    assert findings == []
    assert {r["record_id"]: r for r in recovered.export_all()}["UNKNOWN-PRESERVED"] == record
    assert {r["record_id"]: r for r in recovered.export_all()}["OBJ"] == referent


def test_identity_candidates_and_unknown_status_are_not_collapsed_by_publication():
    record = base(
        "IDENTITY-CANDIDATES",
        "identity",
        {
            "identity_level": "referent",
            "targets": [
                {"record_id": "A", "version": "1"},
                {"record_id": "B", "version": "1"},
            ],
            "criterion": "same referent",
            "identity_status": "ambiguous",
            "candidate_refs": [{"record_id": "A", "version": "1"}],
            "uncertainty": {"status": "unknown"},
        },
    )
    before = copy.deepcopy(record)

    publication = build_publication([record])

    assert record == before
    entry = publication["entries"][0]
    assert entry["content"]["identity_status"] == "ambiguous"
    assert entry["content"]["candidate_refs"] == [{"record_id": "A", "version": "1"}]
    assert entry["content"]["uncertainty"] == {"status": "unknown"}
    assert entry["content"].get("identity_status") != "resolved_same"


def test_context_epistemic_status_and_missing_values_survive_publication():
    records = [
        base(
            "CTX-DISPUTED",
            "context",
            {
                "context_content": {"condition": "historical reconstruction"},
                "target_ref": {"record_id": "CLAIM", "version": "1"},
                "epistemic_status": "disputed",
            },
        ),
        base(
            "CTX-INCOMPLETE",
            "context",
            {
                "context_content": {"condition": "partially recorded"},
                "target_ref": {"record_id": "CLAIM", "version": "1"},
            },
        ),
    ]
    before = copy.deepcopy(records)
    publication = build_publication(records)

    assert records == before
    entries = {e["record_id"]: e for e in publication["entries"]}
    assert entries["CTX-DISPUTED"]["content"]["epistemic_status"] == "disputed"
    assert "epistemic_status" not in entries["CTX-INCOMPLETE"]["content"]


def test_scope_membership_rule_and_universe_are_not_invented_or_expanded():
    record = base(
        "SCOPE-QUALIFIED",
        "scope",
        {
            "target_ref": {"record_id": "CLAIM", "version": "1"},
            "scope_content": {"population": "sample"},
            "level": "sample",
            "membership_rule": "explicit inclusion",
        },
    )
    before = copy.deepcopy(record)

    publication = build_publication([record])

    assert record == before
    content = publication["entries"][0]["content"]
    assert content == before["content"]
    assert "universe_ref" not in content
