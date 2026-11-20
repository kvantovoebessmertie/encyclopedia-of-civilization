# R9 Archival Science and Settlement Geography — Decision Package

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Workstream: PR #22, Work Package 1  
Status: **AUDIT COMPLETE FOR THIS PASS — OWNER DISPOSITIONS AND RELEASE HOLDS REMAIN**

## Purpose and limits

This package records exact source-rights, authorization, evidence-fit and dependency findings for two R9 slices. It does not grant copyright permission, authorize canonical edits, approve inclusion, or change publication/release state. No Claim, Source, Evidence Use, Context, Scope, Relation, coverage count or allowlist is changed by this package.

## 1. Archival Science

### Exact current graph

- `SRC-ARCHIVAL_SCIENCE@2` — Society of American Archivists (SAA), “Archives 101: Basic Principles”.
- `SRC-ARCHIVAL_SCIENCE-ICA@1` — International Council on Archives (ICA), *ISAD(G): General International Standard Archival Description*, Second Edition.
- `CLM-ARCHIVAL_SCIENCE-A@2` / `EU-ARCHIVAL_SCIENCE-A@2` — four processing activities from SAA.
- `CLM-ARCHIVAL_SCIENCE-B@3` / `EU-ARCHIVAL_SCIENCE-B@3` — provenance and preservation of discernible original order from SAA.
- `CLM-ARCHIVAL_SCIENCE-C@2` / `EU-ARCHIVAL_SCIENCE-C@2` — multilevel description hierarchy from ICA.
- `CTX-ARCHIVAL_SCIENCE@2`, `SCP-ARCHIVAL_SCIENCE@2`.

### Rights findings

**SAA.** The exact source page is marked PRELIMINARY DRAFT. SAA's site-wide copyright notice grants permission to use, copy and distribute documents delivered from its web server and related graphics for private, non-commercial and educational purposes only, not for resale, with the SAA copyright and permission notices retained. Other rights are reserved; SAA names/logos need separate written permission. The current records use independently worded factual statements and citations, not copied page expression. The site permission nevertheless does not support copying/distributing the SAA page or its expressive content for resale/commercial use. This remains an important project-level distribution constraint and does not make the preliminary guide a professional standard.

**ICA.** The official ICA-hosted PDF's printed p. 2 states that multiplication of the publication is free if due acknowledgement is made. This is an affirmative reproduction permission for the identified publication, conditioned on acknowledgement. It is not expressed as a CC licence and does not expressly authorize adaptations, translations, commercial exploitation, sublicensing or third-party components. The current records use factual paraphrase and section pinpoints; no ICA text, tables, diagrams or page images are reproduced.

### Authorization and evidence boundary

The active `R9-ARCHIVAL-SCIENCE-REMEDIATION-001` entry authorizes preservation of the already-present SAA Source@2 and ICA Source@1, and explicitly says that this does not retroactively authorize the ICA Source's creation. It authorizes the Claim B/EU-B/Context/Scope remediation already listed, but does not authorize creating, changing or newly ratifying the ICA Source/Claim C/EU-C dependency. The ICA rights notice cannot cure this authorization gap.

**Owner disposition required for the ICA branch — choose one:**

A. Ratify the exact existing `SRC-ARCHIVAL_SCIENCE-ICA@1`, `CLM-ARCHIVAL_SCIENCE-C@2`, and `EU-ARCHIVAL_SCIENCE-C@2` dependency as intended current content, without further canonical edits; or  
B. authorize a separately specified replacement/removal of the ICA branch and dependent Claim C/EU-C, with exact record versions and replacement source/claim semantics named before edits.

No path is executed by this report. The slice remains **HOLD** pending owner disposition, independent archival editorial review, Human View, project-level rights decision and exact-head release checks.

### Additional archival ethics boundary

Copyright and source permission do not settle archival access, privacy, confidentiality, donor agreements, cultural sensitivity, consent, sacred/restricted knowledge, custody or legal ownership. The existing Context/Scope exclusions remain appropriate and must not be weakened.

