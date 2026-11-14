# M13 — unassessed-risk content screen package 05

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue: exact 711-row `m13-unassessed-risk-screening.csv`, source revision `f26820e59b08b4036ad78302dad8118c51dac540`  
Scope: 20 additional Claim records selected from the queue after excluding the Claim IDs explicitly covered by the prior 14 November screening reports.  
State: **content-level desk screen; no risk metadata assigned; no canonical Claim/Evidence Use/Source edits; no D/E/B changes.**

## 1. Method and limits

For each Claim, inspected the exact Claim JSON, linked Evidence Use JSON, and registered Source identity/URI on the M13 branch. Rechecked the registered external source pages where available. This pass evaluates statement/source fit and routing only. It does not assign likelihood, severity, exposure, risk domains, final risk classes, D/E/B scores, specialist approval, or publication clearance.

The Evidence Use descriptions in this set are generic or source-level rather than reproducible Claim-specific passages. Even where the source supports the central proposition, the current Evidence Use record is not sufficient for a final evidence certification until a stable section/page/paragraph locator and Claim-specific support boundary are recorded.

## 2. Algebra — 3 Claims

Registered Source: OpenStax, *College Algebra 2e*, https://openstax.org/details/books/college-algebra-2e

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ALGEBRA_BASICS-A@1` | The statement that algebraic expressions consist of numbers, variables and operations is consistent with OpenStax §1.1, “Real Numbers: Algebra Essentials,” which introduces algebraic expressions and operations. | Direct conceptual support. Add a stable §1.1 pinpoint to the EU. |
| `CLM-ALGEBRA_BASICS-B@1` | The equation definition and solving by permissible transformations are supported by the equations material, including §2.2, “Linear Equations in One Variable,” and the book's treatment of equation-solving properties. The Claim should not imply every transformation preserves equivalence without its required conditions. | Direct but bounded support. Add a section pinpoint and retain the equivalence/valid-operation boundary. |
| `CLM-ALGEBRA_BASICS-C@1` | OpenStax §3.1 defines a function as a relation in which each input has exactly one output and identifies domain and range. This directly supports the Claim's mapping formulation. | Direct conceptual support. Add a stable §3.1 pinpoint to the EU. |

All three algebra Claims have correct local Claim→EU→Source identity links. Their EUs remain generic and have no pinpoint. No independent corroboration is established by the single OpenStax textbook.

## 3. Analytical chemistry — 2 Claims

Registered Source: NIST, *Tutorials in Analytical Chemistry*, https://www.nist.gov/programs-projects/tutorials-analytical-chemistry

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ANALYTICAL_CHEMISTRY_BASICS-B@1` | The Claim says analytical measurement quality depends on more than the instrument: method, sample and data processing also matter. NIST's page explicitly lists sample extraction/processing, data treatment, quantitative analysis, chromatography and chemical metrology. This supports the multi-factor framing at an introductory level. | Direct but broad support. Add exact NIST tutorial/video/slide locators for sample processing, data treatment and quantitative analysis. |
| `CLM-ANALYTICAL_CHEMISTRY_BASICS-C@1` | NIST lists calibration and analytical method validation tutorials. These are relevant to linking known quantities to measured response and checking method suitability. The landing page alone does not establish every detail of the Claim's calibration-model and measurement-range boundary. | Partial/bounded support. Obtain exact calibration and method-validation passages/materials; do not infer a validated range from the landing-page topic list. |

The NIST source is current and relevant, but the current EUs are generic and do not identify a particular tutorial, slide, or video segment.

## 4. Archaeology — 2 Claims

