# M13 Batch 13 — exact candidate worklist and source-fit checkpoint

Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Scope and selection rule

This file freezes a **100-Claim candidate worklist** from inventory rows 541–650. Rows with an existing ledger score were excluded, rather than counted as new reviews. The selected rows are exactly those marked `NOT_INSPECTED` and `UNSCORED` in the 2026-10-11 inventory-to-ledger join. Candidate selection is not a score, and it does not itself complete the audit. Semantic duplicates, prior-report linkage, evidence fit, source pinpoints, and D/E/B still require review for each candidate.

- Inventory rows scanned: 110
- Previously scored rows excluded: 10
- Unique selected candidates: 100
- Candidate IDs duplicated within this list: 0
- Claims with provisional D/E/B review recorded across checkpoints: 18
- Remaining candidates without an individual D/E/B review: 82

## Candidate list

| Inventory row | Claim ID | Record path | Work status |
|---:|---|---|---|
| 541 | `CLM-FOOD_DISTRIBUTION_BASICS-D` | `CONTENT/vertical-slices/food-distribution-basics/records/CLM-FOOD_DISTRIBUTION_BASICS-D.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/editorial follow-up open |
| 542 | `CLM-FOOD_FERMENTATION_BASICS-A` | `CONTENT/vertical-slices/food-fermentation-basics/records/CLM-FOOD_FERMENTATION_BASICS-A.json` | PROVISIONAL_REVIEW_RECORDED; source pinpoint follow-up open |
| 543 | `CLM-FOOD_FERMENTATION_BASICS-B` | `CONTENT/vertical-slices/food-fermentation-basics/records/CLM-FOOD_FERMENTATION_BASICS-B.json` | PROVISIONAL_REVIEW_RECORDED; source pinpoint follow-up open |
| 544 | `CLM-FOOD_FERMENTATION_BASICS-C` | `CONTENT/vertical-slices/food-fermentation-basics/records/CLM-FOOD_FERMENTATION_BASICS-C.json` | PROVISIONAL_REVIEW_RECORDED; source pinpoint follow-up open |
| 552 | `CLM-FOOD_SCIENCE_BASICS-A` | `CONTENT/vertical-slices/food-science-basics/records/CLM-FOOD_SCIENCE_BASICS-A.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/editorial follow-up open |
| 553 | `CLM-FOOD_SCIENCE_BASICS-B` | `CONTENT/vertical-slices/food-science-basics/records/CLM-FOOD_SCIENCE_BASICS-B.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/editorial follow-up open |
| 554 | `CLM-FOOD_SCIENCE_BASICS-C` | `CONTENT/vertical-slices/food-science-basics/records/CLM-FOOD_SCIENCE_BASICS-C.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/editorial follow-up open |
| 555 | `CLM-FOOD_SECURITY_BASICS-A` | `CONTENT/vertical-slices/food-security-basics/records/CLM-FOOD_SECURITY_BASICS-A.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 556 | `CLM-FOOD_SECURITY_BASICS-B` | `CONTENT/vertical-slices/food-security-basics/records/CLM-FOOD_SECURITY_BASICS-B.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 557 | `CLM-FOOD_SECURITY_BASICS-C` | `CONTENT/vertical-slices/food-security-basics/records/CLM-FOOD_SECURITY_BASICS-C.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 558 | `CLM-FOOD_SECURITY_BASICS-D` | `CONTENT/vertical-slices/food-security-basics/records/CLM-FOOD_SECURITY_BASICS-D.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 559 | `CLM-FOOD_SYSTEMS-A` | `CONTENT/vertical-slices/food-systems-basics/records/CLM-FOOD_SYSTEMS-A.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 560 | `CLM-FOOD_SYSTEMS-B` | `CONTENT/vertical-slices/food-systems-basics/records/CLM-FOOD_SYSTEMS-B.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 561 | `CLM-FOOD_SYSTEMS-C` | `CONTENT/vertical-slices/food-systems-basics/records/CLM-FOOD_SYSTEMS-C.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 562 | `CLM-FOOD_SYSTEMS-D` | `CONTENT/vertical-slices/food-systems-basics/records/CLM-FOOD_SYSTEMS-D.json` | PROVISIONAL_D_E_B_RECORDED; source-fit/overlap follow-up open |
| 563 | `CLM-FORESTRY_BASICS-A` | `CONTENT/vertical-slices/forestry-basics/records/CLM-FORESTRY_BASICS-A.json` | PROVISIONAL_D_E_B_RECORDED; source-pinpoint follow-up open |
| 564 | `CLM-FORESTRY_BASICS-B` | `CONTENT/vertical-slices/forestry-basics/records/CLM-FORESTRY_BASICS-B.json` | PROVISIONAL_D_E_B_RECORDED; source-pinpoint follow-up open |
| 565 | `CLM-FORESTRY_BASICS-C` | `CONTENT/vertical-slices/forestry-basics/records/CLM-FORESTRY_BASICS-C.json` | PROVISIONAL_D_E_B_RECORDED; source-pinpoint follow-up open |
| 566 | `CLM-FORMAL_METHODS_BASICS-A` | `CONTENT/vertical-slices/formal-methods-basics/records/CLM-FORMAL_METHODS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 567 | `CLM-FORMAL_METHODS_BASICS-B` | `CONTENT/vertical-slices/formal-methods-basics/records/CLM-FORMAL_METHODS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 568 | `CLM-FORMAL_METHODS_BASICS-C` | `CONTENT/vertical-slices/formal-methods-basics/records/CLM-FORMAL_METHODS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 569 | `CLM-FOUNDATION_ENGINEERING_BASICS-A` | `CONTENT/vertical-slices/foundation-engineering-basics/records/CLM-FOUNDATION_ENGINEERING_BASICS-A.json` | PENDING_FULL_REVIEW |
| 570 | `CLM-FOUNDATION_ENGINEERING_BASICS-B` | `CONTENT/vertical-slices/foundation-engineering-basics/records/CLM-FOUNDATION_ENGINEERING_BASICS-B.json` | PENDING_FULL_REVIEW |
| 571 | `CLM-FOUNDATION_ENGINEERING_BASICS-C` | `CONTENT/vertical-slices/foundation-engineering-basics/records/CLM-FOUNDATION_ENGINEERING_BASICS-C.json` | PENDING_FULL_REVIEW |
| 572 | `CLM-GAME_THEORY_BASICS-A` | `CONTENT/vertical-slices/game-theory-basics/records/CLM-GAME_THEORY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 573 | `CLM-GAME_THEORY_BASICS-B` | `CONTENT/vertical-slices/game-theory-basics/records/CLM-GAME_THEORY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 574 | `CLM-GAME_THEORY_BASICS-C` | `CONTENT/vertical-slices/game-theory-basics/records/CLM-GAME_THEORY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 578 | `CLM-GENERATOR-REFUEL-COOL` | `CONTENT/vertical-slices/generator-carbon-monoxide-safety/records/CLM-GENERATOR-REFUEL-COOL.json` | PENDING_FULL_REVIEW |
| 579 | `CLM-GENETIC_ENGINEERING_BASICS-A` | `CONTENT/vertical-slices/genetic-engineering-basics/records/CLM-GENETIC_ENGINEERING_BASICS-A.json` | PENDING_FULL_REVIEW |
| 580 | `CLM-GENETIC_ENGINEERING_BASICS-B` | `CONTENT/vertical-slices/genetic-engineering-basics/records/CLM-GENETIC_ENGINEERING_BASICS-B.json` | PENDING_FULL_REVIEW |
| 581 | `CLM-GENETIC_ENGINEERING_BASICS-C` | `CONTENT/vertical-slices/genetic-engineering-basics/records/CLM-GENETIC_ENGINEERING_BASICS-C.json` | PENDING_FULL_REVIEW |
| 582 | `CLM-GENETICS_BASICS-A` | `CONTENT/vertical-slices/genetics-basics/records/CLM-GENETICS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 583 | `CLM-GENETICS_BASICS-B` | `CONTENT/vertical-slices/genetics-basics/records/CLM-GENETICS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 584 | `CLM-GENETICS_BASICS-C` | `CONTENT/vertical-slices/genetics-basics/records/CLM-GENETICS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 585 | `CLM-GENOMICS_BASICS-A` | `CONTENT/vertical-slices/genomics-basics/records/CLM-GENOMICS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 586 | `CLM-GENOMICS_BASICS-B` | `CONTENT/vertical-slices/genomics-basics/records/CLM-GENOMICS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 587 | `CLM-GENOMICS_BASICS-C` | `CONTENT/vertical-slices/genomics-basics/records/CLM-GENOMICS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 588 | `CLM-GEOCHEMISTRY_BASICS-A` | `CONTENT/vertical-slices/geochemistry-basics/records/CLM-GEOCHEMISTRY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 589 | `CLM-GEOCHEMISTRY_BASICS-B` | `CONTENT/vertical-slices/geochemistry-basics/records/CLM-GEOCHEMISTRY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 590 | `CLM-GEOCHEMISTRY_BASICS-C` | `CONTENT/vertical-slices/geochemistry-basics/records/CLM-GEOCHEMISTRY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 591 | `CLM-GEODESY_BASICS-A` | `CONTENT/vertical-slices/geodesy-basics/records/CLM-GEODESY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 592 | `CLM-GEODESY_BASICS-B` | `CONTENT/vertical-slices/geodesy-basics/records/CLM-GEODESY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 593 | `CLM-GEODESY_BASICS-C` | `CONTENT/vertical-slices/geodesy-basics/records/CLM-GEODESY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 594 | `CLM-GEOGRAPHIC_COORDINATES_BASICS-A` | `CONTENT/vertical-slices/geographic-coordinates-basics/records/CLM-GEOGRAPHIC_COORDINATES_BASICS-A.json` | PENDING_FULL_REVIEW |
| 595 | `CLM-GEOGRAPHIC_COORDINATES_BASICS-B` | `CONTENT/vertical-slices/geographic-coordinates-basics/records/CLM-GEOGRAPHIC_COORDINATES_BASICS-B.json` | PENDING_FULL_REVIEW |
| 596 | `CLM-GEOGRAPHIC_COORDINATES_BASICS-C` | `CONTENT/vertical-slices/geographic-coordinates-basics/records/CLM-GEOGRAPHIC_COORDINATES_BASICS-C.json` | PENDING_FULL_REVIEW |
| 597 | `CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-A` | `CONTENT/vertical-slices/geographic-information-systems-basics/records/CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 598 | `CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-B` | `CONTENT/vertical-slices/geographic-information-systems-basics/records/CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 599 | `CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-C` | `CONTENT/vertical-slices/geographic-information-systems-basics/records/CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 600 | `CLM-GEOLOGIC_MAPPING_BASICS-A` | `CONTENT/vertical-slices/geologic-mapping-basics/records/CLM-GEOLOGIC_MAPPING_BASICS-A.json` | PENDING_FULL_REVIEW |
| 601 | `CLM-GEOLOGIC_MAPPING_BASICS-B` | `CONTENT/vertical-slices/geologic-mapping-basics/records/CLM-GEOLOGIC_MAPPING_BASICS-B.json` | PENDING_FULL_REVIEW |
| 602 | `CLM-GEOLOGIC_MAPPING_BASICS-C` | `CONTENT/vertical-slices/geologic-mapping-basics/records/CLM-GEOLOGIC_MAPPING_BASICS-C.json` | PENDING_FULL_REVIEW |
| 603 | `CLM-GEOLOGY_BASICS-A` | `CONTENT/vertical-slices/geology-basics/records/CLM-GEOLOGY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 604 | `CLM-GEOLOGY_BASICS-B` | `CONTENT/vertical-slices/geology-basics/records/CLM-GEOLOGY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 605 | `CLM-GEOLOGY_BASICS-C` | `CONTENT/vertical-slices/geology-basics/records/CLM-GEOLOGY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 606 | `CLM-GEOMETRY_BASICS-A` | `CONTENT/vertical-slices/geometry-basics/records/CLM-GEOMETRY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 607 | `CLM-GEOMETRY_BASICS-B` | `CONTENT/vertical-slices/geometry-basics/records/CLM-GEOMETRY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 608 | `CLM-GEOMETRY_BASICS-C` | `CONTENT/vertical-slices/geometry-basics/records/CLM-GEOMETRY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 609 | `CLM-GEOMORPHOLOGY_BASICS-A` | `CONTENT/vertical-slices/geomorphology-basics/records/CLM-GEOMORPHOLOGY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 610 | `CLM-GEOMORPHOLOGY_BASICS-B` | `CONTENT/vertical-slices/geomorphology-basics/records/CLM-GEOMORPHOLOGY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 611 | `CLM-GEOMORPHOLOGY_BASICS-C` | `CONTENT/vertical-slices/geomorphology-basics/records/CLM-GEOMORPHOLOGY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 612 | `CLM-GEOPHYSICS_BASICS-A` | `CONTENT/vertical-slices/geophysics-basics/records/CLM-GEOPHYSICS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 613 | `CLM-GEOPHYSICS_BASICS-B` | `CONTENT/vertical-slices/geophysics-basics/records/CLM-GEOPHYSICS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 614 | `CLM-GEOPHYSICS_BASICS-C` | `CONTENT/vertical-slices/geophysics-basics/records/CLM-GEOPHYSICS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 615 | `CLM-GEOSPATIAL_ANALYSIS_BASICS-A` | `CONTENT/vertical-slices/geospatial-analysis-basics/records/CLM-GEOSPATIAL_ANALYSIS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 616 | `CLM-GEOSPATIAL_ANALYSIS_BASICS-B` | `CONTENT/vertical-slices/geospatial-analysis-basics/records/CLM-GEOSPATIAL_ANALYSIS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 617 | `CLM-GEOSPATIAL_ANALYSIS_BASICS-C` | `CONTENT/vertical-slices/geospatial-analysis-basics/records/CLM-GEOSPATIAL_ANALYSIS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 618 | `CLM-GEOTECHNICAL_ENGINEERING_BASICS-A` | `CONTENT/vertical-slices/geotechnical-engineering-basics/records/CLM-GEOTECHNICAL_ENGINEERING_BASICS-A.json` | PENDING_FULL_REVIEW |
| 619 | `CLM-GEOTECHNICAL_ENGINEERING_BASICS-B` | `CONTENT/vertical-slices/geotechnical-engineering-basics/records/CLM-GEOTECHNICAL_ENGINEERING_BASICS-B.json` | PENDING_FULL_REVIEW |
| 620 | `CLM-GEOTECHNICAL_ENGINEERING_BASICS-C` | `CONTENT/vertical-slices/geotechnical-engineering-basics/records/CLM-GEOTECHNICAL_ENGINEERING_BASICS-C.json` | PENDING_FULL_REVIEW |
| 621 | `CLM-GOVERNANCE_BASICS-A` | `CONTENT/vertical-slices/governance-basics/records/CLM-GOVERNANCE_BASICS-A.json` | PENDING_FULL_REVIEW |
| 622 | `CLM-GOVERNANCE_BASICS-B` | `CONTENT/vertical-slices/governance-basics/records/CLM-GOVERNANCE_BASICS-B.json` | PENDING_FULL_REVIEW |
| 623 | `CLM-GOVERNANCE_BASICS-C` | `CONTENT/vertical-slices/governance-basics/records/CLM-GOVERNANCE_BASICS-C.json` | PENDING_FULL_REVIEW |
| 624 | `CLM-GRAPH_THEORY_BASICS-A` | `CONTENT/vertical-slices/graph-theory-basics/records/CLM-GRAPH_THEORY_BASICS-A.json` | PENDING_FULL_REVIEW |
| 625 | `CLM-GRAPH_THEORY_BASICS-B` | `CONTENT/vertical-slices/graph-theory-basics/records/CLM-GRAPH_THEORY_BASICS-B.json` | PENDING_FULL_REVIEW |
| 626 | `CLM-GRAPH_THEORY_BASICS-C` | `CONTENT/vertical-slices/graph-theory-basics/records/CLM-GRAPH_THEORY_BASICS-C.json` | PENDING_FULL_REVIEW |
| 627 | `CLM-GROUNDWATER_BASICS-A` | `CONTENT/vertical-slices/groundwater-basics/records/CLM-GROUNDWATER_BASICS-A.json` | PENDING_FULL_REVIEW |
| 628 | `CLM-GROUNDWATER_BASICS-B` | `CONTENT/vertical-slices/groundwater-basics/records/CLM-GROUNDWATER_BASICS-B.json` | PENDING_FULL_REVIEW |
| 629 | `CLM-GROUNDWATER_BASICS-C` | `CONTENT/vertical-slices/groundwater-basics/records/CLM-GROUNDWATER_BASICS-C.json` | PENDING_FULL_REVIEW |
| 630 | `CLM-TOOL-DEFECTIVE` | `CONTENT/vertical-slices/hand-tool-safety/records/CLM-TOOL-DEFECTIVE.json` | PENDING_FULL_REVIEW |
| 631 | `CLM-TOOL-INSPECT` | `CONTENT/vertical-slices/hand-tool-safety/records/CLM-TOOL-INSPECT.json` | PENDING_FULL_REVIEW |
| 632 | `CLM-TOOL-PPE` | `CONTENT/vertical-slices/hand-tool-safety/records/CLM-TOOL-PPE.json` | PENDING_FULL_REVIEW |
| 633 | `CLM-HEALTH_ECONOMICS_BASICS-A` | `CONTENT/vertical-slices/health-economics-basics/records/CLM-HEALTH_ECONOMICS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 634 | `CLM-HEALTH_ECONOMICS_BASICS-B` | `CONTENT/vertical-slices/health-economics-basics/records/CLM-HEALTH_ECONOMICS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 635 | `CLM-HEALTH_ECONOMICS_BASICS-C` | `CONTENT/vertical-slices/health-economics-basics/records/CLM-HEALTH_ECONOMICS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 636 | `CLM-HEALTH_SYSTEMS_BASICS-A` | `CONTENT/vertical-slices/health-systems-basics/records/CLM-HEALTH_SYSTEMS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 637 | `CLM-HEALTH_SYSTEMS_BASICS-B` | `CONTENT/vertical-slices/health-systems-basics/records/CLM-HEALTH_SYSTEMS_BASICS-B.json` | PENDING_FULL_REVIEW |
| 638 | `CLM-HEALTH_SYSTEMS_BASICS-C` | `CONTENT/vertical-slices/health-systems-basics/records/CLM-HEALTH_SYSTEMS_BASICS-C.json` | PENDING_FULL_REVIEW |
| 639 | `CLM-M4-HEALTH-RESILIENCE-A` | `CONTENT/vertical-slices/health-systems-basics/records/CLM-M4-HEALTH-RESILIENCE-A.json` | PENDING_FULL_REVIEW |
| 640 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A` | `CONTENT/vertical-slices/health-technology-assessment-basics/records/CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A.json` | PENDING_FULL_REVIEW |
| 641 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B` | `CONTENT/vertical-slices/health-technology-assessment-basics/records/CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B.json` | PENDING_FULL_REVIEW |
| 642 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C` | `CONTENT/vertical-slices/health-technology-assessment-basics/records/CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C.json` | PENDING_FULL_REVIEW |
| 643 | `CLM-HEAT_TRANSFER_BASICS-A` | `CONTENT/vertical-slices/heat-transfer-basics/records/CLM-HEAT_TRANSFER_BASICS-A.json` | PENDING_FULL_REVIEW |
| 644 | `CLM-HEAT_TRANSFER_BASICS-B` | `CONTENT/vertical-slices/heat-transfer-basics/records/CLM-HEAT_TRANSFER_BASICS-B.json` | PENDING_FULL_REVIEW |
| 645 | `CLM-HEAT_TRANSFER_BASICS-C` | `CONTENT/vertical-slices/heat-transfer-basics/records/CLM-HEAT_TRANSFER_BASICS-C.json` | PENDING_FULL_REVIEW |
| 646 | `CLM-HISTORICAL_GEOGRAPHY-A` | `CONTENT/vertical-slices/historical-geography-basics/records/CLM-HISTORICAL_GEOGRAPHY-A.json` | PENDING_FULL_REVIEW |
| 647 | `CLM-HISTORICAL_GEOGRAPHY-B` | `CONTENT/vertical-slices/historical-geography-basics/records/CLM-HISTORICAL_GEOGRAPHY-B.json` | PENDING_FULL_REVIEW |
| 648 | `CLM-HISTORICAL_GEOGRAPHY-C` | `CONTENT/vertical-slices/historical-geography-basics/records/CLM-HISTORICAL_GEOGRAPHY-C.json` | PENDING_FULL_REVIEW |
| 649 | `CLM-HISTORY_METHODS_BASICS-A` | `CONTENT/vertical-slices/history-methods-basics/records/CLM-HISTORY_METHODS_BASICS-A.json` | PENDING_FULL_REVIEW |
| 650 | `CLM-HISTORY_METHODS_BASICS-B` | `CONTENT/vertical-slices/history-methods-basics/records/CLM-HISTORY_METHODS_BASICS-B.json` | PENDING_FULL_REVIEW |

