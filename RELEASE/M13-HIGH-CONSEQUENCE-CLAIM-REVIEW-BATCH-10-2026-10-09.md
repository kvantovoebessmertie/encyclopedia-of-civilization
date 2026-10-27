# M13 High-Consequence Claim Review — Batch 10
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: five power-outage food-safety claims and linked Evidence Use / Source records in `power-outage-food`.
Review type: targeted high-consequence review. No content records changed in this batch.

## Scoring rubric
- **D — explanatory depth (0–3):** explanatory value and practical meaning.
- **E — claim-specific evidence fit (0–3):** fit of the linked source and Evidence Use to the exact proposition.
- **B — boundaries / epistemic discipline (0–3):** applicability limits and prevention of overgeneralization.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM-FOOD-FREEZER-48H` — D2 / E3 / B3
**Statement:** With the door closed, a full standalone freezer holds temperature for about 48 hours; a half-full one for about 24 hours.

**Linked records:** `EU-FOOD-FREEZER-48H` → USDA FSIS; `EU-FOOD-FREEZER-48H-FDA` → FDA.

**External check:** FDA's [Power Outages: Key Tips for Consumers About Food Safety](https://www.fda.gov/food/food-safety-during-emergencies/power-outages-key-tips-consumers-about-food-safety) states that a full freezer maintains temperature for approximately 48 hours and a half-full freezer for approximately 24 hours if the door remains closed. USDA/FDA guidance is consistent on this practical estimate.

**Assessment:** The claim gives the key condition (closed door), differentiates full and half-full freezers, and uses approximate rather than absolute timing. Two official sources support it. The linked FDA Evidence Use repeats the same support sentence twice, which is a documentation-quality defect but does not invalidate the claim.

**Disposition:** No substantive claim defect found. Clean up duplicated evidence prose in a narrow correction pass if the correction queue authorizes it.

### 2. `CLM-FOOD-NO-OUTDOOR-FREEZER` — D2 / E2 / B3
**Statement:** During a power outage, do not use outdoors as an improvised refrigerator/freezer, even in winter, because temperatures fluctuate and food may be contaminated or thaw.

**Linked record:** `EU-FOOD-NO-OUTDOOR-FREEZER` → Health Canada.

**External check:** Health Canada's [Food and drinking water safety in an emergency](https://www.canada.ca/en/health-canada/services/food-drinking-water-safe-emergency.html) explicitly says not to place frozen food outside even in winter: animals may contaminate it and sunlight may thaw it even when air temperature is very cold.

**Assessment:** Good practical advice with a clear explanation and useful boundary. The claim's “temperature can fluctuate” is reasonable but the linked Evidence Use specifically records the source's contamination and thawing rationale; no material mismatch was identified. Because this is Canadian public-health guidance, it should be presented as safety advice rather than a jurisdiction-specific legal requirement.

**Disposition:** No immediate content change indicated.

### 3. `CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY` — D3 / E2 / B3
**Statement:** The approximately four-hour estimate applies to an unopened refrigerator; after power returns, check actual temperatures, and do not treat elapsed time as a measurement of the temperature of a specific food.

**Linked record:** `EU-FOOD-OUTAGE-THRESHOLD-BOUNDARY` → FDA.

**External check:** FDA says to keep the refrigerator closed, treats about four hours as the estimate for an unopened refrigerator, and advises checking appliance/food temperatures after power returns. It also warns not to rely on appearance or odor.

**Assessment:** This is a strong boundary claim: it explicitly prevents a rough time estimate from being misused as a direct food-temperature measurement. The Evidence Use is claim-specific and accurately reflects the source. The next practical step should remain discoverable: discard perishable food that has been above 40 °F / 4.4 °C for the specified period, following the source guidance.

**Disposition:** No claim defect found. Human View should verify that this boundary is presented next to the practical keep/discard instructions.

### 4. `CLM-FOOD-REFRIGERATOR-4H` — D2 / E3 / B2
**Statement:** During a power outage, a closed refrigerator keeps food cold for about four hours.

**Linked records:** `EU-FOOD-REFRIGERATOR-4H` → USDA FSIS; `EU-FOOD-REFRIGERATOR-4H-FDA` → FDA.

**External check:** FDA's current power-outage guidance directly gives the four-hour estimate for an unopened refrigerator. USDA/FDA sources agree.

**Assessment:** The claim is concise and supported by two official sources. The Evidence Use records both state the support twice, creating avoidable duplication. The statement itself is correctly approximate but depends on keeping the door closed; that condition is included in the wording.

**Disposition:** No substantive defect. Remove redundant Evidence Use prose only if covered by the authorized correction pass.

### 5. `CLM-FOOD-TARGET-TEMP` — D2 / E3 / B2
**Statement:** The cited USDA FSIS guidance sets a safe operating target of 40 °F / 4.4 °C or lower for the refrigerator and 0 °F / −17.8 °C or lower for the freezer.

**Linked records:** `EU-FOOD-TARGET-TEMP` → USDA FSIS; `EU-FOOD-TARGET-TEMP-FDA` → FDA.

**External check:** FDA's [food safety during power outages](https://www.fda.gov/food/food-safety-during-emergencies/power-outages-key-tips-consumers-about-food-safety) recommends a refrigerator at 40 °F or below and gives 0 °F as the freezer target. Health Canada provides the same Celsius-equivalent targets.

**Assessment:** Specific and supported by independent official sources. The statement appropriately attributes the values to a cited recommendation instead of asserting that they are universal legal limits. The most useful Human View test is whether readers understand these are appliance-storage targets and not a guarantee that any food is safe after a long outage.

**Disposition:** No immediate content change indicated.

## Batch findings
1. These five claims form a strong practical chain: keep doors closed, understand approximate time windows, avoid improvised outdoor storage, check actual temperatures and apply food-specific safety guidance.
2. The strongest feature is explicit boundary-setting around estimates. The corpus correctly distinguishes time-based guidance from actual measured food temperature.
3. Some Evidence Use descriptions repeat identical sentences twice. This is a low-severity documentation defect, not a substantive safety error.
4. Cross-source corroboration is claim-specific rather than source-count-only; FDA, USDA FSIS and Health Canada are used for propositions they actually address.
5. This is a five-claim purposive sample, not a full audit of power-outage food safety. The linked source guidance and thresholds are U.S./Canadian public-health recommendations; local authorities and food-specific guidance may differ.

## Required follow-up
- Add duplicate Evidence Use prose to a low-severity documentation cleanup list, avoiding broad rewrites.
- Human View test whether users can move from the four-hour/48-hour estimates to temperature-based decisions and the specific discard rules.
- Continue the full Claim D/E/B census, high-consequence overlay, Human View, Relation audit and independent review.

## Audit boundary
Review artifact only. No corpus records were edited. M13 remains open; this batch does not close any audit phase.
