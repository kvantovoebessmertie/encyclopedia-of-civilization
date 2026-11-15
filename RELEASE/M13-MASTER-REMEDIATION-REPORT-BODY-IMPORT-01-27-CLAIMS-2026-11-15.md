# M13 master remediation pass — exact report-body import 01

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Baseline: `967da40d66650b1d535744ac676be28519ebc57c`  
Type: noncanonical remediation ledger enrichment; no canonical writes.

## 1. Purpose and boundary

This report records findings extracted from the bodies of existing thematic source-passage reports and reconciles them to the 359-row residual Generic Evidence Use ledger by exact Claim ID and exact canonical EU path.

Only reports whose bodies were opened and inspected in this pass are treated as imported. Other filenames appearing in the CSV are not treated as evidence of completed review.

The exact canonical EU JSON files for all 27 rows were fetched at the baseline HEAD. Each is record version 1 and its `content.claim_ref` and `content.source_ref` point to Claim version 1 and Source version 1 respectively. This verifies the references recorded by each EU file; it does not by itself constitute a separate full content audit of every Claim and Source JSON.

## 2. Import result

| Finding | Rows |
|---|---:|
| Exact report-body imports | 27 |
| DIRECT at the bounded scope described in the report | 20 |
| PARTIAL / additional evidence or scope gap | 7 |
| Canonical EU versions verified | 27/27, all v1 |
| Claim/Source versions referenced by those EUs | 27/27, all v1 |
| Canonical records modified | 0 |
| D/E/B changes | 0 |
| New Sources/Evidence Uses created | 0 |
| Canonical write authorization | 0 |
| Claims accepted or release-cleared | 0 |

**All 27 Claims remain HOLD.** DIRECT here means a source passage was located at the stated scope; it does not mean that the current generic EU description has been repaired, that the record is publishable, or that rights, independence, specialist review or Human View gates have passed.

## 3. Exact row-level findings

### Agriculture basics

Primary report: `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-AGRICULTURE-AGRIFOOD-SYSTEMS-2026-11-12.md`

| Claim / EU | Finding | Imported passage / limitation |
|---|---|---|
| `CLM-AGRICULTURE_BASICS-A@1` / `EU-AGRICULTURE_BASICS-A@1` | PARTIAL | FAO constitutional definition and Strategic Framework ¶¶62,69 support crop/livestock core; associated-resource-management phrase not fully established. Existing FAO Agriculture URL was reported HTTP 404. |
| `CLM-AGRICULTURE_BASICS-B@1` / `EU-AGRICULTURE_BASICS-B@1` | DIRECT | FAO AEZ paragraphs 2–3, Agroecology Knowledge Hub paragraphs 1–2 and Agrifood Systems FAQ support interacting soil, water, biological, climate and management factors at a general systems level; not a universal quantitative causal model. |
| `CLM-AGRICULTURE_BASICS-C@1` / `EU-AGRICULTURE_BASICS-C@1` | DIRECT | FAO Agroecology Knowledge Hub paragraphs 3–4, Family Farming Knowledge Platform opening and AEZ paragraphs 2–3 support local-context dependence. Preserve the cautious wording; do not turn it into an absolute rule. |

### Water, energy and infrastructure systems

Primary report: `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-WATER-ENERGY-INFRASTRUCTURE-2026-11-12.md`

