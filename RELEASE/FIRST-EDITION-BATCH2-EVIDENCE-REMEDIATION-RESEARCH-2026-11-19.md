# First Edition — Batch 2 Evidence Remediation Research

Date: 2026-11-19  
PR: #22 — `mvp-public-contribution-design-2026-10-11`  
Research baseline: PR HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`  
Batch 2 screening baseline: `c4fbc8d1d879ae0c14e2b0ceaba8899d4f6fef0d`  
Status: **RESEARCH-ONLY REMEDIATION DOSSIER — ALL FIVE SLICES REMAIN HOLD; NO CANONICAL CHANGE AUTHORIZED**

## 1. Purpose and change-control

This dossier turns the five completed Batch 2 HOLD findings into a source-and-locator remediation plan. It does not repeat the subject screening and does not change any canonical record.

Controls:
- All five slices remain HOLD.
- No Claim, Evidence Use, Source, Context or Scope record is modified or versioned by this dossier.
- No publication/completion status, INCLUDE/HOLD/EXCLUDE decision, allowlist, Relation or release manifest is changed.
- The current `RELEASE/EDITORIAL-CORRECTION.json` does not authorize edits to these five slices. The source and Claim proposals below are therefore drafts for owner/editorial review, not instructions to write canonical JSON.
- Rights notes are source-specific screening observations, not legal clearance. The project content licence, commercial/non-commercial distribution model, rights holder and editor remain unresolved owner decisions.

## 2. Current-head integrity and register reconciliation

The five Batch 2 slices contain 47 canonical JSON files:
- ancient-civilizations-basics: 11
- anthropology-basics: 9
- linguistics-basics: 9
- philosophy-basics: 9
- ethics-basics: 9

The SHA-1 blob identities for all 47 files were compared between the Batch 2 inspection commit `c4fbc8d1d879ae0c14e2b0ceaba8899d4f6fef0d` and current PR HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`: **47/47 unchanged**. The intervening test corrections did not alter Batch 2 canonical content.

The exact-version master already contains the 47 Batch 2 rows. Independent parsing of its exact-version table yields:
- 1,119 unique exact `record_id@version` rows (1,058 candidate keys + 61 dependency records);
- 124/385 Part II slices represented after Batch 2;
- 261 Part II slices remain unregistered.

The 261 are not an instruction to audit the entire corpus. The controlling domain map examples are explicitly non-exhaustive; unlisted slices remain outside the bounded screen unless the owner approves an expanded scope. The five Batch 2 slices are not a new screening queue: they are screened and HOLD.

## 3. Ancient civilizations — retain substantive Claims; close exact Evidence Use

### Existing Claims and proposed locators

| Claim | Existing proposition (short description) | Evidence candidate and locator | Required treatment |
|---|---|---|---|
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1` | Early civilizations included settled settlements, labor specialization and social stratification | OpenStax, *World History Volume 1*, §3.1 “Early Civilizations”; locator: paragraph describing urban settings, specialization of labor and increasing social stratification | Claim wording appears supportable; add a direct §3.1 pinpoint to its EU. Rights are CC BY-NC-SA 4.0; project distribution model must be checked. |
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1` | In some regions, agriculture related to settlement and demographic changes, with variation by time/place | OpenStax, *World History Volume 1*, §2.3 “The Neolithic Revolution” (independent regional emergence; population growth and labor specialization); Melinda A. Zeder, “The Origins of Agriculture in the Near East,” *Current Anthropology* 52(S4), 2011, DOI 10.1086/659307, Abstract (multi-regional and repeated domestication; regional variation) | Existing Smithsonian Source is a bibliographic profile, not the article itself. A DOI/publisher Source identity is the better article-level locator. The publisher page currently exposes the article and abstract. Keep the Claim bounded to regional variation; do not infer one universal pathway. |
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-C@1` | Evidence about ancient societies includes archaeological evidence and written materials where preserved | OpenStax, *World History Volume 1*, §1.2 “Primary Sources”; locator: opening explanation of source types, primary/secondary sources, hieroglyphs, art, artifacts and the limits of written records; also “Documentary Sources: Competing Narratives” | Claim is supportable as a qualified statement. The locator should preserve the qualification “where they survive”; do not imply that written records exist for every society or that material/oral evidence is inferior in all contexts. |

### Source identity and rights

- Existing Source `SRC-ANCIENT_CIVILIZATIONS_BASICS@1` points to OpenStax §3.1. The source is relevant to Claim A, but the three EUs need their own claim-specific locators.
- Existing `SRC-SMITHSONIAN-ANCIENT-AGRICULTURE@1` points to Smithsonian Profiles record `sro_109973`. That profile identifies Zeder's article and provides its abstract; the publisher's article URL is `https://www.journals.uchicago.edu/doi/full/10.1086/659307`. If a canonical Source correction is later authorized, distinguish the publisher's article from the Smithsonian bibliographic profile; do not conflate them.
- OpenStax *World History Volume 1* is marked CC BY-NC-SA 4.0. This is not project-wide rights clearance and may be incompatible with a commercial distribution model. Do not copy textbook expression, tables or figures on the assumption that a citation alone grants reuse rights.
- Zeder's article is openly readable at the publisher page, but public access does not establish a general republication licence. Use a concise factual paraphrase and citation only after item-level rights review; do not copy the article text or figures.

