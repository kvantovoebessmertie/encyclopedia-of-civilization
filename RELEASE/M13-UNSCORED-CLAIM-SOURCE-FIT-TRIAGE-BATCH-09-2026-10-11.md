# M13 Unscored Claim Source-Fit Triage — Batch 09

Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: exactly 30 Claims: inventory rows 414–425, 430–442, and 446–450.
Mode: source-fit / record-classification triage only; no D/E/B scores.

## Coverage and limits

- Opened the 30 Claim records and corresponding primary Evidence Use records; checked Source metadata for the reviewed slices.
- Primary Claim/EU/Source pointers generally resolve, but some IDs use separator-only filename/internal-ID variants and some EU provenance fields are questionable. Structural resolution is not proof of proposition-level support.
- Assigned **0 D/E/B scores** and made **0 canonical Claim, Evidence Use, Source, or Relation JSON edits**.
- These 30 remain in the frozen 1,494-Claim denominator; 1,242 Claims remain without scored rows.
- Emergency preparedness and safety Claims are high-consequence: this pass is not a substitute for direct source verification or a qualified safety review.

## Claim-level triage

| Inventory row | Claim(s) | Source-fit / classification finding | Follow-up |
|---:|---|---|---|
| 414 | `CLM-EMBEDDED_SYSTEMS_BASICS-C` | Claim states that embedded-device security spans the full lifecycle. The Source is NIST IoT Cybersecurity, a plausible partial domain reference but not by itself proof of a full lifecycle model; EU is generic. | Locate the actual lifecycle guidance and verify whether it covers the complete product/device lifecycle, including support and retirement where applicable. |
| 415 | `CLM-ALERTS-ENABLE-RESPOND` | American Red Cross emergency-preparedness page is relevant broadly, but is not a pinpoint alert-settings reference. EU names advice about enabling alerts and understanding response, with no exact section/paragraph. | Verify the advice against a specific Red Cross/official alert guidance section and keep device/platform/jurisdiction limits clear. |
| 416–417 | `CLM-IPAWS-ALERT-CONTENT`, `CLM-IPAWS-ALERT-ELEMENTS` | FEMA IPAWS best-practices PDF is a specifically relevant alerting source. EUs are generic summaries (“information function” / “main elements”) and do not record page, item, or section. The Claims concern message completeness and elements such as source, event, location and time applicability. | Add exact PDF page/section/item locators and check the complete list and wording against the source. Keep the claims framed as guidance rather than universal legal requirements unless the source establishes that. |
| 418 | `CLM-HANDWASH-20SEC` | CDC’s emergency personal-hygiene page is directly relevant, and the EU explicitly names the 20-second recommendation. The Claim’s type is `descriptive`, although the statement is a recommendation; the content is safety guidance and needs a consistent type/governance decision. | Verify the current CDC wording and applicability; adjudicate Claim type so the record is not misleadingly classified as a descriptive fact. |
| 419–421 | `CLM-LIGHTING-CANDLE-CHILDREN`, `CLM-LIGHTING-CANDLE-UNATTENDED`, `CLM-LIGHTING-EXTINGUISH` | U.S. Fire Administration Candle Safety is directly relevant. EU for children and unattended candles is generic; the extinguishing EU is more specific but has no pinpoint locator. These are concrete fire-safety recommendations. | Add exact source sections for each recommendation; preserve precise conditions (room/home, drowsiness, sleep) and route through high-consequence safety review. |
| 422 | `CLM-LIGHTING-FLASHLIGHT-OUTAGE` | NFPA Candle Safety is a relevant safety source and the EU explicitly mentions flashlights/battery lighting instead of candles. No pinpoint section is recorded; the claim is a practical safety recommendation. | Add the exact NFPA passage and verify whether the recommendation is stated for outage contexts as broadly as the Claim implies. |
| 423–425 | `CLM-EMERGENCY_MANAGEMENT_BASICS-A/B/C` | The Source identity is a descriptive Russian phrase (“Emergency management: FEMA”) and its URI points to an IS-230.e course-overview page, not an identifiable specific passage or full course content. All three EUs are generic. A/B state the cycle/coordination concepts; C is a jurisdictional/context caveat. | Correct the source identity/locator through an authorized correction plan. Identify exact FEMA doctrine/course material for each proposition; retain jurisdictional limits and review C’s methodological nature. |
| 430 | `CLM-WATER-STORAGE-CONTAINER` | CDC “How to Create an Emergency Water Supply” is directly relevant; the EU names food-grade containers and avoiding toxic transfer. No pinpoint locator is stored. This is safety/health-adjacent advice. | Verify the exact current CDC text and applicable container wording, add a direct section locator, and keep the recommendation within CDC’s scope. |
| 431–433 | `CLM-ENERGY_BASICS-A/B/C` | OpenStax Physics “work, energy and energy resources” is a plausible subject source. EUs use the same generic title-level description for kinetic energy, potential energy and work; no section/equation locators are provided. | Add separate section/equation locators for each concept and verify terminology, variables and scope individually. |
| 434–436 | `CLM-ENERGY_EFFICIENCY_BASICS-A/B/C` | IEA Energy Efficiency is a relevant topical source, but all EUs point broadly to the topic page. C is a methodological measurement rule about service, period and units; B’s list of influences needs specific support. | Locate the IEA definition and the relevant methodology/data material; classify C consistently with other measurement-method Claims. |
| 437–439 | `CLM-ENERGY_MARKETS_BASICS-A/B/C` | U.S. EIA Energy Markets is relevant, but broad and U.S.-centred; EUs are generic. C makes a system-level distinction across energy carriers and physical delivery constraints. All three EUs use `provenance.method = source_based_claim_representation` and list the Claim ID in `provenance.created_from`, which is an anomaly for an evidence-link record and should be checked against the provenance contract. | Add claim-specific EIA locators and make any geographic scope explicit. Review EU provenance construction in the authorized correction pass; do not silently rewrite it during triage. |
| 440–442 | `CLM-ENERGY_POLICY_BASICS-A/B/C` | IEA Energy Policy is a relevant but broad topic page. EUs are generic. A/B are broad descriptions of policy goals; C is a context/transferability caution. The EUs repeat the same provenance anomaly seen in Energy Markets: method `source_based_claim_representation` and Claim ID in `created_from`. | Add specific IEA sections or policy documents for A/B; review C as a methodological/context statement. Check EU provenance against the authoring contract in a controlled correction pass. |
| 446–448 | `CLM-ENERGY_STORAGE_BASICS-A/B/C` | DOE’s Solar Integration / Energy and Storage Basics page is plausible for storage in a solar-grid context, but is too narrow by identity/URI to support claims about all storage technologies without qualification. EUs are generic. A describes storage generally, B distinguishes energy capacity and output power, C compares technology characteristics. | Either narrow the claims to the DOE page’s scope or add broader technical sources and exact locators for capacity vs. power, losses, constraints and use cases. |
| 449–450 | `CLM-ENERGY_SYSTEMS_BASICS-A/B` | IEA Energy System is a plausible high-level source and EUs are more informative than the generic pattern. However, filename IDs use hyphens while internal record IDs and references use underscores (`CLM_ENERGY_SYSTEMS_BASICS_A/B`, `EU_ENERGY_SYSTEMS_BASICS_A/B`, `SRC_ENERGY_SYSTEMS_BASICS`). This is a separator-only alias group that must remain visible in identity reconciliation, not silently normalized. Exact page/section locators are still absent. | Preserve literal IDs, document the alias explicitly, and verify the relevant IEA section. Do not rename IDs as part of source-fit triage. |

