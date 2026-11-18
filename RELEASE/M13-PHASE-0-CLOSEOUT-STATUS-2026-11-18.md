# M13 — Phase 0 closeout status (2026-11-18)

**Disposition: OPEN / NOT CLOSED / NOT RELEASE-READY.**  
This is a current status reconciliation, not a Phase 0 acceptance, not Phase 1 authorization, and not a merge request.

## 1. Frozen inspection point

| Item | Verified value |
|---|---|
| Repository | `kvantovoebessmertie/encyclopedia-of-civilization` |
| M13 branch | `m13-system-wide-depth-audit-2026-10-09` |
| PR | #21 — open, Draft, unmerged |
| Current M13 HEAD | `e2c35091341f814e394fe40e4154c208a7913a22` |
| PR base | `m12-human-factors-source-and-human-view-2026-10-09` @ `e87e5bba60c9ed1101ecd4d53493c968c4760dac` |
| Current main | `d58289f319993ede5294a46f4741a506fd2fd710` |
| PR delta vs base | 1,355 commits ahead, 0 behind; GitHub PR reports 827 changed files |
| Relation to main | Diverged: 1,922 commits ahead, 10 behind; merge base `203a7028e08da394fd44630fe38727be07bc8849` |

The branch/base relationship is linear, but the branch is substantially diverged from current `main`. This is an integration risk, not permission to merge or synchronize. No merge, rebase, governance overwrite, or main-branch change is authorized here.

## 2. Exact-HEAD CI — complete

All six workflows below report `head_sha = e2c35091341f814e394fe40e4154c208a7913a22` and conclusion `success`.

| Workflow | Run ID | Event |
|---|---:|---|
| Reference implementation tests | 44317324410 | pull_request |
| Release Conformance Gate | 44317324316 | pull_request |
| Offline Edition | 44317324359 | pull_request |
| M13 Audit Queue Automation | 44317309113 | push |
| Offline Edition | 44317309200 | push |
| M13 Generic Evidence Use Report Coverage | 44317309195 | push |

The Reference Tests job completed successfully. Its Release Gate artifact reports **1,041 passed**, final conformance `CONFORMING`, 18 gates PASS, and no blocking/limiting gates. The exact-head release-gate artifact is run 44317324316 / artifact 14432883016 (SHA-256 `0d68a31b92f4ad55b31bfebcf2f63b66f0e29b61706873e448d7cb56f7f9bdfd`).

The Generic Evidence Use Coverage artifact is run 44317309195 / artifact 14433501168. It maps 496/496 generic-EU candidates; all 496 have at least one source-review filename mention. The artifact explicitly uses exact Claim-ID text mentions, not semantic verification; human confirmation remains required. This is coverage evidence, not proof that 496 evidence chains were substantively accepted.

CI proves technical conformance of this exact revision within the declared implementation contour. It does not prove corpus truth, complete Claim review, source adequacy, Human View completion, independent audit, or release readiness.

## 3. Current corpus and audit artifacts

Artifacts generated from the current HEAD:

| Artifact | Run / Artifact ID | Verified result |
|---|---|---|
| Claim audit worksheet | 44317324410 / 14433995042 | 4,851 records; 1,494 Claims |
| Scored-Claim reconciliation ledger | 44317324410 / 14432707398 | 1,501 historical scored rows; 1,494 normalized IDs |
| Evidence-linkage audit | 44317324410 / 14432598119 | 1,117 structural finding rows |
| Review queue and mention ledger | 44317309113 / 14433236530 | source revision matches current HEAD |
| Generic-EU coverage | 44317309195 / 14433501168 | 496/496 mapped and mentioned |
| Release-gate report | 44317324316 / 14432883016 | CONFORMING; 1,041 tests passed |

### 3.1 Claim worksheet

- 1,494 Claims: 1,478 at record version 1 and 16 at version 2.
- All 1,494 worksheet rows currently have D/E/B fields blank.
- All 1,494 have `human_review_status = NOT_YET_REVIEWED`.

This worksheet is the current machine-generated acceptance register. It does not erase historical batch reports; it shows that historical scores have not yet been validated and accepted into this current exact-version register.

### 3.2 Historical scored-row reconciliation

- 1,501 historical scored-report rows.
- 1,494 unique normalized Claim IDs.
- 1,494/1,494 inventory Claims have at least one normalized report-row match.
- Zero unmatched scored-report rows.
- Seven repeated groups / 14 rows.
- One separator-normalized match still requires manual confirmation.
- 163 filename/internal-ID differences: 160 separator-only and three documented aliases; zero classified canonical filename/internal-ID mismatches.

These are identifier/accounting results only. They do not establish that a row assesses the exact current `Claim ID@version`, that its source passage was verified, or that the score is accepted.

### 3.3 Risk queue and report mentions

- 751 Claims have no recorded risk domain or machine-triage flag; this means **UNASSESSED by the risk queue**, not low risk.
- 743 Claims have at least one risk signal; 520 carry the high-consequence screen.
- 734 unassessed candidates after excluding 17 unreconciled holdouts.
- 100 Claims selected in five deterministic lanes of 20.
- 749/751 have configured prior-report ID mentions; two have no match; 979 mention rows.

The 100 selections are routing packets, not a new completed batch. A mention is only a retrieval lead. The queue assigns no D/E/B scores and makes no canonical edits. No additional package is created by this closeout.

### 3.4 Evidence-linkage findings

The static audit reports 1,117 findings:
- 496 generic material-description candidates;
- 493 separator-only filename aliases;
- 75 duplicate Source URI candidates;
- 47 source-identity sentence candidates;
- 6 documented filename aliases.

These are machine-generated structural review signals, not individually adjudicated defects or automatic invalidations.

## 4. Explicit unresolved exceptions

