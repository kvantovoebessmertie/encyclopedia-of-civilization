# M13 Batch 42 — Scored row 005: toxicological effects and exposure factors

Date: 2026-10-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM_TOXICOLOGY_BASICS_B@1`  
Evidence Use version: `EU_TOXICOLOGY_BASICS_B@1`  
Source version: `SRC_TOXICOLOGY_BASICS@1`

## Claim under review

> Toxicological effects depend on factors such as dose, route, duration, and characteristics of the exposed organism.

## Passage checked and linkage limitation

The current Source record points to the broad ATSDR Toxicology landing page: https://www.atsdr.cdc.gov/tox/. The current Evidence Use text only says that the source is used within the scope of the stated material and provides no heading or passage pinpoint.

During this review, official ATSDR material was located that directly discusses these factors:
- ATSDR, *Environmental Health Resources Self Learning Module: Toxicology*, “Toxicology Terminology” (dose, duration, route of exposure, substance structure and individual human factors): https://www.atsdr.cdc.gov/land-reuse-health-program/media/pdfs/toxicology-508.pdf
- ATSDR, *Overview of the Exposure Pathway Evaluation*, which notes that health effects depend on contaminant properties/toxicity, concentration, duration/frequency, route and individual factors such as age, genetics and health: https://www.atsdr.cdc.gov/pha-guidance/conducting_scientific_evaluations/exposure_pathways/overview_of_the_exposure_pathway_evaluation.html

These passages support the general proposition. However, the two exact passages inspected are not the URI currently recorded in `SRC_TOXICOLOGY_BASICS@1`; source identity and Evidence Use therefore do not yet give a traceable, exact passage-to-Claim mapping. Checked on: 2026-10-15.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM_TOXICOLOGY_BASICS_B` | 2 | 1 | 2 | **D=2:** the statement is a compact general explanatory proposition, but does not distinguish hazard, exposure, dose-response or endpoint. **E=1:** official ATSDR materials support the listed factors, but the currently linked Source URI is only a broad landing page and the Evidence Use is non-specific; the exact supporting passages found are separate pages/PDFs not recorded as the current source. **B=2:** the statement is concise and broadly scoped, but “characteristics of the exposed organism” is less precise than ATSDR's examples (age, genetics, health/developmental stage), and “toxicological effects” could be read more deterministically than a context-dependent risk statement. |

## Disposition

**HOLD for source-linkage/passage pinpoint remediation and independent Human View; specialist review required before any high-consequence public use.** Under separate bounded authorization, either retarget/version the Source and Evidence Use to the exact ATSDR passage(s), or record a new Source/Evidence Use with explicit section/passage pinpoints. Preserve the distinction between a factor influencing effects and a conclusion that exposure necessarily causes illness. Do not edit canonical records from this review note alone.

This is row 005 of Batch 42. It does not establish independent corroboration, source-currentness clearance, specialist approval, or publication eligibility.
