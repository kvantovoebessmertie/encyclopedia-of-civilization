# M3 MATURATION SCOPE — 2026-10-08

## Status

**M3 — SCOPE LOCKED FOR SUBSTANTIVE AUDIT**

## Protected baseline

M2 CLEAN checkpoint:
`bfd0578ca6f8dae9093a96de4f2bf6139589a40f`

Baseline:
- 479 vertical slices
- 4655 Records
- 19 Record types
- 577 Sources
- 1582 Evidence Use
- 57 Relations

M2 is CLOSED CLEAN and is not reopened.

## M3 package

M3 audits and, only where justified, matures these six existing slices:

1. `fire-safety-basics`
2. `shelter-basics`
3. `water-resources-basics`
4. `food-preservation-basics`
5. `scientific-method-basics`
6. `emergency-management-basics`

Selection basis:
- all six are on the 9-Record / single-source profile;
- each has high practical, epistemic or cross-domain reuse;
- current Claims are introductory and source-bounded;
- no existing candidate-specific Relation was found by the structural scan;
- each has a clear applicability boundary that can be tested without turning the slice into individualized or operational advice.

## Candidate rejected after verification

`energy-basics` was screened but not selected. Its current Claims are basic physics concepts (kinetic energy, potential energy and work), so the structural 9/1 profile alone does not establish a separate high-priority maturation asymmetry.

## Audit contract

For every M3 target, independently assess:

1. substantive depth and semantic correctness;
2. evidence relevance and independence;
3. applicability, uncertainty and known/unknown boundaries;
4. Human View / adversarial safety;
5. material cross-domain dependencies;
6. regression and documentation impact.

No Claim, Source, Evidence Use or Relation is added merely to increase a count.

## Domain boundaries

- Fire safety: descriptive safety knowledge; no site-specific fire engineering, code determination or live emergency command.
- Shelter: general shelter/habitability concepts; no site-specific structural design or individualized emergency instructions.
- Water resources: descriptive resource concepts; no local allocation decisions, treatment prescriptions or authority-specific requirements.
- Food preservation: general food-safety/preservation knowledge; no unsupported product-specific safety thresholds.
- Scientific method: educational epistemic foundations; no claim that one method applies identically to every discipline.
- Emergency management: general concepts; no live incident command, local legal requirements or jurisdiction-specific procedures.

## Explicit exclusions

- no reopening M2;
- no mass rewrite;
- no new Record Type;
- no artificial Record/Claim/Source quota;
- no Relation for metric growth;
- no second source unless substantive/evidence audit establishes material benefit;
- no unsupported numerical thresholds;
- no individualized medical, regulatory, engineering, food-safety or emergency instructions.

## Execution order

1. substantive audit of all six;
2. evidence-independence/diversity audit;
3. Human View/adversarial audit;
4. cross-domain Relation audit;
5. unified M3 Debt Map with confirmed findings only;
6. one controlled correction pass;
7. post-correction substantive re-audit;
8. synchronize documentation, coverage and regressions;
9. exact-head Reference + Release Gate + Offline;
10. dedicated M3 CLEAN checkpoint;
11. independent exact-head 3/3 GREEN verification.

No correction is authorized by this Scope itself.

## Definition of Done

M3 is complete only when:
- no confirmed substantive debt remains;
- no unresolved evidence-boundary debt remains;
- no unresolved Human View/adversarial debt remains;
- justified Relations are regression-covered;
- documentation/coverage/registry are synchronized;
- exact checkpoint HEAD is GREEN on all three release workflows.

Evidence and conformance establish traceability and system integrity; they do not by themselves establish factual truth.
