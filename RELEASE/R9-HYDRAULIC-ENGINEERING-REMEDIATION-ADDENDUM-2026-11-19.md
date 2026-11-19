# R9 Hydraulic Engineering Remediation Addendum — 2026-11-19

Date: 2026-11-19  
Authorization: `R9-HYDRAULIC-ENGINEERING-REMEDIATION-001`  
Audit: `RELEASE/R9-FIRST-EDITION-EVIDENCE-DEPTH-FOLLOWUP-2026-11-19.md`  
Branch: `mvp-public-contribution-design-2026-10-11`

## Result

Completed a bounded two-source remediation for `hydraulic-engineering-basics`.

- Existing USACE HEC-RAS Source v1→v2, pinned to the HEC-RAS Hydraulic Reference Manual v6.5.
- Added one additional Source record, `SRC-HYDRAULIC_ENGINEERING-HMS@1`, for the HEC-HMS Application Guide.
- Claims A–C versioned v1→v2 and narrowed to distinct, source-bounded propositions.
- Evidence Use A–C versioned v1→v2 with claim-specific HEC-HMS/HEC-RAS locators and current exact references.
- Context and Scope versioned v1→v2.
- README updated to describe the two-source profile.
- Publication and completion states preserved.
- The slice remains **HOLD**.

## Record profile

The slice now contains 10 canonical records:

| Role | Count |
|---|---:|
| Primary Source (HEC-RAS) | 1 |
| Additional Source (HEC-HMS) | 1 |
| Claims | 3 |
| Evidence Use | 3 |
| Context | 1 |
| Scope | 1 |
| **Total** | **10** |

The additional Source is deliberate: the Claims distinguish hydrologic modelling from hydraulic modelling and require separate authoritative USACE HEC-HMS and HEC-RAS source identities.

## Claim/source mapping

| Claim | Current Source | Pinpoint | Support boundary |
|---|---|---|---|
| A | HEC-HMS Application Guide | “How Should HEC-HMS be used?”, Step 4 | Hydrologic watershed methods vs hydraulic modelling when downstream controls, structures or inundation must be represented |
| B | HEC-RAS Hydraulic Reference Manual v6.5 | Chapter 1, “Introduction” and “Overview of Hydraulic Capabilities” | General 1D/2D hydraulic calculation capabilities; not design validation |
| C | HEC-HMS Application Guide | Step 2 and Step 9 | Hydrologic runoff hydrographs may feed hydraulic and consequence models; no guarantee that a particular transfer/model is valid |

## Safety and scope

This remediation introduces no design equations, sizing instructions, calibration procedures, flood forecasting, dam/levee operation or site-specific engineering advice. The records describe model classes and general capabilities only. Model validity depends on data, assumptions, calibration, boundary conditions and intended application.

## Rights and attribution

USACE is a U.S. federal agency, but federal hosting does not clear every linked item, software component, contractor report, third-party figure or external reference. No HEC-HMS/HEC-RAS manual text, equations, tables, diagrams or figures were copied. The records contain factual paraphrases and bibliographic citations only. Item-level terms and project-level distribution compatibility remain open.

## Validation and disposition

- All updated references point to the exact current Claim and Source versions.
- The added Source record is included in the R9 exact-version inventory.
- The R9 vertical-slice inventory increases from 93 to **94 canonical records** because this slice now has two Sources.
- All ten R9 slices remain HOLD; 0 INCLUDE / 10 HOLD / 0 EXCLUDE.
- No first-edition allowlist, publication state or completion state was changed.
- No main-branch change, merge, deployment, publication or release action was performed.
