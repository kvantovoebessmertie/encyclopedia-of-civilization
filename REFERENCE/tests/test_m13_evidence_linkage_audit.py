from REFERENCE.m13_evidence_linkage_audit import audit_records, normalize_id
import json
from pathlib import Path


def rec(path, record_id, record_type, content=None):
    return {
        "path": path,
        "record_id": record_id,
        "record_type": record_type,
        "data": {"record_type": record_type, "record_id": record_id, "content": content or {}},
        "error": "",
    }


def test_normalization_only_ignores_id_separators():
    assert normalize_id("CLM-WATER_TREATMENT-A") == normalize_id("CLM_WATER-TREATMENT_A")
    assert normalize_id("CLM-WATER-A") != normalize_id("CLM-WATER-B")


def test_evidence_use_flags_generic_description_and_keeps_links_explicit():
    records = [
        rec("CONTENT/x/records/CLM-X.json", "CLM-X", "claim"),
        rec("CONTENT/x/records/SRC-X.json", "SRC-X", "source"),
        rec("CONTENT/x/records/EU-X.json", "EU-X", "evidence_use", {
            "claim_ref": {"record_id": "CLM-X", "version": "1"},
            "source_ref": {"record_id": "SRC-X", "version": "1"},
            "evidence_role": "supports",
            "material": {"description": "Источник используется для представления утверждения без вывода за пределы указанного материала."},
        }),
    ]
    findings = audit_records(records)
    assert any(f["finding"] == "generic_material_description" for f in findings)
    assert not any(f["finding"] in {"unresolved_claim_ref", "unresolved_source_ref"} for f in findings)


def test_evidence_use_flags_broken_references_and_filename_aliases():
    records = [
        rec("CONTENT/x/records/CLM-A.json", "CLM-X-A", "claim"),
        rec("CONTENT/x/records/EU-X.json", "EU-X", "evidence_use", {
            "claim_ref": {"record_id": "MISSING-CLAIM", "version": "1"},
            "source_ref": {"record_id": "MISSING-SOURCE", "version": "1"},
            "evidence_role": "supports",
            "material": {"description": "Specific section 2.1 supports the claim."},
        }),
    ]
    findings = audit_records(records)
    kinds = {f["finding"] for f in findings}
    assert "filename_internal_id_mismatch" in kinds
    assert "unresolved_claim_ref" in kinds
    assert "unresolved_source_ref" in kinds



def test_chemical_water_do_not_drink_evidence_matches_claim_and_cdc_guidance():
    root = Path(__file__).resolve().parents[2]
    records_dir = root / "CONTENT" / "vertical-slices" / "chemical-water-advisory" / "records"

    def load(record_id):
        return json.loads((records_dir / f"{record_id}.json").read_text(encoding="utf-8"))

    claim = load("CLM-CHEM-WATER-NO-DRINK")
    evidence = load("EU-CHEM-WATER-NO-DRINK")
    source = load("SRC-CDC-CHEMICAL-WATER-ADVISORY-2024")

    assert evidence["content"]["claim_ref"]["record_id"] == claim["record_id"]
    assert evidence["content"]["source_ref"]["record_id"] == source["record_id"]
    assert evidence["content"]["evidence_role"] == "supports"
    assert "cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html" in source["content"]["external_ref"]["uri"]

    description = evidence["content"]["material"]["description"].casefold()
    assert "do not drink water advisory" in description
    assert "бутилированную воду" in description
    assert "приготовления пищи" in description
    assert "текстом уведомления местных властей" in description
    assert "кипячение не удаляет химические загрязнители" not in description
