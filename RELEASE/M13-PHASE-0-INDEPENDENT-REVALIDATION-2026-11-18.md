# M13 — Phase 0 independent revalidation (2026-11-18)

Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
PR: #21 (Draft; remains unmerged)  
Inspection basis: `24a01927f0fac4a0e18dc7cebb4a734d30ee3269`  
Disposition: **PHASE 0 NOT CLOSED / NOT RELEASE-READY**

## 1. Scope and method

Read-only inspection of the PR, exact commit trees, current workflow definitions, workflow runs, downloaded workflow artifacts, and canonical records. The inspection basis is the PR head shown above. This report is a new, bounded revalidation record; it does not certify the commit that adds this report. All checks for the resulting commit must be re-run and tied to that exact SHA.

No canonical Claim, Evidence Use, Source, Assessment, or score was modified. No batch was created. PR #21 remains Draft; `main` was not changed.

## 2. Repository and integration state

- PR #21 head: `24a01927f0fac4a0e18dc7cebb4a734d30ee3269`.
- PR base: `e87e5bba60c9ed1101ecd4d53493c968c4760dac`.
- Observed `main`: `d58289f319993ede5294a46f4741a506fd2fd710`.
- PR #21 is 1,352 commits ahead of its base and 0 behind it.
- Compared with current `main`, the PR head is diverged: 1,919 commits ahead and 10 behind, with merge base `203a7028e08da394fd44630fe38727be07bc8849`. This is an integration risk, not authorization to merge or blindly synchronize.
- Exact tree comparison against PR base: 825 changed paths (692 added, 133 modified, 0 deleted). Tree listings were not truncated.

## 3. Exact-head CI observed before this report

The following five workflow runs all identify `24a01927f0fac4a0e18dc7cebb4a734d30ee3269` as `head_sha` and completed successfully:

| Workflow | Run ID | Conclusion |
|---|---:|---|
| Reference implementation tests | 44297443355 | success |
| Release Conformance Gate | 44297443991 | success |
| Offline Edition (pull request) | 44297443452 | success |
| M13 Audit Queue Automation (push) | 44297431442 | success |
| Offline Edition (push) | 44297431590 | success |

The Release Gate report states final conformance `CONFORMING`, 18 gates, no blocking/limiting gates, and 1,041 passing tests. These results apply only to the inspection-basis SHA. They are not evidence of CI for this report's commit.

The workflow definition `.github/workflows/m13-report-coverage.yml` supports `workflow_dispatch` and push on the M13 branch when paths under `RELEASE/M13-**` change. No run for this Generic Evidence Use Report Coverage workflow was found on inspection-basis SHA `24a01927`. Its exact-head result is therefore **NOT RUN / NOT VERIFIED**, not PASS and not FAIL.

## 4. Exact-head artifact reconciliation

Artifacts downloaded from the five successful runs were inspected locally. GitHub-reported artifact digests matched the downloaded ZIP SHA-256 values.

### Corpus and worksheet

The M13 Claim Audit Worksheet artifact records:

- 4,851 records scanned;
- 1,494 Claim records;
- 1,478 Claims at record version 1 and 16 at version 2;
- all 1,494 rows have blank D/E/B scores and rationales;
- all 1,494 rows have `human_review_status = NOT_YET_REVIEWED`.

This is the current generated worksheet state. It does not erase historical assessments; it means those historical rows have not been validated and accepted as current claim-specific assessments in this worksheet.

### Historical scored-row ledger

The exact-head reconciliation summary records:

- 1,501 historical scored-report rows;
- 1,494 unique normalized report IDs;
- 1,494/1,494 inventory Claims with at least one normalized scored-row match;
- zero unmatched scored-report rows;
- seven duplicate groups containing 14 rows;
- one separator-normalized match requiring manual confirmation;
- 163 filename/internal-ID differences: 160 separator-only and three documented filename aliases; zero classified canonical filename/internal-ID mismatches.

This is identifier/accounting reconciliation only. It does not validate exact Claim version applicability, source passage, score rationale, disposition, or independent review. All repeated rows must be preserved until explicit adjudication; no later score is presumed to supersede an earlier one.

### Risk queue and report mentions

The exact-head queue/provenance artifact records:

- 751 Claims without risk-domain or machine-triage metadata;
- 749 of those have at least one configured prior-report ID mention;
- two have no configured-report mention;
- 979 mention rows;
- the mention ledger is explicitly `ID_MENTION_ONLY_REQUIRES_REPORT_BODY_REVIEW`;
- 100 reviewer evidence packets were assembled from repository-local fields only; source text was not fetched and no scores were assigned;
- zero canonical records were modified by queue automation.

A mention is a retrieval lead, not proof of substantive review. Missing risk metadata is not low risk. The 100 selected packets are not a first-pass or completed-review population.

### Evidence linkage

The exact-head linkage artifact records 4,851 record files seen and valid, including 1,494 Claims, 1,679 Evidence Use records, and 627 Sources. It reports 1,117 structural finding rows: 496 generic-material-description candidates, 493 separator-only aliases, 75 duplicate Source URI candidates, 47 source-identity-sentence candidates, and six documented filename aliases. These are machine triage findings, not individually adjudicated defects.

## 5. Specific verification sample

For `CLM-HYDROLOGY_BASICS-C@2`, the canonical Claim, Evidence Use, and Source records at the inspection-basis SHA all identify version 2. The Evidence Use links Claim version 2 to Source version 2 and provides a section/paragraph locator to the USGS Water Science School page. The Batch 43 row 098 report assesses D=3, E=3, B=2 and records HOLD pending exact locator/source-scope, rights, and independent review. This sample confirms internal version linkage for this one Claim only; it does not generalize to all 1,494 Claims.

## 6. Open blockers and Phase 0 decision

1. **Generic Evidence Use Report Coverage:** exact-head run not found on `24a01927`; must run on the new report commit and its artifact must be inspected.
2. **14-ID discrepancy:** remains unresolved. Do not infer or invent the 14 missing identities.
3. **Prior independent REJECT D1–D4:** primary provenance remains unverified; do not describe it as an established independent result.
4. **Seven repeated-score groups:** all 14 rows must be preserved; no approved supersession/adjudication rule has been applied.
5. **Historical score validation:** 1,501 rows are reconciled by normalized ID but not individually validated against exact Claim versions, evidence passages, rationales, or reviewer provenance.
6. **Independent review of this revalidation and its resulting commit:** not yet completed.
7. **PR/main integration:** PR #21 is substantially ahead and diverged from current `main`; do not merge or blindly synchronize.

**Decision: Phase 0 remains OPEN / NOT CLOSED. Phase 1 is not started or authorized by this report.** The next permitted work is to verify all required workflows and artifacts on the commit adding this report, obtain an independent review of this exact report/commit, and resolve or explicitly carry forward the listed provenance and adjudication exceptions. No new Claim batch or canonical-record edits are authorized here.
