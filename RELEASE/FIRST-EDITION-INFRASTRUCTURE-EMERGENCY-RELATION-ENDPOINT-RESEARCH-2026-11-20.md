# First Edition — Emergency Management / Infrastructure Resilience Relation Endpoint Research

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `a632df5d5c078c21b9dbda33e9e0a819e767ad4a`  
Status: **EVIDENCE/ENDPOINT RESEARCH COMPLETE; RELATION CORRECTION PROPOSED ONLY; NO CANONICAL RECORDS CHANGED**

## 1. Scope

This research addresses the infrastructure-specific endpoint gap recorded for `REL_M3_EMERGENCY_INFRASTRUCTURE`. It checks whether an existing, exact-version infrastructure Claim with direct Evidence Use can replace the generic Infrastructure Resilience Claim A endpoint.

No canonical change is authorized by this report. The Relation and its Context remain unchanged and HOLD. No publication, allowlist or INCLUDE decision is made.

## 2. Current Relation and dependency state

Current records re-fetched at inspection HEAD:

- `REL_M3_EMERGENCY_INFRASTRUCTURE@2`
- `CTX-REL_M3_EMERGENCY_INFRASTRUCTURE@1`
- `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1`
- `EU-EMERGENCY_MANAGEMENT_BASICS-A@1`
- `EU_EMERGENCY_MANAGEMENT_BASICS_UNDRR@1`
- `SRC-EMERGENCY_MANAGEMENT_BASICS@1`
- `SRC_UNDRR_EMERGENCY_MANAGEMENT@1`
- `CLM-INFRASTRUCTURE_RESILIENCE-A@1` (current Relation endpoint)
- `CLM-INFRASTRUCTURE_RESILIENCE-D@2`
- `EU-INFRASTRUCTURE_RESILIENCE-D@2`
- `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@2`

Current Relation @2 participants:
1. `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1`: emergency management includes preparation, response, resource coordination and recovery.
2. `CLM-INFRASTRUCTURE_RESILIENCE-A@1`: broad community resilience statement, not infrastructure-specific.

Current Relation provenance:
- `SRC_UNDRR_EMERGENCY_MANAGEMENT@1`
- `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`

The historical FEMA Source @1 has now been restored as a separate versioned record in the infrastructure slice, so this exact historical provenance edge resolves. It must remain historical and must not be silently reinterpreted as CISA @2.

## 3. Better existing infrastructure endpoint found

Existing candidate:

- `CLM-INFRASTRUCTURE_RESILIENCE-D@2`
- `EU-INFRASTRUCTURE_RESILIENCE-D@2`
- `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@2` (corrected source identity: CISA)

Claim D states that dependencies between infrastructure systems can affect community risk and should be considered in resilience planning.

Its Evidence Use @2 has an exact locator:

> CISA, *The Infrastructure Dependency Primer* (as of June 2, 2023), p. 1, “Overview” and “Learn” module.

The official CISA PDF's first-page Overview states that the primer is intended to help state and local planners understand how infrastructure dependencies can affect risk and resilience in their communities and incorporate that knowledge into ongoing planning. The Learn module identifies essential community functions/services, the infrastructure systems supporting them, and how interdependencies can affect risk and resilience.

Official source:
https://www.cisa.gov/sites/default/files/2023-06/InfrastructureDependencyPrimerFS_June23_508c.pdf

This directly supports the infrastructure-specific Claim D at the stated qualitative level. It does not quantify dependency effects, establish universal failure/recovery pathways, or prove that any specific emergency-management action causes an infrastructure outcome.

## 4. Emergency-management endpoint evidence

The current emergency-management Claim A has two existing source chains.

### UNDRR

Source:
https://www.undrr.org/terminology/disaster-management

Exact locator candidate for `EU_EMERGENCY_MANAGEMENT_BASICS_UNDRR@1`:

> UNDRR, *Sendai Framework Terminology on Disaster Risk Reduction* (2017), entry “Disaster management”, definition and annotation.

The definition describes disaster management as the organization, planning and application of measures preparing for, responding to and recovering from disasters. Its annotation describes preparedness and other plans to decrease disaster impacts. This is a direct match to the preparedness/response/recovery portion of Claim A.

### FEMA IS-230.E

Source:
https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-230.e&lang=en

Exact locator candidate for `EU-EMERGENCY_MANAGEMENT_BASICS-A@1`:

> FEMA, IS-230.E *Fundamentals of Emergency Management*, “Course Objectives”: objectives on preparedness mission areas, comprehensive emergency operations planning, and planning/managing/coordinating resources for an effective response.

The current overview page directly identifies the course objectives to explain partner roles, preparedness, emergency operations planning, and resource coordination for response. The current page is an overview, not the full course lesson text. It should not be cited as evidence for every detailed phase or for operational procedures beyond the listed objectives.

These locators make the emergency-management endpoint chain more specific, but the Evidence Use records remain generic until separately authorized and versioned.

## 5. Semantic endpoint assessment

A stronger existing pair is available:

1. `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1`
2. `CLM-INFRASTRUCTURE_RESILIENCE-D@2`

The UNDRR source supports the organization/planning of preparedness, response and recovery measures; the CISA source supports incorporating infrastructure dependencies into community risk and resilience planning. Together they justify a **bounded contextual/navigation link** between emergency management and infrastructure resilience planning.

