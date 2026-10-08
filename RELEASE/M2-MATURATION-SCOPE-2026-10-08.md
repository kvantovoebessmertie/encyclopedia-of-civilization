# M2 MATURATION SCOPE — 2026-10-08

## Status

**M2 — SCOPE LOCKED FOR SUBSTANTIVE AUDIT**

## Baseline

Protected M1 CLEAN checkpoint:
`0019aa2376fd45ecc063f3f6ee680e087ab8d729`

Current corpus:
- 479 vertical slices
- 4619 records
- 19 Record types
- 51 Relation records

## M2 package

M2 audits and, only where justified, matures these existing slices:

1. air-quality-basics
2. agriculture-basics
3. anatomy-basics
4. antimicrobial-resistance-basics
5. acid-base-basics
6. analytical-chemistry-basics
7. algebra-basics
8. agrifood-systems-basics
9. architecture-basics
10. ancient-civilizations-basics

## Definition of Done

For each slice:
- substantive claims are reviewed;
- source independence is assessed;
- applicability/Scope/Context boundaries are assessed;
- Human View/adversarial risks are assessed;
- cross-domain Relations are added only if materially justified;
- any confirmed debt receives a concrete correction;
- dedicated regression is synchronized;
- documentation/registry remains consistent;
- full Reference, Release Gate and Offline verification pass.

There is no artificial target for record count, claim count, source count, or Relations.

## Safety and epistemic boundaries

- Health content does not become individualized medical advice.
- Chemistry content does not become hazardous procedural instruction.
- Environmental content does not imply universal local exposure limits.
- Architecture content does not substitute for jurisdiction-specific engineering/code requirements.
- Historical claims distinguish evidence from inference and chronology from causality.

## Execution order

1. substantive audit;
2. evidence-independence audit;
3. Human View/adversarial audit;
4. corrections;
5. regression and documentation synchronization;
6. re-audit;
7. unified debt closure;
8. exact-head CI;
9. CLEAN checkpoint.

No CLEAN status is declared before exact-head verification.
