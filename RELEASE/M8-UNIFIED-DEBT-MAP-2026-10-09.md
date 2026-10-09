# M8 Unified Debt Map — 2026-10-09

## Status

**CONTROLLED CORRECTIONS IMPLEMENTED; POST-CORRECTION AUDIT AND EXACT-HEAD CI PENDING. M8 IS NOT CLEAN.**

- Accepted source corpus SHA scored: `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.
- Current work branch: `m8-depth-baseline-2026-10-09`.
- Candidate corpus after current corrections: 483 slices / 4,831 Records / 19 Record types; 617 Sources / 1,669 Evidence Use / 484 Context / 483 Scope.
- The M8 baseline audit is in `M8-INITIAL-DEPTH-DIAGNOSTIC-2026-10-09.md`; scope is locked in `M8-CORRECTION-SCOPE-LOCK-2026-10-09.md`.

## Finding ledger

### M8-DEPTH-001 — mechanics-basics was substantively hollow
**Status: CORRECTION IMPLEMENTED; RE-AUDIT PENDING.**
- Replaced three self-referential/meta Claims with introductory statements of Newton's first, second and third laws.
- Replaced generic Evidence Use material with claim-specific descriptions of the relevant OpenStax University Physics sections.
- Updated Context, Scope and README to state the classical-mechanics boundary and important exclusions.
- Strengthened the dedicated regression to assert each law and claim-specific Evidence Use, while preserving all prior count/provenance checks.
- No new Records, Sources, or Relations were added to this slice.

### M8-DEPTH-002 — statistics-basics had generic Evidence Use for Claims B/C
**Status: CORRECTION IMPLEMENTED; RE-AUDIT PENDING.**
- Narrowed Claims B/C to source-supported principles on method assumptions/data representativeness and experimental design.
- Replaced generic Evidence Use descriptions with specific NIST/SEMATECH and OpenStax support.
- Added Source `SRC-OPENSTAX-STATISTICS-EXPERIMENTAL-DESIGN` and Evidence Use `EU-STATISTICS_BASICS-C-OPENSTAX`; these support the experimental-design claim rather than inflating source count.
- Updated Context, Scope, README and dedicated regression assertions.
- Structural delta: +1 Source, +1 Evidence Use.

Source check: NIST describes its handbook as a guide to statistical methods and underlying assumptions; OpenStax §1.4 covers experimental design, explanatory/response variables and random assignment. Locators:
- https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook
- https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics

### M8-BOUNDARY-003 — water lacked machine-readable Context/Scope
**Status: CORRECTION IMPLEMENTED; RE-AUDIT PENDING.**
- Added `CTX-WATER-EMERGENCY` and `SCP-WATER-EMERGENCY`, targeted to an existing water Claim.
- Both records make contamination-dependent applicability explicit; Scope states that local advisories, testing and health-authority guidance remain controlling.
- Extended the dedicated water regression to require both records, target references and chemical/radioactive limitations.
- Existing water Claims and Sources were not rewritten.
- Structural delta: +1 Context, +1 Scope.

### M8-HUMAN-004 — governance-basics mixed English Claims/README with Russian Context/Scope
**Status: CORRECTION IMPLEMENTED; RE-AUDIT PENDING.**
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

## Remaining release gates

1. Inspect the actual diff and validate all changed JSON against the current Record schema and semantic rules.
2. Run the four targeted regression tests (mechanics, statistics, water, governance).
3. Re-audit all changed Claims and Evidence Use; verify Context/Scope targeting and source-fit boundaries.
4. Perform Human View/adversarial desk review and confirm no canonical source identity/title was translated.
5. Verify the no-Relation-delta condition.
6. Synchronize coverage counts from the actual record tree; current expected count is 4,831 Records / 483 slices / 19 types.
7. Run Reference tests, Release Conformance Gate and Offline Edition on the same exact final HEAD.
8. Independently verify exact SHA, PR/base and protected branch state. Record CLEAN only if all checks pass; any post-CI code-tree change requires all three workflows again.

No M8 CLEAN claim is made in this document.
