# Package A — proposed Evidence Use and Source implementation packet

Date: 2026-11-21  
Status: **NONCANONICAL PROPOSAL ONLY — research authorization does not authorize implementation**  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Research base HEAD: `914a6f7feb6b71354093aa77397fdf7ff9f02e5d`

## 1. Decision boundary

This packet translates the Package A research into a proposed, reviewable implementation. It is not a canonical record, does not create any record version, and does not change the master register, candidate denominator, coverage manifest, allowlist, release manifest, publication state, `main`, or PR merge state.

The only authorization currently received covers research into alternative sources and rights for Package A. It does **not** authorize canonical Source/Evidence Use @2 records. All 11 records in the Ancient Civilizations slice remain HOLD. Existing record metadata `publication_status=published` and `completion_status=complete` is not first-edition approval.

## 2. Exact schema findings at research HEAD

Inspected at the pinned HEAD:

- `STANDARD/003-SOURCE.md`
- `STANDARD/004-EVIDENCE-USE.md`
- `STANDARD/001-RECORD.md`
- `IMPLEMENTATION/005-RECORD-SCHEMA.json`
- all three Claim records, four existing Evidence Use records, and two existing Source records in `CONTENT/vertical-slices/ancient-civilizations-basics/records/`.

Relevant machine constraints:

1. An Evidence Use record requires exactly one `claim_ref`, one `source_ref`, a semantically defined `material` and one of `supports` / `contradicts`.
2. `material` supports `locator`, `fragment`, `quote`, and/or `description`; no unregistered `url`, `rights`, `notes`, `author`, or free-form metadata keys belong inside that object.
3. A Source `external_ref` supports `uri` and optional `locator`. Rights and attribution notes are not fields in the current Source profile. They belong in the separate rights/attribution register or a noncanonical research document until a schema/policy explicitly provides otherwise.
4. Evidence Use must point to one exact Claim version and one exact Source version. A section locator should be explicit enough for another reviewer to retrieve the exact material.
5. Distinct scholarly works are distinct Source identities even where they discuss the same topic. Multiple publications derived from a common dataset, review, or source lineage must not be counted as independent without a dependency analysis.

## 3. Material correction to the previous locator plan

Use the live OpenStax 2023 *World History, Volume 1, to 1500* edition for the three existing textbook Evidence Use chains, not the Open Book Project adaptation as the default.

The Open Book Project adaptation publicly claims CC BY 4.0 and identifies upstream OpenStax commit `3e17beda9130380d24be881e6d1942dfcc1be845`, but its source files are private and its adaptation authorship/authority and full third-party component rights remain independently unverified. It is therefore **not** the preferred basis for a canonical Source identity at this stage. It remains a locator/reference lead only.

The live OpenStax edition is clearly addressable by the three section URLs below. Its book-level licence is CC BY-NC-SA 4.0; this is not a blanket permission for the Encyclopedia to reproduce or adapt its expressive material, and the NonCommercial / ShareAlike conditions must be assessed against the eventual distribution model. Use factual, independently written summaries and citations/links only pending project-owner rights decisions. Do not ingest, copy, translate or reproduce the textbook's expressive content, figures, tables, maps or images under this packet.

## 4. Proposed exact Evidence Use @2 values

These are proposed payloads for a later, separately authorized implementation. They are not committed canonical JSON.

### EU A — early civilization characteristics

Target: `EU-ANCIENT_CIVILIZATIONS_BASICS-A@2`  
Claim: `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1`  
Source: proposed `SRC-ANCIENT_CIVILIZATIONS_BASICS@2`

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-ANCIENT_CIVILIZATIONS_BASICS-A",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {"record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS", "version": "2"}
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-ANCIENT_CIVILIZATIONS_BASICS-A",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS",
      "version": "2"
    },
    "evidence_role": "supports",
    "material": {
      "locator": "§3.1, “Early Civilizations”; subsections on attributes of early civilizations, urban concentration, surplus and specialization; see also §3 Section Summary",
      "description": "The section describes settled populations, concentrated urban communities, surplus production and specialization of labour; the section summary explicitly names urban settings, labour specialization and increasing social stratification. This is an introductory synthesis, not a universal definition applying identically to every early civilization."
    }
  }
}
```

Pinpoint URL: https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations  
Section summary: https://openstax.org/books/world-history-volume-1/pages/3-section-summary

Boundary: this source can support the general introductory proposition, but independent case studies below should be used to avoid treating the textbook's broad synthesis as the sole basis. Claim A's wording “early civilizations” is broad; evidence from one site cannot establish universality.

### EU B — agriculture, settlement and demography

Target: `EU-ANCIENT_CIVILIZATIONS_BASICS-B@2`  
Claim: `CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1`  
Source: proposed `SRC-ANCIENT_CIVILIZATIONS_BASICS@2`

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-ANCIENT_CIVILIZATIONS_BASICS-B",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {"record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS", "version": "2"}
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-ANCIENT_CIVILIZATIONS_BASICS-B",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS",
      "version": "2"
    },
    "evidence_role": "supports",
    "material": {
      "locator": "§2.3, “The Neolithic Revolution”; subsections “The Development of Agriculture” and “Neolithic Peoples”",
      "description": "The section describes agriculture emerging independently in different regions and discusses differing settlement and population consequences, including cases where settled agriculture was not adopted. It supports a qualified association with regional and temporal variation, not a single universal sequence or one-way causal law."
    }
  }
}
```

