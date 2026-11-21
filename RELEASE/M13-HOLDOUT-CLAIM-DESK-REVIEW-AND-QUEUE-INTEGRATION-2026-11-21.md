# M13 — Holdout Claim Desk Review and Queue Integration Findings

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Inspection HEAD before this documentation commit: `0756764951c4238bf51fe2dc39481f790c281a88`  
Scope: two exact unresolved Package 32 holdout Claims; risk-queue interpretation; historical score-ledger reconciliation.  
Disposition: **desk-level evidence review only; no canonical edits, no risk metadata assignment, no D/E/B scoring, no release clearance**.

## 1. Executive result

Two previously unresolved Package 32 holdout Claims received a source-level desk review against their exact current Claim → Evidence Use → Source chains:

- `CLM-DISASTER_RISK_REDUCTION_BASICS-C@1`: UNDRR Sendai Framework material is substantively relevant to the proposition, but the registered Evidence Use lacks a reproducible claim-specific locator. Route: **MODERATE desk-review priority**; retain HOLD pending versioned locator remediation and independent/domain review.
- `CLM-HYDROPOWER_BASICS-C@1`: the broad registered DOE “Hydropower Basics” source is not the most precise registered source for pumped-storage hydropower. A dedicated DOE pumped-storage source directly supports the basic two-reservoir storage cycle and grid-storage role. Route: **ELEVATED specialist-review priority** before engineering, grid-planning or operational use; retain HOLD pending source-record/Evidence Use remediation and specialist review.

These routes are workflow priorities, not formal risk ratings. Historical D/E/B values remain historical only. The current Claim worksheet still has no accepted current D/E/B assessments.

## 2. Exact Claim review

### 2.1 Disaster risk reduction — Claim C

**Current Claim:**  
“Меры снижения риска зависят от конкретной опасности, территории, уязвимости, ресурсов и институционального контекста.”

**Canonical chain at inspection HEAD:**
- Claim: `CLM-DISASTER_RISK_REDUCTION_BASICS-C@1`
- Evidence Use: `EU-DISASTER_RISK_REDUCTION_BASICS-C@1`
- Source: `SRC-DISASTER_RISK_REDUCTION_BASICS@1`
- Registered source: UNDRR, “What is the Sendai Framework?”  
  https://www.undrr.org/implementing-sendai-framework/what-sendai-framework

**Passage-level finding.** UNDRR Priority 1 says disaster-risk management should be based on all dimensions of risk: vulnerability, capacity, exposure of people and assets, hazard characteristics and the environment. The same page identifies Priority 2 as strengthening disaster-risk governance and Priority 3 as investing in risk reduction for resilience. This directly supports the Claim’s general context-dependence, vulnerability and institutional-governance elements. It does not, without a more precise passage and careful terminology mapping, establish every listed phrase as a one-to-one factor. In particular, “territory” and “resources” should not be treated as exact substitutes for UNDRR’s “exposure,” “capacity” or “environment.”

**Recommended remediation:**
1. Retain the UNDRR source identity only if the canonical Source record resolves to this exact framework page.
2. Version the Evidence Use with an explicit locator to Priority 1 (“Understanding disaster risk”), and separately cite Priority 2 and Priority 3 only if the EU material relies on governance and investment/resilience.
3. Reconcile the Claim’s wording against the framework’s defined dimensions; consider naming exposure, capacity and environmental context explicitly if that better reflects the intended proposition.
4. Do not infer local hazard assessment, territorial suitability, resource sufficiency or operational measures from this introductory Claim.

**Disposition:** MODERATE desk-review route; current risk metadata remains UNASSESSED; no score assigned; HOLD remains.

### 2.2 Hydropower — Claim C

**Current Claim:**  
“Pumped-storage hydropower stores energy by moving water between reservoirs and can provide grid-scale energy-storage services.”

**Canonical chain at inspection HEAD:**
- Claim: `CLM-HYDROPOWER_BASICS-C@1`
- Evidence Use: `EU-HYDROPOWER_BASICS-C@1`
- Source: `SRC-HYDROPOWER_BASICS@1`
- Registered source: U.S. Department of Energy, “Hydropower Basics”  
  https://www.energy.gov/cmei/water/hydropower-basics

**Passage-level finding.** The registered general hydropower landing page is broader than the pumped-storage proposition and the current Evidence Use does not identify a reproducible pumped-storage passage. DOE has a dedicated “Pumped Storage Hydropower” page that defines pumped storage as two reservoirs at different elevations: water generates electricity as it moves down through a turbine, and electricity is used to pump water back to the upper reservoir. DOE describes the technology as energy storage and discusses its role in grid reliability and integration. DOE’s “How Pumped Storage Hydropower Works” page independently explains the same charge/discharge cycle and grid-reliability role.

**Recommended remediation:**
1. Add a dedicated, versioned Source record for DOE “Pumped Storage Hydropower” or another approved stable DOE page; do not silently repurpose the broad hydropower Source identity.
2. Version the Evidence Use with an exact locator to the “What is Pumped Storage Hydropower?” section; add the separate “How Pumped Storage Hydropower Works” page only if the second source is actually used and its corroborative role is described.
3. Limit the Claim’s evidentiary scope to the storage mechanism and general grid-storage service. Do not infer project feasibility, round-trip efficiency, capacity, dispatch performance, environmental acceptability, geotechnical suitability or safety requirements.
4. Require hydropower / power-systems specialist review before engineering, grid-planning or operational use.

