# R9 Settlement Geography — CC BY 4.0 Eurostat Source Alternative

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `e5cfde7902f0abd0b38ffd0acbc2b39998882bee`  
Status: **RIGHTS-COMPATIBLE SOURCE ALTERNATIVE IDENTIFIED; DIRECT LOCATORS FOUND FOR CLAIMS A–C; NINE-RECORD SCOPE UNCHANGED; NO CANONICAL JSON CHANGED; ALL HOLD**

## 1. Why this addendum exists

The earlier R9 Settlement Geography locator research used the joint 2021 *Applying the Degree of Urbanisation* manual published by the European Commission, FAO, UN-Habitat, ILO, OECD and World Bank. That manual is CC BY-NC-SA 3.0 IGO. Its NonCommercial restriction does not clear commercial reuse, so it is a material blocker if the Encyclopedia's distribution model may be commercial.

A stronger alternative has now been identified: Eurostat's 2026 *Review and implementation of the degree of urbanisation* statistical report. The PDF explicitly licenses its content under **CC BY 4.0**, subject to item-specific exclusions for third-party cover photography, most maps and other photos. The proposed use is factual paraphrase and text locators only; no maps, photos, charts or other visuals will be reproduced.

## 2. Exact alternative source

**Bibliographic identity**

Eurostat, *Review and implementation of the degree of urbanisation*, 2026 edition, Statistical Reports, manuscript completed December 2025, first edition, Luxembourg: Publications Office of the European Union, 2026. ISBN 978-92-68-36274-7; DOI 10.2785/3471430; catalogue number KS-01-26-004-EN-N.

Official PDF:
https://ec.europa.eu/eurostat/documents/7870049/23036903/KS-01-26-004-EN-N.pdf/a9203c0d-53be-f7af-73e5-d53e0e7b7a2e?t=1771237274568&version=1.0

Official current methodology page:
https://ec.europa.eu/eurostat/en/web/degree-of-urbanisation/methodology

The 2026 report states that the degree-of-urbanisation methodology was endorsed by the UN Statistical Commission in 2020 and provides a globally comparable framework for classifying settlements beyond national definitions. It explicitly says that the methodology **complements rather than replaces national definitions**.

## 3. Exact licence and rights boundary

The 2026 report's front matter, printed page 2, states:
- © European Union, 2026;
- reuse is authorised under Creative Commons Attribution 4.0 International (CC BY 4.0), unless otherwise noted;
- reusers must provide appropriate credit and indicate changes;
- third-party elements may require separate permission.

The report expressly excludes from the EU's ownership/licence:
- cover photo;
- all maps other than Maps 4.1 and 4.2;
- other photos;
- administrative boundaries for Maps 4.1 and 4.2, credited to EuroGeographics and OpenStreetMap.

**Permitted proposed use:** factual paraphrase of the methodology, exact section/page locators and bibliographic metadata, with CC BY 4.0 attribution and indication of changes where applicable.

**Excluded proposed use:** all cover images, maps, photos, administrative-boundary data, charts/figures and other expressive assets unless their individual rights are separately verified. No such asset reuse is needed for the three Claims.

This is a materially better rights position than the 2021 joint manual's CC BY-NC-SA 3.0 IGO licence. It does not by itself clear the Encyclopedia's entire project licence, source mix or AI-assisted production workflow; those remain WP2 owner decisions.

## 4. Current Claims and direct locators

Current canonical records, all v1:
- `CLM-SETTLEMENT_GEOGRAPHY-A@1`
- `CLM-SETTLEMENT_GEOGRAPHY-B@1`
- `CLM-SETTLEMENT_GEOGRAPHY-C@1`
- `EU-SETTLEMENT_GEOGRAPHY-A/B/C@1`
- `SRC-SETTLEMENT_GEOGRAPHY@1`
- `CTX-SETTLEMENT_GEOGRAPHY@1`
- `SCP-SETTLEMENT_GEOGRAPHY@1`

The nine exact records were re-fetched from the current branch. All three EUs still lack claim-specific `material.locator` values. All remain HOLD.

### Claim A — urban-to-rural continuum and international comparison

Current statement: “Для международных сравнений населённые территории могут классифицироваться по непрерывной шкале от городских до сельских областей.”

**Direct locators:**
- Eurostat 2026 report, §1.2 “Importance of a harmonised global definition for urban and rural areas”, printed p. 6: national definitions vary widely; a harmonised approach enables international comparison of urban and rural statistics.
- §2.1 “Brief overview of the methodology”, printed p. 7: the classification covers the entire territory of a country along the urban–rural continuum and combines population-size and population-density thresholds.

**Fit:** direct. The report explicitly describes a continuum and the purpose of international comparison.

### Claim B — consistent criteria distinguish settlement types

Current statement: “Методология Degree of Urbanisation использует согласованные критерии для различения городов, малых городов и сельских территорий.”

**Direct locators:**
- Eurostat 2026 report, §2.1, printed p. 7: Level 1 distinguishes cities, towns and semi-dense areas, and rural areas; the method classifies 1 km² population-grid cells by population density and population in contiguous cells, then classifies smaller spatial units by the distribution of their population across those grid-cell classes.
- The same section: Level 2 provides seven classes — cities, dense towns, semi-dense towns, semi-dense areas, villages, dispersed rural areas and very dispersed rural areas.
- Current Eurostat methodology page, “Methodology”, paragraphs 1–4: local administrative units are classified using geographical contiguity and population density based on 1 km² population grid cells; it lists the three Level 1 classes.

