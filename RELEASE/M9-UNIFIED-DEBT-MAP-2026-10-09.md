# M9 Unified Debt Map — 2026-10-09

## Status

**CONTROLLED LANGUAGE CORRECTION IMPLEMENTED; desk audit PASS.** CI acceptance is determined from the three workflows attached to the exact current HEAD of draft PR #14, not from a previously tested SHA. Keep the PR draft/open/unmerged. M9 is not CLEAN until the exact-head 3/3 gate and independent verification both pass.

## M9-HUMAN-001 — residual English Evidence Use in sleep-basics

**Content debt resolved; acceptance is subject to the exact-head CI gate.**

- Translated the four human-facing Evidence Use descriptions to Russian.
- Preserved all record IDs, claim/source refs, evidence roles and provenance.
- Retained the independent CDC corroboration and explicit no-diagnosis/no-treatment boundary.
- Added regression assertions for the Russian-facing descriptions while preserving record count, source diversity, links and medical scope.

## M9-HUMAN-002 — residual English Evidence Use in supply-chain-basics

**Content debt resolved; acceptance is subject to the exact-head CI gate.**

- Translated the seven human-facing Evidence Use descriptions to Russian across NIST, CISA and OECD support.
- Preserved the cyber-risk scope of the NIST claims and the separate broader visibility/due-diligence role of the OECD-backed claim.
- Preserved record IDs, claim/source refs, evidence roles, provenance, source identities and URLs.
- Added regression assertions for all seven descriptions while preserving all existing count, source-linkage, schema and semantic assertions.

## Scope and structural delta

- Only the 11 authorized Evidence Use `content.material.description` fields and the two dedicated regression files changed, plus M9 planning/audit documentation.
- No new or deleted Records, Sources, Record types, or Relations.
- No Relation participants changed.
- Corpus structure remains 483 slices / 4,831 Records / 19 Record types; 617 Sources / 1,669 Evidence Use / 64 Relations; 484 Context / 483 Scope.
- No unrelated slice, Claim, Context, Scope, README, source identity, or canonical URL was changed.

## Acceptance gates

1. The two targeted tests and all applicable Reference tests must pass.
2. Release Conformance Gate and Offline Edition must pass on the same exact final HEAD.
3. Recheck final diff, coverage, Relation delta, PR base/head and `main`.
4. Record M9 CLEAN only if all three workflows PASS on the same SHA and independent verification succeeds. Do not merge the PR as part of the checkpoint.
