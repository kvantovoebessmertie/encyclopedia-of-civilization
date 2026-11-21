# M13 — Batch 42 supplementary report-body spot check (rows 045–052)

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Inspected revision: `3db08db06619acf9489c1de5cb2412a6a7527eaf`  
Scope: eight individual Batch 42 scored-row reports, rows 045–052.  
Method: read each complete report body; extract explicit historical Claim/Evidence Use/Source version headers, Claim statement, historical D/E/B rationale, evidence-fit analysis and disposition.  
Status: **supplementary report-body inspection only; no current score acceptance and no canonical edits**.

## 1. Row-level findings

| Row | Exact historical chain declared in report | Historical D/E/B | Evidence-fit finding | Disposition |
|---|---|---:|---|---|
| 045 — Refrigerator outage threshold | `CLM-FOOD-REFRIGERATOR-4H@1` → `EU-FOOD-REFRIGERATOR-4H@1` → `SRC-USDA-POWER-OUTAGE-2024@1` | 2/2/1 | USDA FSIS summary directly matches approximately four hours for a closed refrigerator, but no exact passage locator is stored. Time estimate must not be read as a guarantee for any particular food. | HOLD; exact USDA locator, conditions/scope review and independent Human View. |
| 046 — Risk communication | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A@1` → `EU-PUBLIC_RISK_COMMUNICATION_BASICS-A@1` → `SRC-PUBLIC_RISK_COMMUNICATION_BASICS@1` | 1/1/1 | UNDRR resource is relevant, but generic EU does not pinpoint support for both shared understanding and support for risk-reduction action; causal “helps” phrasing needs exact support. | HOLD; exact UNDRR locator and independent Human View. |
| 047 — REM/non-REM cycles | `CLM-SLEEP_BASICS-A@1` → `EU-SLEEP_BASICS-A@1` → `SRC-SLEEP_BASICS@1` | 1/2/2 | NHLBI/NIH “How Sleep Works” and EU directly match recurring REM/non-REM cycles, but the actual sleep-stages section locator is absent. | HOLD; exact NHLBI section locator and independent Human View. |
| 048 — Sleep, health and attention | `CLM-SLEEP_BASICS-C@1` → `EU-SLEEP_BASICS-C@1` → `SRC-SLEEP_BASICS@1` | 1/2/2 | NHLBI/NIH EU summary aligns with cautious wording that insufficient/poor-quality sleep may affect health, clear thinking and concentration; canonical URI is broad and no pinpoint is preserved. | HOLD; exact NHLBI locator and independent Human View. |
| 049 — Food-grade emergency water containers | `CLM-CDC-FOOD-GRADE-CONTAINER@1` → `EU-CLAIM-SOURCE@1` → `SRC-CDC-WATER-STORAGE-ATTRIBUTION-2025@1` | 2/2/2 | CDC source/EU summary align on FDA-approved food-grade containers and avoiding toxic transfer. Exact paragraph is absent; Claim's “CDC recommends” wording needs to match the page's precise wording. | HOLD; exact CDC locator, wording check and independent Human View. |
| 050 — Urban planning scope | `CLM-URBAN_PLANNING_BASICS-A@1` → `EU-URBAN_PLANNING_BASICS-A@1` → `SRC-URBAN_PLANNING_BASICS@1` | 1/1/1 | UN-Habitat topic is relevant, but generic EU does not pinpoint support for the complete list of housing, transport, infrastructure and public spaces. | HOLD; exact UN-Habitat locator and independent Human View. |
| 051 — Wastewater treatment purpose | `CLM-WASTEWATER_BASICS-B@1` → `EU-WASTEWATER_BASICS-B@1` → `SRC-WASTEWATER_BASICS@1` | 1/1/1 | EPA “Wastewater 101: Fundamentals” is relevant, but no passage is identified for the full purpose statement about reducing associated risks and impacts; scope is broad. | HOLD; exact EPA locator and scope clarification. |
| 052 — WHO household water-treatment performance | `CLM-WATER-FILTER-WHO-PERFORMANCE@1` → `EU-WATER-FILTER-WHO-PERFORMANCE@1` → `SRC-WHO-HWT-EVALUATION@1` | 2/2/2 | WHO evaluation scheme and EU directly match comparative microbial pathogen-removal performance, but exact criteria/table locator and formal terminology (“health-based performance criteria”) are not pinned. | HOLD; exact WHO criteria/table locator and independent Human View. |

## 2. Cross-row synthesis

- All eight report bodies contain explicit historical Claim/Evidence Use/Source version headers, claim wording, D/E/B rationale, source-fit discussion and a disposition. This is substantive historical report material, not a bare ID mention.
- Historical E distribution: **E=2 for rows 045, 047, 048, 049 and 052 (five rows); E=1 for rows 046, 050 and 051 (three rows)**. Preserve the distinction.
- Rows 047–049 and 052 have strong summary-level evidence alignment but lack reproducible passage/table pinpoints. Row 049 additionally needs a precise check of whether the canonical CDC wording is a recommendation or a description of suitable containers.
- Rows 046, 050 and 051 have broad propositions whose full wording is not mapped to the generic source chain.
- Rows 045 and 049 are emergency water/food safety matters; their statements must not be converted into guarantees or complete protocols. Row 052 must not be read as device-specific approval.
- All eight reports retain HOLD. None grants specialist clearance, independent review, Human View approval, formal risk assessment or publication clearance.

## 3. Reuse limits and current-version boundary

This inspection confirms that the eight named reports contain reasoned historical assessments and explicit historical version chains. It does **not** establish that those historical Claim/EU/Source versions equal the current canonical versions. A current graph comparison remains required before classifying any row as an exact-version reusable assessment candidate.

It also does not establish current passage availability, source rights, formal risk assessment, specialist review, independent review, Human View or release clearance.

No score was transferred or newly assigned. No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was changed. No queue exclusion is authorized by this spot check.

## 4. Next use

Reconcile each declared historical chain against the current canonical graph. Prioritize exact locator recovery for all eight, with safety-focused scope checks for rows 045, 049 and 052. Preserve historical scores and provenance; current E must be evaluated from the current canonical Evidence Use and its reproducible locator.
