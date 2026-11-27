# Package A — Ancient Civilizations: Alternative Source and Rights Research

Date: 2026-11-21
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`
PR: #22 — `mvp-public-contribution-design-2026-10-11`
Research baseline: `ea2ace943219159e9bcebddc0249cd67a19e14e4`
Authorization: owner approved Package A for **research of alternative sources and rights only**.
Status: **RESEARCH DOSSIER — NO CANONICAL EDITS; ALL AFFECTED RECORDS REMAIN HOLD**

## 1. Authorization and strict boundary

The owner authorized Package A in the mode “first research alternative sources and rights.” This permits source discovery, edition comparison, locator verification, rights-term screening and preparation of recommendations.

It does not authorize:
- changing any canonical Claim, Evidence Use or Source JSON, including creating @2 versions;
- changing Context, Scope, Relations or any dependent record;
- changing any INCLUDE/HOLD/EXCLUDE disposition;
- changing the exact-version master, candidate denominator, allowlist, release manifest, preview or publication state;
- adopting a project-wide content licence or resolving R-01–R-10;
- changing `main`, merging PRs or publishing a first-edition artifact.

All current canonical versions remain @1. All 11 records in `ancient-civilizations-basics` remain as-is and the slice remains HOLD.

## 2. Canonical propositions and exact record scope rechecked

The current HEAD contains these three substantive Claims:

| Claim | Current proposition | Current Evidence Use |
|---|---|---|
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1` | Early civilizations were characterized, among other things, by settled settlements, labour specialization and social stratification. | `EU-ANCIENT_CIVILIZATIONS_BASICS-A@1` |
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1` | In some regions, development of agriculture was associated with changes in settlement patterns and demography, but the direction and strength of those relationships varied by time and place. | `EU-ANCIENT_CIVILIZATIONS_BASICS-B@1`; independent `EU-ANCIENT-CIVILIZATIONS-SMITHSONIAN@1` |
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-C@1` | Sources about ancient societies include archaeological evidence and written materials where preserved. | `EU-ANCIENT_CIVILIZATIONS_BASICS-C@1` |

The three OpenStax-linked Evidence Use records currently contain only the generic description “the indicated source is used within the stated material”; they have no pinpoint locator. The Smithsonian-linked EU already has a useful support-boundary description but no direct article locator. Existing Source identities point respectively to OpenStax §3.1 and a Smithsonian Profiles bibliographic record.

This research is directed at the three extant propositions. It does not broaden them or draft canonical replacements.

## 3. Strong alternative: Open Book Project's separately licensed edition of World History

### 3.1 Source identity

The Open Book Project hosts *World History, Volume 1, to 1500* by Ann Kordas, Ryan J. Lynch, Brooke Nelson and Julie Tatlock. Its own book description says it is adapted from OpenStax *World History, Volume 1, to 1500* and explicitly identifies the source version as OpenStax repository commit `3e17beda91`, which the project states was licensed CC BY 4.0. It warns that later OpenStax versions carry a different licence and that credited photographs/illustrations retain their own terms.

- Book overview and exact-version/licence statement: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/index.html
- Chapter 3, *Early Civilizations and Urban Societies*: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/early-civilizations-and-urban-societies.html
- Chapter 1, *Understanding the Past*: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/understanding-the-past.html
- Chapter 2, *Early Humans*: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/early-humans.html

**Assessment:** this is the strongest candidate for a rights-compatible textual reference route for the existing Claims, subject to independent verification of the exact upstream commit, attribution chain, the Open Book Project adaptation's own grant and third-party components. It is a separately prepared adaptation, not the same Source object as the live OpenStax 2023 edition and not an independent scholarly corroboration of that textbook.

### 3.2 Claim A — settlement, labour specialization and social stratification

The Open Book Project Chapter 3, section 3.1, contains directly relevant passages:
- early civilizations and settled populations: opening section, paragraphs describing agriculturally sustained settled populations;
- labour specialization and surplus: “Attributes of Early Civilizations,” paragraphs on surplus production, cities and specific tasks;
- social stratification: same section, paragraphs describing accumulated wealth, political/religious power and differences in wealth/status;
- concise recap: Chapter Review, “Summary — 3.1 Early Civilizations.”

The live OpenStax section independently confirms these same locator anchors:
- https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations
- section text: opening paragraphs and “Attributes of Early Civilizations,” especially paragraphs on surplus, specialization and stratification.

