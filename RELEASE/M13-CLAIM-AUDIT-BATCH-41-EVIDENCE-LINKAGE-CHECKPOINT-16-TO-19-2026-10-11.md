# M13 Claim Audit — Batch 41 Evidence-Linkage Checkpoint 16–19
Date: 2026-10-11
Branch: m13-system-wide-depth-audit-2026-10-09
Scope: diagnostic source-fit review only. No Claim, Evidence Use, Source, or Relation JSON was changed. This checkpoint is not a D/E/B score and does not mark these candidates complete.

## Checkpoint 16 — Behavioral Economics and Biochemistry

### Behavioral Economics Basics
Source reviewed: Nobel Prize, 2002 Economic Sciences press release, https://www.nobelprize.org/prizes/economic-sciences/2002/press-release/
- A — “slice introduces basic concepts…”: source gives context for behavioral economics but cannot establish that the local corpus slice is adequately scoped. Treat as a corpus/editorial acceptance claim.
- B — Prospect theory and decisions under uncertainty: source directly supports the core statement about Kahneman/Tversky and prospect theory.
- C — Decisions can systematically depart from standard economic predictions: source supports the core synthesis; EU should pinpoint the relevant passage.
- Claim IDs and Evidence Use links were checked; EU descriptions remain generic. No score assigned.

### Biochemistry Basics
Stored source: OpenStax Biology 2e, Metabolism, https://openstax.org/books/biology-2e/pages/7-introduction
- A — local slice coverage/purpose: cannot be validated by an external metabolism chapter; needs corpus-internal acceptance criteria.
- B — interpretation depends on source, context, and applicability: generic epistemic rule not established by the metabolism chapter.
- C — basic knowledge does not replace specialist checking where conditions/measurements/professional assessment matter: not established by the linked chapter; needs a suitable cross-cutting policy/source or explicit internal rule.
- IDs and EU source links match. No score assigned.

## Checkpoint 17 — Biodiversity and Bioinformatics

### Biodiversity Basics
Stored source: OpenStax Biology 2e, “Preserving Biodiversity” (stored source family).
- A — biodiversity includes species diversity, genetic variation, and ecosystem diversity: core synthesis is plausible from the source family, but the EU needs a precise locator.
- B — species counts may change through the balance of speciation and extinction: the current biodiversity-preservation source does not directly establish this mechanism; add a better-matched source/locator before scoring.
- C — biodiversity assessment depends on area, time, and observation method: broad and not directly pinned to the current source; partial fit pending a specific passage.
- Claim IDs match filenames; EU links point to the stored source. No score assigned.

### Bioinformatics Basics
- Filename IDs use hyphens (for example, CLM-BIOINFORMATICS_BASICS-A); internal record IDs and linked pointers use underscores (for example, CLM_BIOINFORMATICS_BASICS_A). This is a separator-only variant. Preserve as an alias/reconciliation item; do not rewrite IDs without an authorized correction plan.
- A — computational methods applied to biological data; B — biological databases store/retrieve biological information; C — sequence analysis identifies similarities/differences. The stored NCBI Bookshelf landing page, https://www.ncbi.nlm.nih.gov/books/, is too broad to substantiate each claim specifically. Add direct NCBI/primary reference pages and locators.
- EU pointers are structurally consistent after separator normalization. No score assigned.

## Checkpoint 18 — Biomedical Engineering and Calculus

### Biomedical Engineering Basics
- Internal IDs use underscores while filenames use hyphens; Claim/EU references are internally consistent after separator normalization. Log for alias reconciliation; do not rewrite.
- A — engineering applied to biological/medical problems: NIBIB’s biomedical-engineering topic page, https://www.nibib.nih.gov/science-education/science-topics/biomedical-engineering, is well matched to the core.
- B — devices interact with biological systems for diagnosis, monitoring, or therapy: source is relevant, but needs an exact locator for the stated functions.
- C — field spans engineering, biology, materials science, and medicine: source is relevant but broad; pinpoint the interdisciplinary description.
- EU descriptions are generic. No score assigned.

### Calculus Basics
Stored source: OpenStax Calculus Volume 1 book landing page.
- A — limit describes function behavior as the input approaches a value; use the direct limits section (section 2.2) rather than only the book landing page.
- B — derivative as instantaneous rate of change where defined; add the direct derivative section locator.
- C — definite integral as accumulation under appropriate conditions; add direct integral/accumulation section locators.
- IDs and source links match; EU descriptions lack pinpoint locations. No score assigned.

## Checkpoint 19 — Cartography and Civil Society

