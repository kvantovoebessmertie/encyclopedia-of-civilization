# M13 Batch 42 — Scored row 045: refrigerator outage time guidance

Date: 2026-10-18  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-FOOD-REFRIGERATOR-4H@1`  
Evidence Use version: `EU-FOOD-REFRIGERATOR-4H@1`  
Source version: `SRC-USDA-POWER-OUTAGE-2024@1`

## Claim under review

> При отключении электроэнергии закрытый холодильник сохраняет продукты холодными примерно 4 часа.

## Evidence fit

The canonical Source is USDA FSIS, “How do you keep food safe during a power failure?”:
https://ask.fsis.usda.gov/article/How-do-you-keep-food-safe-during-a-power-failure

The Evidence Use directly states that USDA FSIS gives approximately four hours for a closed refrigerator during a power outage. The claim and source summary align, but the stored Evidence Use lacks an exact passage locator. As a food-safety threshold, the estimate must not be treated as a guarantee that any specific food remains safe after that interval.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-FOOD-REFRIGERATOR-4H` | 2 | 2 | 1 | **D=2:** can affect food-safety decisions. **E=2:** the current USDA source/Evidence Use summary directly matches the four-hour guidance, though no pinpoint is stored. **B=1:** the time estimate lacks an explicit condition note in the Claim itself and may be misread as a guarantee for individual foods. |

## Disposition

**HOLD pending exact USDA passage locator, explicit conditions/scope review, and independent Human View.** No canonical record changed; this is not a food-safety clearance.