## Initial source-fit findings (triage only; no canonical JSON changed)

Detailed scoring and source-fit notes for row 541 and rows 552–554 are recorded in [Batch 13 source-fit review checkpoint](M13-CLAIM-REVIEW-BATCH-13-SOURCE-FIT-TRIAGE-ROWS-541-554-2026-10-11.md). A second checkpoint reviews rows 555–562: [food security and food systems](M13-CLAIM-REVIEW-BATCH-13-SOURCE-FIT-TRIAGE-ROWS-555-562-2026-10-11.md). A third checkpoint reviews rows 563–565: [forestry basics](M13-CLAIM-REVIEW-BATCH-13-SOURCE-FIT-TRIAGE-ROWS-563-565-2026-10-11.md).

1. **CLM-FOOD_DISTRIBUTION_BASICS-D** (row 541): Claim provenance and its Evidence Use consistently point to `SRC-FOOD_DISTRIBUTION_WFP`, whose source record exists and identifies the World Food Programme 2024 procurement infographics (`https://www.wfp.org/publications/2024-procurement-infographics`). A separate `SRC-FOOD_DISTRIBUTION_BASICS.json` record points to FAO and is not the referenced source for this Claim. The structural reference chain is therefore present; the substantive source-fit remains unresolved because the WFP locator is procurement-focused while the Claim also asserts storage, transport, and delivery through final points, and the Evidence Use description supplies no pinpoint. Do not score E as adequate until the source's relevant content and scope are verified.

