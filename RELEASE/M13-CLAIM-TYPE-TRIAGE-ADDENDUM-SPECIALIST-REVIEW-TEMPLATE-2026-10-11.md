# M13 Claim Type Triage Addendum — Repeated Specialist-Review Template
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source revision: `4453783e9dc2db55c4936a8acd85cbc666c46f86`
Status: **Nine additional exact-template candidates; human review required. No content JSON changed.**

## Finding

A corpus-wide exact-statement scan found a second repeated C-pattern in nine slices:

> Обобщённые сведения среза не заменяют специализированную проверку там, где вывод зависит от условий, измерений или профессиональной оценки.

All nine records currently have `content.claim_type = documented_fact`. The caution itself can be valid, but its repeated generic form is a cross-cutting epistemic/editorial boundary rather than a straightforward domain fact. It should be reviewed for shared-policy placement or domain-specific justification.

## Affected Claims

- `CLM-ARCHITECTURE_BASICS-C`
- `CLM-EPIDEMIOLOGY_BASICS-C`
- `CLM-ETHICS_BASICS-C`
- `CLM-FOOD_SCIENCE_BASICS-C`
- `CLM-IMMUNOLOGY_BASICS-C`
- `CLM-LINGUISTICS_BASICS-C`
- `CLM-PHILOSOPHY_BASICS-C`
- `CLM-RENEWABLE_ENERGY_BASICS-C`
- `CLM-ROBOTICS_BASICS-C`

## Cumulative template triage

The prior exact-template report identified 20 slice-purpose and 30 source/context/applicability Claims. This addendum adds 9 specialist-review Claims, for **59 distinct template candidates** in the current triage set (20 + 30 + 9). Two groups of nine Claims contain identical statement text across slices, so the issue is not merely similar wording: it includes exact repeated propositions.

This remains a human-review queue, not an automatic finding of falsehood. No IDs or Claim/Evidence Use/Source/Relation JSON were changed; M13 remains open.