## 4. Anthropology — replace editorial metadata Claims with subject-matter Claims

The three existing Claims are about the purpose of the slice, evidence interpretation and the need for specialist review. They are not anthropology propositions. A broad AAA overview cannot make those statements into domain knowledge.

### Draft Claim concepts for editorial review (not canonical wording)

| Record | Proposed subject proposition | Direct source locator |
|---|---|---|
| `CLM-ANTHROPOLOGY_BASICS-A@1` | Introductory anthropology commonly uses four complementary fields: biological anthropology, archaeology, cultural anthropology and linguistic anthropology. | OpenStax, *Introduction to Anthropology*, §1.2 “The Four-Field Approach”; cross-check §1 Summary. |
| `CLM-ANTHROPOLOGY_BASICS-B@1` | Anthropological holism examines how biological, social and cultural aspects of human life are interconnected rather than treating them as isolated domains. | OpenStax, *Introduction to Anthropology*, §1.5 “Holism, Anthropology’s Distinctive Approach”. |
| `CLM-ANTHROPOLOGY_BASICS-C@1` | Participant observation is a field method in which a researcher participates in activities in a host culture and records observations; interviews and recordings require informed permission and ethical safeguards. | OpenStax, *Introduction to Anthropology*, §2.4 “Participant Observation and Interviewing”; locator: “Participant Observation” and “Ethical Considerations”. The claim should be split if the schema requires one proposition per Claim. |

### Source and rights

Preferred subject-matter source candidate: OpenStax, *Introduction to Anthropology* (Hasty, Lewis and Snipes), especially §§1.2, 1.5, 2.3 and 2.4. These sections provide direct locators for the four-field approach, holism, ethnography and participant observation.

**Licence correction:** the live OpenStax section page currently identifies the book as CC BY-NC-SA 4.0, not CC BY 4.0, and states that use in LLM/generative-AI offerings requires prior written permission. A separate Universal Open Textbook Initiative adaptation page describes its OpenStax-derived text as CC BY 4.0. Those are distinct source/edition statements and must not be collapsed. Before any Source versioning, the editor/rights reviewer must pin the exact edition actually consulted, inspect its own licence and resolve the adaptation lineage. Until then, treat OpenStax as a locator/research candidate, not as cleared reusable content; do not assume commercial reuse is permitted.

The source's research-ethics discussion is important: participant consent, cultural protocols, data ownership, informant rights and institutional review are not optional decoration. If this material is used, the Claim and Context must avoid treating Indigenous/community knowledge as freely extractable or assuming researcher ownership.

Rights screening remains item-level. Confirm the exact edition and licence page at the time of any authorized Source versioning; do not copy chapter text or third-party figures.

## 5. Linguistics — replace editorial metadata Claims with testable language facts

The three existing Claims describe the slice, source interpretation and specialist review. They are editorial metadata rather than propositions about linguistics.

### Draft Claim concepts for editorial review (not canonical wording)

| Record | Proposed subject proposition | Direct source locator |
|---|---|---|
| `CLM-LINGUISTICS_BASICS-A@1` | Linguistics is the systematic, empirical study of human language and language behaviour. | Catherine Anderson, *Essentials of Linguistics*, §1.1 “Linguistics is Science”. |
| `CLM-LINGUISTICS_BASICS-B@1` | All human languages have systematic grammatical structures; the absence of a writing system or prescriptive grammar does not mean a language lacks grammar. | Anderson, *Essentials of Linguistics*, §1.4 “Fundamental Properties of Language”. |
| `CLM-LINGUISTICS_BASICS-C@1` | Linguistic analysis distinguishes interacting levels including phonetics, phonology, morphology, syntax and semantics. | Anderson, *Essentials of Linguistics*, §1.4 and the book's chapter sequence (Chapters 2–6). A more precise locator should identify each relevant chapter if the Claim enumerates all five levels. |

### Source and rights

Preferred source candidate: Catherine Anderson, *Essentials of Linguistics*, McMaster University / eCampusOntario open textbook. The source record should identify the author, title, edition and stable publication location rather than the current Britannica overview. The book is licensed CC BY-SA 4.0 according to the publisher/repository description. Attribution is required; ShareAlike applies to adaptations. This is a source candidate, not a conclusion that the project has adopted a compatible content licence.

