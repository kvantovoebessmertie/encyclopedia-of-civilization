# Agent task report

- **Agent:** CI Engineer
- **Task:** PR #36 task file §2.A — exact-revision and governance verification (report-only)
- **Date (UTC):** 2026-11-17
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** ci-engineer-phase-0-exact-revision-governance-2026-11-17
- **Starting HEAD:** 92d76761bdc6e6d1bdbcfd74608652ae555b4fd3 (M13 tip, `m13-system-wide-depth-audit-2026-10-09`)
- **Final HEAD:** see the Draft PR body / `git log` (a report cannot contain its own commit SHA)
- **Status:** VERIFIED for run/SHA/diff data below; INFERRED where labelled; NOT VERIFIED for approval-gate cause

## 1. Request and acceptance criteria
1. Exact-head CI matrix for M13 tip, PR #34 head, PR #35 head, PR #36 head; explain `action_required` vs `failed`, and why only Offline Edition push runs exist.
2. Inspect `m13-audit-queue.yml` and `m13-report-coverage.yml` for missing exact-revision verification vs the "Verify exact source revision" step; propose bounded fix text **without applying it**.
3. Diff `.github/copilot-instructions.md`, five agent profiles, `REPORT-TEMPLATE.md`: main vs M13.
4. PR #28 overlap: byte-wise comparison; recommend minimum safe conflict-free governance change. PR #28 untouched.

## 2. Scope
- In scope: read-only GitHub API/git inspection; this report file only.
- Out of scope: any change to workflows, `.github/**`, canonical records, main, PR #28, merges/retargets; Phase 1; D/E/B scores.
- Dependencies: `gh` token cannot read repo Actions settings (HTTP 403 on `actions/permissions*`).

## 3. Work performed
Separate worktree `/tmp/wt-ci-engineer`. Queried `actions/runs?head_sha=<SHA>` for each SHA, run detail/jobs/approvals endpoints, `gh pr view` file lists and status rollups, workflow YAML at M13 tip, and `git rev-parse`/`git diff`/`git merge-tree --write-tree` for governance files.

## 4. Files changed
| Path | Change | Reason |
|---|---|---|
| reports/agent-work/ci-engineer/phase-0-exact-revision-and-governance-report.md | added | this report |

## 5. Findings and evidence

### 5.1 Exact-head CI matrix (VERIFIED via `gh api repos/…/actions/runs?head_sha=`)
Run URL pattern: `https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/<ID>`.

