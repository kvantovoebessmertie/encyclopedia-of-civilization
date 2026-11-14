# M13 Claim Audit — Batch 41 Scored Block 03
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: Batch 41 worklist candidates #21–40: algebra (2), analytical chemistry (3), anatomy (3), ancient civilizations (3), anthropology (3), antimicrobial resistance (3), archaeology (3).
Status: **20 Claims scored.** This is not M13 completion.

## Method
D = explanatory depth, E = claim-specific evidence fit, B = boundary discipline; each scored 0–3. Claim JSON, relevant Source JSON, and selected Evidence Use JSON were inspected; external source pages were checked. Scores describe support/traceability in the corpus, not whether an idea is generally plausible. No Claim, Evidence Use, Source or Relation JSON was modified.

## Claim-level results

| # | Claim ID | D | E | B | Rationale and disposition |
|---:|---|---:|---:|---:|---|
| 21 | `CLM-ALGEBRA_BASICS-B` | 2 | 2 | 3 | OpenStax College Algebra 2e §2.2 explicitly treats equations as equality conditions and describes solution sets and algebraic solving. “Permissible transformations” is mathematically sound but not fully supported by the stored book-level Source locator or generic EU text. Direct section locator recommended. |
| 22 | `CLM-ALGEBRA_BASICS-C` | 2 | 3 | 3 | OpenStax §3.1 defines a function as a relation assigning exactly one output to each input and explicitly defines domain/range as input/output values. Strong direct support for the statement. Stored Source still points to the book landing page and EU has no pinpoint locator. |
| 23 | `CLM-ANALYTICAL_CHEMISTRY_BASICS-A` | 2 | 1 | 3 | NIST tutorials cover chemical metrology, analytical methods, sample processing and data treatment, but the landing page does not itself define analytical chemistry as methods for measuring composition and properties. The claim is plausible but the source fit is indirect; add a direct authoritative definition or narrow the statement. |
| 24 | `CLM-ANALYTICAL_CHEMISTRY_BASICS-B` | 2 | 2 | 3 | NIST covers sample preparation/processing, instrument and method development, troubleshooting, data treatment and method validation, supporting the broad point that quality is not solely an instrument property. The exact full combination of instrument, method, sample and data processing is a synthesis; Evidence Use is generic. |
| 25 | `CLM-ANALYTICAL_CHEMISTRY_BASICS-C` | 3 | 3 | 3 | NIST’s dedicated Calibration tutorial directly defines calibration as relating a known analyte quantity to measured instrumental response and notes that model details matter; its Analytical Method Validation tutorial says validation demonstrates fitness for intended purpose. Strong support for the calibration and task-specific model/range qualification. The stored Source/EU should cite these exact tutorials. |
| 26 | `CLM-ANATOMY_BASICS-A` | 1 | 2 | 3 | The claim is a basic biological statement and is consistent with the NIGMS cells/tissues/organs/systems reference. The stored URL is a legacy-style NIGMS fact-sheet locator and could not be independently confirmed from the current search results; verify it or replace with a stable current NIGMS/NIH page. |
| 27 | `CLM-ANATOMY_BASICS-B` | 1 | 2 | 3 | The NIGMS reference is directly relevant to tissue/organ organization and the statement is narrowly framed. Source identity and Evidence Use align, but the current accessibility and exact passage need confirmation; add a direct locator for the multiple-tissue definition. |
| 28 | `CLM-ANATOMY_BASICS-C` | 2 | 1 | 3 | Organ systems are part of the named NIGMS topic, but the available source record does not establish a specific passage showing organs interacting to perform related functions, and the legacy URL could not be confirmed in current results. Keep as a likely correct basic claim but improve the source locator. |
| 29 | `CLM-ANCIENT_CIVILIZATIONS_BASICS-A` | 2 | 3 | 3 | OpenStax World History §3.1 directly describes settled populations, labor specialization and social stratification as characteristics of early civilizations. “Among other things” properly avoids making the list exhaustive. Strong claim-source fit. |
| 30 | `CLM-ANCIENT_CIVILIZATIONS_BASICS-B` | 3 | 2 | 3 | OpenStax §3.1 directly connects farming, settled populations, population growth, specialization and emerging urban settings, but the claim’s comparative statement that strength/direction varied by time and place is a qualified historical synthesis rather than a direct quotation. The qualifications reduce overgeneralization; more comparative sources would improve support. |
| 31 | `CLM-ANCIENT_CIVILIZATIONS_BASICS-C` | 2 | 2 | 3 | OpenStax explains that prehistoric groups without writing are studied through artifacts and archaeological evidence, while writing exists for some later societies. The claim appropriately qualifies written materials with “where preserved,” but the source does not fully establish the general source taxonomy for all ancient societies. |
| 32 | `CLM-ANTHROPOLOGY_BASICS-A` | 1 | 0 | 2 | The statement describes the editorial purpose of this corpus slice, not an independently documented fact about anthropology. The AAA overview explains the discipline but does not establish that this particular slice introduces the necessary concepts/relations. Reclassify as editorial metadata or document against the project’s own learning design; no record changed. |
| 33 | `CLM-ANTHROPOLOGY_BASICS-B` | 2 | 0 | 3 | Source/context/scope is sound general epistemic guidance, but the AAA source describes anthropology’s breadth and methods rather than directly supporting this generic interpretation rule. Claim type `documented_fact` is a questionable fit for a methodological principle. Needs a methodology/epistemology source or a different record type, subject to authorized correction. |
| 34 | `CLM-ANTHROPOLOGY_BASICS-C` | 2 | 0 | 3 | The AAA overview does not support the rule that introductory knowledge cannot replace specialist checking for claims depending on conditions, measurements or professional evaluation. This is a sensible safety/editorial principle but not evidenced as an anthropology fact. Use a governance/editorial guidance record or a direct source; no content change authorized here. |
| 35 | `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-A` | 1 | 3 | 3 | WHO’s AMR fact sheet explicitly defines resistance as microorganisms no longer responding to antimicrobial medicines. Direct, authoritative support. |
| 36 | `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-B` | 1 | 3 | 3 | WHO explicitly distinguishes antibacterials/antibiotics, antivirals, antifungals and antiparasitics. The claim matches this list. |
| 37 | `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C` | 2 | 3 | 3 | WHO One Health material directly connects human, animal, plant and environmental health, and WHO’s AMR materials explicitly include food systems and call for cross-sectoral action. Strong support for the claim’s multi-sector scope and conclusion. |
| 38 | `CLM-ARCHAEOLOGY_BASICS-A` | 2 | 3 | 3 | Smithsonian Tropical Research Institute’s archaeology overview directly describes archaeologists studying past societies through material culture, human/animal bones and other preserved evidence. Strong match for the core statement. |
| 39 | `CLM-ARCHAEOLOGY_BASICS-B` | 3 | 3 | 3 | STRI explicitly describes a multidisciplinary approach using human/animal bones, material culture, plant microfossils, genetic and biochemical analysis. The claim tracks the source’s actual methods closely. |
| 40 | `CLM-ARCHAEOLOGY_BASICS-C` | 3 | 2 | 3 | STRI’s multidisciplinary approach and comparative lines of evidence support combining material findings with context and other evidence. However, the general rule that interpretation requires independent lines of data is stronger than the source’s descriptive passage; use a methodological archaeology source for the independence/context principle. |

