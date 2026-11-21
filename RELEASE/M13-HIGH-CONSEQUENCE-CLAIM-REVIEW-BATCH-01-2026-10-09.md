# M13 High-Consequence Claim Review — Batch 01

**Date:** 2026-10-09  
**Branch:** `m13-system-wide-depth-audit-2026-10-09`  
**Worksheet source:** CI artifact `m13-claim-audit-worksheet`, generated for branch head `2d8545a083082decf4bd850e02e0db136e3539eb` (workflow checks out a PR merge candidate; the worksheet's own `source_revision` is the checked-out merge-candidate SHA).  
**Purpose:** First substantive claim/evidence review, not a closure report. Scores are reviewer assessments of the displayed claim and linked Evidence Use material; they are not automatic classifications. The linked official source pages for CO response/alarms, chemical water advisories, electrical safety, food safety, and hypothermia were checked during this batch. Source verification confirms support for several claims but also exposes where the Evidence Use text fails to record the actual supporting detail.

## Scoring

- **D — explanatory depth:** 0–3.
- **E — claim-specific evidence fit:** 0–3.
- **B — boundaries and epistemic discipline:** 0–3.

A low E score here can mean the Evidence Use material is boilerplate or too thin to show the match, even where the named institutional source is plausible. It does **not** by itself establish that the underlying claim is false.

## Batch results

| Claim ID | Slice | D | E | B | Assessment |
|---|---|---:|---:|---:|---|
| `CLM-CO-HEATING-ALARMS` | carbon-monoxide-heating-safety | 2 | 1 | 1 | Practical, specific placement advice; linked CDC source is relevant, but Evidence Use is only “CDC directly supports the recorded recommendation” and does not state the source's actual recommendation or applicable scope. Check local installation/code wording in the next source-verification pass. |
| `CLM-CO-HEATING-EMERGENCY` | carbon-monoxide-heating-safety | 3 | 2 | 3 | Clear trigger (alarm or possible symptoms), immediate action, and explicit no-return boundary. CPSC page directly confirms move outside, call emergency services, and do not re-enter until responders permit return. The claim's safety boundary is source-verified. |
| `CLM-CO-HEATING-MAINTENANCE` | carbon-monoxide-heating-safety | 2 | 2 | 2 | Useful maintenance rule and clear statement that alarms do not replace safe use/maintenance. Evidence Use captures the relevant role of alarms, though manufacturer instructions and local inspection requirements are not elaborated. |
| `CLM-CO-HEATING-OUTSIDE` | carbon-monoxide-heating-safety | 2 | 1 | 2 | Important and clear prohibition for fuel-burning devices indoors or in partially enclosed spaces. CDC is an appropriate source family, but Evidence Use is a one-line assertion rather than a traceable summary of the source's actual rule. |
| `CLM-CHEM-WATER-NO-BOIL` | chemical-water-advisory | 2 | 3 | 3 | Correctly bounded to water contaminated by harmful chemicals/toxins; Evidence Use gives the precise boiling/disinfection limitation and links both EPA and CDC. Strong evidence-fit example in this batch. |
| `CLM-CHEM-WATER-NO-DRINK` | chemical-water-advisory | 2 | 1 | 2 | Condition is explicit: a “do not drink” advisory tied to possible chemical contamination. The CDC page explicitly defines “do not drink” advisories as requiring commercially bottled water for drinking and cooking. The claim is source-supported; the Evidence Use material should state that specific instruction instead of only describing the boiling limitation. |
| `CLM-COLD-HYPOTHERMIA-EMERGENCY` | cold-weather-hypothermia | 2 | 3 | 2 | Urgent action and 35 °C / 95 °F threshold are stated; two institutional sources are linked and the Evidence Use summaries directly describe the threshold and urgency. The statement could distinguish suspected hypothermia from a measured temperature threshold more clearly, since care should not be delayed to obtain a measurement. |
| `CLM-COLD-HYPOTHERMIA-SIGNS` | cold-weather-hypothermia | 2 | 2 | 2 | Useful symptom list with a defined population (adults) and CDC source summary. It does not state that symptoms may vary or that not every sign must be present; consider adding that boundary in a later content-fix pass. |
| `CLM-COLD-HYPOTHERMIA-WETNESS` | cold-weather-hypothermia | 2 | 2 | 2 | Adds an important boundary beyond severe frost: prolonged cold/water exposure and wet clothing increase risk. Evidence Use describes the source's scope but not a more precise exposure threshold, which is acceptable for a general risk statement. |
| `CLM-ELECTRICAL_SAFETY_BASICS-A` | electrical-safety-basics | 1 | 1 | 1 | Valid-looking hazard inventory, but explanatory depth is a list rather than a mechanism or control. Evidence Use is generic boilerplate; it does not show how NIOSH supports each listed hazard. Source check confirms NIOSH lists electric shock/burns, arcing, and fire from faulty equipment or installations. The claim is supported; the Evidence Use material remains too generic to make that support auditable. |
| `CLM-ELECTRICAL_SAFETY_BASICS-B` | electrical-safety-basics | 2 | 1 | 2 | Establishes a qualified-person boundary and mentions procedures/PPE. Source check confirms NIOSH limits energized work to qualified persons and requires appropriate PPE and safety procedures. The claim is supported; Evidence Use should record those source-specific details. The slice has a separate OSHA claim, but it is not linked as corroboration to this claim. |
| `CLM-ELECTRICAL_SAFETY_BASICS-C` | electrical-safety-basics | 2 | 1 | 2 | Safe default for unqualified people is clear. Source check supports the qualified-person boundary and says unqualified persons should not work on energized parts. Evidence Use should record this detail; retain the claim as a safe default rather than implying all electrical interactions have identical risk. |
| `CLM-FOOD_SAFETY_BASICS-A` | food-safety-basics | 1 | 1 | 1 | Four-part food-safety summary is useful but compressed; Evidence Use is generic boilerplate and gives no claim-specific support for cleaning, separation, heating, and cooling. FDA source check confirms the four-step framework (clean, separate, cook, chill). The claim is supported, but Evidence Use should name those four steps and their role rather than use generic boilerplate. |
| `CLM-FOOD_SAFETY_BASICS-B` | food-safety-basics | 2 | 1 | 2 | Mechanism/risk is named (cross-contamination), but Evidence Use is generic boilerplate. FDA source check explicitly advises keeping raw meat, poultry, seafood, and eggs away from other foods to prevent cross-contamination. The claim is supported; Evidence Use should record that direct match. |
| `CLM-FOOD_SAFETY_BASICS-C` | food-safety-basics | 2 | 1 | 2 | Correctly signals context dependence (product, process, rules), but Evidence Use is generic boilerplate and does not show which source supports the variability claim. The FDA page confirms the general variability statement is plausible but does not itself establish jurisdiction-specific requirements. Evidence Use needs a source that directly supports the contextual/normative part, or the claim should be narrowed to product/process variability. |

## Findings from this batch

1. **Confirmed documentation-quality issue:** Several high-consequence claims have an Evidence Use record that merely says a source “directly supports” or is “used within the stated material,” without describing the source-specific support. This weakens auditability even where the source itself appears appropriate.
2. **No factual falsehood is declared from boilerplate alone.** These claims need source-specific evidence summaries and targeted source verification before content edits are approved.
3. **Positive control:** `CLM-CHEM-WATER-NO-BOIL` demonstrates a stronger pattern: the Evidence Use states the exact limitation, and two institutional sources independently support it.
4. **Potential content-boundary improvement:** the hypothermia emergency claim should make clear that suspected hypothermia warrants urgent help without waiting to measure body temperature.
5. **Next review batch:** verify the linked pages for the 15 claims above; then continue with high-consequence water, fire/CO, electrical, chemical, construction, and emergency claims whose Evidence Use material is generic or short. Record source mismatch as a confirmed defect only after inspecting the source.

## Status

**Batch 01 reviewed; M13 remains OPEN.** This is a purposive high-consequence batch, not a statistically representative sample and not the full 1,494-claim D/E/B census. No claim records, schemas, relation types, or tests were changed by this review.


## Source-verification update

Official pages were checked after the initial scoring pass:

- **CO alarms and response:** CPSC confirms alarms on every level and outside sleeping areas, and says to leave immediately, call emergency services, and not re-enter until responders permit it: https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Carbon-Monoxide-Questions-and-Answers. CDC also confirms alarm placement and fuel-burning-device precautions: https://www.cdc.gov/carbon-monoxide/about/index.html. The linked claims are substantively supported; the very short Evidence Use material remains a traceability weakness.
- **Chemical water advisories:** EPA says boiling/disinfection does not remove heavy metals, salts, and most other chemicals: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water. CDC explicitly says “do not drink” advisories require commercially bottled water for drinking and cooking, and that boiling chemically contaminated water does not make it safe: https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html. Both water claims are source-supported; the Evidence Use record for `CLM-CHEM-WATER-NO-DRINK` should explicitly document the bottled-water instruction.
- **Electrical safety:** NIOSH explicitly lists shock/burns, arcing and fire, restricts energized work to qualified persons, and describes PPE/procedure requirements: https://www.cdc.gov/niosh/electrical-safety/about/. The three basic claims are supported, but their Evidence Use material is boilerplate and should be rewritten with those details.
- **Food safety:** FDA's “Food Safety at Home” page explicitly gives the four steps clean, separate, cook, and chill, including separation of raw foods to prevent cross-contamination: https://www.fda.gov/consumers/womens-health-topics/food-safety-home. Claims A and B are supported. Claim C's jurisdiction-specific portion is not established by that general FDA page; it needs a more suitable source or narrower wording.
- **Hypothermia:** CDC confirms the symptom list and advises immediate medical attention for signs of hypothermia: https://www.cdc.gov/natural-disasters/psa-toolkit/recognizing-hypothermia.html. The NWS/CDC threshold material also supports urgent response below 35 °C / 95 °F. Preserve the warning not to delay action while trying to obtain a temperature.

This pass found **no confirmed factual falsehood** among these 15 claims. It did confirm an Evidence Use quality issue in the electrical and food-safety claims, and a source-scope gap for the jurisdiction-specific portion of `CLM-FOOD_SAFETY_BASICS-C`. The latter is a **candidate for correction**, not a content edit yet; next step is to inspect the relevant source record and decide whether to add a better source or narrow the claim.
