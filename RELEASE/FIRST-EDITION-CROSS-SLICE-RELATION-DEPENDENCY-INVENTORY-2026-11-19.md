# First Edition — Cross-Slice Relation Dependency Inventory

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `cd6ce793d4e2d540b5167c272a84f702d85686ff`  
Status: **63/63 RELATIONS INVENTORIED; 126/126 PARTICIPANT REFERENCES EXACT-VERIFIED; 63/63 SEMANTICALLY REVIEWED; 0 RELATION SEMANTICS OPEN**

## Scope and rules

This is a separate inventory of canonical `relation` records. Relations are not included in the 809-row vertical-slice candidate denominator. This file records exact relation versions and declared participants/frame references; path existence is not proof of participant version correctness, semantic validity, or release eligibility.

- No Relation, Claim, Evidence Use, Source, Context or Scope record is modified.
- All existing HOLD decisions remain unchanged.
- Relation dependencies must be resolved to exact participant record IDs and versions before any candidate allowlist is considered.

## Exact relation records

| Relation/version | Relation type | Declared participants (path lookup only) | Frame reference | Canonical path |
|---|---|---|---|---|
| `REL-CROSS-LIGHTING-HOME-FIRE@1` | temporary_lighting_and_home_fire_safety | CLM-LIGHTING-FLASHLIGHT-OUTAGE@1; CLM-HOME-FIRE-LEAVE-STAY-OUT@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LIGHTING-HOME-FIRE.json |
| `REL-CROSS-AIR-POWER-SYSTEMS@1` | air_quality_and_energy_systems_link | CLM-AIR_QUALITY_BASICS-A@1 [path]; CLM-POWER_SYSTEMS_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-AIR-POWER-SYSTEMS.json |
| `REL-CROSS-ALERTS-WILDFIRE-SMOKE@1` | public_alerts_and_wildfire_smoke_response | CLM-ALERTS-ENABLE-RESPOND@1 [path]; CLM-WILDFIRE-AIR-QUALITY@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-ALERTS-WILDFIRE-SMOKE.json |
| `REL-CROSS-AMR-PLANT-HEALTH@1` | one_health_plant_health_link | CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1 [path]; CLM-PLANT_PATHOLOGY_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-AMR-PLANT-HEALTH.json |
| `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@2` | shared_spatial_representation_context | CLM-CARTOGRAPHY-A@2 [path]; CLM-SETTLEMENT_GEOGRAPHY-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY.json |
| `REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE@1` | adaptation_resilience_planning_link | CLM-CLIMATE_ADAPTATION-C@1 [path]; CLM-INFRASTRUCTURE_RESILIENCE-C@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE.json |
| `REL-CROSS-CO-EMERGENCY-ESCALATION@1` | shared_carbon_monoxide_emergency_escalation | CLM-CO-HEATING-EMERGENCY@1 [path]; CLM-GENERATOR-CO-ALARM-EMERGENCY@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-EMERGENCY-ESCALATION.json |
| `REL-CROSS-CO-PREVENTION@1` | shared_carbon_monoxide_prevention | CLM-GENERATOR-OUTSIDE-20FT@1 [path]; CLM-CO-HEATING-OUTSIDE@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-PREVENTION.json |
| `REL-CROSS-GEODESY-SURVEYING@1` | shared_spatial_measurement_foundation | CLM-GEODESY_BASICS-B@1 [path]; CLM-SURVEYING_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-GEODESY-SURVEYING.json |
| `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1` | subsurface_water_and_soil_biology_link | CLM-GROUNDWATER_BASICS-A@1 [path]; CLM-SOIL_MICROBIOLOGY_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY.json |
| `REL-CROSS-HISTORY-GEOGRAPHY-ECONOMIC-HISTORY@1` | shared_spatiotemporal_analysis_context | CLM-HISTORICAL_GEOGRAPHY-A@1 [path]; CLM-ECONOMIC_HISTORY-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-HISTORY-GEOGRAPHY-ECONOMIC-HISTORY.json |
| `REL-CROSS-HOME-FIRE-ALERTS@1` | emergency_warning_and_home_fire_response | CLM-HOME-FIRE-LEAVE-STAY-OUT@1 [path]; CLM-ALERTS-ENABLE-RESPOND@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-HOME-FIRE-ALERTS.json |
| `REL-CROSS-INDUSTRIAL-PROCUREMENT@1` | systems_and_procurement_link | CLM-INDUSTRIAL_ENGINEERING_BASICS-A@1 [path]; CLM-PUBLIC_PROCUREMENT_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-INDUSTRIAL-PROCUREMENT.json |
| `REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY@2` | labor_and_social_protection_measurement_link | CLM-LABOR_ECONOMICS_BASICS-C@1 [path]; CLM-SOCIAL_POLICY_BASICS-C@2 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY.json |
| `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3` | shared_information_preservation_context | CLM-LIBRARY_SCIENCE-A@2 [path]; CLM-ARCHIVAL_SCIENCE-A@2 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION.json |
| `REL-CROSS-DISASTER-BUILDING-SERVICES@1` | recovery_and_building_systems_link | CLM-DISASTER_RECOVERY_BASICS-A@1; CLM-BUILDING_SERVICES_ENGINEERING_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-DISASTER-BUILDING-SERVICES.json |
| `REL-CROSS-EARTHQUAKE-AFTERSHOCK@1` | subsequent_hazard_context | EVT-EARTHQUAKE-SHAKING@1; CLM-AFTERSHOCK-EXPECT@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-EARTHQUAKE-AFTERSHOCK.json |
| `REL-CROSS-ETHNOBOTANY-AGRIFOOD@1` | plant_knowledge_and_food_systems_link | CLM-ETHNOBOTANY_BASICS-B@1; CLM-AGRIFOOD_SYSTEMS_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-ETHNOBOTANY-AGRIFOOD.json |
| `REL-CROSS-FLOOD-HAZARDOUS-WASTE@1` | flood_cleanup_and_hazardous_waste_boundary | CLM-FLOOD-REENTRY-HAZARD-ESCALATION@1; CLM-WASTE-HAZARDOUS-ESCALATION@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FLOOD-HAZARDOUS-WASTE.json |
| `REL-CROSS-FLOOD-SAFETY@1` | shared_flood_cleanup_context | CLM-FLOOD-FOOD-CONTACT@1; CLM-FLOOD-CLEAN-PROTECT@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FLOOD-SAFETY.json |
| `REL-CROSS-FOOD-DISTRIBUTION-LOGISTICS@1` | food_distribution_and_humanitarian_logistics_link | CLM-FOOD_DISTRIBUTION_BASICS-D@1; CLM-HUMANITARIAN_LOGISTICS_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FOOD-DISTRIBUTION-LOGISTICS.json |
| `REL-CROSS-FOOD-PUBLIC-HEALTH@1` | food_security_and_population_health_link | CLM-FOOD_SECURITY_BASICS-D@1; CLM-PUBLIC_HEALTH_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FOOD-PUBLIC-HEALTH.json |
| `REL-CROSS-M2-AGRICULTURE-SOIL@1` | agriculture_and_soil_dependency | CLM-AGRICULTURE_BASICS-B@1; CLM-SOIL_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-AGRICULTURE-SOIL.json |
| `REL-CROSS-M2-ENERGY-SECURITY-RESILIENCE@1` | energy_security_and_infrastructure_resilience_link | CLM-ENERGY_SECURITY_BASICS-A@1; CLM-INFRASTRUCTURE_RESILIENCE-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-ENERGY-SECURITY-RESILIENCE.json |
| `REL-CROSS-M2-GEOGRAPHIC-COORDINATES-GEODESY@1` | geographic_coordinates_and_geodesy_link | CLM-GEOGRAPHIC_COORDINATES_BASICS-C@1; CLM-GEODESY_BASICS-B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-GEOGRAPHIC-COORDINATES-GEODESY.json |
| `REL-CROSS-M2-MEASUREMENT-UNCERTAINTY-SCIENCE@1` | measurement_uncertainty_and_measurement_science_link | CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1; CLM-MEASUREMENT_SCIENCE_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-MEASUREMENT-UNCERTAINTY-SCIENCE.json |
| `REL-CROSS-M2-RISK-MANAGEMENT-ANALYSIS@1` | risk_management_and_risk_analysis_link | CLM-RISK_MANAGEMENT_BASICS-B@1; CLM-RISK_ANALYSIS_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-RISK-MANAGEMENT-ANALYSIS.json |
| `REL-CROSS-M2-STATISTICS-RESEARCH@1` | statistics_and_research_design_link | CLM-STATISTICS_BASICS-C@1; CLM-RESEARCH_METHODS_BASICS-B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-STATISTICS-RESEARCH.json |
| `REL-CROSS-MATH-ENGINEERING-HISTORY@3` | shared_history_of_technical_knowledge_context | CLM-HISTORY_OF_MATHEMATICS-A@2; CLM-HISTORY_OF_ENGINEERING-A@2 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MATH-ENGINEERING-HISTORY.json |
| `REL-CROSS-MANUFACTURING-HUMAN-FACTORS@1` | manufacturing_and_human_factors_link | CLM-MANUFACTURING_PROCESSES_BASICS-B@1; CLM-HUMAN_FACTORS_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MANUFACTURING-HUMAN-FACTORS.json |
| `REL-CROSS-MEASUREMENT-CALIBRATION@1` | measurement_and_calibration_link | CLM-MEASUREMENT_SCIENCE_BASICS-A@1; CLM-CALIBRATION_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MEASUREMENT-CALIBRATION.json |
| `REL-CROSS-MECHANICAL-METALLURGY@1` | same_engineering_material_system | CLM-MECHANICAL_ENGINEERING_BASICS-A@1; CLM-METALLURGY_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MECHANICAL-METALLURGY.json |
| `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2` | migration_and_labor_measurement_link | CLM-MIGRATION_AND_MOBILITY_BASICS-C@2; CLM-LABOR_ECONOMICS_BASICS-C@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MIGRATION-LABOR-ECONOMICS.json |
| `REL-CROSS-PLANTPATH-ENTOMOLOGY@1` | plant_health_and_insect_ecology_link | CLM-PLANT_PATHOLOGY_BASICS-A@1; CLM-ENTOMOLOGY_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-PLANTPATH-ENTOMOLOGY.json |
| `REL-CROSS-POLITICAL-ECONOMY-TAXATION@2` | institutional_economic_policy_link | CLM-POLITICAL_ECONOMY_BASICS-B@2; CLM-TAXATION_BASICS-B@2 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-POLITICAL-ECONOMY-TAXATION.json |
| `REL-CROSS-QUANTUM-MEASUREMENT@1` | quantum_and_measurement_link | CLM-QUANTUM_MECHANICS_BASICS-A@1; CLM-MEASUREMENT_SCIENCE_BASICS-B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-QUANTUM-MEASUREMENT.json |
| `REL-CROSS-RESEARCH-STATISTICS@1` | research_and_statistical_inference_link | CLM-RESEARCH_METHODS_BASICS-B@1; CLM-STATISTICS_INFERENCE_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-RESEARCH-STATISTICS.json |
| `REL-CROSS-SANITATION-HYGIENE@1` | hygiene_control_after_waste_contact | CLM-WASTE-HAND-HYGIENE@1; CLM-HANDWASH-20SEC@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SANITATION-HYGIENE.json |
| `REL-CROSS-SANITATION-WASTEWATER@1` | sanitation_wastewater_service_chain | CLM_SANITATION_BASICS_A@1; CLM-WASTEWATER_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SANITATION-WASTEWATER.json |
| `REL-CROSS-SEPTIC-FLOOD-SANITATION@1` | flooded_septic_and_cleanup_sanitation | CLM-SEPTIC-FLOOD-NO-PUMP@1; CLM-FLOOD-CLEAN-PROTECT@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SEPTIC-FLOOD-SANITATION.json |
| `REL-CROSS-SETTLEMENT-ENERGY@1` | settlement_energy_system_dependency | CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1; CLM_ENERGY_SYSTEMS_BASICS_A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-ENERGY.json |
| `REL-CROSS-SETTLEMENT-HOUSING@1` | settlement_housing_system_dependency | CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1; CLM-HOUSING_SYSTEMS_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-HOUSING.json |
| `REL-CROSS-SETTLEMENT-INFRASTRUCTURE@1` | settlement_infrastructure_system_dependency | CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1; CLM-INFRASTRUCTURE_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-INFRASTRUCTURE.json |
| `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1` | settlement_public_health_system_link | CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C@1; CLM-PUBLIC_HEALTH_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-PUBLIC-HEALTH.json |
| `REL-CROSS-SETTLEMENT-TRANSPORTATION@1` | settlement_transportation_system_dependency | CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1; CLM-TRANSPORTATION_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-TRANSPORTATION.json |
| `REL-CROSS-STANDARDS-QUALITY@1` | standards_and_quality_link | CLM-STANDARDS_AND_CERTIFICATION_BASICS-A@1; CLM-QUALITY_MANAGEMENT_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-STANDARDS-QUALITY.json |
| `REL-CROSS-WATER-CHEMICAL@1` | same_water_safety_boundary | CLM-WATER-CHEMICAL-LIMIT@1; CLM-CHEM-WATER-NO-BOIL@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-CHEMICAL.json |
| `REL-CROSS-WATER-CLIMATE-ADAPTATION@1` | shared_water_climate_risk_context | CLM-WATER_SECURITY-C@1; CLM-CLIMATE_ADAPTATION-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-CLIMATE-ADAPTATION.json |
| `REL-CROSS-WATER-FILTER@1` | complementary_water_treatment_limits | CLM-WATER-FILTER-LIMITS@1; CLM-WATER-BOILING-EFFECTIVE@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-FILTER.json |
| `REL-CROSS-WATER-QUALITY-TREATMENT@1` | water_quality_guides_treatment_selection | CLM_WATER_QUALITY_WHO_A@1; CLM-WATER_TREATMENT_BASICS-B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-QUALITY-TREATMENT.json |
| `REL-P11-CONSTRUCTION-SAFETY-ENGINEERING@1` | construction_safety_and_safety_engineering_link | CLM-CONSTRUCTION_SAFETY_BASICS-A@1; CLM-SAFETY_ENGINEERING_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-CONSTRUCTION-SAFETY-ENGINEERING.json |
| `REL-P11-INFORMATION-CRITICAL-THINKING@1` | information_literacy_and_critical_thinking_link | CLM-INFORMATION_LITERACY_BASICS-B@1; CLM-CRITICAL_THINKING_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-INFORMATION-CRITICAL-THINKING.json |
| `REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@1` | infrastructure_resilience_and_systems_thinking_link | CLM-INFRASTRUCTURE_RESILIENCE-A@1; CLM-SYSTEMS_THINKING_BASICS-B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING.json |
| `REL-P11-RISK-COMMUNICATION@1` | risk_analysis_and_public_risk_communication_link | CLM-RISK_ANALYSIS_BASICS-B@1; CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-RISK-COMMUNICATION.json |
| `REL-P11-RISK-SYSTEMS-THINKING@1` | risk_analysis_and_systems_thinking_link | CLM-RISK_ANALYSIS_BASICS-A@1; CLM-SYSTEMS_THINKING_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-RISK-SYSTEMS-THINKING.json |
| `REL-CONTAINER-WATER-STORAGE@1` | storage_container_for | ST-WATER-CONTAINER-SANITIZED@1; ST-WATER-CONTAINER-STORED@1 | `CTX-WATER-STORAGE-EMERGENCY@1` | CONTENT/vertical-slices/emergency-water-storage-state/records/REL-CONTAINER-WATER-STORAGE.json |
| `REL_M3_FIRE_SAFETY_EMERGENCY_MANAGEMENT@1` | fire_safety_and_emergency_management_link | CLM_FIRE_SAFETY_BASICS_B@1; CLM-EMERGENCY_MANAGEMENT_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/fire-safety-basics/records/REL-M3-FIRE-SAFETY-EMERGENCY-MANAGEMENT.json |
| `REL_M3_FOOD_PRESERVATION_SAFETY@1` | food_preservation_and_food_safety_link | CLM-FOOD_PRESERVATION_BASICS-B@1; CLM-FOOD_SAFETY_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/food-preservation-basics/records/REL-M3-FOOD-PRESERVATION-SAFETY.json |
| `REL_M3_SCIENTIFIC_METHOD_RESEARCH@1` | scientific_method_and_research_methods_link | CLM_SCIENTIFIC_METHOD_BASICS_D@1; CLM-RESEARCH_METHODS_BASICS-B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/scientific-method-basics/records/REL-M3-SCIENTIFIC-METHOD-RESEARCH.json |
| `REL_M3_SHELTER_SETTLEMENT@1` | shelter_and_settlement_systems_link | CLM-SHELTER_BASICS-A@1; CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/shelter-basics/records/REL-M3-SHELTER-SETTLEMENT.json |
| `REL_M3_WATER_RESOURCES_HYDROLOGY@1` | water_resources_and_hydrology_link | CLM_WATER_RESOURCES_BASICS_B@1; CLM-HYDROLOGY_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/water-resources-basics/records/REL-M3-WATER-RESOURCES-HYDROLOGY.json |
| `REL-CROSS-SETTLEMENT-WATER@1` | settlement_water_infrastructure_dependency | CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1; CLM-WATER_INFRASTRUCTURE_BASICS-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-WATER.json |
| `REL_M3_EMERGENCY_INFRASTRUCTURE@1` | emergency_management_and_infrastructure_resilience_link | CLM-EMERGENCY_MANAGEMENT_BASICS-A@1; CLM-INFRASTRUCTURE_RESILIENCE-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/emergency-management-basics/records/REL-M3-EMERGENCY-INFRASTRUCTURE.json |