| Head SHA | Workflow | Run ID | Event | Branch of run | Conclusion | Approval needed |
|---|---|---|---|---|---|---|
| 92d76761bdc6e6d1bdbcfd74608652ae555b4fd3 (M13 tip) | Offline Edition | 44064343095 | push | m13-system-wide-depth-audit-2026-10-09 | success | no |
| 92d76761… | M13 Generic Evidence Use Report Coverage | 44064343133 | push | m13-… | success | no |
| 92d76761… | M13 Audit Queue Automation | 44064343161 | push | m13-… | success | no |
| 92d76761… | Offline Edition | 44064352984 | pull_request | m13-… (earlier PR with this head, now closed) | success | no |
| 92d76761… | Release Conformance Gate | 44064352915 | pull_request | m13-… | success | no |
| 92d76761… | Reference implementation tests | 44064353436 | pull_request | m13-… | success | no |
| 92d76761… | Offline Edition | 44080381840 | push | chief-engineer-phase-0-remediation-coordination-2026-11-17 (same SHA pushed to PR #36 branch) | success | no |
| fb2b11af62554caf2fb5bee261494cff1d145b94 (PR #34) | Offline Edition | 44077774361 | push | chief-engineer-m13-phase-0-plan-2026-11-17 | **action_required**, 0 jobs | yes (see 5.2) |
| d2861284d3acebb32a4713ba3dab953cc9581b17 (PR #35) | Offline Edition | 44080048182 | push | m13-auditor-phase-0-independent-review-2026-11-17 | **action_required**, 0 jobs | yes |
| a136d6fdd37b436efeaf0b623581a1a20cf52bc7 (PR #36) | Offline Edition | 44080388593 | push | chief-engineer-phase-0-remediation-coordination-2026-11-17 | success (1 job) | no |

Reference (not requested): main d58289f3… has Reference tests 44075859897, Release Gate 44075860613, Offline 44075859896, all push/success. PR #28 head 3127aa64… has only Offline 43865032541 push/success.
Caveat: the M13-tip pull_request runs belong to an earlier PR with that head; they are exact-SHA results but are not evidence for #34–#36. Only one other `action_required` run exists in the latest 200 runs: 44084747651 (Offline Edition, push, branch `security-offline-phase-0-boundary-review-2026-11-17`; head SHA not inspected).

### 5.2 `action_required` vs `failed`
- VERIFIED: runs 44077774361 and 44080048182 have conclusion `action_required` with **zero jobs** — no step executed, so nothing passed or failed. `failure` means jobs ran and a step exited non-zero. `action_required` means GitHub is holding the run for maintainer approval; it is neither pass nor fail.
- VERIFIED: `actions/runs/44077774361/approvals` returns `[]` (no approval recorded). `gh pr view` reports #34/#35 `mergeStateStatus: UNSTABLE`, the rollup of this pending check.
- INFERRED (NOT VERIFIED): why gated. Both heads contain `Copilot`-co-authored commits, whereas #36's head (owner-only commits) ran immediately; the repo's Actions approval policy could not be read (403). Likely approval gating of Copilot-authored pushes; confirm in Settings → Actions → General.
- Remedy (owner action, not performed): "Approve and run" on the two runs. Until then PR #34/#35 heads have **no verified CI result**.

### 5.3 Why only Offline Edition push runs exist (VERIFIED from YAML at 92d76761)
| Workflow | push | pull_request |
|---|---|---|
| offline-edition.yml | **all branches (no filter)** | paths: CONTENT, IMPLEMENTATION, REFERENCE, RELEASE, ROADMAP.md, the workflow |
| reference-tests.yml | `[main, master]` | paths: REFERENCE, schema, CONTENT, ROADMAP, CONTENT-COVERAGE.json, RELEASE/M13-**, workflow |
| release-gate.yml | `[main, master]` | paths: IMPLEMENTATION, REFERENCE, RELEASE, CONTENT, ROADMAP, workflow |
| m13-audit-queue.yml | M13 branch only | none |
| m13-report-coverage.yml | M13 branch only (+paths) | none |

PRs #34, #35, #36 each change exactly one file under `reports/agent-work/**` (`gh pr view --json files`), matching **no** `pull_request` path filter → no pull_request runs (runs API returns 0 for these PRs). Offline Edition is the only workflow with an unfiltered push trigger, so it alone fires on feature-branch pushes. Absence of PR-event runs is expected path-filter behaviour, not a failure; report-only PRs simply get no Reference/Release-gate coverage.

### 5.4 Exact-revision step gaps in M13 workflows (VERIFIED)
Reference step (reference-tests.yml L26–L37; same in offline-edition.yml, release-gate.yml): `ref: ${{ github.event.pull_request.head.sha || github.sha }}`, then `Verify exact source revision` writing expected/actual to `$GITHUB_STEP_SUMMARY` and `test "$actual" = "$EXPECTED"`.

- `m13-audit-queue.yml` L21–25: pins `ref: ${{ github.sha }}` and `persist-credentials: false`, **but has no assertion step and no step-summary record**. Artifact name embeds `github.sha` (L39). `m13_audit_pipeline.py` records `source_revision` in its JSON (partial provenance, not a gate).
- `m13-report-coverage.yml` L26: bare `actions/checkout@v4` (no `ref`, no verification); artifact name `m13-generic-eu-report-coverage` (L39) has **no SHA**; `m13_generic_eu_report_coverage.py` has no revision field (grep: none). Artifacts from different pushes are indistinguishable by name.
- Neither workflow runs on pull_request, so the `pull_request.head.sha ||` fallback is not strictly required; keeping the same expression keeps the idiom uniform.

### 5.5 Proposed bounded fix text (NOT APPLIED)
`m13-audit-queue.yml` — insert after the checkout step (L25), and set checkout `ref:` to `${{ github.event.pull_request.head.sha || github.sha }}`:
```yaml
      - name: Verify exact source revision
        shell: bash
        env:
          EXPECTED_HEAD: ${{ github.event.pull_request.head.sha || github.sha }}
        run: |
          actual_head="$(git rev-parse HEAD)"
          echo "Expected source revision: ${EXPECTED_HEAD}" >> "$GITHUB_STEP_SUMMARY"
          echo "Checked-out source revision: ${actual_head}" >> "$GITHUB_STEP_SUMMARY"
          test "${actual_head}" = "${EXPECTED_HEAD}"
```
`m13-report-coverage.yml` — replace L26 with:
```yaml
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha || github.sha }}
          fetch-depth: 2
          persist-credentials: false
```
add the same verify step directly after, and rename the artifact (L39) to `m13-generic-eu-report-coverage-${{ github.sha }}`. Optional separate change: emit `source_revision` from the coverage script, with a regression test asserting every checkout-using workflow has the verify step. NOT VERIFIED: whether anything consumes the old fixed artifact name (no consumer search done). Not run/tested.

### 5.6 Governance diff, main d58289f3 vs M13 92d76761 (VERIFIED: `git diff`, blob IDs)
| File | main blob | M13 blob | Relationship |
|---|---|---|---|
| .github/copilot-instructions.md | 66f89715… | c2fc7332… | M13 is a **byte-prefix** of main; main adds 14 lines ("Mandatory agent reporting", 7 rules) |
| agents/chief-engineer.agent.md | 241e9553… | 89f8a5b4… | prefix; main adds 4 lines "Mandatory durable handoff" |
| agents/ci-engineer.agent.md | 013ea13c… | 545af2e7… | prefix; +4 "Mandatory CI report" |
| agents/evidence-researcher.agent.md | 43b24b33… | 98e4070b… | prefix; +4 "Mandatory evidence report" |
| agents/m13-auditor.agent.md | 527bb03a… | 5ee0b937… | prefix; +4 "Mandatory audit report" |
| agents/security-offline.agent.md | b2b0d483… | 1cdb19d6… | prefix; +4 "Mandatory security/offline report" |
| reports/agent-work/REPORT-TEMPLATE.md | 2bb5c3dc… | **absent** | main-only (44 lines) |

Main's additions came via PR #33 (commits incl. d2147b43, c179647b). Whole tree: main is 10 commits ahead / 1909 behind M13; `git merge-tree` M13↔main gives 7 conflicts: the six governance files (add/add) plus `REFERENCE/tests/test_content_architecture_basics_vertical_slice.py` (content; not governance — flagged only). M13 also has `m13-audit-queue.yml`, `m13-report-coverage.yml` and exact-head edits to the three shared workflows that main lacks (no conflicts reported there). `reports/agent-work/` does not exist on M13 before report PRs land.

### 5.7 PR #28 overlap (VERIFIED, byte-wise by blob ID)
- PR #28 head 3127aa64313ae1c76075d3c53e44d38e836df325 (base M13, MERGEABLE/CLEAN, 6 files). Its six governance blobs are **identical** to M13's (c2fc7332…, 89f8a5b4…, 545af2e7…, 98e4070b…, 5ee0b937…, 1cdb19d6…); `git diff M13 pr/28 -- .github reports` is empty. It has no REPORT-TEMPLATE.
- Not an ancestor of M13 (5 M13-only / 6 PR-only commits): same content reached M13 by different commits. Remaining M13↔#28 differences are M13-only pipeline/test/RELEASE files, unrelated to #28.
- Net: PR #28 adds nothing M13 lacks; to main it would reproduce the same six add/add conflicts (merge-tree confirmed same 7 conflicts).

### 5.8 Recommendation: minimum safe conflict-free governance change
Every M13 governance file is a strict byte-prefix of main's. Safe change: one bounded sync commit on M13 (separate PR, owner-authorised, NOT performed) setting exactly these seven paths to main's blobs (`git checkout origin/main -- <7 paths>`; expected blobs 66f89715…, 241e9553…, 013ea13c…, 43b24b33…, 527bb03a…, b2b0d483…, 2bb5c3dc…). Then M13 and main hold identical blobs, so the six add/add conflicts vanish on a later M13→main merge and nothing from main is lost. Verify by blob equality and `git merge-tree` showing only the unrelated vertical-slice test conflict. Do **not** resolve by taking M13's version (would drop the mandatory-report rules). PR #28 then becomes stale (merging it into M13 would revert the appended sections): owner should close or supersede it; I did not touch it. The vertical-slice test conflict needs a separate resolution by its owner.

## 6. Commands and verification
| Command/check | Result | Exact SHA / run URL | Notes |
|---|---|---|---|
| `gh api …/actions/runs?head_sha=<SHA>` ×6 | table 5.1 | SHAs in 5.1 | listing per SHA |
| `gh api …/runs/44077774361/approvals` | `[]` | run 44077774361 | no approval recorded |
| `gh api …/actions/permissions*` | HTTP 403 | — | policy unreadable |
| `gh pr view 34/35/36 --json files,mergeStateStatus` | 1 report file each; UNSTABLE/UNSTABLE/CLEAN | PR heads | |
| `git rev-parse <ref>:<path>`, `cmp` prefix check | 5.6/5.7 | main d58289f3, M13 92d76761, pr/28 3127aa64 | |
| `git merge-tree --write-tree` M13↔main, #28↔main | 7 conflicts each | same | no tree modified |
| pytest / validators | **not run** | — | report-only |

## 7. Unresolved issues, risks, and blockers
- #34 and #35 heads have no executed CI (`action_required`); owner approval needed.
- Cause of the gate unproven (settings 403).
- M13 queue/coverage workflows lack revision assertions; coverage artifact name lacks SHA.
- Governance drift main vs M13 will conflict on integration (7 paths).

## 8. Not done / not verified
Workflow changes (proposal only); approval-policy settings; head SHA of run 44084747651; artifact consumers; whether the vertical-slice conflict is semantic; no tests executed. CI for this report's own head is recorded in the Draft PR.

## 9. Recommendation and acceptance
- **Recommendation:** (1) owner approves runs 44077774361 / 44080048182; (2) bounded workflow PR per 5.5; (3) bounded 7-file governance sync per 5.8; (4) owner decides on PR #28.
- **Acceptance status:** CONDITIONAL
- **Reason:** Evidence complete for what was inspected, but exact-head CI on #34/#35 is unverified and the gate cause is inferred.

## 10. Handoff
- **Draft PR:** see PR body (target `m13-system-wide-depth-audit-2026-10-09`)
- **Report path:** reports/agent-work/ci-engineer/phase-0-exact-revision-and-governance-report.md
- **Next owner/action:** repository owner (approve runs; authorise 5.5/5.8 changes); Chief Engineer to integrate.
