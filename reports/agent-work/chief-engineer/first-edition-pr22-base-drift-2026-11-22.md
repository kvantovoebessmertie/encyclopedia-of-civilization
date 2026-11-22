# First Edition PR #22 — current gates and main-base drift review

- **Agent:** chief-engineer
- **Task:** Reconcile the first-edition PR's exact-head status, release gates, and divergence from current `main`; identify safe next actions without changing the base or merging.
- **Date (UTC):** 2026-11-22
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** `14ddc6687d50f2cfcfe2e93735a9155409c7a7dc`
- **Final evidence-artifact HEAD:** `14ddc6687d50f2cfcfe2e93735a9155409c7a7dc` (the report-only commit that adds this handoff follows)
- **Status:** VERIFIED findings; integration and publication remain BLOCKED by explicit owner/release gates

## 1. Request and acceptance criteria

Continue the bounded first-edition MVP work in parallel with M13. The first edition must become a real, usable, offline program without waiting for all 483 slices or the full 1,494-Claim M13 audit. It must use an explicit, exact-version, owner-approved selection and must not accidentally package the entire corpus as a public release.

Acceptance criteria for this review:
- Verify current PR #22 head/base and exact-head CI.
- Reconcile the branch against current `main` without modifying `main`, changing the PR base, rebasing, or merging.
- Inspect the current first-edition selection and offline-build contract.
- Identify what is technically complete versus what remains an owner, rights, editorial, or corpus-selection blocker.
- Preserve PR #22 as Draft and unmerged.

## 2. Scope

- **In scope:** PR #22 metadata; current main/base divergence; exact-head Actions runs; Part I/Part II first-edition inventories; owner decision record; selected offline manifest contract; offline builder entry point; current Part II and relation review checkpoints.
- **Out of scope:** changing the PR base; merging/rebasing; creating an INCLUDE allowlist; changing canonical records or selection decisions; public release, deployment or distribution.
- **Dependencies:** first-edition scope and owner decision record; Part I survival inventory; Part II exact-version master; selected offline edition manifest 1.1; PR #22 exact-head technical conformance.

## 3. Work performed

1. Re-fetched PR #22 and confirmed it is OPEN / DRAFT / NOT MERGED at HEAD `14ddc6687d50f2cfcfe2e93735a9155409c7a7dc`, based on `main`.
2. Re-fetched all Actions runs for that exact HEAD and checked the four required workflow types.
3. Compared current `main` (`d58289f319993ede5294a46f4741a506fd2fd710`) with PR #22 HEAD.
4. Retrieved the eight commits on current main since the PR's recorded base SHA and inspected their changed paths.
5. Read the first-edition scope, owner decision record, Part I implementation, Part II exact-version master and current-head recheck, five-slice bounded screen, selected offline manifest contract, offline builder entry point, and prior full-corpus artifact audit.
6. Inspected the complete recursive tree at PR #22 HEAD for a production INCLUDE manifest. No production first-edition allowlist was found.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `reports/agent-work/chief-engineer/first-edition-pr22-base-drift-2026-11-22.md` | Added | Mandatory durable report of PR #22 exact-head, base drift, and first-edition gates |

No canonical content, schemas, tests, builder implementation, workflow, selection manifest, or `main` file was changed.

## 5. Findings and evidence

### VERIFIED — PR #22 exact-head technical status

- PR #22: OPEN / DRAFT / NOT MERGED.
- Exact HEAD: `14ddc6687d50f2cfcfe2e93735a9155409c7a7dc`.
- Recorded base: `main`, base SHA `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.
- Four required workflows all completed successfully on the exact same HEAD:

| Required workflow | Run ID | Result |
|---|---:|---|
| Reference implementation tests | 45044018050 | PASS |
| Release Conformance Gate | 45044017946 | PASS |
| Offline Edition | 45044017905 | PASS |
| MVP Contribution Form Browser Tests | 45044018040 | PASS |

Two additional duplicate workflow attempts for Reference implementation tests and Offline Edition also completed successfully on the same SHA (runs 45044015259 and 45044015378). This establishes technical conformance for the named workflows on HEAD `14ddc668...`; it does not establish factual accuracy, rights clearance, owner release approval, Human View, or permission to publish.

### VERIFIED — PR #22 is eight commits behind current main

Current main is `d58289f319993ede5294a46f4741a506fd2fd710`. GitHub comparison reports PR #22 HEAD as **1,569 commits ahead and 8 commits behind** current main, with a diverged history and merge base `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.

