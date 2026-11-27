# P4/P5 Disaster, Water Quality and Electrical Grid — Bounded Pinpoint Remediation Authorization Proposal

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `d0b820f0d90ef9bb04a5228153b7ec5b3ef169d5`  
Status: **PROPOSED ONLY — NO AUTHORIZATION RECORDED; NO CANONICAL JSON CHANGED; ALL FOUR SLICES REMAIN HOLD**

## 1. Purpose

This proposal converts the supplemental P4/P5 pinpoint review into an exact, bounded implementation scope. It does not reopen or replace the substantive P4/P5 audits. It addresses current-head source identity, claim-specific Evidence Use locators, support boundaries and two claim-wording defects.

The root `authorized_slices` list in `RELEASE/EDITORIAL-CORRECTION.json` names these slices, but no separate record-level bounded authorization for the changes below was found. Therefore **none of the proposed canonical edits may be applied until this exact proposal is explicitly approved and entered into the authorization manifest**.

## 2. Frozen inspection and record topology

Inspection baseline: `d0b820f0d90ef9bb04a5228153b7ec5b3ef169d5`.

| Slice | Existing topology | Existing records to be versioned in proposal | New record dependencies |
|---|---:|---:|---:|
| disaster-response-logistics-basics | 13 records: 3 Claims, 6 EUs, 2 Sources, Context, Scope | 12 | 0 mandatory; optional 1 new Source + 1 EU for FEMA Distribution Management Plan Guide |
| disaster-recovery-basics | 12 records: 4 Claims, 4 EUs, 2 Sources, Context, Scope | 10 | 0 |
| water-quality-basics | 12 records: 4 Claims, 4 EUs, 2 Sources, Context, Scope | 10 | 0 |
| electrical-grid-basics | 12 records: 4 Claims, 4 EUs, 2 Sources, Context, Scope | 4 | 0 |
| **Total** | **49 existing records** | **36 exact versioned records** | **Optional +2 after canonical ID allocation** |

Every record listed below was re-fetched from the branch and exact ID/version/type checked. The existing P4/P5 audit denominators remain unchanged. The candidate denominator remains 1,058 and the exact-version master remains 1,129 rows.

## 3. Exact record-level proposed changes

### 3.1 Disaster Response Logistics Basics

Current exact records:
- Claims: `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A/B/C@1`
- Primary EUs: `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A/B/C@1`
- FEMA EUs: `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A_FEMA@1`, `EU-DISASTER_RESPONSE_LOGISTICS_BASICS-B-FEMA@1`, `EU-DISASTER_RESPONSE_LOGISTICS_BASICS-C-FEMA@1`
- Sources: `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1`, `SRC-FEMA-DISASTER-LOGISTICS-2026@1`
- Context/Scope: `CTX-DISASTER_RESPONSE_LOGISTICS_BASICS@1`, `SCP_DISASTER_RESPONSE_LOGISTICS_BASICS@1`

**Proposed versioned records: 12**

| Exact record | Proposed version | Exact permitted change |
|---|---:|---|
| `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS` | v1→v2 | Replace generic OCHA homepage identity/URI with WFP-hosted Logistics Cluster, exact title and stable official URI; locator to mandate, Coordination and Information Management sections |
| `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A/B/C` | v1→v2 | Keep each Claim statement and claim_type unchanged; update provenance only to primary Source v2 |
| `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A/B/C` | v1→v2 | Add claim-specific WFP Logistics Cluster locators; update Source reference to v2 and Claim reference to current Claim v2; keep evidence_role= supports |
| `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A_FEMA` | v1→v2 | Add FEMA IS-52 course-overview/objective locator for disaster-logistics components and interdependencies; current Claim v2 and FEMA Source v1 |
| `EU-DISASTER_RESPONSE_LOGISTICS_BASICS-B-FEMA` | v1→v2 | Add FEMA IS-52 risk, interdependency, disruption, sourcing and rerouting locators; state that the page only partially supports the full constraint list |
| `EU-DISASTER_RESPONSE_LOGISTICS_BASICS-C-FEMA` | v1→v2 | Add FEMA IS-52 public-private collaboration, governance, technology and real-time situational-awareness locators |
| `CTX-DISASTER_RESPONSE_LOGISTICS_BASICS` | v1→v2 | Target Claim A v2; specify descriptive educational scope, need for incident-specific situational information, coordination and qualified operational command |
| `SCP_DISASTER_RESPONSE_LOGISTICS_BASICS` | v1→v2 | Target Claim A v2; explicitly exclude operational command, live allocation, transport routing, procurement and incident-specific instructions |

