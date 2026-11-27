# Package A — revised CC BY-only owner decision and implementation-readiness packet

Date: 2026-11-21
Status: **NONCANONICAL RESEARCH / OWNER DECISION SUPPORT ONLY**
Research base HEAD: `74c6943ebac58e4aea12f8cba8dcd42b8caf9b0b`
PR: #22 — OPEN / DRAFT / UNMERGED

## 1. Purpose and authorization boundary

This document consolidates the Package A research after exact-head CI revalidation and the additional Claim C study. It is decision support only. Existing authorization covers alternative-source and rights research; it does not authorize canonical writes, record versioning, Claim edits, Source/Evidence Use creation, test/coverage/README edits, register or allowlist changes, rights clearance, HOLD removal, publication, merge, deployment, or changes to `main`.

All 11 records in the Ancient Civilizations slice remain HOLD for first-edition selection. Their machine fields `publication_status=published` and `completion_status=complete` are not first-edition approval.

## 2. Technical checkpoint

At exact PR HEAD `74c6943ebac58e4aea12f8cba8dcd42b8caf9b0b`, the following PR workflows completed successfully:

- Reference implementation tests — run 44872243366.
- Offline Edition — run 44872243383.
- MVP Contribution Form Browser Tests — run 44872243370.
- Release Conformance Gate — run 44872243404.

All four reported jobs concluded `success`. Release Gate artifact `release-gate-report` (artifact 14694701476; 1,523 bytes) was uploaded and was not expired at verification.

This is a technical CI PASS only. It is not content approval, legal clearance, an allowlist, or release authorization.

## 3. Exact current slice and dependent accounting

At the inspected HEAD, the slice contains exactly 11 logical records:

- 2 Source;
- 3 Claim;
- 4 Evidence Use;
- 1 Context;
- 1 Scope.

The slice test asserts those exact counts. The current Claim statements are:

- Claim A: “Ранние цивилизации характеризовались, среди прочего, оседлыми поселениями, специализацией труда и социальной стратификацией.”
- Claim B: “В ряде регионов развитие земледелия было связано с изменениями в характере поселений и демографии, но направление и сила этих связей различались по времени и месту.”
- Claim C: “Источники об древних обществах включают археологические свидетельства и письменные материалы там, где они сохранились.”

The existing OpenStax Source @1 and Smithsonian Source @1, and their existing Evidence Use records, must remain intact as historical records unless separately authorized. Do not repurpose the generic OpenStax Source ID as a journal article. Do not silently overwrite or relabel any existing identity.

The coverage manifest at this HEAD reports:

- total_records: 4,751;
- types.source.count: 597;
- types.evidence_use.count: 1,590;
- vertical_slices: 479.

If, and only if, the owner authorizes six new Source records and six new Evidence Use records, the expected metadata-only totals would be:

- total_records: 4,763 (+12);
- Source: 603 (+6);
- Evidence Use: 1,596 (+6);
- vertical_slices remains 479;
- all other type counts remain unchanged.

The slice test would then need to change from 11 to 23 total records, Source 2 to 8, Evidence Use 4 to 10; Claim 3, Context 1 and Scope 1 remain unchanged. The test should also assert exact new Source/Evidence Use links and one-target Claim semantics, not only counts. The slice README currently names OpenStax and Smithsonian; if the new set is selected, its source summary must be revised under the same separate authorization. None of these dependent files has been changed.

## 4. Revised six-source candidate set

The preferred minimal CC BY 4.0 candidate set is now six distinct scholarly works. Publisher/repository records reviewed identify each article as CC BY 4.0. This is an item-level rights screen, not blanket clearance: separately credited third-party images, maps, tables, datasets or other components remain excluded unless independently cleared. The proposed Encyclopedia use is independently authored factual summary, bibliographic attribution and pinpoint citation/link; no copied article expression or third-party media.

### Claim A — early civilization characteristics

**A1. McMahon et al. (2023).** “Dense urbanism and economic multi-centrism at third-millennium BC Lagash.” *Antiquity* 97(393):596–615. DOI: 10.15184/aqy.2023.36.
Publisher: https://www.cambridge.org/core/journals/antiquity/article/dense-urbanism-and-economic-multicentrism-at-thirdmillennium-bc-lagash/2D27165A470831B32B9B29C72EBEF8AD
Rights: article page explicitly states CC BY 4.0.
Pinpoints: Abstract; Introduction; Results/Discussion; Conclusion.
Role: site-specific archaeological evidence for dense urban occupation, distinct walled quarters and multiple foci of intensive industrial production at Lagash in the Early Dynastic period.
Limit: does not establish that all early civilizations shared this pattern or prove every component of Claim A.

