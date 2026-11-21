import json
from pathlib import Path

SLICE = Path("CONTENT/vertical-slices/ancient-civilizations-basics")


def test_ancient_civilizations_basics_has_23_records_and_exact_evidence_links():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in (SLICE / "records").glob("*.json")]
    assert len(records) == 23
    types = [r["record_type"] for r in records]
    assert types.count("source") == 8
    assert types.count("claim") == 3
    assert types.count("evidence_use") == 10
    assert types.count("context") == 1
    assert types.count("scope") == 1

    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = {r["record_id"] for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence} == claims

    expected = {
        "EU-ANCIENT_CIVILIZATIONS_BASICS-A-MCMAHON": ("SRC-MCMAHON-LAGASH-URBANISM", "CLM-ANCIENT_CIVILIZATIONS_BASICS-A"),
        "EU-ANCIENT_CIVILIZATIONS_BASICS-A-LAMB": ("SRC-LAMB-CHUNHUAYUM-SOCIAL-DIFFERENTIATION", "CLM-ANCIENT_CIVILIZATIONS_BASICS-A"),
        "EU-ANCIENT_CIVILIZATIONS_BASICS-B-LESURE": ("SRC-LESURE-AGRICULTURAL-DEMOGRAPHIC-TRANSITION", "CLM-ANCIENT_CIVILIZATIONS_BASICS-B"),
        "EU-ANCIENT_CIVILIZATIONS_BASICS-B-CREMA": ("SRC-CREMA-RICE-FARMING-JAPAN-DEMOGRAPHY", "CLM-ANCIENT_CIVILIZATIONS_BASICS-B"),
        "EU-ANCIENT_CIVILIZATIONS_BASICS-B-NEIL": ("SRC-NEIL-BRITAIN-NEOLITHIC-MOBILITY", "CLM-ANCIENT_CIVILIZATIONS_BASICS-B"),
        "EU-ANCIENT_CIVILIZATIONS_BASICS-C-CLARK": ("SRC-CLARK-URUK-TEXTS-ARCHAEOLOGY", "CLM-ANCIENT_CIVILIZATIONS_BASICS-C"),
    }
    by_id = {r["record_id"]: r for r in evidence}
    for evidence_id, (source_id, claim_id) in expected.items():
        record = by_id[evidence_id]
        assert record["content"]["source_ref"]["record_id"] == source_id
        assert record["content"]["claim_ref"]["record_id"] == claim_id
        assert record["content"]["evidence_role"] == "supports"
        assert record["content"]["material"]["description"]
