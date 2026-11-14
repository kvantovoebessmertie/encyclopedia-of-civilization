# M13 Unscored Claim Source-Fit Triage — Batch 07

Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: inventory rows 345–374, exactly 30 Claims.
Mode: source-fit / record-classification triage only; no D/E/B scores.

## Coverage and limits

- Opened all 30 Claim records and their primary Evidence Use records.
- Checked the referenced Source metadata for the covered groups.
- Confirmed primary Evidence Use records generally resolve to the expected Claim/Source IDs and use `supports`; this is structural linkage, not proof of passage-level support.
- Assigned **0 D/E/B scores** and made **0 canonical Claim, Evidence Use, Source, or Relation JSON edits**.
- All 30 remain within the frozen 1,494-Claim denominator and remain unscored. The inventory count of 1,242 Claims without a scored row is unchanged.
- This pass does not verify every cited source passage against the full proposition and does not establish independent corroboration.

## Claim-level triage

| Inventory row | Claim(s) | Source-fit / classification finding | Follow-up |
|---:|---|---|---|
| 345 | `CLM-DISASTER_RISK_REDUCTION_BASICS-D` | FEMA hazard-mitigation planning source is topically relevant. EU says FEMA “independently supports” the boundary, but the inspected primary record does not itself establish independence from other evidence. No pinpoint locator is recorded. | Keep in high-consequence disaster-management review; verify the exact FEMA passage and independence wording. |
| 346–348 | `CLM-DISTRIBUTED_SYSTEMS_BASICS-A/B/C` | Source identity is a descriptive Russian sentence rather than a stable publication/title; URI points only to the NIST ITL landing page. All three EUs use the same generic “within the indicated material” wording, with no passage locator. | High-priority Source identity/locator defect and weak traceability. Identify the actual source or replace it under an authorized correction plan; then check each Claim separately. |
| 349–351 | `CLM-EARLY_AGRICULTURE-A/B/C` | FAO AGRIS / ICARDA Harlan Symposium record is a concrete, plausible subject source. EUs A–C repeat the same generic description and do not identify the supporting section or passage. Claim C makes a geographically and chronologically specific crop-domestication statement that needs a specific locator. | Keep unscored until exact support is located, especially for the specific crop/geography statement. |
| 352–354 | `CLM-EARTH_SYSTEM_BASICS-A/B/C` | NASA Earth-science landing page is relevant to the topic but broad. EUs repeat generic wording and provide no exact section or passage. The broad concepts are plausible, but topic relevance alone is not claim-specific evidence. | Add claim-specific section/page locators and verify the wording against the actual NASA material. |
| 355–356 | `CLM-AFTERSHOCK-DAMAGE`, `CLM-AFTERSHOCK-EXPECT` | USGS “Aftershock Forecasts” is relevant to the possibility/forecasting of aftershocks. It does not, by title or landing-page URI alone, establish the additional statement that damaged buildings pose danger or that building safety requires a qualified professional. Both EUs use generic wording and omit pinpoint locators. | High-consequence safety review. Separate the aftershock-expectation proposition from structural-safety guidance and require direct authoritative support for each. Do not publish these as fully verified based only on the current pointer. |
| 357 | `CLM-EARTHQUAKE-DROP-COVER-HOLD` | FEMA/Ready.gov source is a named, relevant hazard-information PDF; EU identifies the protective action, but gives no page or section locator. Exact applicability and wording should be checked against the relevant page. | High-consequence safety review; confirm exact instruction and locator before pilot inclusion. |
| 358–360 | `CLM-ECOLOGY_BASICS-A/B/C` | OpenStax Biology 2e ecology introduction is a plausible ecology source. However, the Claims describe what a thematic slice does, how interpretation depends on source/context, and when specialist checking is needed; these read as editorial/methodological guidance rather than documented ecology facts. | Route all three through the cross-slice methodology/type-adjudication family; do not deduplicate or rewrite automatically. |
| 361–363 | `CLM-ECONOMETRICS_BASICS-A/B/C` | World Bank econometrics PDF is a concrete source, but the EUs identify only the title and provide no page/section locator. The three propositions concern distinct concepts (disciplinary scope, error term, hypothesis/model use) and need separate passage checks. | Add pinpoint locators and verify each statement independently; no blanket acceptance based on one PDF. |
| 364–366 | `CLM-ECONOMIC_GEOGRAPHY_BASICS-A/B/C` | World Development Report 2009 is a relevant thematic source, but the stored URI is a broad archive page rather than the report itself. EUs repeat the same title-level description without page/chapter locators. Claim C is a general methodological caution about context and universalization, not obviously a substantive fact of economic geography. | Fix locator under a controlled correction plan; review Claim C’s record type alongside the methodology-template family. |
| 367–369 | `CLM-ECONOMIC_HISTORY-A/B/C` | Our World in Data economic-growth material is plausibly relevant. EUs B/C contain more substantive caveats about measurement and welfare than many other slices, but no direct chart/series/methodology locators are provided; Claim A's broad “historical production and income estimates” also needs a defined measure and scope. | Preserve the stronger descriptions but add direct links/sections and check each proposition against the named measure and methodology. |
| 370–372 | `CLM-ECONOMICS_BASICS-A/B/C` | World Bank “understanding poverty” URI is broad for production/distribution/use of goods and services, scarcity, and limits of indicators. EUs repeat generic title-level language and do not establish passage fit. | Source-fit gap across all three; replace or supplement with claim-specific, accessible references under an authorized plan. |
| 373–374 | `CLM-ECOPHYSIOLOGY_BASICS-A/B` | Source identity is itself a descriptive sentence about ecophysiology, while the URI points to an OpenStax Biology 2e page on animal sensory systems and movement. This is a likely source identity/scope mismatch for general environmental dependence and physiological tolerance ranges. EUs are generic. | High-priority Source identity/URI scope defect. Identify a fit-for-purpose source and verify the exact propositions before scoring. |

## Cross-cutting findings

1. **Generic EUs remain pervasive.** Distributed systems, early agriculture, Earth system, ecology, econometrics, economic geography, economics, and ecophysiology primarily use generic/title-level descriptions without pinpoint support.
2. **Source identity/scope defects confirmed as triage findings:** `SRC-DISTRIBUTED_SYSTEMS_BASICS` uses a descriptive sentence as identity and a broad NIST ITL root URI; `SRC-ECOPHYSIOLOGY_BASICS` uses a descriptive sentence as identity and an OpenStax URI whose page title/topic is narrower than the claims.
3. **Possible record-type/template family:** all three Ecology Basics Claims are about the slice or evidence/review method rather than ecology subject matter. Economic Geography C is also a likely methodological/editorial caution. Adjudicate as families, not isolated deletions.
4. **High-consequence material:** aftershock/building safety, earthquake protective action, and disaster-risk-reduction planning need exact authoritative passages and human safety review.
5. A relevant publisher, reputable institution, or plausible source title is not sufficient evidence that the cited passage supports the complete statement.

## Disposition

- D/E/B scores: **0**.
- Canonical content JSON changes: **0**.
- Claims reviewed in this batch: **30**.
- Remaining unscored count: **1,242** (unchanged).
- The batch remains source-fit triage only. Any content/source correction requires an explicit, reviewable correction plan and regression checks.

