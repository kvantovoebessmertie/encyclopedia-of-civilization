# Bounded Owner Authorization Request — Relation-level evidence provenance additions

Date: 2026-11-20  
Prepared against PR branch HEAD: `1dfada65a54eaeadbadfa2024140dcb9df73de02`  
Purpose: request explicit approval for three narrowly scoped, evidence-backed Relation provenance additions.  
Status: **NOT AUTHORIZED / NO CANONICAL CHANGES MADE**.

## Decision requested

Approve or reject each numbered scope independently. Approval of one item does not approve the others. The proposed changes add external source identity/provenance only; they do not change Claim wording, Claim participants, Relation semantics, publication states, candidate membership, allowlists or release decisions.

For every approved item:
- create the named Source @1 under `CONTENT/vertical-slices/cross-slice-linkage/records/`;
- increment the named Relation and its target-specific Context by one version;
- add the new Source reference to the Relation and Context `provenance.created_from` arrays, preserving all existing entries;
- update only the reciprocal Relation.frame_ref / Context.target_ref version values;
- preserve relation_type, participants, order, roles, direction, Context content, epistemic status, publication_status and completion_status;
- preserve HOLD for the Relation and all affected slices;
- do not create Evidence Use records for Relations: the current Evidence Use schema is Claim-targeted, and these additions are Relation-level provenance only;
- run exact-reference validation and the required CI workflows on the final immutable HEAD after all approved canonical changes.

No approval is inferred from this request. If the owner wants a different source identity, record scope or version plan, the item must be revised before execution.

---

## A. Groundwater / Soil Microbiology

<badge color="success">Strong direct mechanism located</badge>

**Current records**
- Relation: `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2`
- Context: `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1`
- Participants remain `CLM-GROUNDWATER_BASICS-A@1` and `CLM-SOIL_MICROBIOLOGY_BASICS-A@1`.

**Proposed new Source**
- ID/version: `SRC-USGS-GROUNDWATER-SOIL-MICROBIAL-INTERACTIONS@1`
- Identity: USGS, *The significance of microbial processes in hydrogeology and geochemistry* (2000).
- URI: https://www.usgs.gov/publications/significance-microbial-processes-hydrogeology-and-geochemistry
- Representation: official USGS publication page; external canonical source, no copied publication stored locally.
- Evidence boundary: the abstract states that microbial processes affect groundwater chemical composition and aquifer hydraulic properties in contaminated and pristine systems. A companion USGS hydrologic-cycle page also describes soil microbial effects on water chemistry during infiltration: https://pubs.usgs.gov/circ/circ1139/htdocs/natural_processes_of_ground.htm

**Exact authorized mutation if approved**
1. Create the Source record above at version @1.
2. Relation @2 → @3; append Source @1 to existing `provenance.created_from`.
3. Context @1 → @2; append Source @1 to existing `provenance.created_from`.
4. Set Relation.frame_ref to Context @2 and Context.target_ref to Relation @3.
5. Preserve both participant Claims, roles, direction, relation_type and all other fields.

**Non-goals:** no Claim rewrite, no new endpoint, no claim that all soil microbes enter aquifers, no claim that microbial activity makes groundwater safe, no INCLUDE or release approval.

## B. Food Security / Public Health

<badge color="success">Direct WHO bridge located</badge>

**Current records**
- Relation: `REL-CROSS-FOOD-PUBLIC-HEALTH@2`
- Context: `CTX-REL-CROSS-FOOD-PUBLIC-HEALTH@1`
- Participants remain `CLM-FOOD_SECURITY_BASICS-D@1` and `CLM-PUBLIC_HEALTH_BASICS-A@1`.

**Proposed new Source**
- ID/version: `SRC-WHO-FOOD-SAFETY-2026@1`
- Identity: WHO, *Food safety*, fact sheet dated 4 June 2026.
- URI: https://www.who.int/news-room/fact-sheets/detail/food-safety
- Representation: official WHO web fact sheet; external canonical source, no copied publication stored locally.
- Pinpoint locator: “Key facts”; “Overview”; “The burden of foodborne diseases”; “A public health priority – from production to consumption”; “WHO response”.
- Evidence boundary: WHO directly links food security, nutrition and health; describes foodborne disease burden and national food-control/surveillance responses. This supports contextual navigation, not a universal causal claim about every food-insecurity condition.