**Direct locators:**
- WFP Logistics Cluster: “The Logistics Cluster” → mandate; “Core Services At Country Level” → “Coordination” and “Information Management”. https://logcluster.org/en/who-we-are/cluster-approach/logistics-cluster
- FEMA IS-52: course overview and objectives, including logistics terminology, disaster-specific components/interdependencies, supply-chain risk/vulnerability, resilience, governance, public-private collaboration, technology, rapid sourcing, transportation rerouting and situational awareness. https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-52&lang=en

**Important support limit:** FEMA IS-52 does not itself enumerate all five constraints in Claim B. The FEMA *Distribution Management Plan Guide 2.0*, Chapter 4, directly addresses defining requirements, ordering resources, distribution methods, inventory, transport, staging, demobilization and matching resource quantities to storage/distribution capacity. If the owner requires direct independent support for every element of Claim B, authorize one additional Source and one additional Evidence Use record for that guide. Their canonical IDs must be allocated by the existing ID process; this proposal does not invent them. https://www.fema.gov/sites/default/files/documents/fema_distribution-management-plan-guide-2.0.pdf

### 3.2 Disaster Recovery Basics

Current exact records:
- Claims: `CLM-DISASTER_RECOVERY_BASICS-A/B/C/D@1`
- EUs: `EU-DISASTER_RECOVERY_BASICS-A/B/C/D@1`
- Sources: `SRC-DISASTER_RECOVERY_BASICS@1`, `SRC-UNDRR-RECOVERY-2026@1`
- Context/Scope: `CTX-DISASTER_RECOVERY_BASICS@1`, `SCP-DISASTER_RECOVERY_BASICS@1`

**Proposed versioned records: 10**

| Exact record | Proposed version | Exact permitted change |
|---|---:|---|
| `SRC-DISASTER_RECOVERY_BASICS` | v1→v2 | Correct identity/URI to FEMA *National Disaster Recovery Framework — Third Edition* (10 Dec 2024), not the IS-2900.a course-overview page; locator to §§2.1–2.3 and §3.3 |
| `CLM-DISASTER_RECOVERY_BASICS-A` | v1→v2 | Statement unchanged; provenance-only alignment to FEMA Source v2 |
| `CLM-DISASTER_RECOVERY_BASICS-B` | v1→v2 | Replace the misleading “separate phase” formulation with the approved statement below; provenance to FEMA Source v2 |
| `CLM-DISASTER_RECOVERY_BASICS-C` | v1→v2 | Statement unchanged; provenance-only alignment to FEMA Source v2 |
| `EU-DISASTER_RECOVERY_BASICS-A/B/C` | v1→v2 | Add claim-specific NDRF §2.1/§2.3/§3.3 locators; exact current Claim/Source references |
| `EU-DISASTER_RECOVERY_BASICS-D` | v1→v2 | Add exact UNDRR “Definition: Recovery” locator; keep UNDRR Source v1 |
| `CTX-DISASTER_RECOVERY_BASICS` | v1→v2 | Target Claim A v2; describe recovery as cyclical, locally contextualized and overlapping with response/mitigation/rebuilding |
| `SCP-DISASTER_RECOVERY_BASICS` | v1→v2 | Target Claim A v2; retain event/jurisdiction boundary and exclude site-specific recovery plans or emergency instructions |

**Proposed Claim B v2 wording (requires explicit editor approval):**

> FEMA's National Disaster Recovery Framework describes recovery as an interdependent process that begins during response and overlaps with rebuilding and mitigation; it organizes federal recovery support through defined coordination roles and functions.

**Direct locators:**
- FEMA NDRF Third Edition: §2.1, printed pp. 2–3 (cyclical/interdependent process and community context); §2.2, printed pp. 3–4 (recovery begins during response); §2.3, printed pp. 4–5 (community-driven locally executed strategy); §3.3, printed pp. 7–8 (Recovery Support Functions and coordination); §4.1, printed p. 18 (local-government responsibilities). https://www.fema.gov/sites/default/files/documents/fema_national-disaster-recovery-framework-third-edition_2024.pdf
- UNDRR, “Definition: Recovery”, complete entry in Sendai Framework Terminology. https://www.undrr.org/terminology/recovery

