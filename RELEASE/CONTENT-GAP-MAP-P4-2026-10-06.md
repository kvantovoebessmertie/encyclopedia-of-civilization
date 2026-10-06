# P4 Gap Map — Water Safety & Resilience — 2026-10-06

## Baseline

- Verified P3 CLEAN checkpoint: `8bd1a889e83406a43b9d511b54da233f51e86cc9`
- Corpus baseline: 478 vertical slices / 4371 Records / 19 Record types.
- P1, P2 and P3 are CLOSED and must not be reopened except for a verified regression.
- P4 acceptance rule: no unresolved substantive, Human View, documentation, evidence, or technical debt is carried into the next CLEAN checkpoint.

## P4 priority

**P4 — Water Safety & Resilience**

This is the next coherent maturation cluster because safe water is a foundational dependency connecting emergency survival, sanitation, food safety, public health, infrastructure, and long-term resilience. The corpus already contains a broad water-related set, so P4 will audit and mature the highest-consequence connected slices rather than expanding water content indiscriminately.

## Target cluster

### 1. emergency-water-storage-state
Anchor emergency slice. Audit whether the existing state/identity/relation structure clearly distinguishes stored-water state, uncertainty, applicability and escalation boundaries.

### 2. water-quality-basics
Audit foundational water-quality claims for evidence independence, source scope, interpretation boundaries and safe reuse.

### 3. water-treatment-basics
Audit treatment claims for evidence provenance, applicability and failure modes. No unsupported treatment recipes, concentrations or exposure times.

### 4. chemical-water-advisory
Audit how advisory information is represented, especially the boundary between an authoritative advisory and a generalized safety instruction.

### 5. water-filter-assessment
Audit assessment/inference boundaries, evidence linkage and Human View so that filter capability is not mistaken for universal water safety.

### 6. water-infrastructure-basics
Audit the infrastructure layer for resilience, dependencies and appropriate links to emergency water, sanitation and public-health systems.

### 7. water-security-basics
Audit higher-level resilience claims and their relation to emergency conditions, infrastructure and resource management without turning the slice into policy advocacy.

## Cross-domain dependencies to audit

Review only semantically justified links among:
- water safety ↔ sanitation/hygiene;
- water safety ↔ food safety;
- water safety ↔ flood response;
- water safety ↔ public health;
- water safety ↔ water infrastructure;
- emergency water ↔ disaster response/logistics.

No Relation is to be added solely to improve metrics.

## Maturity criteria

For every target slice:

1. Content depth: identify mechanisms, conditions, limitations, dependencies and failure modes that materially improve safe reuse.
2. Evidence independence: distinguish genuinely independent institutional evidence from duplicated URLs, derivative summaries or publisher relabeling.
3. Applicability: make jurisdiction, water source, advisory status and intended use explicit where relevant.
4. Limits and escalation: preserve uncertainty and professional/public-authority escalation boundaries.
5. Human View/adversarial: test realistic emergency interpretation, including contaminated water, advisories, failed treatment assumptions and filter overconfidence.
6. Cross-domain integration: add only semantically justified Relations.
7. Documentation: synchronize READMEs, coverage and audit registries after accepted changes.
8. Technical closure: Reference + Release Gate + Offline all green before P4 CLEAN.

## Explicit exclusions

- No blanket expansion of all water-related slices.
- No artificial Relations.
- No unsupported disinfection concentrations, exposure limits, storage times, procedural recipes or other high-consequence numbers.
- No claim that filtration, treatment, boiling or storage universally makes water safe without source-specific evidence.
- No editorial assertion replacing source evidence.
- No correction of P4 findings before the complete unified P4 debt map is established, except repository-safety fixes.

## Planned audit sequence

**P4 target cluster → full substantive audit (content depth + evidence independence + applicability + cross-domain + Human View/adversarial + documentation) → complete unified debt map → one correction pass fixing all findings → repeat substantive audit → full 3/3 CI → dedicated P4 CLEAN checkpoint → independent 3/3 CI on checkpoint.**

## Success condition

P4 is complete only when:
- blocking findings = 0;
- critical contradictions = 0;
- exact duplicate clusters in target cluster = 0;
- substantive findings remaining = 0;
- Human View/adversarial findings remaining = 0;
- evidence/documentation/coverage are synchronized;
- Reference, Release Gate and Offline are independently GREEN on the checkpoint commit.

## Epistemic boundary

Conformance, provenance, evidence linkage and CI establish system integrity and traceability; they do not establish the factual truth of every Claim.
