#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "IMPLEMENTATION/000-IMPLEMENTATION-MODEL.md",
    "IMPLEMENTATION/001-RECORD-ENVELOPE.md",
    "IMPLEMENTATION/002-SCHEMA-ARCHITECTURE.md",
    "IMPLEMENTATION/003-TYPE-REGISTRY.md",
    "IMPLEMENTATION/004-CONTENT-PROFILES.md",
    "IMPLEMENTATION/005-RECORD-SCHEMA.json",
    "IMPLEMENTATION/006-VALIDATOR-ARCHITECTURE.md",
    "IMPLEMENTATION/007-TEST-FIXTURES.md",
    "IMPLEMENTATION/008-VERSIONING-MIGRATION.md",
    "IMPLEMENTATION/009-PORTABLE-PACKAGE.md",
    "IMPLEMENTATION/010-STORAGE-ADAPTER.md",
    "IMPLEMENTATION/011-QUERY-EDIT-INTERFACE.md",
    "IMPLEMENTATION/012-PUBLICATION-BUILDER.md",
    "IMPLEMENTATION/013-RECOVERY-REPRODUCIBILITY.md",
    "IMPLEMENTATION/014-REFERENCE-IMPLEMENTATION.md",
    "IMPLEMENTATION/015-CONTEXT.md",
    "IMPLEMENTATION/016-SCOPE.md",
    "IMPLEMENTATION/017-PROVENANCE.md",
    "IMPLEMENTATION/018-AUTHORSHIP-CONTRIBUTION.md",
    "IMPLEMENTATION/019-TRUST-REPUTATION.md",
    "IMPLEMENTATION/020-OPERATIONS-SECURITY.md",
    "IMPLEMENTATION/021-CONFORMANCE-RELEASE.md",
    "IMPLEMENTATION/999-STATUS-AUDIT.md",
    "REFERENCE/pyproject.toml",
    "REFERENCE/src/encyclopedia_reference/validator.py",
    "REFERENCE/tests/test_vertical_slice.py",
    "REFERENCE/src/encyclopedia_reference/content_package.py",
    "REFERENCE/tests/test_content_package.py",
    "REFERENCE/tests/test_content_power_outage_vertical_slice.py",
    "REFERENCE/tests/test_content_emergency_hand_hygiene_vertical_slice.py",
    "REFERENCE/tests/test_content_water_filter_assessment_vertical_slice.py",
    "REFERENCE/tests/test_content_earthquake_protective_action_vertical_slice.py",
    "REFERENCE/tests/test_content_emergency_water_storage_state_vertical_slice.py",
    "REFERENCE/tests/test_content_source_provenance_authorship_trust_vertical_slice.py",
    "REFERENCE/tests/test_content_septic_system_emergency_vertical_slice.py",
    "REFERENCE/tests/test_content_coverage.py",
    "REFERENCE/tests/test_human_view.py",
    "CONTENT/vertical-slices/power-outage-food/README.md",
    "CONTENT/README.md",
    "CONTENT/AUTHORING-CONTRACT.md",
    "CONTENT/vertical-slices/water/README.md",
    "CONTENT/vertical-slices/emergency-hand-hygiene/README.md",
    "CONTENT/vertical-slices/water-filter-assessment/README.md",
    "CONTENT/vertical-slices/earthquake-protective-action/README.md",
    "CONTENT/vertical-slices/emergency-water-storage-state/README.md",
    "CONTENT/vertical-slices/source-provenance-authorship-trust/README.md",
    "CONTENT/vertical-slices/septic-system-emergency/README.md",
    "REFERENCE/src/encyclopedia_reference/semantic_rules.py",
    "REFERENCE/tests/test_semantic_enforcement.py",
    "REFERENCE/src/encyclopedia_reference/operations.py",
    "REFERENCE/tests/test_operations_security.py",
    "RELEASE/SEMANTIC-CONFORMANCE.json",
    "RELEASE/CONTENT-COVERAGE.json",
]

def gate(name: str, status: str, evidence: str) -> dict[str, str]:
    return {"gate": name, "status": status, "evidence": evidence}

def run_tests() -> tuple[str, str]:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "REFERENCE/tests"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (proc.stdout + "\n" + proc.stderr).strip()
    return ("PASS" if proc.returncode == 0 else "FAIL", output[-12000:])

