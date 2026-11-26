from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "soil-basics" / "records"


def test_soil_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 10
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}

    source_records = [r for r in records if r["record_type"] == "source"]
    assert len(source_records) == 2
    assert {r["record_id"] for r in source_records} == {"SRC-SOIL_BASICS"}
    source_versions = {r["record_version"]: r for r in source_records}
    assert set(source_versions) == {"1", "2"}
    assert source_versions["1"]["content"]["external_ref"]["uri"] == (
        "https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/soils"
    )
    assert source_versions["2"]["content"]["external_ref"]["uri"] == (
        "https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil"
    )

    sources = {r["record_id"] for r in source_records}
    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(claims) == 3
    assert len(evidence) == 3
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(
            e["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and e["content"]["source_ref"]["record_id"] in sources
            for e in evidence
        )
