# First Edition — bounded screen of five remaining structural-map slices

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `09be8ce8e5733a3a8e533732a19cf1fbc841ef11`  
Workstream: WP1 — first-edition corpus selection  
Status: **47/47 record files screened; all five slices remain HOLD; no canonical changes**

## 1. Scope and controls

This bounded screen covers only the five slices identified by the controlling Part II structural-gap triage:
- `ancient-civilizations-basics` — 11 records
- `anthropology-basics` — 9 records
- `linguistics-basics` — 9 records
- `philosophy-basics` — 9 records
- `ethics-basics` — 9 records

All 47 JSON record files were read at the inspection baseline. This is a record-level screening of claim substance, evidence-use linkage, source locator quality, and basic scope/context alignment. It is not a complete subject-matter peer review, legal rights clearance, or publication approval.

Controls:
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation was modified.
- No publication_status or completion_status value was changed or treated as release eligibility.
- No INCLUDE or EXCLUDE decision was created.
- Existing HOLD dispositions are preserved.
- No allowlist, preview, or publication artifact was created.
- No M13 work was started and no closed audit was repeated.
- Findings below are screening recommendations and evidence gaps, not owner approvals.

## 2. Summary

| Slice | Records | Screening outcome | Principal reason |
|---|---:|---|---|
| ancient-civilizations-basics | 11 | HOLD | Two claims have plausible subject-specific source coverage, but Evidence Use entries lack pinpoint locators and the generic OpenStax EU descriptions do not identify supporting passages; claim C is broad and under-specified |
| anthropology-basics | 9 | HOLD | All three Claims are meta-statements about the slice or general interpretation, not substantive anthropology knowledge; all three EU entries use a generic description without a locator |
| linguistics-basics | 9 | HOLD | All three Claims are meta-statements rather than substantive linguistics knowledge; Evidence Use has no pinpoint locator; source URL was not independently verified during this screen |
| philosophy-basics | 9 | HOLD | All three Claims are generic meta-statements rather than philosophical concepts or arguments; listed Stanford Encyclopedia of Philosophy URL returned 404 at inspection |
| ethics-basics | 9 | HOLD | All three Claims are generic meta-statements; the source is a valid SEP entry on the definition of morality, but the EU entries contain no pinpoint locator and do not specify which parts support the claims |

**Totals: 5/5 slices screened; 47/47 records read; 0 INCLUDE; 5 HOLD; 0 canonical changes.**

## 3. Slice findings

### 3.1 ancient-civilizations-basics — 11 records

Claims:
- `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1`: settlement, labour specialisation and social stratification.
- `CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1`: regional variation in agriculture, settlement and demography.
- `CLM-ANCIENT_CIVILIZATIONS_BASICS-C@1`: archaeological and written evidence for ancient societies.

Evidence:
- `EU-ANCIENT_CIVILIZATIONS_BASICS-A@1`, `-B@1`, and `-C@1` point to `SRC-ANCIENT_CIVILIZATIONS_BASICS@1`, but each only says the source is used “within the stated material”; no chapter/section/page/paragraph locator is recorded.
- `EU-ANCIENT-CIVILIZATIONS-SMITHSONIAN@1` points to `CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1` and `SRC-SMITHSONIAN-ANCIENT-AGRICULTURE@1`. Its description is directionally relevant to regional variation but still has no precise locator.

Source inspection:
- The OpenStax section “3.1 Early Civilizations” contains material on settled populations, farming, specialisation and social stratification (especially its paragraphs on attributes of early civilizations). It also cautions against treating older lifeways as having disappeared.
- The Smithsonian profile identifies Melinda Zeder’s 2011 article and its abstract describes multiple regional domestication processes and regional variation. This is relevant to the qualified wording of Claim B.
- These source observations support further targeted Evidence Use work, not release approval. The three generic EU records need exact locators and a precise statement of what each passage supports. Claim C may need narrower wording and a source that directly addresses the range and survival of archaeological/written evidence.

Context and scope both target Claim A. Their broad educational wording does not resolve the evidence gaps.

Disposition: **HOLD retained.**

### 3.2 anthropology-basics — 9 records

Claims:
- `CLM-ANTHROPOLOGY_BASICS-A@1`: says the slice introduces basic concepts and relations.
- `CLM-ANTHROPOLOGY_BASICS-B@1`: says interpretation depends on source, context and applicability.
- `CLM-ANTHROPOLOGY_BASICS-C@1`: says general knowledge does not replace specialist review.

