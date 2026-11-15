# M13 master remediation pass — Batch 49 Lane 1 import 03

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Baseline HEAD: `c953e7acca9019ed2df309f817a384b4d1abafe7`  
Source report: `M13-BATCH-49-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-12.md`  
Type: noncanonical report-body import and exact cohort join.

## 1. Exact join and no-double-count rule

The source report contains 20 Lane 1 claims. Exact Claim-ID matching against the 359-row residual ledger yields **18 matches**. Two marine-biology Claims in the report are not rows in this 359-EU residual cohort and are deliberately not imported or added to the denominator.

The complete source report body was inspected. Its 20 source-report scores are provisional desk assessments; all 20 are HOLD and E=1 because no sufficiently precise claim-specific locator is preserved in the Evidence Use. This import stores only the 18 in-cohort rows in dedicated desk-score columns; it does not change the official D/E/B fields.

All 18 canonical EU JSON files were fetched at baseline HEAD. Each is EU v1 and points to the exact Claim v1 and Source v1.

## 2. The 18 exact residual rows

| Claim / EU | Desk D/E/B | Report finding | Required next action |
|---|---:|---|---|
| `CLM-LINGUISTIC_TYPOLOGY_BASICS-A@1` / `EU-LINGUISTIC_TYPOLOGY_BASICS-A@1` | 3/1/3 | WALS compares structural properties across languages; direct fit but broad landing page lacks feature locator. | Add exact feature/chapter locator and preserve dataset version. |
| `CLM-LINGUISTIC_TYPOLOGY_BASICS-B@1` / `EU-LINGUISTIC_TYPOLOGY_BASICS-B@1` | 3/1/3 | WALS contains phonological, grammatical and lexical features from descriptive linguistic sources. | Add specific chapter/feature locator and dataset version. |
| `CLM-LINGUISTIC_TYPOLOGY_BASICS-C@1` / `EU-LINGUISTIC_TYPOLOGY_BASICS-C@1` | 3/1/3 | WALS maps geographic distribution of linguistic features; claim-specific map/chapter locator absent. | Add exact map/chapter locator. |
| `CLM-LITERATURE-A@1` / `EU-LITERATURE-A@1` | 3/1/3 | LoC Literary Research Guide includes fiction, poetry, drama, historical, theoretical and critical studies; Introduction not cited. | Pinpoint Introduction. |
| `CLM-LITERATURE-B@1` / `EU-LITERATURE-B@1` | 3/1/3 | LoC collections include print, periodicals, manuscripts, microforms, digital, audio and film. | Add exact Introduction/collections locator. |
| `CLM-LITERATURE-C@1` / `EU-LITERATURE-C@1` | 2/1/3 | LoC guide is a resource catalogue, not a method source distinguishing interpretation from external historical fact. | Add literary-methods/historiography sources. |
| `CLM-LIVESTOCK_SYSTEMS_BASICS-A@1` / `EU-LIVESTOCK_SYSTEMS_BASICS-A@1` | 3/1/3 | FAO describes land-based animal production systems and goods/services provided. | Add exact FAO definition/overview locator. |
| `CLM-LIVESTOCK_SYSTEMS_BASICS-B@1` / `EU-LIVESTOCK_SYSTEMS_BASICS-B@1` | 3/1/3 | FAO systems framing includes resources, people, products, environmental impacts and benefits. | Add exact systems-framework locator. |
| `CLM-LIVESTOCK_SYSTEMS_BASICS-C@1` / `EU-LIVESTOCK_SYSTEMS_BASICS-C@1` | 3/1/3 | FAO distinguishes systems by species, production model, geography, resources and goals. | Add exact classification passage locator. |
| `CLM-MACROECONOMICS_BASICS-A@1` / `EU-MACROECONOMICS_BASICS-A@1` | 3/1/3 | IMF Back to Basics defines macroeconomics through aggregate output, income, employment and price-level indicators. | Add exact IMF article/section locator. |
| `CLM-MACROECONOMICS_BASICS-B@1` / `EU-MACROECONOMICS_BASICS-B@1` | 2/1/2 | IMF series page does not pinpoint GDP definition or final-goods/domestic-boundary/period qualifications. | Cite exact GDP article or national-accounts standard. |
| `CLM-MACROECONOMICS_BASICS-C@1` / `EU-MACROECONOMICS_BASICS-C@1` | 2/1/2 | IMF series page too broad for general price-level change and inflation-index methodology. | Cite an exact inflation definition and index methodology. |
| `CLM-MANUFACTURING_PROCESSES_BASICS-A@1` / `EU-MANUFACTURING_PROCESSES_BASICS-A@1` | 2/1/2 | NIST MEP is a support program, not a technical definition of transformation of materials/components into products. | Add a manufacturing-process source and locator. |
| `CLM-MANUFACTURING_PROCESSES_BASICS-B@1` / `EU-MANUFACTURING_PROCESSES_BASICS-B@1` | 2/1/2 | NIST MEP page does not pinpoint process sequence, quality control and product requirements. | Add a specific manufacturing-process source. |
| `CLM-MANUFACTURING_PROCESSES_BASICS-C@1` / `EU-MANUFACTURING_PROCESSES_BASICS-C@1` | 2/1/2 | NIST MEP page does not establish process selection by material, geometry, properties and scale. | Add process-selection engineering references. |
| `CLM-MARKET_DESIGN_BASICS-A@1` / `EU-MARKET_DESIGN_BASICS-A@1` | 3/1/2 | Nobel Prize 2012 overview supports matching/allocative institutions but is not a technical market-design definition. | Add a specific Roth/Shapley source and technical locator. |
| `CLM-MARKET_DESIGN_BASICS-C@1` / `EU-MARKET_DESIGN_BASICS-C@1` | 2/1/2 | Stable matching source does not establish that stable mechanisms generally reduce manipulation for all participants; strategy-proofness depends on mechanism/proposing side. | Narrow to a specified mechanism and cite strategy-proofness source. |
| `CLM-MEASUREMENT_INSTRUMENTATION_BASICS-A@1` / `EU-MEASUREMENT_INSTRUMENTATION_BASICS-A@1` | 3/1/3 | NIST Metrology supports quantitative measurement by instruments, but broad program page does not pinpoint the definition. | Add metrology glossary/guide locator. |

## 3. Import totals

- Source report reviewed: 20 Claims.
- Exact matches to residual-359 ledger: 18.
- Outside residual-359 cohort and excluded: 2 marine-biology Claims.
- Exact report-body imports added: 18.
- Current EU records fetched: 18/18, all version 1.
- Claim/Source versions referenced by those EUs: 18/18, all version 1.
- All 18 remain HOLD.
- Provisional desk D/E/B stored only in separate fields; official score fields unchanged.
- Canonical JSON modified: 0; score records modified: 0; new records: 0; authorization used: 0.

The companion CSV now records **65/359** exact report-body imports: 27 prior thematic rows + 20 Batch 48 Lane 3 rows + 18 Batch 49 Lane 1 residual rows. The other 294 rows remain unimported.

## 4. Next action

Continue the exact Claim-ID join for the remaining completed lane reports, verifying current EU versions and retaining only in-cohort rows. Preserve all HOLD states and prepare grouped noncanonical correction proposals only after the report-body imports are reconciled. No canonical write authorization is created.
