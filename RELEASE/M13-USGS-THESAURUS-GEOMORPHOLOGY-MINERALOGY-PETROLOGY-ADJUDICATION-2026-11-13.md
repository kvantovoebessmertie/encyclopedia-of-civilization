# M13 duplicate-source adjudication: USGS Thesaurus — geomorphology, mineralogy, and petrology

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `06aec1c16c35874c7fc53f6bbf6b4d50d1d112ab`  
Scope: one shared-URI group with three Source records and nine linked Claims. Source, Evidence Use and Claim records were inspected directly; the USGS thesaurus entries were checked separately.

## 1. Executive findings

| Shared URI | Source IDs | Linked Claims | Adjudication |
|---|---:|---:|---|
| `https://apps.usgs.gov/thesaurus/thesaurus-full.php` | 3 | 9 | One USGS Thesaurus resource, not three independent publications. It directly defines the three disciplines, but it is a broad/shallow controlled vocabulary and does not support all process, identification and interpretation claims. |

All three Source identity fields are descriptive sentences about the discipline rather than the actual title of the referenced resource:

- `SRC-GEOMORPHOLOGY_BASICS`
- `SRC-MINERALOGY_BASICS`
- `SRC-PETROLOGY_BASICS`

The common URI is the USGS Thesaurus. Its current search-indexed entries provide specific discipline definitions. The root page returned HTTP 403 on direct retrieval during this review, but the current search-indexed USGS content exposed the relevant entries and descriptions.

**Totals: 3 Source records, 9 linked Claims, one source identity.** Same-URL IDs do not create independent corroboration.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed. This is a source-fit report only.

## 2. Claim-level review

### Geomorphology

| Claim | Source fit |
|---|---|
| `CLM-GEOMORPHOLOGY_BASICS-A` — geomorphology studies landforms and the processes that form them | Direct. The USGS Thesaurus entry defines geomorphology as the branch of geology dealing with surface land features and the processes that create and change them. A term-specific locator is available at `https://apps.usgs.gov/thesaurus/term-simple.php?code=468&thcode=2`. |
| `CLM-GEOMORPHOLOGY_BASICS-B` — erosion, weathering, deposition and tectonic processes can change relief | Partial. The thesaurus defines geomorphology through landforms and formative/changing processes and separately lists erosion, sedimentation, tectonic processes and related terms. It does not directly establish the full causal list in this Claim. Add a geomorphology text or USGS process-specific reference with sections on erosion, weathering, deposition and tectonics. |
| `CLM-GEOMORPHOLOGY_BASICS-C` — landforms should be considered with active processes and observation scale | Not directly supported by the thesaurus definition. Scale-of-observation and process-based interpretation require a geomorphology methods/reference source; the Claim should not be treated as proven by a one-line discipline definition. |

### Mineralogy

| Claim | Source fit |
|---|---|
| `CLM-MINERALOGY_BASICS-A` — mineralogy studies naturally occurring inorganic elements and compounds | Direct. The USGS Thesaurus defines mineralogy as the study of naturally occurring inorganic elements or compounds. |
| `CLM-MINERALOGY_BASICS-B` — minerals are characterized by composition, structure and physical properties | Partial. The default USGS Thesaurus entry defines the discipline but does not list all three characteristics as mineral properties. A separate Marine Realms Information Bank entry at `https://apps.usgs.gov/thesaurus/term-simple.php?code=720&thcode=61` describes mineralogy as the study of mineral chemistry, crystalline structure and physical properties. That is a different thesaurus namespace/entry and must be cited explicitly if used; it is not an independent source simply because it is a separate term page. |
| `CLM-MINERALOGY_BASICS-C` — mineral identification requires matching observations with diagnostic characteristics | Not directly supported by the current linked USGS Thesaurus entry. Add a mineral-identification reference that explains diagnostic properties and testing methods. |

### Petrology

| Claim | Source fit |
|---|---|
| `CLM-PETROLOGY_BASICS-A` — petrology studies the origin, structure and composition of rocks | Direct. The USGS Thesaurus defines petrology as the branch of earth sciences concerned with the origin, structure, alteration and composition of rocks. A term-specific locator is `https://apps.usgs.gov/thesaurus/term-simple.php?code=883&thcode=2`. |
| `CLM-PETROLOGY_BASICS-B` — rocks are classified by composition and origin | Partial. The thesaurus definition identifies composition and origin as central to petrology, but does not itself set out a rock-classification scheme. Add an introductory petrology/geology reference for igneous, sedimentary and metamorphic classification and its criteria. |
| `CLM-PETROLOGY_BASICS-C` — interpretation depends on mineral composition and geological context | Partial. The thesaurus identifies composition, structure, alteration and origin, but does not establish the full contextual interpretation method. Add a petrology reference that treats mineral assemblages, texture, formation conditions and geological setting. |

## 3. Evidence Use quality

All nine Evidence Use records have the generic description:

“Источник используется для представления утверждения без вывода за пределы указанного материала.”

None identifies a term entry, term code, section, page or passage. The generic sentence does not show which part of the thesaurus supports each Claim.

The USGS Thesaurus is a controlled vocabulary intended to help users find scientific information. It is not a substitute for a textbook, technical monograph or process-specific evidence when a Claim goes beyond the meaning of a discipline term.

## 4. Adjudication and next actions

1. Count the three Source IDs as one USGS Thesaurus source identity for independence analysis.
2. Preserve the three Claim/Evidence Use chains; do not merge Source IDs or alter canonical records solely because the URI is shared.
3. Correct Source identity metadata only through an authorized versioned change: identify the resource as **U.S. Geological Survey Thesaurus**, and record the exact term entry/namespace as the locator.
4. Use the default USGS Thesaurus namespace (`thcode=2`) for the geomorphology and petrology term pages. Do not confuse the separate MRIB namespace (`thcode=61`) with the default USGS Thesaurus entry.
5. Add distinct technical sources for the process, diagnostic and interpretive Claims:
   - geomorphology: erosion, weathering, sediment transport/deposition, tectonic processes and scale;
   - mineralogy: diagnostic mineral properties and identification methods;
   - petrology: rock classification, mineral assemblages, texture and geological context.
6. Add exact term-level or section-level locators to the Evidence Use records through authorized corrections. Run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA after any canonical changes.

## 5. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records source identity, term-level support and limitations. It is not a release approval or authorization to edit canonical records.
