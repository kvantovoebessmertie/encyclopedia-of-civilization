# Readiness Development Roadmap — 2026-10-05

## Objective

Move the Encyclopedia of Civilization from a broad, conforming corpus to a deep, connected and practically usable knowledge system without sacrificing the existing architectural and CI guarantees.

## Priority order

### 1. Depth
Expand selected high-value slices beyond the introductory 9-Record profile.

Target improvements:
- additional independent sources;
- additional claims only where justified;
- competing or complementary evidence;
- conditions and limitations;
- uncertainty and known/unknown separation;
- practical applicability boundaries.

### 2. Evidence diversity
Prioritize triangulation for:
- safety-sensitive knowledge;
- high-consequence domains;
- claims likely to be reused as practical guidance;
- claims where a single source is insufficient.

### 3. Cross-domain integration
Add explicit Relations where they materially improve navigation, reasoning or practical use.

Do not create Relations merely to increase a metric.

### 4. Human View
Run structured human-facing audits on representative high-risk, practical and conceptual slices.

Test whether an ordinary user can:
- find the relevant knowledge;
- understand what is known and unknown;
- distinguish historical description from current instruction;
- identify applicability conditions;
- recognize when verification or expert/current-context input is required.

### 5. Breadth
Continue new vertical-slice waves only when the Gap Map identifies a meaningful uncovered area. Breadth remains valuable, but it is no longer the only optimization target.

## Wave discipline

Every expansion must:
1. preserve the current CLEAN baseline;
2. avoid undocumented mutation of existing content;
3. pass authoring and registration checks;
4. pass full Reference Tests;
5. pass Release Gate;
6. pass Offline Edition;
7. undergo substantive audit;
8. establish and validate a new CLEAN checkpoint.

## Maturity model

- **Level 1 — Conforming:** schema, provenance, evidence-use and CI contract satisfied.
- **Level 2 — Substantive:** meaningful depth and source diversity for the domain.
- **Level 3 — Integrated:** useful cross-domain relationships and context.
- **Level 4 — Human-validated:** representative users can reliably understand and use the knowledge boundaries.
- **Level 5 — Mature:** deep, independently triangulated, integrated and repeatedly human-audited.

The corpus currently has broad Level-1 conformance, with selected slices already reaching higher levels. The next phase should raise the maturity of the most important slices systematically.

## Non-negotiable principle

Do not trade correctness, provenance, safety boundaries or reproducibility for speed or corpus size.
