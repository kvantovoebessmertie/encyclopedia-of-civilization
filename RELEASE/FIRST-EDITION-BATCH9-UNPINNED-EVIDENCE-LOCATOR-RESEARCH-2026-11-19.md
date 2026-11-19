# First Edition — Batch 9 Locator Remediation Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical record inspection HEAD: `430c1da028ac3aa8c44db68b0e4455226f88fcfd`  
Baseline audit: `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH9-2026-11-19.md`  
Status: **5/5 UNPINNED EVIDENCE USES RESEARCHED; 5 DIRECT LOCATOR CANDIDATES IDENTIFIED; ALL RECORDS HOLD; NO CANONICAL CHANGE AUTHORIZED**

## 1. Purpose and controls

This bounded research closes the locator-discovery task for the five unpinned Evidence Use records in Batch 9:

- settlement-geography-basics: three EUs;
- antimicrobial-resistance-basics: one EU;
- statistics-basics: one EU.

The canonical Claim, Evidence Use and Source records were re-fetched at the inspection HEAD. Official publisher/agency source pages and relevant sections were checked. The proposed locators below are research recommendations only.

- No canonical JSON was changed.
- No Source URI, Claim wording, Evidence Use material, record version or provenance was changed.
- No HOLD was promoted.
- No rights clearance, legal conclusion or publication authorization is implied.
- The five locator gaps can be considered **research-resolved / implementation pending authorization**, not canonical closure.

## 2. Settlement geography — 3/3 locator candidates found

Current Source identity: `UN-Habitat — Applying the Degree of Urbanisation`. The inspected publication is more precisely a joint 2021 manual produced by the European Commission, FAO, UN-Habitat, ILO, OECD and the World Bank: *Applying the Degree of Urbanisation: A Methodological Manual to Define Cities, Towns and Rural Areas for International Comparisons* (2021; 102 pp.; ISBN 978-92-76-20306-3; DOI 10.2785/706535).

The currently stored URI is a legacy-looking path. The current official UN-Habitat publication page and the direct official PDF are:

- Landing page: https://unhabitat.org/knowledge/publications/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas
- Official PDF: https://unhabitat.org/sites/default/files/2021/12/ks-02-20-499-en-n.pdf
- Alternative publisher record: https://doi.org/10.2785/706535

| Claim / EU | Proposition fit | Recommended locator | Assessment |
|---|---|---|---|
| `CLM-SETTLEMENT_GEOGRAPHY-A@1` / `EU-SETTLEMENT_GEOGRAPHY-A@1` | The methodology captures an urban-rural continuum and classifies territories into distinct levels/classes. | Abstract; Chapter 1 “Introduction”, p. 7; §6.2 “Short description”, pp. 33–34. | Direct support for the continuum. Preserve the fact that the method uses three classes rather than a simple binary urban/rural split. |
| `CLM-SETTLEMENT_GEOGRAPHY-B@1` / `EU-SETTLEMENT_GEOGRAPHY-B@1` | Degree of Urbanisation uses harmonised criteria to distinguish cities, towns/semi-dense areas and rural areas. | §6.1 “Terminology” and Table 6.2, p. 33; §6.2, pp. 33–34; §6.3 “Grid cell classification”, beginning p. 34. | Direct support. The method classifies small spatial units using 1 km² grid cells, population density, population size and contiguity. |
| `CLM-SETTLEMENT_GEOGRAPHY-C@1` / `EU-SETTLEMENT_GEOGRAPHY-C@1` | Classification is for statistical comparison and does not replace national definitions. | Abstract; Chapter 1 “Introduction”, p. 7. | Direct support. The manual expressly says it is intended to complement, not replace, national statistical office and ministry definitions. |

### Source identity and rights findings

1. Correct the bibliographic identity in the Source record to reflect the six co-producing institutions rather than attributing the work to UN-Habitat alone.
2. Prefer the official UN-Habitat landing page or direct PDF as the canonical URI; preserve the DOI as a stable publication identifier.
3. The PDF explicitly states **CC BY-NC-SA 3.0 IGO**. This is a non-commercial licence with ShareAlike requirements for adaptations. It does not clear commercial redistribution or automatically establish compatibility with an as-yet-unselected project content licence.
4. The publication excludes third-party cover photography and maps from the blanket copyright grant. The corpus currently uses source identity and locators, not copied maps; any future image/map reuse requires separate item-level review.
5. The methodology complements rather than replaces national statistical definitions. Do not convert it into a universal legal definition of “city” or “rural area”.

**Disposition:** all three locator gaps have direct candidate passages. The Source identity/URI and item-level rights record still need authorized remediation and review. All three Claims remain HOLD.

## 3. Antimicrobial resistance — 1/1 locator candidate found

Current Claim: `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` — resistance affects people, animals, plants, food systems and the environment and therefore requires a multisectoral approach.

