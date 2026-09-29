from __future__ import annotations

import copy
import random
from pathlib import Path

from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def valid_claim():
    return {
        "record_id": "FUZZ-1",
        "record_type": "claim",
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "schema": "record/0.1",
        "provenance": {"method": "fuzz"},
        "content": {"statement": "stable", "claim_type": "descriptive"},
    }


def mutate(record, mutation):
    value = copy.deepcopy(record)
    if mutation == "delete_root":
        value.pop(random.choice(["record_id", "record_type", "record_version", "type_version", "publication_status", "schema", "provenance", "content"]))
    elif mutation == "wrong_type":
        value[random.choice(["record_id", "record_version", "type_version", "schema"])] = 123
    elif mutation == "unknown_type":
        value["record_type"] = "UNKNOWN"
    elif mutation == "bad_status":
        value["publication_status"] = "UNKNOWN"
    elif mutation == "bad_schema":
        value["schema"] = "record/999"
    elif mutation == "bad_profile":
        value["type_version"] = "999.0"
    elif mutation == "bad_ref":
        value["content"]["scope_ref"] = ["not", "a", "ref"]
    elif mutation == "truth_inference":
        value["publication_status"] = "published"
        value["content"]["truth"] = True
    elif mutation == "extra":
        value["unexpected"] = {"nested": [1, 2, 3]}
    return value


def test_fuzz_mutations_never_raise_and_are_deterministic():
    validator = Validator(SCHEMA)
    mutations = [
        "delete_root",
        "wrong_type",
        "unknown_type",
        "bad_status",
        "bad_schema",
        "bad_profile",
        "bad_ref",
        "truth_inference",
        "extra",
    ]

    rng = random.Random(20260929)
    for _ in range(500):
        mutation = rng.choice(mutations)
        record = mutate(valid_claim(), mutation)
        first = validator.validate(record)
        second = validator.validate(copy.deepcopy(record))
        assert first == second
        assert first.status in {"pass", "fail"}
        if mutation in {"delete_root", "wrong_type", "unknown_type", "bad_status", "bad_schema", "bad_profile", "bad_ref", "truth_inference", "extra"}:
            if mutation == "extra":
                assert first.status == "fail"
            elif mutation == "truth_inference":
                assert any(f.code == "VAL-L4-PUBLICATION-TRUTH" for f in first.findings)
            else:
                assert first.status == "fail"


def test_fuzz_nested_values_are_rejected_or_pass_without_exception():
    validator = Validator(SCHEMA)
    rng = random.Random(20260930)

    for _ in range(250):
        record = valid_claim()
        depth = rng.randint(1, 12)
        nested = "x"
        for _ in range(depth):
            nested = {"value": nested}
        record["content"]["statement"] = nested
        result = validator.validate(record)
        assert result.status in {"pass", "fail"}
