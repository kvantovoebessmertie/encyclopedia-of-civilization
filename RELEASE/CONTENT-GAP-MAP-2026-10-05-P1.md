# Content Gap Map — Post-CLEAN Maturation Cycle 1 — 2026-10-05

## Baseline
- CLEAN checkpoint: `43ca2cf2bb2acf8f13b8a7744e1ce0833aa40474`
- Corpus: 478 vertical slices / 4310 Records / 19 Record types
- Technical state: 3/3 release-layer CI GREEN
- Rule: no unresolved acceptance debt is carried into the next checkpoint.

## Selection method
Priority is based on:
1. consequence if a user applies incomplete guidance;
2. current content depth;
3. independence/triangulation needs;
4. operational edge cases and failure modes;
5. cross-domain usefulness.

## Priority map

### P1 — Emergency / high-consequence practical guidance
Current thin slices (mostly 7 records = Source + 2 Claims + 2 Evidence Use + Context + Scope):
- burn-first-aid
- cold-weather-hypothermia
- extreme-heat-safety
- flood-cleanup-safety
- emergency-waste-sanitation
- wildfire-smoke-safety
- carbon-monoxide-heating-safety
- generator-carbon-monoxide-safety
- hand-tool-safety
- home-fire-smoke-safety
- emergency-lighting-safety
- emergency-alert-warning

Special thin slice:
- septic-system-emergency (5 records)

**Why P1:** these are actionable, safety-sensitive domains where introductory two-claim coverage leaves important boundaries, escalation criteria, failure modes, and context conditions underrepresented.

### P2 — Water / food / infrastructure resilience
Examples:
- water-treatment-basics
- water-quality-basics
- water-filter-assessment
- food-safety-basics
- wastewater-treatment-basics
- sanitation-basics
- infrastructure-resilience-basics
- disaster-recovery-basics

Existing maturation work already strengthened a subset; next work should extend depth beyond the previously audited critical cluster.

### P3 — Core technical and scientific foundations
Large number of 9-record introductory slices remain source-bounded and shallow. Enrichment should be selected by downstream dependency and practical reuse, not by arbitrary slice count.

### P4 — Governance / law / economics / social systems
Prioritize only where the corpus is likely to support practical decisions or where cross-domain dependencies make shallow treatment materially limiting.

## Immediate maturity priority

**P1 emergency/high-consequence practical guidance**.

First enrichment batch should focus on a coherent safety cluster rather than isolated additions. The initial target is:
1. burn-first-aid
2. cold-weather-hypothermia
3. extreme-heat-safety
4. carbon-monoxide-heating-safety
5. generator-carbon-monoxide-safety
6. wildfire-smoke-safety
7. flood-cleanup-safety
8. emergency-waste-sanitation

For each target:
- add independent evidence where warranted;
- deepen claims with limits, failure modes, escalation/context boundaries;
- add operationally useful but source-supported content;
- add natural cross-domain relations only where semantically justified;
- run Human View/adversarial review;
- fix every real finding before CI/CLEAN.

## Non-goals
- No arbitrary bulk expansion.
- No synthetic Relations merely to increase linkage counts.
- No treating provenance/conformance as proof of truth.
- No carrying "known but unfixed" defects into the next checkpoint.

## Next gate
P1 batch → Content Depth audit → Evidence Diversity/Independence audit → Cross-domain integration → Human View/adversarial → full CI → CLEAN.
