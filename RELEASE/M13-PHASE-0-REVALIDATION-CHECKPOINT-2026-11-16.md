# M13 — Phase 0 baseline revalidation checkpoint

Date: 2026-11-16  
Purpose: revalidate Phase 0 on the current PR #21 head; this checkpoint does not certify M13 completion or authorize later phases.

## 1. Exact repository and PR state

| Item | Verified value |
|---|---|
| Repository | `kvantovoebessmertie/encyclopedia-of-civilization` |
| PR | #21, open, Draft, unmerged |
| PR head branch | `m13-system-wide-depth-audit-2026-10-09` |
| PR head at revalidation | `83097b28c30b0b385193c9aacdbc85199b7e4e66` |
| PR base branch | `m12-human-factors-source-and-human-view-2026-10-09` |
| PR base SHA | `e87e5bba60c9ed1101ecd4d53493c968c4760dac` |
| Current `main` SHA | `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9` |
| Working tree used for inspection | Clean; inspection was read-only |

The PR base SHA is an ancestor of the PR head. The current `main` SHA is not an ancestor of the PR head. No merge or change to `main` was made.

### Changed-file inventory

The inventory is `git diff --name-only e87e5bba60c9ed1101ecd4d53493c968c4760dac..83097b28c30b0b385193c9aacdbc85199b7e4e66`:

| Top-level path | Files |
|---|---:|
| `.github` | 5 |
| `CONTENT` | 120 |
| `REFERENCE` | 37 |
| `RELEASE` | 649 |
| **Total** | **811** |

SHA-256 of the newline-terminated, Git-sorted path-list produced by that command: `866db29c4311f858f3e7d12969f38e540844cdc9ef2b982ab0c328b02583fbdc`.

The last-five-commit path delta ending at the revalidated head was: `.github/workflows/reference-tests.yml`, `REFERENCE/filename_id_alias_registry.py`, `REFERENCE/m13_claim_scored_report_ledger.py`, `REFERENCE/m13_evidence_linkage_audit.py`, `REFERENCE/tests/test_m13_claim_scored_report_ledger.py`, and `RELEASE/M13-PHASE-0-BASELINE-CHECKPOINT-2026-11-16.md`.

## 2. Reconciliation with earlier checkpoints

Earlier checkpoint statements remain historical facts about their recorded revisions. They are not silently rewritten as facts about this head.

| Artifact | Recorded basis | Previously recorded `main` | Current revalidation |
|---|---|---|---|
| `M13-PHASE-0-BASELINE-CHECKPOINT-2026-11-16.md` | `005470fcb3899b7e5db8dc4f3017e8c1f85f14c2` | `203a7028e08da394fd44630fe38727be07bc8849` | Current PR head is `83097b28c30b0b385193c9aacdbc85199b7e4e66`; current `main` is `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`. The old checkpoint head is an ancestor of the current head. |
| `M13-BLOCK-1-TECHNICAL-INTEGRITY-CHECKPOINT-2026-11-16.md` | audit basis `e0fed0258aa3f5c215a556fc7861806f9e2ace43` | `203a7028e08da394fd44630fe38727be07bc8849` | Current PR head is later; the Block 1 basis is an ancestor of the current head. Its checks and conclusions are not a fresh technical-integrity audit of the current tree. |

The current corpus and queue counts below are from the newly generated exact-head queue artifact; they are not carried forward solely from either older checkpoint.

## 3. Exact-head CI and generated artifact

The following successful runs all identify `83097b28c30b0b385193c9aacdbc85199b7e4e66` as their `head_sha`. The Reference Tests and Release Gate jobs also report successful “Verify exact source revision” steps.

| Workflow | Run ID | Conclusion |
|---|---:|---|
| Reference implementation tests | `43862283081` | success |
| Release Conformance Gate | `43862283109` | success |
| Offline Edition | `43862283084` | success |
| M13 Audit Queue Automation | `43862271881` | success |

M13 Audit Queue Automation artifact `14224480874` was created for the same head. Its ZIP SHA-256 is `809ed890567416231acc79c8ab5d6a081aad1e484aa06ce4104bdf34c45f6595`. It contains the queue JSON/CSV, risk-screen CSV, review evidence packets, runtime metrics, and prior-report mention ledger JSON/CSV. The queue and mention-ledger JSON both record `source_revision` as the exact PR head.

The latest successful M13 Generic Evidence Use Report Coverage run found during revalidation was run `43861993029` on ancestor `65fa048bd0a23a23977cc4a81b6ac134bd120dca`; it is not exact-head coverage. No successful coverage run on the current PR head was identified. CI above predates this checkpoint commit and must not be represented as CI on the checkpoint commit.

## 4. Verified current corpus and queue findings

The exact-head queue artifact reports:

- 4,851 records scanned; 1,494 Claims inventoried.
- 1,501 scored-report rows; zero Claims without a scored-report match. A match is reconciliation metadata, not validation of a score.
- 1,117 structural-finding rows, all classified medium by this pipeline. These are machine-generated findings, not individually adjudicated defects.
- 751 Claims without recorded risk-domain or machine-triage signals.
- Among those 751, 749 have configured prior-report ID mentions and 2 have no configured-report match; the ledger contains 979 report-line mention rows.
- 17 unreconciled holdout Claims, 15 overlapping the prior-report match set; 751 unique exclusions after that overlap.
- Zero fresh candidates selected; all 100 requested queue slots are unfilled.

The accompanying ledger labels matches `ID_MENTION_ONLY_REQUIRES_REPORT_BODY_REVIEW` and unmatched Claims `NO_MATCH_IN_CONFIGURED_REPORTS`. These outputs do not establish substantive Claim review, source-passage support, low risk, finalized D/E/B assessments, rights clearance, or release readiness.

## 5. Outstanding discrepancies and limitations

- The previous Phase 0 report’s discrepancy of 14 Claim IDs—17 inspections claimed but only 3 explicitly identified—remains unresolved. No IDs are inferred or supplied by this revalidation.
- This checkpoint does not regenerate the authoritative 1,494-Claim inventory, reconstruct report-body review provenance, or reconcile all Claims and versions.
- The exact-head queue automation is not a semantic or source-passage audit. Zero fresh queue candidates is not evidence that the underlying Claims are complete or low risk.
- The older Block 1 tree census and coverage reconciliation remain tied to its recorded basis; this checkpoint does not claim a fresh full tree census.
- The Generic Evidence Use Report Coverage result is not exact-head verified, as stated above.
- No Phase 1, Phase 2, or Phase 3 calculations, new batch, or Claim selection are authorized or performed here.

## 6. Protected state and disposition

This is a noncanonical Phase 0 report only. No Claim, Source, Evidence Use, Assessment, canonical record, or audit score was modified or assigned. PR #21 remains Draft and unmerged; `main` remains unchanged.

**Disposition:** Phase 0 facts have been revalidated at baseline head `83097b28c30b0b385193c9aacdbc85199b7e4e66`. This checkpoint does not advance M13 beyond Phase 0. Stop for independent review before any later phase.
