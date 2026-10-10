from REFERENCE.m13_evidence_linkage_audit import audit_records, normalize_id


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
