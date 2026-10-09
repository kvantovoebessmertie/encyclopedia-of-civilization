# M10 Unified Debt Map — 2026-10-09

## Status

**SCOPE LOCKED; CORRECTION NOT YET IMPLEMENTED.** This is a candidate audit record, not a CLEAN checkpoint. Working branch: `m10-gap-map-2026-10-09`; starting point: M9 candidate HEAD `40537f67ad8e4faf5f3b840aa49946f1902a236a`.

## Finding ledger

### M10-DEPTH-001 — broad settlement-system claims lack explicit mechanisms
**Status: CONFIRMED; CORRECTION AUTHORIZED.**
The three Claims are directionally appropriate and linked to relevant public sources, but the explanatory contract is weak: Claim A defines the system without showing how shared functions connect people and place; Claim B lists components without explaining a dependency pathway; Claim C says planning is integrated without explaining the coordination problem. The current regression protects counts and references but not explanatory depth.

### M10-EVIDENCE-002 — Evidence Use descriptions are accurate but mostly catalogue-like
**Status: CONFIRMED; CORRECTION AUTHORIZED.**
Existing descriptions identify the general source topic and component list. The correction should clarify the claim-specific support and source limits without changing claim/source links, evidence roles, canonical identities or locators. No source-count increase is authorized.

### M10-HUMAN-003 — introductory user view needs one bounded example
**Status: CONFIRMED; CORRECTION AUTHORIZED.**
The README only states the purpose and record pattern. Add a brief, clearly illustrative dependency example and a direct statement that local conditions differ and this slice is not a design or operational guide. This is a desk-based content review, not a live novice usability study.

## Protected invariants

- Starting M9 HEAD: `40537f67ad8e4faf5f3b840aa49946f1902a236a`.
- M9 PR #14 remains open/draft/unmerged; do not merge it as part of M10.
- `main` was last independently verified at `203a7028e08da394fd44630fe38727be07bc8849`; do not change it.
- Preserve accepted M4/M5 and M7/M8 checkpoints.
- Preserve all 11 record identities, the 3 Source identities/URLs, all 3 claim/source links and the `supports` roles.
- No Relation records or participants may change.

## Acceptance gates

1. Implement only the scope in `M10-CORRECTION-SCOPE-LOCK-2026-10-09.md`.
2. Run the targeted regression and inspect all edited JSON/README diffs.
3. Perform post-correction claim/evidence/source-scope/Human View/Relation desk audit.
4. Reconcile coverage against actual corpus counts; do not assume or inflate totals.
5. Run Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
6. Independently verify the branch head, PR base/head/state, exact file list, Relation delta and `main` SHA.
7. Record CLEAN only if every gate passes. Do not merge or promote as part of the checkpoint.