Pinpoint URL: https://openstax.org/books/world-history-volume-1/pages/2-3-the-neolithic-revolution

**Locator correction:** the correct OpenStax section is §2.3 “The Neolithic Revolution”. “The Development of Agriculture” is a subsection heading, not the section title.

### EU C — kinds of evidence about ancient societies

Target: `EU-ANCIENT_CIVILIZATIONS_BASICS-C@2`  
Claim: `CLM-ANCIENT_CIVILIZATIONS_BASICS-C@1`  
Source: proposed `SRC-ANCIENT_CIVILIZATIONS_BASICS@2`

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-ANCIENT_CIVILIZATIONS_BASICS-C",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {"record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS", "version": "2"}
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-ANCIENT_CIVILIZATIONS_BASICS-C",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS",
      "version": "2"
    },
    "evidence_role": "supports",
    "material": {
      "locator": "§1.2, “Primary Sources”; subsections “Learning to Evaluate Documents and Images” and “Hidden in History”",
      "description": "The section identifies documentary and textual materials, objects, works of art and other material traces as source material used to interpret the past. The locator supports the coexistence of textual and material evidence; it does not establish that every ancient society left written records or that one source class is inherently superior."
    }
  }
}
```

Pinpoint URL: https://openstax.org/books/world-history-volume-1/pages/1-2-primary-sources

**Important qualification:** the textbook's §1.2 contains a broad hierarchy favouring textual evidence over images/material traces. The Encyclopedia must not adopt that hierarchy as a general epistemic rule. Claim C's own wording is narrower and does not require it.

## 5. Proposed Source @2 identity

Proposed version of existing logical Source ID:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "SRC-ANCIENT_CIVILIZATIONS_BASICS",
  "record_type": "source",
  "provenance": {
    "method": "external_public_reference"
  },
  "content": {
    "source_identity": "OpenStax, World History, Volume 1, to 1500 (2023 edition)",
    "expression": "2023 published textbook edition",
    "representation": "OpenStax online HTML textbook",
    "external_ref": {
      "uri": "https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations"
    },
    "availability": "public",
    "preservation": "External source; Encyclopedia stores bibliographic identity and exact section locators, not a local copy."
  }
}
```

This proposed @2 repairs the existing generic source identity and makes clear that one logical textbook work is used at three section locators. The external URI is a representative stable section URL; each EU carries its own pinpoint locator. Do not record a licence as a machine field: the current Source profile has no licence property. Keep item-level rights evidence in the rights register.

## 6. Independent corroboration — proposed additional Source/Evidence Use records

These are candidate additions for a later authorization. They are not substitutes for the OpenStax locators and must not be counted as independent merely because they have distinct record IDs. The table records the exact role and limitation each publication can support.

