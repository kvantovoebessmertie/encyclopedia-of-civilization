from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "statistics-basics" / "records"


def test_statistics_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 13
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 3
    assert "SRC-OPENSTAX-STATISTICS-EXPERIMENTAL-DESIGN" in sources

    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    for claim in claims.values():
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)

    by_id = {r["record_id"]: r for r in evidence}
    assert "предпосыл" in by_id["EU-STATISTICS_BASICS-B"]["content"]["material"]["description"]
    assert "эксперимент" in by_id["EU-STATISTICS_BASICS-C"]["content"]["material"]["description"]
    assert by_id["EU-STATISTICS_BASICS-C-OPENSTAX"]["content"]["source_ref"]["record_id"] == "SRC-OPENSTAX-STATISTICS-EXPERIMENTAL-DESIGN"
    assert "случайное распределение" in by_id["EU-STATISTICS_BASICS-C-OPENSTAX"]["content"]["material"]["description"]
    assert all("Источник используется для представления утверждения" not in e["content"]["material"]["description"] for e in evidence if e["content"]["claim_ref"]["record_id"] in {"CLM-STATISTICS_BASICS-B", "CLM-STATISTICS_BASICS-C"})