## Inventory completion

- All 63 canonical relation JSON files in the repository tree are represented exactly once in this inventory.
- Exact relation IDs, versions, relation types, participant IDs/versions, frame references and canonical paths have been extracted.
- Filename presence is only a locator check. Participant `record_id`, version, type and relation endpoint eligibility still require canonical content verification.

## Current batch

- Canonical relation JSON files discovered in the repository tree: 63.
- Relation records inventoried so far: 63.
- Participant references are listed verbatim; bracketed path markers only indicate a matching filename exists somewhere in the corpus tree.
- Remaining relation files: 0.

## Next

Continue semantic review of the 46 unreviewed Relations in bounded batches. Exact participant identity/version/type closure is complete (126/126 references); do not conflate that structural result with semantic validity or release eligibility.

## Candidate-endpoint canonical verification

Inspection HEAD: `8904471655b2db7192fd4806bc8c1465a6e4b538`.

- The 63 relation rows declare 126 participant references.
- 29 participant references resolve to the 99-slice Part II candidate set; these represent 25 unique exact-version Claim records.
- All 25 unique candidate Claim endpoints were fetched from canonical JSON at this HEAD. Every `record_id`, `record_version` and `record_type=claim` matched the declared relation participant.
- The shared frame `CTX-CROSS-SLICE-LINKAGE@1` was also fetched and verified as a Context record at this HEAD.
- The remaining 97 participant references point to other corpus slices. All 97 references / 82 unique exact-version IDs have now been fetched from canonical JSON at the current inspection HEAD; record ID, version and type match in every case. The 82 unique endpoints comprise 79 Claims, one Event and two State records. Semantic validity and release eligibility remain separate review tasks.
- The candidate master has since expanded to 119 Part II slices through prior-audit reuse. None of the 11 newly reused slices appears as a participant endpoint in these 63 Relations; the candidate intersection remains 29 references / 25 unique Claims, and the 97 other references remain outside the candidate set.

