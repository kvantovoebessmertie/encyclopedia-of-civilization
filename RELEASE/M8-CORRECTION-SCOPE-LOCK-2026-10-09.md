# M8 Controlled Correction Scope Lock — 2026-10-09

## Status

**AUTHORIZED FOR CONTROLLED CORRECTION on `m8-depth-baseline-2026-10-09` only.** This lock follows the initial diagnostic at corpus SHA `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`. It does not modify or reopen the accepted M7 checkpoint, M6 CLEAN, protected M4/M5, or `main`.

## Basis

The M8 initial depth diagnostic reviewed all 43 Claims in a frozen 12-slice purposive sample. It identified:
- M8-DEPTH-001: three non-substantive, self-referential Claims and generic Evidence Use in `mechanics-basics`.
- M8-DEPTH-002: generic Evidence Use for `statistics-basics` Claims B/C.
- M8-BOUNDARY-003: the `water` slice has useful README limitations but no machine-readable Context/Scope Records.
- M8-HUMAN-004: English Claim statements and README in `governance-basics`, inconsistent with Russian Context/Scope and the Russian-facing corpus.

## Authorized target files and actions

### 1. `mechanics-basics` — substantive repair
- Replace only Claims A–C with introductory, source-supported propositions covering Newton's first, second and third laws in their bounded classical-mechanics context.
- Replace each generic Evidence Use description with claim-specific support and a clear section-level locator to the existing OpenStax University Physics source.
- Improve the slice Context, Scope and README to describe the actual subject and exclusions.
- Strengthen the existing dedicated regression to assert the substantive concepts and claim-specific Evidence Use. Do not reduce existing schema, semantic, provenance or count assertions.

### 2. `statistics-basics` — claim-specific evidence repair
- Narrow/rewrite Claims B/C only as needed to express source-supported assumptions/data representativeness and experimental design without overclaiming.
- Replace generic Evidence Use material with source-specific explanations tied to the NIST/SEMATECH handbook and OpenStax section on experimental design.
- Add one canonical Source record for OpenStax *Introductory Statistics 2e*, section 1.4, and one claim-specific Evidence Use record for the experimental-design claim if needed.
- Strengthen dedicated regression assertions so generic placeholder evidence cannot pass. Do not add sources merely to increase source counts.

### 3. `water` — structured boundary repair
- Add one Context and one Scope Record, targeted to an existing Claim, making the README's contamination-dependent limits machine-readable.
- Extend the existing water regression to assert both Records and the chemical/radioactive limitation.
- Do not alter supported emergency-water claims unless a separate source-based substantive defect is found.

### 4. `governance-basics` — language consistency
- Translate the three Claim statements and README prose into clear Russian while preserving attribution to the OECD framework and the World Bank indicator methodology.
- Translate human-facing Evidence Use descriptions to Russian without changing source identities/titles, claim/source links, evidentiary roles or scope.
- Strengthen existing regression to check the intended Russian-facing statements and retain the existing source/provenance assertions.

## Non-negotiable limits

- No new Record type, no new Relation, no changes to unrelated slices.
- No claim/source quota and no mass rewrite.
- Do not change canonical source titles or identities merely to translate presentation text.
- Any new source or Evidence Use must have a precise, auditable reason and a dedicated regression.
- After changes: re-run targeted tests; perform post-correction claim/evidence/Human View/Relation review; reconcile coverage counts and registry metadata; then run Reference tests, Release Conformance Gate and Offline Edition on the exact same final HEAD.
- Record CLEAN only after all three exact-head workflows succeed and independent branch/PR/base/main verification passes. Any post-CI tree change requires all three gates again.

## Expected structural delta

- `water`: +2 Records (Context + Scope).
- `statistics-basics`: expected +2 Records (Source + Evidence Use) if the existing source is not sufficiently specific for the new claim.
- No change to slice count or Record-type count. Final counts must be calculated from the actual tree and synchronized, not assumed from this expectation.
