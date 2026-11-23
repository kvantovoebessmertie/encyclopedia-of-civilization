# M13 — execution order and closure protocol

Date: 2026-11-16
Branch: `m13-system-wide-depth-audit-2026-10-09`
PR: #21 (Draft; do not merge)
Status: OPEN / NOT RELEASE-READY
Protocol type: execution control; does not itself certify audit completion.

## 1. Purpose

Establish one mandatory, ordered workflow for reconstructing the actual M13 state, reconciling historical work, remediating verified defects, completing substantive assessment, and deciding release readiness. No new screening batch may be created merely to keep batch numbering moving.

## 2. Non-negotiable controls

1. Keep `main` unchanged and PR #21 Draft/unmerged until explicit final release decision.
2. Every result is tied to an exact source revision and exact `Claim ID@version`.
3. Distinguish an ID mention, a desk/content screen, source-passage verification, specialist adjudication, D/E/B assessment, and publication approval. These are different states.
4. A prior score-ledger match is not proof that the score is valid, current, or final.
5. A missing risk signal is UNASSESSED, never LOW RISK.
6. Never infer missing IDs, source passages, locators, authorizations, or approvals.
7. Do not create a new first-pass batch when the reconciled candidate count is zero.
8. Canonical changes require exact bounded authorization, regression coverage, and exact-head CI.
9. Every phase ends with a versioned artifact, reconciliation, and explicit exit criteria.

## 3. Ordered execution phases

### Phase 0 — Freeze and verify the baseline

Capture branch HEAD, PR head/base, base SHA, main SHA, changed-file inventory, exact-head workflow runs, relevant artifacts and digests. Confirm the working tree/PR state before any further write.

Exit criteria: a baseline checkpoint identifies exact SHAs and distinguishes PASS, pending, failed, and not-run checks.

### Phase 1 — Build the authoritative corpus inventory

Regenerate the Claim inventory from the exact baseline. Preserve canonical ID, version, path, slice, linked Evidence Use IDs, Source IDs, and record integrity metadata. Detect duplicate IDs, duplicate versions, path/ID mismatches, missing links, and malformed identifiers.

Exit criteria: one reproducible inventory with stable unique keys and explicit exceptions.

### Phase 2 — Reconstruct historical review provenance

Collect every M13-related report, package, erratum, batch worklist, scored row, ledger, and workflow artifact. For every Claim, record exact report path, line/table location, excerpt, ID match type, package/batch, version if stated, review type, stated disposition, limitations, and artifact/revision provenance.

Do not treat an arbitrary textual mention as a completed review. Classify each occurrence as substantive review evidence, incidental mention, grouped-ID mention, erratum/correction, duplicate, or unresolved.

Exit criteria: a traceable Claim-to-report evidence ledger, with unmatched Claims and ambiguous mentions retained explicitly.

### Phase 3 — Resolve the known 14-ID discrepancy and deduplicate coverage

Reconcile the preliminary report's 17 claimed inspections against its three explicitly named IDs and all later packages/errata. Reconcile Packages 01–32, Batch 53/54 reports, and all later reports without double counting. Preserve exact `Claim ID@version`; aliases are matching aids, not canonical identity changes.

Reconcile the reported 709 prior-report matches, 17 historical holdouts, and 15 overlap against actual per-Claim report evidence. Treat the 711 union as queue accounting, not proof of completed audit.

Exit criteria: every one of the 1,494 Claims has one deduplicated history state; the 14 discrepancy is either resolved with exact IDs and evidence or remains explicitly OPEN with bounded unknowns.

### Phase 4 — Establish the actual remaining-work register

Assign each Claim one or more evidence-backed states: NOT REVIEWED; ID MENTION ONLY; DESK SCREEN; SOURCE PASSAGE VERIFIED; PARTIAL; HOLD; SPECIALIST REVIEW REQUIRED; D/E/B REQUIRED; D/E/B COMPLETE; HUMAN VIEW REQUIRED; RIGHTS REVIEW REQUIRED; READY FOR INDEPENDENT REVIEW; CLOSED. Do not collapse distinct gates into one "reviewed" status.

Exit criteria: exact remaining counts by state, with each count reproducible from the per-Claim ledger.

### Phase 5 — Evidence-chain and source-quality audit

For each in-scope Claim, verify Claim → Evidence Use → Source identity/version → exact source passage/pinpoint → scope/context → independence/contradictions → access/rights. Record the specific defect, severity/rationale, evidence, owner/action, and authorization requirement.

Exit criteria: a defect register linked to exact records and passages; all unresolved items remain HOLD or explicitly pending.

### Phase 6 — Bounded remediation

Prioritize verified high-consequence and high-severity defects. Make only authorized, minimal, versioned changes. Add focused regression tests and update coverage/manifests and dependent relations only where authorization requires. Never silently substitute sources or broaden Claim wording.

Exit criteria: each remediation has before/after evidence, authorization, tests, dependency review, and exact-head CI.

### Phase 7 — Complete D/E/B assessment