| Candidate endpoint | Slice | Canonical verification |
|---|---|---|
| `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` | `antimicrobial-resistance-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-PLANT_PATHOLOGY_BASICS-A@1` | `plant-pathology-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-CARTOGRAPHY-A@2` | `cartography-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-SETTLEMENT_GEOGRAPHY-A@1` | `settlement-geography-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-INFRASTRUCTURE_RESILIENCE-C@1` | `infrastructure-resilience-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-SOIL_MICROBIOLOGY_BASICS-A@1` | `soil-microbiology-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-HISTORICAL_GEOGRAPHY-A@1` | `historical-geography-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-LABOR_ECONOMICS_BASICS-C@1` | `labor-economics-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-SOCIAL_POLICY_BASICS-C@2` | `social-policy-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-LIBRARY_SCIENCE-A@2` | `library-science-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-ARCHIVAL_SCIENCE-A@2` | `archival-science-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-DISASTER_RECOVERY_BASICS-A@1` | `disaster-recovery-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-AGRIFOOD_SYSTEMS_BASICS-A@1` | `agrifood-systems-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-FOOD_DISTRIBUTION_BASICS-D@1` | `food-distribution-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-INFRASTRUCTURE_RESILIENCE-A@1` | `infrastructure-resilience-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | `measurement-uncertainty-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-STATISTICS_BASICS-C@1` | `statistics-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-HISTORY_OF_MATHEMATICS-A@2` | `history-of-mathematics-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-HISTORY_OF_ENGINEERING-A@2` | `history-of-engineering-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-MIGRATION_AND_MOBILITY_BASICS-C@2` | `migration-and-mobility-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-ENTOMOLOGY_BASICS-A@1` | `entomology-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-POLITICAL_ECONOMY_BASICS-B@2` | `political-economy-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-TAXATION_BASICS-B@2` | `taxation-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM-WATER_SECURITY-C@1` | `water-security-basics` | MATCH — canonical record_id, version and type=claim |
| `CLM_WATER_QUALITY_WHO_A@1` | `water-quality-basics` | MATCH — canonical record_id, version and type=claim |

This verification does not approve any relation for publication. All first-edition candidate decisions remain HOLD, and relation eligibility still depends on both endpoints' eventual disposition, source/evidence quality, relation semantics, and editorial review.


## Current-head participant closure — completed

Inspection HEAD: `c4fbc8d1d879ae0c14e2b0ceaba8899d4f6fef0d`.

- All 63 Relation records remain unchanged since their canonical inventory snapshot; the commit comparison from the original relation inspection HEAD showed no Relation JSON changes.
- The 29 participant references to the Part II candidate set map to 25 unique Claim endpoints. All 25 were previously fetched and matched exact canonical ID, version and type; the comparison from that verification HEAD to this inspection HEAD contains no canonical JSON changes.
- The two candidate Claims missing from the master register were independently re-fetched at the current PR HEAD and added to the master as HOLD: `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` and `CLM-STATISTICS_BASICS-C@1`.
- The other 97 participant references map to 82 unique exact-version records. All 82 were fetched at this inspection HEAD and matched their declared `record_id`, `record_version` and `record_type`: 79 Claims, one Event and two State records.
- Shared frame `CTX-CROSS-SLICE-LINKAGE@1` was re-fetched at this inspection HEAD and matched `record_type=context`.
- Result: **126/126 participant references resolve to canonical records with exact version and type.** Repeated references are retained as 126 edges; 107 distinct endpoint records are represented by the 25 candidate Claims plus 82 other unique records.

This closes canonical participant identity/version/type validation only. It does not approve the 63 Relations: relation semantics, directionality, role compatibility, endpoint substantive quality, candidate disposition, rights, editorial ownership and Human View remain open. No canonical JSON was changed and no relation was promoted to INCLUDE.


## Semantic review follow-up — Batch 1

Inspection at `6368903f471b85d6e22e3962f58074bb95368eb4`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH1-2026-11-19.md`.

