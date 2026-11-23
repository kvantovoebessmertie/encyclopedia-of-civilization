# M13 Batch 13 — Source-fit triage (rows 594–596): geographic coordinates

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional source-fit review; linked USGS educational source contains directly relevant material**

Scoring rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional triage assessments, not finalized scored-ledger rows. No canonical JSON changed.

## Source trail

The three Claims link to `SRC-GEOGRAPHIC_COORDINATES_BASICS`, “27 Ideas for Teaching with Topographic Maps” (USGS): https://www.usgs.gov/educational-resources/27-ideas-teaching-topographic-maps-0. Unlike a generic map overview, this source includes specific sections on coordinate systems, latitude/longitude, comparing coordinate systems, precision of coordinates, and accuracy limitations. The Evidence Use records are structurally aligned but contain only generic descriptions, with no section-specific pinpoint. The content fit is therefore materially better than a locator check alone suggests, but exact evidence passages should still be recorded.

## 1. `CLM-GEOGRAPHIC_COORDINATES_BASICS-A` — **D1 / E2 / B2**

**Claim:** “Географические координаты позволяют задавать положение объектов на поверхности Земли.”

**Assessment:** This is a concise introductory statement with little explanation of how the coordinate reference works (D1). The USGS resource uses latitude/longitude to locate a school or campus and discusses absolute location, which supports the core idea, though it is a teaching-activity collection rather than a formal definition page (E2). The claim is appropriately scoped but leaves the coordinate reference and precision unspecified (B2).

**Disposition:** Keep provisionally; add a pinpoint to the coordinate-system or absolute-location section.

## 2. `CLM-GEOGRAPHIC_COORDINATES_BASICS-B` — **D1 / E3 / B2**

**Claim:** “Широта и долгота образуют координатную систему для определения положения.”

**Assessment:** The statement is brief and descriptive (D1). The USGS page explicitly discusses latitude/longitude as the geographic coordinate system and describes using them to determine a location, giving direct support (E3). The wording is accurate at this introductory level, although it does not discuss datum or coordinate reference details (B2).

**Disposition:** Retain provisionally; link the Evidence Use to the specific “Coordinate Systems” section.

## 3. `CLM-GEOGRAPHIC_COORDINATES_BASICS-C` — **D2 / E3 / B2**

**Claim:** “Точность координат и выбор системы координат зависят от задачи и требуемой пространственной точности.”

**Assessment:** This identifies a meaningful dependency between use case and precision, but does not explain the practical decision process (D2). The USGS resource directly contrasts location tasks requiring different precision, discusses limitations in GPS readings, and compares coordinate systems for different purposes (E3). The claim is appropriately conditional but would be more actionable with examples of when a coordinate system or precision level is appropriate (B2).

**Disposition:** Source fit is strong. Add a pinpoint to the sections on precision and comparing coordinate systems; consider adding one concrete example in an authorized content-editing pass.

## Batch accounting

- Individual Claims reviewed in this checkpoint: **3**.
- Claim → Evidence Use → Source IDs: present and aligned.
- Source-fit follow-up: add section-level pinpoints to Evidence Use records.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
