from __future__ import annotations

import copy
from pathlib import Path

from encyclopedia_reference.publication import build_publication
from encyclopedia_reference.storage import FileStorage
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def base(record_id: str, record_type: str, content: dict) -> dict:
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

    assert storage.read("ROUNDTRIP-SEMANTICS") == record