**Disposition:** ELEVATED specialist-review route; current risk metadata remains UNASSESSED; no score assigned; HOLD remains.

## 3. Queue integration: do not mistake prior work for formal risk assessment

The current M13 automation run at inspection HEAD selects 100 Claims because the caller passes an empty verified-disposition set to `build_lanes`. The pipeline separately records prior report-ID mentions as retrieval leads. Its conservative rule is explicit: an ID mention alone does not prove that the exact Claim version received a completed review.

The Package 32 report documents a prior content-level routing pass of 41 Claims, with 7 elevated, 17 moderate and 17 low-direct-consequence routes. It explicitly records zero risk-metadata assignments, zero D/E/B scores, zero specialist adjudications, zero Human View approvals and zero release clearances. Package 32 therefore cannot be treated as formal risk assessment.

The new queue's 100 selected rows have historical score-ledger matches and prior report-body mentions, but those facts are not sufficient by themselves to exclude them. The correct next integration step is a curated, exact-version disposition ledger with report-body verification and explicit scope, not an automatic exclusion based on mentions.

Recommended distinct states for that ledger:
- `CONTENT_SCREENED`: exact Claim ID@version and report body verified; statement-level content/routing screen only.
- `SOURCE_PASSAGE_REVIEWED`: exact Claim/EU/Source versions and the inspected passage are verified in the report.
- `RISK_METADATA_PENDING`: content screen exists but formal risk metadata has not been assigned.
- `FORMAL_RISK_ASSESSED`: a separately authorized, documented risk assessment exists with reviewer and method.
- `HOLDOUT_UNRECONCILED`: a known holdout remains outside the active queue pending reconciliation.
- `NOT_YET_REVIEWED`: no qualifying exact-version review disposition is established.

Only dispositions that meet the exclusion policy should be passed to the queue as verified reviewed IDs. Do not use a broad “reviewed” boolean to conflate desk screening, source-passage review, formal risk assessment, specialist approval or release clearance.

## 4. Historical D/E/B ledger: preserve provenance and conflicts

The reproduced ledger contains 1,501 historical score rows for 1,494 current Claims, with seven repeated Claim-ID groups (14 rows) and no unmatched rows. These are historical report rows, not accepted current scores.

- Six repeated groups have at least one conflicting D/E/B dimension.
- One emergency-disinfection group is concordant and should count as one historical assessment with two report references, not as two independent confirmations.
- Do not select the later score by chronology and do not average conflicting scores.
- The 1,494-row current worksheet still has blank D/E/B and `NOT_YET_REVIEWED` for every Claim.
- The historical row-level E distribution is E=0: 11; E=1: 1,177; E=2: 217; E=3: 96. The 1,177 E=1 rows identify a major canonical locator/source-fit remediation workload; they do not prove that the underlying Claims are false or that no passage was consulted.

The separate historical duplicate adjudication plan remains the governing method for the six conflicts. This desk review does not resolve or overwrite any of them.

## 5. Source references checked

- UNDRR, “What is the Sendai Framework?” — Priority 1 (risk dimensions), Priority 2 (risk governance), Priority 3 (investment in disaster risk reduction):  
  https://www.undrr.org/implementing-sendai-framework/what-sendai-framework
- UNDRR, “Sendai Framework for Disaster Risk Reduction 2015–2030” — paragraphs 23–24 and the four priorities:  
  https://www.undrr.org/media/16176/download
- U.S. Department of Energy, “Pumped Storage Hydropower” — definition, two-reservoir configuration, discharge/recharge cycle and grid role:  
  https://www.energy.gov/cmei/water/pumped-storage-hydropower
- U.S. Department of Energy, “How Pumped Storage Hydropower Works” — charge/discharge sequence and grid-reliability context:  
  https://www.energy.gov/cmei/water/how-pumped-storage-hydropower-works

## 6. Change boundary and remaining gates

This report is a noncanonical audit note. It does not modify Claim, Evidence Use, Source, Context, Scope, Relation, Decision, Assessment or risk metadata records. It creates no new D/E/B scores and does not accept historical scores into the current worksheet.

Still required:
1. Versioned canonical locator/source remediation for the two Claims, under their own bounded editorial authorization.
2. Specialist review for the hydropower Claim and appropriate domain review for the disaster-risk Claim.
3. Exact-version, report-body-verified disposition ledger before queue exclusions are automated.
4. Exact-version reconciliation of historical rows, all seven duplicate groups, the 594 versionless historical Claim cases and the 16 current Claim@2 cases.
5. Independent review, Human View, source independence, rights/editorial gates and exact-head CI.
6. Final exact-tree, PR and base/main verification.

No new scoring batch is authorized by this report. PR #21 remains Draft / open / unmerged; `main` is not modified. M13 remains **OPEN / NOT RELEASE-READY**.
