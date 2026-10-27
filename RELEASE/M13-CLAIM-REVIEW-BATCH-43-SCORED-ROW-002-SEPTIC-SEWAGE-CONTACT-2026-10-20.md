# M13 Batch 43 — Scored row 002: avoid sewage-contaminated water during septic emergencies

Date: 2026-10-20  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-SEPTIC-SEWAGE-CONTACT@1`  
Evidence Use version: `EU-SEPTIC-SEWAGE-CONTACT@1`  
Source version: `SRC-CDC-SEPTIC-EMERGENCY-2026@1`

## Claim under review

> При затоплении или переполнении септической системы следует избегать контакта с водой, которая может быть загрязнена сточными водами.

## Passage checked

Canonical Source: CDC, “Guidelines for Septic and Onsite Wastewater Systems,” https://www.cdc.gov/floods/safety/guidelines-for-septic-and-onsite-wastewater-systems.html, updated and reviewed August 24, 2026.

The page warns: “Always avoid contact with any floodwater that may be contaminated with sewage—it can make you sick!” (page lines 37–40). It further states that heavy rain, severe flooding or other emergencies can damage sewer systems and cause untreated wastewater overflow, and specifically instructs people to avoid standing water that may contain sewage (lines 27–35 and 61–65). These passages directly support the avoidance recommendation.

The canonical Evidence Use text describes the same advice but has no explicit locator. The Claim's “flooding or overflow of a septic system” framing is close to the source context, but the reader must not narrow the warning to only visible overflow or imply that water is safe when contamination is not visible.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-SEPTIC-SEWAGE-CONTACT` | 2 | 2 | 2 | **D=2:** actionable exposure-avoidance guidance related to sewage contamination and illness. **E=2:** the current CDC page directly supports the core warning; the canonical Evidence Use lacks a section locator. **B=2:** the claim identifies flood/septic emergency context, but the public-facing rendering should retain the source's broader “any floodwater that may be contaminated” boundary and not suggest contamination is reliably visible. |

## Disposition

**HOLD for qualified Human View and exact locator; not cleared for public pilot.** Passage fit is direct, but high-consequence content requires independent review and a fully traceable locator. Any record correction must be separately authorized and versioned; no canonical JSON changed here.