These are statements about the educational package and general epistemic caution, rather than claims that teach anthropology. The three Evidence Use records each have only a generic description and no pinpoint locator. The American Anthropological Association’s current “What is Anthropology?” page describes the discipline’s broad approach and four pillars, but the stored source URL differs from the current indexed path and no precise passage is pinned.

Disposition: **HOLD retained.** Rework the Claims into substantive, bounded anthropology propositions and pin the relevant AAA sections or other appropriate sources before reconsideration.

### 3.3 linguistics-basics — 9 records

Claims:
- `CLM-LINGUISTICS_BASICS-A@1`: says the slice describes basic concepts and relations.
- `CLM-LINGUISTICS_BASICS-B@1`: says interpretation requires source, context and applicability limits.
- `CLM-LINGUISTICS_BASICS-C@1`: says generalised information does not replace specialist verification.

All three Claims are meta-statements rather than substantive linguistics knowledge. All three Evidence Use records contain generic descriptions and no pinpoint locators. The stored Britannica linguistics URL was not independently validated in this screen.

Disposition: **HOLD retained.** Replace the meta-statements with actual linguistics propositions and provide source sections that directly support them.

### 3.4 philosophy-basics — 9 records

Claims:
- `CLM-PHILOSOPHY_BASICS-A@1`: says the slice describes basic concepts and relations.
- `CLM-PHILOSOPHY_BASICS-B@1`: says interpretation requires source, context and applicability limits.
- `CLM-PHILOSOPHY_BASICS-C@1`: says generalised information does not replace specialist verification.

All three Claims are generic meta-statements, not philosophical concepts, distinctions or arguments. The stored source URL `https://plato.stanford.edu/entries/philosophy/` returned 404. The Stanford Encyclopedia of Philosophy itself is active, but no replacement entry is selected here because a broad SEP index or a guessed entry is not an adequate substitute for the exact source intended by the record. The EU entries also lack pinpoint locators.

Disposition: **HOLD retained.** Select suitable topic-specific SEP entries or other scholarly sources, record exact locators, and replace the meta-claims with substantive propositions.

### 3.5 ethics-basics — 9 records

Claims:
- `CLM-ETHICS_BASICS-A@1`: says the slice describes basic concepts and relations.
- `CLM-ETHICS_BASICS-B@1`: says interpretation requires source, context and applicability limits.
- `CLM-ETHICS_BASICS-C@1`: says generalised information does not replace specialist verification.

The Claims are generic meta-statements rather than ethical concepts, theories, distinctions or arguments. The source `SRC-ETHICS_BASICS@1` points to the active SEP entry “The Definition of Morality”, a scholarly source with useful distinctions between descriptive and normative senses of morality. However, the three EU records only say the source is used within the stated material and provide no section locator or account of how the cited discussion supports each claim.

Disposition: **HOLD retained.** Build substantive ethics Claims and use exact SEP sections or additional suitable sources; do not treat a broad source match as evidence for the current meta-statements.

## 4. Cross-slice pattern

The four slices anthropology, linguistics, philosophy and ethics share a repeated template:
- Claim A describes what the slice contains.
- Claim B repeats a general source/context caution.
- Claim C repeats a generic specialist-review caveat.
- Evidence Use entries repeat a non-specific “source used within stated material” description.

This pattern creates the appearance of three Claims and three Evidence Use records per slice without delivering three substantive, independently assessable propositions. It should be corrected as a content-design issue across these four slices, not by merely adding more generic Evidence Use records.

The ancient-civilizations slice is materially stronger: it has specific historical propositions and two relevant source identities. Its outstanding problems are exact evidence locators, support mapping, and claim-level precision.

## 5. Next bounded actions

1. For ancient civilizations, locate exact OpenStax and Smithsonian passages and update Evidence Use only under a separately approved canonical-edit scope. Reassess Claim C’s wording and support.
2. For anthropology, linguistics, philosophy and ethics, draft substantive candidate Claims and evidence maps outside the canonical corpus first. Require precise locators and check that each source actually supports its linked Claim.
3. Resolve the broken philosophy source locator with an explicitly selected, topic-appropriate source; do not silently replace it with a general SEP homepage.
4. Re-run a focused cross-slice template audit after proposed content is prepared. Do not infer INCLUDE from improved evidence alone; preserve HOLD pending editorial, rights and owner gates.

## 6. Rights and release boundary

The existence of a public URL does not establish a reusable licence for the source text, images, tables or other protected expression. This screen does not clear rights or attribution. The four generic/template slices and the ancient-civilizations slice remain outside any public selection until evidence, editorial and rights decisions are separately resolved.
