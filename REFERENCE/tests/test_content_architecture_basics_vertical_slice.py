import json
from pathlib import Path

SLICE = Path("CONTENT/vertical-slices/architecture-basics")


def test_content_architecture_basics_vertical_slice():
    records = [
        json.loads(p.read_text(encoding="utf-8"))
        for p in (SLICE / "records").glob("*.json")
    ]
    assert len(records) == 11
    types = [r["record_type"] for r in records]
    assert types.count("source") == 2
    assert types.count("claim") == 3
    assert types.count("evidence_use") == 4
    assert types.count("context") == 1
    assert types.count("scope") == 1

    source_ids = {
        r["record_id"] for r in records if r["record_type"] == "source"
    }
    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]

    # Claims may legitimately derive from different sources. Do not select
    # one source via filesystem iteration order and require every claim to
    # reference it: glob ordering is not a stable contract.
    assert all(
        r["provenance"]["created_from"]
        and all(
            origin["record_id"] in source_ids
            for origin in r["provenance"]["created_from"]
        )
        for r in claims
    )
    assert all(
        r["content"]["source_ref"]["record_id"] in source_ids
        for r in evidence
    )
    assert {
        r["content"]["claim_ref"]["record_id"] for r in evidence
    } == {r["record_id"] for r in claims}

    claim_a = next(
        r for r in claims if r["record_id"] == "CLM-ARCHITECTURE_BASICS-A"
    )
    assert "Архитектура объединяет" in claim_a["content"]["statement"]