| Claim / EU | Finding | Imported passage / limitation |
|---|---|---|
| `CLM-ENERGY_SECURITY_BASICS-A@1` / `EU-ENERGY_SECURITY_BASICS-A@1` | DIRECT | IEA Energy Security heading and opening overview support reliable, affordable access and avoiding/mitigating/managing disruptions. |
| `CLM-ENERGY_SECURITY_BASICS-B@1` / `EU-ENERGY_SECURITY_BASICS-B@1` | DIRECT | IEA opening overview identifies geopolitical risks, cyberattacks, supply-chain disruptions and extreme weather. |
| `CLM-ENERGY_SECURITY_BASICS-C@1` / `EU-ENERGY_SECURITY_BASICS-C@1` | PARTIAL | IEA topic page is too broad for the assessment dimensions; IEA ASEAN Energy Security Review provides a framework across fuels, technologies, systems, regions and time horizon. Requires a distinct Source/EU and must not turn the five-year example into a universal requirement. |
| `CLM-HYDROPOWER_BASICS-B@1` / `EU-HYDROPOWER_BASICS-B@1` | DIRECT | DOE Types of Hydropower Plants, Overview/Impoundment/Diversion supports the descriptive typology; no inference on safety, site suitability or engineering design. |
| `CLM-HYDROPOWER_BASICS-C@1` / `EU-HYDROPOWER_BASICS-C@1` | DIRECT | DOE Types of Hydropower Plants, Pumped Storage subsection describes pumping to an upper reservoir and release through a turbine during high demand; descriptive operation only. |
| `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-A@1` / `EU-WATER_RESOURCES_MANAGEMENT_BASICS-A@1` | PARTIAL | USGS supports quantity, quality and availability; it does not fully establish distribution and variability as a complete management framework. |
| `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-B@1` / `EU-WATER_RESOURCES_MANAGEMENT_BASICS-B@1` | DIRECT | USGS Water Resources Mission Area opening and Water Data for the Nation support monitoring/assessment of streamflow and groundwater. |
| `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-C@1` / `EU-WATER_RESOURCES_MANAGEMENT_BASICS-C@1` | PARTIAL | Current USGS page does not directly establish a decision framework involving user needs, infrastructure and applicable rules; jurisdiction- and basin-specific policy evidence is needed. |
| `CLM-WATER_SECURITY-A@1` / `EU-WATER_SECURITY-A@1` | DIRECT | UN-Water Analytical Brief §1 working definition: sustainable access to adequate quantities of acceptable-quality water. Not a binding legal or technical water-safety standard. |
| `CLM-WATER_SECURITY-C@1` / `EU-WATER_SECURITY-C@1` | DIRECT | UN-Water Analytical Brief §1 definition/explanation connects water cycle, livelihoods, well-being, development, pollution/disasters, ecosystems and stability. Preserve its status as an analytical brief. |
| `CLM-WASTE_INFRASTRUCTURE_BASICS-B@1` / `EU-WASTE_INFRASTRUCTURE_BASICS-B@1` | PARTIAL | EPA waste hierarchy and SMM tools support non-universal approaches and measurement; local capacity, technology, workforce and regulatory constraints are not fully established. |
| `CLM-WASTE_INFRASTRUCTURE_BASICS-C@1` / `EU-WASTE_INFRASTRUCTURE_BASICS-C@1` | PARTIAL | EPA SMM Basics/Tools support life-cycle, environmental and economic considerations; local system, permits and technical feasibility need additional evidence. |
| `CLM-INFRASTRUCTURE_GOVERNANCE_BASICS-A@1` / `EU-INFRASTRUCTURE_GOVERNANCE_BASICS-A@1` | DIRECT | OECD Infrastructure Governance Key messages: institutional frameworks, coordination, evidence-based decisions, regulation and stakeholder participation. Policy framework, not national law. |
| `CLM-INFRASTRUCTURE_GOVERNANCE_BASICS-B@1` / `EU-INFRASTRUCTURE_GOVERNANCE_BASICS-B@1` | DIRECT | OECD long-term strategic planning and project selection/prioritisation support alignment of goals, funding and implementation. |
| `CLM-INFRASTRUCTURE_GOVERNANCE_BASICS-C@1` / `EU-INFRASTRUCTURE_GOVERNANCE_BASICS-C@1` | DIRECT | OECD Infrastructure Governance Indicators life-cycle perspective/Figure 4.2 covers planning, appraisal, budgeting, procurement, asset management and evaluation. |

### Measurement uncertainty

