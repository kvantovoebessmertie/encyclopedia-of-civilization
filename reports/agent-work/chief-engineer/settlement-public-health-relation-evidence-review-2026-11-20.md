# Human Settlement Systems / Public Health Relation — current-head evidence and rights desk review

Date: 2026-11-20  
Inspection ref: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `97d5b08b520c2bd785ed1a1b12a808a70ebb1dbc`  
Disposition: report-only; preserve all canonical records and HOLD states.

## Exact canonical records re-fetched

- `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@2`
- `CTX-REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1` → exact target Relation @2; reciprocal Relation/Context cycle is coherent.
- Settlement endpoint: `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C@1`, `EU_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C@1`, `SRC_OECD_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1`.
- Public-health endpoint: `CLM-PUBLIC_HEALTH_BASICS-A@1`, `EU-PUBLIC_HEALTH_BASICS-A@1`, `SRC-PUBLIC_HEALTH_BASICS@1`.

The settlement Claim describes integrated planning/management of human settlements across spatial, infrastructure, social and environmental dimensions. Its EU points to the OECD *Sustainable urban development* topic page and provides a descriptive summary, but no pinpoint locator.

The public-health Claim is a general definition: public health aims to improve population health and prevent disease. Its EU points to the WHO Regional Office for Europe / European Observatory public-health page, without a pinpoint locator.

The Relation uses roles `settlement_system_claim` and `linked_domain_claim`, is undirected, and has a generic settlement/public-health system link type. Its Context targets Relation @2 exactly.

## Important provenance traceability observation

The Relation's `provenance.created_from` names `SRC_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1` (UN Human Settlements) and `SRC-PUBLIC_HEALTH_BASICS@1` (WHO public-health overview). However, the actual settlement endpoint Claim C and its Evidence Use point to `SRC_OECD_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1`, not the UN source. This is not proof that the Relation is invalid: the UN source may have been used for broader relation framing. But the provenance list does not mirror the actual endpoint Claim/EU source chain, and the current report does not find a pinpoint locator in either endpoint EU. Preserve this as a traceability question; do not silently replace the source or rewrite provenance.

## Direct official evidence for the cross-domain mechanism

WHO's current urban-health materials explicitly connect urban systems to population health:

1. WHO, *Providing cross-cutting solutions to improve health in urban areas*: https://www.who.int/activities/providing-cross-cutting-solutions-to-improve-health-in-urban-areas  
   The page states that urban population health and well-being are determined by social, environmental and economic factors strongly influenced by housing, transport, energy, spatial planning, water and sanitation, urban agriculture and waste management. It expressly describes coordinated cross-sector action as necessary for urban health.
2. WHO, *Urban health* fact sheet (19 March 2025): https://www.who.int/news-room/fact-sheets/detail/urban-health  
   Identifies sanitation, drinking water, air pollution, transport design, housing, waste management and built-environment conditions as determinants or risk pathways for population health; discusses infectious disease, noncommunicable disease, injury and health inequities.
3. WHO, *Health equity in urban settings*: https://www.who.int/teams/environment-climate-change-and-health/healthy-urban-environments/urban-planning/health-equity  
   Specifically lists built environments, housing, safe water and sanitation, food security, transport and air quality among health determinants; describes elevated exposure and unequal risk for vulnerable groups in poorly serviced settlements.

These are direct evidence for a settlement-systems / public-health relationship. The strongest direct bridge is WHO's cross-cutting urban-health page, which names the same cross-sector settlement systems implicated by the endpoint Claim and connects them to population health.

## Assessment and boundaries

**Strong contextual-navigation candidate.** The relation is scientifically and conceptually defensible as a systems-level link: settlement planning and infrastructure shape exposures, access to services and environmental conditions that influence population health.

Boundaries:
- Do not imply that every settlement design feature has a uniform health effect or that urbanization itself is necessarily harmful.
- Keep the distributional dimension visible: effects vary by neighbourhood, infrastructure access and social vulnerability.
- Distinguish planning/system determinants from direct clinical causation.
- The new WHO urban-health sources support the cross-domain relation, but they are not yet in the canonical Source/Evidence Use graph.

## Rights / attribution screen

WHO website terms restrict use of website information beyond research/private study and prohibit sale/commercial use absent the relevant permission; substantial reproduction or other educational/non-commercial use requires prior written authorization under the site terms. WHO's separate publications CC BY-NC-SA 3.0 IGO policy should not be assumed to apply to these specific web pages without page-level confirmation. See:
- https://www.who.int/about/policies/terms-of-use
- https://www.who.int/about/policies/publishing/copyright

The current UN Human Settlements source is a UN website page. UN's copyright notice states that materials are all rights reserved and reproduction/transmission requires written permission except as allowed by the website terms: https://www.un.org/en/about-us/copyright. The OECD source page's item-level terms and the project's intended distribution model also require review. No broad reuse licence is inferred for any of these web pages.

## Disposition and next action

- Keep Relation @2, Context @1, both Claims @1, EUs @1, Sources @1 and affected slices HOLD.
- Do not change Relation provenance, add WHO Sources/Evidence Uses, replace the settlement endpoint, or change publication states without bounded owner authorization.
- Recommended bounded next step: authorize a WHO urban-health Relation-level evidence path with exact locators; separately reconcile whether the UN source in Relation provenance is intentional and whether OECD source should be represented in Relation-level provenance. Keep the endpoint Claim and EU unchanged unless a reviewer finds a specific defect.
- Independent urban planning / public-health review, rights review, Human View and release approval remain separate gates.
- No canonical JSON or implementation file was changed. No CI result is claimed for this documentation-only report.