## 2. Settlement Geography

### Exact current graph

The slice contains nine v1 records:
- `SRC-SETTLEMENT_GEOGRAPHY@1`
- `CLM-SETTLEMENT_GEOGRAPHY-A/B/C@1`
- `EU-SETTLEMENT_GEOGRAPHY-A/B/C@1`
- `CTX-SETTLEMENT_GEOGRAPHY@1`
- `SCP-SETTLEMENT_GEOGRAPHY@1`

The current Source is the joint UN-Habitat *Applying the Degree of Urbanisation* 2021 manual. The three Evidence Use records contain no exact page/section locators. Claim B's phrase “малые города” is too imprecise for the Level 1 categories and should not stand as a translation of “towns and semi-dense areas”.

### Preferred replacement source and verified support

Preferred source: Eurostat, *Review and implementation of the degree of urbanisation — 2026 edition*, Statistical Reports, published 17 February 2026, DOI `10.2785/3471430`.

The official report states:
- printed p. 2/front matter: EU-owned content is reusable under CC BY 4.0 unless otherwise noted; appropriate credit and indication of changes are required. The cover photo, maps other than Maps 4.1/4.2, other photos, and third-party administrative boundaries for Maps 4.1/4.2 are excluded.
- §1.2, printed p. 6: the harmonised method supports international comparisons; national urban/rural definitions vary.
- §2.1, printed p. 7: Level 1 classes are “cities”, “towns and semi-dense areas”, and “rural areas”; it uses 1 km² population-grid cells, population density and population-size thresholds; Level 2 subdivides into seven categories; and the method complements rather than replaces national definitions.
- front matter, printed p. 2: the report should not be considered representative of the European Commission's official position. Cite it as a Eurostat Statistical Report, not as an adopted Commission policy statement.

This is a stronger and more precise text-only rights/source route than the multi-organization 2021 manual for the proposed use. No maps, photographs, graphics or third-party boundary data are needed or authorized.

### Proposed nine-record remediation — NOT YET AUTHORIZED

If the owner approves the Eurostat path, prepare a bounded authorization covering exactly:

1. `SRC-SETTLEMENT_GEOGRAPHY@1 → @2`: identify the exact Eurostat 2026 report, DOI, publication date, CC BY 4.0 notice and excluded third-party assets; pin §1.2 and §2.1.
2. `CLM-SETTLEMENT_GEOGRAPHY-A@1 → @2`: retain the urban–rural continuum / international-comparison proposition, bounded to the Eurostat methodology.
3. `CLM-SETTLEMENT_GEOGRAPHY-B@1 → @2`: correct Level 1 wording to “cities, towns and semi-dense areas, and rural areas”; optionally distinguish Level 2's seven categories without calling the Level 1 intermediate class simply “small towns”.
4. `CLM-SETTLEMENT_GEOGRAPHY-C@1 → @2`: retain the complement-not-replace-national-definitions boundary.
5. `EU-SETTLEMENT_GEOGRAPHY-A/B/C@1 → @2`: add exact §1.2/§2.1 pinpoints, current Claim/Source references, attribution and precise support boundaries.
6. `CTX-SETTLEMENT_GEOGRAPHY@1 → @2` and `SCP-SETTLEMENT_GEOGRAPHY@1 → @2`: bound the slice to an introductory explanation of this statistical classification, distinguish Level 1 from Level 2, and state that the Eurostat report is not an official Commission position or a substitute for national definitions.
7. Update only the Settlement Geography README and named R9 audit/register/rights/remediation documentation.
8. Preserve publication/completion status and all release decisions; no INCLUDE/EXCLUDE, allowlist, preview, publication or merge.

### Cross-slice dependency that must be included in any authorization