## External sources checked
- OpenStax, College Algebra 2e §2.2, “Linear Equations in One Variable”: https://openstax.org/books/college-algebra-2e/pages/2-2-linear-equations-in-one-variable
- OpenStax, College Algebra 2e §3.1, “Functions and Function Notation”: https://openstax.org/books/college-algebra-2e/pages/3-1-functions-and-function-notation
- NIST, Tutorials in Analytical Chemistry: https://www.nist.gov/programs-projects/tutorials-analytical-chemistry
- NIST, Calibration: https://www.nist.gov/video/calibration
- NIST, Analytical Method Validation: https://www.nist.gov/video/analytical-method-validation
- NIGMS, Cells, Tissues, Organs and Systems (stored legacy locator): https://www.nigms.nih.gov/education/fact-sheets/Pages/cells-tissues-organs-and-systems.aspx
- OpenStax, World History Volume 1 §3.1, “Early Civilizations”: https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations
- American Anthropological Association, “What is Anthropology?”: https://americananthro.org/practice-teach/what-is-anthropology/
- WHO, Antimicrobial resistance fact sheet: https://www.who.int/europe/news-room/fact-sheets/item/antimicrobial-resistance
- WHO, One Health: https://www.who.int/health-topics/one-health
- WHO, “The World Health Assembly adopts updated Global Action Plan on Antimicrobial Resistance (2026–2036)” (25 May 2026): https://www.who.int/news/item/25-05-2026-the-world-health-assembly-adopts-updated-global-action-plan-on-antimicrobial-resistance-%282026-2036%29
- Smithsonian Tropical Research Institute, Archaeology: https://stri.si.edu/discipline/archaeology

## Block tally
- Candidates in this block: 20 (Batch 41 worklist #21–40).
- Scored with D/E/B and individual rationale: 20/20.
- Claim/Evidence Use/Source/Relation records changed: 0.
- Batch 41 cumulative scored candidates: 40/100, pending final prior-score/alias reconciliation.
- Remaining candidates to score in Batch 41: 60, subject to overlap and evidence-fit gates.

## Findings requiring follow-up
1. Analytical chemistry A has a definition/source-fit gap; B is a synthesis; C is well supported by NIST but the source record needs exact tutorial locators.
2. Anatomy source URI is legacy-style and could not be confirmed in the current search results; all three claims need a stable current source/passage before closure.
3. Anthropology A is a slice/editorial statement; B/C are generic methodological guidance. The AAA overview does not evidence these statements, and `documented_fact` may be the wrong type.
4. Archaeology C needs a direct methodology source for context and independent lines of evidence.
5. Algebra B/C have good direct section-level support available, but the stored source and evidence links remain book-level/generic.

## Limitations / next actions
Scores are not a declaration that low-fit claims are false. They identify evidence and classification gaps. No content records were edited; substantive record changes remain outside this scoring-only authorization. Continue candidates #41 onward in the next block. PR #21 must remain open as Draft; do not change `main`. M13 is not complete.
