# M13 historical Claim-version recovery — Batches 18–40

- **Agent:** m13-auditor
- **Task:** Reconstruct the 133 remaining historical Claim versions using exact report-parent Git snapshots; identify content-lineage exceptions.
- **Date (UTC):** 2026-11-22
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** m13-system-wide-depth-audit-2026-10-09
- **Starting HEAD:** `fde5b351cf2310d7152c5873e25624420c98f56b`
- **Final evidence-artifact HEAD:** `834bd4beefddeb328d452b21c71f26530469f3f2` (the report-only commit that adds this handoff follows)
- **Status:** VERIFIED, with one explicit integrity HOLD

## 1. Request and acceptance criteria

Continue M13 Phase 3 historical Claim-version reconstruction from the exact state where 106/239 rows had been recovered and 133 remained unresolved.

Acceptance criteria:
- Reconcile every remaining row to its original scored report and exact historical Git snapshot.
- Inspect the exact historical Claim path and compare its Blob SHA with the current M13 comparison HEAD.
- Preserve IDs, paths, historical scores and all unresolved exceptions.
- Do not transfer historical D/E/B into current assessments.
- Do not modify canonical records, `main`, or protected checkpoints.

## 2. Scope

- **In scope:** 133 unique Claim rows in Batches 18–20, 22–26, and 28–40; exact report commits; each report commit's first-parent snapshot; historical/current Claim path and Blob SHA comparison.
- **Out of scope:** historical Evidence Use/Source version recovery; passage-level source validation; D/E/B acceptance; canonical Claim correction; Human View; specialist review; rights; release decisions.
- **Dependencies:** Phase 2 Claim-to-report provenance ledger; Phase 3 remaining worklist; Phase 1 version inventory; M13 system-wide protocol; M13 execution order and closure protocol.

## 3. Work performed

1. Reconstructed the exact report-introduction commit for each remaining report cohort using the GitHub commits-by-path endpoint scoped to the M13 branch.
2. Used the first parent of each report commit as the pre-report historical snapshot. The report commit and snapshot-parent SHA are retained per row in the CSV crosswalks.
3. Retrieved complete recursive Git trees for each snapshot and for comparison HEAD `fde5b351cf2310d7152c5873e25624420c98f56b`. Every relevant tree response was non-truncated.
4. Matched the 133 IDs to exactly one current repository path. Existing filename aliases were handled deterministically for lookup only; no canonical ID or path was changed.
5. Compared historical and current Blob SHAs for all 133 records.
6. Cross-checked the 133 IDs against the Phase 1 inventory's 16 version-2 Claims. There are zero intersections; all 133 are Claim@1. The one differing record was additionally fetched and parsed at both refs; both JSON records explicitly contain `record_version: "1"`.
7. Investigated the one Blob mismatch through its own file history and exact content-changing commit.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `RELEASE/M13-PHASE-3-BATCH-18-24-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` | Added, 40 rows | Row-level historical/current path and Blob SHA evidence |
| `RELEASE/M13-PHASE-3-BATCH-25-30-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` | Added, 24 rows | Same |
| `RELEASE/M13-PHASE-3-BATCH-31-34-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` | Added, 12 rows | Same |
| `RELEASE/M13-PHASE-3-BATCH-35-40-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` | Added, 57 rows | Same |
| `RELEASE/M13-PHASE-3-BATCH-18-40-HISTORICAL-CLAIM-VERSION-RECOVERY-ADDENDUM-2026-11-22.md` | Added | Consolidated result and exception disposition |
| `reports/agent-work/m13-auditor/phase3-batches-18-40-historical-claim-version-recovery-2026-11-22.md` | Added | Mandatory durable task handoff |

## 5. Findings and evidence

### VERIFIED — reconciliation totals

| Measure | Result |
|---|---:|
| Rows in original remaining worklist | 133 |
| Unique Claim IDs | 133 |
| Historical Claim versions identified | 133/133 |
| Exact historical/current path + Blob SHA matches | 132/133 |
| Same-version content-drift exceptions | 1 |
| Unknown historical Claim versions remaining | 0 |
| Historical D/E/B transferred to current assessments | 0 |
| Current accepted D/E/B | 0/1,494 |

Combined with the earlier Phase 3 packages (Batch 41: 94; Batches 17 and 21: 12), the original 239-row version gap now has no unknown version labels. Of the 239 rows, 238 have exact historical/current Claim path and Blob SHA equality; one has a same-version content-drift exception.

### VERIFIED — one same-version content-drift exception

