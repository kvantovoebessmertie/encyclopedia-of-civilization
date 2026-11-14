# M13 thematic source-passage review — Statistics Basics — 2026-11-12

## Status and boundary

This is a source-passage desk review of the three Claims in `statistics-basics`, based on the exact M13 branch tree at parent revision `3900b9f3576426ecdf23af0b64f2b777bd5da38c`. It is not independent specialist review, final D/E/B scoring, a canonical-record correction, or publication approval.

**Disposition: all three Claims remain HOLD.** No Claim, Evidence Use, Source, Context, Scope, manifest, score ledger, or publication state was modified. This report is a noncanonical audit artifact only.

## Claim-by-claim findings

### CLM-STATISTICS_BASICS-A@1

**Claim:** Statistics provides methods for describing data, analyzing variation, and quantitatively supporting conclusions.

- Direct conceptual support located in OpenStax *Introductory Statistics 2e*, §1.1: it defines statistics as the collection, analysis, interpretation, and presentation of data, then distinguishes descriptive and inferential statistics. This is a good introductory fit for the core of the Claim.
- NIST/SEMATECH e-Handbook is a relevant engineering-statistics reference. Its official NIST overview identifies exploratory data analysis, measurement/process characterization, process modeling, comparisons, and reliability as top-level areas. It is an overview of the handbook, not a pinpoint for the full Claim.
- Existing `EU-STATISTICS_BASICS-A@1` is generic and contains no source-specific material or locator. A separate OpenStax Evidence Use exists (`EU-STATISTICS_BASICS-OPENSTAX@1`) and describes §1.1, but it also lacks an exact pinpoint and its source title should be checked against the canonical book title when any bounded correction is authorized.
- **Disposition: HOLD.** The Claim is broadly supported at introductory level, but the current primary Evidence Use does not demonstrate that support and the corroborating Evidence Use needs a reproducible locator.

### CLM-STATISTICS_BASICS-B@1

**Claim:** Statistical inference depends on method assumptions and data-collection quality; data that do not represent the process under study can produce unreliable conclusions.

- NIST's official e-Handbook overview and Chapter 1 (Exploratory Data Analysis) support the need to inspect data, investigate structure/outliers, and examine underlying assumptions before modeling or inference.
- OpenStax §1.1 explains population, sample, and sampling, including the purpose of using a sample to learn about a population. This is relevant to representativeness, but it is not currently linked as an Evidence Use for this Claim.
- Existing `EU-STATISTICS_BASICS-B@1` describes NIST sections about exploratory analysis and model assumptions, but gives no chapter subsection, page, heading, or other exact locator. Its description also combines two ideas—method assumptions and representativeness—that need separate pinpoint-level support.
- **Disposition: HOLD.** The method-assumption portion has a plausible direct NIST basis; the representativeness portion needs a precise source passage or a separately linked source. Do not infer that a generic reference to the handbook proves both parts.

### CLM-STATISTICS_BASICS-C@1

**Claim:** Experimental studies distinguish explanatory and measured response variables; random assignment helps reduce the influence of lurking factors, while an observed difference alone does not establish causation.

- OpenStax *Introductory Statistics 2e*, §1.4 “Experimental Design and Ethics” directly discusses explanatory and response variables, lurking variables, random assignment, and why a non-randomized comparison (its vitamin E example) does not prove causation. This is a strong introductory source fit for the Claim's central distinction.
- Existing `EU-STATISTICS_BASICS-C-OPENSTAX@1` correctly names §1.4 and describes the relevant passage, but does not provide a precise subheading/example locator or a quotation/extract sufficient for reproducibility.
- Existing `EU-STATISTICS_BASICS-C@1` refers generally to the NIST handbook and does not identify a relevant chapter or passage. NIST's landing page alone is not enough to substantiate the random-assignment/causality portion.
- **Disposition: HOLD.** The OpenStax passage is direct and well matched, but the current Evidence Use still needs a stable exact pinpoint and the generic NIST linkage should not be treated as independent proof of the experimental-design statements.

## Cross-record observations

1. Three Claims are present and each has at least one Evidence Use linked to the intended Claim. No Claim-to-Evidence Use mislink was observed in the records inspected.
2. Claim A has a second OpenStax Evidence Use; Claim C has a separate OpenStax §1.4 Evidence Use. These are useful source distinctions, but no independence score is assigned here.
3. The primary NIST Source record identifies the official NIST/SEMATECH handbook landing page. That page is an entry point to a multi-chapter handbook, not a sufficiently precise locator for any individual proposition.
4. The README's OpenStax §1.1 and §1.4 links are consistent with the official OpenStax chapter pages reviewed. The source records should preserve exact section identity and stable chapter URLs.
5. The Scope correctly excludes choosing a particular model, checking assumptions on real data, professional statistical analysis, and ethics/legal approval. Keep these boundaries.

## Required next steps

- For Claim A, add an exact locator to the NIST handbook passage(s) actually used, or explicitly treat OpenStax §1.1 as the direct support and provide its pinpoint. Keep the descriptive/inferential distinction accurate.
- For Claim B, split the support into (a) method-specific assumptions / exploratory checks and (b) sampling/representativeness. Add an exact NIST locator for (a) and a direct sampling source locator for (b), if the full wording is retained.
- For Claim C, record the exact OpenStax §1.4 subsection/example headings for explanatory/response variables, lurking variables, random assignment, and the vitamin E observational comparison. Reassess whether the generic NIST Evidence Use is necessary.
- Any canonical edit requires a bounded authorization, versioned record changes, updated tests/manifests where required, and exact-head CI. Do not silently rewrite published records from this desk review.

## Sources reviewed

- NIST/SEMATECH Engineering Statistics Handbook official overview: https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook
- NIST/SEMATECH e-Handbook, Chapter 1: Exploratory Data Analysis (official NIST publication page): https://www.nist.gov/publications/nistsematech-e-handbook-statistical-methods-chapter-1-exploratory-data-analysis
- OpenStax, *Introductory Statistics 2e*, §1.1: https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms
- OpenStax, *Introductory Statistics 2e*, §1.4: https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics
