# M10 Human View Completion — Audit Scope Lock — 2026-10-09

## Status and correction to acceptance language

**OPEN — REQUIRED HUMAN VIEW GATE NOT YET COMPLETE. NOT CLEAN FOR FULL MATURITY ACCEPTANCE.**

The three technical CI workflows previously passed on M10 HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`. Those results remain valid for that exact HEAD and the checks they execute. They do not establish that a novice can successfully use the slice.

The earlier M10 CLEAN statement was too broad if interpreted as full maturity acceptance. This follow-up preserves the technical CI result while reopening the overall M10 acceptance decision until the missing Human View gate is completed. Do not rewrite or alter the protected M10 branch, M9, earlier accepted checkpoints, or `main` as part of this audit branch.

Working branch: `m10-human-view-completion-2026-10-09`, created from M10 HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`.
Proposed PR base: `m10-gap-map-2026-10-09`. Keep draft/open/unmerged.

## Audit target

Slice: `human-settlement-systems-basics`, including its README, Claims, linked Evidence Use records, Context and Scope. Compare with source records and applicable release constraints. No unrelated slice is an edit target.

## Mandatory task-based Human View audit

Perform and record each scenario with the exact user question, expected answer/action, observed answer/action from the slice, result (PASS / PARTIAL / FAIL / NOT TESTABLE), evidence, and required correction if any.

1. **Cold start:** Can a reader unfamiliar with the architecture explain what a settlement system is after reading only the README and linked introductory material?
2. **Dependency reasoning:** Given an illustrative disruption to one basic service, can the reader identify likely dependencies and distinguish an example from a universal rule?
3. **Use in a real decision:** Can the reader identify which local facts, applicable rules and qualified expertise are still needed before making a real planning/design decision?
4. **Evidence traceability:** Can the reader follow each central claim to its evidence and understand what the source does and does not establish?
5. **Misinterpretation / adversarial reading:** Attempt to infer that the model guarantees outcomes, applies identically everywhere, or replaces local assessment. Record whether the content prevents or corrects that inference.
6. **Failure and uncertainty:** Can the reader identify missing local data, uncertainty, trade-offs and dependencies rather than treating the overview as a complete implementation recipe?
7. **Navigation and recovery:** Can a reader who does not know record types, IDs, or repository architecture find the next useful step without first learning the schema?
8. **Boundary and safety:** Does the slice avoid presenting general concepts as site-specific engineering, legal, emergency or public-health instructions?

This is a structured desk-based task simulation unless a real novice participant is actually involved. Do not describe simulated results as observed human-subject results. If a real novice test is unavailable, record that limitation explicitly and require the content to pass adversarial task simulation plus automated regressions; do not claim a live usability study occurred.

## Technical and structural audit

- Reconfirm the three M10 workflows and their exact tested SHA; do not treat CI alone as Human View evidence.
- Verify the full M10 diff against M9, the 11-record shape, Claim/Evidence Use linkage, source identities/URLs, provenance, Context/Scope and Relation invariants.
- Verify coverage and the dedicated regression. Add content-specific assertions only after the task audit confirms the expected behaviors.
- Check the README as a standalone entry point, not merely as a repository-maintenance artifact.
- Review source diversity and independent corroboration claim by claim. Do not add sources merely to increase a count.
- Reconcile all findings into one unified debt map. No finding may disappear merely because the three CI workflows are green.

## Locked boundaries

- This branch is audit-first. No slice-content changes until the task-based audit and exact proposed correction file list are recorded.
- No changes to `main`, M10 protected branch, M9, accepted earlier checkpoints, or unrelated slices.
- No new Records, Sources, Relations, record types or slices are authorized by this lock.
- No weakening existing tests, changing source identities/URLs, changing IDs/provenance/refs, or modifying Relation participants to make checks pass.
- If the audit finds no content debt, record the negative finding with evidence. Do not manufacture a correction.
- Any confirmed correction needs an explicit bounded authorization, dedicated regression and a fresh exact-HEAD run of all three required CI workflows.

## Acceptance gate

M10 overall maturity acceptance remains **OPEN** until:
1. All eight task scenarios have evidence-backed results.
2. Every FAIL/PARTIAL is resolved or explicitly retained as a blocker with rationale.
3. Regression tests protect the newly verified user-facing behavior without weakening existing checks.
4. Source scope, claims, linkage, boundaries, coverage and diff are independently rechecked.
5. Reference, Release Conformance Gate and Offline Edition all PASS on the same final HEAD.
6. Branch/PR base/head/state, diff, Relation delta and unchanged `main` are independently verified.
7. No commits are added after that exact-head CI acceptance.

Do not merge this PR or promote any branch as part of the checkpoint.