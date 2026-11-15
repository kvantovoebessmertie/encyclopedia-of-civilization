from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "political-science-basics" / "records"

def test_political_science_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 1
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"] == "evidence_use")

def test_political_science_evidence_uses_have_claim_specific_openstax_pinpoints():
    expected = {
        "EU-POLITICAL_SCIENCE_BASICS-B": ("CLM-POLITICAL_SCIENCE_BASICS-B", "1-5-empirical-political-science"),
        "EU-POLITICAL_SCIENCE_BASICS-C": ("CLM-POLITICAL_SCIENCE_BASICS-C", "1-4-normative-political-science"),
    }
    records = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    for eu_id, (claim_id, marker) in expected.items():
        eu = records[eu_id]
        assert eu["record_version"] == "2"
        assert eu["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert eu["content"]["source_ref"] == {"record_id": "SRC-POLITICAL_SCIENCE_BASICS", "version": "1"}
        description = eu["content"]["material"]["description"]
        assert marker in description
        assert "1-5-empirical-political-science" in description
    assert records["CLM-POLITICAL_SCIENCE_BASICS-B"]["content"]["statement"] == "Эмпирический подход в политической науке использует наблюдаемые данные и проверяемые свидетельства для изучения политических явлений."
    assert records["CLM-POLITICAL_SCIENCE_BASICS-C"]["content"]["statement"] == "Политический анализ различает описательные вопросы о том, что происходит, и нормативные вопросы о том, что должно происходить."