A more independent, case-specific scholarly companion is:
- *Dense urbanism and economic multi-centrism at third-millennium BC Lagash*, *Antiquity* 97(393), June 2023, DOI https://doi.org/10.15184/aqy.2023.36
- Publisher page: https://www.cambridge.org/core/journals/antiquity/article/dense-urbanism-and-economic-multicentrism-at-thirdmillennium-bc-lagash/2D27165A470831B32B9B29C72EBEF8AD
- The article reports dense urban occupation, distinct walled quarters, multiple foci of intensive industrial production and exploitation of varied surrounding environments.
- The publisher page identifies the article as open access under CC BY 4.0.

**Support boundary:** Lagash is a specific third-millennium BCE case. It can independently contextualize urban density and production specialization, but it does not alone establish that all early civilizations shared the same social structure or degree of stratification. Keep the broad textbook Claim appropriately qualified.

A second, narrower case study is:
- Twiss et al. (2024), “But some were more equal than others: Exploring inequality at Neolithic Çatalhöyük,” *PLOS ONE* 19(9), e0307067, DOI https://doi.org/10.1371/journal.pone.0307067
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0307067
- The article examines inequality within and between buildings at Çatalhöyük and over time; the article identifies a Creative Commons Attribution licence (CC BY 4.0).

**Support boundary:** this is evidence about variation and inequality at one Neolithic settlement, not a universal model of “civilization.” It is useful precisely because it cautions against treating stratification as identical across all early urban communities.

## 4. Claim B — agriculture, settlement and demographic variation

### 4.1 Open Book Project alternative locator

The Open Book Project Chapter 2, section 2.3, “The Development of Agriculture,” provides an explicit multi-region account:
- the shift to agriculture did not occur in one place or at one time;
- it identifies independent developments in the Near East, China, sub-Saharan Africa, Mesoamerica and South America;
- it distinguishes region-specific crops and subsequent diffusion;
- later paragraphs discuss population growth, labour specialization, and differing social/environmental consequences.

Useful direct page:
https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/early-humans.html

Useful section anchors in the page:
- “The Development of Agriculture” — independent regional emergence and regional crop examples;
- “How Farming Changed the Human Experience” — population growth, labour specialization, wealth and social divisions;
- “Neolithic Peoples” — settlement examples and archaeological observations.

The text is a useful alternative locator, but it is a textbook synthesis adapted from the same OpenStax work lineage. It is not independent corroboration of the proposition.

### 4.2 Independent open research

A strong independent open-access companion is:
- “Origins of food crops connect countries worldwide” (2016), *Proceedings of the Royal Society B* 283:20160792, DOI https://doi.org/10.1098/rspb.2016.0792
- https://royalsocietypublishing.org/doi/10.1098/rspb.2016.0792
- PubMed Central record: https://pmc.ncbi.nlm.nih.gov/articles/PMC4920324/
- The article is published under CC BY 4.0. It studies geographical regions of crop diversity and the contribution of crops originating in other regions to national food supplies.

**Support boundary:** this paper supports the importance of geographically distinct crop-origin/diversity regions and later crop exchange/dependence. It does not by itself establish the chronology or independent domestication of every crop, nor does its modern food-supply analysis prove prehistoric settlement or demographic causation. Use it only as a companion for regional diversity and crop geography, not as the sole support for the full Claim B.

### 4.3 Existing Zeder article and Smithsonian profile

- Melinda A. Zeder (2011), “The Origins of Agriculture in the Near East,” *Current Anthropology* 52(S4), S221–S235, DOI https://doi.org/10.1086/659307.
- Publisher page: https://www.journals.uchicago.edu/doi/full/10.1086/659307
- Smithsonian Profiles bibliographic record: https://profiles.si.edu/display/sro_109973

The publisher page labels the article “Free” and exposes its abstract. The abstract describes a pluralistic view of domestication across the Near East, including repeated domestication processes and regional variation. The Smithsonian profile reproduces bibliographic information and an abstract.

**Rights distinction:** “Free” access and an accessible abstract are not a reuse licence. The publisher page inspected here does not establish a CC reuse licence for the article. The Smithsonian profile is a metadata/abstract record, not a licence for the journal article. Do not copy the abstract, article text, tables or figures into the Encyclopedia. A factual paraphrase with a citation may be a different legal question from reproducing protected expression, but this dossier does not provide legal clearance.

**Recommendation:** retain Zeder as a scholarly citation-only candidate if the editor accepts its relevance; keep the Smithsonian profile as a separate bibliographic discovery record. Do not merge either into the Open Book Project source identity.

## 5. Claim C — archaeological and written evidence where preserved

### 5.1 Open Book Project alternative locator

The Open Book Project Chapter 1, section 1.2, “Primary Sources,” discusses:
- documentary and textual sources;
- oral histories of preliterate societies;
- prehistoric cave paintings and archaeological artifacts;
- the difficulty of interpreting evidence without context;
- the uneven survival and destruction of written records.

Direct page:
https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/understanding-the-past.html

The section contains a sentence asserting that written evidence is “more accurate” than oral/artifactual evidence. **Do not import that ranking into the Encyclopedia.** It is a broad methodological generalization and is not required by the existing Claim. The existing Claim only identifies archaeological evidence and written materials where preserved; it does not rank source types.

OpenStax's corresponding §1.2 Primary Sources is also available:
https://openstax.org/books/world-history-volume-1/pages/1-2-primary-sources

### 5.2 Recommended Claim boundary

The current wording is defensible only as a non-exhaustive statement:
- archaeological evidence includes material remains and built environments;
- written records can contribute where they exist and survive;
- neither category is universal, complete or self-interpreting;
- oral histories, images, environmental evidence and other forms may also be material to reconstructing past societies.

The source locator should support the two named categories without implying that they exhaust historical evidence or that written evidence is inherently more reliable. The current Claim need not be expanded to enumerate every evidence class.

## 6. Rights screen — what is established and what is not

| Candidate | Rights information found | Screening result |
|---|---|---|
| Live OpenStax *World History Volume 1, to 1500* (2023 edition) | CC BY-NC-SA 4.0; OpenStax states noncommercial-only reuse, attribution and ShareAlike; its current attribution page also says no LLM/generative-AI ingestion without prior written permission | **Not a safe default** for a project whose future distribution model and AI/data rights policy are unresolved |
| Open Book Project *World History, Volume 1, to 1500* | Its own overview identifies a distinct OpenStax source version at commit `3e17beda91` and states CC BY 4.0 for this adaptation; third-party credited figures/photos retain their own terms | **Best candidate for further rights review**; confirm exact upstream commit, adaptation author/rights chain, attribution and excluded third-party material before any incorporation |
| Cambridge Antiquity Lagash article (2023) | Publisher identifies CC BY 4.0 | **Promising independent article-level source**; attribute authors and DOI; check any separately credited third-party material |
| PLOS ONE Çatalhöyük inequality article (2024) | Publisher identifies CC BY 4.0 | **Promising independent article-level source**; attribute authors and DOI; check article-level figure/data credits |
| Royal Society crop origins article (2016) | Article identifies CC BY 4.0 | **Promising independent article-level source** for crop-region diversity; narrower than full Claim B |
| Zeder (2011), *Current Anthropology* | Publisher page is free to read and abstract is exposed; no CC licence established in this screen | **Citation/access only pending rights review**; no republication permission inferred |
| Smithsonian Profiles record | Bibliographic metadata and abstract are public; no general reuse grant established here | **Discovery/metadata citation only pending terms review**; not a substitute for the article |

### 6.1 Critical distinction: rights to facts, source expression and the database record

The research supports a potential route that avoids reproducing protected textbook prose:
1. use the candidate sources to verify facts and pinpoint passages;
2. have the Encyclopedia author independently written, concise statements in its own language;
3. cite the exact source, edition, section and access date;
4. do not copy expressive passages, figures, maps, tables or datasets;
5. separately review any database extraction, images, translations, third-party material and applicable jurisdictional exceptions.

This is a risk-reduction approach, not a legal opinion. Facts are not the same thing as the author's protected expression, but the applicable legal analysis depends on jurisdiction, use, amount, database rights, licence conditions and distribution model.

### 6.2 OpenStax licensing correction and AI-ingestion caveat

The current OpenStax book page and licensing help pages state CC BY-NC-SA 4.0 and noncommercial restrictions. The current book attribution page additionally says the 2023 edition may not be ingested into LLMs or generative-AI offerings without prior written permission.

The Open Book Project states that its adaptation was made from an earlier OpenStax source version at commit `3e17beda91` published under CC BY 4.0. Do not transfer the current 2023 edition's licence statement to that earlier source version, or transfer the earlier CC BY 4.0 statement to the 2023 edition. The exact source commit and adaptation provenance still need independent confirmation before any rights decision.

## 7. Proposed evidence map — research recommendation only

