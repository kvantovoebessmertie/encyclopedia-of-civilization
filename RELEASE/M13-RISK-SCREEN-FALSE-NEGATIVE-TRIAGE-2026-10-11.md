# M13 Risk-Screen Calibration — Known High-Consequence False Negatives
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source revision reviewed: `4453783e9dc2db55c4936a8acd85cbc666c46f86`
Status: **Four known false negatives identified; keyword screen expanded in the accompanying code change. No content JSON changed.**

## Method

Compared the full 1,494-Claim worksheet's machine risk-domain results against the explicit high-consequence review reports (batches 01–11 and 13–15). The reports contain **53 unique Claim IDs**. Four Claims had no `risk_domains` despite being included in the high-consequence overlay. Two of the four had no other machine triage flag; the other two were only flagged as actionable or short-evidence items, not as high-consequence.

## Confirmed missed candidates

| Claim | Why the existing screen missed it | Added vocabulary |
|---|---|---|
| `CLM-COLD-HYPOTHERMIA-WETNESS` | “Гипотермия”, cold exposure and wetness were absent from the health vocabulary | hypothermia, frostbite, cold exposure, переохлаждение |
| `CLM-COLD-LIMIT-OUTDOOR` | “зимней непогоде” did not match an existing risk term | зимняя непогода, winter storm/weather |
| `CLM-WASTE-HAND-HYGIENE` | “гигиена рук” was not recognized by the sanitation terms | hand hygiene, handwashing, гигиена рук |
| `CLM_FOOD_SAFETY_CDC_A` | “safe cooking”, internal temperature and food thermometer were not recognized | safe cooking, internal temperature, food thermometer, foodborne |

## Calibration change and limitations

The risk screen now includes the missing term families and has regression tests for all four cases. This is a discovery-screen improvement, not a guarantee that every high-consequence Claim will be found: different wording, implicit hazards, and missing context can still create false negatives. Re-run the full worksheet on the new commit and compare the resulting risk-domain count and the four named IDs before accepting this calibration.

No published Claim, Evidence Use, Source, or Relation JSON was edited. M13 remains open.
