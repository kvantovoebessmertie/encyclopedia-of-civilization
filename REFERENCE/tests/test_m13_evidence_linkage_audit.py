from REFERENCE.m13_evidence_linkage_audit import audit_records, normalize_id
import json
from pathlib import Path


def rec(path, record_id, record_type, content=None):
    return {
        "path": path,
        "record_id": record_id,
        "record_type": record_type,
        "data": {"record_type": record_type, "record_id": record_id, "record_version": "1", "content": content or {}},
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
    assert "по конкретному уведомлению местных властей" in description
    assert "кипячение не удаляет химические загрязнители" not in description


def test_generator_co_emergency_evidence_matches_cdc_guidance_without_unsupported_reentry_clause():
    root = Path(__file__).resolve().parents[2]
    records_dir = root / "CONTENT" / "vertical-slices" / "generator-carbon-monoxide-safety" / "records"

    def load(record_id):
        return json.loads((records_dir / f"{record_id}.json").read_text(encoding="utf-8"))

    claim = load("CLM-GENERATOR-CO-ALARM-EMERGENCY")
    evidence = load("EU-GENERATOR-CO-ALARM-EMERGENCY")
    source = load("SRC-CDC-GENERATOR-CO-2026")

    assert evidence["content"]["claim_ref"]["record_id"] == claim["record_id"]
    assert evidence["content"]["source_ref"]["record_id"] == source["record_id"]
    assert evidence["content"]["evidence_role"] == "supports"
    assert "cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html" in source["content"]["external_ref"]["uri"]

    statement = claim["content"]["statement"].casefold()
    description = evidence["content"]["material"]["description"].casefold()
    assert "свежий воздух" in statement
    assert "экстренной медицинской помощью" in statement
    assert "свежий воздух" in description
    assert "экстренной медицинской помощью" in description
    assert "нельзя возвращаться" not in statement
    assert "до проверки безопасности" not in statement


def test_evidence_use_flags_explicit_claim_and_source_version_mismatches():
    records = [
        rec("CONTENT/x/records/CLM-X.json", "CLM-X", "claim"),
        rec("CONTENT/x/records/SRC-X.json", "SRC-X", "source"),
        rec("CONTENT/x/records/EU-X.json", "EU-X", "evidence_use", {
            "claim_ref": {"record_id": "CLM-X", "version": "2"},
            "source_ref": {"record_id": "SRC-X", "version": "3"},
            "evidence_role": "supports",
            "material": {"description": "Specific section 2.1 supports the claim."},
        }),
    ]
    findings = audit_records(records)
    mismatches = {f["finding"] for f in findings}
    assert "claim_ref_version_mismatch" in mismatches
    assert "source_ref_version_mismatch" in mismatches


def test_source_identity_sentence_is_flagged_for_human_review():
    records = [
        rec("CONTENT/x/records/SRC-X.json", "SRC-X", "source", {
            "source_identity": "Криптография использует математические методы для защиты информации.",
            "external_ref": {"uri": "https://www.nist.gov/cryptography"},
        }),
    ]
    findings = audit_records(records)
    assert any(f["finding"] == "source_identity_sentence_candidate" for f in findings)


def test_reused_source_uri_is_flagged_without_asserting_duplicate_identity():
    records = [
        rec("CONTENT/x/records/SRC-A.json", "SRC-A", "source", {
            "source_identity": "Publisher — Topic A",
            "external_ref": {"uri": "https://example.org/shared"},
        }),
        rec("CONTENT/y/records/SRC-B.json", "SRC-B", "source", {
            "source_identity": "Publisher — Topic B",
            "external_ref": {"uri": "https://example.org/shared"},
        }),
    ]
    findings = audit_records(records)
    candidates = [f for f in findings if f["finding"] == "duplicate_source_uri_candidate"]
    assert len(candidates) == 2
    assert all("shared URI does not prove identical source" in f["detail"] for f in candidates)


def test_web_systems_filename_id_mismatches_preserve_exact_record_identity_and_links():
    root = Path(__file__).resolve().parents[2]
    records_dir = root / "CONTENT" / "vertical-slices" / "web-systems-basics" / "records"
    expected = {
        "CLM-A.json": "CLM-WEB_SYSTEMS_BASICS-A",
        "CLM-B.json": "CLM-WEB_SYSTEMS_BASICS-B",
        "CLM-C.json": "CLM-WEB_SYSTEMS_BASICS-C",
        "EU-A.json": "EU-WEB_SYSTEMS_BASICS-A",
        "EU-B.json": "EU-WEB_SYSTEMS_BASICS-B",
        "EU-C.json": "EU-WEB_SYSTEMS_BASICS-C",
    }

    loaded = {
        filename: json.loads((records_dir / filename).read_text(encoding="utf-8"))
        for filename in expected
    }
    for filename, record_id in expected.items():
        assert loaded[filename]["record_id"] == record_id

    for suffix in ("A", "B", "C"):
        claim = loaded[f"CLM-{suffix}.json"]
        evidence = loaded[f"EU-{suffix}.json"]
        source_id = evidence["content"]["source_ref"]["record_id"]
        source_path = records_dir / f"{source_id}.json"
        source = json.loads(source_path.read_text(encoding="utf-8"))

        assert claim["record_type"] == "claim"
        assert evidence["record_type"] == "evidence_use"
        assert evidence["content"]["claim_ref"] == {
            "record_id": claim["record_id"],
            "version": claim["record_version"],
        }
        assert source["record_type"] == "source"
        assert evidence["content"]["source_ref"]["version"] == source["record_version"]
        assert evidence["content"]["evidence_role"] in {"supports", "contradicts"}


def test_m13_authorized_evidence_use_provenance_lineage_corrections():
    root = Path(__file__).resolve().parents[2]
    expected = {
        "international-trade-basics": {
            "EU-INTERNATIONAL_TRADE_BASICS-B": "SRC-INTERNATIONAL_TRADE_BASICS",
        },
        "labor-law-basics": {
            "EU-LABOR_LAW_BASICS-B": "SRC-LABOR_LAW_BASICS",
        },
        "risk-management-basics": {
            "EU-RISK_MANAGEMENT_BASICS-B": "SRC-RISK_MANAGEMENT_BASICS",
            "EU-RISK_MANAGEMENT_BASICS-C": "SRC-RISK_MANAGEMENT_BASICS",
        },
    }

    for slice_name, records in expected.items():
        records_dir = root / "CONTENT" / "vertical-slices" / slice_name / "records"
        for evidence_id, source_id in records.items():
            evidence = json.loads((records_dir / f"{evidence_id}.json").read_text(encoding="utf-8"))
            source = json.loads((records_dir / f"{source_id}.json").read_text(encoding="utf-8"))
            claim_id = evidence["content"]["claim_ref"]["record_id"]
            claim = json.loads((records_dir / f"{claim_id}.json").read_text(encoding="utf-8"))

            assert evidence["record_version"] == "2"
            assert evidence["provenance"]["created_from"] == [
                {"record_id": source_id, "version": "1"}
            ]
            assert evidence["content"]["claim_ref"] == {
                "record_id": claim_id,
                "version": "1",
            }
            assert evidence["content"]["source_ref"] == {
                "record_id": source_id,
                "version": "1",
            }
            assert source["record_version"] == "1"
            assert claim["record_version"] == "1"

    risk_records = root / "CONTENT" / "vertical-slices" / "risk-management-basics" / "records"
    coso_evidence = json.loads((risk_records / "EU-RISK_MANAGEMENT_COSO.json").read_text(encoding="utf-8"))
    assert coso_evidence["record_version"] == "1"
    assert coso_evidence["provenance"]["created_from"] == [
        {"record_id": "SRC-COSO-ERM-RISK-MANAGEMENT", "version": "1"}
    ]


def test_m13_package_29_31_source_fit_additions_are_exact_and_bounded():
    root = Path(__file__).resolve().parents[2]

    def load(slice_name, record_id):
        return json.loads((root / "CONTENT" / "vertical-slices" / slice_name / "records" / f"{record_id}.json").read_text(encoding="utf-8"))

    map_claim = "CLM-MAPS_AND_NAVIGATION_BASICS-C"
    for evidence_id, source_id in [
        ("EU-MAPS_AND_NAVIGATION_BASICS-C-US-TOPO-ACCURACY", "SRC-USGS-US-TOPO-ACCURACY"),
        ("EU-MAPS_AND_NAVIGATION_BASICS-C-US-TOPO-CURRENCY", "SRC-USGS-US-TOPO-CURRENCY"),
    ]:
        evidence = load("maps-and-navigation-basics", evidence_id)
        source = load("maps-and-navigation-basics", source_id)
        assert evidence["content"]["claim_ref"] == {"record_id": map_claim, "version": "1"}
        assert evidence["content"]["source_ref"] == {"record_id": source_id, "version": "1"}
        assert evidence["provenance"]["created_from"] == [{"record_id": source_id, "version": "1"}]
        assert source["record_type"] == "source"

    for slice_name, evidence_id, claim_id, source_id in [
        ("materials-basics", "EU-MATERIALS_BASICS-A-NIST-MSED", "CLM-MATERIALS_BASICS-A", "SRC-NIST-MATERIALS-SCIENCE-ENGINEERING-DIVISION"),
        ("materials-basics", "EU-MATERIALS_BASICS-C-NIST-MECHANICAL-PERFORMANCE", "CLM-MATERIALS_BASICS-C", "SRC-NIST-MECHANICAL-PERFORMANCE-GROUP"),
        ("materials-science-basics", "EU-M5-MATERIALS-SCIENCE-NIST-B", "CLM-MATERIALS_SCIENCE_BASICS-B", "SRC-NIST-MECHANICAL-PERFORMANCE"),
        ("materials-science-basics", "EU-M5-MATERIALS-PERFORMANCE-NIST-D", "CLM-M5-MATERIALS-PERFORMANCE-D", "SRC-NIST-MECHANICAL-PERFORMANCE"),
        ("manufacturing-systems-basics", "EU-MANUFACTURING_SYSTEMS_BASICS-B-SMS", "CLM-MANUFACTURING_SYSTEMS_BASICS-B", "SRC-NIST-SMART-MANUFACTURING-TEST-BED"),
        ("manufacturing-systems-basics", "EU-MANUFACTURING_SYSTEMS_BASICS-C-SMS", "CLM-MANUFACTURING_SYSTEMS_BASICS-C", "SRC-NIST-SMART-MANUFACTURING-TEST-BED"),
        ("manufacturing-systems-basics", "EU-MANUFACTURING_SYSTEMS_BASICS-C-AMS-200-2", "CLM-MANUFACTURING_SYSTEMS_BASICS-C", "SRC-NIST-AMS-200-2"),
    ]:
        evidence = load(slice_name, evidence_id)
        source = load(slice_name, source_id)
        assert evidence["content"]["claim_ref"] == {"record_id": claim_id, "version": "1"}
        assert evidence["content"]["source_ref"] == {"record_id": source_id, "version": "1"}
        assert evidence["content"]["evidence_role"] == "supports"
        assert evidence["provenance"]["created_from"] == [{"record_id": source_id, "version": "1"}]
        assert source["record_type"] == "source"

    nsf = load("materials-science-basics", "EU-M5-MATERIALS-SCIENCE-NSF-B")
    assert nsf["record_version"] == "2"
    assert "does not explicitly name composites" in nsf["content"]["material"]["description"]
    assert "composites" not in nsf["content"]["material"]["description"].split(";")[0].casefold()
