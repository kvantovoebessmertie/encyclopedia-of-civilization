# P4 Water Safety & Resilience — Unified Debt Map — 2026-10-06

## Audit baseline

- P3 CLEAN checkpoint: `8bd1a889e83406a43b9d511b54da233f51e86cc9`
- P4 audit HEAD: `25a67750060e7ca0d5c64dfeb74a0f12873c414e`
- Corpus: 478 vertical slices / 4371 Records / 19 Record types
- P4 target slices: 7

## Confirmed findings

### P4-EVIDENCE-001 — OPEN
**Artifact:** `water-treatment-basics`
**Class:** evidence independence / high-consequence boundary

The slice contains 1 source (WHO) supporting all three claims. The claims concern water-treatment purpose, method selection and the non-universality of treatment. Independent institutional triangulation is warranted before this baseline is reused as high-consequence guidance.

**Required correction:** add genuinely independent evidence where it materially strengthens the claims; do not duplicate the same evidence under another publisher.

### P4-EVIDENCE-002 — OPEN
**Artifact:** `water-infrastructure-basics`
**Class:** evidence independence / infrastructure resilience

The slice contains 1 EPA source supporting all three claims. The claims cover distribution-system structure, contamination risk and system conditions. Independent institutional evidence is warranted for the resilience/reliability boundary.

**Required correction:** add independent evidence only where it materially improves applicability or resilience interpretation.

### P4-EVIDENCE-003 — OPEN
**Artifact:** `water-security-basics`
**Class:** evidence independence / broad systems claim

The slice contains 1 UN-Water source supporting all three broad water-security claims. Independent corroboration is warranted because the claims span access, contamination, disasters, ecosystems and contextual assessment.

**Required correction:** triangulate the substantive baseline without turning the slice into policy advocacy.

### P4-EVIDENCE-004 — OPEN
**Artifact:** `emergency-water-storage-state`
**Class:** evidence independence / emergency practical guidance

The operationally relevant storage-container claim is represented through a single CDC source. The state/relation/identity structure is useful, but the practical storage baseline warrants independent institutional confirmation before higher-consequence reuse.

**Required correction:** add independent evidence if it adds genuine confirmation; preserve the existing state/identity semantics.

### P4-DOC-005 — OPEN
**Artifacts:** `emergency-water-storage-state/README.md`, `water-filter-assessment/README.md`
**Class:** documentation drift

The emergency-water-storage README declares 9 Records while the slice contains 10. The water-filter-assessment README describes 7 Records while the slice contains 11.

**Required correction:** synchronize documentation to actual topology without altering content merely for presentation.

### P4-DOC-006 — OPEN
**Artifact:** `water-quality-basics/README.md`
**Class:** documentation completeness

The README gives only the canonical pattern and does not state the actual two-source / four-claim / four-evidence-use topology now present in the slice.

**Required correction:** document the actual evidence topology and applicability boundary.

### P4-DOC-007 — OPEN
**Artifact:** `RELEASE/CONTENT-COVERAGE.json`
**Class:** lifecycle metadata drift

The coverage manifest still identifies its audit touch as the P3 correction cycle despite P4 having started.

**Required correction:** synchronize lifecycle metadata after the P4 debt map/correction cycle; do not rewrite corpus counts manually without validation.

### P4-DOC-008 — OPEN
**Artifact:** `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json`
**Class:** lifecycle scope drift

The cross-slice audit now has a P4 next step, but its `corpus_scope` still describes R1–R23 plus P1/P2 and does not explicitly include P3/P4 maturation.

**Required correction:** synchronize the scope statement with the current maturation corpus after the substantive P4 cycle is established.

### P4-TEST-009 — OPEN
**Artifact:** `REFERENCE/tests/test_content_chemical_water_advisory_vertical_slice.py`
**Class:** regression-contract weakness

The `test_claims_have_evidence` function is effectively empty: it calls `_records()` but performs no assertions. The slice has two sources and multiple evidence-use records, but this test does not enforce claim→evidence→source linkage.

**Required correction:** implement a real linkage regression covering every claim and its evidence/source references.

### P4-TEST-010 — OPEN
**Artifacts:** `REFERENCE/tests/test_content_water_infrastructure_basics_vertical_slice.py`, `REFERENCE/tests/test_content_water_quality_basics_vertical_slice.py`
**Class:** regression-contract weakness

These tests enforce only minimum/shape conditions. They do not enforce exact record topology or complete claim/evidence linkage, allowing silent evidence/documentation drift.

**Required correction:** strengthen the contracts to reflect the audited topology after the substantive correction pass.

### P4-TEST-011 — OPEN
**Artifact:** `REFERENCE/tests/test_content_water_treatment_basics_vertical_slice.py`
**Class:** regression-contract weakness

The test explicitly enforces exactly one source, which encodes the current evidence weakness rather than protecting the intended maturation criterion. After independent evidence is added, the contract must be changed to validate linkage without requiring a single-source baseline.

**Required correction:** replace the single-source invariant with an evidence-linkage invariant.

## No confirmed findings at this stage

- No duplicate-source defect confirmed in chemical-water-advisory or water-filter-assessment.
- Water-filter-assessment already has explicit Assessment/Inference separation and limitations.
- Chemical-water-advisory already contains CDC + EPA evidence and an explicit chemical-vs-microbial boundary.
- No artificial cross-slice Relation should be added solely for P4 metrics.
- No unsupported high-consequence numerical procedure was identified in the reviewed P4 target material.

## Audit status

This is the complete first-pass P4 debt map. No correction pass has begun.

Next:
**complete/independently recheck this debt map → one correction pass fixing all confirmed findings → repeat full P4 substantive audit → technical 3/3 → P4 CLEAN checkpoint → independent 3/3 checkpoint validation.**
