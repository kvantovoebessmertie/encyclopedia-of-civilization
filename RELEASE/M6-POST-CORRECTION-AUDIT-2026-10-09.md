# M6 Post-Correction Audit — 2026-10-09

## Status
**CORRECTIONS RE-READ; FINAL-HEAD CI AND INDEPENDENT CLOSURE PENDING.** The controlled correction pass has been checked against the M6 branch. This is not a CLEAN checkpoint. M4/M5 remain closed; `main` is unchanged.

## Re-read results
- Four Claims were re-read and now stay within the reviewed source scope:
  - `CLM-LEARNING_BASICS-C`: experimental systems and individual differences in learning/memory research.
  - `CLM-LAW_BASICS-C`: Cornell LII/Wex jurisdiction examples explicitly bounded to U.S. law.
  - `CLM-GOVERNANCE_BASICS-C`: cross-country governance indicators are estimates to be interpreted with methods and uncertainty, not definitive rankings.
  - `CLM-EDUCATION_SYSTEMS-C`: narrowed to country differences in organisation and financing with country/reference-period limits.
- `CTX-DEMOGRAPHY_BASICS` was re-read; the mixed-language sentence is now consistently Russian and preserves the observation/projection distinction.
- All 18 pre-existing Evidence Use records were re-read. Each now has a claim-specific description rather than the earlier boilerplate. The described source section/material and inferential limits are explicit.
- Four additional Source records and five claim-linked Evidence Use records were added for:
  - CDC Preventing Chronic Disease (2023), independent corroboration for sleep health.
  - World Bank Worldwide Governance Indicators (2026), comparative governance estimates and methodological uncertainty.
  - OECD Education at a Glance 2026, international comparison of education-system organisation and financing.
  - UN Population Division, WPP 2024 Methodology Report, claim-specific support for age-structure trajectories and projection assumptions.
- The new Evidence Use records were re-read; their Claim and Source references match the intended records.
- Dedicated regressions for sleep, governance, and education were updated to expect 11 records and 2 Sources and to assert the new independent evidence link. The other three candidate slices remain 9 records and 1 Source.
- The tree was re-counted from the current branch: 479 slices / 4,763 record files. The coverage manifest reports 4,763 Records, 605 Sources, 1,639 Evidence Use, 64 Relations, and 19 Record types.
- The Relation audit covered all 64 Relation records for M6 target references and duplicate participant pairs. No M6 target reference, broken endpoint, or duplicate unordered participant pair was confirmed. Filename/ID separator differences were checked against actual record IDs rather than treated as defects.

## External-source verification boundary
NHLBI, NIMH, Cornell LII/Wex, OECD governance, UNESCO right-to-education, World Bank WGI, OECD Education at a Glance 2026, and CDC PCD source pages were accessible and consistent with the narrowed claims and Evidence Use descriptions. The initial WPP summary page returned HTTP 403, so the official UN Population Division methodology report was located separately; its published methodology explicitly describes population-by-age/sex starting populations, the cohort-component method, and assumptions for fertility, mortality, and migration. Claim B/C Evidence Use now links to that method report. M6-EV-05 is addressed pending final CI validation.

## CI evidence and exact-head boundary
The corrected content HEAD `3082855f6a145e39fecfbc14de3b5c01e136764b` passed Reference implementation tests (#2569), Release Conformance Gate (#2546), and Offline Edition (#2042), all successful. The debt-map count reconciliation was then committed as `6d4374c114a199b47e7e1427b0abf2d2223ad1b5`; therefore those green results are not yet evidence for the new exact HEAD. All three workflows must be green again on the final unchanged HEAD before CLEAN.

## Process deviation and remaining open items
The first CI run correctly failed because `RELEASE/EDITORIAL-CORRECTION.json` had not yet been updated to authorize the six locked M6 slices. The manifest now explicitly lists those six slices and the M6 findings; the guard has not been weakened. Because the first content edits preceded the manifest update, this sequencing deviation is recorded as **M6-PROC-01**. A fresh preflight on the current authorized HEAD must pass, and this process finding remains open until the final exact-head verification.

1. Verify M6-PROC-01 with successful preflight on the authorized current HEAD; preserve the initial failure and manifest correction in the audit trail.
2. Run content preflight and the six affected slice regressions on the final HEAD.
3. Run Reference implementation tests, Release Conformance Gate, and Offline Edition on the exact same final HEAD without merging to `main` or altering M4/M5.
4. If any test fails, correct only the confirmed defect and rerun all three checks on the resulting exact HEAD.
5. Independently verify all three workflow conclusions, the final commit, corpus counts, and audit sign-offs before any CLEAN checkpoint.

No unsupported claim, new Record type, speculative Relation, quota-driven expansion, or weakened validation was introduced.
