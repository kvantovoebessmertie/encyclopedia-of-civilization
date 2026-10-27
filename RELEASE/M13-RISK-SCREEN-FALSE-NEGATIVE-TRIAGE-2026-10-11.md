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

## Calibration change and validation

The full worksheet was regenerated on `bb3f67d1755441f7815b26c6666e9a903c4d99d2`. The `high_consequence_screen` count increased from **586 to 590**, and all four named Claims now have a risk domain: hypothermia/wetness and winter outdoor exposure under health, hand hygiene under water/food/sanitation, and safe cooking/internal temperature under water/food/sanitation. Regression tests for these vocabulary gaps are included.

This validates the four known misses; it does not prove the screen has no other false negatives. Different wording, implicit hazards, and missing context can still evade a keyword screen.

No published Claim, Evidence Use, Source, or Relation JSON was edited. M13 remains open.
