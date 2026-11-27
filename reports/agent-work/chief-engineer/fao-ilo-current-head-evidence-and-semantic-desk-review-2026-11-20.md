# FAO / ILO Evidence Integration — Current-Head Verification and Bounded Semantic Desk Review

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Exact inspected PR branch HEAD: `0386a0ebaadcf023c9ec03438c5b153d79e67f95`  
Status: **CURRENT RECORDS VERIFIED; DESK REVIEW SUPPORTS BOUNDED NAVIGATION ONLY; INDEPENDENT SUBJECT-MATTER / RIGHTS / HUMAN VIEW GATES OPEN; HOLD PRESERVED**

## 1. Purpose and scope

Continue Work Package 1 after the owner-authorized FAO plant-health AMR and ILO migration/labour Guide evidence additions. Re-fetch the exact current records, check the relation/context version cycle, verify the ILO Guide's actual printed-page locators and work-level licence notice against the PDF, and assess only the propositions these sources support.

This is a desk review by the implementation agent. It is not an independent qualified subject-matter review, legal opinion, rights clearance, Human View, or publication decision. No canonical record, candidate denominator, register disposition, allowlist, or release state is changed by this report.

## 2. Exact current canonical state at HEAD 0386a0e

All eight target records below were fetched from the PR branch at the exact inspected HEAD. Their IDs, versions and types match the expected graph.

### FAO — AMR / Plant Health

| Record | Current version | Result |
|---|---:|---|
| `SRC-FAO-AMR-PLANT-HEALTH` | @1 | Exact Source |
| `REL-CROSS-AMR-PLANT-HEALTH` | @3 | Exact Relation |
| `CTX-REL-CROSS-AMR-PLANT-HEALTH` | @2 | Exact Context |

Reference cycle: Relation @3 `frame_ref` → Context @2; Context @2 `target_ref` → Relation @3.

The Relation retains the original two participants, order, relation type `one_health_plant_health_link`, linked-record roles and undirected direction. Its provenance now includes the FAO Source @1 alongside the pre-existing WHO and APS Sources. The Context condition remains explicitly relation-scoped and does not replace either Claim, Scope or Evidence Use.

### ILO — Migration / Labour Economics

| Record | Current version | Result |
|---|---:|---|
| `SRC-MIGRATION-LABOUR-STATISTICS-ILO-GUIDE` | @1 | Exact Source |
| `EU-MIGRATION_AND_MOBILITY_BASICS-C-ILO-GUIDE` | @1 | Exact Evidence Use |
| `EU-LABOR_ECONOMICS_BASICS-C-ILO-GUIDE` | @1 | Exact Evidence Use |
| `CLM-MIGRATION_AND_MOBILITY_BASICS-C` | @2 | Exact Claim target |
| `CLM-LABOR_ECONOMICS_BASICS-C` | @2 | Exact Claim target |

Both new Evidence Use records resolve to the exact ILO Guide Source @1 and the exact existing Claim @2. The existing UNSD migration Evidence Use @2 and ILOSTAT labour Evidence Use @2 are unchanged. The existing ILOSTAT path remains the source path for the productivity component.

The dependent Relation remains `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`; its Context @1 targets Relation @4 exactly. Both Relation participants and provenance Claim references resolve to the two Claim @2 records. The Relation and Context were not changed under the ILO Guide authorization.

## 3. FAO evidence and semantic boundary

### Direct source support

The canonical FAO Source identifies the official FAO AMR / Plant Health page:

https://www.fao.org/pest-and-pesticide-management/pesticide-risk-reduction/amr/en/

The page states that AMR in plant health includes (a) resistance of plant pathogens to antimicrobials used as pesticides and (b) contributions from pesticide use in plant production to AMR in human and animal pathogens. It gives crop disease control examples and explicitly places plant health within AMR programmes.

This is direct evidence for a plant-health / AMR cross-domain connection. It is not merely a shared topic label.

### Endpoint fit

