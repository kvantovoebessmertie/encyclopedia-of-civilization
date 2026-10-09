# M6 Post-Correction Audit — 2026-10-09

## Status
**CORRECTIONS RE-READ; CI AND FINAL CLOSURE PENDING.** The controlled correction pass has been checked against the current M6 branch. This is not a CLEAN checkpoint. M4/M5 remain closed; `main` is unchanged.

## Re-read results
- Four Claims were re-read and now stay within the reviewed source scope:
  - `CLM-LEARNING_BASICS-C`: experimental systems and individual differences in learning/memory research.
  - `CLM-LAW_BASICS-C`: Cornell LII/Wex jurisdiction examples explicitly bounded to U.S. law.
  - `CLM-GOVERNANCE_BASICS-C`: cross-country governance indicators are estimates to be interpreted with methods and uncertainty, not definitive rankings.
  - `CLM-EDUCATION_SYSTEMS-C`: narrowed to country differences in organisation and financing with country/reference-period limits.
- `CTX-DEMOGRAPHY_BASICS` was re-read; the mixed-language sentence is now consistently Russian and preserves the observation/projection distinction.
- All 18 pre-existing Evidence Use records were re-read. Each now has a claim-specific description rather than the earlier boilerplate. The described source section/material and inferential limits are explicit.
- Three additional Source records and three claim-linked Evidence Use records were added for:
  - CDC Preventing Chronic Disease (2023), independent corroboration for sleep health.
  - World Bank Worldwide Governance Indicators (2026), comparative governance estimates and methodological uncertainty.
  - OECD Education at a Glance 2026, international comparison of education-system organisation and financing.
- The new Evidence Use records were re-read; their Claim and Source references match the intended records.
- Dedicated regressions for sleep, governance, and education were updated to expect 11 records and 2 Sources and to assert the new independent evidence link. The other three candidate slices remain 9 records and 1 Source.
- The tree was re-counted from the current branch: 479 slices / 4,760 record files. The coverage manifest reports 4,760 Records, 604 Sources, 1,637 Evidence Use, 64 Relations, and 19 Record types.
- The Relation audit covered all 64 Relation records for M6 target references and duplicate participant pairs. No M6 target reference, broken endpoint, or duplicate unordered participant pair was confirmed. Filename/ID separator differences were checked against actual record IDs rather than treated as defects.

## External-source verification boundary
NHLBI, NIMH, Cornell LII/Wex, OECD governance, UNESCO right-to-education, World Bank WGI, OECD Education at a Glance 2026, and CDC PCD source pages were accessible and consistent with the narrowed claims and Evidence Use descriptions. The UN World Population Prospects 2024 page returned HTTP 403 during this check; the source remains the official UN locator, but the precise WPP material for age structure and projection assumptions still requires a final source-level verification. Therefore M6-EV-05 remains **OPEN for external-source verification**, even though the Evidence Use descriptions were improved.

## Remaining open items
1. Verify `demography-basics` Claims B/C against accessible WPP methods/results material or an appropriate official mirror; revise wording/source locator if necessary.
2. Run Reference implementation tests and Offline Edition on the exact same final HEAD.
3. Run Release Conformance Gate on that same HEAD without merging to `main` or altering M5.
4. If any test fails, correct only the confirmed defect and rerun all three checks on the resulting exact HEAD.
5. Independently verify all three workflow conclusions and the final commit before any CLEAN checkpoint.

No unsupported claim, new Record type, speculative Relation, quota-driven expansion, or weakened validation was introduced.
