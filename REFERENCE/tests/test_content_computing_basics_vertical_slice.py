from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "computing-basics" / "records"

def test_computing_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert len(sources) == 1
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(
            e["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and e["content"]["source_ref"]["record_id"] in sources
            for e in records if e["record_type"] == "evidence_use"
        )

def test_computing_basics_evidence_uses_have_claim_specific_openstax_pinpoints():
    expected = {
        "EU-COMPUTING_BASICS-A": ("CLM-COMPUTING_BASICS-A", "5-1-computer-systems-organization"),
        "EU-COMPUTING_BASICS-B": ("CLM-COMPUTING_BASICS-B", "3-2-algorithm-design-and-discovery"),
        "EU-COMPUTING_BASICS-C": ("CLM-COMPUTING_BASICS-C", "Data Storage Inside a Computer"),
    }
    records = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    for eu_id, (claim_id, marker) in expected.items():
        eu = records[eu_id]
        assert eu["record_version"] == "2"
        assert eu["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert eu["content"]["source_ref"] == {"record_id": "SRC-COMPUTING_BASICS", "version": "1"}
        assert marker in eu["content"]["material"]["description"]
    assert records["CLM-COMPUTING_BASICS-A"]["content"]["statement"] == "Компьютерная система обрабатывает данные по заданным правилам, используя аппаратные и программные компоненты."
    assert records["CLM-COMPUTING_BASICS-B"]["content"]["statement"] == "Алгоритм задаёт последовательность шагов для решения задачи или преобразования входных данных."
    assert records["CLM-COMPUTING_BASICS-C"]["content"]["statement"] == "Данные и инструкции могут быть представлены в цифровой форме, которую обрабатывает вычислительная система."