Assess Depth, Evidence Quality, and Boundaries for the full required denominator, including validation of historical rows. Record rationale, source pinpoints, reviewer, version, confidence/limitations, and HOLD disposition where evidence is insufficient. Separate provisional desk-screen findings from final scored assessments.

Exit criteria: denominator and numerator reconciled; no missing or duplicate assessment rows; every score traceable and reviewable.

### Phase 8 — System-wide and independent review

Complete cross-slice relation review, evidence diversity/independence review, contradiction and duplication checks, high-consequence specialist review, adversarial review, Human View, and rights/editorial gates.

Exit criteria: each required gate has an explicit result and evidence; unresolved blockers are listed, not waived implicitly.

### Phase 9 — Exact-head technical verification

Run all required CI on the exact final candidate HEAD, including Reference Tests, Release Conformance Gate, Offline Edition, audit automation, coverage, and integrity checks as applicable. Reconcile artifacts to the same SHA. Recheck PR head/base and main.

Exit criteria: all required checks complete successfully on one exact SHA; no stale CI is carried forward.

### Phase 10 — Final M13 decision

Publish a closure report with scope, denominator, status counts, evidence links, residual risks, unresolved exceptions, CI SHA/results, and release recommendation. M13 can be called complete only if all defined substantive gates and technical gates are satisfied. Merge is a separate explicit decision.

Exit criteria: documented GO / NO-GO decision. If any mandatory gate remains unresolved, status remains OPEN / NOT RELEASE-READY.

## 4. Current known starting facts (must be revalidated at Phase 0)

- Historical inventory reports 1,494 Claims.
- The 2026-11-15 queue reconciliation reports 4,834 records scanned, 1,501 scored-report rows, 711 Claims without risk metadata, 709 ID matches in prior risk/content-screen reports, 17 historical holdouts, 15 overlap, and zero fresh candidates.
- The queue report explicitly states that prior report mentions do not certify final D/E/B or risk assessment.
- The 2026-11-14 coverage reconciliation identifies a discrepancy: 17 preliminary inspections claimed, only 3 explicitly named, leaving 14 unresolved at that checkpoint.
- Existing packages contain errata and corrections; package row counts and report mentions must be reconciled against exact Claim IDs and versions.
- The queue pipeline assembles local metadata only; it does not fetch source text, assign scores, or modify canonical records.
- PR #21 must remain Draft/unmerged; `main` must remain unchanged.

These are starting observations, not a fresh certification. Later exact-head artifacts take precedence where they are directly comparable.

## 5. Immediate next action

Execute Phase 0 only: revalidate the exact branch/PR/base/main SHAs, inspect the current mention-ledger implementation and tests, inspect exact-head CI, and verify whether the newly generated provenance ledger is present in a workflow artifact. Do not start Phase 1–3 calculations from stale artifacts until this baseline is recorded.

## 6. Change-control rule

Any change to this protocol must be recorded as a dated, versioned amendment explaining the reason and impact. Do not reorder phases for convenience. A phase may be revisited when new evidence invalidates an earlier result, with the dependency and affected outputs explicitly recorded.

## 7. Amendments

### A1 — 2026-11-17: reconciliation with exact-head findings at `58d73fd685ae6091ad3f9e88c46cb3a7e55e887a`

Reason: the independent Phase 0 audit (REJECT, D1–D4) found §4 and §5 inconsistent with the corrected queue semantics. Sections 1–6 above are historical text and are not rewritten; this amendment supersedes them only where stated. Evidence: `RELEASE/M13-PHASE-0-REVALIDATION-CHECKPOINT-2026-11-17.md`.

1. **Historical counts in §4 (superseded as operational figures).** 711 Claims without risk metadata and 709 prior-report matches were the 2026-11-15 observations; the exact-head figures are 751 and 749 (cause documented in the 2026-11-16 baseline checkpoint §5). The "zero fresh candidates" observation is obsolete: prior ID mentions no longer exclude Claims from the queue (`2a032eb5`), so the exact-head queue reports 734 candidates, 0 `previously_screened_claims_excluded`, 17 `unreconciled_holdout_claims_excluded`, 100 `selected_claims`, 0 `unfilled_slots`. The 711 and 751 unions remain queue accounting, not completed audit.
2. **Control 7 (§2) restated.** The condition "reconciled candidate count is zero" no longer holds as written. No new first-pass batch or screening may be started until Phases 1–3 establish per-Claim history states. The 100 selected Claims all carry prior ID mentions, so they are a routing list, not unseen first-pass work. This is a sequencing rule, not a statement that candidates are zero.
3. **Exclusions.** A Claim may be excluded from the work queue only by an explicitly supplied, exact `Claim ID@version` review disposition verified from report-body evidence. Mentions, score-ledger matches and risk metadata do not qualify.
4. **Phase 0 exit.** Phase 0 requires a checkpoint that names the exact head, the PR base, the `main` SHA and the exact-head runs and artifacts, and that is re-checked after its own commit. The 2026-11-17 checkpoint is the current candidate; Phase 0 is not accepted until independent re-review.
5. **Unchanged.** Phase order, PR #21 Draft status, `main` unchanged, and the 14-ID discrepancy remaining OPEN.
