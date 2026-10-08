from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"

EXPECTED = {
    "ratios-and-percentages": 10,
    "probability-basics": 7,
    "motion-basics": 9,
    "energy-basics": 9,
    "matter-basics": 9,
    "cell-basics": 9,
    "earth-system-basics": 9,
    "anatomy-basics": 9,
    "economics-basics": 9,
    "computing-basics": 9,
}

EXPECTED_SOURCES = {
    "ratios-and-percentages": 2,
}

def test_ten_foundational_domain_slices_are_complete():
    for slug, expected_count in EXPECTED.items():
        records_dir = CONTENT / slug / "records"
        records = [json.loads(p.read_text(encoding="utf-8")) for p in records_dir.glob("*.json")]
        assert len(records) == expected_count, slug
        types = {r["record_type"] for r in records}
        assert {"source", "claim", "evidence_use", "context", "scope"} <= types
        source_ids = {r["record_id"] for r in records if r["record_type"] == "source"}
        assert len(source_ids) == EXPECTED_SOURCES.get(slug, 1)
        for claim in [r for r in records if r["record_type"] == "claim"]:
            assert claim["provenance"]["created_from"][0]["record_id"] in source_ids
            evidence = [
                r for r in records
                if r["record_type"] == "evidence_use"
                and r["content"]["claim_ref"]["record_id"] == claim["record_id"]
            ]
            assert evidence
            assert all(e["content"]["source_ref"]["record_id"] in source_ids for e in evidence)
