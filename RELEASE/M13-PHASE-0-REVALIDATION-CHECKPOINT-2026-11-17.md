# M13 — Phase 0 revalidation checkpoint (2026-11-17)

Date: 2026-11-17  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
PR: #21 (Draft; do not merge)  
Status: OPEN / NOT RELEASE-READY. Phase 0 documentation revalidated against source HEAD `58d73fd685ae6091ad3f9e88c46cb3a7e55e887a`; this checkpoint is not an ACCEPT declaration and does not authorize Phase 1.

This checkpoint resolves the documentation and provenance blockers D1–D4 returned by the independent Phase 0 audit of 2026-11-17. It is noncanonical. No Claim, Evidence Use, Source, Assessment or other canonical record was modified, no D/E/B score was assigned, and no batch was created.

## 1. Supersession of earlier Phase 0 checkpoints

The two 2026-11-16 Phase 0 checkpoints are preserved unchanged as historical records of the revisions they name. For operational purposes they are superseded as follows.

| Historical record | Recorded basis | Status after this checkpoint |
|---|---|---|
| `RELEASE/M13-PHASE-0-BASELINE-CHECKPOINT-2026-11-16.md` | HEAD `005470fcb3899b7e5db8dc4f3017e8c1f85f14c2`, `main` `203a7028e08da394fd44630fe38727be07bc8849` | Historical. Its `main` SHA, CI and artifact IDs, and queue figures (751 / 749 / 15 overlap / zero candidates) do not describe the current HEAD. The 711→751 explanation (§5 there) and the structural observations remain valid history. |
| `RELEASE/M13-PHASE-0-REVALIDATION-CHECKPOINT-2026-11-16.md` | PR head `83097b28c30b0b385193c9aacdbc85199b7e4e66`, `main` `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9` | Historical. Its statements "751 unique exclusions", "zero fresh candidates selected; all 100 requested queue slots are unfilled" and "Generic Evidence Use Report Coverage is not exact-head" were true for that head but are superseded by §3–§5 below. |

The queue-semantics change that made those statements obsolete is three commits after `83097b28`: `2a032eb5` (stop using prior ID mentions as queue exclusions), `247a488d` (regression test), `58d73fd6` (comment and interpretation text clarification). The corrected semantics are retained and not reverted.

## 2. Exact repository state

