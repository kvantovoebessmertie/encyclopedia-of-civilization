from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "asset-management-basics" / "records"
SOURCE_ID = "SRC-ASSET_MANAGEMENT_BASICS"
SOURCE_URI = "https://www.iso.org/standard/83054.html"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]


def test_asset_management_basics_slice_is_complete():
    records = _records()
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert sources == {SOURCE_ID}
    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(claims) == 3 and len(evidence) == 3
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(
            e["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and e["content"]["source_ref"]["record_id"] in sources
            for e in evidence
        )


def test_asset_management_source_identity_and_versioned_evidence_fit():
    records = _records()
    by_id = {r["record_id"]: r for r in records}
    source = by_id[SOURCE_ID]
    assert source["record_version"] == "2"
    assert source["content"]["source_identity"] == (
        "International Organization for Standardization — ISO 55001:2024 — Asset management — Asset management system — Requirements"
    )
    assert source["content"]["external_ref"]["uri"] == SOURCE_URI

    expected = {
        "A": "supports the Claim’s lifecycle/value/risk/objectives framing",
        "B": "The Claim also mentions “opportunities”, which this cited overview does not expressly establish",
        "C": "identifies an asset-management policy, objectives, design and implementation of a management system",
    }
    for letter, phrase in expected.items():
        eu = by_id[f"EU-ASSET_MANAGEMENT_BASICS-{letter}"]
        assert eu["record_version"] == "2"
        assert eu["provenance"]["created_from"] == [{"record_id": SOURCE_ID, "version": "2"}]
        assert eu["content"]["source_ref"] == {"record_id": SOURCE_ID, "version": "2"}
        assert phrase in eu["content"]["material"]["description"]
