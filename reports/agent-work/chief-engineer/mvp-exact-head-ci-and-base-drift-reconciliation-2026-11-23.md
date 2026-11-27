# First Edition MVP — exact-head CI and base-drift reconciliation

Date: 2026-11-23  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: #22  
Exact tested HEAD: `04ff4dd6191995f10513a132249ac608532d1c9b`

## 1. Exact-head technical verification

PR #22 is OPEN / DRAFT / NOT MERGED. The four required workflows all completed successfully on the same immutable HEAD:

| Workflow | Run ID | Result |
|---|---:|---|
| Reference implementation tests | 45152036604 | PASS |
| Offline Edition | 45152036750 | PASS |
| MVP Contribution Form Browser Tests | 45152036722 | PASS |
| Release Conformance Gate | 45152036602 | PASS |

This is an exact-head technical conformance result for the listed workflows. It is not factual/editorial acceptance, rights clearance, Human View approval, owner release authorization, or public deployment approval.

## 2. Included technical hardening

The tested HEAD includes:
- selection-aware offline build schema 1.1 with exact record/version/type/profile/schema pins;
- explicit approval attestations and complete dependency closure;
- source-commit and clean-tree verification;
- fail-closed output isolation (selection output directory must be absent or empty);
- regression tests that prove non-empty directories and file paths are rejected without altering existing data;
- Offline Edition workflow execution of selection-aware and output-isolation tests;
- contribution-form local-only browser workflow with JSON Schema validation, dynamic source/relation controls, conditional requirements, reset, duplicate-ID rejection, keyboard focus, mobile viewport checks and no external requests.

The full-corpus offline build remains a diagnostic/recovery artifact. No real-record INCLUDE allowlist or public first-edition artifact was created.

## 3. Main-base drift

PR #22 records base `main` at `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`. Current `main` is `d58289f319993ede5294a46f4741a506fd2fd710`.

The GitHub compare result reports current main as 8 commits ahead of the recorded base, 0 behind. The eight-commit delta changes only agent instructions, Copilot instructions and the new report template:
- `.github/agents/chief-engineer.agent.md`
- `.github/agents/ci-engineer.agent.md`
- `.github/agents/evidence-researcher.agent.md`
- `.github/agents/m13-auditor.agent.md`
- `.github/agents/security-offline.agent.md`
- `.github/copilot-instructions.md`
- `reports/agent-work/REPORT-TEMPLATE.md`

No canonical encyclopedia content, schema or runtime implementation appears in that main-only delta.

No rebase, retarget, merge, or main-branch modification was performed. The 1,569-commit PR history and the 8-commit base drift remain a separate integration decision; do not infer that a green CI run resolves that integration question.

## 4. Remaining first-edition blockers

The first edition is technically buildable as a controlled offline selection, but no public content selection is authorized:
- Part I inventory: 980/980 records remain HOLD.
- Part II exact-version register: 1,058 candidate keys plus dependency records; inventory coverage is not INCLUDE approval.
- No production selection manifest/allowlist exists.
- Project-authored content licence/rights model, rights holder, accountable editor/release approver, correction/takedown contact, distribution decision and language policy remain owner decisions.
- Item-level third-party rights, editorial review, high-consequence specialist review and Human View remain separate gates.
- Hosted intake remains blocked; the contribution form is local-only and downloads a proposal JSON.

## 5. Protected state

- No canonical Claim/Evidence Use/Source/Context/Scope/Relation was changed by this report.
- No HOLD was promoted.
- No production INCLUDE manifest or allowlist was created.
- No publication, deployment, merge, rebase or retarget was performed.
- PR #22 remains Draft/open/unmerged.
- `main` remains unchanged.

## 6. Next execution order

1. Continue exact source-report and locator reconciliation for M13; do not transfer historical or filename-level mentions into current D/E/B evaluations.
2. Keep first-edition work on the technical side: maintain the selection builder, tests, reproducibility and artifact isolation.
3. Prepare an owner-decision packet for the smallest defensible initial content set, with exact record/version closure and item-level rights evidence. Do not generate INCLUDE decisions or an allowlist from HOLD inventory.
4. Treat the 8-commit main-base delta as a separate integration review; only retarget/rebase after a deliberate conflict and dependency assessment.
5. Keep PR #22 Draft and unmerged until the owner, rights, editorial, Human View and exact release gates are satisfied.
