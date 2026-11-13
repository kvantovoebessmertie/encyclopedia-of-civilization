# M13 thematic source-passage review — Demography Basics

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Review type: source-passage desk review; noncanonical audit artifact  
Scope: 3 Claims, 5 Evidence Uses, 2 Sources

## Executive result

This slice is materially better sourced than the adjacent Demographic Methods Basics slice: it has a publication-specific WPP 2024 Source and a separate methodology-report Source, with method-oriented Evidence Uses. The core concepts are credible. However, the current Evidence Uses identify broad report sections and frameworks rather than exact page/table/paragraph locators. Claim B also combines age structure and population momentum; the provided Evidence Use clearly supports cohort/age-structure dynamics but does not yet isolate the population-momentum concept.

**Disposition: HOLD for all 3 Claims** pending exact pinpoint locators and a focused passage for population momentum. No canonical records, scores, manifests, or publication states were changed.

## Records and findings

### A — Population change components

Claim: “Population change is shaped by fertility, mortality and international migration.”

Evidence Uses:
- `EU-DEMOGRAPHY_BASICS-A`: WPP 2024 Summary of Results, demographic-component framework.
- `SRC-DEMOGRAPHY_BASICS`: UN Population Division, *World Population Prospects 2024: Summary of Results*.

Finding: **SUBSTANTIVE SUPPORT FOUND**. The UN WPP 2024 framework describes fertility, mortality and migration as the principal drivers of population change. This is a concise and defensible statement. Improve the EU by pinpointing the relevant section/figure and distinguish international migration from migration generally only where the source wording does so.

### B — Past patterns, age structure and population momentum

Claim: “Past demographic patterns also affect current age structure and population momentum.”

Evidence Use:
- `EU-DEMOGRAPHY_BASICS-B`: WPP 2024 summary results, with linked methodology EU.
- `EU-DEMOGRAPHY_BASICS-B-WPP-METHOD`: WPP 2024 Methodology Report, Introduction and cohort-component projection method.
- `SRC-DEMOGRAPHY_BASICS-WPP-METHODOLOGY-2024`: publication-specific methodology report Source.

Finding: **PARTIAL SUPPORT FOUND**. Cohort-component methods explicitly track population by age and sex through fertility, mortality and net migration, supporting the age-structure component. The exact phrase/concept “population momentum” is not pinned to a passage in the current EU. Add a distinct locator and evidence statement for population momentum, or narrow the Claim to the part already evidenced. Do not treat a broad mention of future trajectories as equivalent to a direct definition of momentum.

### C — Estimates, projections, data and assumptions

Claim: “Demographic estimates and projections are model-based and depend on data and assumptions.”

Evidence Use:
- `EU-DEMOGRAPHY_BASICS-C`: WPP 2024 Summary of Results, distinguishing estimates from projections.
- `EU-DEMOGRAPHY_BASICS-C-WPP-METHOD`: WPP 2024 Methodology Report, Introduction and section II, “The Preparation of Population Projections”.

Finding: **SUBSTANTIVE SUPPORT FOUND**. The methodology report describes the production of estimates and projections using observed demographic data and assumptions about fertility, mortality and migration, including probabilistic methods and uncertainty. The distinction between historical estimates and future projections is essential and correctly flagged. Exact subsections/pages and the relevant uncertainty treatment still need pinpoints.

## Source and locator quality

Positive:
- Source identities name the UN Population Division and the WPP 2024 publication.
- A separate Source record exists for the WPP 2024 methodology report.
- The linked methodology Evidence Uses identify the cohort-component approach and projection-preparation section.
- The EU descriptions include useful caveats: reference dates, assumptions, and projections not being observations.

Remaining defects:
1. Evidence Uses rely on section names/framework descriptions rather than reproducible page, subsection, table, figure or paragraph locators.
2. Claim B's “population momentum” element lacks its own pinpoint.
3. Source URLs are landing pages; the exact methodology PDF/report version should be preserved as a stable direct publication URL where the repository's Source policy allows it.
4. Claim A says “international migration”; confirm the selected WPP passage uses that exact scope rather than generic migration.

## Required correction packet

1. Add exact WPP 2024 Summary of Results locators to EU-A.
2. Add exact methodology-report subsection/page locators to EU-B-WPP-METHOD and EU-C-WPP-METHOD.
3. Add a dedicated UN Population Division passage defining/explaining population momentum to EU-B, or narrow Claim B.
4. Confirm the source passage supports “international” migration for Claim A.
5. Run schema, reference, source-identity and release-conformance checks after any authorized canonical changes.
6. Obtain independent reviewer assessment; this desk review is not independent specialist review and does not assign D/E/B scores.

## Decision

| Claim | Desk-review finding | D/E/B disposition | Release disposition |
|---|---|---|---|
| A | Substantive support found; exact locator and scope check remain | Not newly scored | HOLD |
| B | Age-structure support; population-momentum pinpoint missing | Not newly scored | HOLD |
| C | Substantive support found; exact locator remains | Not newly scored | HOLD |

## Limits

No canonical record was edited. No D/E/B score was assigned or inferred. No source-independence finding, specialist approval, editorial authorization or release approval is claimed.