| Claim | Preferred research locator | Independent corroboration | Limit |
|---|---|---|---|
| A | Open Book Project, *World History*, Ch. 3, §3.1, “Attributes of Early Civilizations”; paragraphs on surplus, specialization, hierarchy/stratification | Cambridge Antiquity (2023) Lagash study; PLOS ONE (2024) Çatalhöyük inequality study | Textbook is adapted from OpenStax; case studies are geographically/temporally specific |
| B | Open Book Project, *World History*, Ch. 2, §2.3, “The Development of Agriculture” | Royal Society (2016) crop-origin/diversity study; Zeder (2011) as citation-only specialist source | Royal Society paper does not prove prehistoric independent domestication or settlement causation by itself; Zeder rights not cleared |
| C | Open Book Project, *World History*, Ch. 1, §1.2, “Primary Sources” | OpenStax §1.2 may be consulted as an additional source, subject to its separate licence | Do not adopt the source's overbroad ranking of written evidence over oral/material evidence; preserve the Claim's non-exhaustive wording |

## 8. Proposed next decision gates for Package A

Before any canonical versioning, the editor/rights owner should resolve:

1. **Source edition choice:** whether the Open Book Project's CC BY 4.0 adaptation is acceptable as the principal textbook source, subject to verification of commit `3e17beda91` and attribution chain.
2. **Independent scholarly companions:** whether the Cambridge Antiquity and PLOS ONE articles are appropriate for bounded, case-specific corroboration of Claim A.
3. **Claim B source mix:** whether the Royal Society article is useful as a regional crop-diversity companion, while Zeder remains citation-only unless article reuse terms are separately established.
4. **Claim C evidence boundary:** whether the editor accepts the primary-source discussion as adequate without ranking written, oral and material evidence.
5. **Project distribution and AI/data use:** owner decisions R-01/R-02/R-04 remain unresolved. No source is deemed compatible with the eventual project licence or AI-ingestion policy by this dossier.

After those decisions, and only after separate explicit authorization for canonical operations, a locator-only implementation package can be prepared for A. The package should create new exact versions rather than overwrite @1, preserve all existing references/history, and leave the slice HOLD.

## 9. Sources consulted

1. Open Book Project, *World History, Volume 1, to 1500*, overview and exact-version licence statement: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/index.html
2. Open Book Project, Chapter 3, *Early Civilizations and Urban Societies*: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/early-civilizations-and-urban-societies.html
3. Open Book Project, Chapter 2, *Early Humans*: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/early-humans.html
4. Open Book Project, Chapter 1, *Understanding the Past*: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/understanding-the-past.html
5. OpenStax, *World History Volume 1, to 1500*, §3.1: https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations
6. OpenStax, *World History Volume 1, to 1500*, §1.2: https://openstax.org/books/world-history-volume-1/pages/1-2-primary-sources
7. OpenStax, *World History Volume 1, to 1500*, Preface/licence and attribution terms: https://openstax.org/books/world-history-volume-1/pages/preface
8. OpenStax licensing information: https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks
9. OpenStax commercial-use terms: https://help.openstax.org/s/article/Commercial-use-under-the-Creative-Commons-License
10. Zeder, M. A. (2011), *Current Anthropology* 52(S4), S221–S235, DOI https://doi.org/10.1086/659307
11. Smithsonian Profiles, Zeder bibliographic record: https://profiles.si.edu/display/sro_109973
12. “Origins of food crops connect countries worldwide” (2016), *Proceedings of the Royal Society B* 283:20160792, DOI https://doi.org/10.1098/rspb.2016.0792
13. “Dense urbanism and economic multi-centrism at third-millennium BC Lagash” (2023), *Antiquity* 97(393), DOI https://doi.org/10.15184/aqy.2023.36
14. Twiss et al. (2024), “But some were more equal than others: Exploring inequality at Neolithic Çatalhöyük,” *PLOS ONE* 19(9), e0307067, DOI https://doi.org/10.1371/journal.pone.0307067

## 10. Final disposition

- Package A research authorization: **executed within scope**.
- Alternative source route identified: **Open Book Project World History adaptation, stated CC BY 4.0 at source version commit `3e17beda91`**, subject to provenance/rights verification.
- Independent open research candidates identified: **Cambridge Antiquity 2023; PLOS ONE 2024; Royal Society 2016**.
- Zeder article: remains **readable/citable candidate, reuse rights not established**.
- Canonical Claims/Evidence Use/Sources: **unchanged**.
- Slice disposition: **HOLD retained**.
- Master register, denominator, allowlist, release manifest and publication: **unchanged**.
- `main`: **unchanged**.
- This dossier is research, not legal clearance, editorial approval or authorization to implement canonical versions.