The eight main-only commits since that merge base are dated 2026-11-17:

| Commit | Message |
|---|---|
| `4d51a24d3cdff0aa3bf2f724ff8ce2d14d8a8a89` | docs: require committed reports from Copilot agents |
| `0defe4e00ae9d341845b0e56893a7ff6a375d7a8` | docs: require committed reports from Copilot agents |
| `e78288bacc0cdcbfad7684f6d5559c8d75697441` | docs: require committed reports from Copilot agents |
| `b3aa050f53fb758359671d367c8bf272c29d5af6` | docs: require committed reports from Copilot agents |
| `46645782a91fef7885f9592c501726850f629efd` | docs: require committed reports from Copilot agents |
| `d2147b43a437a5e785e771ed45e1333f1ba47917` | docs: require committed reports from Copilot agents |
| `c179647b5bbf2aae9a3f779d516899818d22691a` | docs: add mandatory agent task report template |
| `d58289f319993ede5294a46f4741a506fd2fd710` | Merge PR #33: require durable, committed reports from every Copilot agent |

The resulting main-only file changes are governance/documentation:
- `.github/agents/chief-engineer.agent.md`
- `.github/agents/ci-engineer.agent.md`
- `.github/agents/evidence-researcher.agent.md`
- `.github/agents/m13-auditor.agent.md`
- `.github/agents/security-offline.agent.md`
- `.github/copilot-instructions.md`
- `reports/agent-work/REPORT-TEMPLATE.md`

No canonical encyclopedia content, schema, or runtime implementation appears in this eight-commit main-only delta. The new governance requires one durable task report in the repository, exact-head CI evidence, and a report link in each Draft PR.

**Disposition:** record the base drift; do not retarget, merge main into the branch, rebase, or merge PR #22 in this task. The 1,569-ahead / 8-behind history must be reviewed as a separate integration decision.

### VERIFIED — first-edition content selection is not yet approved

**Part I — Survival and Preservation of Life**
- The Part I inventory reports 94/94 slices and 980/980 record files screened.
- All 980 records remain HOLD.
- The reader-facing section architecture and chapter order are implemented, but the Part I document explicitly says record-level publication is not approved.

**Part II — bounded foundations and supporting disciplines**
- The current-head structural recheck reports 1,134 unique exact-version rows: 1,058 candidate keys plus 76 dependency records.
- All 1,134 rows remain HOLD; INCLUDE = 0; EXCLUDE = 0.
- Represented Part II slice coverage is 124/385. The separate `cross-slice-linkage` dependency label is outside that denominator.
- The five-slice bounded screen covers 47/47 records across ancient civilizations, anthropology, linguistics, philosophy and ethics. All five slices remain HOLD.
- These are exact-version inventory and bounded screening results, not an approved publication selection.

**Production allowlist**
- The selection manifest contract explicitly says no production INCLUDE manifest is supplied.
- The complete recursive tree at PR #22 HEAD contains `REFERENCE/SELECTION-MANIFEST.md`, but no `RELEASE/FIRST-EDITION-INCLUDE.json` or other production allowlist.
- No selected record set is currently authorized for a first-edition release.

### VERIFIED — selection-aware offline builder exists; production release remains gated

The current builder entry point supports both:
- the legacy full-corpus diagnostic build; and
- a separate `--selection-manifest` path that calls `build_selected_offline_edition` with an exact source commit.

Manifest schema 1.1 requires each selected record and direct dependency to pin:
- `record_id`;
- `record_version`;
- `record_type`;
- `type_version`;
- `schema`;
- `decision: INCLUDE`;
- an explicit APPROVED attestation with approver and decision reference.

