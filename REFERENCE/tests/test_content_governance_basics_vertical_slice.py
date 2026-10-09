from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "governance-basics" / "records"


def test_governance_basics_slice_is_complete_and_human_facing_text_is_russian():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 11
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert "SRC-GOVERNANCE_BASICS-WGI-2026" in sources
    assert any(r["record_id"] == "EU-GOVERNANCE_BASICS-C-WGI" and r["content"]["claim_ref"]["record_id"] == "CLM-GOVERNANCE_BASICS-C" and r["content"]["source_ref"]["record_id"] == "SRC-GOVERNANCE_BASICS-WGI-2026" for r in records)
    assert len(sources) == 2

    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    for claim in claims.values():
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)

    assert "Публичное управление" in claims["CLM-GOVERNANCE_BASICS-A"]["content"]["statement"]
    assert "взаимосвязанные ценности" in claims["CLM-GOVERNANCE_BASICS-B"]["content"]["statement"]
    assert "неопределённости" in claims["CLM-GOVERNANCE_BASICS-C"]["content"]["statement"]
    assert all(any(ch in claim["content"]["statement"] for ch in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for claim in claims.values())

    scope = next(r for r in records if r["record_type"] == "scope")
    assert "не задаёт универсальную классификацию" in scope["content"]["scope_content"]
    assert all(any(ch in e["content"]["material"]["description"] for ch in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for e in evidence)
