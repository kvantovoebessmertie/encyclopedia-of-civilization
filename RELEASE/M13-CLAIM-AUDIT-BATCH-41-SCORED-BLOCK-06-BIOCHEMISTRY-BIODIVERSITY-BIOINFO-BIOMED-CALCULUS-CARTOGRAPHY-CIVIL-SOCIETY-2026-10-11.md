# M13 Claim Audit — Batch 41 Scored Block 06
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: Batch 41 worklist candidates #81–100: biochemistry (2), biodiversity (3), bioinformatics (3), biomedical engineering (3), calculus (3), cartography (3), civil society (3).
Status: **20 Claims scored. Batch 41 candidates #1–100 now all have a scored block report.** This does not certify the global ledger or complete M13.

## Method
D = explanatory depth, E = claim-specific evidence fit, B = boundary discipline; each scored 0–3. Claim, Source and selected Evidence Use records were inspected; external pages were checked for direct fit. Several worklist paths/record IDs use separator variants; these are recorded for reconciliation and were not rewritten. No Claim, Evidence Use, Source or Relation JSON was changed.

## Claim-level results

| # | Claim ID | D | E | B | Rationale and disposition |
|---:|---|---:|---:|---:|---|
| 81 | `CLM-BIOCHEMISTRY_BASICS-B` | 2 | 0 | 3 | The source is an OpenStax Biology metabolism chapter, which does not directly support the generic epistemic rule that interpretation depends on source, context and applicability limits. This is methodological guidance, not a biochemistry fact; move to project-wide editorial guidance or cite a methodology source. |
| 82 | `CLM-BIOCHEMISTRY_BASICS-C` | 2 | 0 | 3 | The OpenStax metabolism source does not establish the rule that basic knowledge cannot replace specialist checking for condition-, measurement- or professional-judgment-dependent conclusions. Sensible governance guidance, but the current source and `documented_fact` type are mismatched. No record changed. |
| 83 | `CLM-BIODIVERSITY_BASICS-A` | 2 | 3 | 3 | OpenStax Biology 2e §47.1 explicitly discusses species diversity, genetic diversity and ecosystem diversity. The claim captures these levels without overclaiming that they are identical measures. Strong direct support. |
| 84 | `CLM-BIODIVERSITY_BASICS-B` | 2 | 3 | 3 | OpenStax §47.1 explicitly states that species numbers change with the relative rates of speciation and extinction. Strong direct support. |
| 85 | `CLM-BIODIVERSITY_BASICS-C` | 2 | 1 | 3 | OpenStax discusses different biodiversity measures, survey-area effects and observation limitations, but the full scale/time/method triad is not directly established as a single rule by the stored source. Plausible methodological synthesis; add a biodiversity-monitoring/measurement source. |
| 86 | `CLM_BIOINFORMATICS_BASICS_A` (worklist filename uses `CLM-BIOINFORMATICS_BASICS-A`) | 2 | 2 | 3 | NCBI’s glossary defines bioinformatics as computational approaches for collecting, storing, organizing and analyzing biological data. Strong substantive fit, but the stored Source URI is only the NCBI Bookshelf root rather than the direct glossary entry. Preserve the ID/filename separator variant for reconciliation. |
| 87 | `CLM_BIOINFORMATICS_BASICS_B` (worklist filename uses `CLM-BIOINFORMATICS_BASICS-B`) | 2 | 2 | 3 | NCBI supports organizing/storing/retrieving biological information, but the stored root URL does not pinpoint a database definition or example. Claim is straightforward; add direct NCBI database documentation or the relevant NCBI Bookshelf chapter. |
| 88 | `CLM_BIOINFORMATICS_BASICS_C` (worklist filename uses `CLM-BIOINFORMATICS_BASICS-C`) | 2 | 3 | 3 | NCBI’s BLAST glossary defines sequence alignment as matching nucleotide/amino-acid residues to assess similarity and describes BLAST sequence comparison. Strong direct support. Stored Source still needs the direct glossary/BLAST locator. |
| 89 | `CLM_BIOMEDICAL_ENGINEERING_BASICS_A` | 2 | 2 | 3 | NIBIB’s biomedical-engineering material connects engineering methods with healthcare problems and biological/medical technologies, supporting the core definition. The stored NIBIB topic page is relevant but the exact definition passage should be linked. |
| 90 | `CLM_BIOMEDICAL_ENGINEERING_BASICS_B` | 2 | 3 | 3 | NIBIB explicitly describes medical devices as technologies interacting with the body to improve health and says they can monitor, modulate or supplement bodily functions; examples include diagnostics and treatment. Strong support for diagnostic/monitoring/therapeutic purposes. |
| 91 | `CLM_BIOMEDICAL_ENGINEERING_BASICS_C` | 2 | 2 | 3 | NIBIB’s educational materials show biomedical engineering spans medical technology, biological systems, imaging, biomaterials and devices, but the precise four-discipline list is a synthesis and not directly enumerated in the stored source. Add a direct interdisciplinary definition. |
| 92 | `CLM-CALCULUS_BASICS-A` | 2 | 3 | 3 | OpenStax Calculus Volume 1 §2.2 directly defines a limit through function behavior as the argument approaches a value. Strong direct support; stored Source points only to the book landing page. |
| 93 | `CLM-CALCULUS_BASICS-B` | 2 | 3 | 3 | OpenStax Calculus Volume 1 §3.1 defines the derivative through a limit and connects it to instantaneous velocity/rate of change, provided the limit exists. The claim’s existence-condition caveat is appropriate. |
| 94 | `CLM-CALCULUS_BASICS-C` | 2 | 3 | 3 | OpenStax Calculus Volume 1 §5.2 defines the definite integral and explains its relationship to net area and accumulation/average value. The phrase “under appropriate conditions” preserves mathematical boundaries. |
| 95 | `CLM-CARTOGRAPHY-A` | 2 | 3 | 3 | USGS Mapping 101 explicitly calls cartography the science of making maps and describes maps as representing geographic areas/features. Strong support for map creation/use to represent spatial information. |
| 96 | `CLM-CARTOGRAPHY-B` | 2 | 2 | 3 | USGS Mapping 101 links topographic maps and elevation mapping, and USGS mapping resources describe topographic map products; however, the stored landing page does not itself pinpoint contour lines and symbol conventions together. Add a direct topographic-map reading lesson/symbol sheet. |
| 97 | `CLM-CARTOGRAPHY-C` | 1 | 1 | 3 | The map-scale definition is standard, but the stored Mapping 101 page does not directly define the ratio between map distance and ground distance. The source is broadly relevant, not claim-specific. Add a direct USGS map-scale definition. |
| 98 | `CLM-CIVIL_SOCIETY_BASICS-A` | 2 | 2 | 3 | The World Bank public-reference PDF is relevant to civil society, but the source record is a document-level locator and does not give a pinpoint definition for the voluntary sphere distinct from state and market. The word “usually” appropriately signals variation across definitions; cite the definition passage and preserve context. |
| 99 | `CLM-CIVIL_SOCIETY_BASICS-B` | 2 | 2 | 3 | The World Bank reference is relevant to the forms and functions of civil-society organizations, but the claim’s specific list (groups, foundations, professional associations, NGOs and networks) needs a pinpoint passage. Do not imply a universal legal status for all listed forms. |
| 100 | `CLM-CIVIL_SOCIETY_BASICS-C` | 2 | 2 | 3 | The Evidence Use record says the source supports participation in public discussion, interest representation and public-interest services, with jurisdiction caveats. The linked World Bank document is relevant but needs an exact passage locator; keep the “may participate” qualification. |

