# P6 Gap Map — Public Health & Health Resilience — 2026-10-06

## Baseline

- Verified P5 CLEAN checkpoint: `b0da033bc3e566c5a2259598e660c4abcfef63fc`.
- Corpus baseline: 478 vertical slices / 4390 Records / 19 Record types.
- P1–P5 are CLOSED and must not be reopened except for verified regression.
- P6 rule: no unresolved substantive, evidence, Human View, documentation or technical debt is carried into the next CLEAN checkpoint.

## P6 priority

**P6 — Public Health & Health Resilience**

This is the next coherent high-consequence cluster because public-health knowledge connects the completed emergency food, sanitation, water, disaster-recovery and infrastructure work to population-level prevention, surveillance, environmental exposure and behavioral-health resilience.

## Target cluster

1. `public-health-basics` — audit foundational public-health concepts, evidence independence and applicability boundaries.
2. `public-health-surveillance-basics` — audit surveillance mechanisms, emergency context, interpretation limits and source independence.
3. `epidemiology-basics` — audit core epidemiological concepts, causal-interpretation boundaries and evidence diversity.
4. `environmental-health-basics` — audit exposure/pathway concepts, environmental context and safe interpretation.
5. `disaster-behavioral-health-basics` — audit disaster mental/behavioral-health claims, limits, escalation and Human View boundaries.

## Cross-domain dependencies

Audit only semantically justified links among:
- public health ↔ epidemiology;
- surveillance ↔ emergency response;
- public health ↔ environmental health;
- environmental health ↔ water/food/sanitation;
- disaster behavioral health ↔ disaster response/recovery;
- public health ↔ health systems where the dependency is explicit.

No Relation is added solely to improve metrics.

## Maturity criteria

1. Content depth: mechanisms, conditions, limitations, uncertainty, dependencies and failure modes materially improve safe reuse.
2. Evidence independence: genuinely independent institutional/scientific evidence; no duplicated URLs or publisher relabeling.
3. Applicability: distinguish descriptive population-level knowledge from individual diagnosis, treatment or public-authority decisions.
4. Causality and interpretation: correlation, surveillance signal and causal inference must not be conflated.
5. Human View/adversarial: ordinary users must not mistake educational population-health information for individualized medical advice or live public-health directives.
6. Cross-domain integration: only semantically justified Relations.
7. Documentation: READMEs, coverage and audit registries synchronized.
8. Technical closure: Reference + Release Gate + Offline all green.

## Explicit exclusions

- No individualized diagnosis or treatment.
- No unsupported outbreak thresholds, dosing, exposure limits or emergency commands.
- No policy advocacy presented as factual health guidance.
- No artificial Relations.
- No correction before the complete unified P6 Debt Map is established, except repository-safety fixes.

## Planned sequence

**P6 target cluster → full substantive audit → unified Debt Map → one correction pass fixing every finding → repeat substantive audit → full 3/3 CI → dedicated P6 CLEAN checkpoint → independent 3/3 validation.**

## Success condition

P6 is complete only when blocking findings, critical contradictions, substantive findings, Human View/adversarial findings and documentation/coverage mismatches are all zero, with independent 3/3 GREEN on the checkpoint commit.

## Epistemic boundary

Conformance, provenance, evidence linkage and CI establish system integrity and traceability; they do not establish the factual truth of every Claim.
