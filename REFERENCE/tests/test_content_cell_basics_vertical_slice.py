from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "cell-basics" / "records"

def test_cell_basics_slice_is_complete():
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

def test_cell_basics_evidence_uses_have_claim_specific_openstax_pinpoints():
    expected = {
        "EU-CELL_BASICS-A": ("CLM-CELL_BASICS-A", "4-1-studying-cells", "basic building blocks"),
        "EU-CELL_BASICS-B": ("CLM-CELL_BASICS-B", "4-2-prokaryotic-cells", "4-3-eukaryotic-cells"),
    }
    records = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    for eu_id, (claim_id, *markers) in expected.items():
        eu = records[eu_id]
        assert eu["record_version"] == "2"
        assert eu["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert eu["content"]["source_ref"] == {"record_id": "SRC-CELL_BASICS", "version": "1"}
        assert eu["content"]["evidence_role"] == "supports"
        description = eu["content"]["material"]["description"]
        for marker in markers:
            assert marker in description
    assert records["CLM-CELL_BASICS-A"]["content"]["statement"] == "Клетка является основной структурной и функциональной единицей живых организмов."
    assert records["CLM-CELL_BASICS-B"]["content"]["statement"] == "Прокариотические клетки не имеют мембранного ядра, тогда как эукариотические клетки имеют ядро."