- Claim: `CLM-GENERATOR-CO-ALARM-EMERGENCY@1`
- Historical report: `RELEASE/M13-CLAIM-REVIEW-BATCH-19-GENERATOR-CO-HYPOTHERMIA-2026-10-10.md`, line 13, row 1.
- Historical score row: D/E/B = 2/3/3; remains historical-only.
- Historical snapshot: `18d9c1ba150c5b9d4e6d8f4a5b2923cf47ac13d5`.
- Historical Blob SHA: `29c7f166b28510e323f0b391f2bcc37506839ce2`.
- Comparison HEAD: `fde5b351cf2310d7152c5873e25624420c98f56b`.
- Current Blob SHA: `743a7c0ee1003b7b22b80a01f3372b728587820b`.
- Both JSON snapshots explicitly declare `record_version: "1"` and the same record path.

The content-changing commit is `a58294e3af144077d37075d0e73da9f73438101b`, titled “Narrow generator CO emergency claim to CDC-supported advice”. Its diff removes the phrase “в помещение нельзя возвращаться до проверки безопасности” while leaving `record_version` unchanged at `"1"`.

**Disposition:** retain `SAME_VERSION_CONTENT_DRIFT` / integrity HOLD. Preserve both Blob SHAs. Do not silently resolve as an exact content match, transfer the historical score, or edit the canonical Claim in this task. Because this is CO emergency guidance, the removed return-to-building boundary requires a separate high-consequence/source-fit review and a bounded versioning decision.

### VERIFIED — scope boundary

The crosswalks establish Claim-version provenance only. They do not establish historical Evidence Use/Source versions, current passage-level source fit, locator reproducibility, source independence, specialist review, Human View, rights or publication eligibility. Seven repeated-assessment groups remain separately preserved and unadjudicated by this task.

## 6. Commands and verification

| Command/check | Result | Exact SHA / run URL | Notes |
|---|---|---|---|
| GitHub REST commits-by-path for each B18–B40 report | PASS | Exact report commits recorded in the four CSVs | First-parent snapshot used for each report |
| GitHub REST recursive Git trees | PASS | Snapshot-parent SHAs recorded per row | All relevant trees non-truncated |
| Historical/current path + Blob SHA comparison | 132 exact / 1 drift | Comparison HEAD `fde5b351cf2310d7152c5873e25624420c98f56b` | 133 unique IDs, zero missing paths |
| Phase 1 version-inventory cross-check | PASS | `RELEASE/M13-PHASE-1-CLAIM-INVENTORY-2026-11-18.md` | 16 v2 IDs; zero overlap with these 133 |
| Exact JSON inspection for CO exception | PASS | Historical `18d9c1ba...`; current `fde5b351...` | Both version 1; content differs |
| Exact-head CI before this package | 6/6 PASS | `fde5b351cf2310d7152c5873e25624420c98f56b` | Runs: [Reference tests](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044355214), [Release Gate](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044355377), [Offline Edition](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044355247), [M13 Evidence Use Coverage](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044351873), [Offline Edition diagnostic](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044351874), [M13 Audit Queue Automation](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044351840) |
| Exact-head CI after the five evidence artifacts | 4 success / 2 running | `834bd4beefddeb328d452b21c71f26530469f3f2` | Release Gate and Reference tests were still running at inspection; see run IDs 45051253691 and 45051253635. Offline Edition (45051253587, 45051248691), Evidence Use Coverage (45051248684), and Audit Queue Automation (45051248654) completed successfully. |
| Local shell/unit-test commands | NOT RUN | N/A | Work was a read-only Git tree/blob provenance reconstruction plus noncanonical CSV/Markdown artifacts; exact-head CI is the relevant automated verification. |

## 7. Unresolved issues, risks, and blockers

- One same-version content-drift exception remains an integrity HOLD.
- Historical Evidence Use/Source versions for the early report cohorts remain separate work.
- Historical score rationales have not been re-adjudicated; no score reuse is authorized.
- Exact-head CI must be checked again after this report-only commit advances the branch.
- M13 remains OPEN / NOT CLEAN and PR #21 remains Draft/unmerged.

## 8. Not done / not verified

- No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was edited.
- No historical D/E/B value was accepted or transferred.
- No claim was declared scientifically validated or publication-ready.
- No full M13 closure, independent score audit, Human View, specialist review, rights review or release decision was performed.
- No merge, deployment, publication or change to `main` was performed.

## 9. Recommendation and acceptance

- **Recommendation:** accept the 132 exact Blob matches as historical Claim@1 provenance; keep the CO emergency Claim as a separate versioning-integrity HOLD; continue with historical Evidence Use/Source recovery and the required substantive review gates.
- **Acceptance status:** CONDITIONAL
- **Reason:** all 133 historical Claim version labels are identified, but one content-drift exception and the separate evidence/release gates remain open. This does not close M13.

## 10. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/21
- **Report path:** `reports/agent-work/m13-auditor/phase3-batches-18-40-historical-claim-version-recovery-2026-11-22.md`
- **Next owner/action:** M13 auditor — continue historical Evidence Use/Source version provenance; Chief Engineer — coordinate a separate bounded review of the CO Claim's same-version content drift and high-consequence boundary.