**Wording alignment:** the current phrase “малых городов” is not an exact rendering of the 2026 Level 1 class “towns and semi-dense areas”. To preserve the updated classification, propose Claim B v2:

> Методология Degree of Urbanisation использует согласованные пороги численности населения и плотности населения, чтобы различать города, малые города и территории средней плотности (towns and semi-dense areas), а также сельские территории.

If the editor prefers the official English category names, retain “towns and semi-dense areas” in parentheses rather than implying a single administrative size class.

### Claim C — complements, does not replace, national definitions

Current statement: “Классификация населённых территорий предназначена для статистического сравнения и не заменяет национальные определения городов и сельских районов.”

**Direct locators:**
- Eurostat 2026 report, §1.2, printed p. 6: harmonised definitions support cross-country comparison; national definitions have varied widely.
- §2.1, printed p. 7, closing paragraph: the degree-of-urbanisation methodology “complements rather than replaces national definitions”.
- Current Eurostat methodology page, lines/paragraph on local administrative units and the three Level 1 classes, as corroborating current online presentation.

**Fit:** direct. Preserve the distinction between an international statistical classification and a country's own legal/administrative urban definitions.

## 5. Proposed exact bounded remediation

The same nine-record scope from the earlier R9 Settlement Geography proposal remains sufficient. No new canonical Source/EU ID is required if the existing Source record is versioned to the Eurostat 2026 report.

| Exact record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-SETTLEMENT_GEOGRAPHY` | v1→v2 | Correct identity to Eurostat, *Review and implementation of the degree of urbanisation*, 2026 edition; set the official Eurostat PDF URI; record CC BY 4.0 and the excluded third-party visual assets in the remediation/rights dossier |
| `CLM-SETTLEMENT_GEOGRAPHY-A` | v1→v2 | Statement unchanged; provenance-only alignment to Source v2 |
| `CLM-SETTLEMENT_GEOGRAPHY-B` | v1→v2 | Refine “малые города” to the current official Level 1 categories; provenance to Source v2 |
| `CLM-SETTLEMENT_GEOGRAPHY-C` | v1→v2 | Statement unchanged; provenance-only alignment to Source v2 |
| `EU-SETTLEMENT_GEOGRAPHY-A/B/C` | v1→v2 | Add exact section/page locators from §1.2 and §2.1, current Claim v2 / Source v2 references and concise support limits |
| `CTX-SETTLEMENT_GEOGRAPHY` | v1→v2 | Target Claim A v2; preserve the boundary that the harmonised statistical classification complements national definitions and that Level 1/Level 2 categories differ |
| `SCP-SETTLEMENT_GEOGRAPHY` | v1→v2 | Target Claim A v2; state that the slice is not a national legal definition, municipal boundary rule, land-use classification or complete settlement typology |

No record is changed by this addendum. The earlier joint-manual proposal remains archived as a source alternative but should no longer be the default implementation route if the owner approves Eurostat 2026.

## 6. Rights and source-fit comparison

| Criterion | Joint 2021 manual | Eurostat 2026 report |
|---|---|---|
| Direct methodological support | Strong | Strong; includes updated Level 1/Level 2 description |
| International-comparison purpose | Explicit | Explicit |
| National-definition boundary | Explicit | Explicit |
| Licence | CC BY-NC-SA 3.0 IGO | CC BY 4.0 unless otherwise noted |
| Commercial reuse | Not cleared by NC licence | Permitted under CC BY 4.0 for EU-owned content, subject to conditions |
| Third-party assets | Cover/maps and contributed components need separate review | Cover photo, most maps, other photos and administrative boundaries excluded |
| Recommended role | Backup/context only | Preferred primary source for text-only Claim/EU use |

The Eurostat report says it should not be considered representative of the European Commission's official position. Identify it precisely as a Eurostat Statistical Report and use it as a methodological source, not as an EU policy statement.

## 7. Authorization boundary and next steps

- The root `authorized_slices` list does not itself contain a record-level version/change scope for this remediation. No separate settlement-geography bounded authorization was found.
- Owner approval is still required for the exact nine-record v1→v2 scope and the Claim B terminology refinement.
- After approval, re-fetch all nine records at one frozen HEAD; update Source first, then Claims, EUs, Context and Scope; verify every exact reference and run the affected-slice tests.
- Record the CC BY 4.0 source identity and third-party exclusions in the WP2 rights register.
- Keep all records and the slice HOLD until independent editorial review, Human View and project-wide rights decisions close.

**Disposition:** preferred rights-compatible source alternative identified; no canonical edits authorized or performed; all nine records remain HOLD.

## Recommendation update — 2026-11-20

Eurostat 2026 is the preferred implementation route. The 2021 manual is retained only as a documented fallback because its CC BY-NC-SA 3.0 IGO licence carries a NonCommercial condition. The 2026 report is CC BY 4.0 for EU-owned content (unless otherwise noted), with third-party exclusions for the cover photo, most maps, other photos and certain administrative boundaries. The report's non-endorsement disclaimer must be preserved.

The preferred route versions the existing Source record rather than creating a new Source ID. The exact bounded scope remains nine existing records, all v1→v2. Claim A/C wording remains unchanged; Claim B terminology is narrowly corrected to the actual Level 1 class “towns and semi-dense areas”; all three EUs gain exact locators (§1.2 p. 6 and §2.1 p. 7) and support boundaries; Context/Scope references align to Claim A v2. This route avoids a record-count/coverage-denominator delta.

No canonical record changes are authorized or performed by this document. Owner approval remains required for the exact nine-record scope. All records remain HOLD.