- `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` states that AMR affects people, animals, plants, food systems and the environment and therefore requires an intersectoral approach. The existing WHO Evidence Use remains the Claim-level support path.
- `CLM-PLANT_PATHOLOGY_BASICS-A@1` states that phytopathology studies plant diseases and disorders. The existing APS Evidence Use remains the Claim-level support path.
- The FAO Source is linked at Relation level only, as expressly authorized. No FAO Evidence Use was created for the generic phytopathology definition.

### Desk-review disposition

The current endpoint pair and relation type are defensible as **contextual navigation** between antimicrobial resistance and plant pathology / plant health. The FAO page provides a concrete bridge: plant pathogens may be exposed to antimicrobials used as pesticides, and plant-production practices may contribute to wider AMR pathways.

Do not interpret this as:
- FAO evidence supporting the generic definition of phytopathology;
- proof that every plant disease involves antimicrobial resistance;
- proof of a quantified transmission pathway or causal effect in a specific crop, population or location;
- a replacement for the existing WHO or APS Claim-level Evidence Use.

**Result: retain HOLD pending independent plant-health / AMR subject-matter review, rights/distribution review and Human View.** The desk review improves the evidential basis for the Relation but does not close its release gates.

Additional current FAO background page with a more detailed narrative on the One Health plant-production pathway:
https://www.fao.org/one-health/highlights/amr-does-it-matter-for-plant-health-too

That additional page was consulted as corroborating public context only; it is not part of the canonical Source @1 and no new Source record or canonical change is proposed in this report.

## 4. ILO Guide evidence and semantic boundary

### Work-level licence verified against the PDF

The exact ILO PDF is available at:

https://www.ilo.org/sites/default/files/2026-07/ILO_Guide_Mapping_ILMS_2026_FINAL.pdf

Printed page ii states **Creative Commons Attribution 4.0 International (CC BY 4.0)**. It requires attribution to ILO and indication of changes. The notice excludes third-party materials from the licence and restricts use of the ILO emblem, name and logo in connection with translations, adaptations or derivative works. The Guide itself is not translated or adapted by the authorized records.

This is a work-specific licence statement, not an inference from a general ILO policy. It does not clear any third-party component or determine the Encyclopedia's project-level distribution licence.

### Migration Claim C — locator fit

The Claim states that comparison of migration processes requires clarification of definitions, reference period, territory and the method of measuring stocks or flows.

The new Evidence Use locator (printed pp. 22–27 and 34–38) is well aligned:
- printed pp. 22–27 cover reference statistical concepts, migration concepts, international mobility, migrant categories and stock/flow measures;
- printed pp. 34–38 cover international labour mobility, labour attachment and related population groups.

The Guide explicitly distinguishes stocks (a count at a point in time) from flows (movement over a specified period), and distinguishes international migration from temporary mobility. These passages directly support the need to define the population, time period and measure before comparing migration statistics.

**Result: additive support is substantively well matched to the current Claim.** It does not determine an individual's immigration status, provide legal advice, or supersede the UNSD general migration-statistics recommendations.

### Labour Economics Claim C — locator fit and limits

The Claim identifies employment, earnings, working time, productivity and labour underutilization as labour-market indicators.

The new ILO Guide Evidence Use (printed pp. 30–33, 57–58 and 63–66) is well matched to selected parts:
- printed pp. 30–33 cover labour-force status, employment, unemployment and labour underutilization;
- printed pp. 57–58 cover core labour-market indicators for international migrants, including participation, employment, unemployment and underutilization measures;
- printed pp. 63–66 discuss source-specific coverage and limitations, including the challenges of measuring migrant groups and the use of surveys / administrative records.

The Guide is **not** relied upon as support for all wage measures or for labour productivity comparability. The existing ILOSTAT Evidence Use remains the source path for productivity and for the broader indicator set. Its source-specific page-level rights and comparability limitations remain separate.

A focused current ILOSTAT recheck also found:
- the LFS/RURBAN database description identifies employment and labour-underutilization measures;
- the COND database description identifies hourly/monthly earnings and actual weekly hours and explains that working-time measures can differ according to actual/usual hours, reference periods and job coverage;
- ILOSTAT's labour-productivity materials identify output per worker and output per hour worked as separate measures.

