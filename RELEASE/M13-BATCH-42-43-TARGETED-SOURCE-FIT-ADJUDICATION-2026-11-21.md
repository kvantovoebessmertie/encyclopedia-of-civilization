# M13 Batch 42–43 — targeted source-fit adjudication addendum

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: targeted external source verification arising from the 200-report master crosswalk.  
Mutation boundary: **read-only source verification. No canonical record changed.**

## Executive result

Five source-fit questions were directly rechecked against official publisher pages. The findings sharpen the remediation queue:

1. **Batch 42 row 018 — confirmed CPSC source mismatch.** The currently linked May 27, 2026 CPSC page does not contain the generator refuelling/cooling instruction. A different official CPSC release dated January 23, 2026 contains the exact instruction.
2. **Batch 42 row 030 — direct source candidate found.** The same January 23 CPSC release directly recommends battery-powered flashlights or lanterns instead of candles during a power outage. The current NFPA candle-safety Source/EU should not be presumed to prove that preference without a passage check.
3. **Batch 43 row 081 — the secondary FDA edge is not yet sufficient.** The current canonical FDA Source URL supports the refrigerator 40°F threshold but not the freezer 0°F threshold. A different FDA page directly states both thresholds.
4. **Batch 43 row 012 — prior report's URL transcription is wrong; current Source history does not show an unversioned mutation.** The current canonical Source URI already contained the valid WHO path at its only recorded introduction commit (2026-10-05) and is unchanged now. The older URL quoted in the row report returns 404. The current WHO page directly supports the Claim.
5. **Batch 42 row 068 — source-fit defect confirmed.** The current WHO Source points to a participatory-surveillance news item, not a direct epidemiology definition. WHO's *Basic Epidemiology*, second edition, Box 1.2 is a direct definition candidate.

These are evidence findings and correction proposals only. They do not change current D/E/B, do not clear HOLD, and do not authorize canonical edits.

## 1. Batch 42 row 018 — generator refuelling/cooling

### Current canonical chain

- Claim: `CLM-GENERATOR-REFUEL-COOL@1`
- EU: `EU-GENERATOR-REFUEL-COOL@1`
- Source: `SRC-CPSC-GENERATOR-2026@1`
- Current Source URI: https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Warns-of-Generator-Carbon-Monoxide-and-Fire-Hazards-Ahead-of-Hurricane-Season

### Direct inspection

The linked CPSC page is dated May 27, 2026. Its generator section covers outdoor use, distance from buildings, carbon-monoxide shutoff features and maintenance; it does not state the rule to stop and cool a generator before refuelling. Its page text was inspected directly.

A separate CPSC release dated January 23, 2026, *Keep Warm and Safe This Winter: Tips for Using Generators, Furnaces and Space Heaters*, has a “Generators” section stating: “Never refuel a generator while it is running. Turn off generators and let them cool before refueling.”

Direct official page: https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters

### Finding and disposition

**CONFIRMED CURRENT SOURCE/EU MISMATCH.** The exact support exists in a different official CPSC resource, but that page is not the current canonical Source. Preserve the historical row score (2/1/1) as historical only. A future bounded correction should add a distinct Source record for the January 23 release and a versioned EU edge with the exact “Generators” section locator, or otherwise follow the project's explicit source-versioning policy. Do not silently repoint the current Source or overwrite its history.

## 2. Batch 42 row 030 — flashlight preference during power outage

### Current canonical chain

- Claim: `CLM-LIGHTING-FLASHLIGHT-OUTAGE@1`
- EU: `EU-LIGHTING-FLASHLIGHT-OUTAGE@1`
- Source: `SRC-NFPA-CANDLE-SAFETY-2026@1`
- Current Source URI: https://www.nfpa.org/education-and-research/home-fire-safety/candles

### Direct source candidate

The CPSC January 23, 2026 release cited above has a dedicated section “Use Flashlights Instead of Candles” and says to use battery-powered flashlights or lanterns instead of candles during a power outage. It also says never to leave burning candles unattended.

This is a direct official passage candidate for the Claim's preference. The current NFPA candle-safety chain remains the canonical historical chain and must not be silently substituted or assumed to contain the same recommendation.

### Finding and disposition

**DIRECT ALTERNATE SOURCE IDENTIFIED.** Add a separately versioned CPSC Source/EU edge only after bounded authorization and exact locator review. Retain the NFPA edge if it independently supports other candle-safety propositions; do not flatten source roles.

## 3. Batch 43 row 081 — refrigerator/freezer target temperatures

### Current canonical primary and secondary chains

- Claim: `CLM-FOOD-TARGET-TEMP@1`
- Primary USDA EU/Source: `EU-FOOD-TARGET-TEMP@1` → `SRC-USDA-POWER-OUTAGE-2024@1`
- Secondary FDA EU/Source: `EU-FOOD-TARGET-TEMP-FDA@1` → `SRC-FDA-POWER-OUTAGE-2026@1`
- Current FDA Source URI: https://www.fda.gov/food/food-safety-during-emergencies/power-outages-key-tips-consumers-about-food-safety

### Direct inspection

The current FDA Source URL, *Power Outages: Key Tips for Consumers About Food Safety*, directly states that refrigerators should be kept at 40°F or below and gives the approximately four-hour unopened-refrigerator interval. The inspected page does not state the freezer's 0°F target.