- `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@2`: exact participant/source versions verified; accepted as contextual navigation only.
- `REL-CROSS-MATH-ENGINEERING-HISTORY@3`: exact participant/source versions verified; accepted as contextual navigation only.
- `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3`: exact participant/source versions verified; structurally valid but semantically weak for release navigation because the selected library Claim A is access-focused rather than preservation-specific. Retain HOLD for release use.

Cumulative semantic review: 3/63 Relations. The 97 participant references outside the Part II candidate set still require exact version/type and semantic review. No canonical Relation or endpoint record changed.


## Semantic review follow-up — Batch 2

Inspection at `80b4b11f7df2c193f365e8db660ab7f53076d305`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH2-2026-11-19.md`.

- Six additional Relation records were reviewed: lighting/home-fire, CO emergency escalation, CO prevention, home-fire/alerts, flood safety and alerts/wildfire smoke.
- Ten distinct participant Claims and nine unique provenance Sources were fetched and matched to exact version-1 IDs/types.
- Five Relations are accepted as contextual navigation only; the CO emergency pair remains HOLD for release use pending editorial review of substantial Claim overlap.
- Cumulative semantic review: 9/63 Relations. This does not close the separate non-candidate endpoint reconciliation; its remaining count must be recomputed only after exact overlap accounting.
- No canonical records or publication decisions changed.


## Semantic review follow-up — Batch 3

Inspection at `cd6ce793d4e2d540b5167c272a84f702d85686ff`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH3-2026-11-19.md`.