| Item | Verified value |
|---|---|
| Source HEAD under revalidation | `58d73fd685ae6091ad3f9e88c46cb3a7e55e887a` |
| PR | #21, open, Draft, unmerged |
| PR base branch / SHA | `m12-human-factors-source-and-human-view-2026-10-09` / `e87e5bba60c9ed1101ecd4d53493c968c4760dac` (GitHub compare: PR base is an ancestor of the source HEAD; behind by 0) |
| `main` SHA (verified 2026-11-17) | `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9` ("Prepare Copilot specialist agents for cloud sessions (#31)") |
| `main` relation to branch | Diverged: `main` also holds `fadb915a` (#30, a vertical-slice source-provenance test). `main` was not merged into this branch and was not modified. |

### 2.1 Specialist configuration files (D3)

The M13 branch did not contain `.github/copilot-instructions.md` or `.github/agents/`. The six files were copied byte-for-byte (verified with `cmp`) from `main` commit `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`, not by merging `main`:

- `.github/copilot-instructions.md`
- `.github/agents/chief-engineer.agent.md`
- `.github/agents/ci-engineer.agent.md`
- `.github/agents/evidence-researcher.agent.md`
- `.github/agents/m13-auditor.agent.md`
- `.github/agents/security-offline.agent.md`

They are present on the branch at the commit that adds this checkpoint (not at `58d73fd6`). No other `main`-only change (such as `fadb915a`) was brought over.

## 3. Changed-file inventory (D4)

Command: `git diff --name-only e87e5bba60c9ed1101ecd4d53493c968c4760dac..58d73fd685ae6091ad3f9e88c46cb3a7e55e887a`, bytewise-sorted, newline-terminated.

| Top-level path | Files at source HEAD `58d73fd6` | Files after this checkpoint commit |
|---|---:|---:|
| `.github` | 5 | 11 |
| `CONTENT` | 120 | 120 |
| `REFERENCE` | 37 | 37 |
| `RELEASE` | 650 | 651 |
| **Total** | **812** | **819** |

- SHA-256 of the path list at `58d73fd6`: `f9295043da7976b570724d53c293d0268ed9f44457a2dd49fb167536d9efc669`.
- SHA-256 of the expected path list after this checkpoint commit (the 812 paths plus the six configuration files and this checkpoint file; the protocol amendment edits an already-listed path): `a9e27ede2c398b8edf04b6af2f9a1b2c4f232ffca823ba7e18aa25dfb6886680`.

Both are computed from path names only; the second must be re-derived against the final PR head and reported there. The earlier 811-file inventory (hash `866db29c…fbdc`) belonged to `83097b28`; the +1 is the 2026-11-16 revalidation checkpoint itself.

## 4. Exact-head workflow evidence at `58d73fd6` (D4)

All runs below list `head_sha = 58d73fd685ae6091ad3f9e88c46cb3a7e55e887a` and conclusion `success`. "Verify exact source revision" is a workflow step that exists in the Reference, Release Gate and Offline workflows only.

| Workflow | Run ID | Event / branch | Exact-revision step |
|---|---:|---|---|
| Reference implementation tests | 43960960770 | pull_request / M13 branch | success; pytest summary in job log: 1040 passed |
| Release Conformance Gate | 43960960514 | pull_request / M13 branch | success; report `CONFORMING`, no blocking or limiting gates, 1040 passed |
| Offline Edition | 43960960477 | pull_request / M13 branch | success |
| Offline Edition | 43960952175 | push / M13 branch | success |
| Offline Edition | 44056117060 | push / `m13-agent-configuration-2026-11-17` | success (different branch, same SHA) |
| M13 Audit Queue Automation | 43960952064 | push / M13 branch | "Checkout exact revision" success; no separate verify step |
| M13 Generic Evidence Use Report Coverage | 44058713946 | workflow_dispatch / M13 branch | no exact-revision verification step; run `head_sha` matches |

The 2026-11-16 checkpoints state 1 039 tests; at `58d73fd6` the count is 1040 (the regression test added by `247a488d`).

### 4.1 Artifacts

| Artifact | Run / artifact ID | Digest (SHA-256) |
|---|---|---|
| `m13-review-queue-58d73fd685ae6091ad3f9e88c46cb3a7e55e887a` (queue, mention ledger, risk-screen CSV, evidence packets, metrics) | 43960952064 / 14273229948 | `b2ba681a223d7cadc9ac95894f5e6a29cb2cb70030f26bec19a542eff9cfdf3a` (ZIP; re-downloaded and re-hashed locally, identical) |
| `m13-claim-audit-worksheet` | 43960960770 / 14273891513 | `433b0070bc33d47c34531f800347dbd3377616fb1aedda454910e254da0e3e19` |
| `m13-scored-claim-reconciliation-ledger` | 43960960770 / 14274881138 | `eba627cb0ab01429a73b4dcaa9073164dc18b5785b40875c8d6d8db7847a0f84` |
| `m13-evidence-linkage-audit` | 43960960770 / 14274786166 | `a17b1eb449e4962ec181e5c9e6bc33c256fb45949f32f2c77c22aa637b05ac18` |
| `release-gate-report` | 43960960514 / 14273359061 | `d04304189dc9485a2652eff95b6afdc8e8d71731888c5ae5620c0e81b81e0491` |
| `encyclopedia-offline-edition` | 43960960477 / 14275180396 | `898efcdf7ef2ec46d96c7eea2489c4fc4e07b9d95625e6d1717d4720a9b60b31` |
| `m13-generic-eu-report-coverage` | 44058713946 / 14316549056 | `d1990ecb6256f327066c233e409e94c74aac97c88b0a0aad6e7c89950666ce44` |

Queue and mention-ledger JSON record `source_revision = 58d73fd685ae6091ad3f9e88c46cb3a7e55e887a`.

CI evidence above applies to source HEAD `58d73fd6` only. It is not evidence for the commit that adds this checkpoint; that commit's runs are recorded outside this file, because a document cannot contain the SHA of its own commit.

## 5. Reconciled queue figures from the exact-head artifact (D2)

Source: `m13-automation-queue.json` and `m13-prior-report-mention-ledger.json` in artifact 14273229948.

| Figure | Value |
|---|---:|
| Records scanned | 4,851 |
| Claims inventoried (unique IDs; a working-tree count of `record_type: claim` records also found 1,494 unique IDs, 1,478 at version 1 and 16 at version 2) | 1,494 |
| Scored-report rows / Claims with no scored-report match | 1,501 / 0 |
| Structural finding rows (all severity medium, machine-generated) | 1,117 |
| Claims with any risk signal / high-consequence screen | 743 / 520 |
| Claims without risk-domain or machine-triage metadata (UNASSESSED) | 751 |
| `candidate_unassessed_risk_claims` | 734 |
| `previously_screened_claims_excluded` | 0 |
| `unreconciled_holdout_claims_excluded` | 17 |
| `reviewed_holdout_overlap` | 0 |
| `unique_unassessed_claims_excluded` | 17 |
| `selected_claims` / `unfilled_slots` / lanes | 100 / 0 / 5 × 20 |

Arithmetic check: 751 UNASSESSED − 17 holdouts = 734 candidates. Reported as an observed identity, not used to infer any ID.

### 5.1 Why historical figures changed

| Historical figure | Where | Disposition |
|---|---|---|
| 711 Claims without risk metadata, 709 mentioned | Protocol §4; 2026-11-15 queue report | Historical. Superseded by 751 / 749; the cause (`OpenStax` matched as `tax`) is documented in the 2026-11-16 baseline checkpoint §5. |
| 751 / 749 / 17 holdouts / 15 overlap / zero candidates / 751 exclusions | 2026-11-16 checkpoints | 751 / 749 / 17 remain correct as counts. "15 overlap" and "751 exclusions" came from using mentions as exclusions; that use was removed. "Zero candidates" is obsolete: 734 candidates, 100 selected. |
| 15 holdout–mention overlap | Baseline §4.3 | Not computed by the queue any more (`reviewed_holdout_overlap` is 0 because nothing is treated as reviewed). The mention ledger still shows 15 of the 17 holdouts with mentions and 2 (`CLM-DISASTER_RISK_REDUCTION_BASICS-C`, `CLM-HYDROPOWER_BASICS-C`) without; this is unchanged. |

### 5.2 Mentions are not completed assessments

- The mention ledger covers 751 Claims: 749 `ID_MENTION_ONLY_REQUIRES_REPORT_BODY_REVIEW`, 2 `NO_MATCH_IN_CONFIGURED_REPORTS`; 979 report-line mention rows. Every row is a retrieval lead only.
- All 100 currently selected Claims have at least one prior-report ID mention. The selected set is therefore a deterministic routing list that overlaps previously mentioned (and possibly screened) Claims. It is not a first-pass batch of unseen Claims, and it is not a determination that any of those Claims was or was not substantively reviewed.
- No substantive completed assessment was identified or counted at this checkpoint. Report bodies for the 47 configured documents were not read. A match in the scored-report ledger remains reconciliation metadata, not validation of a score.
- Risk and routing flags are machine heuristics. A missing risk signal is UNASSESSED, not low risk.

## 6. Open items retained as unknowns

- 14-ID discrepancy: the preliminary screen claims 17 inspections and names 3 IDs; 14 remain unidentified and OPEN (`RELEASE/M13-UNASSESSED-RISK-SCREEN-COVERAGE-RECONCILIATION-2026-11-14.md`). Not resolved here; no IDs inferred.
- 7 repeated-score groups (14 rows) have no stated supersession rule.
- Two suspected over-classifications (`CLM-MANUFACTURING_SYSTEMS_BASICS-C`, `CLM-MATTER_BASICS-A`) await rule calibration.
- 163 filename/internal-ID differences (160 separator-only, 3 documented `web-systems-basics` aliases) are recorded, not normalized.
- The mention ledger covers only the 751 Claims without risk metadata, not all 1,494.
- Phase 1–3 work (authoritative inventory, report provenance, deduplication) has not started. The 16 version-2 Claims must be handled as exact `Claim ID@version` there.
- No exact-head verification step exists in the Audit Queue and Generic EU Coverage workflows beyond the `head_sha` recorded by GitHub.

## 7. Disposition

D1–D4 are addressed by this checkpoint, the protocol amendment A1, and the configuration files. The disposition remains **OPEN / NOT RELEASE-READY**. CI on the commit adding this checkpoint, and an independent re-review, are required before Phase 0 can be called accepted. No Phase 1 start, no batch, no canonical change, and no merge is authorized.
