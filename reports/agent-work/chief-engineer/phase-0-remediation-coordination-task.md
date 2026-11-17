# Chief Engineer Task — Phase 0 Remediation Coordination

- **Date (UTC):** 2026-11-17
- **Role:** Chief Engineer
- **Target branch:** `m13-system-wide-depth-audit-2026-10-09`
- **Baseline M13 HEAD:** `92d76761bdc6e6d1bdbcfd74608652ae555b4fd3`
- **Inputs:** Chief Engineer current-state report (PR #34); independent M13 Auditor report (PR #35).
- **Purpose:** Coordinate closure of Phase 0 conditions. This is not authorization to start Phase 1.

## 1. Read first and verify live state

Read the complete reports:
- `reports/agent-work/chief-engineer/m13-phase-0-current-state-and-plan.md` (PR #34)
- `reports/agent-work/m13-auditor/phase-0-independent-review.md` (PR #35)

Re-query live PRs #21, #28, #34, #35; branch tips; main; and exact-head CI. Do not assume the SHAs below remain current. Preserve the audited baseline `92d76761bdc6e6d1bdbcfd74608652ae555b4fd3` as a historical reference.

Auditor verdict: **CONDITIONAL ACCEPT** of Phase 0 baseline facts; **Phase 1 is not authorized**.

## 2. Coordinate bounded specialist work

Create a non-overlapping task ledger and coordinate the existing profiles. Do not claim that a specialist session has started unless its report/commit is published.

### A. CI Engineer — exact-revision and governance verification
- Recheck CI on the current M13 tip and on PR #34 and PR #35 heads; record exact SHA, workflow, run ID, conclusion and any approval requirement.
- Investigate PR #34's reported `action_required` state and distinguish approval-gated from failed checks.
- Inspect the Audit Queue and Generic Evidence Use Coverage workflow YAML for missing exact-revision verification steps.
- Compare `.github/copilot-instructions.md`, all five agent profiles and `reports/agent-work/REPORT-TEMPLATE.md` on current `main` versus M13.
- Coordinate the overlap with PR #28. Recommend the minimum safe, conflict-free governance change. Do not merge, retarget, or rewrite PR #28 without explicit owner authorization.
- Deliver a report-only Draft PR to M13 with exact evidence.

### B. Evidence Researcher — unresolved provenance and 14 IDs
- Search repository history, all relevant reports, workflow artifacts and available branch/commit history for the original 17-item preliminary screen and its 14 unnamed Claim IDs.
- Do not infer identities from thematic similarity, the 17 queue holdouts, or current queue membership.
- If IDs cannot be recovered, document exactly which sources and artifacts were searched and retain the 14 as unresolved.
- Search for the referenced prior independent Phase 0 REJECT (D1–D4): locate the original report/artifact, exact SHA, date, author/agent and evidence. If not found, state that provenance remains unverified.
- Deliver a report-only Draft PR to M13. No canonical edits.

### C. Security & Offline — independent boundary review
- Review relevant M13 workflows, artifact handling, offline build boundary, permissions, and proposed governance synchronization.
- Check for unintended writes to canonical records, network dependencies in offline paths, secret exposure, unsafe artifact trust, and branch/PR boundary violations.
- Report only concrete findings with file paths, lines, reproduction/evidence, severity and remediation.
- Do not change workflows or canonical records; propose bounded fixes separately.

### D. M13 Auditor — clarification follow-up (not a new full audit)
- Review any remediation reports and verify that the auditor's conditions are addressed.
- Specifically preserve the distinction between a scored row, a queue entry, a mention, and a substantive claim-specific review.
- Do not assign new D/E/B scores or certify the 1,501 rows uniformly.

## 3. Required Chief Engineer deliverable

Create:
`reports/agent-work/chief-engineer/phase-0-remediation-coordination-report.md`

The report must include:
1. Live repository/PR/branch SHAs and exact-head CI matrix.
2. A traceable mapping from every Auditor condition/finding (C1–C3, F-1–F-10) to owner, evidence, status and acceptance criterion.
3. Separate task status for CI Engineer, Evidence Researcher and Security & Offline; distinguish assigned from actually completed.
4. PR #28 overlap decision and minimal governance-sync proposal.
5. Reconciliation of the queue/scored-row interpretation and proposed checkpoint addendum (new dated addendum; do not silently rewrite historical checkpoint).
6. The 14 IDs and prior REJECT provenance: recovered with evidence or explicitly unresolved.
7. Remaining blockers and a clear Phase 0 recommendation: ACCEPT / CONDITIONAL ACCEPT / REJECT.
8. Explicit statement that Phase 1 remains unauthorized absent separate owner approval.

Publish the report on a dedicated branch and open a Draft PR targeting `m13-system-wide-depth-audit-2026-10-09`.

## 4. Mandatory safeguards

- Do not modify `main`.
- Do not merge any PR or close/retarget #28, #34 or #35.
- Do not edit canonical Claim, Evidence Use, Source, Relation or risk-metadata records.
- Do not start Phase 1, create new Claim batches, or assign D/E/B scores.
- Do not equate prior scored rows with substantive review or certification.
- Do not equate the 14 unnamed IDs with the 17 holdouts.
- Do not claim agent work is complete without a published artifact and exact SHA.
- Recheck CI on exact commit heads; empty status results are not proof of success.
- Stop and report any missing access, artifacts or ambiguous evidence.

## 5. Handoff format

Return:
- report path and Draft PR URL;
- exact final commit SHA;
- exact-head CI evidence (or explicit pending/approval-required state);
- task status for each specialist (assigned / published / blocked);
- remaining blockers;
- one recommended next action.

**No Phase 1 authorization is granted by this task.**
