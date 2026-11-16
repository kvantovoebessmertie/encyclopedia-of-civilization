# Encyclopedia of Civilization — Copilot Governance

## Mission
Help develop a durable, evidence-based, offline-capable encyclopedia of practical and civilizational knowledge. Work incrementally and preserve the integrity of the corpus.

## Non-negotiable rules
1. Never modify `main`, merge a pull request, or change protected historical checkpoints unless the repository owner explicitly authorizes that exact action.
2. Work on a dedicated feature branch. Keep pull requests Draft until the owner explicitly approves readiness.
3. Never invent Claim IDs, Source IDs, evidence, quotations, locators, dates, audit results, CI results, or coverage counts.
4. Distinguish clearly between verified facts, machine-generated routing/heuristics, provisional human review, and completed semantic assessment.
5. A mention of a Claim ID in a report is not proof that the Claim was substantively reviewed. Require traceable evidence: report path, line/row, review scope, source pinpoint, and status.
6. Do not assign D/E/B scores automatically from metadata, keyword matches, or model confidence. Scores require claim-specific evidence and explicit reasoning.
7. Do not change canonical RECORD, CLAIM, SOURCE, EVIDENCE USE, ASSESSMENT, INFERENCE, or DECISION records unless the task explicitly authorizes the exact bounded change. Prefer reports, tests, and generated artifacts.
8. Preserve record IDs, version history, schema conventions, and existing terminology. Do not silently normalize, deduplicate, rename, or rewrite records.
9. Do not treat a passing CI run on a different commit as proof that the current head passed. Verify exact head SHA and relevant tree identity.
10. Before editing, inspect the current branch, HEAD, working tree, relevant standards, tests, and existing reports. Do not assume prior checkpoints are current.
11. Keep changes small, reproducible, reviewable, and covered by tests. Explain why each change is necessary.
12. If evidence or scope is ambiguous, stop and report the gap instead of guessing.

## Required workflow
- Inspect repository state and relevant standards before acting.
- State the intended scope and files to change.
- Make changes only on a dedicated branch.
- Add or update regression tests for behavior changes.
- Run the narrowest relevant checks, then broader required checks when feasible.
- Report exact commands, commit SHA, test results, unresolved issues, and what was not verified.
- Never claim completion while acceptance criteria remain unmet.

## M13 audit semantics
- Keep inventory, linkage triage, prior-report mentions, source-fit screening, provisional assessment, finalized D/E/B scoring, Human View, high-consequence review, relation review, and independent review as distinct statuses.
- Maintain one auditable row per Claim and preserve source/report provenance.
- Do not equate a worklist being processed with the audit being complete.
- Do not infer missing IDs from counts or neighboring sequences.
- Any hold remains a hold until its stated release criteria are met.

## Collaboration
Agents may work in parallel only on independent scopes and separate branches/worktrees. The Chief Engineer coordinates integration. A second agent must review substantive changes. If two agents touch the same files or canonical records, stop and coordinate before proceeding.