**Exact authorized mutation if approved**
1. Create the Source record above at version @1.
2. Relation @2 → @3; append Source @1 to existing `provenance.created_from`.
3. Context @1 → @2; append Source @1 to existing `provenance.created_from`.
4. Set Relation.frame_ref to Context @2 and Context.target_ref to Relation @3.
5. Preserve both participant Claims, roles, direction, relation_type and all other fields.

**Non-goals:** no Claim rewrite, no new endpoint, no claim that household food insecurity necessarily causes a particular disease, no INCLUDE or release approval.

**Rights condition:** WHO website terms and WHO publication licensing are distinct. Do not assign CC BY-NC-SA 3.0 IGO to this web fact sheet without item-level confirmation. WHO site terms restrict sale/commercial use and require prior written permission for substantial reproduction or uses outside educational/non-commercial purposes. The proposed Source stores identity and locator only, not WHO text, images or tables. Project distribution compatibility remains open.

## C. Human Settlement Systems / Public Health

<badge color="success">Strong systems-level bridge located</badge>

**Current records**
- Relation: `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@2`
- Context: `CTX-REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1`
- Participants remain `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C@1` and `CLM-PUBLIC_HEALTH_BASICS-A@1`.

**Proposed new Source**
- ID/version: `SRC-WHO-URBAN-HEALTH-CROSS-SECTOR@1`
- Identity: WHO, *Providing cross-cutting solutions to improve health in urban areas*.
- URI: https://www.who.int/activities/providing-cross-cutting-solutions-to-improve-health-in-urban-areas
- Representation: official WHO web page; external canonical source, no copied publication stored locally.
- Pinpoint locator: page title and opening substantive paragraphs (paragraphs describing housing, transport, energy, spatial planning, water/sanitation, urban agriculture, waste management and population health).
- Evidence boundary: WHO explicitly states that social, environmental and economic factors shaped by urban systems determine urban population health and well-being. This supports systems-level contextual navigation, not a deterministic health effect for every settlement feature.

**Additional provenance traceability decision required**
The current Relation provenance names `SRC_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1` (UN Human Settlements) and `SRC-PUBLIC_HEALTH_BASICS@1`. However, the settlement endpoint Claim C and its EU point to `SRC_OECD_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1`. The source record already exists. Choose one of the following before mutation:
- **C1 (recommended, additive):** preserve both current Relation provenance entries and append both the existing OECD Source @1 and the new WHO Urban Health Source @1 to Relation and Context `created_from`; this records the actual endpoint chain and the direct cross-domain bridge without deleting historical provenance.
- **C2:** append only the WHO Source @1 and leave the current UN/OECD provenance difference explicitly unresolved for a later audit.
- **Not proposed:** deleting or replacing the UN Source reference, because its role in historical Relation framing has not been disproved.

**Exact authorized mutation if approved**
1. Create `SRC-WHO-URBAN-HEALTH-CROSS-SECTOR@1`.
2. Relation @2 → @3; append WHO Source @1 and (if C1 selected) existing OECD Source @1 to `provenance.created_from`, preserving existing entries.
3. Context @1 → @2; apply the same additive provenance update.
4. Set Relation.frame_ref to Context @2 and Context.target_ref to Relation @3.
5. Preserve both participant Claims, roles, direction, relation_type and all other fields.

**Rights condition:** WHO website terms apply unless the exact page is shown to be a WHO publication under a specific licence. UN website material is all rights reserved subject to UN website terms. OECD page-level terms also require review. No broad reuse licence is inferred.

## Shared constraints and execution control

- Each item remains HOLD after implementation.
- These are source/provenance improvements, not semantic re-adjudication or publication approval.
- No Relation endpoint, Claim text, Evidence Use, Scope, candidate membership, allowlist or release status may be changed under this authorization.
- Independent domain review remains required: hydrogeology/microbial ecology for A; food safety/public health for B; urban planning/public health for C.
- Rights review, Human View, editorial approval and owner decisions R-01–R-10 remain separate.
- If approved, execute only the selected item(s), re-fetch every changed record at the resulting exact HEAD, compare all preserved fields, validate reciprocal refs, and run all four required workflows on one immutable HEAD.
- Do not merge PR #22, alter `main`, publish, deploy or create a release allowlist.

## Owner response format

Please authorize only the exact scopes selected, for example:
- “Approve A and B exactly as written; C1 for C.”
- “Approve C only, option C2.”
- “Reject A; approve B; defer C.”

No changes will be made until the owner gives explicit approval for the relevant bounded scope.