- Eight additional Relation records were reviewed: air/power systems, AMR/plant health, climate adaptation/infrastructure resilience, geodesy/surveying, groundwater/soil microbiology, historical geography/economic history, industrial engineering/procurement, and labor economics/social policy.
- Sixteen participant Claims and sixteen provenance Sources were fetched; all exact IDs, versions, and record types matched. Claim provenance Source identities match the Relation `created_from` entries for all 16 participants.
- Five Relations are defensible as contextual navigation only (two with explicit restrictions); three remain HOLD for release use because the endpoints do not establish the specific relationship stated.
- A cross-cutting frame issue was identified: `CTX-CROSS-SLICE-LINKAGE@1` has a `target_ref` specifically to `REL-CROSS-WATER-CHEMICAL@1`. Its applicability to all other Relations is therefore not established by the shared frame ID alone. This requires schema/Context-scope resolution before any linked Relation can be release-eligible.
- Cumulative semantic review: **17/63 Relations**. Remaining semantic review: **46/63**.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.


## Semantic review follow-up — Batch 4

Inspection at `81a2e174d69c206d8b2ade2b776479de8c23f84e`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH4-2026-11-19.md`.

- Eight additional Relation records were reviewed: flood/hazardous waste, food distribution/logistics, food/public health, agriculture/soil, energy security/resilience, geographic coordinates/geodesy, measurement uncertainty/metrology, and risk management/analysis.
- Sixteen participant Claims and sixteen provenance Source edges were fetched and checked; 15 unique Source records were involved because infrastructure resilience is shared by two Relations. Exact IDs, versions, types, and Claim-to-Relation source identity were checked.
- Seven Relations are defensible as contextual navigation only (one with an explicit restriction); one remains HOLD for release use because its public-health endpoint is too generic for the named food-security relationship.
- Cumulative semantic review: **25/63 Relations**. Remaining semantic review: **38/63**.
- The shared Context `target_ref` applicability ambiguity identified in Batch 3 remains unresolved and continues to block release eligibility.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.


## Semantic review follow-up — Batch 5

Inspection at `53aa8006f17e82122724c7d4831bf29a15fde07a`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH5-2026-11-19.md`.