The book's focus includes Canadian English examples and Indigenous languages in Canada. Avoid universalizing examples from one language community. Keep claims at the level supported by the cited section and distinguish descriptive linguistics from prescriptive judgments.

## 6. Philosophy — replace the broken SEP URL and metadata Claims

All three existing Claims are generic editorial statements. In addition, the existing Source URL `https://plato.stanford.edu/entries/philosophy/` is invalid (404 in the prior Batch 2 screen).

### Draft Claim concepts for editorial review (not canonical wording)

| Record | Proposed subject proposition | Direct source locator |
|---|---|---|
| `CLM-PHILOSOPHY_BASICS-A@1` | Philosophy is a broad inquiry into fundamental questions about the world, knowledge, morality and human life, using reasoned examination of assumptions. | *Introduction to Philosophy* (Open Book Project adaptation of OpenStax), §1.1 “What Is Philosophy?”. |
| `CLM-PHILOSOPHY_BASICS-B@1` | Philosophical inquiry draws on multiple kinds of evidence, including historical thought, common-sense observation and findings from other disciplines. | Same text, §1.2 “How Do Philosophers Arrive at Truth?”; locator: “Sources of Evidence”. |
| `CLM-PHILOSOPHY_BASICS-C@1` | A philosophical argument uses premises as reasons supporting a conclusion; logical analysis tests support and consistency but does not by itself prove that a coherent set of claims is true. | Same text, §1.2; locators: “Argument”, “Coherence” and the distinction between consistency and truth. |

### Source and rights

Preferred source candidate: *Introduction to Philosophy*, Open Book Project adaptation of OpenStax. Its preface identifies the source version as licensed CC BY 4.0 at OpenStax repository commit `d7bd4f0f52`; it explicitly warns that later versions of the OpenStax book carry a different licence. The adaptation also notes that credited images and illustrations may have separate terms. If selected, pin the exact adaptation/version and retain the attribution/derivation statement; do not assume every figure is CC BY 4.0.

The current Stanford Encyclopedia Source should not be silently redirected to a different SEP page. The Open Book Project is a distinct source identity and would require a properly versioned Source record under explicit authorization.

## 7. Ethics — use a general ethics source, not only the bioethics declaration

The current three Claims are editorial metadata, not ethics propositions. The existing SEP morality-definition source is not a sufficient locator for all three.

### Draft Claim concepts for editorial review (not canonical wording)

| Record | Proposed subject proposition | Direct source locator |
|---|---|---|
| `CLM-ETHICS_BASICS-A@1` | Ethics is the philosophical study of morality and is commonly distinguished into metaethics, normative ethics and applied ethics. | *Introduction to Philosophy* (Open Book Project adaptation of OpenStax), §9.1 “Requirements of a Normative Moral Theory”; locator: “Three Areas of Ethics”. |
| `CLM-ETHICS_BASICS-B@1` | Major normative approaches assess conduct by consequences, duties/rules or virtues/character, respectively. | Same text, §9.1; locators: “Three Coherent Frameworks for Understanding Morality”; §§9.2–9.4 for separate treatment. |
| `CLM-ETHICS_BASICS-C@1` | Applied ethics examines how moral concepts and frameworks bear on practical issues, including bioethics, environmental ethics and business/technology. | Same text, Chapter 10 “Applied Ethics”; locators §§10.1–10.3. |

### Optional official primary-source companion

UNESCO's *Universal Declaration on Bioethics and Human Rights* (adopted 19 October 2005) can support a separate, explicitly scoped bioethics proposition, not a general definition of all ethics. Potential locators include Articles 3–5 (dignity, benefit/harm, autonomy), 8–12 (vulnerability, privacy, equality, non-discrimination and cultural diversity), and 18–20 (decision-making, ethics committees and risk assessment). Do not use this declaration to imply that every ethical theory or jurisdiction is exhausted by the instrument.

### Source and rights

Use the same pinned Open Book Project / OpenStax-derived philosophy text as a candidate for the general ethics framework, subject to the edition/licence conditions in §6. UNESCO is an official normative text; any republication, translation or derivative use still needs the project rights reviewer to record the applicable UNESCO publication terms and exact edition. A treaty/declaration is a primary normative document, not empirical proof that its principles are universally implemented.

## 8. Consolidated proposed remediation sequence

