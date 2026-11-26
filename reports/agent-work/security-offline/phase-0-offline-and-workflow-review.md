# Agent task report

- **Agent:** security-offline
- **Task:** Phase 0 independent boundary review (PR #36 task file §2.C): M13 workflows, artifacts, offline build boundary, permissions, triggers, write-back, network, secrets, action pinning, proposed 7-file governance sync
- **Date (UTC):** 2026-11-17
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** security-offline-phase-0-boundary-review-2026-11-17 (from `origin/m13-system-wide-depth-audit-2026-10-09`)
- **Starting HEAD:** 92d76761bdc6e6d1bdbcfd74608652ae555b4fd3 (reviewed tree; `main` = d58289f319993ede5294a46f4741a506fd2fd710)
- **Final HEAD:** the commit containing this report (see Draft PR body; a commit cannot name its own SHA)
- **Status:** VERIFIED for items labelled VERIFIED; the rest as labelled. Report-only; no workflow, `.github/**` or canonical record changed.

## 1. Request and acceptance criteria
Report only concrete findings (path, lines, evidence, severity) and bounded remediation proposed separately. State explicitly when there is no finding. Do not change workflows or canonical records. No D/E/B scores; no Phase 1.

## 2. Scope
- In scope: `.github/workflows/*.yml` (5 files) at 92d76761; `REFERENCE/build_offline_edition.py`, `REFERENCE/src/encyclopedia_reference/offline_edition.py`; default output paths of M13 scripts; diff of the 7 governance files `main` vs M13.
- Out of scope: content/claim review, safety certification of any practical instruction, repository/org settings (not readable by this session), run logs.
- Dependencies: PR #36 task file (read); PR #34/#35 reports (not re-read in full; not needed for these findings).

## 3. Work performed
Read all five workflows with line numbers; grepped for secrets/write-back/trigger constructs; read the offline builder; reproduced HTML injection with a synthetic record; built the offline edition twice from the real corpus and compared SHA-256s; diffed the 7 governance files and the workflows `main` vs M13.

## 4. Files changed
| Path | Change | Reason |
|---|---|---|
| reports/agent-work/security-offline/phase-0-offline-and-workflow-review.md | added | this report |

## 5. Findings and evidence
Line numbers are file-relative at 92d76761.

### Summary
| ID | Severity | Status | Title |
|---|---|---|---|
| SEC-1 | Medium | CONFIRMED (repro) | Offline `index.html` embeds record fields unescaped (stored HTML/script injection) |
| SEC-2 | Low | CONFIRMED (static) | `offline-edition.yml` and `reference-tests.yml` have no `permissions:` block; checkout keeps credentials |
| SEC-3 | Low | CONFIRMED (static) | Actions pinned by mutable tag; Python deps unpinned/unhashed; build not hermetic |
| SEC-4 | Low / Info | CONFIRMED (static) | `m13-report-coverage.yml` and `m13-audit-queue.yml` lack exact-revision verification; coverage artifact not SHA-bound |
| SEC-5 | Low | CONFIRMED (static) | M13 script defaults write inside `RELEASE/` (canonical area) if run without `--output-dir` |
| SEC-6 | Info | THEORETICAL | Manifest hashes are unsigned and do not cover the manifest itself |

### SEC-1 — Medium — unescaped HTML in offline edition (VERIFIED by reproduction)
- Evidence: `REFERENCE/src/encyclopedia_reference/offline_edition.py` lines 24–25 concatenate `r["record_id"]`, `r["record_type"]`, `r["record_version"]` and `json.dumps(r["content"])` into HTML with no `html.escape`. `json.dumps` does not escape `<`, `>`, `&`.
- Reproduction (run in worktree, `PYTHONPATH=REFERENCE/src`): `build_offline_edition` with a synthetic record `record_id="X<img src=x onerror=alert(1)>"`, `content={"t":"</pre><script>alert(1)</script>"}`. Result: output `index.html` contains `<script>alert(1)</script>` and the `<img onerror>` verbatim (printed `True True`).
- Why tests miss it: `REFERENCE/tests/test_offline_edition.py` line 27 only checks for external `src/href=http(s)`; it does not test escaping.
- Precondition: a record containing markup reaches `CONTENT/vertical-slices/*/records/*.json` (e.g. via the contribution intake work in PRs #26/#27, CITED only, not reviewed) and a user opens the distributed `index.html` locally (file://, same-origin access to sibling `records.json`). Current corpus: 0 of the records have HTML-like tags in `content` (VERIFIED by regex scan limited to the `content` field; `record_id`/`type`/`version` not scanned) → no current exploit; latent.
- Impact: script execution in the reader's browser from a durable, redistributed artifact; breaks the "no network, safe offline" promise; also CI artifact `encyclopedia-offline-edition` carries it.
- Related: open PR #24 "Fix HTML escaping in offline edition" (CITED from `gh pr list`; its content and CI NOT VERIFIED).

### SEC-2 — Low — permissions / credentials (VERIFIED static)
- `offline-edition.yml` (no `permissions:` anywhere; triggers lines 3–10) and `reference-tests.yml` (no `permissions:`; lines 1–15): token scope falls back to the repository default, which this session cannot read → NOT VERIFIED whether it is read-write. Contrast: `m13-audit-queue.yml` line 9, `m13-report-coverage.yml` line 14 (top-level `contents: read`) and `release-gate.yml` line 26 (job level).
- `actions/checkout@v4` without `persist-credentials: false` in offline-edition (line 20), reference-tests (line 26), release-gate (line 30), m13-report-coverage (line 26): the token stays in `.git/config` while PR-supplied code runs (`pip install -e REFERENCE` executes setup code; scripts under REFERENCE run). Only `m13-audit-queue.yml` line 22–24 sets it false.
- Preconditions/impact: needs a malicious PR whose workflows run with write-capable token; for fork PRs GitHub forces read-only, so the realistic exposure is same-repo branches. Low.
- Absent (VERIFIED by grep over `.github/workflows`): `pull_request_target`, `workflow_run`, `secrets.`, `GITHUB_TOKEN`, `id-token`, `contents: write`, `git push/commit/add`, `download-artifact`. **No write-back or secret exposure finding.**

### SEC-3 — Low — supply chain / network dependency in the build path (VERIFIED static)
- All actions use mutable tags: `actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4` (every workflow). No commit-SHA pins.
- `pip install -e "REFERENCE[test]"` (offline-edition line 37; reference-tests line 42; release-gate line 48) pulls `jsonschema>=4.23,<5`, `pytest>=8,<9` (`REFERENCE/pyproject.toml`) from PyPI with `setuptools>=68` as build backend; no lock file or hashes (`git ls-files` finds no requirements/lock file). Not reproducible over time; CI build needs network.
- Boundary note (VERIFIED): the *built offline edition* has no network need (`network_required: False`, no `http(s)` in generated HTML for the current corpus) and the builder itself imports only stdlib (`hashlib, json, sqlite3, pathlib`). The network dependency is CI-build-time only.
- Positive (VERIFIED): two consecutive builds from the real corpus produced identical SHA-256 for all 6 output files (deterministic).

### SEC-4 — Low/Info — provenance gaps in M13 workflows (VERIFIED static)
- `m13-report-coverage.yml` line 26: `actions/checkout@v4` with no `ref`/verify step; artifact name `m13-generic-eu-report-coverage` (line 39) has no SHA, retention 14 days; push-only on M13 branch with path filters, so a PR head is never built.
- `m13-audit-queue.yml` line 22–24 checks out `github.sha` (correct for push) but has no verification step; artifact is SHA-named (line 39), retention 90 days, holds claim queues/evidence packets. Artifacts are unsigned and consumed by nobody automatically (no `download-artifact`), so the trust issue is human-consumption only.
- `reference-tests.yml` lines 48–53: `if: always()` upload step runs even after failed generation with `if-no-files-found: warn` (worksheet) — a partial artifact can look like a result. Low. Exact-revision verification itself is CI Engineer scope; noted here only for provenance.
- Trigger note: `offline-edition.yml` line 6 `push:` has no branch filter (every branch push builds) plus `pull_request` with paths → duplicate runs on PR branches; no security impact.

### SEC-5 — Low — default writes into canonical area (VERIFIED static)
- Defaults: `m13_audit_pipeline.py` line 499 → `RELEASE/m13-automation-run`; `m13_claim_audit_inventory.py` line 133, `m13_claim_scored_report_ledger.py` line 263, `m13_evidence_linkage_audit.py` line 157 → `RELEASE/m13-*`; `release_gate.py` line 151 always writes `RELEASE/release-gate-report.json`. Workflows pass `/tmp/...` for the first four (VERIFIED), so CI does not write into RELEASE (the gate report is written into the ephemeral workspace and uploaded). Local developer/agent runs without arguments would create untracked generated files under `RELEASE/`. No canonical RECORD/CLAIM/EVIDENCE file is written by any reviewed script (VERIFIED: write calls target only output dirs / `RELEASE/release-gate-report.json`; `git status` clean after my builds apart from `__pycache__`).

### SEC-6 — Info (theoretical)
- `offline_edition.py` line 33: manifest lists SHA-256 of 5 files, not of itself, and no signature/verification tool is referenced. Detects accidental corruption only, not tampering by someone who can rewrite the manifest. The manifest correctly states "packaging and integrity do not establish truth".

### Governance synchronization (7 files from `main`) — NO finding on privilege/secrets (VERIFIED)
Diff `92d76761..origin/main` for `.github/copilot-instructions.md` (+14), the 5 `.github/agents/*.agent.md` (+4 each) and new `reports/agent-work/REPORT-TEMPLATE.md` (+44; absent on M13): added text is only a mandatory-report-and-Draft-PR rule block. No tools, permissions, network, secret, auto-merge, push-to-main or write-scope changes; existing prohibitions (no main, no merge, no canonical edits, Draft only) are retained. 
- Caution (VERIFIED): `main` vs M13 also differs in workflows: M13 has `m13-audit-queue.yml`, `m13-report-coverage.yml` and the exact-revision steps that `main`'s `offline-edition.yml`, `reference-tests.yml`, `release-gate.yml` lack. A whole-tree/merge-style sync would regress or delete those. The sync must be path-limited to exactly the 7 files.
- Note: new rule requires agents to commit and push reports and open PRs — operationally a write instruction, but bounded to `reports/agent-work/**` and Draft PRs.

## 6. Commands and verification
| Command/check | Result | Exact SHA / run URL | Notes |
|---|---|---|---|
| `grep -rnE "secrets\.\|git (push\|commit\|add)\|download-artifact\|pull_request_target\|workflow_run\|GITHUB_TOKEN\|id-token\|contents: write" .github/workflows` | no matches | 92d76761 | |
| `git diff HEAD origin/main -- <7 files>` | additions only, as above | 92d76761 vs d58289f3 | |
| synthetic-record `build_offline_edition` | script/img injected verbatim | 92d76761 | SEC-1 |
| `build_offline_edition.py --output /tmp/o1` and `/tmp/o2`, `sha256sum` diff | identical | 92d76761 | deterministic |
| regex scan of record `content` for HTML tags | 0 hits | 92d76761 | `content` field only |
| CI run on this report's head | see Draft PR | NOT VERIFIED at time of writing | |

## 7. Unresolved issues, risks, and blockers
SEC-1 (latent) is open on M13; PR #24 may address it. Repo-level Actions settings (default token perms, fork-approval, branch protection) unreadable here.

## 8. Not done / not verified
Repository settings; actual run logs/artifacts; contents of PRs #24/#26/#27/#28/#29; `pytest` suite not run; safety review of practical instructions (health/chemical/electrical/fire/water/food) not performed; `record_id/type/version` fields not scanned for markup; PyPI/wheel integrity not tested.

## 9. Recommendation and acceptance (proposals only; nothing implemented)
1. SEC-1: `html.escape()` all interpolated fields (and `edition_id`) in `offline_edition.py`; add regression test with the synthetic record above; add a CSP `<meta>` (`default-src 'none'; style-src 'unsafe-inline'`). Prefer reviewing/landing PR #24 rather than duplicating.
2. SEC-2: add `permissions: contents: read` to `offline-edition.yml` and `reference-tests.yml`; `persist-credentials: false` on all checkouts.
3. SEC-3: pin actions to full commit SHAs (Dependabot for updates); add a hash-pinned constraints file for CI.
4. SEC-4: coordinate with CI Engineer: add the exact-revision step to the two M13 workflows; SHA-name the coverage artifact.
5. SEC-5: make `--output-dir` mandatory or default to a temp/`/tmp` path; ignore `RELEASE/m13-*-run` generated dirs.
6. Governance sync: copy exactly the 7 paths from `main` (path-limited checkout), never workflows.
- **Acceptance status:** CONDITIONAL — no blocker for the governance sync from a security standpoint; SEC-1 should be fixed before any distribution of an offline edition containing contributed content.
- **Reason:** no write-back, secret, or privilege-escalation findings; one confirmed latent injection and several hardening gaps.

## 10. Handoff
- **Draft PR:** see PR body (targets `m13-system-wide-depth-audit-2026-10-09`)
- **Report path:** reports/agent-work/security-offline/phase-0-offline-and-workflow-review.md
- **Next owner/action:** Chief Engineer to route SEC-1 (with PR #24) and SEC-2/3 to CI Engineer after owner approval. Phase 1 remains unauthorized.
