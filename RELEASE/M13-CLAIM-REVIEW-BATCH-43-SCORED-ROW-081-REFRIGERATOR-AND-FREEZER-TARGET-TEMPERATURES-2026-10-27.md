# M13 Batch 43 — Scored row 081: Refrigerator and freezer target temperatures

Date: 2026-10-27  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-FOOD-TARGET-TEMP@1`  
Evidence Use version: `EU-FOOD-TARGET-TEMP@1`  
Source version: `SRC-USDA-POWER-OUTAGE-2024@1`

## Claim under review

> В указанной рекомендации USDA FSIS безопасная рабочая температура холодильника — 40 °F (4,4 °C) или ниже, а морозильника — 0 °F (-17,8 °C) или ниже.

## Passage checked

The canonical Source record points to USDA FSIS, “How do you keep food safe during a power failure?” The live page focuses on how long refrigerated and frozen food remains cold during an outage (about four hours for a refrigerator and about 48 hours for a full freezer), and does not state the specific refrigerator/freezer target temperatures in the page text retrieved. The Claim and Evidence Use mention the 40 °F and 0 °F thresholds, but the canonical source chain does not substantiate them. A separate source that explicitly states those temperatures must be linked and pinpointed before this Claim can pass.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-FOOD-TARGET-TEMP` | 3 | 1 | 3 | **D=3:** precise, measurable guidance. **E=1:** the canonical USDA outage page retrieved does not directly establish the stated temperature thresholds. **B=3:** food-safety thresholds can materially affect health decisions. |

## Disposition

**HOLD** pending canonical source alignment, exact passage locator, attribution/rights review where applicable, and independent review. No canonical Claim, Evidence Use, or Source record changed. No publication clearance is granted by this assessment.