The existing `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@2` references `SRC-SETTLEMENT_GEOGRAPHY@1` and `CLM-SETTLEMENT_GEOGRAPHY-A@1` in both provenance and participants. The existing cartography relation-alignment authorization explicitly preserves these Settlement Geography v1 references. If Settlement Geography advances to v2, that Relation will need a separate, exact reference-only authorization to advance the corresponding two references to v2 while preserving relation type, participants/order, roles, direction, frame, and all semantics. Do not update it under the existing cartography authorization.

### Owner disposition required

Approve or reject the Eurostat replacement path above. No canonical changes are made pending explicit approval of the source replacement and the nine-record scope, including the dependent Relation alignment. The slice remains **HOLD**.

## 3. Verified public sources

- ICA, *ISAD(G)* Second Edition, printed p. 2: https://www.ica.org/app/uploads/2024/01/CBPS_2000_Guidelines_ISADG_Second-edition_EN.pdf
- SAA, “Disclaimer & Copyright Statement”: https://www2.archivists.org/disclaimer
- SAA, “Archives 101: Basic Principles”: https://www2.archivists.org/groups/diverse-sexuality-and-gender-section/information-for-community-archives-archives-101-basic-principles
- Eurostat publication page: https://ec.europa.eu/eurostat/web/products-statistical-reports/w/ks-01-26-004
- Eurostat 2026 report PDF: https://ec.europa.eu/eurostat/documents/7870049/23036903/KS-01-26-004-EN-N.pdf/a9203c0d-53be-f7af-73e5-d53e0e7b7a2e?t=1771237274568&version=1.0

## 4. Session disposition

- Archival Science rights screen and README updated with the exact SAA and ICA terms; canonical records untouched.
- Settlement Geography's nine-record graph and proposed Eurostat replacement scope reviewed; canonical records untouched.
- The cross-slice Relation dependency was identified and included in the required authorization boundary.
- Both slices remain HOLD.
- No INCLUDE/EXCLUDE decision, public allowlist, merge, deployment or release was made.


## 5. Owner decisions and implementation record — 2026-11-20

### Archival Science — option A approved

The project owner explicitly ratified the exact existing dependency `SRC-ARCHIVAL_SCIENCE-ICA@1` → `CLM-ARCHIVAL_SCIENCE-C@2` → `EU-ARCHIVAL_SCIENCE-C@2` as intended current content, without canonical edits. The ratification is recorded as `R9-ARCHIVAL-SCIENCE-OWNER-RATIFICATION-2026-11-20` in `RELEASE/EDITORIAL-CORRECTION.json`. It resolves only the owner-authorization/provenance mismatch. It does not expand copyright permissions, establish project-level licence compatibility, or close independent editorial, privacy/donor/access, cultural-protocol or Human View review. Archival Science remains **HOLD**.

### Settlement Geography — Eurostat path approved and implemented

The project owner explicitly approved the Eurostat 2026 source replacement and the bounded nine-record scope, including separate reference-only alignment of the dependent cross-slice Relation. Implementation is recorded under `R9-SETTLEMENT-GEOGRAPHY-EUROSTAT-REMEDIATION-2026-11-20` and `R9-SETTLEMENT-GEOGRAPHY-CROSS-RELATION-ALIGNMENT-2026-11-20` in `RELEASE/EDITORIAL-CORRECTION.json`.

- All nine slice records advanced from @1 to @2.
- Claims retain IDs and documented_fact types; Claim B uses exact Level 1 terminology.
- Evidence Use A–C now contain exact §1.2 / §2.1 locators, current @2 Claim/Source references and support boundaries.
- Context and Scope point to Claim A@2 and preserve the statistical/national-definition limits.
- `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY` advanced from @2 to @3. Only the two Settlement Geography references advanced; Cartography references, participant order, roles, relation type, direction, frame and method were preserved.
- All publication/completion states were preserved. The Settlement Geography denominator remains nine; no coverage denominator changed.

Both slices remain **HOLD**. No INCLUDE/EXCLUDE, allowlist, publication, deployment, merge or release decision was made.