A different FDA page, *Food and Water Safety During Power Outages and Floods*, has a section “Prepare Yourself Before Power Emergencies” that directly says: freezer at or below 0°F and refrigerator at or below 40°F.

Direct official page: https://www.fda.gov/food/buy-store-serve-safe-food/food-and-water-safety-during-power-outages-and-floods

The same FDA page's “Power Outages: During and After” section gives the approximately four-hour refrigerator and 48-hour/24-hour freezer intervals, but those duration statements are distinct from the steady-state target-temperature claim.

### Finding and disposition

**SECONDARY FDA EDGE PARTIALLY SUPPORTS, NOT FULLY SUPPORTS.** The current FDA EU's summary includes 0°F, but its linked Source URL does not. The different FDA page is a direct candidate for the freezer threshold. A future bounded correction should create a distinct Source/EU edge for the exact page and section, or version the Source according to the established correction policy. Until then, the historical E=1 and HOLD remain; the existing FDA EU must not be counted as resolving the 0°F gap.

## 4. Batch 43 row 012 — WHO drinking-water guideline URI and version history

### Current canonical record

- Claim: `CLM_WATER_QUALITY_WHO_A@1`
- EU: `EU_WATER_QUALITY_WHO_A@1`
- Source: `SRC_WATER_QUALITY_WHO@1`
- Current Source URI: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/water-safety-and-quality/drinking-water-quality-guidelines

### Source-history check

The GitHub path history for the Source record returns one recorded introduction commit: `9c1df38dcab8ff76e5103799cd1f360536530444` (2026-10-05). Fetching the Source JSON at that commit and at the current M13 branch yields the same `record_version=1` and the same current WHO URI. No later change to this Source record was found in the path history.

The Batch 43 row 012 report quotes a different URL that omits the `water-safety-and-quality` path segment. Direct retrieval of that older URL returns 404; the current canonical URL resolves to WHO's “Drinking-water quality guidelines” page.

The current WHO page states that the Guidelines promote public-health protection through locally relevant health-based targets, preventive risk management from catchment to consumer (Water Safety Plans), and independent surveillance. The page identifies the current fourth edition incorporating the first, second and third addenda, dated 17 June 2026.

### Finding and disposition

**THE REPORTED VERSION-HISTORY DEFECT IS NOT SUBSTANTIATED BY THE CURRENT SOURCE HISTORY.** The evidence indicates a report-to-record URL transcription/staleness discrepancy, not an observed unversioned canonical Source mutation. Correct the audit interpretation in a future report addendum; do not bump Source version merely to repair the report's copied URL.

The canonical EU still has no precise passage locator. A future authorized EU correction should point to the WHO page heading “Drinking-water quality guidelines” and its paragraph describing health-based targets, preventive risk management and independent surveillance. Keep the Claim's “basis for protecting public health” phrasing as a framework description, not a guarantee of safety for any particular supply.

## 5. Batch 42 row 068 — epidemiology definition

### Current canonical chain

- Claim: `CLM-EPIDEMIOLOGY_BASICS-D@1`
- EU: `EU-EPIDEMIOLOGY_BASICS-D-WHO@1`
- Source: `SRC-WHO-EPIDEMIOLOGY-2024@1`
- Current Source URI: https://www.who.int/news/item/16-10-2024-putting-participatory-surveillance-into-practice--new-who-publication-released

### Finding

The current Source identity is a WHO news item about participatory surveillance. It is not a direct epidemiology definition. The row report's source-fit concern is confirmed.

A direct WHO definition candidate is *Basic Epidemiology*, second edition, Chapter 1, Box 1.2, “Definition of epidemiology.” The box explains “study,” “distribution,” “determinants,” health-related states/events and specified populations. The WHO IRIS PDF is available at:

https://iris.who.int/bitstream/handle/10665/43541/9241547073_eng.pdf

A WHO-hosted glossary also gives the definition: epidemiology is the study of distribution and determinants of health-states or events in specified populations, and the application of this study to control health problems:

https://www.afro.who.int/sites/default/files/2017-06/9789241507981_eng.pdf

### Disposition

**CONFIRMED SOURCE-IDENTITY/SCOPE DEFECT.** The current WHO news Source must not be treated as a definition source. A separately authorized, versioned Source/EU correction should link a direct WHO epidemiology definition and identify the exact chapter/box or glossary entry. Preserve the current Source and historical chain.

## 6. Evidence and authorization boundary

The official pages above were directly inspected on 2026-11-21. These findings are source-fit adjudications, not accepted current assessments.

- No canonical Claim, EU, Source, Assessment, Relation or risk record changed.
- No historical D/E/B score was accepted or transferred.
- No current D/E/B score was assigned.
- No HOLD was cleared.
- No rights, jurisdictional, specialist, independent Human View or release gate was passed.
- Any canonical Source/EU change requires the project's bounded authorization, versioning, regression and exact-head CI process.

## 7. Updated priority queue

1. **Immediate source-chain correction candidate:** Batch 42 row 018 (CPSC generator refuelling) and row 030 (CPSC flashlight preference).
2. **High-consequence source-chain correction candidate:** Batch 43 row 081 (FDA freezer 0°F target).
3. **Definition-source correction candidate:** Batch 42 row 068 (WHO epidemiology).
4. **Report reconciliation, not canonical correction:** Batch 43 row 012 WHO URI transcription discrepancy; current Source history and URI are internally consistent, but EU locator remains open.

