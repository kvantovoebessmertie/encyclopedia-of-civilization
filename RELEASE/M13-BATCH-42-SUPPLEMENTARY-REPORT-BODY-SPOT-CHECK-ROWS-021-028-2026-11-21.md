# M13 — Batch 42 supplementary report-body spot check (rows 021–028)

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Inspected revision: `7819ec08b07aaa23f08f1c55ded0faecacc4fe6d`  
Scope: eight individual Batch 42 scored-row reports, rows 021–028.  
Method: read the complete report bodies; extract explicit Claim/Evidence Use/Source version headers, Claim statement, historical D/E/B row, evidence-fit discussion and disposition.  
Status: **supplementary report-body inspection only; no current score acceptance and no canonical edits**.

## 1. Row-level findings

| Batch row | Exact historical chain stated in report | Historical D/E/B | Report-body finding | Recorded disposition |
|---|---|---:|---|---|
| 021 — Home fire escape plan | `CLM-HOME-FIRE-ESCAPE-PLAN@1` → `EU-HOME-FIRE-ESCAPE-PLAN@1` → `SRC-USFA-HOME-FIRE-2026@1` | 2/1/1 | The Evidence Use describes two exits per room, meeting place and practice, but the canonical Source URI points to the smoke-alarm page rather than the direct escape-plan page. No exact locator. | HOLD; bounded source/locator correction and independent Human View. |
| 022 — Two ways out | `CLM-HOME-FIRE-TWO-WAYS-NFPA@1` → `EU-HOME-FIRE-TWO-WAYS-NFPA@1` → `SRC-NFPA-HOME-FIRE-2026@1` | 2/1/1 | NFPA landing page is broad; the EU summarizes two routes and exit availability but records no exact section or passage. | HOLD; exact NFPA locator and independent Human View. |
| 023 — Power-electronics applications | `CLM_POWER_ELECTRONICS_BASICS_C@1` → `EU_POWER_ELECTRONICS_BASICS_C@1` → `SRC_POWER_ELECTRONICS_BASICS@1` | 1/1/1 | DOE source is plausibly relevant, but no pinpoint demonstrates all listed application domains (transportation, industrial systems, consumer devices, renewables and grids). | HOLD; map each domain to a passage or propose a separately authorized narrower Claim. |
| 024 — Refrigerator outage threshold | `CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` → `EU-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` → `SRC-FDA-POWER-OUTAGE-2026@1` | 2/2/2 | FDA material supports the distinction between the roughly four-hour unopened-refrigerator guideline and checking actual temperature after power returns. Exact heading/paragraph locator is absent. | HOLD; exact locator and independent Human View. |
| 025 — Municipal wastewater treatment | `CLM_WASTEWATER_TREATMENT_BASICS_A@1` → `EU_WASTEWATER_TREATMENT_BASICS_A@1` → `SRC_WASTEWATER_TREATMENT_BASICS@1` | 1/1/1 | EPA Municipal Wastewater page is topically relevant, but the stored generic EU does not pinpoint a passage supporting the full combination of physical, biological and chemical processes and the stated outcomes. | HOLD; exact EPA passage and configuration/scope check. |
| 026 — Construction hazards | `CLM-M4-CONSTRUCTION-HAZARDS-A@1` → `EU-CLM-M4-CONSTRUCTION-HAZARDS-A@1` → `SRC-M4-CONSTRUCTION-HAZARDS-OSHA@1` | 2/1/1 | OSHA construction resource is relevant; no exact passage supports each listed hazard category in the canonical EU. | HOLD; exact OSHA locator and independent Human View. |
| 027 — Mental health in emergencies | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D@1` → `EU-DISASTER_BEHAVIORAL_HEALTH_BASICS-D-WHO@1` → `SRC-WHO-MENTAL-HEALTH-EMERGENCIES-2025@1` | 1/2/2 | WHO fact sheet and EU align with population-level distress and access-to-care boundaries; no precise section/paragraph locator is preserved. Individualized diagnosis/treatment is explicitly out of scope. | HOLD; exact WHO locator and independent Human View. |
| 028 — Electronic component characteristics | `CLM-ELECTRONICS_BASICS-C@1` → `EU-ELECTRONICS_BASICS-C@1` → `SRC-ELECTRONICS_BASICS@1` | 1/1/1 | NIST electronics landing page and generic EU do not pinpoint support for all four listed factors: design, materials, operating conditions and measurement methods. | HOLD; passage-level mapping and independent Human View. |

## 2. Cross-row synthesis

- All eight report bodies explicitly state Claim, Evidence Use and Source versions. These are historical report-chain declarations, not proof that the same versions remain current today.
- Six rows have historical E=1; two rows have historical E=2 (rows 024 and 027). Do not flatten the two E=2 cases into the E=1 cohort.
- Seven of eight rows explicitly identify missing or insufficient canonical pinpoints, broad landing pages, or incomplete claim-to-passage mapping. Row 027 has a strong topical/scope match but still lacks a reproducible locator.
- The home-fire escape row (021) has a more specific chain defect: the registered Source URI points to a smoke-alarm page while the EU narrative describes escape-plan material. The report recommends a separately authorized, versioned correction, not silent substitution.
- The power-electronics applications row (023), wastewater row (025), and electronic-components row (028) require scope mapping across multiple parts of a broad proposition; merely adding a generic section locator may not cure the mismatch.
- The construction hazards row (026) is descriptive, but its complete hazard list still needs passage-level support; source authority alone is insufficient.
- Every report keeps its Claim on HOLD. None grants specialist clearance, independent review, Human View approval or publication clearance.

## 3. Reuse and limits

This spot check confirms that the eight named reports contain substantive report-body material beyond a bare Claim-ID mention: exact historical chain headers, Claim wording, an evidence-fit analysis, a D/E/B rationale and a disposition. Their historical work should be retained as review input rather than discarded or repeated automatically.

It does **not** establish:
- that any historical Claim/EU/Source version equals the current canonical version;
- that historical D/E/B scores are accepted current scores;
- that source passages or rights remain valid at the current revision;
- that the Claims have been formally risk-assessed;
- that any Claim has passed specialist review, independent review, Human View or release gates.

No score was transferred. No new score was assigned. No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was changed. No queue exclusion is authorized by this spot check.

## 4. Next use

For each row, reconcile the exact historical chain against the current canonical Claim/EU/Source graph. Then prioritize locator/source repair by defect type:

1. wrong or misaligned Source URI (row 021);
2. broad proposition requiring multiple passage mappings (rows 023, 025, 028);
3. broad landing page or generic EU requiring a claim-specific pinpoint (rows 022, 024, 026, 027).

Preserve the original historical scores and report provenance. Current E must be determined from the current canonical EU and its reproducible locator under the active protocol, not copied from this report.
