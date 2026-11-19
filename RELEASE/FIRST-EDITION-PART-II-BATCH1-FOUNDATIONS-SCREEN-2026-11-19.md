# First Edition — Part II Foundations and Natural Sciences Screening Batch 1

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `62c75dc7468e7b6d388eb99d39701019dd898248`  
Post-inspection integrity check: all 89 record-file blob SHAs are unchanged at `c479d66e2c2c40719ad862bf6d3d3a1740a259ff` (tree comparison).  
Status: **9/9 SLICES SCREENED; 89/89 CANONICAL JSON RECORDS FETCHED AND PARSED; ALL 9 HOLD**

## 1. Scope

This report screens the first bounded batch from `FIRST-EDITION-PART-II-STRUCTURAL-GAP-TRIAGE-2026-11-19.md`:

- ratios-and-percentages
- probability-basics
- algebra-basics
- matter-basics
- acid-base-basics
- analytical-chemistry-basics
- earth-system-basics
- oceanography-basics
- astronomy-observation-basics

The 89 canonical JSON records were read at the same pinned inspection HEAD. A later repository-tree comparison confirms that all 89 record-file blob SHAs remained unchanged at the subsequent branch HEAD shown above. No canonical file was modified. This is a record-level screening recommendation, not a publication allowlist.

## 2. Inventory and version profile

| Slice | JSON records | Current version profile | Screening result |
|---|---:|---|---|
| ratios-and-percentages | 10 | all listed records @1 | HOLD |
| probability-basics | 10 | all listed records @1 | HOLD |
| algebra-basics | 11 | all listed records @1 | HOLD |
| matter-basics | 9 | all listed records @1 | HOLD |
| acid-base-basics | 11 | Source/Claims/Context/Scope/IUPAC corroboration @1; EU-A/B/C @2 | HOLD |
| analytical-chemistry-basics | 11 | all listed records @1 | HOLD |
| earth-system-basics | 9 | all listed records @1 | HOLD |
| oceanography-basics | 9 | all listed records @1 | HOLD |
| astronomy-observation-basics | 9 | all listed records @1 | HOLD |
| **Total** | **89** | **3 Evidence Use records are v2; other listed records are v1** | **9 HOLD** |

The inventory comprises 27 Claims, 30 Evidence Use records, 14 Sources, 9 Contexts and 9 Scopes. Three additional Evidence Use records provide independent corroboration in algebra, acid-base chemistry and analytical chemistry.

## 3. Slice-by-slice findings

