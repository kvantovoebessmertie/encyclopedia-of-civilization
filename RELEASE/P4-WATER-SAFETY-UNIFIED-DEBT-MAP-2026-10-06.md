# P4 Water Safety & Resilience — Unified Debt Map — 2026-10-06

## Audit baseline

- P3 CLEAN checkpoint: `8bd1a889e83406a43b9d511b54da233f51e86cc9`
- P4 audit HEAD: `25a67750060e7ca0d5c64dfeb74a0f12873c414e`
- Correction HEAD before this synchronization: `e9f41ed8b0f14fe9b8a34e5aa07df75d5446a945`
- Corpus after correction: 478 vertical slices / 4379 Records / 19 Record types
- P4 target slices: 7
- Confirmed findings in the first-pass debt map: 11
- Additional finding discovered during independent correction recheck: P4-TEST-012
- Additional findings discovered during full substantive re-audit: P4-DOC-013, P4-DOC-014
- Total confirmed findings: 14

## Confirmed findings and closure status

### P4-EVIDENCE-001 — CLOSED
**Artifact:** `water-treatment-basics`

Independent EPA evidence was added alongside the existing WHO source. The regression contract now enforces 2 sources, 3 claims, 4 evidence uses and complete claim→evidence→source linkage.

### P4-EVIDENCE-002 — CLOSED
**Artifact:** `water-infrastructure-basics`

Independent EPA infrastructure-resilience evidence was added. The regression contract now enforces exact topology and complete claim→evidence→source linkage.

### P4-EVIDENCE-003 — CLOSED
**Artifact:** `water-security-basics`

Independent EPA water-security evidence was added. The regression contract now enforces exact topology and complete claim→evidence→source linkage.

### P4-EVIDENCE-004 — CLOSED
**Artifact:** `emergency-water-storage-state`

Independent EPA emergency-water-supply evidence was added while preserving the existing State/Relation/Identity semantics.

### P4-DOC-005 — CLOSED
**Artifacts:** `emergency-water-storage-state/README.md`, `water-filter-assessment/README.md`

README topology was synchronized to the actual record counts: 12 and 11 Records respectively.

### P4-DOC-006 — CLOSED
**Artifact:** `water-quality-basics/README.md`

README now records the actual 2-source / 4-claim / 4-evidence-use / 1-context / 1-scope topology and applicability boundary.

### P4-DOC-007 — CLOSED
**Artifact:** `RELEASE/CONTENT-COVERAGE.json`

Lifecycle metadata and corpus counts were synchronized to the P4 correction state: 478 slices / 4379 Records / 19 types, with audit touch `p4-water-safety-correction-2026-10-06`.

### P4-DOC-008 — CLOSED
**Artifact:** `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json`

Cross-slice scope now explicitly includes R1–R23 plus P1/P2/P3 and the current P4 water-safety/resilience correction cycle. The cross-slice baseline remains 30 dedicated Relation records.

### P4-TEST-009 — CLOSED
**Artifact:** `REFERENCE/tests/test_content_chemical_water_advisory_vertical_slice.py`

The formerly empty evidence test now asserts sources, claims, evidence records and complete claim→evidence→source linkage.

### P4-TEST-010 — CLOSED
**Artifacts:** `REFERENCE/tests/test_content_water_infrastructure_basics_vertical_slice.py`, `REFERENCE/tests/test_content_water_quality_basics_vertical_slice.py`

Contracts were strengthened to exact audited topology and complete evidence linkage.

### P4-TEST-011 — CLOSED
**Artifact:** `REFERENCE/tests/test_content_water_treatment_basics_vertical_slice.py`

The single-source invariant was removed and replaced with the intended multi-source evidence-linkage contract.

### P4-DOC-013 — CLOSED
**Artifacts:** `water-infrastructure-basics/README.md`, `water-security-basics/README.md`

Full re-audit found stale evidence-use counts in both READMEs (3 declared vs 4 actual). Both were synchronized to the audited 11-record / 2-source / 3-claim / 4-evidence-use topology.

### P4-DOC-014 — CLOSED
**Artifacts:** `water-treatment-basics/README.md`, `chemical-water-advisory/README.md`

Full re-audit found insufficient current topology documentation in both READMEs. Both were synchronized to their audited record/source/claim/evidence/context/scope topology.

### P4-TEST-012 — CLOSED
**Artifact:** `REFERENCE/tests/test_content_water_security_basics_vertical_slice.py`

Independent recheck found that the water-security regression remained weaker than the corrected maturation contract. It was strengthened to exact topology and complete claim→evidence→source linkage.

## Correction principles

- Independent evidence was added only where it materially strengthens a safety/resilience boundary.
- No duplicate publisher/source was introduced merely to inflate counts.
- Existing State/Relation/Identity semantics were preserved.
- No artificial cross-slice Relation was added for P4 metrics.
- No unsupported high-consequence numerical procedure was introduced.

## Remaining required gates

The correction pass and full substantive re-audit are complete, but **P4 CLEAN is not yet declared**.

Required sequence:
1. Technical CI 3/3 on the final re-audit correction state: Reference + Release Gate + Offline.
3. P4 CLEAN checkpoint.
3. P4 CLEAN checkpoint.
4. Independent 3/3 checkpoint validation.

A clean technical CI result alone is not sufficient for P4 CLEAN.