### Cartography
Stored source: USGS Mapping 101, https://www.usgs.gov/science/science-explorer/maps-and-mapping/mapping-101
- A — cartography creates/uses maps to represent spatial information: source is relevant; EU needs a direct locator.
- B — topographic maps use symbols/contours for features and terrain: likely source-fit, but the exact claim needs a specific map/key/contour passage.
- C — map scale relates map distance to ground distance: core is directly supportable in basic mapping material, but EU lacks a pinpoint locator.
- IDs and source links match; no score assigned.

### Civil Society Basics
- A — civil society as voluntary associations distinct from state and commercial sector; B — possible forms include public groups, foundations, professional associations, NGOs and networks; C — roles may include public discussion, representation and public services. World Bank PDF and Britannica civil-society article are linked.
- Three independent Evidence Use records exist for A/B/C, each referencing the Britannica source with role `supports`. This is a stronger independence structure than in many reviewed families, but source independence and claim-specific fit still require verification; two records are not automatically independent merely because they are separate.
- Stored sources: World Bank PDF https://documents1.worldbank.org/curated/en/115751468316166282/pdf/514320WP0WB1CS10Box342028B01PUBLIC1.pdf and Britannica https://www.britannica.com/topic/civil-society.
- EU descriptions are relatively scoped; B notes that legal status/authority vary by jurisdiction.
- Civil-society Claim provenance lacks `created_from` fields present in many other claims. This is a metadata consistency observation, not a proven schema violation; verify against the governing schema/policy before treating as a defect.
- IDs/links were inspected. No score assigned.

## Gate status
- This checkpoint records diagnostics only; it does not certify truth, source independence, D/E/B, or batch completion.
- Do not modify substantive Claim/Evidence Use/Source/Relation records under this checkpoint.
- Remaining global work: reconcile all scored reports into one ledger; deduplicate repeated IDs across batches; normalize separator-only aliases without rewriting stored IDs; complete claim-specific source-fit and D/E/B assessment; inspect Relations and evidence independence; complete Human View/adversarial and independent review; only then define any separately authorized corrections and regression tests.


## Source-fit follow-up — direct locators verified after initial triage

This addendum improves locator specificity for three reviewed families. It remains diagnostic only: no Claim/Evidence Use/Source/Relation JSON changed, and no D/E/B scores were assigned.

### Biodiversity Basics — source fit refined
- OpenStax Biology 2e, section 47.1, “The Biodiversity Crisis”: https://openstax.org/books/biology-2e/pages/47-1-the-biodiversity-crisis
- The section explicitly describes biodiversity estimates at multiple organizational levels, and species-number change as the balance between speciation and extinction. This directly addresses the earlier gap for Claim B and strengthens the core of Claim A. Keep the wording scoped: biodiversity is measured in different ways depending on scientific goals; a single species-count measure does not exhaust biodiversity.
- For Claim C (area/time/observation-method dependence), section 47.1 supports scale and observation limitations in examples (e.g., species-area relationship and unobserved extinctions), but the full three-part methodological synthesis still needs exact claim wording and a locator/source that directly covers observation methods. Status: improved, not fully closed.

### Bioinformatics Basics — direct source candidates found
- NLM/NCBI Bookshelf, “Bioinformatics,” Collection Development Guidelines: https://www.ncbi.nlm.nih.gov/books/NBK518748/
  - Defines bioinformatics as organization and analysis of biological information using computers, including databases, retrieval mechanisms and data-analysis tools. This is a much better direct locator for Claim A and part of B than the NCBI Bookshelf landing page.
- NCBI Bookshelf, “BLAST Glossary”: https://www.ncbi.nlm.nih.gov/books/NBK62051/
  - Defines sequence alignment as matching nucleotide or amino-acid residues to assess similarity and possible homology. This directly supports the sequence-similarity component of Claim C.
- These sources improve topical fit, but the specific stored Evidence Use records still have generic descriptions. Do not count evidence-linkage quality as closed until the exact source passage is mapped to each claim and source independence is checked. Preserve filename/internal-ID separator variants as aliases for reconciliation only.

### Calculus Basics — direct section locators verified
- Limits: OpenStax Calculus Volume 1, section 2.2, “The Limit of a Function”: https://openstax.org/books/calculus-volume-1/pages/2-2-the-limit-of-a-function
- Derivatives: section 3.1, “Defining the Derivative”: https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative
- Definite integrals: section 5.2, “The Definite Integral”: https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral
- The direct sections support the respective core definitions (limit as input approaches a value; derivative as a limit/rate of change; definite integral as a generalized limit of sums/net area, where defined). Replace the book-level citation with these exact locators in a future separately authorized source-metadata correction; do not edit records during this audit checkpoint.

## Updated gate note
The source-fit triage has now identified better direct source locators for biodiversity, bioinformatics, and calculus, but Batch 41 remains unscored. A source being relevant does not itself prove that the stored Evidence Use record is sufficiently specific, that independent corroboration exists, or that all claim qualifiers are supported.
