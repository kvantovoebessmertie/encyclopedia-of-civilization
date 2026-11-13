from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "electrical-safety-basics" / "records"

def test_electrical_safety_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) >= 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) >= 1
    claims = [r for r in records if r["record_type"] == "claim"]
    assert len(claims) >= 3
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(evidence) >= 3
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)

def test_electrical_safety_evidence_uses_have_claim_specific_niosh_pinpoints():
    expected = {
        "EU-ELECTRICAL_SAFETY_BASICS-A": (
            "CLM-ELECTRICAL_SAFETY_BASICS-A",
            ("Electrical hazards", "Electrical injuries"),
        ),
        "EU-ELECTRICAL_SAFETY_BASICS-B": (
            "CLM-ELECTRICAL_SAFETY_BASICS-B",
            ("Key points", "Qualified vs. unqualified persons", "Recommendations"),
        ),
        "EU-ELECTRICAL_SAFETY_BASICS-C": (
            "CLM-ELECTRICAL_SAFETY_BASICS-C",
            ("Qualified vs. unqualified persons", "does not establish a universal prohibition"),
        ),
    }
    for evidence_id, (claim_id, required_phrases) in expected.items():
        record = json.loads((SLICE / f"{evidence_id}.json").read_text(encoding="utf-8"))
        assert record["record_version"] == "2"
        assert record["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert record["content"]["source_ref"] == {
            "record_id": "SRC-ELECTRICAL_SAFETY_BASICS",
            "version": "1",
        }
        description = record["content"]["material"]["description"]
        for phrase in required_phrases:
            assert phrase in description
        assert record["provenance"]["created_from"] == [{
            "record_id": "SRC-ELECTRICAL_SAFETY_BASICS",
            "version": "1",
        }]