The builder rejects missing/stale identities, profile/schema drift, unresolved decisions, missing/duplicate versions, omitted or extraneous dependencies, and unselected Claim/Evidence Use/Source endpoints. Dependencies are not auto-added.

The selection contract states that synthetic fixtures are not public content and that no production INCLUDE manifest is supplied. The prior offline artifact audit also established that the legacy Offline Edition workflow builds the full canonical corpus and is a diagnostic/recovery artifact, not the first edition. A successful selected build would prove packaging and declared dependency closure only; rights, factual/source review and owner publication approval remain separate.

### VERIFIED — WP2 owner decisions remain open

The owner decision record requires, before public release:
1. a project-authored content licence / rights model;
2. a named accountable editor and release approver;
3. a monitored correction/takedown contact route and backup;
4. exact rights/attribution checks for every included record and asset;
5. qualified review for high-consequence included material, or exclusion of that instructional item.

Distribution and language decisions also remain for owner confirmation. The proposed defaults are recommendations, not adopted policy. No owner decision is inferred from repository activity.

## 6. Commands and verification

| Command/check | Result | Exact SHA / run URL | Notes |
|---|---|---|---|
| PR metadata re-fetch | PASS | PR #22, HEAD `14ddc668...` | OPEN / DRAFT / NOT MERGED |
| Exact-head workflow run query | 4/4 required PASS | [Reference](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044018050), [Release Gate](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044017946), [Offline Edition](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044017905), [Browser Tests](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45044018040) | Same immutable HEAD |
| Compare current main to PR #22 | VERIFIED DIVERGED | `d58289f...` vs `14ddc668...` | 1,569 ahead / 8 behind |
| Main-only commit/file review | PASS | Eight commits listed in §5 | Documentation/governance only |
| PR #22 recursive tree scan | PASS | `14ddc668...` | No production INCLUDE allowlist |
| Selection contract / builder inspection | PASS | `REFERENCE/docs/SELECTED-OFFLINE-EDITION-MANIFEST.md`; `REFERENCE/build_offline_edition.py` | Contract and entry point inspected; no production manifest |
| Local shell/unit-test commands | NOT RUN | N/A | This was a read-only repository-state and release-gate review |

## 7. Unresolved issues, risks, and blockers

- PR #22 is 8 commits behind current main and has a diverged 1,569-commit-ahead history. No branch synchronization action was taken.
- Part I and Part II candidate records remain HOLD; no approved INCLUDE allowlist exists.
- WP2 owner decisions, rights/attribution register, named accountable editor/release approver, monitored correction route and qualified reviewers remain outstanding.
- A real selected offline build must be generated from an owner-approved exact-version allowlist and inspected separately from the full-corpus diagnostic artifact.
- A report-only commit will advance PR #22 HEAD; the four required workflows must be checked again on that new exact SHA before citing CI as current.
- PR #22 remains Draft/unmerged; no public distribution is authorized.

## 8. Not done / not verified

- No PR base change, merge, rebase or branch synchronization.
- No canonical content, selection decision, allowlist, rights record or publication state changed.
- No INCLUDE/EXCLUDE decision was made.
- No real first-edition selected artifact was built or distributed.
- No legal rights clearance, external peer review, Human View, specialist approval or owner sign-off was performed.
- No change to `main`.

## 9. Recommendation and acceptance

- **Recommendation:** preserve the existing PR #22 scope and Draft status; resolve the main-base drift as a separate explicit integration decision; continue WP1 within the bounded first-edition map; obtain WP2 owner decisions and rights/review evidence; only then build the real first edition using the schema-1.1 exact-version selection manifest.
- **Acceptance status:** CONDITIONAL
- **Reason:** PR #22 is technically conforming on its inspected exact HEAD, and the selection-aware build path exists, but no production allowlist or release approvals exist and the branch is behind current main.

## 10. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/first-edition-pr22-base-drift-2026-11-22.md`
- **Next owner/action:** Project owner — decide whether/when to synchronize PR #22 with the eight governance-only main commits; Chief Engineer — continue bounded WP1 dependency closure and maintain the selection/release boundary; owner/editor — resolve WP2 decisions before any public first-edition release.
