from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "wastewater-basics" / "records"


def test_wastewater_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 13
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}

    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 2

    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(claims) == 3
    assert len(evidence) == 6

    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        linked_sources = {
            e["content"]["source_ref"]["record_id"]
            for e in evidence
            if e["content"]["claim_ref"]["record_id"] == claim["record_id"]
        }
        assert linked_sources == sources
