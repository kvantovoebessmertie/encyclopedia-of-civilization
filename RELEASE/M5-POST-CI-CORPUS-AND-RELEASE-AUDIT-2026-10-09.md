# M5 Post-CI Corpus and Release Audit — 2026-10-09

## Audit target and CI evidence

- Audited content/CI target: `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`.
- Reference implementation tests: PASS, workflow run #2489 (`37885196482`).
- Release Conformance Gate: PASS, workflow run #2539 (`37885196502`).
- Offline Edition: PASS, workflow run #1962 (`37885196496`).
- All three workflows completed successfully on the same target SHA.

## Tree-level inventory

A recursive Git tree inspection of the audited target returned a complete, non-truncated tree:

- 4,754 JSON record files under `CONTENT/vertical-slices/**/records/`.
- 479 distinct vertical-slice directories containing records.
- Coverage registry declares 4,754 total Records, 479 slices and 19 Record types.
- Coverage type counts sum to the declared total of 4,754; all 19 registered types are directly covered.
- Relation count is 64. The Relation audit records 57 cross-slice Relation records plus one shared Context; remaining Relations are elsewhere in the corpus.
- M5 scope remains nine existing slices only. No new vertical slice or Record type was added.
- M4 accepted content baseline remains `83b2e3185cd92c55d53a5ce661be384508870e1a`.

## Audit interpretation and limitations

The CI results establish passing repository-defined checks for the audited SHA; they do not prove the truth of every claim or replace expert review. The substantive, evidence-independence, Human View/adversarial and Relation audits are PASS at their stated scope. Claim-level single-source limitations and source-jurisdiction/date limits remain documented in the dedicated audit reports.

## Exact-HEAD rule

This report records successful CI on `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`. The subsequent release-document synchronization changes the branch HEAD, so the release gates must be rerun on that final documentation-synchronized HEAD before M5 can be declared CLEAN. This report alone does not authorize a merge or CLEAN checkpoint.