**A2. Lamb (2022).** “Rural social differentiation in Early Classic Chunhuayum, Yucatan, Mexico.” *Ancient Mesoamerica* 33(1):162–185. DOI: 10.1017/S0956536121000547.
Publisher: https://www.cambridge.org/core/journals/ancient-mesoamerica/article/rural-social-differentiation-in-early-classic-chunhuayum-yucatan-mexico/72469C57B9FFD3D8B0F99C40D5CEE25F
Rights: article page explicitly states CC BY 4.0.
Pinpoints: Abstract; “Dimensions of Household Social Differentiation”; “Identifying Difference at Chunhuayum”; Discussion; Conclusions.
Role: a Maya rural-community case documenting socioeconomic differentiation across households, including wealth, occupation, labour access and social networks; the conclusion describes distinctions as both hierarchical and heterarchical.
Limit: one rural settlement and one historical setting; it cannot establish a universal or permanent class structure across early civilizations.

**Claim A assessment:** these two works are complementary, not interchangeable. McMahon directly supports urban concentration and production specialization in one Mesopotamian city; Lamb directly supports differentiated household wealth/occupation and hierarchical/heterarchical relations in one Maya community. Together they provide bounded case evidence for the components of Claim A, but do not establish a universal definition. Keep the phrase “among other things” and the plural/historical variation explicit in any editorial explanation. Do not silently revise the Claim. If the owner/editor considers “social stratification” too strong for the evidence or too broad in scope, keep Claim A HOLD and request a separate Claim wording decision rather than stretching the evidence.

### Claim B — agriculture, settlement and demography

**B1. Lesure et al. (2021).** “Large-Scale Patterns in the Agricultural Demographic Transition of Mesoamerica and Southwestern North America.” *American Antiquity* 86(3):593–612. DOI: 10.1017/aaq.2021.23.
Publisher: https://www.cambridge.org/core/journals/american-antiquity/article/largescale-patterns-in-the-agricultural-demographic-transition-of-mesoamerica-and-southwestern-north-america/31DD609E9D81DC72BFC9CB28D72E0F27
Rights: article page explicitly states CC BY 4.0.
Pinpoints: Abstract; “Spatial Structure”; “Temporal Structure”; “The Agricultural Demographic Transition in Two Macroregions”; “A Look at Other Macroregions”; Conclusions.
Role: comparative settlement/subsistence synthesis for Mesoamerica and the North American Southwest; identifies prolonged, multi-phase and spatially variable demographic transitions.
Limit: regional macroregional synthesis, not a universal global sequence; population estimates and archaeological survey resolution constrain inference.

**B2. Crema et al. (2024).** “Regional variations in the demographic response to the arrival of rice farming in prehistoric Japan.” *Antiquity* 98(401):1290–1305. DOI: 10.15184/aqy.2024.146.
Publisher: https://www.cambridge.org/core/journals/antiquity/article/regional-variations-in-the-demographic-response-to-the-arrival-of-rice-farming-in-prehistoric-japan/7E6D28520A04B2F07DDD36908F291808
Rights: article page explicitly states CC BY 4.0.
Pinpoints: Abstract; Introduction; Results; Discussion; Conclusions.
Role: settlement and radiocarbon evidence for geographically different population-growth trajectories after rice farming arrived.
Limit: radiocarbon-date frequency and settlement evidence are proxies, not a census; preserve sampling, calibration and chronology limitations.

**B3. Neil et al. (2016).** “Isotopic evidence for residential mobility of farming communities during the transition to agriculture in Britain.” *Royal Society Open Science* 3(1):150522. DOI: 10.1098/rsos.150522.
Publisher/repository: https://pmc.ncbi.nlm.nih.gov/articles/PMC4736932/
Rights: article record explicitly states CC BY 4.0.
Pinpoints: Abstract; Introduction; Results and Discussion.
Role: strontium and oxygen isotope evidence from an Early Neolithic Gloucestershire burial population consistent with residential mobility among early farming communities; useful evidence against equating farming automatically with immediate permanent sedentism.
Limit: one geographically specific burial population; does not quantify broad population growth or represent all British farmers.

**Claim B assessment:** this is the strongest three-source set. It triangulates macroregional settlement-demographic synthesis, a Japanese regional comparison using radiocarbon/settlement proxies, and a British isotopic mobility case. These are different regions, research designs and underlying datasets; do not collapse them into a single causal model. Neil is used chiefly to bound the settlement/mobility component, not as direct demographic measurement.

### Claim C — archaeological and written evidence

