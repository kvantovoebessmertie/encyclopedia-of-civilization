# M13 — preliminary content-level screen of unassessed-risk Claims

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input artifact: `m13-review-queue-f26820e59b08b4036ad78302dad8118c51dac540` (run `43496934373`, artifact `14071268296`)  
State: **preliminary desk triage only; no risk metadata assigned; no canonical record, score, or source record changed.**

## 1. Purpose and method

The exact-head M13 queue contains 711 Claims with no recorded `risk_domains` or `machine_triage_flags`. These records are `UNASSESSED`; absence of metadata is not a low-risk determination.

A first content-level screen inspected 17 Claim records selected from the unassessed queue because their slice names or statements concerned disaster response, earthquake aftershocks, electrical/industrial safety, food/water safety, public-health surveillance, or safety engineering. The screen used Claim text and linked local EU/Source identity records. External source pages were checked only where an exact official locator was available.

This is a routing screen, not a complete risk assessment. It does not determine likelihood, severity, exposure, jurisdiction, or operational risk class. No risk labels are written back to the canonical records.

## 2. Immediate manual-review candidates

The following three records contain direct safety or emergency-consumer guidance and should be routed before routine informational Claims:

| Claim | Linked Evidence Use / Source | Preliminary reason | Current desk disposition |
|---|---|---|---|
| `CLM-AFTERSHOCK-DAMAGE@1` | `EU-AFTERSHOCK-DAMAGE@1` → `SRC-USGS-AFTERSHOCK-2026@1` | Warns that damaged buildings may be hazardous during subsequent shaking and requires competent assessment | **Priority review; support is only partial at current locator.** The registered source is a general USGS aftershock-forecast page. A directly relevant USGS report exists: *Estimating Aftershock Risk for Entry into Earthquake-Damaged Buildings*, Open-File Report 2026-1029, first posted 2026-09-03. It discusses risk during entry and limits of the model. The report is not currently the Source record linked by the EU; do not silently substitute it. The “competent specialist” clause needs its own source support. |
| `CLM-ELECTRICAL_SAFETY_OSHA_A@1` | `EU-ELECTRICAL_SAFETY_OSHA_A@1` → `SRC-ELECTRICAL_SAFETY_OSHA@1` | Summarizes OSHA requirements for work near/on energized equipment and qualified-person boundary | **Priority review; direct regulatory text located.** OSHA 29 CFR 1910.333(a), (b), and (c)(2) require hazard-appropriate safety practices, de-energization subject to stated exceptions, lockout/tagging and verification, and restrict work on equipment not de-energized under paragraph (b) to qualified persons. Jurisdiction and employer/employee scope must remain explicit. |
| `CLM-FLOOD-FOOD-FDA-CONTACT@1` | `EU-FLOOD-FOOD-FDA-CONTACT@1` → `SRC-FDA-FLOOD-FOOD-2024@1` | Contains direct consumer advice not to eat food contacted by floodwater and a packaging-specific salvage distinction | **Priority review; direct FDA guidance located.** FDA's current page says not to eat food that may have contacted floodwater and distinguishes undamaged commercially prepared all-metal cans and retort pouches under a specific cleaning/sanitizing procedure. Verify that the Claim's narrower wording preserves all package exclusions and does not overgeneralize the salvage exception. The stored URI resolves to an older path; current canonical page is `https://www.fda.gov/food/food-safety-during-emergencies/floods-key-tips-consumers-about-food-and-water-safety`. Treat this as a Source identity/locator review, not an automatic Source update. |

## 3. External verification notes

- **OSHA:** `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333`. Sections 1910.333(a), (b)(2)(iv), and (c)(2) directly support the work-practice, de-energization/verification, and qualified-person boundaries. The rule is a U.S. occupational safety standard; it is not a universal legal rule for all jurisdictions or all independent repair.
- **FDA:** `https://www.fda.gov/food/food-safety-during-emergencies/floods-key-tips-consumers-about-food-and-water-safety`. Sections “Keep Food Safe” and “How to Save Undamaged Food Packages Exposed to Flood Water” support the direct-contact prohibition and narrow salvage exception. The source also gives water-safety instructions, but those must not be inferred into this Claim unless separately represented.
- **USGS:** `https://pubs.usgs.gov/publication/ofr20261029/full` and DOI `https://doi.org/10.3133/ofr20261029`. The 2026 report directly studies aftershock risk during entry into earthquake-damaged buildings. It uses simplifying assumptions and example risk thresholds; it is not a universal building-entry clearance rule. The currently linked Source record points instead to `https://www.usgs.gov/programs/earthquake-hazards/science/aftershock-forecasting`. The relationship between the registered Source and the Claim must be adjudicated before any canonical edit.

## 4. Other inspected Claims

The remaining 14 of the 17 inspected records were not assigned a risk level by this screen. They include general statements about disaster-response phases and preparedness, hydropower energy storage, industrial safety management, public-health surveillance methods, and safety-engineering concepts. Some are adjacent to consequential domains, but slice name alone is not enough to infer that the individual Claim is high-consequence. They remain in the 711-record `UNASSESSED` queue until their statements, likely use, exposure, and linked evidence are reviewed.

## 5. Required next steps

1. Have a reviewer with earthquake/structural-safety competence adjudicate the aftershock Claim, especially the “competent specialist” clause and the exact USGS source identity.
2. Have an electrical-safety reviewer verify the OSHA Claim's wording, jurisdictional boundary, exceptions, and current regulatory text.
3. Have a food-safety reviewer verify the FDA Claim's package categories, exception conditions, and stored Source URI.
4. Record any accepted risk metadata only through a separately bounded canonical correction authorization, with exact Claim IDs/versions and regression tests.
5. Continue the remaining 708 unassessed Claims through content-level screening; do not infer low risk from absent flags or from the 14 non-prioritized records in this small sample.

## 6. Integrity statement

- Unassessed queue at source revision: 711 Claims.
- Claim records inspected in this preliminary screen: 17.
- Immediate manual-review candidates routed: 3.
- Independent specialist adjudications: 0.
- Risk metadata assigned or changed: 0.
- Canonical Claim/EU/Source records changed: 0.
- Historical D/E/B score rows changed: 0.
- Publication or Human View approval: 0.

This report narrows the next human-review queue. It does not close any M13 finding, certify the 711 Claims, or authorize publication.
