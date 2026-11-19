# First Edition — Part II Batch 2: History, Culture and Humanities Screening

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `c4fbc8d1d879ae0c14e2b0ceaba8899d4f6fef0d`  
Current-head integrity check: all 47 record-file blob SHAs are unchanged at `5a746e7be8c8a72aaa911b6e958689768be7a916`.  
Status: **5/5 SLICES SCREENED; 47/47 CANONICAL JSON RECORDS FETCHED AND PARSED; ALL 5 HOLD**

## 1. Scope and duplicate-control

This is the final five-slice remainder from the controlling Part II structural map after:
- reusing 18 prior-screened slices / 170 records;
- completing two new bounded screens in Batch 1 (matter-basics and earth-system-basics);
- retaining the seven Part I overlaps without repeating their audits.

The five slices below had no matching exact-slice prior audit or candidate-register entry in the inspected release records. Adjacent slices such as `cultural-anthropology-basics`, `culture-and-language` or `comparative-civilizations-basics` were not treated as identical to these canonical slice IDs.

## 2. Inventory and version profile

| Slice | JSON records | Current versions | Screening result |
|---|---:|---|---|
| ancient-civilizations-basics | 11 | all v1 | HOLD |
| anthropology-basics | 9 | all v1 | HOLD |
| linguistics-basics | 9 | all v1 | HOLD |
| philosophy-basics | 9 | all v1 | HOLD |
| ethics-basics | 9 | all v1 | HOLD |
| **Total** | **47** | **all 47 records v1** | **5 HOLD** |

The inventory contains 15 Claims, 16 Evidence Use records, 6 Sources, 5 Contexts and 5 Scopes. Ancient civilizations includes one additional Smithsonian corroboration Evidence Use and Source.

## 3. Slice-by-slice findings

| Slice | Records | Decision | Finding and blocker |
|---|---:|---|---|
| `ancient-civilizations-basics` | 11 | **HOLD** | Claims A/B are substantive. OpenStax World History §3.1 directly supports settled populations, agricultural surplus, specialization and stratification. EU-A/B/C remain generic with no passage locators. The Smithsonian corroboration supports regional variation in agricultural origins, but the Source points to a bibliographic profile rather than the DOI article and EU-SMITHSONIAN has no exact locator. Claim C needs direct evidence distinguishing archaeological and written records across contexts. |
| `anthropology-basics` | 9 | **HOLD** | All three Claims describe the purpose, evidence boundary and limitations of the slice; none states a substantive anthropological proposition. The AAA overview is a broad source and all EUs are generic. Replace the three metadata Claims with falsifiable subject-matter propositions and rebuild evidence links. |
| `linguistics-basics` | 9 | **HOLD** | All three Claims are editorial metadata, not linguistics propositions. Britannica is a broad overview and all EUs are generic. The current source has no open reuse licence identified; retain a link only unless permission is obtained. |
| `philosophy-basics` | 9 | **HOLD** | All three Claims are editorial metadata, not philosophical propositions. The current SEP Source URL `/entries/philosophy/` returns 404. SEP content is copyright-protected and has limited non-commercial distribution rights; replace the source with a valid entry and use links rather than reproducing text absent permission. |
| `ethics-basics` | 9 | **HOLD** | All three Claims are editorial metadata, not ethics propositions. The SEP morality-definition page is live and relevant to one possible subject, but the current EUs contain no locators and do not support the generic Claims. SEP reuse/distribution is limited; link-only unless author permission is secured. |

## 4. Subject-matter findings

### Ancient civilizations

OpenStax World History Volume 1, §3.1 directly supports the core attributes in Claim A: settled populations, agricultural surplus, task specialization, social hierarchy and stratification. It also discusses agricultural settlement and demographic change. The current EUs A/B/C, however, contain only generic statements and no exact passage locators.

The Smithsonian Profiles page identifies Melinda Zeder's 2011 article, “The Origins of Agriculture in the Near East,” and provides an abstract describing multiple regional trajectories and variation. It is useful independent support for Claim B, but the canonical Source points to the profile record rather than the article DOI. The Source/EU chain should identify the article via DOI `10.1086/659307` and give a pinpoint; do not treat the profile metadata page as the full article. Claim C needs a direct locator for the use of archaeological evidence and written records, with an explicit boundary for prehistoric societies that left no writing.

### Anthropology, linguistics, philosophy and ethics

