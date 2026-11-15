from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "energy-basics" / "records"


def test_energy_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {
        record["record_type"] for record in records
    }
    sources = [record for record in records if record["record_type"] == "source"]
    assert len(sources) == 1
    source_ids = {record["record_id"] for record in sources}
    for claim in [record for record in records if record["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in source_ids
        assert any(
            evidence["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and evidence["content"]["source_ref"]["record_id"] in source_ids
            for evidence in records
            if evidence["record_type"] == "evidence_use"
        )


def test_energy_basics_openstax_source_identity_and_claim_specific_pinpoints():
    records = {
        record["record_id"]: record
        for record in (json.loads(path.read_text(encoding="utf-8")) for path in SLICE.glob("*.json"))
    }
    source = records["SRC-ENERGY_BASICS"]
    assert source["record_version"] == "2"
    assert source["content"]["source_identity"] == (
        "OpenStax, College Physics, Chapter 7, “Work, Energy, and Energy Resources”"
    )
    assert source["content"]["external_ref"]["uri"] == (
        "https://openstax.org/books/college-physics/pages/7-introduction-to-work-energy-and-energy-resources"
    )

    expected_statements = {
        "CLM-ENERGY_BASICS-A": "Кинетическая энергия связана с движением тела и зависит от его массы и скорости.",
        "CLM-ENERGY_BASICS-B": "Потенциальная энергия описывает энергию, связанную с положением или конфигурацией системы.",
        "CLM-ENERGY_BASICS-C": "Работа является способом передачи энергии посредством действия силы на перемещение.",
    }
    expected_locators = {
        "EU-ENERGY_BASICS-A": ("CLM-ENERGY_BASICS-A", "§7.2", "kinetic energy"),
        "EU-ENERGY_BASICS-B": ("CLM-ENERGY_BASICS-B", "§§7.3", "§7.4"),
        "EU-ENERGY_BASICS-C": ("CLM-ENERGY_BASICS-C", "§7.1", "force"),
    }
    for claim_id, statement in expected_statements.items():
        claim = records[claim_id]
        assert claim["record_version"] == "1"
        assert claim["content"]["statement"] == statement

    for evidence_id, (claim_id, locator_a, locator_b) in expected_locators.items():
        evidence = records[evidence_id]
        assert evidence["record_version"] == "2"
        assert evidence["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert evidence["content"]["source_ref"] == {"record_id": "SRC-ENERGY_BASICS", "version": "2"}
        assert evidence["provenance"]["created_from"][0] == {
            "record_id": "SRC-ENERGY_BASICS",
            "version": "2",
        }
        description = evidence["content"]["material"]["description"]
        assert locator_a in description
        assert locator_b in description