- Eight additional Relations reviewed: statistics/research design, manufacturing/human factors, measurement/calibration, mechanical engineering/metallurgy, migration/labor economics, plant pathology/entomology, political economy/taxation, and quantum/measurement.
- Sixteen participant Claims and their 16 provenance Source references were fetched; 15 unique Source records were checked. Exact IDs, versions, and types match.
- Four Relations are defensible as contextual navigation only; four remain HOLD for release use because the selected endpoints are too generic or do not express the named link.
- A provenance-convention exception was found in `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2`: its `created_from` references the two participant Claims instead of their Source records. It is recorded as a blocker; canonical JSON was not modified.
- Cumulative semantic review: **33/63 Relations**. Remaining semantic review: **30/63**.
- The shared Context target-scope ambiguity remains unresolved.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.


## Semantic review follow-up — Batch 6

Inspection at `8121eec3dda995e8019f99ed547a5fa06ed31726`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH6-2026-11-19.md`.

- Eight additional Relations reviewed: research/statistics, sanitation/hygiene, sanitation/wastewater, septic/flood sanitation, and settlement links to energy, housing, infrastructure, and public health.
- All 16 participant references were fetched and matched exact canonical Claim IDs, versions, and types (14 unique Claims). Sixteen Claim provenance Source references were checked (13 unique Sources); all exact source identities and versions matched Relation provenance.
- Six Relations are defensible as contextual navigation only (one restricted); two remain HOLD for release use because the selected endpoints are too generic or do not state the named relationship.
- Cumulative semantic review: **41/63 Relations**. Remaining semantic review: **22/63**.
- The shared Context `target_ref` scope ambiguity remains unresolved.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.


## Semantic review follow-up — Batch 7

Inspection at `9711cc7cdd803d0aa30c7121ce00ec1e12a32a27`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH7-2026-11-19.md`.

