# M13 Claim Type Triage Addendum — Complete Specialist-Review Template
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Initial exact-template screen revision: `bb3f67d1755441f7815b26c6666e9a903c4d99d2`
Status: **Expanded triage; human review required. No Claim content JSON changed.**

## Additional family C: 20 repeated Claims

The corpus contains a repeated C-pattern in the same 20 slices as the slice-purpose and source/context families:

> Базовое знание по [slice] не заменяет специализированную проверку, когда вывод зависит от условий, измерений или профессиональной оценки.

All 20 records currently have `content.claim_type = documented_fact`. The boundary may be sound, but the repeated form is cross-cutting epistemic/editorial guidance and should be reviewed for shared-policy placement or domain-specific justification.

- `CLM-ANTHROPOLOGY_BASICS-C`
- `CLM-BIOCHEMISTRY_BASICS-C`
- `CLM-CELL_BIOLOGY_BASICS-C`
- `CLM-CIVIL_ENGINEERING_BASICS-C`
- `CLM-CLIMATE_SCIENCE_BASICS-C`
- `CLM-COMPUTER_NETWORKS_BASICS-C`
- `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C`
- `CLM-DATA_SCIENCE_BASICS-C`
- `CLM-ECOLOGY_BASICS-C`
- `CLM-ELECTROMAGNETISM_BASICS-C`
- `CLM-FLUID_MECHANICS_BASICS-C`
- `CLM-GENETICS_BASICS-C`
- `CLM-GENOMICS_BASICS-C`
- `CLM-GEOLOGY_BASICS-C`
- `CLM-LOGIC_BASICS-C`
- `CLM-OCEANOGRAPHY_BASICS-C`
- `CLM-OPERATING_SYSTEMS_BASICS-C`
- `CLM-ORGANIC_CHEMISTRY_BASICS-C`
- `CLM-PSYCHOLOGY_BASICS-C`
- `CLM-SOCIOLOGY_BASICS-C`

## Additional exact duplicate family: 9 Claims

A separate set of nine C-Claims repeats the same specialist-review statement verbatim across slices:

- `CLM-ARCHITECTURE_BASICS-C`
- `CLM-EPIDEMIOLOGY_BASICS-C`
- `CLM-ETHICS_BASICS-C`
- `CLM-FOOD_SCIENCE_BASICS-C`
- `CLM-IMMUNOLOGY_BASICS-C`
- `CLM-LINGUISTICS_BASICS-C`
- `CLM-PHILOSOPHY_BASICS-C`
- `CLM-RENEWABLE_ENERGY_BASICS-C`
- `CLM-ROBOTICS_BASICS-C`

## Reconciled candidate count

- 20 slice-purpose Claims (family A);
- 20 source/context/applicability Claims in the repeated family B, plus 9 exact duplicate B-Claims and one additional cross-cutting source-provenance rule `CLM-HISTORY_METHODS_BASICS-B` — 30 candidates in the existing source/context triage queue;
- 20 family-C specialist-review Claims listed above;
- 9 additional exact duplicate C-Claims listed above.

The expanded queue therefore contains **79 distinct Claim IDs** (20 + 30 + 20 + 9). The earlier semantic-duplicate report recorded 78 (three 20-Claim families plus two exact duplicate groups of nine); the expanded exact-template screen identifies `CLM-HISTORY_METHODS_BASICS-B` as one additional cross-cutting methodology candidate outside those 78. This is a classification/placement review queue, not a finding that the propositions are false.

## Disposition

1. Review whether the 79 Claims belong in a shared methodology/editorial layer or need domain-specific wording.
2. Do not treat an external domain overview as evidence that a local slice is complete or that a general caution is a domain fact.
3. Preserve IDs and content JSON until the separately authorized correction phase.
4. Keep M13 open pending full inventory reconciliation, source-fit review, Human View, adversarial review, independent review and regression/CI on the exact final HEAD.