## External sources checked
- OpenStax Biology 2e §47.1, “The Biodiversity Crisis”: https://openstax.org/books/biology-2e/pages/47-1-the-biodiversity-crisis
- NCBI Bookshelf, “BLAST Glossary”: https://www.ncbi.nlm.nih.gov/books/NBK62051/
- NCBI Bookshelf, “Glossary — The NCBI Handbook”: https://www.ncbi.nlm.nih.gov/books/NBK470040/
- NIH NIBIB, “Medical Device Technologies”: https://www.nibib.nih.gov/science-education/science-topics/medical-device-technologies
- NIH NIBIB, Biomedical Engineering topic: https://www.nibib.nih.gov/science-education/science-topics/biomedical-engineering
- OpenStax Calculus Volume 1 §2.2, “The Limit of a Function”: https://openstax.org/books/calculus-volume-1/pages/2-2-the-limit-of-a-function
- OpenStax Calculus Volume 1 §3.1, “Defining the Derivative”: https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative
- OpenStax Calculus Volume 1 §5.2, “The Definite Integral”: https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral
- U.S. Geological Survey, “Mapping 101”: https://www.usgs.gov/science/science-explorer/maps-and-mapping/mapping-101
- World Bank, civil society public-reference PDF stored in the Source record: https://documents1.worldbank.org/curated/en/115751468316166282/pdf/514320WP0WB1CS10Box342028B01PUBLIC1.pdf

## Block tally
- Candidates in this block: 20 (Batch 41 worklist #81–100).
- Scored with D/E/B and individual rationale: 20/20.
- Claim/Evidence Use/Source/Relation records changed: 0.
- Batch 41 candidate scoring: 100/100 across six saved block reports, **before final prior-score/alias reconciliation**.
- Candidates remaining to score in Batch 41: 0; reconciliation, evidence-linkage/source-fit closure and global ledger integration remain open.

## Findings requiring follow-up
1. Biochemistry B/C are editorial/methodological statements, not source-supported biochemical facts.
2. Biodiversity A/B are directly supported; C needs a more direct monitoring/measurement source.
3. Bioinformatics and biomedical engineering records have filename/internal-ID separator variants and broad source locators. NCBI A/C have good direct source material available; B needs a direct database source.
4. Calculus A–C have direct section-level support available, but the stored Source/EU references remain book-level/generic.
5. Cartography A is supported; B/C need direct contour/symbol and scale passages.
6. Civil society A–C need exact locators in the World Bank reference. Evidence-use descriptions include appropriate jurisdictional caveats, but no independent source has been established here.

## Limitations / next actions
This completes scoring of the 100-item Batch 41 worklist, not the full M13 audit. Do not silently treat all 100 as 100 globally unique accepted Claims until prior scored rows, aliases, overlaps and exclusions are reconciled against the frozen inventory. No Claim, Evidence Use, Source or Relation JSON was changed. PR #21 must remain open as Draft; do not change `main`. M13 is not complete.
