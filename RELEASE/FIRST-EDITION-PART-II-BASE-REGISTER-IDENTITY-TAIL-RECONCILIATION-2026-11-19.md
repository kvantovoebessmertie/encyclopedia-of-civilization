# First Edition — Part II Base Register Identity-Tail Reconciliation

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `3ae8482b9d6fbaedf7272727278a93c8ce0f5242`  
Status: **24/24 REMAINING IDENTITY-ONLY MASTER ROWS RE-FETCHED; 11 DEPENDENCY NODES CLOSED; 13 CONTEXT/SCOPE/SOURCE IDENTITIES VERIFIED; ALL HOLD**

## 1. Result

The master register's remaining 24 rows marked `canonical_json_verified_identity_only` were re-fetched from canonical JSON at this HEAD. All 24 exact `record_id`, `record_version` and `record_type` values match.

| Result | Count |
|---|---:|
| Existing identity-only rows re-fetched | 24/24 |
| Exact ID/version/type matches | 24/24 |
| Existing rows advanced to dependency-verified HOLD | 11 |
| Existing rows advanced to current-head identity-verified HOLD | 13 |
| New dependency Source discovered from an independent Evidence Use | 1 |
| Identity-only rows remaining after this reconciliation | 0 |

## 2. Dependency chain extension

The existing `EU-STATISTICS_BASICS-OPENSTAX@1` points to `CLM-STATISTICS_BASICS-A@1` and to `SRC-OPENSTAX-STATISTICS-BASICS@1`. The Source was absent from the master register. It was fetched at this inspection HEAD and verified as exact `record_id`, version 1, type `source`; it is added once as a dependency record.

The Source points to the OpenStax Introductory Statistics 2e definitions/key-terms page. The EU and Source still lack claim-specific pinpoint locators, so the chain remains HOLD.

## 3. Existing rows reclassified

### Dependency-verified HOLD (11)

- `EU-SI-DERIVED@2`
- `EU-SI-SEVEN-BASE@2`
- `SRC-SOIL_MICROBIOLOGY_BASICS@1`
- `SRC_SOIL_SCIENCE_BASICS@1`
- `EU-STATISTICS_BASICS-A@1`
- `EU-STATISTICS_BASICS-OPENSTAX@1`
- `SRC-STATISTICS_BASICS@1`
- `EU-THERMODYNAMICS_BASICS-A@1`
- `SRC-THERMODYNAMICS_BASICS@1`
- `EU_WATER_RESOURCE_MANAGEMENT_BASICS_A@1`
- `SRC_WATER_RESOURCE_MANAGEMENT_BASICS@1`

These exact versions were already inspected as part of the 40-Claim closure batches. The SI EUs are version 2 and correctly target version-1 Claims; no version was rewritten or downgraded.

### Identity/version/type verified HOLD (13)

- `SRC-ANTIMICROBIAL_RESISTANCE_BASICS@1`
- `SCP-MOTION_BASICS@1`
- `SRC-PARASITOLOGY_BASICS@1`
- `CTX_PATHOLOGY_BASICS@1`
- `SCP_PATHOLOGY_BASICS@1`
- `CTX-PLANT_PATHOLOGY_BASICS@1`
- `SCP-PLANT_PATHOLOGY_BASICS@1`
- `CTX-SI@1`
- `SCP-SI@1`
- `SRC-VACCINATION_INFORMATION_BASICS@1`
- `SRC-VIROLOGY_BASICS@1`
- `CTX_WATER_RESOURCE_MANAGEMENT_BASICS@1`
- `SCP_WATER_RESOURCE_MANAGEMENT_BASICS@1`

These are identity/version/type checks only. Their applicability, context boundaries, scope constraints, source fit and rights remain separate review tasks.

## 4. Decision

- No canonical JSON changed.
- No INCLUDE or EXCLUDE decisions were made.
- All 24 rows remain HOLD.
- One additional dependency Source was identified and added to the master.
- The 40/40 identity-only Claim → Evidence Use → Source chain pass is complete. The wider Part II candidate set still requires evidence sufficiency, relation semantics, rights, editorial accountability and Human View review.