**Source correction rationale:** current FEMA Source v1 is titled “National Disaster Recovery Framework Overview” but links to a FEMA IS-2900.a course page. The actual NDRF publication is the Third Edition PDF. The NDRF explicitly states recovery is not a separate linear phase; it is cyclical and often overlaps with response and mitigation. Do not leave the existing Claim B unchanged and simply attach the new locator.

### 3.3 Water Quality Basics

Current exact records:
- Claims: `CLM_WATER_QUALITY_BASICS_A/B/C@1`, `CLM_WATER_QUALITY_WHO_A@1`
- EUs: `EU_WATER_QUALITY_BASICS_A@1`, `EU_WATER_QUALITY_BASICS-B@1`, `EU_WATER_QUALITY_BASICS-C@1`, `EU_WATER_QUALITY_WHO_A@1`
- Sources: `SRC_WATER_QUALITY_BASICS@1`, `SRC_WATER_QUALITY_WHO@1`
- Context/Scope: `CTX-WATER_QUALITY_BASICS@1`, `SCP-WATER_QUALITY_BASICS@1`

**Proposed versioned records: 10**

| Exact record | Proposed version | Exact permitted change |
|---|---:|---|
| `CLM_WATER_QUALITY_BASICS_A` | v1→v2 | Narrow “pollutants and other stressors” to the directly supported EPA pollutant-specific criteria scope |
| `CLM_WATER_QUALITY_BASICS_C` | v1→v2 | Make the U.S. Clean Water Act / EPA-approved state, territorial, authorized tribal and federal regulatory boundary explicit |
| `CLM_WATER_QUALITY_WHO_A` | v1→v2 | Statement unchanged; provenance-only alignment to WHO Source v2 |
| `SRC_WATER_QUALITY_WHO` | v1→v2 | Correct generic identity to exact WHO 2026 publication title and date; preserve official WHO publication URI |
| `EU_WATER_QUALITY_BASICS_A/B/C` | v1→v2 | Add EPA claim-specific locators and current Claim/Source references; retain EPA Source v1 |
| `EU_WATER_QUALITY_WHO_A` | v1→v2 | Pin WHO overview and 2026 edition's health-based targets, catchment-to-consumer Water Safety Plans and independent surveillance |
| `CTX-WATER_QUALITY_BASICS` | v1→v2 | Target Claim A v2; distinguish ambient/surface-water criteria from drinking-water quality guidance; state U.S. legal scope |
| `SCP-WATER_QUALITY_BASICS` | v1→v2 | Target Claim A v2; exclude global legal generalization, site-specific safety determination and operational treatment advice |

**Proposed Claim A v2 wording (requires editor approval):**

> Water-quality criteria are scientific benchmarks used to protect designated human-health or aquatic-life uses of surface waters from pollutants.

**Proposed Claim C v2 wording (requires editor approval):**

> In the U.S. Clean Water Act framework, water-quality standards are jurisdictional legal instruments that combine designated uses, criteria and antidegradation requirements.

**Direct locators:**
- EPA “Basic Information on Water Quality Criteria”: opening paragraph; “Aquatic Life Criteria”; “Human Health Criteria”. https://www.epa.gov/wqc/basic-information-water-quality-criteria
- EPA “What are Water Quality Standards?”: opening definition; “Core Components of WQS”; “Designated Uses”; “Criteria”; “Antidegradation Requirements”. https://www.epa.gov/wqs-tech/what-are-water-quality-standards
- WHO “Drinking-water quality guidelines”: current publication entry dated 17 June 2026 and overview on health-based targets, preventive risk management and independent surveillance. https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/water-safety-and-quality/drinking-water-quality-guidelines
- WHO exact 2026 publication record: *Guidelines for Drinking-water Quality: Fourth Edition Incorporating the First, Second and Third Addenda*. https://www.who.int/publications/i/item/9789240121225

### 3.4 Electrical Grid Basics

Current exact records:
- Claims: `CLM_ELECTRICAL_GRID_BASICS_A/B/C@1`, `CLM-ELECTRICAL_GRID_BASICS-D@1`
- EUs: `EU_ELECTRICAL_GRID_BASICS_A/B/C@1`, `EU-ELECTRICAL_GRID_BASICS-D@1`
- Sources: `SRC_ELECTRICAL_GRID_BASICS@1`, `SRC-DOE-ELECTRIC-GRIDS-2026@1`
- Context/Scope: `CTX_ELECTRICAL_GRID_BASICS@1`, `SCP_ELECTRICAL_GRID_BASICS@1`

**Proposed versioned records: 4**

