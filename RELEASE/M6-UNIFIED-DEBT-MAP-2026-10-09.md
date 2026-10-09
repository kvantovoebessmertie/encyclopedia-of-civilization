# Unified M6 Debt Map — 2026-10-09

## Status
**CONTENT CORRECTIONS RE-READ; DOCUMENTATION-FINALIZED HEAD CI 3/3 PASS; CHECKPOINT COMMIT REVALIDATION PENDING.** Reference, Release Conformance Gate, and Offline Edition all passed on documentation-finalized HEAD `aebef62de87407dbdcdbf988461242cd09ee3098` (runs `37899900359`, `37899900362`, `37899895530`); all three Content preflight steps passed. Independent tree/coverage verification matched 4,763 record files, 479 slices, 19 types, 605 Sources, 1,639 Evidence Use, and 64 Relations. The M6 checkpoint document and final debt-map reconciliation will advance HEAD, so all three workflows must run once more on the resulting checkpoint HEAD. M4/M5 remain closed; `main` is unchanged. M6 remains OPEN until checkpoint-head CI and independent verification pass.

## Debt resolution ledger

| ID | Original finding | Correction applied | State |
|---|---|---|---|
| M6-SUB-01 | Learning Claim C exceeded direct source support. | Narrowed Claim C to experimental systems and individual differences described by NIMH; updated its Evidence Use. | RE-READ; CURRENT DOCUMENTATION HEAD CI PASS — CHECKPOINT-HEAD REVALIDATION PENDING |
| M6-SUB-02 | Law Claim C was broader than the Cornell LII/Wex locator. | Narrowed Claim C to the U.S. federal/state jurisdiction example; updated its Evidence Use and retained the jurisdiction/date Context. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-SUB-03 | Governance Claim C lacked precise comparative support. | Reframed Claim C around the interpretation of defined indicators/estimates; added World Bank Worldwide Governance Indicators (2026) Source and claim-linked Evidence Use. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-SUB-04 | Education Claim C was too broad for UNESCO’s rights-focused page. | Narrowed Claim C to country-level differences in organisation and financing; added OECD Education at a Glance 2026 Source and claim-linked Evidence Use. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-01 | 18 existing Evidence Use descriptions were formulaic. | Updated all 18 descriptions to name claim-specific source sections/material and their inferential role. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-02 | Sleep Claim C lacked independent corroboration. | Added a CDC Preventing Chronic Disease (2023) Source and claim-linked Evidence Use; retained cautious wording. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-03 | Learning Claim C needed narrower wording or methods support. | Resolved with the narrowed Claim C and revised Evidence Use. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-04 | Law Claim C needed narrower wording or broader legal authority. | Resolved with the narrowed U.S.-law example and revised Evidence Use. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-05 | Demography Claims B/C had coarse source descriptions. | Added the official WPP 2024 Methodology Report Source and separate claim-linked Evidence Use records for Claims B/C; existing Evidence Use now cross-references the method report. Context distinguishes projections from observations in one language. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-06 | Governance Claim C needed comparative evidence. | Added World Bank WGI 2026 and claim-linked Evidence Use; preserved non-ranking boundary. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-EV-07 | Education Claim C needed comparative evidence. | Added OECD Education at a Glance 2026 and claim-linked Evidence Use; preserved country/reference-period limits. | RE-READ; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-HV-01 | Demography Context mixed Russian and English in one sentence. | Rewrote the sentence consistently in Russian and re-read it in post-correction review. | RESOLVED; CURRENT DOCUMENTATION HEAD CI PASS — CHECKPOINT-HEAD REVALIDATION PENDING |
| M6-HV-02 | Language-policy ambiguity: English Claims with Russian Context/Scope/Evidence Use. | Cross-slice sampling of existing M5/corpus records confirms this is an established convention; no inconsistent translation pass is warranted. | RESOLVED; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-HV-03 | Generic Scope text did not make Claim B/C limits readily discoverable. | Rewrote all six existing Scope records with claim-group coverage and domain-specific boundaries; added focused assertions to all six dedicated slice regressions. No records/types or reference semantics added. | RESOLVED; CANDIDATE CI PASS — FINAL-HEAD REVALIDATION PENDING |
| M6-PROC-01 | The first correction commit preceded the update to `RELEASE/EDITORIAL-CORRECTION.json`; CI correctly blocked preflight. | Added all six locked M6 slices and the M6 finding IDs to the authorization manifest. The guard was not weakened; fresh preflight passed in all three workflows on candidate HEAD `b5ec0a846e7d9a9436f6718d04a349537c41e03a`. Repeat preflight on the documentation-finalized HEAD before closure. | DOCUMENTED; preflight and all 3 workflows PASS on `aebef62de87407dbdcdbf988461242cd09ee3098`; checkpoint-head recheck pending |

## Non-debt decisions preserved
- One Source per slice is not automatically a defect. New sources were added only where a specific claim required independent corroboration or comparative evidence.
- No new vertical slice or Record type was added.
- No Relation was added. The 64-record Relation audit found no M6 target references, no confirmed broken endpoints, and no duplicate unordered participant pair.
- Filename/ID separator mismatches are not treated as broken references unless the actual target `record_id` fails to match.
- Bilingual Claims and Russian Context/Scope/Evidence Use remain unchanged outside the confirmed mixed-language sentence; no broad translation pass was performed.

## Remaining closure gates
1. The original M6-PROC-01 failure and manifest correction are preserved. Preflight passed on all three workflows on documentation-finalized HEAD `aebef62de87407dbdcdbf988461242cd09ee3098`; recheck on the checkpoint HEAD.
2. Record-level re-read covered all changed Claims, Sources, Evidence Use, Context, Scope, coverage fields, and the six dedicated slice regressions; documentation-finalized exact-head CI passed.
3. Documentation-finalized exact-head preflight and all three CI workflows passed (Reference `37899900359`, Release Gate `37899900362`, Offline Edition `37899895530`); rerun all three on the final checkpoint HEAD.
4. Substantive, evidence-independence, Human View, and Relation audits are recorded; no new Relation or Record type was introduced.
5. Independently enumerated the untruncated exact candidate tree: 7,076 entries, 4,763 record JSON files, 479 slices. Coverage manifest matches 4,763 Records, 605 Sources, 1,639 Evidence Use, 64 Relations, and 19 types. `CONTENT/README.md` M6 counts match all six locked slice directories.
6. Reference tests (`37899900359`), Release Conformance Gate (`37899900362`), and Offline Edition (`37899895530`) passed on exact documentation-finalized HEAD `aebef62de87407dbdcdbf988461242cd09ee3098`; all three Content preflight steps passed. These runs do not validate the forthcoming checkpoint commit.
7. Re-run and independently verify all three workflows on the final checkpoint HEAD. If all pass, record formal CLEAN acceptance in the PR conversation without changing that tested HEAD.

No mass rewrite, quota-driven expansion, new Record type, speculative Relation, unsupported claim, or weakened validation is authorized.
