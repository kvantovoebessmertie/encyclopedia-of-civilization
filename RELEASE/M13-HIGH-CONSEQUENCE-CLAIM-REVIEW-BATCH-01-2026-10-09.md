# M13 High-Consequence Claim Review — Batch 01

**Date:** 2026-10-09  
**Branch:** `m13-system-wide-depth-audit-2026-10-09`  
**Worksheet source:** CI artifact `m13-claim-audit-worksheet`, generated for branch head `2d8545a083082decf4bd850e02e0db136e3539eb` (workflow checks out a PR merge candidate; the worksheet's own `source_revision` is the checked-out merge-candidate SHA).  
**Purpose:** First substantive claim/evidence review, not a closure report. Scores are reviewer assessments of the displayed claim and linked Evidence Use material; they are not automatic classifications. Source-page contents have not been independently re-fetched in this batch, so any conclusion depending on details beyond the linked source identity/URI remains provisional.

## Scoring

- **D — explanatory depth:** 0–3.
- **E — claim-specific evidence fit:** 0–3.
- **B — boundaries and epistemic discipline:** 0–3.

A low E score here can mean the Evidence Use material is boilerplate or too thin to show the match, even where the named institutional source is plausible. It does **not** by itself establish that the underlying claim is false.

## Batch results

| Claim ID | Slice | D | E | B | Assessment |
|---|---|---:|---:|---:|---|
| `CLM-CO-HEATING-ALARMS` | carbon-monoxide-heating-safety | 2 | 1 | 1 | Practical, specific placement advice; linked CDC source is relevant, but Evidence Use is only “CDC directly supports the recorded recommendation” and does not state the source's actual recommendation or applicable scope. Check local installation/code wording in the next source-verification pass. |
| `CLM-CO-HEATING-EMERGENCY` | carbon-monoxide-heating-safety | 3 | 2 | 3 | Clear trigger (alarm or possible symptoms), immediate action, and explicit no-return boundary. CPSC Evidence Use summarizes the core action and return restriction. Verify exact wording against the linked CPSC page before final sign-off. |
| `CLM-CO-HEATING-MAINTENANCE` | carbon-monoxide-heating-safety | 2 | 2 | 2 | Useful maintenance rule and clear statement that alarms do not replace safe use/maintenance. Evidence Use captures the relevant role of alarms, though manufacturer instructions and local inspection requirements are not elaborated. |
| `CLM-CO-HEATING-OUTSIDE` | carbon-monoxide-heating-safety | 2 | 1 | 2 | Important and clear prohibition for fuel-burning devices indoors or in partially enclosed spaces. CDC is an appropriate source family, but Evidence Use is a one-line assertion rather than a traceable summary of the source's actual rule. |
| `CLM-CHEM-WATER-NO-BOIL` | chemical-water-advisory | 2 | 3 | 3 | Correctly bounded to water contaminated by harmful chemicals/toxins; Evidence Use gives the precise boiling/disinfection limitation and links both EPA and CDC. Strong evidence-fit example in this batch. |
| `CLM-CHEM-WATER-NO-DRINK` | chemical-water-advisory | 2 | 1 | 2 | Condition is explicit: a “do not drink” advisory tied to possible chemical contamination. The linked CDC source is relevant, but the Evidence Use sentence summarizes the boiling limitation more directly than the bottled-water instruction; confirm that the cited advisory explicitly supports the recommended substitute. |
| `CLM-COLD-HYPOTHERMIA-EMERGENCY` | cold-weather-hypothermia | 2 | 3 | 2 | Urgent action and 35 °C / 95 °F threshold are stated; two institutional sources are linked and the Evidence Use summaries directly describe the threshold and urgency. The statement could distinguish suspected hypothermia from a measured temperature threshold more clearly, since care should not be delayed to obtain a measurement. |
| `CLM-COLD-HYPOTHERMIA-SIGNS` | cold-weather-hypothermia | 2 | 2 | 2 | Useful symptom list with a defined population (adults) and CDC source summary. It does not state that symptoms may vary or that not every sign must be present; consider adding that boundary in a later content-fix pass. |
| `CLM-COLD-HYPOTHERMIA-WETNESS` | cold-weather-hypothermia | 2 | 2 | 2 | Adds an important boundary beyond severe frost: prolonged cold/water exposure and wet clothing increase risk. Evidence Use describes the source's scope but not a more precise exposure threshold, which is acceptable for a general risk statement. |
| `CLM-ELECTRICAL_SAFETY_BASICS-A` | electrical-safety-basics | 1 | 1 | 1 | Valid-looking hazard inventory, but explanatory depth is a list rather than a mechanism or control. Evidence Use is generic boilerplate; it does not show how NIOSH supports each listed hazard. Prioritize evidence-material repair and check the source's exact hazard list. |
| `CLM-ELECTRICAL_SAFETY_BASICS-B` | electrical-safety-basics | 2 | 1 | 2 | Establishes a qualified-person boundary and mentions procedures/PPE. Evidence Use is generic boilerplate and does not substantiate the qualification, procedure, or PPE wording. The slice has a separate OSHA claim, but it is not linked as corroboration to this claim. |
| `CLM-ELECTRICAL_SAFETY_BASICS-C` | electrical-safety-basics | 2 | 1 | 2 | Safe default for unqualified people is clear. Evidence Use repeats generic boilerplate; source-fit should be made explicit, and the statement should avoid implying that every interaction with any electrical system is identical in risk. |
| `CLM-FOOD_SAFETY_BASICS-A` | food-safety-basics | 1 | 1 | 1 | Four-part food-safety summary is useful but compressed; Evidence Use is generic boilerplate and gives no claim-specific support for cleaning, separation, heating, and cooling. Needs a specific summary of the FDA material or separate source mappings. |
| `CLM-FOOD_SAFETY_BASICS-B` | food-safety-basics | 2 | 1 | 2 | Mechanism/risk is named (cross-contamination), but Evidence Use is generic boilerplate. Add a source-specific summary that identifies the raw/ready-to-eat separation guidance. |
| `CLM-FOOD_SAFETY_BASICS-C` | food-safety-basics | 2 | 1 | 2 | Correctly signals context dependence (product, process, rules), but Evidence Use is generic boilerplate and does not show which source supports the variability claim. Jurisdiction-specific requirements should be tied to applicable authorities where presented as binding. |

## Findings from this batch

1. **Confirmed documentation-quality issue:** Several high-consequence claims have an Evidence Use record that merely says a source “directly supports” or is “used within the stated material,” without describing the source-specific support. This weakens auditability even where the source itself appears appropriate.
2. **No factual falsehood is declared from boilerplate alone.** These claims need source-specific evidence summaries and targeted source verification before content edits are approved.
3. **Positive control:** `CLM-CHEM-WATER-NO-BOIL` demonstrates a stronger pattern: the Evidence Use states the exact limitation, and two institutional sources independently support it.
4. **Potential content-boundary improvement:** the hypothermia emergency claim should make clear that suspected hypothermia warrants urgent help without waiting to measure body temperature.
5. **Next review batch:** verify the linked pages for the 15 claims above; then continue with high-consequence water, fire/CO, electrical, chemical, construction, and emergency claims whose Evidence Use material is generic or short. Record source mismatch as a confirmed defect only after inspecting the source.

## Status

**Batch 01 reviewed; M13 remains OPEN.** This is a purposive high-consequence batch, not a statistically representative sample and not the full 1,494-claim D/E/B census. No claim records, schemas, relation types, or tests were changed by this review.