## Cross-cutting findings

1. **High-consequence emergency/safety claims:** emergency alert content, hand hygiene, candle safety and emergency water storage require exact current authoritative passages; title-level references are not sufficient for release.
2. **Source identity/locator defects:** Emergency Management uses a descriptive identity and a course-overview URI; Energy Storage uses a solar-integration/storage page for broader claims about storage technologies; Embedded Systems’ IoT cybersecurity source may support only a subset of lifecycle claims.
3. **Evidence-use quality:** multiple EUs are generic or title-level. Emergency Water Storage and several candle/alert EUs describe support more clearly but still lack exact locators.
4. **Potential type/governance issue:** handwashing is a recommendation but is tagged `descriptive`; Energy Efficiency C is a measurement rule; Emergency Management C is a context/transferability rule. Adjudicate these consistently across the corpus.
5. **EU provenance anomaly:** Energy Markets and Energy Policy EUs cite their own Claim as `created_from` while using `source_based_claim_representation`. Verify against the authoring/provenance contract and fix only in a reviewable correction pass.
6. **ID reconciliation:** Energy Systems has three separator-only filename/internal-ID aliases across Claim/EU/Source records. This is a comparison-only normalization issue, not permission to rewrite record identities.

## Disposition

- Claims reviewed: **30**.
- D/E/B scores: **0**.
- Canonical content JSON changes: **0**.
- Claims without scored rows: **1,242** (unchanged).
- This batch is source-fit triage only. Corrections require an authorized, reviewable plan and regression checks.
