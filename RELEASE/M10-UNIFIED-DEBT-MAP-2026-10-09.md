# M10 Unified Debt Map — 2026-10-09

## Status

**DEBT STATUS: the scoped correction and post-correction desk audit are recorded below. Exact-HEAD CI and final acceptance must be determined from current workflow state and independent verification; this document does not assert a static CI result.** Working branch: `m10-gap-map-2026-10-09`; starting point: M9 candidate HEAD `40537f67ad8e4faf5f3b840aa49946f1902a236a`.

## Finding ledger

### M10-DEPTH-001 — broad settlement-system claims lack explicit mechanisms
**Status: RESOLVED BY CONTROLLED CORRECTION; regression gate added.**
The three Claims now explain settlement functions, dependencies among housing/basic services/infrastructure, and the coordination problem addressed by integrated planning. The wording remains introductory and avoids universal or site-specific guarantees.

### M10-EVIDENCE-002 — Evidence Use descriptions are accurate but mostly catalogue-like
**Status: RESOLVED BY CONTROLLED CORRECTION.**
The three descriptions now explain what the linked source supports and what it does not establish. Claim/source references, `supports` roles, record IDs, provenance, canonical source identities and URLs are preserved. No source-count increase was used to create apparent progress.

### M10-HUMAN-003 — introductory user view needs one bounded example
**Status: RESOLVED BY CONTROLLED CORRECTION; desk review only.**
The README now includes an explicitly illustrative dependency example and a direct local-data/specialist boundary. This is not a live novice usability study or independent external review.

## Editorial authorization and preflight

The first Reference and Release Gate preflight failed because `human-settlement-systems-basics` lacked explicit editorial authorization in `RELEASE/EDITORIAL-CORRECTION.json`. This was a valid fail-closed result, not a content/schema defect. The registry has now been updated on the M10 branch to add `M10-DEPTH-001`, `M10-EVIDENCE-002`, `M10-HUMAN-003` and the single authorized slice. No unrelated authorization was added or changed. All three workflows must rerun on the new exact HEAD.

## Structural and linkage audit

- The slice remains 11 records: 3 Sources, 3 Claims, 3 Evidence Use, 1 Context, 1 Scope.
- No Record, Source, Relation, Record type or slice was added or deleted.
- No Relation participants changed.
- Canonical source URLs and identities remain unchanged.
- Context/Scope content and target references remain unchanged.
- Targeted regression retains all original count/type/linkage assertions and adds content-specific assertions.
- The exact file delta against M9 is expected to contain only the three Claims, three linked Evidence Use records, README, dedicated regression, the single required M10 authorization entry, and the M10 planning/audit documents.

## Protected invariants

- Starting M9 HEAD: `40537f67ad8e4faf5f3b840aa49946f1902a236a`.
- M9 PR #14 remains open/draft/unmerged; do not merge it as part of M10.
- `main` was last independently verified at `203a7028e08da394fd44630fe38727be07bc8849`; do not change it.
- Preserve accepted M4/M5 and M7/M8 checkpoints.

## Acceptance gates

1. Targeted regression and all applicable Reference tests pass.
2. Release Conformance Gate and Offline Edition pass on the same exact final HEAD.
3. Actual coverage agrees with the unchanged structural count; no stale registry or coverage metadata is introduced.
4. Independent verification confirms branch head, PR base/head/state, exact file list, Relation delta and `main` SHA.
5. Record CLEAN only if every gate passes. Do not merge or promote as part of the checkpoint.


## M10-HUMAN-004 — novice navigation and applied Human View

**Content correction implemented on the separate follow-up branch. Desk simulation passes for the eight tested behaviors; no live novice study was conducted. Acceptance requires exact-head CI and independent final verification.**

Initial task audit found:
- the README described internal record architecture instead of a reader journey;
- the dependency example was too short to guide reasoning;
- source traceability depended on knowing repository records and IDs;
- the uncertainty boundary did not give readers useful next questions.

Correction on the M10 Human View follow-up branch is limited to the README and its dedicated regression, plus audit/authorization records. The README now includes a step-by-step illustrative dependency example, direct links from each Claim to Evidence Use and Source, a question-based next-step list, explicit local-decision boundaries and a technical-only structure note. Regression retains prior shape/linkage/content checks and adds assertions for all nine source/evidence/claim links and user-facing navigation.

Task-based desk simulation after correction records all eight scenarios as PASS for the specifically tested behaviors. This is not a live novice study and must not be described as one.

**Acceptance rule:** verify targeted/full test coverage through the required workflows on one identical current HEAD, then independently check diff, coverage, linkage, Relations, PR state and `main`. Do not infer final acceptance from this static document.