All four slices share the same structural defect: the three Claims describe what the slice is for, how evidence should be interpreted, or when specialist review is needed. These are editorial/epistemic boundary statements, not subject-matter Claims for the named discipline. A broad reference page cannot make those Claims into anthropology, linguistics, philosophy or ethics facts.

Replace the metadata Claims with discipline-specific, falsifiable propositions. Then rebuild each Evidence Use with a direct source section, inspected passage and scope boundary. For philosophy, the current source URL is broken (404) and must be replaced before any further evaluation. For ethics, the SEP morality-definition page is live, but it is not evidence for the three current generic Claims.

## 5. Rights and reuse screen — preliminary, not legal clearance

| Source | Public terms located | Release implication |
|---|---|---|
| OpenStax World History Volume 1 | CC BY-NC-SA 4.0; attribution and ShareAlike apply to reused/adapted expression; no LLM training or ingestion into LLM/generative-AI offerings without prior written permission. | Do not ingest the textbook into an AI/training pipeline or reproduce/adapt its expression without permission. Determine whether the project uses only independently written factual propositions and citations, or adapted OpenStax expression. |
| Smithsonian Profiles VIVO record | Smithsonian Profiles states that copyrightable VIVO profile data is distributed under CC BY 3.0; non-copyrightable data under CC0. Linked source documents and images may have separate rights. | Attribute the profile metadata. The linked Current Anthropology article is a separate copyrighted publication; do not reproduce its text without rights review. |
| American Anthropological Association page | No open licence was identified for the specific “What is Anthropology?” page; AAA's publications/media permissions process is separate. | Link and cite only; do not copy page text or treat the page as openly licensed. |
| Encyclopaedia Britannica | No open licence was identified for the linguistics entry. Britannica content is copyright-protected; its published terms restrict use to personal/non-commercial use and prohibit automated extraction absent permission. | Link-only for this project unless explicit reuse permission is obtained. |
| Stanford Encyclopedia of Philosophy | SEP entries have limited user rights; distribution is restricted to non-commercial cases, and fixed-media distribution requires author permission. Non-entry pages have separate reproduction restrictions. | Use direct links and citations only. Do not copy/redistribute SEP entries in the encyclopedia without the required author permission and project-level rights approval. |

Official rights and source references:
- OpenStax World History §3.1: https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations
- OpenStax World History preface/licence: https://openstax.org/books/world-history-volume-1/pages/preface
- OpenStax licensing: https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks
- Smithsonian Profiles — The Origins of Agriculture in the Near East: https://profiles.si.edu/display/sro_109973
- Smithsonian Profiles terms: https://profiles.si.edu/termsOfUse
- AAA overview: https://americananthro.org/learn-teach/what-is-anthropology/
- AAA reprints and permissions: https://americananthro.org/publications/reprints-permissions/
- Britannica linguistics entry: https://www.britannica.com/science/linguistics
- Stanford Encyclopedia of Philosophy — editorial information and terms: https://plato.stanford.edu/info.html
- Stanford Encyclopedia of Philosophy — The Definition of Morality: https://plato.stanford.edu/entries/morality-definition/

Rights status is not cleared. The project-level licence, commercial/non-commercial distribution model, and AI ingestion policy remain project-owner decisions.

## 6. Record-graph checks

- All 47 canonical JSON files were valid JSON; their IDs, versions and record types were read.
- The main Claim → Evidence Use → Source references resolve at the declared versions.
- All Context and Scope records target Claim A only. Confirm that this is the intended slice-level model before release.
- No canonical record, Relation, allowlist, release manifest or `main` branch was changed.

## 7. Required remediation

1. Replace the three metadata Claims in anthropology, linguistics, philosophy and ethics with substantive domain Claims.
2. Replace the broken philosophy Source URL and add exact SEP or alternative-source locators.
3. Add direct section/passages to every Evidence Use; no generic “source used within scope” statements.
4. For ancient civilizations, correct the Smithsonian Source identity to the DOI article, add claim-specific locators, and support Claim C directly.
5. Complete source-specific rights/attribution decisions under the approved project licence and distribution model.
6. Preserve all five HOLD decisions until versioned corrections, independent review and Human View are complete.

No automatic promotion is permitted. The five slices are now screened and added to the HOLD queue; the 261 map-external unregistered slices remain outside the approved bounded scope.