| Slice | Records | Decision | Finding and blocker |
|---|---:|---|---|
| `ratios-and-percentages` | 10 | **HOLD** | Claim/Evidence Use mapping is misaligned: the primary NIST SP 811 source supports SI value conventions and percent notation (§7.10.2), not the general ratio definition. OpenStax §5.4 directly defines ratios; §6.1 defines percent, but the current OpenStax Source points only to §5.4. EU-A/B have no claim-specific locators. A third Claim is named `CLM-RATIOS_AND_PERCENTAGES-CONTEXT`, not `-C`; preserve its canonical ID. |
| `probability-basics` | 10 | **HOLD** | Claims A/B are substantive, but both EUs point to a NIST/SEMATECH landing page without locators. OpenStax Introductory Statistics 2e §3.1 directly supports probabilities in [0,1] and the complement identity; the current OpenStax Source/EU is attached to the separate MODEL Claim. The MODEL Claim ID is not `-C`; preserve its canonical ID. |
| `algebra-basics` | 11 | **HOLD** | Three substantive Claims and a separate UMN corroboration for Claim B exist. The primary OpenStax Source is a book landing page and EU-A/B/C have generic descriptions without pinpoints. UMN corroboration is limited to Claim B. Exact sections and rights boundary remain open. |
| `matter-basics` | 9 | **HOLD** | Three substantive Claims are present. The only Source is OpenStax Chemistry 2e §1 introduction; all three EUs are generic and lack claim-specific pinpoints. Verify direct sections for elements, compounds and mixtures; rights boundary remains open. |
| `acid-base-basics` | 11 | **HOLD** | Strongest evidence structure in this batch: EU-A/B/C are v2 and include §14.1/§14.2/§14.6 locators; IUPAC independently supports the activity-based pH definition. However, the OpenStax Source URI is `14-summary` while the EUs cite different chapter sections; normalize source identity/locator linkage. Keep the distinction between activity-based pH and concentration approximation. |
| `analytical-chemistry-basics` | 11 | **HOLD** | Three substantive Claims exist. NIST Source is a tutorial landing page and EU-A/B/C are generic without locators. IUPAC corroboration supports Claim A's definition only; it does not establish Claims B/C about method/sample/data quality and calibration/model range. |
| `earth-system-basics` | 9 | **HOLD** | Three Claims are plausible but broad. NASA Source is the Earth portal and all EUs are generic; no exact page/section supports components, cross-component interaction, or multi-domain observation. Claim C is especially broad and needs a direct locator or narrower wording. |
| `oceanography-basics` | 9 | **HOLD** | All three Claims describe the purpose, evidence boundary and limitations of the slice rather than substantive oceanography propositions. NOAA Ocean Exploration is a broad portal and EUs contain no locators. Replace the editorial placeholders with falsifiable subject-matter Claims before evidence review. |
| `astronomy-observation-basics` | 9 | **HOLD** | Claims B/C concern multi-band observation and telescopes, but the NASA Universe overview is too broad and EUs have no pinpoints. Claim A is a general universe definition, not an observation-method proposition. Add direct NASA/observatory sources and narrow the Claims to observational astronomy. |

## 4. Source-fit corrections established during screening

### Ratios and percentages

The current NIST SP 811 URL is Chapter 7, “Rules and Style Conventions for Expressing Values of Quantities.” Its §7.10.2 directly addresses the percent symbol as 0.01 and formatting, but it is not a general introductory definition of a ratio. OpenStax Contemporary Mathematics §5.4 directly defines ratios as comparisons of two quantities; §6.1 directly defines percent as a number per hundred and converts percent to decimal/fraction form. The current OpenStax Source points to §5.4 only. Reassign the evidence links and create/identify an exact §6.1 Source locator before any INCLUDE consideration.

### Probability

