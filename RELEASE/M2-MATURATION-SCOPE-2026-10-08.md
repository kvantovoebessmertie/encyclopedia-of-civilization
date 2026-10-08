# M2 MATURATION SCOPE — 2026-10-08

## Status

**M2 — SCOPE LOCKED FOR SUBSTANTIVE AUDIT**

## Baseline

Protected M1 CLEAN checkpoint:
`0019aa2376fd45ecc063f3f6ee680e087ab8d729`

Fresh M2 Content Gap Map:
`2f19e7b1b70dbfb3aecd18b476dbd7d127a13a45`

Current corpus at Gap Map:
- 479 vertical slices
- 4619 Records
- 19 Record types
- 51 Relation records

M1 is CLOSED CLEAN and is not reopened.

## M2 package

M2 audits and, only where justified, matures these six existing slices:

1. `measurement-uncertainty-basics`
2. `statistics-basics`
3. `risk-management-basics`
4. `agriculture-basics`
5. `energy-security-basics`
6. `geographic-coordinates-basics`

These six are selected because they form a material cross-domain maturity asymmetry while remaining on the 9-Record / single-source profile.

## Substantive audit contract

For every target slice, independently assess:

### 1. Content depth and semantic correctness

Check whether existing Claims adequately cover:
- core definition;
- mechanism, dependency, or interpretation where materially relevant;
- meaningful conditions and limitations;
- uncertainty or applicability boundaries.

Do not add Claims merely to increase record count.

### 2. Evidence use and source diversity

Check:
- whether each substantive Claim has an explicit and materially relevant Evidence Use;
- whether the source is appropriate for the Claim;
- whether the current single evidence track creates a material verification weakness;
- whether an independent second source would materially improve corroboration, applicability, or reuse.

Do not add a second source unless the audit establishes a substantive reason.

### 3. Scope / Context / Human View

Check that:
- educational knowledge is distinguishable from individualized advice;
- numerical or statistical statements do not imply unsupported precision;
- risk statements do not become universal risk thresholds;
- agriculture statements preserve system, crop, climate, and context dependence;
- energy-security statements distinguish general concepts from jurisdiction-specific policy or infrastructure requirements;
- geographic-coordinate statements distinguish coordinate concepts from navigation, surveying, GIS, or emergency operational instructions.

### 4. Cross-domain integration

Evaluate only semantically material dependencies. Candidate relationships include:
- measurement uncertainty ↔ measurement/instrumentation, statistics, scientific method;
- statistics ↔ probability, sampling, measurement, data science;
- risk management ↔ risk analysis, decision analysis, disaster response, infrastructure resilience;
- agriculture ↔ soil, food systems, seed storage, water resources, food security;
- energy security ↔ energy basics, energy markets, energy policy, infrastructure resilience, disaster response;
- geographic coordinates ↔ maps/navigation, geospatial analysis, remote sensing, surveying-related domains.

No Relation is added solely to improve a metric.

### 5. Regression and documentation impact

Any substantive modification must identify and synchronize the affected:
- slice README;
- record fixtures;
- dedicated regression;
- coverage/registry metadata;
- provenance/evidence references;
- Relation audit metadata where applicable.

## Explicit exclusions

- no reopening of M1;
- no mass rewrite of the 479-slice corpus;
- no new Record Type;
- no artificial Record/Claim/Source quota;
- no Relation added for metric growth;
- no second source added merely to satisfy a count;
- no unsupported numerical thresholds;
- no individualized medical, agronomic, regulatory, or emergency/local-authority instructions.

## Execution order

1. substantive audit of all six slices;
2. evidence-independence/diversity audit;
3. Human View/adversarial audit;
4. cross-domain Relation audit;
5. create a unified M2 Debt Map containing only confirmed findings;
6. perform one controlled correction pass;
7. repeat substantive audit;
8. synchronize documentation, coverage, and regressions;
9. exact-head Reference + Release Gate + Offline CI;
10. create a dedicated M2 CLEAN checkpoint;
11. independently verify 3/3 GREEN on that exact checkpoint HEAD.

No correction is authorized by this Scope itself; corrections begin only after confirmed audit findings.

## Definition of Done

M2 is complete only when:
- no confirmed substantive debt remains in the six target slices;
- no unresolved evidence-boundary debt remains;
- no unresolved Human View/adversarial debt remains;
- Relation changes, if any, are semantically justified and regression-covered;
- documentation and coverage are synchronized;
- dedicated regressions are green;
- exact checkpoint HEAD has Reference + Release Gate + Offline GREEN.

Evidence and conformance establish traceability and system integrity; they do not by themselves establish factual truth.
