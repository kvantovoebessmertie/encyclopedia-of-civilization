import json
from pathlib import Path

SLICE = Path("CONTENT/vertical-slices/materials-science-basics")


def test_content_materials_science_basics_vertical_slice():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in (SLICE / "records").glob("*.json")]
    assert len(records) == 18
    types = [r["record_type"] for r in records]
    assert types.count("source") == 3
    assert types.count("claim") == 4
    assert types.count("evidence_use") == 9
    assert types.count("context") == 1
    assert types.count("scope") == 1

    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    primary = "SRC-MATERIALS_SCIENCE_BASICS"
    independent = "SRC-M5-MATERIALS-SCIENCE-NSF"
    nist_mechanical = "SRC-NIST-MECHANICAL-PERFORMANCE"
    assert sources == {primary, independent, nist_mechanical}

    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    assert claims["CLM-MATERIALS_SCIENCE_BASICS-A"]["provenance"]["created_from"][0]["record_id"] == primary
    assert claims["CLM-MATERIALS_SCIENCE_BASICS-B"]["provenance"]["created_from"][0]["record_id"] == primary
    assert claims["CLM-MATERIALS_SCIENCE_BASICS-C"]["provenance"]["created_from"][0]["record_id"] == primary
    assert claims["CLM-M5-MATERIALS-PERFORMANCE-D"]["provenance"]["created_from"][0]["record_id"] == independent

    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    by_claim = {}
    for item in evidence:
        claim_id = item["content"]["claim_ref"]["record_id"]
        source_id = item["content"]["source_ref"]["record_id"]
        assert source_id in sources
        by_claim.setdefault(claim_id, set()).add(source_id)

    assert set(by_claim) == set(claims)
    assert by_claim["CLM-MATERIALS_SCIENCE_BASICS-A"] == {primary, independent}
    assert by_claim["CLM-MATERIALS_SCIENCE_BASICS-B"] == {primary, independent, nist_mechanical}
    assert by_claim["CLM-MATERIALS_SCIENCE_BASICS-C"] == {primary, independent}
    assert by_claim["CLM-M5-MATERIALS-PERFORMANCE-D"] == {independent, nist_mechanical}

    nsf_b = next(e for e in evidence if e["record_id"] == "EU-M5-MATERIALS-SCIENCE-NSF-B")
    nist_b = next(e for e in evidence if e["record_id"] == "EU-M5-MATERIALS-SCIENCE-NIST-B")
    performance = next(e for e in evidence if e["record_id"] == "EU-M5-MATERIALS-PERFORMANCE-NIST-D")
    assert nsf_b["record_version"] == "2"
    assert "does not explicitly name composites" in nsf_b["content"]["material"]["description"]
    assert "composites" in nist_b["content"]["material"]["description"]
    assert "does not fully establish" in performance["content"]["material"]["description"]
