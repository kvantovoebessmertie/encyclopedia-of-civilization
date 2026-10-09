# M11 Candidate Verification and Scope Lock — 2026-10-09

## Status

**CANDIDATE VERIFICATION ONLY — NOT A CONTENT-CORRECTION AUTHORIZATION; NOT CLEAN.**

Working branch: `m11-gap-map-after-m10-human-view-2026-10-09`, created from the exact M10 Human View follow-up HEAD `313b5dc663e032da0e7499829fd55aaf2a1ee157`.
Stacked PR base: `m10-human-view-completion-2026-10-09`. Keep all maturity PRs open, draft and unmerged. Do not change `main`, the protected M10 candidate branch, or prior accepted checkpoints.

## Candidate and rationale

Primary candidate for read-only verification: `accessibility-basics`.

Prior provenance must be respected: this slice was included in the R18 controlled-slice expansion. M11 must assess whether a genuine maturity/depth debt remains; it must not recreate the slice, inflate record counts, or present its original planned shape as a new finding.

Related slices `ergonomics-basics` and `human-factors-basics` are comparison context only until a separate evidence-backed scope decision is recorded. Existing cross-slice Relations must be inspected before claiming a missing relationship or proposing any Relation change.

Earlier M11 planning and correction branches were based on the earlier M10 candidate HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`, before the Human View follow-up was completed. Treat those branches as audit references only; do not assume their baseline or acceptance state carries forward. Revalidate candidate findings against the current stacked baseline before authorizing content edits.

## Initial read-only questions

1. Verify the exact current contents and dedicated regression for `accessibility-basics`.
2. Compare each Claim and linked Evidence Use description against the canonical source's actual scope and limits. Do not treat multiple paraphrases of one source as independent corroboration.
3. Check whether the README gives a usable introductory explanation, bounded example where appropriate, and clear limits for local standards/design decisions.
4. Check whether the regression protects substantive meaning, source boundaries and Human View in addition to structure/linkage.
5. Search prior M1–M10 scope locks, audits and unified debt maps for duplicate or already-resolved work.
6. Inspect relevant Relation records before deciding whether a cross-slice linkage debt exists.
7. Verify source diversity only where each proposed source independently supports a specific claim. Do not add sources solely to improve a numeric diversity metric.

## Locked boundaries

- This commit authorizes only candidate verification and this planning record.
- No changes to `main`, M10, accepted earlier checkpoints, or any other maturity branch.
- No new Records, Sources, Relations, record types or slices are authorized by this lock.
- No edits to comparison slices unless a separate finding and explicit bounded authorization is recorded.
- No change to canonical source identity/URL, provenance, Claim IDs, Evidence Use IDs, source/claim refs, evidence roles, Context/Scope target refs, Relation participants, or corpus coverage without a separate finding and explicit authorization.
- If no material debt is confirmed, record the negative finding and stop; do not manufacture a correction.
- Any confirmed correction requires a separate finding ledger and exact authorized file list before implementation.

## Required sequence

1. Finish the read-only initial audit against this branch's actual baseline and compare prior M1–M10 records for overlap.
2. Record evidence-backed findings and proposed correction scope; do not edit slice content during the initial audit.
3. If and only if material debt is confirmed, authorize the minimal exact file list and update one unified debt map.
4. Implement narrow corrections and dedicated regressions without weakening existing tests.
5. Run targeted tests and the full Reference implementation suite.
6. Run Reference, Release Conformance Gate and Offline Edition on one identical final HEAD.
7. Independently verify final diff, coverage, Relation delta, branch/PR base and head, draft/unmerged state, and unchanged `main`.
8. Record CLEAN only if every applicable gate passes on that exact HEAD. Any later commit invalidates the CI acceptance and requires a fresh exact-head 3/3 run.

## Acceptance status

M11 is **OPEN / CANDIDATE VERIFICATION ONLY**. No content change is accepted by this document.
