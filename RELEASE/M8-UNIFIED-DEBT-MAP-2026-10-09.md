# M8 Unified Debt Map — 2026-10-09

## Status

**POST-CORRECTION AUDIT PASS; EXACT-HEAD 3/3 CI PASS ON SHA `247007768453f2679cb5823b663e97212449f22c`. A documentation status-sync commit creates a successor HEAD and requires a fresh exact-head 3/3 before CLEAN acceptance.**

- Accepted source corpus SHA scored: `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.
- Current work branch: `m8-depth-baseline-2026-10-09`.
- Candidate corpus after current corrections: 483 slices / 4,831 Records / 19 Record types; 617 Sources / 1,669 Evidence Use / 484 Context / 483 Scope.
- The M8 baseline audit is in `M8-INITIAL-DEPTH-DIAGNOSTIC-2026-10-09.md`; scope is locked in `M8-CORRECTION-SCOPE-LOCK-2026-10-09.md`.

## Finding ledger

### M8-DEPTH-001 — mechanics-basics was substantively hollow
**Status: RESOLVED AFTER POST-CORRECTION AUDIT.**
- Replaced three self-referential/meta Claims with introductory statements of Newton's first, second and third laws.
- Replaced generic Evidence Use material with claim-specific descriptions of the relevant OpenStax University Physics sections.
- Updated Context, Scope and README to state the classical-mechanics boundary and important exclusions.
- Strengthened the dedicated regression to assert each law and claim-specific Evidence Use, while preserving all prior count/provenance checks.
- No new Records, Sources, or Relations were added to this slice.

### M8-DEPTH-002 — statistics-basics had generic Evidence Use for Claims B/C
**Status: RESOLVED AFTER POST-CORRECTION AUDIT.**
- Narrowed Claims B/C to source-supported principles on method assumptions/data representativeness and experimental design.
- Replaced generic Evidence Use descriptions with specific NIST/SEMATECH and OpenStax support.
- Added Source `SRC-OPENSTAX-STATISTICS-EXPERIMENTAL-DESIGN` and Evidence Use `EU-STATISTICS_BASICS-C-OPENSTAX`; these support the experimental-design claim rather than inflating source count.
- Updated Context, Scope, README and dedicated regression assertions.
- Structural delta: +1 Source, +1 Evidence Use.

Source check: NIST describes its handbook as a guide to statistical methods and underlying assumptions; OpenStax §1.4 covers experimental design, explanatory/response variables and random assignment. Locators:
- https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook
- https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics

### M8-BOUNDARY-003 — water lacked machine-readable Context/Scope
**Status: RESOLVED AFTER POST-CORRECTION AUDIT.**
- Added `CTX-WATER-EMERGENCY` and `SCP-WATER-EMERGENCY`, targeted to an existing water Claim.
- Both records make contamination-dependent applicability explicit; Scope states that local advisories, testing and health-authority guidance remain controlling.
- Extended the dedicated water regression to require both records, target references and chemical/radioactive limitations.
- Updated Release Gate G16 to validate the authorized 12-record water package and require the two targeted Context/Scope Records with their contamination boundary. This replaces a stale exact-10-record assumption with a stricter semantic check, not a weakened gate.
- Existing water Claims and Sources were not rewritten.
- Structural delta: +1 Context, +1 Scope.

### M8-HUMAN-004 — governance-basics mixed English Claims/README with Russian Context/Scope
**Status: RESOLVED AFTER POST-CORRECTION AUDIT.**
- Translated the three Claim statements, README and all four human-facing Evidence Use descriptions into Russian.
- Preserved canonical source identities/titles, record IDs, provenance, claim/source links and evidence roles.
- Strengthened the existing regression to assert Russian-facing Claim text and preserve the WGI evidence linkage.
- No new Records, Sources, or Relations were added to this slice.

### M8-HUMAN-005 — residual English Evidence Use in sleep/supply-chain
**Status: DEFERRED, NOT A RELEASE BLOCKER FOR THIS CORRECTION PASS.**
- This finding is a language/usability observation, not by itself a source-fit failure.
- It remains outside the locked four-slice scope. Do not bulk-translate these older slices without a concrete follow-up scope and regression plan.

## Relation audit delta

No Relation records were added, removed or modified by this correction pass. The work is confined to Records and dedicated regression files in the four locked slices. A post-correction check must verify that the final diff indeed contains no Relation changes.

## Exact-head verification completed

At SHA `247007768453f2679cb5823b663e97212449f22c`:
- Reference implementation tests #2768 — PASS, 969 tests.
- Release Conformance Gate #2610 — PASS, CONFORMING, no blocking or limiting gates.
- Offline Edition #2242 — PASS.
- All three passed on the same exact SHA.
- Actual coverage and cross-slice audit agree: 4,831 Records / 483 slices / 19 types.
- No Relation Records or participants changed; G16 was strengthened to validate the water Context/Scope contract.
- PR #13 remains open/draft/unmerged against accepted M7; `main` is unchanged.

The complete post-correction audit is `M8-POST-CORRECTION-AUDIT-2026-10-09.md`. Human View was desk-based, not a live novice study; no external human reviewer is claimed.

## Remaining release gate

This audit/status-sync documentation commit creates a new HEAD. Re-run Reference tests, Release Conformance Gate and Offline Edition on that exact successor SHA and independently verify PR/base/main. If all three succeed, record CLEAN in PR #13 discussion without further code-tree changes. Do not merge PR #13 as part of this checkpoint.


## CI feedback and controlled follow-up

The first post-authorization run exposed four regression/metadata mismatches; these were corrected by aligning the assertions to the intended content and synchronizing the cross-slice audit count to 4,831. The next exact-head run exposed G16's hard-coded expectation that the original water slice contained exactly ten Records. Because the authorized correction adds one Context and one Scope Record, G16 now checks the 12-record package shape plus the presence, target links and chemical/radioactive boundary of those Records. This is a stricter content contract, not a bypass. The G16 change is explicitly included in the M8 scope lock and editorial authorization. All three release gates must pass again on the resulting exact HEAD.
