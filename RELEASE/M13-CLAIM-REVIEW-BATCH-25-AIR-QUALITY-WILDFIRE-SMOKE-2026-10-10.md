# M13 Claim Review Batch 25 — Air Quality and Wildfire Smoke
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **7 additional Claims reviewed. This is a bounded review batch, not domain closure or corpus completion.**

## Method
Reviewed three Claims in `air-quality-basics` and four in `wildfire-smoke-safety`, including the actual linked Evidence Use and source records. D (explanatory depth), E (claim-specific evidence fit) and B (boundary discipline) are scored independently from 0–3. High-consequence health/smoke recommendations receive a conservative desk-review standard; this is not medical advice or a safety certification.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-AIR_QUALITY_BASICS-A` | 2 | 1 | 2 | Measuring pollutant concentrations at monitoring stations is a sound description of ambient-air monitoring. The linked EPA Evidence Use text is generic and does not identify the relevant AirData material. WHO corroboration is explicitly limited to health-based guideline levels and does not independently prove the mechanics of EPA monitoring. Improve claim-specific support and keep the U.S. EPA context explicit. |
| `CLM-AIR_QUALITY_BASICS-B` | 2 | 2 | 2 | The six listed pollutants match the U.S. EPA criteria-pollutant framework, but the Evidence Use record only points generally to EPA AirData. Cite the exact EPA criteria-pollutant material and avoid implying that these are the only pollutants relevant to every air-quality assessment or every jurisdiction. |
| `CLM-AIR_QUALITY_BASICS-C` | 2 | 1 | 2 | AQI as a daily public communication index is a reasonable introductory statement. The linked EPA description is generic and does not show the AQI-specific support; WHO health guideline material is not an AQI definition. Add direct EPA AQI documentation and preserve the U.S.-specific scope. |
| `CLM-WILDFIRE-AIR-QUALITY` | 2 | 3 | 3 | Monitoring local air-quality reports and following outdoor-activity guidance during wildfire smoke is directly supported by the CDC Evidence Use. It appropriately defers to local conditions and public-health instructions rather than supplying one universal exposure threshold. |
| `CLM-WILDFIRE-CLEAN-AIR-ROOM` | 3 | 3 | 2 | Closing a room off from outdoor air and using an appropriate portable cleaner/filter is supported by CDC guidance. The statement should be interpreted as reducing indoor particle exposure, not creating a perfectly sealed or universally safe space; practical ventilation, heat, indoor sources and device instructions remain relevant. |
| `CLM-WILDFIRE-FILTER-LIMIT` | 3 | 2 | 3 | Room-size matching and avoiding ozone-producing air cleaners are important limitations; EPA is the appropriate source for clean-room and filtration advice. The Evidence Use description is still broad rather than naming the precise device-sizing and ozone statements. The DIY-device clause is appropriately framed as temporary, but should retain the EPA design caveats and must not imply all improvised designs are effective or safe. |
| `CLM-WILDFIRE-SMOKE-EMERGENCY` | 3 | 3 | 3 | Serious symptoms such as breathing difficulty, chest pain or confusion warrant urgent medical evaluation, and people with heart/lung conditions may be at elevated risk. CDC Evidence Use is specific to severe symptoms and vulnerable groups. Keep this as escalation guidance, not a diagnosis or a substitute for local emergency services. |

## Findings
1. **Air-quality evidence-description debt:** EPA Evidence Use descriptions for all three foundational claims are generic. The WHO entry provides a useful independent source for health-based guideline levels, but correctly disclaims support for an EPA AQI definition.
2. **Scope distinction matters:** criteria pollutants, routine monitoring, health-based guideline levels and the AQI are related but distinct concepts. Evidence and wording should not collapse them into one interchangeable measure.
3. **Wildfire-smoke guidance is more claim-specific:** CDC/EPA Evidence Use records identify the supported action or limitation. The remaining improvement is to make the portable-cleaner claim's sizing/ozone support more explicit.
4. **Safety boundary:** cleaner/filter use can reduce exposure but does not guarantee safe air under every condition. Emergency symptom guidance should remain prominent and not be weakened by general educational framing.
5. No content Records were changed. These seven Claims remain within the frozen 1,494-Claim denominator. This batch does not close air quality, wildfire smoke, high-consequence review, or M13.

## Records inspected
- `CONTENT/vertical-slices/air-quality-basics/records/CLM-AIR_QUALITY_BASICS-A.json`
- `CONTENT/vertical-slices/air-quality-basics/records/CLM-AIR_QUALITY_BASICS-B.json`
- `CONTENT/vertical-slices/air-quality-basics/records/CLM-AIR_QUALITY_BASICS-C.json`
- `CONTENT/vertical-slices/air-quality-basics/records/EU-AIR_QUALITY_BASICS-A.json`
- `CONTENT/vertical-slices/air-quality-basics/records/EU-AIR_QUALITY_BASICS-B.json`
- `CONTENT/vertical-slices/air-quality-basics/records/EU-AIR_QUALITY_BASICS-C.json`
- `CONTENT/vertical-slices/air-quality-basics/records/EU-AIR-QUALITY-WHO-CORROBORATION.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/CLM-WILDFIRE-AIR-QUALITY.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/CLM-WILDFIRE-CLEAN-AIR-ROOM.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/CLM-WILDFIRE-FILTER-LIMIT.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/CLM-WILDFIRE-SMOKE-EMERGENCY.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/EU-WILDFIRE-AIR-QUALITY.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/EU-WILDFIRE-CLEAN-AIR-ROOM.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/EU-WILDFIRE-FILTER-LIMIT.json`
- `CONTENT/vertical-slices/wildfire-smoke-safety/records/EU-WILDFIRE-SMOKE-EMERGENCY.json`

## Sources
- U.S. EPA, AirData Basic Information: https://www.epa.gov/outdoor-air-quality-data/airdata-basic-information
- WHO, Global Air Quality Guidelines: https://www.who.int/publications/b/59593
- CDC, Safety Guidelines: Wildfires and Wildfire Smoke: https://www.cdc.gov/wildfires/safety/how-to-safely-stay-safe-during-a-wildfire.html
- U.S. EPA, Create a Clean Room to Protect Indoor Air Quality During a Wildfire: https://www.epa.gov/emergencies-iaq/create-clean-room-protect-indoor-air-quality-during-wildfire

## Acceptance status
Seven additional Claim rows have explicit D/E/B scores and rationales. Follow-up actions: make EPA evidence for monitoring/AQI/criteria-pollutant claims specific and strengthen the evidence description for cleaner sizing and ozone limitations. Full 1,494-Claim scoring, high-consequence recall, Human View, Relation endpoint review, independent scoring review, authorized corrections with regression tests, and final same-HEAD 3/3 CI remain open.
