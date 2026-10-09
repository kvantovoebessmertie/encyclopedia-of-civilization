# M10 Human View Correction Authorization — 2026-10-09

## Authorization basis

Authorized by the findings in `RELEASE/M10-HUMAN-VIEW-TASK-AUDIT-2026-10-09.md`. The task simulation identified novice navigation as FAIL and dependency reasoning, evidence traceability, and next-step guidance as PARTIAL.

## Exact authorized file list

1. `CONTENT/vertical-slices/human-settlement-systems-basics/README.md`
2. `REFERENCE/tests/test_content_human_settlement_systems_basics_vertical_slice.py`
3. `RELEASE/M10-HUMAN-VIEW-TASK-AUDIT-2026-10-09.md` — update status/findings after post-correction audit only.
4. `RELEASE/M10-UNIFIED-DEBT-MAP-2026-10-09.md` — append/resolve only the four Human View findings and preserve historical CI facts.
5. `RELEASE/M10-POST-CORRECTION-AUDIT-2026-10-09.md` — add follow-up audit result and accurately distinguish technical CI from Human View acceptance.

This is a zero-structural-delta, README-and-regression correction. No other paths are authorized.

## Required README behaviors

- Start with plain-language purpose and explain that settlements are systems of people, homes, services, infrastructure, governance and environment.
- Show a small step-by-step dependency example, explicitly labelled illustrative and not universal.
- Provide human-readable links to the three claims and their supporting sources using repository-relative links to the existing files; do not alter canonical source identity/URL or provenance.
- Explain how a reader can inspect the source and its limits without requiring them to understand record IDs or record types.
- Include a short question-based “what to check next” list: service availability/access, connections/dependencies, local data, applicable requirements, affected people and qualified expertise. Do not turn this into a universal design recipe or site-specific advice.
- Keep a clear boundary against replacing local assessment, engineering calculations, legal advice or operational instructions.
- Keep internal schema/count pattern out of the main novice journey; if retained, label it as a technical note.

## Regression requirements

Retain every existing assertion and add explicit assertions that:
- the README has a novice-facing dependency sequence;
- all three claim files and their supporting Evidence Use/source files are linked;
- the next-step questions include local data, requirements and qualified expertise;
- the boundary against site-specific design/calculation remains;
- the novice path is not presented primarily as “Source → 3 Claims → 3 Evidence Use → Context → Scope”.

## Invariants

Do not change any Claim, Evidence Use, Source, Context, Scope, Relation, record ID, provenance, canonical URL, record count, record type, coverage or Relation participant. Do not weaken or delete existing tests. No edits outside the exact list above.

## Required acceptance

Run targeted test and full applicable Reference tests. Then Reference implementation tests, Release Conformance Gate and Offline Edition must all PASS on one identical final HEAD. Repeat diff, coverage, linkage, Relation and PR/main checks. Any post-CI commit requires a new exact-head 3/3 run. This authorization does not itself make M10 CLEAN; acceptance remains OPEN until every gate passes.