Useful official pages:
- https://ilostat.ilo.org/databases/lfs/description/
- https://ilostat.ilo.org/methods/concepts-and-definitions/description-wages-and-working-time-statistics/
- https://ilostat.ilo.org/blog/why-would-labour-productivity-surge-during-a-pandemic/
- https://ilostat.ilo.org/Data/

These ILOSTAT pages were checked as source-fit context only. No new canonical Source/Evidence Use or locator correction is authorized by this report. In particular, productivity comparisons require attention to output concept, worker/hour denominator, price basis, PPP and national measurement methods; the ILO Guide does not automatically establish comparability for migrant groups.

**Result: the new ILO Guide is valid additive support for migration-related labour-market measurement, while UNSD and ILOSTAT remain in place.** It must not be treated as replacing the existing source chain or proving productivity comparability.

## 5. Rights and distribution status

- **FAO:** the canonical Source @1 records citation, hyperlink, locator and independently worded paraphrase only. FAO's terms restrict translation/adaptation and commercial resale without permission; third-party components require separate clearance. No FAO expressive material or logo is reproduced. This is not commercial/adaptive rights clearance.
- **ILO Guide:** work-level CC BY 4.0 is verified on printed p. ii, with attribution/change indication and third-party exclusions. No logo or third-party material is reproduced. This does not adopt the Encyclopedia's project licence or settle all rights for the complete first-edition bundle.
- **ILOSTAT:** the existing Source @2 expressly does not assert CC BY 4.0 for its web pages because item-level publication dates/licences are not established. The new Guide licence must not be transferred to ILOSTAT pages.
- **WHO / APS / UNSD:** their existing source-specific rights conditions remain as previously recorded; the FAO/ILO additions do not clear or replace those conditions.

Project-wide owner decisions R-01–R-10 remain open. No rights holder, project content licence, software licence, contributor terms, editor, release approver or correction contact is inferred.

## 6. Disposition and remaining gates

| Item | Desk-review result | Release status |
|---|---|---|
| FAO / AMR–Plant Health Relation @3 | Defensible contextual-navigation candidate; FAO relation-level boundary preserved | HOLD |
| Migration / Labour Relation @4 | Additive ILO Guide evidence is well matched to migration/labour measurement intersection | HOLD |
| Migration Claim C / ILO Guide EU @1 | Directly supports definitions, periods, stocks/flows and mobility concepts | HOLD |
| Labour Claim C / ILO Guide EU @1 | Supports selected labour-force and migrant labour-market indicators, not productivity comparability | HOLD |

Required next steps:
1. Obtain independent plant-health / AMR review of the FAO-linked Relation.
2. Obtain independent labour-statistics review of the Migration/Labour Relation and the split between the ILO Guide, UNSD and ILOSTAT support paths.
3. Complete item-level rights review against the final distribution model and close owner decisions R-01–R-10.
4. Complete Human View and the other record-level first-edition gates.
5. Keep both Relations and all affected slices HOLD until explicit release review. Do not create or infer an INCLUDE allowlist from this report.

## 7. Technical and repository boundary

At exact branch HEAD `0386a0ebaadcf023c9ec03438c5b153d79e67f95`, all four required PR #22 workflows completed successfully:

| Workflow | Run ID | Result |
|---|---:|---|
| Offline Edition | 44737912286 | PASS |
| MVP Contribution Form Browser Tests | 44737912271 | PASS |
| Reference implementation tests | 44737912270 | PASS |
| Release Conformance Gate | 44737912273 | PASS |

This confirms technical conformance for that exact HEAD only. It does not confer semantic, legal, editorial or publication approval.

No canonical JSON, standard, validator, test, candidate register, allowlist, publication state or release decision was changed by this report. PR #22 remains Draft and unmerged. `main` remains unchanged at the previously verified SHA `d58289f319993ede5294a46f4741a506fd2fd710`.

**Acceptance:** accept as a current-head record verification and bounded semantic desk review. Independent expert review, rights clearance, Human View and release approval remain open.