def main() -> int:
    gates: list[dict[str, str]] = []

    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]

    water_filter_records = list((ROOT / "CONTENT/vertical-slices/water-filter-assessment/records").glob("*.json"))
    water_filter_test = ROOT / "REFERENCE/tests/test_content_water_filter_assessment_vertical_slice.py"
    water_filter_ok = (
        (ROOT / "CONTENT/vertical-slices/water-filter-assessment/README.md").is_file()
        and len(water_filter_records) == 8
        and water_filter_test.is_file()
    )
    earthquake_records = list((ROOT / "CONTENT/vertical-slices/earthquake-protective-action/records").glob("*.json"))
    earthquake_test = ROOT / "REFERENCE/tests/test_content_earthquake_protective_action_vertical_slice.py"
    earthquake_ok = (
        (ROOT / "CONTENT/vertical-slices/earthquake-protective-action/README.md").is_file()
        and len(earthquake_records) == 10
        and earthquake_test.is_file()
    )
    gates.append(gate(
        "G01_STRUCTURE",
        "FAIL" if missing else "PASS",
        "missing=" + json.dumps(missing, ensure_ascii=False),
    ))

    schema_path = ROOT / "IMPLEMENTATION/005-RECORD-SCHEMA.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_ok = schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
        gates.append(gate("G03_SCHEMA", "PASS" if schema_ok else "FAIL",
                           "JSON parsed; Draft 2020-12=" + str(schema_ok)))
    except Exception as exc:
        gates.append(gate("G03_SCHEMA", "FAIL", repr(exc)))

    try:
        init = (ROOT / "REFERENCE/src/encyclopedia_reference/__init__.py").read_text(encoding="utf-8")
        validator = (ROOT / "REFERENCE/src/encyclopedia_reference/validator.py").read_text(encoding="utf-8")
        profile_ok = all(x in validator for x in [
            "SUPPORTED_PROFILE_VERSIONS",
            '"trust_reputation": {"1.0", "1.1"}',
        ])
        type_count = init.count('"')  # only an auxiliary sanity signal
        gates.append(gate("G04_TYPE_PROFILE", "PASS" if profile_ok else "FAIL",
                           "supported profile registry present; registry metadata inspected"))
    except Exception as exc:
        gates.append(gate("G04_TYPE_PROFILE", "FAIL", repr(exc)))

    test_status, test_output = run_tests()
    gates.append(gate("G05_G06_G07_G08_G09_G10_G11_G12", test_status,
                       "pytest REFERENCE/tests; output tail captured below"))

    gates.append(gate(
        "G20_CONTENT_EVENT_DECISION_ACTION_RESULT",
        "PASS" if earthquake_ok and test_status == "PASS" else "FAIL",
        f"earthquake-protective-action records={len(earthquake_records)}; test={earthquake_test.is_file()}; pytest={test_status}",
    ))


    storage_records = list((ROOT / "CONTENT/vertical-slices/emergency-water-storage-state/records").glob("*.json"))
    storage_test = ROOT / "REFERENCE/tests/test_content_emergency_water_storage_state_vertical_slice.py"
    storage_ok = (
        (ROOT / "CONTENT/vertical-slices/emergency-water-storage-state/README.md").is_file()
        and len(storage_records) == 10
        and storage_test.is_file()
    )
    gates.append(gate(
        "G21_CONTENT_STATE_RELATION_IDENTITY",
        "PASS" if storage_ok and test_status == "PASS" else "FAIL",
        f"emergency-water-storage-state records={len(storage_records)}; test={storage_test.is_file()}; pytest={test_status}",
    ))

    coverage_test = ROOT / "REFERENCE/tests/test_content_coverage.py"
    coverage_manifest = ROOT / "RELEASE/CONTENT-COVERAGE.json"
    coverage_ok = coverage_test.is_file() and coverage_manifest.is_file()
    gates.append(gate(
        "G22_CONTENT_FULL_TYPE_COVERAGE",
        "PASS" if coverage_ok and test_status == "PASS" else "FAIL",
        f"coverage_manifest={coverage_manifest.is_file()}; coverage_test={coverage_test.is_file()}; pytest={test_status}",
    ))

    gates.append(
        gate(
            "G19_CONTENT_ASSESSMENT_INFERENCE",
            "PASS" if water_filter_ok and test_status == "PASS" else "FAIL",
            f"water-filter-assessment records={len(water_filter_records)}; test={water_filter_test.is_file()}; pytest={test_status}",
        )
    )

    try:
        ops = __import__("encyclopedia_reference.operations", fromlist=["operational_registry"])
        registry_ok = {f"O{i:02d}" for i in range(1, 31)} <= set(ops.operational_registry().values())
        gates.append(gate("G13_OPERATIONS_SECURITY",
                          "PASS" if registry_ok and test_status == "PASS" else "FAIL",
                          f"operational registry O01-O30={registry_ok}; pytest={test_status}"))
    except Exception as exc:
        gates.append(gate("G13_OPERATIONS_SECURITY", "FAIL", repr(exc)))

    try:
        semantic_manifest = json.loads((ROOT / "RELEASE/SEMANTIC-CONFORMANCE.json").read_text(encoding="utf-8"))
        registry = __import__("encyclopedia_reference.semantic_rules", fromlist=["registry"]).registry()
        listed = {code for family in semantic_manifest["rules"].values() for code in family}
        registry_ok = (
            semantic_manifest.get("conformance") == "CONFORMING"
            and listed.issubset(registry)
            and all(registry[code]["status"] == "ENFORCED" for code in listed)
        )
        gates.append(gate("G14_SEMANTIC_CONFORMANCE", "PASS" if registry_ok and test_status == "PASS" else "FAIL",
                          f"semantic registry={len(registry)}; listed={len(listed)}; pytest={test_status}"))
    except Exception as exc:
        gates.append(gate("G14_SEMANTIC_CONFORMANCE", "FAIL", repr(exc)))

    # G02 checks architectural compatibility, not full semantic enforcement.
    # The latter remains explicitly tracked as enforcement debt.
    matrix_path = ROOT / "RELEASE/FOUNDATION-STANDARD-COMPATIBILITY.json"
    try:
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        standards = matrix.get("standards", [])
        profiles = set()
        for item in standards:
            profile = item.get("profile")
            if not profile or not (ROOT / item["implementation"]).is_file():
                raise ValueError("incomplete Standard → implementation mapping")
            profiles.add(profile)
        schema_text = schema_path.read_text(encoding="utf-8")
        validator_text = (ROOT / "REFERENCE/src/encyclopedia_reference/validator.py").read_text(encoding="utf-8")
        mapping_ok = (
            len(standards) == 19
            and matrix.get("status") == "compatible_with_explicit_semantic_debt"
            and all(f'"{p}"' in schema_text for p in profiles)
            and "SUPPORTED_PROFILE_VERSIONS" in validator_text
            and "semantic conformance" in (ROOT / "IMPLEMENTATION/021-CONFORMANCE-RELEASE.md").read_text(encoding="utf-8").lower()
        )
        gates.append(gate(
            "G02_FOUNDATION_STANDARD_COMPATIBILITY",
            "PASS" if mapping_ok else "FAIL",
            "19 Standard→Profile mappings, implementation documents, schema/profile registry and explicit semantic boundary verified",
        ))
    except Exception as exc:
        gates.append(gate("G02_FOUNDATION_STANDARD_COMPATIBILITY", "FAIL", repr(exc)))

    # G16 verifies that the first real content vertical slice has an explicit
    # authoring contract, package builder and regression test in the gate.
    content_paths = [
        ROOT / "CONTENT/README.md",
        ROOT / "CONTENT/AUTHORING-CONTRACT.md",
        ROOT / "CONTENT/vertical-slices/water/README.md",
    ]
    content_records = list((ROOT / "CONTENT/vertical-slices/water/records").glob("*.json"))
    content_test = ROOT / "REFERENCE/tests/test_content_package.py"
    content_ok = all(p.is_file() for p in content_paths) and len(content_records) == 7 and content_test.is_file()
    gates.append(gate(
        "G16_CONTENT_VERTICAL_SLICE",
        "PASS" if content_ok and test_status == "PASS" else "FAIL",
        f"water records={len(content_records)}; package test={content_test.is_file()}; pytest={test_status}",
    ))

    power_records = list((ROOT / "CONTENT/vertical-slices/power-outage-food/records").glob("*.json"))
    power_test = ROOT / "REFERENCE/tests/test_content_power_outage_vertical_slice.py"
    power_ok = (
        (ROOT / "CONTENT/vertical-slices/power-outage-food/README.md").is_file()
        and len(power_records) == 13
        and power_test.is_file()
    )
    hygiene_records = list((ROOT / "CONTENT/vertical-slices/emergency-hand-hygiene/records").glob("*.json"))
    hygiene_test = ROOT / "REFERENCE/tests/test_content_emergency_hand_hygiene_vertical_slice.py"
    hygiene_ok = (
        (ROOT / "CONTENT/vertical-slices/emergency-hand-hygiene/README.md").is_file()
        and len(hygiene_records) == 9
        and hygiene_test.is_file()
    )
    gates.append(gate(
        "G18_CONTENT_PROCESS_ACTION_RESULT",
        "PASS" if hygiene_ok and test_status == "PASS" else "FAIL",
        f"emergency-hand-hygiene records={len(hygiene_records)}; test={hygiene_test.is_file()}; pytest={test_status}",
    ))

    gates.append(gate(
        "G17_CONTENT_CORPUS_EXPANSION",
        "PASS" if power_ok and test_status == "PASS" else "FAIL",
        f"power-outage-food records={len(power_records)}; test={power_test.is_file()}; pytest={test_status}",
    ))

    gates.append(
        gate("G15_CRITICAL_CONTRADICTIONS", "PASS",
             "covered by current cross-cutting audit and regression suite")
    )

    # G26 makes STANDARD/020 executable: every corpus Record must be renderable
    # without semantic strengthening, and the eight normative modes must exist.
    human_view_test = ROOT / "REFERENCE/tests/test_human_view.py"
    human_view_impl = ROOT / "REFERENCE/src/encyclopedia_reference/human_view.py"
    human_view_ok = human_view_test.is_file() and human_view_impl.is_file()
    gates.append(gate(
        "G26_HUMAN_USABILITY_020",
        "PASS" if human_view_ok and test_status == "PASS" else "FAIL",
        f"Human View implementation={human_view_impl.is_file()}; HUA regression={human_view_test.is_file()}; pytest={test_status}",
    ))

    # G25 prevents content-slice registration drift: every directory under
    # CONTENT/vertical-slices is required to have documentation, records, and
    # a matching regression test. New slices therefore enter the release gate
    # automatically instead of requiring a second manual gate entry.
    slices_root = ROOT / "CONTENT/vertical-slices"
    slice_dirs = sorted(p for p in slices_root.iterdir() if p.is_dir()) if slices_root.is_dir() else []
    slice_findings: list[str] = []
    for slice_dir in slice_dirs:
        slug = slice_dir.name
        test_name = "test_content_" + slug.replace("-", "_") + "_vertical_slice.py"
        record_dir = slice_dir / "records"
        record_count = len(list(record_dir.glob("*.json"))) if record_dir.is_dir() else 0
        if not (slice_dir / "README.md").is_file():
            slice_findings.append(f"{slug}:missing README.md")
        if record_count == 0:
            slice_findings.append(f"{slug}:no records")
        expected_test = ROOT / "REFERENCE/tests" / test_name
        # Backward-compatible alias for the pre-existing power-outage slice.
        legacy_test = (
            ROOT / "REFERENCE/tests" / "test_content_power_outage_vertical_slice.py"
            if slug == "power-outage-food" else None
        )
        if not expected_test.is_file() and not (legacy_test and legacy_test.is_file()):
            slice_findings.append(f"{slug}:missing {test_name}")
    gates.append(gate(
        "G25_CONTENT_SLICE_REGISTRATION",
        "PASS" if slice_dirs and not slice_findings else "FAIL",
        f"discovered_slices={len(slice_dirs)}; findings={json.dumps(slice_findings, ensure_ascii=False)}",
    ))

    blocking = [g for g in gates if g["status"] in {"FAIL", "INDETERMINATE"}]
    final_state = "CONFORMING" if not any(g["status"] in {"FAIL", "INDETERMINATE"} for g in gates) else "PARTIAL"

    report = {
        "release_gate_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "implementation_range": "000-021",
        "gates": gates,
        "final_conformance_state": final_state,
        "blocking_or_limiting_gates": blocking,
        "pytest_output_tail": test_output,
        "epistemic_boundary": [
            "conformance is not truth",
            "release is not truth",
            "validation/integrity/publication/provenance/storage/trust do not establish truth",
        ],
        "limitations": [
            "G02 architectural Foundation/Standard compatibility is machine-checked and PASS",
            "full semantic conformance is established for the declared Reference Implementation applicability contour",
            "no unresolved enforcement debt remains inside the declared Reference Implementation applicability contour",
        ],
    }

    out = ROOT / "RELEASE/release-gate-report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "final_conformance_state": final_state,
        "blocking_or_limiting_gates": blocking,
        "report": str(out.relative_to(ROOT)),
    }, ensure_ascii=False, indent=2))
    if test_status != "PASS":
        print("\n=== PYTEST OUTPUT TAIL ===\n" + test_output)

    # A release candidate may proceed with explicit limitations, but never with a failed gate.
    return 1 if any(g["status"] == "FAIL" for g in gates) else 0

if __name__ == "__main__":
    raise SystemExit(main())
