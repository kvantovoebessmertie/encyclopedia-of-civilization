# M1 — MATURATION SCOPE — FOUNDATIONAL AND WATER SAFETY — 2026-10-08

## Baseline

Post-P1 Gap Map commit: `5af5be5b4be5e6fa99094b1d44e57e5ff1f072ca`

P1 CLEAN baseline:
- 479 vertical slices
- 4601 Records
- 19 Record types
- 51 Relations

## Objective

Resolve the identified maturity asymmetry in six thin subject slices without artificial expansion or schema change.

## Target slices

1. `probability-basics`
2. `ratios-and-percentages`
3. `seed-storage-basics`
4. `si-units-basics`
5. `time-standard-basics`
6. `water`

## Audit targets

For every slice:

### 1. Content depth
Check whether the current Claims adequately cover:
- definition;
- mechanism or dependency where materially relevant;
- conditions/limitations;
- uncertainty or applicability boundaries.

Do not add Claims solely to reach a target count.

### 2. Evidence diversity
Check source independence and Evidence Use materiality.

A second source is added only when it materially improves corroboration, applicability, or reuse.

### 3. Human View
Check that:
- educational knowledge remains distinguishable from individualized advice;
- mathematical and standards Claims do not imply unsupported precision;
- seed-storage Claims remain appropriately bounded by crop/context;
- water-safety Claims preserve hazard boundaries and escalation.

### 4. Cross-domain integration
Evaluate, but do not assume, Relations involving:
- probability ↔ statistics/measurement;
- ratios/percentages ↔ measurement/units;
- SI units ↔ measurement/uncertainty;
- time standards ↔ astronomy/geospatial/computing;
- seed storage ↔ agriculture/food systems;
- water ↔ emergency-water-storage/water-infrastructure/public-health.

Only semantically material Relations may be added.

### 5. Documentation and regression
Any substantive modification must synchronize:
- slice README where needed;
- coverage metadata;
- regression contract;
- provenance/evidence references;
- cross-slice audit metadata where Relations change.

## Explicit exclusions

- no fixed Record quota;
- no new Record type;
- no generic domain duplication;
- no mass rewrite;
- no unsupported numerical thresholds;
- no individualized medical/agronomic advice;
- no live emergency/local-authority instructions;
- no reopening P1 without verified regression.

## Sequence

1. substantive audit of all six slices;
2. evidence independence/diversity audit;
3. Human View/adversarial audit;
4. cross-domain Relation audit;
5. create one unified M1 Debt Map containing only confirmed findings;
6. perform one correction pass;
7. repeat substantive audit;
8. synchronize documentation/coverage/regressions;
9. exact-head Reference + Release Gate + Offline CI;
10. create dedicated M1 CLEAN checkpoint;
11. independently verify 3/3 GREEN on the exact checkpoint HEAD.

## Definition of Done

- no confirmed substantive debt;
- no unresolved evidence-boundary debt;
- no unresolved Human View/adversarial debt;
- no Relation discrepancy/duplicate;
- documentation and coverage synchronized;
- dedicated regressions green;
- exact checkpoint HEAD has Reference + Release Gate + Offline GREEN.

Evidence and conformance establish traceability and system integrity; they do not by themselves establish factual truth.
