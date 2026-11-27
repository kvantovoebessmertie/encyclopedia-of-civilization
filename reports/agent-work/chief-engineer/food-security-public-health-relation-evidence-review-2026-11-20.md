# Food Security / Public Health Relation — current-head evidence and rights desk review

Date: 2026-11-20  
Inspection ref: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `97d5b08b520c2bd785ed1a1b12a808a70ebb1dbc`  
Disposition: report-only; preserve all canonical records and HOLD states.

## Exact canonical records re-fetched

- `REL-CROSS-FOOD-PUBLIC-HEALTH@2`
- `CTX-REL-CROSS-FOOD-PUBLIC-HEALTH@1` → exact target Relation @2; reciprocal Relation/Context cycle is coherent.
- Food endpoint: `CLM-FOOD_SECURITY_BASICS-D@1`, `EU-FOOD_SECURITY_BASICS-D@1`, `SRC-FOOD_SECURITY_USDA@1`.
- Public-health endpoint: `CLM-PUBLIC_HEALTH_BASICS-A@1`, `EU-PUBLIC_HEALTH_BASICS-A@1`, `SRC-PUBLIC_HEALTH_BASICS@1`.

The food Claim defines household food security as all household members having access at all times to sufficient food for an active and healthy life. Its EU points to the USDA Economic Research Service food-security measurement page but currently provides only a generic material description, with no section/heading locator.

The public-health Claim states that public health aims to improve population health and prevent disease. Its EU points to the WHO Regional Office for Europe / European Observatory public-health page, again without a pinpoint locator.

The Relation is undirected, with generic `linked_record` roles. The Context targets Relation @2 exactly.

## Direct evidence for the cross-domain link

WHO's *Food safety* fact sheet, dated 4 June 2026, states that food safety, nutrition and food security are closely/inextricably linked; access to sufficient safe and nutritious food is key to sustaining life and promoting good health; unsafe food can cause more than 200 diseases; foodborne diseases create a public-health burden; and food safety requires coordinated national systems, surveillance and a multisectoral One Health approach.

Official page: https://www.who.int/news-room/fact-sheets/detail/food-safety

Useful exact web locators verified:
- Key facts and food security/nutrition linkage: page section “Key facts”.
- Access to safe/nutritious food and disease outcomes: “Overview”.
- Foodborne hazards and diseases: “Major foodborne illnesses and causes”.
- Disease burden and surveillance: “The burden of foodborne diseases”.
- Governmental prevention, control systems and public-health surveillance: “A public health priority – from production to consumption” and “WHO response”.

This is direct evidence for a food-system / population-health connection. It is stronger than the current endpoint EUs, which establish the endpoints separately but do not themselves contain the cross-domain mechanism.

Boundary: the canonical food Claim D is specifically household access to sufficient food. WHO's page provides the broader food safety / nutrition / food-security bridge, but does not mean every household food-insecurity condition directly causes a particular disease. The Relation should remain contextual navigation, not a causal or epidemiological Claim.

## Rights / attribution screen

WHO's general website terms state that site information may be reviewed/reproduced/translated for research or private study but not for sale or commercial use; substantial reproduction or use outside educational/non-commercial purposes requires prior written authorization. WHO's separate publications policy applies CC BY-NC-SA 3.0 IGO to WHO publications, but the fact that a page is hosted on WHO's website does not by itself establish that this specific web fact sheet is a publication carrying that licence. No licence is inferred for this page. See:
- https://www.who.int/about/policies/terms-of-use
- https://www.who.int/about/policies/publishing/copyright

The current review stores only a source identity, locators and concise factual paraphrase. It does not reproduce WHO text, tables, figures or images. Project-level compatibility, commercial-use permission if applicable, and exact item-level rights classification remain open.

## Assessment

**Strong contextual-navigation candidate.** The scientific/operational intersection is direct and authoritative. The current relation can be retained as a navigation link, provided its scope is not overstated. New WHO evidence is not yet represented in the canonical Source/Evidence Use graph.

## Disposition and next action

- Keep Relation @2, Context @1, both endpoint Claims @1, both EUs @1, Sources @1 and both slices HOLD.
- Do not add a WHO Source/Evidence Use, change Relation provenance, alter Claims or change publication states without bounded owner authorization.
- Recommended bounded change, if authorized: add one WHO Food Safety Source record and a Relation-level evidence path with the exact section locators above; retain existing endpoint Claims and the Relation's navigation-only interpretation.
- Independent food-safety / public-health review, rights review, Human View and release approval remain separate gates.
- No canonical JSON or implementation file was changed. No CI result is claimed for this documentation-only report.
