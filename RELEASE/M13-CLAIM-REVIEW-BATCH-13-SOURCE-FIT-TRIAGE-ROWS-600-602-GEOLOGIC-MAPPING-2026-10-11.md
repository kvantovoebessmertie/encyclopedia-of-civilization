# M13 Batch 13 — Source-fit triage (rows 600–602): geologic mapping

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional source-fit review; relevant official source, but explicitly planetary scope**

Scoring rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional triage assessments, not finalized scored-ledger rows. No canonical JSON changed.

## Source trail

All three Claims reference `SRC-GEOLOGIC_MAPPING_BASICS`, “USGS — Planetary Geologic Mapping” at https://www.usgs.gov/special-topics/planetary-geologic-mapping. The USGS page states that the program produces high-quality standardized geologic maps of planetary bodies, supports planetary science, and provides map search and interactive map resources. The related USGS “Current Planetary Mapping Guidelines” page explains that mapping guidelines help maintain consistency and timeliness of published products and links a handbook covering data, tools, procedures, review, and publication.

This is a genuine, relevant official source, but it is deliberately focused on planetary geologic mapping, not all terrestrial geologic mapping. The Evidence Use records identify the source generally but do not give a section, quote, or pinpoint. Claims B/C explicitly refer to planetary surfaces / mission observations and fit the source scope better than a broad all-geology interpretation would.

## 1. `CLM-GEOLOGIC_MAPPING_BASICS-A` — **D2 / E2 / B2**

**Claim:** “Geologic mapping represents the distribution and relationships of geologic materials and features in a spatial framework.”

**Assessment:** The claim gives the central purpose of geologic mapping but does not explain map units, contacts, stratigraphic relationships, or interpretation (D2). The USGS program's production of standardized geologic maps of planetary bodies is relevant support, but the landing page is a program overview rather than a direct technical definition of “distribution and relationships” (E2). The claim is broadly worded and does not mark its intended planetary scope (B2).

**Disposition:** Add a technical handbook/source pinpoint. Consider making the planetary scope explicit if this Claim is intended to be supported only by the current source.

## 2. `CLM-GEOLOGIC_MAPPING_BASICS-B` — **D2 / E3 / B2**

**Claim:** “Standardized geologic maps can provide a common basis for communicating observations and interpretations about planetary surfaces.”

**Assessment:** The claim states a practical role for standardized maps but does not explain symbology or map-unit correlation (D2). The USGS source directly describes high-quality standardized maps of planetary bodies, and the guidelines explicitly emphasize consistency between published products, directly supporting the core (E3). “Communicating observations and interpretations” is a reasonable purpose statement but could be tied to the handbook's standards and review sections with a pinpoint (B2).

**Disposition:** Retain provisionally; add a pinpoint to the USGS mapping-guidelines / standardization material.

## 3. `CLM-GEOLOGIC_MAPPING_BASICS-C` — **D2 / E2 / B2**

**Claim:** “Geologic mapping programs can combine imagery, geospatial data and field or mission observations to produce map products for scientific use.”

**Assessment:** This describes a multi-input workflow but does not explain how observations are reconciled into mapped units or interpretations (D2). USGS resources support the use of imagery, geospatial data, mapping guidelines, and planetary mission data; planetary mapping differs from terrestrial field mapping because remote observations are central. However, the exact combination “field or mission observations” is not established in one pinpoint on the landing page, so source fit is relevant but not fully claim-specific (E2). The wording “can combine” is appropriately conditional but does not distinguish terrestrial and planetary workflows (B2).

**Disposition:** Add a technical handbook or tutorial pinpoint for image/mission data and field observations. Keep the scope distinction explicit.

## Batch accounting

- Individual Claims reviewed in this checkpoint: **3**.
- Source trail: structurally aligned; official USGS source is relevant.
- Open follow-up: add section-level pinpoints and make planetary vs. terrestrial scope explicit where necessary.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