2. **CLM-FOOD_SCIENCE_BASICS-A/B/C** (rows 552–554): all three Claims use the same `SRC-FOOD_SCIENCE_BASICS` locator, labelled “OpenStax — Food Science,” while its URI resolves to *Biology 2e: Nutrition and Energy Production*. The claim statements are generic editorial/methodological assertions about a slice, source/context limitations, and need for specialized review, not clearly claims about nutrition and energy production. Their linked Evidence Use descriptions are boilerplate (“the indicated source is used within the stated material”) and have no quoted/pinpointed support. Flag source identity/fit and possible claim-type mismatch for human adjudication; do not treat these as evidence-supported merely because the structural refs exist.

3. **CLM-FOOD_FERMENTATION_BASICS-A/B/C** (rows 542–544): a separate initial checkpoint contains provisional D/E/B estimates and an FAO chapter locator. These three reviews remain provisional: pinpoint and wording follow-up is still required, especially for Claim B's “different processes” wording. See [initial checkpoint](M13-CLAIM-REVIEW-BATCH-13-INITIAL-CHECKPOINT-FOOD-FERMENTATION-2026-10-11.md).

## Guardrails

- No canonical Claim/Evidence Use/Source JSON modified.
- No scores were written into the inventory or canonical records.
- Batch 13 is **not complete** until all 100 selected candidates have individual evidence-fit, source-trail, duplicate, and D/E/B review recorded, with unresolved cases explicitly flagged rather than silently accepted.
- Draft PR only; do not merge, publish, or modify `main`.
