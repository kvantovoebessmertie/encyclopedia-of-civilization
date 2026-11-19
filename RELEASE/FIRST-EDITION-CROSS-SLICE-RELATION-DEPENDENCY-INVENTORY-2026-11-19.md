# First Edition — Cross-Slice Relation Dependency Inventory

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `5779c3b2dd6e1276b3c5d7d3b19f83e86ae93aca`  
Status: **INVENTORY IN PROGRESS — NO RELATION APPROVAL OR PUBLICATION DECISION**

## Scope and rules

This is a separate inventory of canonical `relation` records. Relations are not included in the 809-row vertical-slice candidate denominator. This file records exact relation versions and declared participants/frame references; path existence is not proof of participant version correctness, semantic validity, or release eligibility.

- No Relation, Claim, Evidence Use, Source, Context or Scope record is modified.
- All existing HOLD decisions remain unchanged.
- Relation dependencies must be resolved to exact participant record IDs and versions before any candidate allowlist is considered.

## Exact relation records

| Relation/version | Relation type | Declared participants (path lookup only) | Frame reference | Canonical path |
|---|---|---|---|---|
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
| `REL_M3_EMERGENCY_INFRASTRUCTURE@1` | emergency_management_and_infrastructure_resilience_link | CLM-EMERGENCY_MANAGEMENT_BASICS-A@1; CLM-INFRASTRUCTURE_RESILIENCE-A@1 | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/emergency-management-basics/records/REL-M3-EMERGENCY-INFRASTRUCTURE.json |
| `REL-CONTAINER-WATER-STORAGE@1` | storage_container_for | ST-WATER-CONTAINER-SANITIZED@1; ST-WATER-CONTAINER-STORED@1 | `CTX-WATER-STORAGE-EMERGENCY@1` | CONTENT/vertical-slices/emergency-water-storage-state/records/REL-CONTAINER-WATER-STORAGE.json |

## Current batch

- Canonical relation JSON files discovered in the repository tree: 63.
- Relation records inventoried so far: 56.
- Participant references are listed verbatim; bracketed path markers only indicate a matching filename exists somewhere in the corpus tree.
- Remaining relation files: 7.

## Next

Continue the remaining relation inventory, then validate each participant's exact canonical `record_id@record_version`, record type, and slice ownership. Resolve missing/stale references and ensure relations are only included where both endpoint records are eligible and the relation itself is approved.
