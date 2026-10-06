# P2 Gap Map — Food Safety & Preservation Resilience — 2026-10-06

## Baseline

- Verified CLEAN checkpoint: `0169c9189cf2867a4387c46f8d71f1af64260adf`
- Corpus baseline: 478 vertical slices / 4361 Records / 19 Record types.
- P1 is CLOSED and must not be reopened except for a verified regression.
- P2 acceptance rule: no unresolved substantive or technical debt is carried into the next CLEAN checkpoint.

## P2 priority

**P2 — Food safety and preservation resilience**

This is the next coherent maturation cluster because food safety is a high-consequence practical domain already represented across normal handling, preservation, flooding and power-outage scenarios. The current corpus has useful coverage, but several slices remain source-bounded or only lightly triangulated.

## Target cluster

### 1. food-preservation-basics — 9 Records
Primary gap:
- single-source baseline;
- needs independent evidence where claims materially affect safe preservation/handling;
- review conditions, limitations and Human View boundaries before adding operational detail.

### 2. power-outage-food — 13 Records
Primary gap:
- practical high-consequence guidance is currently anchored to one USDA source;
- independently triangulate the key time/temperature claims;
- test whether a user can distinguish general thresholds from product-specific decisions and uncertainty.

### 3. flood-food-safety — 10 Records
Primary gap:
- already has CDC + FDA evidence;
- focus on substantive depth, limits and cross-domain integration rather than metric-driven expansion;
- verify interaction with flood cleanup, sanitation and water-safety knowledge.

### 4. food-safety-basics — 12 Records
Role:
- reference/anchor slice for the cluster;
- audit existing claims and evidence rather than expanding automatically;
- identify any introductory claims whose reuse would benefit from independent triangulation.

## Maturity criteria

For every target slice:

1. Content depth: add claims only when they close a real knowledge or safety boundary.
2. Evidence independence: prefer independent institutional sources; do not duplicate the same evidence under different publishers.
3. Geographic diversity: where regional applicability or regulation matters, include authoritative regional sources (including Russian sources when they add genuine independent or local value), without adding sources solely for geographic balance.
4. Limits and failure modes: make uncertainty, exceptions and escalation boundaries explicit.
5. Cross-domain integration: add only semantically justified Relations to water safety, flood cleanup, sanitation, emergency response, power outage or related domains.
6. Human View/adversarial: test ordinary-user interpretation under realistic food-loss/contamination scenarios.
7. Documentation: synchronize README, coverage and audit registries with the actual corpus.
8. Technical closure: Reference + Release Gate + Offline must all be green before the P2 CLEAN checkpoint.

## Explicit exclusions

- No blanket expansion of all food-related slices.
- No artificial Relation creation to improve metrics.
- No unsupported storage times, temperatures, dosages or procedural details.
- No replacement of source evidence with editorial assertions.
- No P3 / next-priority work before P2 reaches CLEAN.

## Planned audit sequence

**P2 cluster → content-depth audit → evidence-independence/diversity → cross-domain integration → Human View/adversarial → fix every finding → full 3/3 CI → dedicated P2 CLEAN checkpoint.**

## Success condition

P2 is complete only when:

- blocking findings = 0;
- critical contradictions = 0;
- exact duplicate clusters = 0;
- substantive findings remaining = 0;
- Human View/adversarial findings remaining = 0;
- documentation/coverage are synchronized;
- Reference, Release Gate and Offline are independently GREEN on the checkpoint commit.

## Epistemic boundary

Conformance, provenance, evidence linkage and CI establish system integrity and traceability; they do not establish the factual truth of every Claim.
