# P13 — MATURATION SCOPE — HUMAN SETTLEMENT SYSTEMS — 2026-10-07

## Baseline
P12 CLEAN checkpoint: eb8aa9022c23369774e9cbd76abfa341cec0e26c
Corpus baseline: 478 vertical slices / 4565 records / 19 record types / 43 Relations (42 dedicated cross-slice).

## Objective
Address the identified system-level gap by adding one foundational vertical slice for human settlement systems, while integrating rather than duplicating existing domain knowledge.

## New vertical slice
human-settlement-systems-basics

Core dimensions:
- population and settlement structure;
- housing and buildings;
- land use and spatial organization;
- water supply and wastewater;
- sanitation and waste;
- energy and building services;
- transportation and accessibility;
- communications and information dependencies;
- public services and governance;
- environmental conditions and public health;
- infrastructure interdependencies;
- resilience, maintenance and continuity of services.

Epistemic boundary: descriptive and source-bounded. The slice is not site-specific planning, engineering design, legal determination, emergency command, or policy prescription.

## Targeted maturation audit
The following existing slices are audit targets, not automatic expansion targets:
1. housing-systems-basics
2. infrastructure-basics
3. urban-planning-basics
4. transportation-basics
5. water-infrastructure-basics
6. energy-systems-basics
7. waste-infrastructure-basics
8. environmental-health-basics
9. public-health-basics
10. accessibility-basics

Audit questions:
- does the existing slice already cover the proposed concept?
- is there a genuine substantive gap?
- is evidence sufficiently bounded and diverse for the intended reuse?
- does Human View remain clear?
- would a Relation materially improve conceptual reuse?

## Candidate Relations
Evaluate, but add only when directly justified:
- settlement ↔ housing
- settlement ↔ infrastructure
- settlement ↔ urban planning
- settlement ↔ transportation
- settlement ↔ water infrastructure
- settlement ↔ energy systems
- settlement ↔ waste infrastructure
- settlement ↔ environmental health
- settlement ↔ public health
- settlement ↔ accessibility

No Relation is to be created merely because two topics coexist or because they share metrics.

## Sequence
1. New-slice content-depth design.
2. Existing-target substantive audit.
3. Evidence independence/diversity audit.
4. Cross-domain Relation audit.
5. Human View/adversarial audit.
6. Unified P13 Debt Map.
7. One correction pass.
8. Repeat substantive audit.
9. Synchronize README, coverage, registry and package metadata as required.
10. Exact-head Reference + Release Gate + Offline CI.
11. Dedicated P13 CLEAN checkpoint.
12. Independent 3/3 verification on exact checkpoint HEAD.

## Explicit exclusions
- no artificial ten-slice quota;
- no duplicate generic transport, medical, industrial, agricultural, economic or technology system slices;
- no site-specific settlement design;
- no engineering calculations;
- no jurisdiction-specific legal determinations;
- no live emergency instructions;
- no unsupported numerical thresholds;
- no Relations for metrics;
- no reopening P2–P12 without verified regression.

## Definition of Done
- identified system-level gap addressed;
- all targeted existing-slice findings fixed or explicitly recorded as no-change;
- substantive debt = 0;
- unresolved Human View/adversarial findings = 0;
- Relation discrepancies/duplicates = 0;
- documentation/coverage synchronized;
- Reference, Release Gate and Offline GREEN on exact checkpoint HEAD;
- independent 3/3 verification completed.

Evidence, provenance, Relations and CI conformance do not by themselves establish factual truth.