Registered Source: Smithsonian Tropical Research Institute, *Archaeology*, https://stri.si.edu/discipline/archaeology

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ARCHAEOLOGY_BASICS-A@1` | STRI describes archaeological research using material culture, animal and human bones, plant microfossils, genetic and biochemical analysis to study past societies. This supports the Claim's broad account of studying past human societies through material and other surviving evidence. | Direct conceptual support within the STRI research context. Add a pinpoint and avoid treating one institute's regional programme page as a complete disciplinary definition. |
| `CLM-ARCHAEOLOGY_BASICS-C@1` | STRI demonstrates multidisciplinary comparison across material, biological and other evidence lines. The page does not explicitly establish the Claim's stronger methodological rule that finds must be interpreted in their discovery context. | Partial support. Add an authoritative archaeological-context/provenience source or narrow the statement to the methods actually described. |

## 5. Archival description and archival science — 5 Claims

Registered sources:
- Society of American Archivists, *Describing Archives: A Content Standard* (DACS), https://saa-ts-dacs.github.io/
- Society of American Archivists, *Archives 101: Basic Principles*, https://www2.archivists.org/groups/diverse-sexuality-and-gender-section/information-for-community-archives-archives-101-basic-principles

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ARCHIVAL_DESCRIPTION_BASICS-B@1` | Claim concerns distinguishing records from non-record materials and consistent organizational handling. DACS is a standard for describing archives, papers and manuscript collections; the inspected DACS contents focus on description, identity, content, access/use, appraisal and related materials. The registered source does not directly establish the records/non-records distinction as stated. | HOLD for source-fit remediation. Add a records-management authority that directly defines records and non-record materials, or narrow the Claim to archival description. |
| `CLM-ARCHIVAL_DESCRIPTION_BASICS-C@1` | DACS includes custodial history, appraisal/destruction/scheduling information, access conditions and description control. Its principles also address lifecycle and administration information. This partially supports linking description to lifecycle and retention, but the Claim's “responsible organization” element needs a direct creator/records-management pinpoint. | Partial support. Add exact DACS elements and an appropriate records-management/creator-context source; preserve jurisdiction and records-system scope. |
| `CLM-ARCHIVAL_SCIENCE-A@1` | Archives 101 describes processing as appraisal, arrangement, description and preservation, and explains that these activities preserve collections and make them accessible. The Claim additionally names acquisition/accessioning as a distinct function. | Partial support. The registered page supports four core processing functions and access, but does not fully enumerate accessioning. Add a specific accessioning/acquisitions source or qualify the list. |
| `CLM-ARCHIVAL_SCIENCE-B@1` | Archives 101 states the principle of provenance: materials from different creators should not be intermingled, preserving the ability to understand the creator and authenticate origins. This directly supports the Claim. | Direct support. Add a pinpoint to the “Principle of Provenance” passage. |
| `CLM-ARCHIVAL_SCIENCE-C@1` | Archives 101 links provenance and keeping a creator's materials together to understanding the creator and authenticating origins. This supports the context/collection-level principle, but does not fully define all archival-description structures or levels. | Direct but bounded support. Add the provenance passage and avoid implying a complete description model from this short overview. |

DACS is a U.S. archival-description standard and should not be represented as universal records-management law. The Archives 101 page is an introductory SAA community-archives resource, not a comprehensive archival code.

## 6. Art history — 3 Claims

Registered Source: Smarthistory, *The Basics of Art History*, https://smarthistory.org/curated-guide/the-basics-of-art-history/

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ART_HISTORY_BASICS-A@1` | The Smarthistory guide introduces art history through visual analysis and historical context and links visual interpretation to wider contexts. The registered landing page is a curated guide rather than a single disciplinary definition. | Direct at introductory level, but broad. Add the specific “Understanding art, an introduction” and historical-context lesson locators. |
| `CLM-ART_HISTORY_BASICS-B@1` | The guide explicitly lists line, shape/form, color, space, texture, light/shadow and principles of composition. A separate Smarthistory formal-analysis lesson discusses these elements. | Direct support. Add stable lesson/section locators; retain the distinction between visual description and interpretation. |
| `CLM-ART_HISTORY_BASICS-C@1` | The registered guide includes a linked introduction to iconography and iconographic analysis. The top-level landing page alone does not supply the actual explanatory passage. | Relevant source candidate, but pinpoint is missing. Add the exact iconography lesson as a separately identified Source/EU if the current source record does not resolve to it. |

## 7. Artificial intelligence — 3 Claims

Registered Source: NIST AI landing page, https://www.nist.gov/artificial-intelligence

A material source-identity/currentness issue was found: the registered URI now redirects to NIST's “Super intelligence” page. The current page describes NIST research, testing/evaluation, guidelines, standards and responsible deployment; it no longer functions as the stable generic AI overview implied by the local Source identity.

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-A@1` | The Claim says AI systems may use models and algorithms to process data and produce results. The redirected NIST page discusses models and applications but does not provide a clear, stable general definition matching the Claim. | HOLD for Source identity/currentness remediation. Do not treat the redirected landing page as direct support for the definition. |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-B@1` | The Claim says system behaviour depends on data, model, goals and conditions of use. The current NIST page supports the importance of use cases, evaluation requirements and deployment context, but does not directly establish all four dependencies. | Partial support. Add a stable NIST AI RMF or other authoritative source with explicit system/data/context passages. |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-C@1` | The Claim requires evaluation to consider context, data limitations and quality criteria. NIST's current page discusses testing/evaluation and trustworthy/responsible deployment, but the registered landing page does not provide Claim-specific data-quality or context-limitation passages. | Partial support. Add an exact AI risk/evaluation framework source and pinpoint; retain application-specific evaluation boundaries. |