| Order | Slice | Canonical work that would be needed after authorization | Main closure condition |
|---:|---|---|---|
| 1 | ancient-civilizations-basics | Correct Smithsonian Source identity to the publisher article if approved; add claim-specific locators to EUs A/B/C and the independent Smithsonian EU; review Context/Scope targeting | Direct source identity, exact locators, rights/attribution, preserve regional variation and evidence limits |
| 2 | anthropology-basics | Replace Claims A–C with discipline propositions; version Source and EUs; update Context/Scope only if the domain boundary changes | Four-field coverage, holism, field-method accuracy, Indigenous/community research ethics |
| 3 | linguistics-basics | Replace Claims A–C; replace Britannica Source with a version-pinned OER Source; rebuild EUs; adjust Context/Scope only if needed | Stable edition/locators, descriptive scope, CC BY-SA rights compatibility |
| 4 | philosophy-basics | Replace broken SEP Source with a distinct valid source; replace Claims A–C and rebuild EUs | Source identity/edition pinning, philosophical pluralism, attribution and image-rights separation |
| 5 | ethics-basics | Replace Claims A–C; use the general philosophy/ethics source and, only for a bioethics-specific Claim, UNESCO as a companion Source; rebuild EUs | Distinguish metaethics/normative/applied ethics; avoid presenting one declaration as universal ethical consensus |

For all five slices:
1. Keep current `@1` records as history; any correction must create the next exact version and update every dependent reference.
2. Ensure one Evidence Use supports one Claim with a direct locator and explicit support boundary.
3. Re-check Source identity, author/publisher, edition, stable URI, licence and third-party content.
4. Re-check Context and Scope targets against their intended claims; do not assume Claim A automatically frames the entire slice.
5. Preserve HOLD until independent editorial/Human View and rights review; no automated promotion.

## 9. Research references

- OpenStax, *World History Volume 1*, §3.1 “Early Civilizations”: https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations
- OpenStax, *World History Volume 1*, §2.3 “The Neolithic Revolution”: https://openstax.org/books/world-history-volume-1/pages/2-3-the-neolithic-revolution
- OpenStax, *World History Volume 1*, §1.2 “Primary Sources”: https://openstax.org/books/world-history-volume-1/pages/1-2-primary-sources
- Zeder, M. A. (2011), “The Origins of Agriculture in the Near East,” *Current Anthropology* 52(S4), S221–S235, DOI: https://doi.org/10.1086/659307; publisher full text: https://www.journals.uchicago.edu/doi/full/10.1086/659307
- Smithsonian Profiles bibliographic record: https://profiles.si.edu/display/sro_109973
- OpenStax, *Introduction to Anthropology*, §1.2: https://openstax.org/books/introduction-anthropology/pages/1-2-the-four-field-approach-four-approaches-within-the-guiding-narrative
- Universal Open Textbook Initiative, OpenStax-derived *Introduction to Anthropology* adaptation and its separately stated CC BY 4.0 terms: https://read.uotinitiative.org/read/en-introduction-to-anthropology-3o9x2
- OpenStax, *Introduction to Anthropology*, §1.5: https://openstax.org/books/introduction-anthropology/pages/1-5-holism-anthropology-s-distinctive-approach
- OpenStax, *Introduction to Anthropology*, §2.3: https://openstax.org/books/introduction-anthropology/pages/2-3-ethnography-and-ethnology
- OpenStax, *Introduction to Anthropology*, §2.4: https://openstax.org/books/introduction-anthropology/pages/2-4-participant-observation-and-interviewing
- Anderson, C., *Essentials of Linguistics*, §1.1: https://open.maricopa.edu/essentialsoflinguistics/chapter/1-1-linguistics-is-science/
- Anderson, C., *Essentials of Linguistics*, §1.4: https://open.maricopa.edu/essentialsoflinguistics/chapter/1-5-fundamental-properties-of-language/
- Open Book Project, *Introduction to Philosophy*, preface and source-version/licence statement: https://open-book-project.github.io/textbooks/social-science-textbooks/introduction_philosophy/
- Open Book Project, *Introduction to Philosophy*, §1.1–1.2: https://open-book-project.github.io/textbooks/social-science-textbooks/introduction_philosophy/introduction-to-philosophy.html
- Open Book Project, *Introduction to Philosophy*, Chapter 9: https://open-book-project.github.io/textbooks/social-science-textbooks/introduction_philosophy/normative-moral-theory.html
- UNESCO, *Universal Declaration on Bioethics and Human Rights*: https://www.unesco.org/en/legal-affairs/universal-declaration-bioethics-and-human-rights

## 10. Decision

- Batch 2 screening remains closed: 5/5 slices, 47/47 canonical records, all HOLD.
- Current-head canonical integrity: 47/47 record blobs unchanged since Batch 2 inspection.
- The 47 rows are already present in the 1,119-row exact-version master; Part II coverage is 124/385 slices, with 261 not yet registered.
- This dossier supplies a bounded, source-located remediation route for all five HOLD slices, but does not grant authorization to execute canonical changes.
- No record is promoted to INCLUDE or EXCLUDE. No canonical content, release allowlist, preview, or publication state is changed.