| Exact record | Proposed version | Exact permitted change |
|---|---:|---|
| `EU_ELECTRICAL_GRID_BASICS_A` | v1→v2 | Pin EIA “The electric power grid”, paragraphs 1–2 |
| `EU_ELECTRICAL_GRID_BASICS_B` | v1→v2 | Pin EIA “Delivering electricity”: transmission lines, distribution lines and transformers at substations |
| `EU_ELECTRICAL_GRID_BASICS_C` | v1→v2 | Pin EIA “U.S. electrical system interconnections” and “Balancing authorities”; retain U.S.-specific topology boundary |
| `EU-ELECTRICAL_GRID_BASICS-D` | v1→v2 | Pin DOE “Electric Grids” opening paragraphs and reliability/resilience discussion; retain U.S. context |

Claims, Sources, Context and Scope remain unchanged. Do not update a Claim merely because its EU version changes.

Sources:
- U.S. EIA, “Electricity explained: How electricity is delivered to consumers”, “The electric power grid”, “Delivering electricity”, “U.S. electrical system interconnections” and “Balancing authorities”. https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php
- U.S. DOE, “Electric Grids”, opening section and reliability/resilience discussion. https://www.energy.gov/topics/electric-grids

**Support boundary:** EIA's three-interconnection model is specific to the contiguous United States. General supply-demand balancing and coordination may be described more broadly, but do not present the EIA's regional topology as global. The DOE page supports the U.S. grid's reliability/resilience framing; it is not a full reliability-engineering standard.

## 4. Exact prohibited changes

The following are outside this proposal and remain prohibited:

- changing publication_status or completion_status;
- changing any Claim except the three expressly proposed wording updates (Disaster Recovery B; Water Quality A and C);
- changing any Source except the Disaster Response primary Source and Disaster Recovery FEMA Source and WHO Source identities listed above;
- creating guessed canonical IDs; any optional FEMA Distribution Management Guide dependency must use the canonical ID allocation process;
- changing Relations, State, Object, Identity, storage, recovery, validators, allowlists, release-gate semantics or candidate membership;
- promoting any record or slice from HOLD;
- modifying README files outside the four named slices or changing unrelated coverage manifests;
- merging PR #22, deploying or changing `main`.

All changes must preserve exact `evidence_role: supports`; no new base Evidence Use role is proposed.

## 5. Required post-authorization validation

After the owner records approval in the authorization manifest:

1. Freeze a new exact PR HEAD and re-fetch all 49 existing records; verify exact ID/version/type and compare against this proposal.
2. Apply the Source changes first; then Claims where explicitly listed; then EUs; then Context/Scope target alignment.
3. Re-fetch every changed record and validate all Claim→EU→Source edges and Context/Scope target references.
4. Validate that the FEMA Distribution Management Plan Guide dependency is either explicitly authorized and ID-allocated or excluded from the graph; do not silently assume full support for Claim B.
5. Update the exact-version master and only the four affected READMEs.
6. Run affected-slice schema/graph/reference tests, then the complete release gate on the final immutable HEAD.
7. Preserve HOLD until source-rights, qualified editorial review, Human View and all WP2 R-01–R-10 decisions close.

## 6. Rights and editorial blockers

- FEMA/US government text may be public-domain government work, but course materials, embedded graphics and third-party content require item-level review.
- WFP Logistics Cluster is an institutional hosted source; item-level reuse terms must be checked.
- UNDRR terminology requires exact attribution and version/date.
- EPA pages are U.S. regulatory sources; third-party media must be checked.
- WHO 2026 guidelines are copyrighted WHO publications; factual paraphrase and attribution only unless a specific reuse permission applies.
- EIA/DOE government pages may contain third-party images/graphics; no media reuse is proposed.
- Disaster Recovery B and Water Quality A/C require explicit subject-editor approval because the proposed changes alter claim wording.
- Disaster recovery and water-quality legal/safety boundaries require qualified review. These educational records must not be presented as live incident instructions, site-specific water safety determinations or electrical-grid operating procedures.

## 7. Approval boundary

This document is a proposal, not authorization. To authorize implementation, the project owner must explicitly approve:
- the exact record/version changes in §3;
- the three proposed Claim wording changes;
- the WFP/Logistics Cluster Source correction and FEMA NDRF Source correction;
- the WHO 2026 Source identity correction;
- whether to add the optional FEMA Distribution Management Plan Guide Source/EU for Disaster Response Claim B, with IDs allocated under the canonical ID policy.

Until that approval is recorded, no canonical edit is permitted. All four slices remain HOLD.