No automatic substitution of a new NIST source is made. The Source identity and any replacement must be handled through a bounded, versioned correction with regression coverage.

## 8. Asset management — 2 Claims

Registered Source identity says ISO 55000:2024, *Asset management — Vocabulary, overview and principles*, but the stored URI is `https://www.iso.org/standard/83054.html`, which identifies **ISO 55001:2024**, *Asset management system — Requirements*. The ISO 55000:2024 page is `https://www.iso.org/standard/83053.html`. This is a confirmed Source identity/URI mismatch; it must not be silently corrected.

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ASSET_MANAGEMENT_BASICS-A@1` | The registered URI currently opens ISO 55001:2024, whose overview describes lifecycle management, organizational objectives, value, risk and cost. The Source record's stated ISO 55000 identity is wrong for that URI. | HOLD for bounded Source identity correction and exact standard-version verification. Both ISO 55000 and ISO 55001 may be relevant, but they are distinct records/standards. |
| `CLM-ASSET_MANAGEMENT_BASICS-B@1` | The current URI's ISO 55001:2024 overview explicitly describes balancing asset performance, risk and expenditure to meet organizational goals. This is a close match to the Claim's performance/risk/cost balance over the lifecycle. | Direct conceptual support from ISO 55001:2024, but the local Source identity is mislabeled as ISO 55000. Correct only under bounded authorization; add exact clause/preview locator and preserve the standard distinction. |

The ISO public preview supports source identity and broad scope, not a substitute for the full paid standard text. Do not invent clause-level pinpoint references from the landing page.

## 9. Batch accounting and integrity

- Additional Claim records inspected: **20/20**.
- Claims with direct conceptual support at a bounded introductory level: algebra A/B/C; analytical chemistry B; archaeology A; archival science B; art history B; art history A (broad); asset management B (URI mismatch must be corrected first).
- Partial or incomplete support: analytical chemistry C; archaeology C; archival description C; archival science A/C; art history C; AI B/C.
- HOLD for source-fit or identity remediation: archival description B; AI A; asset management A; asset management B pending Source identity correction.
- Confirmed Source identity/URI defects: **1** (asset management Source points to ISO 55001 while labeled ISO 55000).
- Source currentness/redirect issue: **1** (NIST AI landing page now redirects to a “Super intelligence” page).
- Generic or non-pinpoint Evidence Use records: **20/20**.
- Risk metadata assigned: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Specialist adjudications completed: **0**.
- Human View / publication approvals: **0**.

This package is a bounded content-level source-fit screen. It is not risk clearance, final D/E/B adjudication, independent review, canonical correction authorization, or M13 closure.

## 10. Required next actions

1. Route the ISO 55000/55001 identity mismatch for a bounded Source correction, exact version check, and regression test.
2. Replace or version the NIST AI landing-page reference with a stable, explicitly identified AI framework/definition source; do not silently relabel the redirected page.
3. Add exact OpenStax, NIST analytical chemistry, SAA/DACS, STRI and Smarthistory locators through bounded Evidence Use version updates.
4. Add supplemental sources for archaeological context, records/non-record distinction, archival accessioning and AI data-quality/context claims.
5. Keep all reviewed Claims on HOLD until exact evidence pinpoints, specialist/Human View, source-independence, rights/attribution and release gates are separately satisfied.
