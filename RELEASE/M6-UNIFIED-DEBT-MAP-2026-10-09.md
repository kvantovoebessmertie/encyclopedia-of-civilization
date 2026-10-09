# Unified M6 Debt Map — 2026-10-09

## Status
**CORRECTION PASS APPLIED — POST-CORRECTION VERIFICATION PENDING.** The confirmed debts below have corresponding edits in the current M6 working tree. They are not considered closed until record-level re-audit, regression validation, and exact-head CI complete. M4/M5 remain closed; `main` is unchanged.

## Debt resolution ledger

| ID | Original finding | Correction applied | State |
|---|---|---|---|
| M6-SUB-01 | Learning Claim C exceeded direct source support. | Narrowed Claim C to experimental systems and individual differences described by NIMH; updated its Evidence Use. | FIX APPLIED — VERIFY |
| M6-SUB-02 | Law Claim C was broader than the Cornell LII/Wex locator. | Narrowed Claim C to the U.S. federal/state jurisdiction example; updated its Evidence Use and retained the jurisdiction/date Context. | FIX APPLIED — VERIFY |
| M6-SUB-03 | Governance Claim C lacked precise comparative support. | Reframed Claim C around the interpretation of defined indicators/estimates; added World Bank Worldwide Governance Indicators (2026) Source and claim-linked Evidence Use. | FIX APPLIED — VERIFY |
| M6-SUB-04 | Education Claim C was too broad for UNESCO’s rights-focused page. | Narrowed Claim C to country-level differences in organisation and financing; added OECD Education at a Glance 2026 Source and claim-linked Evidence Use. | FIX APPLIED — VERIFY |
| M6-EV-01 | 18 existing Evidence Use descriptions were formulaic. | Updated all 18 descriptions to name claim-specific source sections/material and their inferential role. | FIX APPLIED — VERIFY |
| M6-EV-02 | Sleep Claim C lacked independent corroboration. | Added a CDC Preventing Chronic Disease (2023) Source and claim-linked Evidence Use; retained cautious wording. | FIX APPLIED — VERIFY |
| M6-EV-03 | Learning Claim C needed narrower wording or methods support. | Resolved with the narrowed Claim C and revised Evidence Use. | FIX APPLIED — VERIFY |
| M6-EV-04 | Law Claim C needed narrower wording or broader legal authority. | Resolved with the narrowed U.S.-law example and revised Evidence Use. | FIX APPLIED — VERIFY |
| M6-EV-05 | Demography Claims B/C had coarse source descriptions. | Added the official WPP 2024 Methodology Report Source and separate claim-linked Evidence Use records for Claims B/C; existing Evidence Use now cross-references the method report. Context distinguishes projections from observations in one language. | FIX APPLIED — VERIFY |
| M6-EV-06 | Governance Claim C needed comparative evidence. | Added World Bank WGI 2026 and claim-linked Evidence Use; preserved non-ranking boundary. | FIX APPLIED — VERIFY |
| M6-EV-07 | Education Claim C needed comparative evidence. | Added OECD Education at a Glance 2026 and claim-linked Evidence Use; preserved country/reference-period limits. | FIX APPLIED — VERIFY |
| M6-HV-01 | Demography Context mixed Russian and English in one sentence. | Rewrote the sentence consistently in Russian and re-read it in post-correction review. | RESOLVED — EXACT-HEAD CI PENDING |
| M6-HV-02 | Language-policy ambiguity: English Claims with Russian Context/Scope/Evidence Use. | Cross-slice sampling of existing M5/corpus records confirms this is an established convention; no inconsistent translation pass is warranted. | RESOLVED — EXACT-HEAD CI PENDING |
| M6-HV-03 | Generic Scope text did not make Claim B/C limits readily discoverable. | Rewrote all six existing Scope records with claim-group coverage and domain-specific boundaries; added focused assertions to all six dedicated slice regressions. No records/types or reference semantics added. | RESOLVED — EXACT-HEAD CI PENDING |
| M6-PROC-01 | The first correction commit preceded the update to `RELEASE/EDITORIAL-CORRECTION.json`; CI correctly blocked preflight. | Added all six locked M6 slices and the M6 finding IDs to the authorization manifest. The guard was not weakened; fresh preflight on the authorized final HEAD and exact-head CI must pass. | OPEN — PROCESS VERIFICATION |

## Non-debt decisions preserved
- One Source per slice is not automatically a defect. New sources were added only where a specific claim required independent corroboration or comparative evidence.
- No new vertical slice or Record type was added.
- No Relation was added. The 64-record Relation audit found no M6 target references, no confirmed broken endpoints, and no duplicate unordered participant pair.
- Filename/ID separator mismatches are not treated as broken references unless the actual target `record_id` fails to match.
- Bilingual Claims and Russian Context/Scope/Evidence Use remain unchanged outside the confirmed mixed-language sentence; no broad translation pass was performed.

## Remaining closure gates
1. Verify M6-PROC-01 by passing preflight on the authorized current HEAD; preserve the initial failure and manifest correction in the audit trail.
2. Re-read every changed Claim, Source, Evidence Use, Context, coverage field, and dedicated regression.
3. Run content preflight and the six affected slice regressions; fix only confirmed defects.
4. Complete post-correction substantive/evidence/Human View/Relation sign-off.
5. Verify the coverage manifest and README against the exact record tree (479 slices / 4,763 Records / 605 Sources / 1,639 Evidence Use / 64 Relations / 19 types).
6. Run Reference tests, Release Conformance Gate, and Offline Edition on the same exact final HEAD; all 3 must be green.
7. Independently verify that HEAD and all workflow runs match before creating a CLEAN checkpoint.

No mass rewrite, quota-driven expansion, new Record type, speculative Relation, unsupported claim, or weakened validation is authorized.
