# M13 Batch 42 — Scored row 044: freezer outage time guidance

Date: 2026-10-18  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-FOOD-FREEZER-48H@1`  
Evidence Use version: `EU-FOOD-FREEZER-48H@1`  
Source version: `SRC-USDA-POWER-OUTAGE-2024@1`

## Claim under review

> При закрытой двери полный отдельностоящий морозильник сохраняет температуру примерно 48 часов, а наполовину заполненный — примерно 24 часа.

## Evidence fit

The canonical Source is USDA FSIS, “How do you keep food safe during a power failure?”:
https://ask.fsis.usda.gov/article/How-do-you-keep-food-safe-during-a-power-failure

The Evidence Use directly repeats the approximate 48-hour guidance for a full freestanding freezer and 24 hours for a half-full freezer when the door remains closed. This is a strong summary-level match. However, the source passage and its precise conditions are not pinned in the Evidence Use, and the claim is consequential food-safety guidance that should retain the distinction between general time guidance and the actual temperature/state of food.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-FOOD-FREEZER-48H` | 2 | 2 | 1 | **D=2:** this can inform food-safety decisions during an outage. **E=2:** USDA FSIS and the Evidence Use align on both time estimates and the closed-door condition, but the exact locator is missing. **B=1:** the time estimate is stated clearly, yet actual safety depends on conditions and should not be inferred from time alone. |

## Disposition

**HOLD pending exact USDA passage locator, condition/scope review, and independent Human View.** No canonical record changed; this is not a food-safety clearance.
