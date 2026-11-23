# M13 thematic source-passage review — Biostatistics Basics — 2026-11-12

## Status and boundary

Reviewed the three Claims, three Evidence Uses, the MeSH Source, Context and Scope in `biostatistics-basics` against the M13 branch content at parent revision `3900b9f3576426ecdf23af0b64f2b777bd5da38c`.

**Disposition: all three Claims remain HOLD.** The NCBI MeSH source is authentic and directly supports the field definition, but it is a controlled-vocabulary scope note, not a sufficient source for the broader statistical methods and interpretation claims. All three Evidence Uses are generic. No canonical record, manifest, score, or publication state was changed.

## Claim-by-claim findings

### CLM_BIOSTATISTICS_BASICS_A@1

**Claim:** Biostatistics applies statistical methods to biological, medical, and public-health data.

- NCBI MeSH, descriptor “Biostatistics” (D056808), defines the field as applying statistics to biological systems and organisms, including retrieval/collection, analysis, reduction, and interpretation of qualitative and quantitative data.
- NCI Dictionary of Cancer Terms independently defines biostatistics as collecting and analyzing biological or health data using statistical methods.
- The current Source identity, NCBI MeSH — Biostatistics, is appropriate for the core field definition. However, the source URI is the broad MeSH search URL (`?term=Biostatistics`) rather than the stable descriptor page/identifier D056808.
- `EU_BIOSTATISTICS_BASICS_A@1` is generic and contains no definition, scope note, or pinpoint.
- **Disposition: HOLD.** Strong support exists for the biological/health domain, but the Evidence Use needs to cite the actual MeSH descriptor and avoid expanding “biological systems and organisms” into all public-health data without a suitable supporting passage.

### CLM_BIOSTATISTICS_BASICS_B@1

**Claim:** Biostatistical analysis can describe populations, quantify uncertainty, compare groups, and evaluate associations or effects under stated assumptions.

- CDC's *Field Epidemiology Manual*, Chapter 8 “Analyzing and Interpreting Data”, provides direct examples of descriptive statistics, measures of association, risk ratios/odds ratios, significance tests, confidence intervals, and interpretation limits.
- CDC's *Principles of Epidemiology*, Lesson 1 §4, describes design, conduct, analysis, and interpretation of analytic epidemiologic studies, including comparison groups and measures of association.
- MeSH's one-sentence field definition is not enough to substantiate this list of capabilities.
- `EU_BIOSTATISTICS_BASICS_B@1` is generic and links only the MeSH descriptor; it does not identify any methods passage.
- **Disposition: HOLD.** The Claim is broadly reasonable but requires additional source records/Evidence Uses with specific CDC or equivalent methodological passages. “Under stated assumptions” must be supported by the selected method-specific source, not treated as a universal generic assumption.

### CLM_BIOSTATISTICS_BASICS_C@1

**Claim:** Interpretation depends on study design, measurement quality, sampling, model assumptions, and the population to which the analysis applies.

- CDC's *Field Epidemiology Manual*, Chapter 7 “Designing and Conducting Analytic Studies in the Field”, discusses study design, comparison-group selection, and the distinction between randomized and observational studies.
- CDC's Chapter 8 “Analyzing and Interpreting Data” explicitly cautions that observed associations can arise from chance, selection bias, information bias, confounding, or other design/execution/analysis errors; it also explains that confidence intervals reflect sampling uncertainty.
- CDC's “Collecting Data” chapter discusses sample selection, generalizability, probability and nonprobability sampling.
- The current MeSH definition does not directly support this multi-part interpretation claim. `EU_BIOSTATISTICS_BASICS_C@1` is generic.
- **Disposition: HOLD.** The Claim has direct candidate support across several CDC chapters, but it is a composite statement and each component needs its own traceable locator. “Model assumptions” needs a specific methodological source, not an inference from the general biostatistics definition.

## Cross-record findings

1. The three Claim-to-Evidence Use references point to the intended Claim IDs, but the Evidence Use descriptions are all generic.
2. The MeSH Source record should use a stable descriptor URI for D056808 rather than a search-results URL. The NCBI MeSH Browser page is a suitable candidate.
3. MeSH is a controlled vocabulary and its scope note is suitable for defining the discipline, not for certifying the validity or completeness of individual statistical methods.
4. The Claims use internal IDs with underscores while the record filenames use hyphens. This resembles the known separator-only filename/internal-ID alias pattern in the corpus; it is not by itself evidence of a broken Claim/Evidence Use link. Do not mass-rename records.
5. Context and Scope are broad editorial framing and do not supply evidence for the individual Claims.

## Required next steps

- Version the MeSH Source to a stable descriptor identity/URI only under bounded authorization; update the associated Evidence Use with the exact D056808 scope note and its limits.
- Add separate, claim-specific Source/Evidence Use pairs for CDC Chapters 7, 8, and the “Collecting Data” chapter as needed. Record exact headings/subsections and state which clause of each Claim they support.
- Consider narrowing Claim A to “biological systems and organisms” or add an independent health/public-health definition source to justify its broader wording.
- Split or explicitly map the multiple components in Claims B and C so no single generic source is presented as supporting every clause.
- Any canonical edit requires bounded authorization, versioned record changes, required test/manifest updates, and exact-head CI. This desk review does not authorize canonical changes.

## Sources reviewed

- NCBI MeSH, “Biostatistics” (D056808): https://www.ncbi.nlm.nih.gov/mesh/68056808
- NLM MeSH Browser, Biostatistics descriptor D056808: https://meshb.nlm.nih.gov/record/ui?ui=D056808
- NCI Dictionary of Cancer Terms, “biostatistics”: https://www.cancer.gov/publications/dictionaries/cancer-terms/def/biostatistics
- CDC Field Epidemiology Manual, Chapter 7: https://www.cdc.gov/field-epi-manual/php/chapters/design-conduct-analyze-field-studies.html
- CDC Field Epidemiology Manual, Chapter 8: https://www.cdc.gov/field-epi-manual/php/chapters/analyze-interpret-data.html
- CDC Field Epidemiology Manual, “Collecting Data”: https://www.cdc.gov/field-epi-manual/php/chapters/collecting-data.html
- CDC, *Principles of Epidemiology*, Lesson 1 §4: https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section4.html