| Candidate Source identity | Candidate Evidence Use target | Pinpoint locator | Rights / use status | Support boundary |
|---|---|---|---|---|
| McMahon et al. (2023), “Dense urbanism and economic multi-centrism at third-millennium BC Lagash,” *Antiquity* 97(393):596–615, DOI 10.15184/aqy.2023.36 | Claim A | Abstract; Introduction; Discussion; Conclusion | Article-level CC BY 4.0. Check any third-party material separately. | Strong case-specific evidence for dense urban occupation, walled quarters and multiple production foci at Lagash; not universal. |
| Fernández-Götz & Smith (2024), “The Archaeology of Early Cities: ‘What Is the City but the People?’,” *Annual Review of Anthropology* 53:231–247, DOI 10.1146/annurev-anthro-041222-094823 | Claim A | Abstract; sections on definitions, functions, methodological approaches and persistence/collapse | Article-level CC BY 4.0; third-party content requires separate credit-line review. | Broad review; contextualizes diversity, not a primary excavation record. |
| Twiss et al. (2024), “But some were more equal than others: Exploring inequality at Neolithic Çatalhöyük,” *PLOS ONE* 19(9):e0307067, DOI 10.1371/journal.pone.0307067 | Claim A | Abstract; Results and Discussion; Conclusion | Article text CC BY 4.0; Fig. 1 photo is separately credited and must not be reused without its own permission. | Important counterweight: differentiated assets do not automatically prove institutionalized hierarchy. |
| Lesure et al. (2021), “Large-Scale Patterns in the Agricultural Demographic Transition of Mesoamerica and Southwestern North America,” *American Antiquity* 86(3):593–612, DOI 10.1017/aaq.2021.23 | Claim B | Abstract; “Spatial Structure”; “Temporal Structure”; “The Agricultural Demographic Transition in Two Macroregions”; “A Look at Other Macroregions”; Conclusions | Article-level CC BY 4.0. | Strong regional settlement/demographic synthesis; prolonged, uneven transition, not universal global sequence. |
| Crema et al. (2024), “Regional variations in the demographic response to the arrival of rice farming in prehistoric Japan,” *Antiquity* 98(401):1290–1305, DOI 10.15184/aqy.2024.146 | Claim B | Abstract; Introduction; Results; Conclusions | Article-level CC BY 4.0. | Regional demographic trajectories after rice farming; radiocarbon-date frequency is a proxy with uncertainty, not a census. |
| Neil et al. (2016), “Isotopic evidence for residential mobility of farming communities during the transition to agriculture in Britain,” *Royal Society Open Science* 3(1):150522, DOI 10.1098/rsos.150522 | Claim B | Abstract; Introduction; methods/results | Article-level CC BY 4.0. | Gloucestershire case shows early farming is not equivalent to universal permanent sedentism. |
| Fort (2015), “Demic and cultural diffusion propagated the Neolithic transition across different regions of Europe,” *Journal of the Royal Society Interface* 12(106):20150166, DOI 10.1098/rsif.2015.0166 | Claim B | Abstract; Results and Discussion | Article-level CC BY 4.0. | Supports different mechanisms of spread across European regions; does not directly measure all settlement/demographic consequences. |
| Hawkes et al. (2022), “Grounding texts and theories of societal change,” *Antiquity* 96(387):611–627, DOI 10.15184/aqy.2022.28 | Claim C | Abstract; Introduction; Conclusions | Article-level CC BY 4.0. | Case-specific example combining written land-grant charters with archaeological survey; not a universal account of ancient evidence. |
| Styring et al. (2022), “Urban form and scale shaped the agroecology of early ‘cities’ in northern Mesopotamia, the Aegean and Central Europe,” *Journal of Agrarian Change* 22(4):831–854, DOI 10.1111/joac.12497 | Claims A and B, via two separate EUs if selected | Abstract; §4 | Article-level CC BY 4.0. | Comparative association between urban form and agricultural strategies; do not infer a simple one-way causal mechanism. |

### Existing Smithsonian EU — do not silently retain its current characterization

Current record `EU-ANCIENT-CIVILIZATIONS-SMITHSONIAN@1` points to `SRC-SMITHSONIAN-ANCIENT-AGRICULTURE@1`, whose URI is a Smithsonian Profiles bibliographic record for Zeder (2011). It is not the publisher's journal article. The current EU wording says “Smithsonian archaeological evidence”, which overstates what the linked catalog record itself is.

Recommended disposition for the next authorized pass:

- Do not represent the Smithsonian Profiles record as the journal article.
- Do not claim that the Profiles abstract is direct archaeological data.
- Preserve the existing @1 as historical record; do not delete or overwrite it.
- If Zeder's paper is retained, create a distinct Source identity for the *Current Anthropology* article, with DOI/publisher URI and explicit citation-only / rights-pending boundary in the rights register. The publisher labels it free to read but © Wenner-Gren Foundation, all rights reserved; this is not a reuse licence.
- Prefer the CC BY 4.0 regional studies in the table above for affirmative evidence links. Do not create a Zeder Evidence Use unless the actual article and its precise passage are reviewed and the use is explicitly authorized.

## 7. Proposed additional Source IDs (not registered)

If later authorized, suggested stable IDs:

