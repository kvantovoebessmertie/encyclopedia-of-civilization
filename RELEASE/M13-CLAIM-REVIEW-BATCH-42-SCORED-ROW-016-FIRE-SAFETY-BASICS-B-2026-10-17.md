# M13 Batch 42 — Scored row 016: categories of fire-safety measures

Date: 2026-10-17  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM_FIRE_SAFETY_BASICS_B@1`  
Evidence Use versions: `EU_FIRE_SAFETY_BASICS_B@1`, `EU_FIRE_SAFETY_BASICS_NFPA@1`  
Source versions: `SRC_FIRE_SAFETY_BASICS@1`, `SRC_NFPA_FIRE_SAFETY_BASICS@1`

## Claim under review

> Fire-safety measures can include prevention, detection, suppression, compartmentation, evacuation planning, and emergency response.

## Current record linkage

The primary Source URI is the U.S. Fire Administration's **Fire Prevention and Community Risk Reduction** page:

https://www.usfa.fema.gov/prevention/

The vertical slice also links a second Source, the National Fire Protection Association's **How to make a home fire escape plan** page:

https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning

Both canonical Evidence Use records contain only generic descriptions and do not retain an exact passage locator.

## Passage-level assessment

The USFA page describes fire prevention, public fire-safety education, and community risk reduction intended to lower the occurrence and impact of local hazards. This supports the prevention/risk-reduction part of the Claim at a high level, but it is not a direct technical taxonomy of all the listed measures.

The NFPA escape-planning page directly describes smoke alarms and advance warning, household escape planning, checking exits and routes, choosing a meeting place, and practicing the plan. This supports the detection/alerting and evacuation-planning categories. It does not, on the inspected page, directly substantiate the full list's suppression, compartmentation, and emergency-response categories.

The Claim uses “can include,” so it is not asserting that every building or fire-safety system uses every measure. Even so, the two current Evidence Use records do not pinpoint the relevant passages, and the checked passages do not cover the full list. The current evidence chain therefore does not justify a full-support score.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM_FIRE_SAFETY_BASICS_B` | 2 | 1 | 1 | **D=2:** a fire-safety taxonomy can shape decisions in a high-consequence hazard domain. **E=1:** official USFA and NFPA pages were inspected and support prevention/risk-reduction and escape planning, but both canonical Evidence Use records are generic and lack pinpoint locators. **B=1:** the sources directly support only parts of the list; suppression, compartmentation, and emergency response were not all directly substantiated by the inspected passages. |

## Disposition

**HOLD pending pinpointed evidence and independent Human View / M13 high-consequence review.** A follow-up should identify authoritative passages for suppression, compartmentation, and emergency response, add precise locators through a separately authorized versioned Evidence Use change, and re-review the complete Claim scope.

This provisional score is an audit note, not a safety clearance or publication decision. No canonical Claim, Evidence Use, or Source record changed.