Current Source: `SRC-ANTIMICROBIAL_RESISTANCE_BASICS@1`, WHO *Antimicrobial resistance* fact sheet.

The WHO fact sheet at the existing canonical URI was updated **16 July 2026**. It now contains direct coverage of the proposition:

- URI: https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance
- Recommended EU locator: “Overview”; “A global concern”; “WHO response” (GAP-AMR 2026–2036 and One Health paragraphs); six strategic objectives.

| Evidence passage | Direct support |
|---|---|
| “Overview” | Defines antimicrobials as medicines used to prevent/treat infectious diseases in people, animals and plants. |
| “A global concern” | States that drug-resistant infections affect the health of animals and plants, reduce farm productivity and threaten food security. |
| “WHO response” | Describes a One Health approach for human, animal and plant infections; reducing antimicrobial use in agrifood systems and environmental pollution from resistant microbes/residues. |
| Six strategic objectives | Explicitly calls for multisectoral governance and coordinated AMR response across sectors and levels. |

The updated fact sheet is a materially better locator target than an unpinned reference to the page as a whole. The current page is dynamic; record the inspected page date (16 July 2026) in the audit trail and preserve the exact heading-based locator.

**Scope caution:** the Claim is broad but the current WHO page directly covers the human/animal/plant, agrifood and environmental dimensions and the multisectoral response. Do not infer that every AMR organism, sector or pathway is exhaustively covered by this single fact sheet.

**Disposition:** direct locator candidate found; source/locator metadata update remains unauthorized. All related records remain HOLD. WHO page access does not itself establish a reuse licence for republication or adaptation.

## 4. Statistics — 1/1 locator candidate found, wording needs tightening

Current Claim: `CLM-STATISTICS_BASICS-C@1` — experimental design and data analysis are connected; inference quality depends not only on calculations but also on study design.

Current Source: `SRC-STATISTICS_BASICS@1`, NIST/SEMATECH Engineering Statistics Handbook.

Official handbook landing page:
https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook

Direct official section:
https://itl.nist.gov/div898/handbook/pmd/section3/pmd31.htm

Recommended locator: **Chapter 4 “Process Modeling” → §4.3 “Data Collection for Process Modeling” → §4.3.1 “What is design of experiments (DOE)?”**

The section defines DOE as a systematic, rigorous approach that applies principles and techniques at the data-collection stage to ensure valid, defensible and supportable engineering conclusions. It directly supports the importance of experimental design to conclusion quality.

### Wording assessment

The current statement's central point is supported, but “depends not only on calculations” is a comparative formulation not stated verbatim by the locator. The cleanest direct formulation for editorial consideration is:

> Experimental design applies statistical principles at the data-collection stage to help ensure that the resulting engineering conclusions are valid, defensible and supportable.

This is a proposed wording for review, not an authorized Claim replacement. If the current broader statement is retained, the Evidence Use description should explain that the source directly supports the design-to-valid-conclusion link; it should not claim that §4.3.1 itself compares design with calculations.

The NIST/SEMATECH handbook was produced as a joint partnership. Do not assume that every component is automatically public domain solely because NIST is a U.S. federal agency; complete item-level rights/attribution review for the exact handbook and its joint contributions.

**Disposition:** direct locator candidate found; consider a narrowly aligned Claim wording revision. All records remain HOLD.

## 5. Aggregate closure

| Item | Result |
|---|---:|
| Previously unpinned Evidence Use records | 5 |
| Direct locator candidates identified | 5/5 |
| Settlement Geography | 3/3 |
| Antimicrobial Resistance | 1/1 |
| Statistics | 1/1 |
| Source identity/URI correction proposed | 1 (Settlement Geography) |
| Claim wording review proposed | 1 (Statistics) |
| Canonical records changed | 0 |
| INCLUDE / EXCLUDE decisions | 0 / 0 |
| Current dispositions | All HOLD |

The original Batch 9 count remains **22/27 EUs with locators** as measured at its inspection HEAD. This research does not retroactively alter that audit metric. It establishes that the five gaps now have candidate passages ready for authorized canonical remediation.

## 6. Execution order after authorization

1. Settlement Geography: correct the joint publication identity and URI, add the three exact locators, and preserve the national-definition boundary.
2. AMR: pin the three relevant WHO headings and the 16 July 2026 fact-sheet inspection date.
3. Statistics: add §4.3.1 and decide whether to narrow the Claim wording before changing its EU.
4. Re-fetch all affected Claim/EU/Source records at one frozen HEAD and validate exact IDs, versions, types and graph edges.
5. Complete item-level rights checks and independent subject review; keep HOLD until all first-edition gates close.
6. Run affected slice tests and the complete release gates on the final immutable HEAD after any canonical change.

No action in this research note authorizes canonical JSON changes.