The link must not imply:
- a quantified infrastructure risk effect;
- a universal causal chain from infrastructure failure to emergency outcomes;
- a specific service dependency not named in the sources;
- that CISA's planning guidance replaces emergency-management doctrine;
- that either Claim independently proves the other.

This pair is stronger than the current `CLM-INFRASTRUCTURE_RESILIENCE-A@1` endpoint because Claim D explicitly names infrastructure-system dependencies and resilience planning.

## 6. Proposed versioned Relation correction — authorization required

If the owner authorizes this bounded correction, consider:

- `REL_M3_EMERGENCY_INFRASTRUCTURE@2 → @3`
- Replace only the second participant:
  - from `CLM-INFRASTRUCTURE_RESILIENCE-A@1`
  - to `CLM-INFRASTRUCTURE_RESILIENCE-D@2`
- Update Relation provenance from historical FEMA Source @1 to corrected CISA Source @2, retaining the UNDRR Source @1:
  - `SRC_UNDRR_EMERGENCY_MANAGEMENT@1`
  - `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@2`
- Preserve `relation_type`, both roles, undirected direction, first participant and its exact version, all other semantic fields and HOLD status.
- Version Context `CTX-REL_M3_EMERGENCY_INFRASTRUCTURE@1 → @2` to target Relation @3, and point Relation @3's `frame_ref` to Context @2. Preserve the context statement and epistemic status.
- Copy only the authorized, exact source provenance into the new Context; do not introduce additional assertions.

The Relation remains HOLD after any correction until independent semantic review, exact-version/reference validation, rights review, editorial review and Human View are complete.

## 7. Rights and release boundary

- The CISA PDF is publicly available from an official U.S. government domain. The inspected first-page text provides source identity and locator, but public availability is not itself a complete downstream rights clearance.
- No explicit reuse licence or copyright statement was verified from the accessible first-page text. Do not infer rights for third-party images, logos or embedded material. Keep rights-holder, licence, attribution and distribution review separate.
- UNDRR and FEMA pages are official public references; no project-level reuse licence or blanket reproduction permission is inferred.
- Use factual paraphrase and precise attribution; do not reproduce source text, graphics or tables without rights review.

## 8. Result and next action

Completed:
- Identified an existing infrastructure-specific Claim D @2 with exact CISA Source @2 and page-1 locator.
- Located direct UNDRR and FEMA course-overview locators for the emergency-management Claim A.
- Identified a defensible existing endpoint pair and a narrowly bounded Relation/Context versioning plan.

Not done:
- No canonical Claim, Source, Evidence Use, Relation or Context was changed.
- No Relation or Claim was promoted; `REL_M3_EMERGENCY_INFRASTRUCTURE` remains HOLD.
- No rights clearance, owner decision, allowlist or release approval was invented.

Next action: obtain a separate bounded owner authorization for the exact Relation/Context correction above, or explicitly retain the Relation on HOLD / exclude it from first-edition release scope. The existing historical Source @1 restoration does not authorize this semantic Relation change.


## 9. Implemented bounded Relation / Context correction — 2026-11-20

The project owner explicitly authorized the exact limited correction described in the preceding research section. The authorization is recorded as `R9-EMERGENCY-INFRASTRUCTURE-RELATION-ENDPOINT-ALIGNMENT-2026-11-20` in `RELEASE/EDITORIAL-CORRECTION.json`.

Implemented on PR #22:

- `REL_M3_EMERGENCY_INFRASTRUCTURE@2 → @3`
  - Second participant changed only from `CLM-INFRASTRUCTURE_RESILIENCE-A@1` to `CLM-INFRASTRUCTURE_RESILIENCE-D@2`.
  - Infrastructure provenance changed only from `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1` to `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@2`; `SRC_UNDRR_EMERGENCY_MANAGEMENT@1` retained.
  - `frame_ref` now points to `CTX-REL_M3_EMERGENCY_INFRASTRUCTURE@2`.
- `CTX-REL_M3_EMERGENCY_INFRASTRUCTURE@1 → @2`
  - `target_ref` now points to Relation @3.
  - Infrastructure Source provenance changed only to Source @2; UNDRR Source @1 retained.

Preserved exactly: Relation type, first participant and version, participant order, roles, undirected direction, provenance methods, Context condition, epistemic status, record identities, type versions, publication/completion statuses and all other fields.

Implementation commits:
- Bounded authorization manifest: `f928d4fdb69946d596cff5ee469e028e36018862`
- Relation @3: `2f1b34b95a9600edc502d1d74d6956ebb94c69ee`
- Context @2: `8c68b1309d53d6edfc0fdd62e5e058f20f1de556`

The exact-version cycle is now reciprocal: Relation @3 `frame_ref` → Context @2; Context @2 `target_ref` → Relation @3. Both provenance chains resolve to the restored historical Source @1 only where earlier records still pin it, and to current CISA Source @2 for this corrected Relation/Context pair.

The prior research-only status in Sections 1 and 8 is historical and is superseded only as to implementation status by this section. The Relation and both affected slices remain HOLD. No Claim, Source, Evidence Use, Scope, other Relation or Context was changed; no Evidence Use locator, allowlist, INCLUDE/EXCLUDE decision, publication, deployment, merge or main-branch change was made.

The correction establishes a bounded contextual/navigation link only. It does not establish quantified dependency effects, universal causal pathways, a specific service dependency, or a causal relationship between the two Claims. Independent semantic/editorial review, rights/project-distribution review, Human View and exact-head CI remain required.