OpenStax Introductory Statistics 2e §3.1 directly supports both the interval (0 leq P(A) leq 1) and (P(A)+P(A')=1). The current NIST/SEMATECH e-Handbook root URL is not a claim-specific locator. The existing OpenStax Source is connected to the MODEL Claim, not the two primary Claims. A direct §3.1 Source/EU chain is needed.

### Acid-base chemistry

The current EUs identify §14.1 (Brønsted–Lowry definitions), §14.2 (pH/pOH, with a stated concentration-only boundary) and §14.6 (buffers). The independent IUPAC pH Evidence Use is important because the Claim defines pH using hydrogen-ion activity. The canonical OpenStax Source URL currently points to the chapter summary page rather than the specific sections named by the EUs. Normalize the Source identity/URI and exact locators; do not collapse the activity-based definition into the concentration approximation.

## 5. Rights and reuse screen — preliminary, not legal clearance

| Source family | Current public terms located | Release implication |
|---|---|---|
| OpenStax Contemporary Mathematics, Introductory Statistics 2e, College Algebra 2e and Chemistry 2e | CC BY-NC-SA 4.0; attribution and ShareAlike apply to reused/adapted content; NonCommercial restricts commercial reuse. The book prefaces also prohibit LLM training or ingestion without prior written permission. | Do not copy/adapt textbook expression into the corpus or ingest full text into an AI/training pipeline without prior permission. For independently written factual summaries, the rights reviewer must assess the actual expression used; do not assume either that citation alone triggers ShareAlike or that all reuse is unrestricted. |
| IUPAC Gold Book | Individual terms are stated as CC BY-SA 4.0; IUPAC asks parties seeking commercial reuse of the entire Gold Book to contact its Executive Director. | Record the exact term, attribution and any adaptation. Do not treat the individual-term licence as a blanket licence for the whole database. |
| NIST SP 811 and NIST/SEMATECH e-Handbook | NIST says information on its sites is generally public information unless marked copyrighted; NIST publications are generally public domain in the United States. The e-Handbook is jointly branded NIST/SEMATECH, so inspect page-level notices and third-party material. | Conditional source family, not blanket worldwide clearance. Preserve NIST credit and verify any marked/collaborator material and intended distribution jurisdictions. |
| NASA Earth and Universe pages | NASA material is generally reusable, including editorial reuse, with NASA credit; third-party credited material remains separately protected and use must not imply endorsement. | Use text/factual references only unless each image/media item is individually cleared. |
| NOAA Ocean Exploration | Site information is generally public domain unless otherwise noted; text should credit the contributing author and affiliation; selected media may be copyrighted. | The current oceanography slice still fails on subject-matter Claims regardless of the generally permissive text terms. |

Official rights references checked:
- OpenStax Contemporary Mathematics: https://openstax.org/books/contemporary-mathematics/pages/preface
- OpenStax Introductory Statistics 2e: https://openstax.org/books/introductory-statistics-2e/pages/preface
- OpenStax College Algebra 2e: https://openstax.org/books/college-algebra-2e/pages/preface
- OpenStax Chemistry 2e: https://openstax.org/books/chemistry-2e/pages/preface
- IUPAC Gold Book usage licence: https://goldbook.iupac.org/
- NIST copyright/disclaimers: https://www.nist.gov/copyrights-disclaimers
- NIST e-Handbook reference/citation page: https://www.itl.nist.gov/div898/handbook/index2.htm
- NASA Earth Science reuse FAQ: https://science.nasa.gov/earth/faq/
- NASA image/media guidelines: https://www.nasa.gov/nasa-brand-center/images-and-media/
- NOAA Ocean Exploration FAQ: https://oceanexplorer.noaa.gov/faqs/

The project-level first-edition licence and commercial-reuse policy remain project-owner decisions under `FIRST-EDITION-EDITORIAL-RIGHTS-AND-OPERATIONS-POLICY-2026-11-18.md`. This report does not resolve those decisions.

## 6. Cross-slice and record-graph checks

- All 89 files were valid JSON and their canonical IDs/types/versions were read.
- The primary Claim → Evidence Use → Source chains are present in the inspected records.
- The ratios and probability slices contain additional Claims with nonstandard suffixes (`-CONTEXT`, `-MODEL`); these are valid canonical IDs in this snapshot and must not be renamed by assumption.
- Context and Scope records in these slices point to Claim A only. Confirm whether that is the intended schema/application boundary before treating the Context/Scope pair as slice-wide.
- No canonical record, Relation, allowlist, release manifest or `main` branch was changed.

## 7. Required remediation before reconsidering HOLD

1. Replace generic Evidence Use descriptions with claim-specific source sections, passages or definitions.
2. Correct the ratios/probability Source-to-Claim assignments and pin the exact OpenStax sections.
3. Normalize the acid-base Source URI against its three cited sections and preserve the separate IUPAC activity definition.
4. Add direct evidence for analytical-chemistry Claims B/C, earth-system Claims B/C and astronomy-observation Claims B/C.
5. Replace oceanography's three editorial placeholder Claims with substantive, falsifiable oceanography propositions and rebuild their Evidence Use chains.
6. Complete exact-item rights/attribution assessment against the project-owner-approved first-edition licence and distribution model.
7. Preserve all nine HOLD decisions until the remediations are versioned, independently checked and reviewed.

No automatic promotion is permitted. The next screening batch remains the second bounded group in the structural gap triage; it must not be used to bypass the blockers recorded here.
