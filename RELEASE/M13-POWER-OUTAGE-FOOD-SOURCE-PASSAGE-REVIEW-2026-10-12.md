# M13 Power-Outage Food Claims — Source-Passage Review — 2026-10-12

## Scope and decision boundary

Reviewed the current Claim → Evidence Use → Source chains for three high-consequence Claims in `power-outage-food` against the linked official USDA FSIS and FDA guidance. This is a passage-level review note, **not** a D/E/B score, independent Human View, rights clearance, or publication approval.

Reviewed record versions:
- `CLM-FOOD-REFRIGERATOR-4H` v1; Evidence Use `EU-FOOD-REFRIGERATOR-4H` v1 and `EU-FOOD-REFRIGERATOR-4H-FDA` v1.
- `CLM-FOOD-FREEZER-48H` v1; Evidence Use `EU-FOOD-FREEZER-48H` v1 and `EU-FOOD-FREEZER-48H-FDA` v1.
- `CLM-FOOD-TARGET-TEMP` v1; Evidence Use `EU-FOOD-TARGET-TEMP` v1 and `EU-FOOD-TARGET-TEMP-FDA` v1.
- Sources: `SRC-USDA-POWER-OUTAGE-2024` v1 and `SRC-FDA-POWER-OUTAGE-2026` v1.

## Source passages checked

1. USDA FSIS, “How do you keep food safe during a power failure?”  
   https://ask.fsis.usda.gov/article/How-do-you-keep-food-safe-during-a-power-failure  
   Relevant passage: during a power outage, a refrigerator keeps food cold for about 4 hours if it remains unopened; a full stand-alone freezer holds temperature for about 48 hours (24 hours if half full) if the door remains closed. The answer notes that a refrigerator-freezer compartment may not keep food frozen as long.
2. FDA, “Power Outages: Key Tips for Consumers About Food Safety”  
   https://www.fda.gov/food/food-safety-during-emergencies/power-outages-key-tips-consumers-about-food-safety  
   Relevant headings: “When the Power Goes Out” and “Once the Power is Restored.” The page supports the 4-hour unopened-refrigerator guidance, the 48/24-hour freezer estimates with doors closed, refrigerator temperature at 40 °F or below, and the need to assess food after power returns rather than rely on appearance or smell.
3. FDA, “Are You Storing Food Safely?”  
   https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely  
   Relevant passage: refrigerator at or below 40 °F (4 °C) and freezer at or below 0 °F (-18 °C). This is consistent with the Claim's rounded conversions, with minor rounding differences from the record's 4.4 °C and -17.8 °C equivalents.

## Claim-level findings

### `CLM-FOOD-REFRIGERATOR-4H` v1

**Statement:** “При отключении электроэнергии закрытый холодильник сохраняет продукты холодными примерно 4 часа.”

**Finding:** Directly supported when “закрытый” means the door remains unopened/closed as much as possible. The statement is a time estimate, not a guarantee that every item remains safe regardless of starting temperature, door opening, appliance condition, or ambient conditions.

**Evidence-use defect:** Both linked Evidence Use descriptions summarize the claim but contain no reproducible heading/paragraph locator or quoted passage. FDA and USDA both publish substantially matching emergency guidance; the presence of two agencies does not by itself establish independent empirical corroboration.

**Disposition:** Passage support found; HOLD pending versioned Evidence Use locator correction and independent Human View.

### `CLM-FOOD-FREEZER-48H` v1

**Statement:** “При закрытой двери полный отдельностоящий морозильник сохраняет температуру примерно 48 часов, а наполовину заполненный — примерно 24 часа.”

**Finding:** Directly supported by the USDA FSIS passage and FDA guidance. Preserve all qualifiers: a full versus half-full freezer, a closed door, approximate time, and a stand-alone freezer. Do not generalize this to the freezer compartment of a refrigerator-freezer, which the USDA answer explicitly distinguishes.

**Evidence-use defect:** The two Evidence Use descriptions lack reproducible passage locators. The records' use of `independent_evidence_link` should not be read as a proven independence finding; the reviewed guidance repeats the same public-safety estimates and likely reflects common guidance lineage.

**Disposition:** Passage support found; HOLD pending versioned Evidence Use locator correction, source-lineage/independence review, and independent Human View.

### `CLM-FOOD-TARGET-TEMP` v1

**Statement:** “В указанной рекомендации USDA FSIS безопасная рабочая температура холодильника — 40 °F (4,4 °C) или ниже, а морозильника — 0 °F (-17,8 °C) или ниже.”

**Finding:** Supported as a statement about the cited USDA guidance. The FDA storage page independently states 40 °F (4 °C) for the refrigerator and 0 °F (-18 °C) for the freezer; the Celsius conversions differ only by rounding. Keep the current wording anchored to the named guidance rather than presenting these values as a complete food-safety test for every item after an outage.

**Evidence-use defect:** Neither Evidence Use record includes a reproducible locator. The FDA and USDA values are consistent, but this review does not establish independence of the underlying guidance.

**Disposition:** Passage support found; HOLD pending versioned Evidence Use locator correction and independent Human View.

## Required follow-up

1. Under the repository's correction-authorization rules, make bounded, versioned Evidence Use corrections that name the exact source heading and relevant passage; preserve prior versions and history.
2. Review whether the two agencies' pages constitute independent evidence or duplicate/common-lineage guidance; describe corroboration conservatively.
3. Independently verify each Claim's scope, context, wording, and emergency-food-safety implications before any pilot use.
4. Reconcile any future score with the current inventory-to-ledger join; this review adds no D/E/B score.

## Controls

- No canonical JSON was changed.
- No D/E/B score was assigned or altered.
- No allowlist, release status, or publication decision was changed.
- These three Claims remain HOLD for pilot/publication clearance.