Primary report: `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-MEASUREMENT-UNCERTAINTY-BASICS-2026-11-12.md`

| Claim / EU | Finding | Imported passage / limitation |
|---|---|---|
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1` / `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | DIRECT | NIST TN 1297 §2.1: measurement result is an estimate and is complete with a quantitative uncertainty statement. Do not generalize beyond scope. |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B@1` / `EU-MEASUREMENT_UNCERTAINTY_BASICS-B@1` | DIRECT | NIST TN 1297 §2.3; VIM 2.16 (error) and 2.26 (uncertainty) distinguish error and uncertainty. Claim wording should be checked against current VIM definition. |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-C@1` / `EU-MEASUREMENT_UNCERTAINTY_BASICS-C@1` | DIRECT | VIM 2.3 (measurand) and 2.48 (measurement model); NIST TN 1297 Appendix A.1–A.2 on measurement function and uncertainty contributions. Distinct VIM Source identity may be required. |

### Statistical inference

Primary report: `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-STATISTICS-INFERENCE-BASICS-2026-11-12.md`

| Claim / EU | Finding | Imported passage / limitation |
|---|---|---|
| `CLM-STATISTICS_INFERENCE_BASICS-A@1` / `EU-STATISTICS_INFERENCE_BASICS-A@1` | DIRECT | NIST e-Handbook §§1.3.5 and 7.1.4 support sample-to-population estimation and confidence intervals. |
| `CLM-STATISTICS_INFERENCE_BASICS-B@1` / `EU-STATISTICS_INFERENCE_BASICS-B@1` | DIRECT | NIST §§7.1.2 and 1.3.6 support method-specific assumptions and checking distributional conditions. Assumptions must not be presented as universal. |
| `CLM-STATISTICS_INFERENCE_BASICS-C@1` / `EU-STATISTICS_INFERENCE_BASICS-C@1` | DIRECT | NIST §§1.3.5, 1.3.5.2, 7.1.5 and 7.1.3 support estimation uncertainty and hypothesis-test interpretation; preserve the distinction from practical significance. |

## 4. Current canonical crosswalk

All 27 exact EU JSON paths were fetched from HEAD `967da40d66650b1d535744ac676be28519ebc57c`.

- EU record version: 1 for all 27.
- Each EU's `claim_ref`: exact Claim ID at version 1.
- Each EU's `source_ref`: exact Source ID at version 1.
- Current EU material descriptions remain generic; no exact locators have been written.
- No Claim/EU/Source JSON was changed by this import.

The updated CSV adds report-body finding, bounded support disposition, report reference, next action, verified EU version and authorization state for these 27 rows. The other 332 rows remain unimported in this pass.

## 5. Required next actions

1. Prepare grouped, noncanonical correction proposals for the 20 DIRECT rows: exact locators, any new Source/EU identities, source title/edition/URI, rights and scope notes.
2. Prepare evidence-gap proposals for the 7 PARTIAL rows; do not label them as direct support.
3. Check current canonical Source records and slice README/manifest policies before drafting any Source additions.
4. Verify rights/permissions for each proposed source; in particular do not assume open access means unrestricted reuse or automated ingestion rights.
5. Obtain bounded authorization before any canonical Claim/EU/Source write. No blanket authorization is created by this report.
6. Run local schema/reference/regression checks after an authorized group; defer full CI until the consolidated remediation batch is ready.
7. Keep all Claims HOLD until the relevant independent/specialist review, Human View and release gates are complete.

## 6. Acceptance status

This is a report-body import and exact-reference crosswalk, not canonical remediation completion.

- 27/359 rows imported from report bodies.
- 332/359 rows remain for report-body import/reconciliation.
- 20 DIRECT / 7 PARTIAL at the bounded desk-review level.
- 0 canonical edits; 0 new records; 0 score changes.
- M13 remains OPEN / NOT RELEASE-READY.
- PR #21 remains Draft/unmerged; `main` unchanged.