- `SRC-MCMAHON-ETAL-LAGASH-2023`
- `SRC-FERNANDEZ-GOTZ-SMITH-EARLY-CITIES-2024`
- `SRC-TWISS-ETAL-CATALHOYUK-INEQUALITY-2024`
- `SRC-LESURE-ETAL-AGRICULTURAL-DEMOGRAPHIC-TRANSITION-2021`
- `SRC-CREMA-ETAL-RICE-FARMING-JAPAN-2024`
- `SRC-NEIL-ETAL-NEOLITHIC-MOBILITY-BRITAIN-2016`
- `SRC-FORT-NEOLITHIC-DIFFUSION-EUROPE-2015`
- `SRC-HAWKES-ETAL-GROUNDING-TEXTS-2022`
- `SRC-STYRING-ETAL-URBAN-FORM-AGROECOLOGY-2022`

Suggested Evidence Use IDs should be assigned only after the owner/editor selects the corroboration set; avoid pre-allocating IDs for candidates that may not be adopted.

## 8. Rights and attribution register entries to prepare

No licence or permission is adopted by this packet. Proposed rights-register facts:

- OpenStax 2023 book: CC BY-NC-SA 4.0; attribution and ShareAlike conditions apply; NonCommercial condition must be assessed against the project's chosen distribution model. Do not reproduce or adapt textbook text, images, figures, maps or tables until compatibility and component rights are checked.
- McMahon et al. 2023: article-level CC BY 4.0; attribute authors, title, journal, DOI and licence; check any third-party content separately.
- Fernández-Götz & Smith 2024: article-level CC BY 4.0; check third-party images/material separately.
- Twiss et al. 2024: article text CC BY 4.0; the Fig. 1 photograph has separate credit and is not cleared by the article-level licence alone.
- Lesure et al. 2021: article-level CC BY 4.0.
- Crema et al. 2024: article-level CC BY 4.0.
- Neil et al. 2016: article-level CC BY 4.0.
- Fort 2015: article-level CC BY 4.0.
- Hawkes et al. 2022: article-level CC BY 4.0; check third-party components separately.
- Styring et al. 2022: article-level CC BY 4.0; check third-party components/data separately.
- Zeder 2011: publisher says © Wenner-Gren Foundation, all rights reserved; “free” access is not reuse permission. Citation/link only pending separate review.

CC BY status of an article does not automatically license every image, map, dataset or third-party component appearing in it. Do not copy article figures or datasets into the Encyclopedia based solely on article-level licence statements. Do not bulk extract or ingest any source.

## 9. Acceptance checklist for a future implementation authorization

Before creating canonical @2 records, the owner/editor should approve the exact bounded operation list. The implementation should then satisfy all of the following:

- [ ] Pin the OpenStax edition and confirm the current book-level rights terms against the intended distribution model.
- [ ] Approve the proposed Source @2 identity and exact external reference.
- [ ] Approve the three Evidence Use @2 records exactly as mapped above, including locators and support limitations.
- [ ] Decide whether to add any independent CC BY corroboration sources; each selected Source/EU must be separately identified and mapped to one Claim.
- [ ] Decide how to version the Smithsonian EU/Source chain; do not relabel a bibliographic profile as the article.
- [ ] Keep Claims A/B/C at @1 unless separately authorized; no wording changes are included here.
- [ ] Keep all slice records HOLD; no INCLUDE/EXCLUDE, allowlist or release decision.
- [ ] Keep all R-01–R-10 rights/editorial decisions open until explicitly adopted.
- [ ] Re-fetch all affected records and dependent references at the resulting exact HEAD.
- [ ] Run the relevant schema/reference/slice tests and all required PR workflows on the exact resulting HEAD; report only observed results.

## 10. Recommendation

**Preferred minimal canonical scope, if separately authorized:** Source `SRC-ANCIENT_CIVILIZATIONS_BASICS@1 → @2`; three existing OpenStax Evidence Use records `@1 → @2`; no Claim changes; no Context/Scope/Relation changes; no Smithsonian relabelling; no additional sources in the first implementation pass.

**Preferred research-quality extension:** after the minimal pass, separately authorize a selected CC BY 4.0 corroboration set: McMahon + Twiss for Claim A; Lesure + Crema + Neil for Claim B; Hawkes for Claim C. This is a deliberate, manageable evidence-diversity set with positive and limiting cases. Fort and Styring can remain optional secondary support rather than expanding the first implementation unnecessarily.

All records remain HOLD after any such technical remediation. A later, separate editorial and rights decision is still required before first-edition inclusion.
