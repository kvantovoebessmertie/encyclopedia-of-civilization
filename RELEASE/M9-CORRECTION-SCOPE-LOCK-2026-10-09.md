# M9 Controlled Correction Scope Lock — 2026-10-09

## Status

**SCOPE LOCKED; implementation and audit pending.** M9 starts from accepted M8 CLEAN SHA `cb78425bd42790a35046d85e9dbeeb2611969274`. Work is isolated on `m9-gap-map-2026-10-09`; it does not modify `main` or reopen M8, M7, or protected M4/M5 checkpoints.

## Verified finding

M8 explicitly deferred M8-HUMAN-005: residual English in Evidence Use descriptions in `sleep-basics` and `supply-chain-basics`. Read-only inspection confirms four English Evidence Use descriptions in `sleep-basics` (11 Records total) and seven in `supply-chain-basics` (16 Records total). Their README, Context, and Scope are Russian-facing. This is a language-consistency/Human View issue, not by itself a source-fit failure. Existing tests preserve record counts, source identities, claim/source links, and boundaries but do not assert Russian-facing Evidence Use text.

## Authorized scope

Translate only `content.material.description` in these eleven existing Evidence Use records:

- `CONTENT/vertical-slices/sleep-basics/records/EU-SLEEP_BASICS-A.json`
- `CONTENT/vertical-slices/sleep-basics/records/EU-SLEEP_BASICS-B.json`
- `CONTENT/vertical-slices/sleep-basics/records/EU-SLEEP_BASICS-C.json`
- `CONTENT/vertical-slices/sleep-basics/records/EU-SLEEP_BASICS-C-CDC.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-SUPPLY_CHAIN_BASICS-A.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-SUPPLY_CHAIN_BASICS-B.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-SUPPLY_CHAIN_BASICS-C.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-M5-CISA-SUPPLY-CHAIN-A.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-M5-CISA-SUPPLY-CHAIN-B.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-M5-CISA-SUPPLY-CHAIN-C.json`
- `CONTENT/vertical-slices/supply-chain-basics/records/EU-M5-SUPPLY-CHAIN-VISIBILITY-D.json`

Strengthen the two existing dedicated regressions to require Russian-facing descriptions for all listed IDs while retaining all existing assertions. Preserve meaning and limitations, canonical source titles/identities, URLs, IDs, provenance, claim/source references, and evidence roles.

## Non-negotiable limits

- No new Records, Sources, Relations, or Record types.
- No changes to Claims, Context, Scope, README, source identity, or unrelated slices.
- No broad translation beyond the eleven listed descriptions.
- No weakened tests or conformance checks.
- After correction: targeted tests; translation/source-link review; verify no structural or Relation delta; reconcile coverage only if actual counts changed; then Reference tests, Release Conformance Gate, and Offline Edition must pass on the exact same final HEAD.
- Record M9 CLEAN only after exact-head 3/3 PASS and independent PR/base/main verification. Keep the PR open/draft/unmerged for the checkpoint; do not modify `main`.
