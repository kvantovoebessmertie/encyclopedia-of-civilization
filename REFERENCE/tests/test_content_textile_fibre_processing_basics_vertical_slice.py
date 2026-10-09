from __future__ import annotations
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "textile-fibre-processing-basics" / "records"

def test_textile_fibre_processing_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(SLICE.glob("*.json"))]
    assert len(records) == 18
    by_type = {}
    for record in records:
        by_type.setdefault(record["record_type"], []).append(record)
    assert len(by_type["source"]) == 3
    assert len(by_type["claim"]) == 4
    assert len(by_type["evidence_use"]) == 9
    assert len(by_type["context"]) == 1
    assert len(by_type["scope"]) == 1
    sources = {r["record_id"] for r in by_type["source"]}
    claims = {r["record_id"] for r in by_type["claim"]}
    links = {(e["content"]["claim_ref"]["record_id"], e["content"]["source_ref"]["record_id"]) for e in by_type["evidence_use"]}
    assert {c for c, _ in links} == claims
    assert all(s in sources for _, s in links)
    for claim in by_type["claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] for e in by_type["evidence_use"])
    for record_type in ("context", "scope"):
        assert by_type[record_type][0]["content"]["target_ref"]["record_id"] in claims
    # Human View regression: evidence descriptions stay readable in Russian.
    assert all(re.search(r"[А-Яа-яЁё]", e["content"]["material"]["description"]) for e in by_type["evidence_use"])
    # Substantive regression: these claims must remain within the accessible source scope.
    claim_statements = {c["record_id"]: c["content"]["statement"] for c in by_type["claim"]}
    assert claim_statements["CLM-TEXTILE_FIBRE_PROCESSING_BASICS-B"] == "Перед прядением растительные волокна могут проходить подготовку, включая выравнивание или чесание; набор операций зависит от вида и свойств волокна."
    assert claim_statements["CLM-TEXTILE_FIBRE_PROCESSING_BASICS-C"] == "В описаниях растительных волокон формирование нити включает соединение и скручивание волокон; прядение и последующая обработка влияют на свойства нити."
    assert claim_statements["CLM-TEXTILE_FIBRE_PROCESSING_BASICS-D"] == "Растительные волокна различаются по свойствам и способам обработки; пригодность полученной нити для конкретного изделия следует оценивать с учётом его требований."