- Eight additional Relations reviewed: settlement/transportation, standards/quality, water security/climate adaptation, water filter/boiling, water quality/treatment, construction safety/safety engineering, information literacy/critical thinking, and infrastructure resilience/systems thinking.
- Sixteen participant Claims and 16 distinct provenance Sources were fetched and checked; exact IDs, versions, types, and Claim-to-Relation source identity match.
- All eight are defensible as contextual navigation only, with explicit restrictions for the broad water/climate link, contaminant-specific water-treatment limits, and substantial information-literacy/critical-thinking overlap.
- Cumulative semantic review: **49/63 Relations**. Remaining semantic review: **14/63**.
- The shared Context target-scope ambiguity remains unresolved.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.


## Semantic review follow-up — Batch 8

Inspection at `e7fd4e81e7e7f520e5ec5bab2dda074a6472627f`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH8-2026-11-19.md`.

- Eight previously unreviewed Relations reviewed: disaster recovery/building services, earthquake/aftershock, ethnobotany/agrifood, risk communication, risk/systems thinking, container/water storage, fire safety/emergency management, and water chemical safety. The already-reviewed food/public-health Relation is noted only as a cross-check and is not counted again.
- Sixteen participant records were fetched and exact-checked: 13 Claims, 1 Event, and 2 State records. Fifteen provenance Source edges (14 unique Sources) were fetched and matched.
- Six Relations are acceptable as contextual navigation only (two with restrictions); two remain HOLD due to a generic, non-occurrence-specific Event endpoint and a misaligned State/Relation/Context model.
- The water-chemical Relation is a near-duplicate consistency link between two claims from the same institution; it is not independent corroboration.
- Cumulative semantic review: **57/63 Relations**. Remaining semantic review: **6/63**.
- The shared Context target-scope issue remains unresolved; the container-storage Context has a separate target mismatch.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.


## Final semantic review — Batch 9

Inspection at `35036ab0b5caf32c3bac2afb5c181bdf1f860587`; see `RELEASE/FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH9-2026-11-19.md`.

- Final six Relations reviewed: food preservation/safety, scientific method/research methods, shelter/settlement, water resources/hydrology, settlement/water infrastructure, and emergency management/infrastructure resilience.
- Twelve participant references (11 unique Claims) exact-verified. Thirteen Claim provenance Source edges (12 unique Source records) and twelve Relation provenance Source edges (11 unique Source records) were checked.
- All six are defensible as contextual navigation only. No Relation is approved for release.
- **Semantic audit complete: 63/63 Relations reviewed.** Across Batches 1–9: 49 contextual-navigation candidates; 14 remain HOLD for release use.
- No canonical Relation or endpoint record changed. No Claim or Relation was promoted to INCLUDE.

## Consolidated unresolved Relation blockers

1. `CTX-CROSS-SLICE-LINKAGE@1` target-scope ambiguity: `target_ref` names `REL-CROSS-WATER-CHEMICAL@1`, so applicability to the other Relations is not established.
2. `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2` provenance convention: `created_from` points to participant Claims rather than their Source records.
3. `REL-CROSS-EARTHQUAKE-AFTERSHOCK@1` Event endpoint is generic and lacks occurrence-specific time/location/identity.
4. `REL-CONTAINER-WATER-STORAGE@1` links two State records with a `storage_container_for` relation type while its Context targets a separate Claim.
5. Fourteen Relations remain semantic HOLD; none may be auto-promoted.
6. Independent gates remain: participant Claim eligibility, Evidence Use sufficiency, publication rights, editorial responsibility, and exact-head CI.