**C1. Clark, Altaweel & Gordin (2022).** “Urbanscape, Land Use Change and Centralization in the Region of Uruk, Southern Mesopotamia from the 2nd to 1st Millennium BCE.” *Land* 11(11):1955. DOI: 10.3390/land11111955.
Publisher: https://www.mdpi.com/2073-445X/11/11/1955
Institutional repository: https://discovery.ucl.ac.uk/id/eprint/10158193/
Rights: publisher page explicitly states CC BY 4.0.
Pinpoints: Abstract; “Textual Description & Sources”; Materials and Methods; Results; Discussion; Conclusions.
Role: direct case-specific example combining place-name gazetteers derived from translated/published cuneiform texts with archaeological survey results from the same Uruk region, for the 2nd and 1st millennia BCE.
Limit: regional case study; text survival and publication are uneven; the gazetteer/survey comparison is a method demonstration, not proof that all ancient societies produced writing.

**Claim C assessment:** preferred over Hawkes et al. (2022) for this slice because Clark's period is explicitly the 2nd–1st millennia BCE and fits the proposed ancient-history boundary more straightforwardly. Hawkes remains a comparator, not selected. Owner/editor still needs to confirm that this period and Uruk case fit the intended scope of “ancient societies”.

## 5. Additional research candidates and exclusions

These are not part of the proposed six-record implementation set unless the owner later authorizes an expanded pass.

- **Fernández-Götz & Smith (2024), “The Archaeology of Early Cities: ‘What Is the City but the People?’”, Annual Review of Anthropology 53:231–247, DOI 10.1146/annurev-anthro-041222-094823.** CC BY 4.0. A strong comparative review of premodern urbanism, city definitions and concentration of people, institutions and activities. Useful as a broader interpretive synthesis, but the abstract alone does not directly substantiate all three components of Claim A. Keep as an optional replacement/complement if the editor wants a review-level source.
- **Twiss et al. (2024), Çatalhöyük inequality study, PLOS ONE 19(9):e0307067, DOI 10.1371/journal.pone.0307067.** CC BY. Valuable limiting evidence: uneven assets and some income inequality, but no evidence for institutionalized or lasting economic/social inequality at that site. Çatalhöyük is a Neolithic settlement, not a straightforward example of an early civilization; do not use it as affirmative support for Claim A. It can remain in the editorial boundary note.
- **Penske et al. (2024), “Kinship practices at the early bronze age site of Leubingen in Central Germany”, Scientific Reports 14:3871, DOI 10.1038/s41598-024-54462-6.** CC BY 4.0. Useful additional case on hierarchical organization and kinship, but the article itself says stratification among the non-elite remains unclear. Not needed in the minimal six-source set.
- **Hawkes et al. (2022), “Grounding texts and theories of societal change”, Antiquity 96(387):611–627, DOI 10.15184/aqy.2022.28.** CC BY 4.0. Retain as a Claim C comparator; its mid-first-millennium AD / Early Historic chronology needs an explicit editorial scope decision.
- **Fochesato et al. (2021), PNAS, “Changing social inequality from first farmers to early states in Southeast Asia”, DOI 10.1073/pnas.2113598118.** Strong substantive relevance to social inequality and early states, but the accessible record identifies a “PNAS license”, not an explicit CC BY 4.0 grant. Do not include it in a CC BY-only set unless the exact article licence is established from the publisher's authoritative record.
- **Basri & Lawrence (2020), “Wealth Inequality in the Ancient Near East”, Cambridge Archaeological Journal 30(4):689–704, DOI 10.1017/S0959774320000177.** Repository record identifies CC BY-NC-ND 4.0, not CC BY. Exclude from the CC BY-only path.

## 6. Rights boundary

OpenStax World History Volume 1, to 1500 is CC BY-NC-SA 4.0 and its official reuse notice separately says the book may not be used for LLM training or otherwise ingested into LLM/generative-AI offerings without prior written permission. Recommendation: do not use OpenStax as affirmative new Evidence Use for Package A absent written permission and separate assessment of NonCommercial/ShareAlike compatibility. Preserve its existing Source/Evidence Use history; do not delete, overwrite, or silently relabel it.

For the six proposed articles, article-level CC BY 4.0 supports reuse/adaptation with proper attribution and indication of changes. It does not automatically clear third-party items excluded from the article licence. The implementation should use independently authored factual descriptions, exact section locators, DOI/publisher links and required attribution only. No article PDF, copied passage, figure, map, photograph, table or third-party dataset should be incorporated in the first implementation.

This is a conservative rights screen, not legal advice or final rights clearance. The project's own publication licence, distribution model, attribution presentation and rights register still require owner adoption under Work Package 2.

## 7. Proposed implementation boundary if approved

The most conservative, technically coherent first implementation would:

1. Create six new, distinct Source identities for the six selected scholarly works.
2. Create six new Evidence Use records, one per Claim–Source relationship, each with exact Claim @1, exact new Source @1, `supports` role only where the described material genuinely supports the target, and a pinpoint `material.locator` plus independently authored `material.description`.
3. Keep all three Claims @1 unchanged.
4. Preserve the existing OpenStax and Smithsonian Source @1 and all existing Evidence Use @1 records as historical records; do not repurpose their IDs.
5. Leave Context, Scope, Relations, candidate registers, denominators, all HOLD dispositions, allowlists and release manifests unchanged.
6. Separately authorize the dependent README, slice-test and coverage count updates described in §3. Do not change the corpus version label unless the project's versioning rule requires it and the owner explicitly includes that operation.
7. Re-fetch all 23 slice records at the resulting immutable HEAD; validate schema, exact references, Evidence Use semantics, unique IDs, source identity, rights attribution register and slice tests.
8. Run applicable PR workflows on the resulting exact HEAD and report each result separately.
9. Keep every affected record HOLD for first-edition selection until independent editorial and rights decisions are complete.

Proposed ID stems (NOT RESERVED; require final collision check and explicit authorization):

| Claim | Proposed Source ID | Proposed Evidence Use ID |
|---|---|---|
| A | `SRC-MCMAHON-LAGASH-URBANISM` | `EU-ANCIENT_CIVILIZATIONS_BASICS-A-MCMAHON` |
| A | `SRC-LAMB-CHUNHUAYUM-SOCIAL-DIFFERENTIATION` | `EU-ANCIENT_CIVILIZATIONS_BASICS-A-LAMB` |
| B | `SRC-LESURE-AGRICULTURAL-DEMOGRAPHIC-TRANSITION` | `EU-ANCIENT_CIVILIZATIONS_BASICS-B-LESURE` |
| B | `SRC-CREMA-RICE-FARMING-JAPAN-DEMOGRAPHY` | `EU-ANCIENT_CIVILIZATIONS_BASICS-B-CREMA` |
| B | `SRC-NEIL-BRITAIN-NEOLITHIC-MOBILITY` | `EU-ANCIENT_CIVILIZATIONS_BASICS-B-NEIL` |
| C | `SRC-CLARK-URUK-TEXTS-ARCHAEOLOGY` | `EU-ANCIENT_CIVILIZATIONS_BASICS-C-CLARK` |

These identifiers are suggestions only and have not been created or reserved.

## 8. Six owner decisions requested

Please answer these decisions explicitly. “Defer” is allowed and leaves the relevant item HOLD.

1. **OpenStax treatment.** Recommended: no new affirmative Evidence Use based on OpenStax without written permission; preserve all existing @1 records historically. The prior Source identity continuity question is deferred because this route creates distinct Source identities and does not version the OpenStax Source.
2. **Claim A evidence and scope.** Recommended: select McMahon 2023 + Lamb 2022 as bounded case studies. Confirm that they may be used only for their stated local findings, not as universal proof. If “social stratification” is judged too strong or broad, defer Claim A and request separate Claim wording review.
3. **Claim B evidence.** Recommended: select all three — Lesure 2021, Crema 2024 and Neil 2016 — preserving their different roles and proxy limitations.
4. **Claim C period and source.** Recommended: select Clark et al. 2022 as the preferred case-specific source for Claim C; retain Hawkes as an alternative only. Confirm that 2nd–1st millennium BCE Uruk falls within the editorial scope of “ancient societies”.
5. **Implementation scope.** Recommended: authorize in principle only six new Source + six new Evidence Use records, plus exact dependent README/test/coverage updates, with Claims/Context/Scope/Relations/register/denominator/allowlist/HOLD/main untouched. Actual write authorization must be issued separately with exact paths, proposed IDs, permitted fields and expected count deltas.
6. **Rights and distribution.** Recommended: accept CC BY 4.0 text-only factual-summary/link use for these six works as the candidate rights route, subject to attribution and third-party exclusions; do not infer project licence adoption. Separately decide the Encyclopedia's own publication licence, whether commercial reuse is intended, and who maintains the item-level rights/attribution register.

## 9. Explicit non-actions

No canonical JSON, Claim, Source, Evidence Use, Context, Scope, Relation, README, test, coverage file, register, denominator, allowlist, release manifest, policy, rights decision, or main-branch file was changed by this research packet. No identifier is reserved. No rights clearance, first-edition INCLUDE, HOLD removal, publication, merge or deployment is inferred.

**Next gate:** owner/editor decisions 1–6. Only after those decisions should a separate exact bounded authorization be prepared.