from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "behavioral-biology-basics" / "records"
SOURCE_ID = "SRC-BEHAVIORAL_BIOLOGY_BASICS"
SOURCE_URI = "https://openstax.org/books/biology-2e/pages/45-7-behavioral-biology-proximate-and-ultimate-causes-of-behavior"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]


def test_behavioral_biology_basics_slice_is_complete():
    records = _records()
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert sources == {SOURCE_ID}
    claims = [r for r in records if r["record_type"] == "claim"]
    for claim in claims:
        assert claim["record_version"] == "2"
        assert claim["provenance"]["created_from"] == [{"record_id": SOURCE_ID, "version": "2"}]
    claim_ids = {c["record_id"] for c in claims}
    for record in records:
        if record["record_type"] in {"context", "scope"}:
            assert record["record_version"] == "2"
            assert record["content"]["target_ref"]["record_id"] in claim_ids
            assert record["content"]["target_ref"]["version"] == "2"
        if record["record_type"] == "evidence_use":
            assert record["record_version"] == "3"
            assert record["content"]["claim_ref"]["record_id"] in claim_ids
            assert record["content"]["claim_ref"]["version"] == "2"
        assert any(
            e["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and e["content"]["source_ref"]["record_id"] in sources
            for e in records if e["record_type"] == "evidence_use"
        )


def test_behavioral_biology_source_identity_and_versioned_evidence_fit():
    records = _records()
    by_id = {r["record_id"]: r for r in records}
    source = by_id[SOURCE_ID]
    assert source["record_version"] == "2"
    assert source["content"]["source_identity"] == (
        "OpenStax, Biology 2e, §45.7 — Behavioral Biology: Proximate and Ultimate Causes of Behavior (Rice University)"
    )
    assert source["content"]["external_ref"]["uri"] == SOURCE_URI

    expected = {
        "A": "defines behaviour as a change in an organism’s activity in response to a stimulus",
        "B": "innate behaviours have a strong genetic component",
        "C": "does not establish the methodological rule",
    }
    for letter, phrase in expected.items():
        eu = by_id[f"EU-BEHAVIORAL_BIOLOGY_BASICS-{letter}"]
        assert eu["record_version"] == "2"
        assert eu["provenance"]["created_from"] == [{"record_id": SOURCE_ID, "version": "2"}]
        assert eu["content"]["source_ref"] == {"record_id": SOURCE_ID, "version": "2"}
        assert phrase in eu["content"]["material"]["description"]
    assert "only partially supported" in by_id["EU-BEHAVIORAL_BIOLOGY_BASICS-C"]["content"]["material"]["description"]