### A. Fourteen unidentified historical Claim IDs — OPEN

A preliminary screen records 17 inspections but names only three exact Claim IDs. The remaining 14 identities have not been recovered from primary evidence. Do not infer IDs from counts, topics, later queue selections, or the separate 17 holdouts. The 14 remain unknown accounting observations, not 14 established unique Claim records.

### B. Historical independent REJECT D1–D4 — provenance UNVERIFIED

The asserted earlier REJECT disposition lacks a confirmed primary report, named reviewer, audited SHA, and supporting artifact. It must not be presented as an independently established result. PR #35's conditional review is not a substitute for the missing primary record.

### C. Seven repeated assessment groups — NOT ADJUDICATED

The seven groups contain six score conflicts and one same-score repeat with different rationales:

- Nuclear physics A: D1 vs D2.
- Nuclear physics B: B3 vs B2.
- Nuclear physics C: D1/E1/B3 vs D2/E1/B2.
- Water treatment A: E2 vs E3.
- Water treatment B: D2 vs D3.
- Water treatment C: E2 vs E3.
- Emergency-water disinfection D: same D3/E3/B3 in both reports; repeated rationale, not an independent second confirmation.

All 14 historical rows must remain preserved. No later date, higher score, or more detailed rationale automatically supersedes another. A comparison report exists at `RELEASE/M13-REPEATED-ASSESSMENT-COMPARISON-2026-11-18.md`; proposed dispositions are not independent approvals. The six conflicts and the repeated same-score group remain unresolved for final-status purposes.

### D. Historical assessment provenance and exact versions — OPEN

The ledger reconciles report IDs, not all 1,501 rows to the exact Claim/Evidence Use/Source versions and source passages actually reviewed at the time. Reviewer identities and some historical snapshot/locator details are missing. A row match is not a completed, current-version substantive review.

### E. Independent review of the current closeout — NOT DONE

The PR has no submitted GitHub reviews at this inspection point. Historical/conditional reviews and agent-produced research notes do not constitute an independent review of this current HEAD or this closeout report.

### F. Separate audit gates — NOT CLOSED

High-consequence content review, source diversity/independence, cross-slice Relation semantics, Human View/adversarial usability, rights/publication suitability, and final human approval remain separate gates. The machine high-consequence flag count (520) is routing, not completion. The structural linkage report is not a semantic Relation audit.

### G. Governance and integration — OPEN

PR #21 is 1,922 commits ahead and 10 behind current `main`. Governance files and report-template differences require explicit three-way reconciliation before any integration. PR #28 remains outside this closeout; do not use it to overwrite governance files. No integration action is authorized.

## 5. Phase 0 exit-criteria decision

| Exit criterion | Status | Reason |
|---|---|---|
| Reproducible full-corpus inventory and exact-head artifacts | **PASS — technical baseline** | 4,851 records / 1,494 Claims; current revision-bound artifacts generated |
| Explicit exceptions and limitations register | **PARTIAL** | Major exceptions are named; 14 IDs and prior REJECT provenance remain unresolved |
| Provenance-backed register for all historical assessments | **OPEN** | 1,501 rows are ID-reconciled, not individually validated to exact versions/passages/reviewers |
| Approved supersession and disposition rules applied to all repeats | **OPEN** | Seven groups have no owner-approved, reviewer-confirmed adjudication |
| Frozen, unique package manifests and complete coverage proof | **OPEN** | Routing packets exist; no accepted full inventory-to-package coverage register or approved Phase 1 partition |
| Independent review of final exact HEAD and closeout | **OPEN** | No submitted PR review for current HEAD |
| Exact-HEAD technical CI | **PASS** | Six of six workflows succeeded on current HEAD |
| Main/PR integration safety | **HOLD** | Branch is diverged from current main; integration not reconciled |

**Decision: Phase 0 is NOT CLOSED. Phase 1 is NOT STARTED and NOT AUTHORIZED.** The 2026-11-16 baseline note that described Phase 0 as passed is historical; subsequent addendum and independent revalidation correctly narrowed that claim. This report preserves that correction.

## 6. Minimal remaining work, in order

1. **Freeze the register contract and reconciliation rule.** Use `Claim ID@version`; preserve original IDs and every historical row. Approve explicit status meanings and supersession rules. Do not treat ID mentions or queue selection as review.
2. **Resolve or formally carry the 14-ID and prior-REJECT provenance exceptions.** Accept only primary evidence; if none exists, retain them as unresolved and state the impact on coverage.
3. **Adjudicate the seven repeat groups.** For each row, identify exact Claim version, historical evidence chain, pinpoint, rationale, and reviewer. Record an explicit decision while retaining both source rows. Do not choose a winner by date or score magnitude.
4. **Build one provenance-backed historical assessment register for all 1,494 Claims.** Link every report occurrence to exact Claim/EU/Source versions, report path/line, source revision/artifact, review scope, reviewer/date where known, passage/locator, D/E/B rationale, and disposition. Unknown values remain unknown.
5. **Complete the separate substantive gates.** High-consequence, evidence diversity/independence, cross-slice Relations, Human View/adversarial usability, rights and publication review. Keep these dimensions separate from D/E/B and technical CI.
6. **Obtain independent review of the resulting exact HEAD and this closeout.** Re-run all required workflows and inspect their artifacts on that exact SHA.
7. **Only after the above, request an explicit Phase 1 authorization.** Any package partition is a later, separately authorized operation; no new Batch/package, canonical record edit, new score, PR conversion, merge, or main synchronization is authorized by this report.

## 7. Change boundary

This closeout records status only. It does not change canonical Claim, Evidence Use, Source, Assessment, Relation, risk metadata, or D/E/B scores. It creates no new Batch or Package, does not authorize Phase 1, does not change PR state, and does not touch `main`.
