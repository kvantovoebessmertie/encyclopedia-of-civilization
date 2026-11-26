from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "CONTRIBUTIONS" / "contribution-submission-v1.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def _valid_payload():
    return {
        "schema_version": "1.0",
        "submission_type": "new_claim",
        "subject_area": "History",
        "topic": "Demonstration",
        "title": "A proposed demonstration claim",
        "proposal_text": "A carefully scoped proposed statement for review.",
        "rationale": "This proposal fills a clearly described gap.",
        "sources": [{
            "title": "Example source metadata",
            "supports": "This source is offered for reviewer evaluation, not assumed to prove the claim."
        }],
        "evidence_notes": "The relationship between the source and proposal needs editorial verification.",
        "applicability": "Only within the stated historical context.",
        "limitations": "The example is not a real submission.",
        "uncertainty": "Uncertainty has not yet been evaluated.",
        "related_record_ids": [],
        "proposed_relations": [],
        "contributor_role": "reader",
        "rights_and_terms_acknowledged": True,
        "risk_flags": []
    }


def test_valid_payload_passes_schema():
    VALIDATOR.validate(_valid_payload())


def test_unknown_fields_are_rejected_including_contact_data():
    payload = _valid_payload()
    payload["email"] = "person@example.invalid"
    with pytest.raises(Exception):
        VALIDATOR.validate(payload)


@pytest.mark.parametrize(("submission_type", "related_ids", "relations", "sources", "valid"), [
    ("correction", [], [], [], False),
    ("correction", ["CLAIM-1"], [], [], True),
    ("contradiction", ["CLAIM-1"], [], [], False),
    ("contradiction", ["CLAIM-1", "CLAIM-2"], [], [], True),
    ("source", ["CLAIM-1"], [], [], False),
    ("source", ["CLAIM-1"], [], [{"title": "A source", "supports": "Supports the claim context."}], True),
    ("new_claim", [], [], [], False),
    ("new_claim", [], [], [{"title": "A source", "supports": "Supports the claim context."}], True),
    ("relation", [], [], [], False),
    ("relation", [], [{
        "source_record_id": "CLAIM-1",
        "target_record_id": "SOURCE-1",
        "relation_type": "supported_by",
        "direction": "directed",
        "rationale": "This proposed relation links the claim to relevant evidence."
    }], [], True),
])
def test_conditional_submission_requirements(submission_type, related_ids, relations, sources, valid):
    payload = _valid_payload()
    payload["submission_type"] = submission_type
    payload["related_record_ids"] = related_ids
    payload["proposed_relations"] = relations
    payload["sources"] = sources
    errors = list(VALIDATOR.iter_errors(payload))
    assert (not errors) is valid


def test_rights_acknowledgement_must_be_true():
    payload = _valid_payload()
    payload["rights_and_terms_acknowledged"] = False
    assert list(VALIDATOR.iter_errors(payload))


def test_duplicate_record_ids_are_rejected():
    payload = _valid_payload()
    payload["related_record_ids"] = ["CLAIM-1", "CLAIM-1"]
    assert list(VALIDATOR.iter_errors(payload))
