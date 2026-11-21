# M13 — exact-HEAD baseline revalidation checkpoint

Date: 2026-11-21
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`
Branch: `m13-system-wide-depth-audit-2026-10-09`
PR: #21 (open, Draft, unmerged)
Inspection HEAD: `442690867451dc97f9abc35639f5fb08133b74da`
Disposition: **BASELINE REVALIDATED; PHASE 0 REMAINS OPEN / NOT RELEASE-READY.**

## 1. Exact repository state

| Item | Observed value |
|---|---|
| M13 branch HEAD | `442690867451dc97f9abc35639f5fb08133b74da` |
| PR #21 head | Same as inspection HEAD |
| PR base | `m12-human-factors-source-and-human-view-2026-10-09` @ `e87e5bba60c9ed1101ecd4d53493c968c4760dac` |
| PR state | Open / Draft / unmerged |
| PR changed-file count | 836 (cumulative PR delta; not the latest commit delta) |
| Latest commit changed files | Exactly 4 |
| Current main | `d58289f319993ede5294a46f4741a506fd2fd710` |
| M13 vs main | Diverged; 1,942 commits ahead, 10 behind; merge base `203a7028e08da394fd44630fe38727be07bc8849` |

The latest commit changes only:
- `REFERENCE/build_offline_edition.py`
- `REFERENCE/docs/OFFLINE-EDITION.md`
- `REFERENCE/src/encyclopedia_reference/offline_edition.py`
- `REFERENCE/tests/test_offline_edition.py`

No merge, rebase, synchronization, or change to `main` was performed. The substantial divergence from `main` remains an integration risk and is not permission to integrate.

## 2. Exact-HEAD CI

All five returned check runs are completed successfully and point to the inspection HEAD:

| Check | Run | Result |
|---|---:|---|
| Reference implementation tests | 44889951250 | PASS |
| Release Conformance Gate | 44889951246 | PASS |
| Offline Edition (pull request) | 44889951257 | PASS |
| Offline Edition (push) | 44889946388 | PASS |
| M13 Audit Queue Automation | 44889946342 | PASS |

The exact-head Reference Tests run produced the following artifacts:
- Claim audit worksheet: artifact 14701726685; SHA-256 `15d87c3157ccfbc321e8e62fd9418265e495f8926c31ffba6c479903c7bb28e6`.
- Evidence-linkage audit: artifact 14701079517; SHA-256 `8c3ee654fb557c86dadcb4de00293e4b2da3866a461101e1f3766e9e3440f271`.
- Scored-Claim reconciliation ledger: artifact 14700939994; SHA-256 `d57ab605a51c49607c4ff5485d9a8608a9350b8db94e9bc51f1abb6b6e0eef32`.

The exact-head queue workflow produced artifact 14701378847:
- Artifact name: `m13-review-queue-442690867451dc97f9abc35639f5fb08133b74da`.
- SHA-256: `9ec00083cc887756052db6300a959f019ac8f901930872eff1ef9cf4dc1c42d2`.
- Its runtime metadata and prior-report mention ledger both declare source revision `442690867451dc97f9abc35639f5fb08133b74da`.

The separate `M13 Generic Evidence Use Report Coverage` workflow did not run on this HEAD. The workflow is configured for manual dispatch or pushes touching its configured paths; the latest four-file commit did not touch those paths. Its absence is recorded as **NOT RUN**, not PASS or FAIL. The prior report-coverage artifact must not be carried forward as an exact-head result.

## 3. Reproduced corpus and audit accounting

The exact-head Claim worksheet reports:
- 4,851 record JSON files scanned.
- 1,494 Claims across 483 slice directories; 482 slices contain at least one Claim.
- 1,478 Claim@1 and 16 Claim@2.
- 1,679 Claim-to-Evidence Use links and 627 linked Source IDs.
- 1,494/1,494 Claims have at least one Evidence Use.
- D, E, and B fields are blank for all 1,494 rows; all 1,494 rows have `NOT_YET_REVIEWED` in this current worksheet.

The exact-head scored-report ledger reports:
- 1,501 historical scored rows and 1,494 unique normalized Claim IDs.
- All 1,494 inventory Claims have at least one historical row match; zero unmatched scored rows.
- Seven repeated groups containing 14 rows.
- One separator-normalized report match remains for manual confirmation.
- 163 filename/internal-ID differences: 160 separator-only comparisons and three documented aliases; zero unclassified filename/internal-ID mismatches.

These are accounting and provenance-retrieval results only. They do not accept historical scores into the current worksheet or certify current evidence chains.

The exact-head static linkage audit reports 1,117 structural findings:
- 496 generic Evidence Use material-description candidates;
- 493 separator-only filename/ID aliases;
- 75 duplicate Source-URI candidates;
- 47 Source-identity sentence candidates;
- 6 documented filename/ID aliases.

These are triage candidates, not 1,117 adjudicated semantic defects.

The exact-head prior-report mention ledger covers 751 Claims currently marked UNASSESSED by the risk queue:
- 749 have at least one configured report-ID mention;
- 2 have no match in configured reports;
- 979 mention rows in total: 905 exact matches, 73 grouped-suffix matches, and 1 separator-alias match.

A mention is a retrieval lead only. It does not establish a substantive review, exact-version applicability, source-passage verification, D/E/B acceptance, or completion of any separate gate.

## 4. Phase 0 decision

**Exact repository state, exact-head CI, and current machine-generated artifact provenance have been revalidated.** This closes the stale-SHA uncertainty for the inspected baseline.

Phase 0 is nevertheless **not closed**. The existing exceptions remain:
- the 14 unidentified historical inspection IDs;
- unverified provenance for the previously asserted independent REJECT;
- historical score/version and source-passage exceptions;
- outstanding independent human review;
- separate high-consequence, source-independence, Relations, Human View, rights, and governance/integration gates.

No canonical Claim, Evidence Use, Source, Assessment, Relation, risk, or score record was changed by this checkpoint. No new screening batch was created. PR #21 remains Draft/unmerged and `main` remains unchanged.

## 5. Ordered next work

Continue the existing M13 execution protocol; do not create Batch 55 merely to advance numbering.

1. Preserve this exact-head baseline and its artifacts.
2. Complete the Phase 2 Claim-to-report provenance ledger, classifying mentions as substantive review evidence, incidental/grouped mention, erratum, duplicate, or unresolved.
3. Continue Phase 3 exact `Claim ID@version` reconciliation, including the 14-ID discrepancy without inferring missing IDs.
4. Reconcile the known Batch 42–43 report-version sample and remaining report files; recover Batch 53–54 historical Evidence Use/Source versions; then compare current evidence-chain versions for exact-version candidates.
5. Keep all historical rows immutable and all current scores blank until their separate acceptance requirements are met.

Any future canonical correction requires a separate exact bounded authorization, regression coverage, dependent-record review, and exact-head CI. This checkpoint itself authorizes no canonical correction and no integration action.
