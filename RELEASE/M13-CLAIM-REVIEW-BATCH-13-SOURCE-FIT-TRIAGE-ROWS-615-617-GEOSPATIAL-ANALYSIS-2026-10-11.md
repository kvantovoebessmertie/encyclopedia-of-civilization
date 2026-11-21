# M13 Batch 13 — source-fit triage (rows 615–617): geospatial analysis

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; source scope and evidence pinpoints are insufficient for the full claims**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional, not finalized ledger scores. No canonical JSON changed.

## Source trail

All three Claims cite `SRC-GEOSPATIAL_ANALYSIS_BASICS`, whose stored URI is `https://www.usgs.gov/programs/national-geospatial-program/geographic-information-systems-gis`. That stored locator could not be confirmed as the current destination during this check. A current USGS educational resource describes GIS, vector/raster data, adding multiple layers, and GIS applications; it does not automatically establish every proposition in these Claims. The Evidence Use descriptions have no exact sections, paragraphs, or passages. Treat the source trail as structurally connected but not yet evidence-complete. citeturn463443search7turn463443search5

## 1. `CLM-GEOSPATIAL_ANALYSIS_BASICS-A` — **D2 / E1 / B2**

**Claim:** “Геопространственный анализ использует данные, связанные с местоположением, для изучения пространственных отношений и закономерностей.”

**Assessment:** The statement communicates the core purpose but does not give examples of spatial relationships or analysis methods (D2). The current USGS GIS educational resource supports analysis of geographically located data in a broad sense, but the stored URL is unresolved and the evidence description has no pinpoint (E1). The scope is appropriately broad but “закономерности” could imply statistical patterns not addressed in the linked description (B2).

**Disposition:** Keep provisional. Resolve the Source locator and identify the exact source passage supporting location-linked data and analysis of relationships/patterns.

## 2. `CLM-GEOSPATIAL_ANALYSIS_BASICS-B` — **D2 / E1 / B2**

**Claim:** “Географические информационные системы позволяют хранить, отображать, анализировать и сопоставлять пространственные данные.”

**Assessment:** Lists core GIS functions but does not distinguish storage, visualization, analysis, and overlay/combination (D2). The USGS resource supports analysis and combining layers, but the stored URL and claim-specific pinpoint remain unresolved; full support for all four verbs has not been recorded (E1). “Сопоставлять” is ambiguous between visual overlay, comparison, and formal spatial analysis (B2).

**Disposition:** Resolve the source locator and pinpoint each supported function; clarify “сопоставлять” or narrow the wording to the source's explicit functions.

## 3. `CLM-GEOSPATIAL_ANALYSIS_BASICS-C` — **D2 / E1 / B1**

**Claim:** “Результаты геопространственного анализа зависят от качества, масштаба, точности и происхождения исходных пространственных данных.”

**Assessment:** Names important data-quality dimensions but gives no mechanism or example for how each affects results (D2). A USGS GIS data-quality checklist can support parts of the quality/precision/scope discussion, but the current stored source is a GIS educational page and the Evidence Use has no pinpoint; provenance and scale are not demonstrated by the present evidence trail (E1). “Масштаб” could mean map scale, spatial resolution, or analysis extent and should be defined (B1).

**Disposition:** Split into narrower claims or add a source that explicitly addresses scale/resolution, positional accuracy, data provenance, and quality effects on analysis.

## Batch accounting

- Individual Claims triaged: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Stored source locator reconciliation: **open**.
- Exact source pinpoints recorded in canonical Evidence Use: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
