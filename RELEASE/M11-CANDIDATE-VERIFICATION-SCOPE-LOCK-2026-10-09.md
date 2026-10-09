# M11 Candidate Verification and Scope Lock — 2026-10-09

## Status

**CANDIDATE VERIFICATION ONLY — NOT A CONTENT-CORRECTION AUTHORIZATION; NOT CLEAN.**

Working branch: `m11-gap-map-2026-10-09`, created from the exact M10 candidate HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`.
Proposed PR base: `m10-gap-map-2026-10-09`. Keep all maturity PRs open, draft and unmerged. Do not change `main`.

## Candidate and rationale

Primary candidate for read-only verification: `accessibility-basics`.

Prior provenance must be respected: this slice was explicitly included in the R18 controlled-slice expansion. M11 must therefore assess whether a genuine maturity/depth debt remains; it must not recreate the slice, inflate record counts, or present its original planned 9-record shape as a new finding.

Related slices `ergonomics-basics` and `human-factors-basics` are comparison context only. They are not authorized M11 edit targets. Existing cross-slice Relations must be inspected before claiming a missing relationship or proposing any Relation change.

## Initial read-only questions

1. Verify the exact current contents and dedicated regression for `accessibility-basics`.
2. Compare the three Claims and their linked Evidence Use descriptions against the canonical source's actual scope and limits. Do not treat three paraphrases of one source as independent corroboration.
3. Check whether the README gives a usable introductory explanation, bounded example, and clear limits for local standards/design decisions.
4. Check whether the current regression tests only structure/linkage or also protect the slice's substantive meaning, source boundaries and Human View.
5. Search prior M1–M10 scope locks, audits and unified debt maps for duplicate or already-resolved work.
6. Inspect relevant Relation records before deciding whether a cross-slice linkage debt exists.
7. Verify source diversity only where each proposed source independently supports a specific claim. Do not add sources solely to improve a numeric diversity metric.

## Locked boundaries

- This commit authorizes only the candidate verification process and this planning record.
- No changes to `main`, M10, accepted earlier checkpoints, or any other maturity branch.
- No new Records, Sources, Relations, record types or slices are authorized by this lock.
- No edits to `ergonomics-basics` or `human-factors-basics`.
- No change to canonical source identity/URL, provenance, Claim IDs, Evidence Use IDs, source/claim refs, evidence roles, Context/Scope target refs, Relation participants, or corpus coverage without a separate finding and explicit bounded authorization.
- If no material debt is confirmed, record the negative finding and stop; do not manufacture a correction.
- Any confirmed correction requires a separate, explicit finding ledger and exact authorized file list before implementation.

## Required sequence

1. Finish the read-only initial audit and compare M1–M10 records for overlap.
2. Record evidence-backed findings and proposed correction scope; do not edit slice content during initial audit.
3. If and only if material debt is confirmed, authorize the minimal exact file list and update the unified debt map.
4. Implement narrow corrections and dedicated regression without weakening existing tests.
5. Run targeted tests and the full Reference implementation suite.
6. Run Reference, Release Conformance Gate and Offline Edition on one identical final HEAD.
7. Independently verify final diff, coverage, Relation delta, branch/PR base and head, draft/unmerged state, and unchanged `main`.
8. Record CLEAN only if every applicable gate passes on that exact HEAD. Any later commit invalidates the CI acceptance and requires a fresh exact-head 3/3 run.

## Acceptance status

M11 is **OPEN / CANDIDATE VERIFICATION ONLY**. No content change is accepted by this document.