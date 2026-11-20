# R9 Archival Science and Settlement Geography — closure review
Date: 2026-11-20
Inspection branch: `mvp-public-contribution-design-2026-10-11`
Inspection PR: #22
Inspection PR HEAD at start of review: `33ddc9e0270547d8c59f42c681421f235ee58894`

## Purpose and change boundary

This dossier records a current-head, record-level review of the Archival Science and Settlement Geography R9 slices. It is a research/audit document only. No canonical JSON, source identity, claim, Evidence Use, relation, coverage count, allowlist, publication status or release decision was changed by this review. It does not create authorization for canonical edits and does not grant rights.

Both slices remain HOLD. No INCLUDE/EXCLUDE, preview allowlist, release, deployment, merge or main-branch change is authorized.

## 1. Archival Science — exact graph and authorization closure

### 1.1 Current canonical chain re-fetched

| Record | Current version | Current dependency / role |
|---|---:|---|
| `SRC-ARCHIVAL_SCIENCE` | 2 | SAA, “Archives 101: Basic Principles” |
| `SRC-ARCHIVAL_SCIENCE-ICA` | 1 | ICA, ISAD(G), Second Edition |
| `CLM-ARCHIVAL_SCIENCE-A` | 2 | Four processing activities, attributed to SAA |
| `EU-ARCHIVAL_SCIENCE-A` | 2 | SAA “Processing”; appraisal, arrangement, description, preservation |
| `CLM-ARCHIVAL_SCIENCE-B` | 3 | Provenance and discernible original order |
| `EU-ARCHIVAL_SCIENCE-B` | 3 | SAA “Principle of Provenance” and “Arrangement”; explicitly preliminary-draft scoped |
| `CLM-ARCHIVAL_SCIENCE-C` | 2 | Multilevel description under ISAD(G) |
| `EU-ARCHIVAL_SCIENCE-C` | 2 | ICA ISAD(G) §1.1 and §§2.1/2.3 |
| `CTX-ARCHIVAL_SCIENCE` | 2 | Context targeting Claim A@2 |
| `SCP-ARCHIVAL_SCIENCE` | 2 | Scope targeting Claim A@2 |

The exact-version master register contains all ten records above, each as HOLD. The Claim→EU→Source references in the three evidence chains are internally version-aligned in the re-fetched records. The separate cross-slice relation alignment authorization covers only the specified relation's move to SAA Source@2 and Claim A@2; it does not expand the archival slice's source/claim authorization.

### 1.2 ICA rights finding

The official ICA-hosted ISAD(G), Second Edition PDF copyright page (printed p. 2) states: “Multiplication of this publication is free if due acknowledgement is made.” This is an affirmative, attribution-conditioned permission for multiplication/reproduction of this particular publication. It is not a Creative Commons licence and does not expressly settle adaptation, translation, modification, sublicensing, commercial exploitation, third-party components or the project's own licence/distribution compatibility.

The current Claim C/EU-C do not reproduce ICA wording, tables, diagrams or page images. They state a factual description independently and provide section pinpoints (§1.1, §§2.1 and 2.3). Accordingly, the reproduction permission is not being relied upon as a blanket permission for derivative use; the immediate canonical use is factual paraphrase plus citation. Any later reproduction must retain due acknowledgement and the ICA copyright notice. Seek ICA clarification before adaptation, translation or materially different commercial/derivative reuse.

### 1.3 Remaining authorization blocker

The active `R9-ARCHIVAL-SCIENCE-REMEDIATION-001` authorization explicitly says:
- do not modify `SRC-ARCHIVAL_SCIENCE` or `SRC-ARCHIVAL_SCIENCE-ICA`;
- do not modify Claims A/C or Evidence Use A/C;
- do not recreate either Source;
- the current authorization's allowed changes were limited to Claim B@2→@3, EU-B@2→@3, Context/Scope v1→v2 and named documentation/coverage synchronization.

The manifest's rights boundary also says the existing ICA Source was already present and that this authorization does not retroactively authorize its creation. Therefore the current ICA Source@1 → Claim C@2 → EU-C@2 chain remains a distinct provenance/authorization question, even though the source identity, pinpoint and graph are now visible and the ICA copyright page provides a conditional reproduction permission. Rights permission and project-owner authorization are separate controls; neither substitutes for the other.

**Disposition:** no canonical edit is permitted under the current archival authorization to change Source ICA, Claim C or EU-C. Owner/editorial authority must explicitly decide whether to ratify the existing exact chain or authorize a replacement/narrowing. Keep the slice HOLD until that decision, SAA item-specific rights assessment, privacy/donor/access review, cultural-protocol review and independent archival editorial/Human View are complete.

## 2. Settlement Geography — current record-level review

### 2.1 Current canonical chain re-fetched

| Record | Version | Finding |
|---|---:|---|
| `SRC-SETTLEMENT_GEOGRAPHY` | 1 | UN-Habitat, *Applying the Degree of Urbanisation* (2021); source identity only, no item-level locator |
| `CLM-SETTLEMENT_GEOGRAPHY-A` | 1 | “continuous scale” framing; plausible but needs exact distinction between continuum and Level 1 classes |
| `EU-SETTLEMENT_GEOGRAPHY-A` | 1 | generic description only; no pinpoint locator |
| `CLM-SETTLEMENT_GEOGRAPHY-B` | 1 | says “cities, small towns and rural areas”; terminology is imprecise |
| `EU-SETTLEMENT_GEOGRAPHY-B` | 1 | generic description only; no pinpoint locator |
| `CLM-SETTLEMENT_GEOGRAPHY-C` | 1 | says method is for statistical comparison and does not replace national definitions; substantively aligned |
| `EU-SETTLEMENT_GEOGRAPHY-C` | 1 | generic description only; no pinpoint locator |
| `CTX-SETTLEMENT_GEOGRAPHY` | 1 | generic context, target Claim A@1 |
| `SCP-SETTLEMENT_GEOGRAPHY` | 1 | generic scope, target Claim A@1 |

The three Claim→EU→Source identity/version chains are structurally aligned, but all three EUs lack direct locators. The current graph is not evidence-depth complete. The cross-slice relation `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY` also references Source@1 and Claim A@1; any source/claim version change must account for this dependency under its own authorization.

### 2.2 Preferred replacement source: Eurostat 2026 Statistical Report

Preferred source candidate: Eurostat, *Review and implementation of the degree of urbanisation — 2026 edition*, Statistical Reports, DOI `10.2785/3471430`, publication date 17 February 2026.

Verified official locators:
- §1.1, printed p. 6: methodology uses population-density and population-size thresholds applied to a population grid.
- §1.2, printed p. 6: national definitions differ; harmonised methodology enables cross-country comparisons.
- §2.1, printed p. 7: the Level 1 classification has three classes — cities; towns and semi-dense areas; rural areas. It starts from 1 km² grid cells, classifies by population density and contiguous population, then classifies small spatial units by population shares.
- §2.1, printed p. 7: Level 2 subdivides Level 1 into seven classes, including dense towns, semi-dense towns, villages and dispersed rural areas.
- §2.1, printed p. 7: the methodology complements rather than replaces national definitions.

Rights: the official PDF states that, unless otherwise noted, reuse is authorized under CC BY 4.0 with appropriate credit and indication of changes. It excludes the cover photo, all maps other than Maps 4.1 and 4.2, other photos, and third-party administrative boundaries for Maps 4.1 and 4.2. The proposed first-edition use is text-only factual paraphrase and citations; no maps, photos, figures or third-party assets are proposed. The report also states it should not be considered representative of the European Commission's official position. Attribute it as a Eurostat Statistical Report, not as an adopted Commission policy statement.

This is a materially better rights basis for the intended text-only first-edition use than the 2021 joint manual, whose stated licence is CC BY-NC-SA 3.0 IGO and therefore carries a NonCommercial condition and ShareAlike requirement for adaptations. This comparison does not resolve the Encyclopedia's own licence/distribution policy.

### 2.3 Claim-level fit and recommended editorial direction

- **Claim A:** retain the international-comparison/urban–rural-continuum concept, but make explicit that the continuum is represented through a defined classification. The 2026 report supports Level 1's three classes and its purpose. Do not imply that the classification is a universal legal definition of settlement status.
- **Claim B:** correct “малые города” as a standalone equivalent for “towns and semi-dense areas”. Recommended terminology: “города; малые города и территории средней плотности (towns and semi-dense areas); сельские территории”. If describing the method, distinguish Level 1's three classes from Level 2's seven subclasses. The 2026 report supports both.
- **Claim C:** retain the explicit complement-not-replace boundary for national definitions. This is directly supported by §1.1 and §2.1. Do not imply that the methodology supersedes national legal or administrative definitions.

### 2.4 Required bounded authorization before canonical implementation

No Settlement Geography-specific bounded authorization was found in the current `RELEASE/EDITORIAL-CORRECTION.json`. The 2021→2026 source replacement and any Claim/EU changes are therefore not authorized yet. The following exact implementation scope is recommended for owner decision:

1. Version `SRC-SETTLEMENT_GEOGRAPHY@1` to @2 with the full Eurostat 2026 bibliographic identity, DOI, publication date, official URI, CC BY 4.0 attribution/asset exclusions and explicit “not the Commission's official position” limitation.
2. Version Claims A/B/C @1→@2 only with the bounded wording changes described above; preserve their Claim IDs and documented_fact types.
3. Version EUs A/B/C @1→@2 with exact §1.1, §1.2 and §2.1 pinpoints and direct support boundaries; update all Claim and Source references to exact @2.
4. Version Context and Scope @1→@2 only if needed to reflect the method's statistical/comparative boundary; preserve their IDs/types and target Claim A@2.
5. Separately authorize and version `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY` to update only its affected Source/Claim endpoint references. Do not assume the slice authorization automatically authorizes a cross-slice Relation.
6. Update only the Settlement Geography README, rights screen, R9 remediation dossier and exact-version register under the named authorization. No coverage denominator change is expected because no new record is proposed.

Release conditions remain independent: exact-head tests, rights-policy compatibility, independent geographical/statistical editorial review and Human View. No automatic INCLUDE follows from a better source or corrected locators.

## 3. Work order

1. Obtain explicit owner ratification or replacement decision for the existing ICA Source@1 / Claim C@2 / EU-C@2 archival chain. Do not modify it under the current archival authorization.
2. Obtain explicit owner approval for the Settlement Geography Eurostat 2026 bounded implementation scope above. Until then, preserve all nine records at v1 and HOLD.
3. Continue to Labour Economics only after the separate Path B (ILO-led replacement) owner decision; no such decision is inferred here.

## Evidence links

- ICA ISAD(G), official PDF: https://www.ica.org/app/uploads/2024/01/CBPS_2000_Guidelines_ISADG_Second-edition_EN.pdf
- Eurostat 2026 publication page: https://ec.europa.eu/eurostat/web/products-statistical-reports/w/ks-01-26-004
- Eurostat 2026 official PDF: https://ec.europa.eu/eurostat/documents/7870049/23036903/KS-01-26-004-EN-N.pdf/a9203c0d-53be-f7af-73e5-d53e0e7b7a2e?t=1771237274568&version=1.0
- UN-Habitat 2021 manual page: https://unhabitat.org/knowledge/publications/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas
- Eurostat methodology page: https://ec.europa.eu/eurostat/en/web/degree-of-urbanisation/methodology


## Addendum — exact SAA site-wide terms and parallel owner decision package (2026-11-20)

A further source-rights check located the SAA “Disclaimer & Copyright Statement” (updated 2022-01-18). It permits use, copying and distribution of documents delivered from the SAA web server and related graphics for private, non-commercial and educational purposes only, not for resale, provided the SAA copyright and permission notices are retained. Other rights are reserved; SAA names and logos require separate written permission. The SAA Archives 101 page is itself marked PRELIMINARY DRAFT. This is a materially narrower reuse basis than an unrestricted open licence. The current record content uses independently worded factual propositions and locators, not copied page prose or graphics; this does not eliminate the need to assess the project's eventual distribution model.

A parallel, more detailed owner-decision package is present on the current PR head:
`RELEASE/R9-ARCHIVAL-SCIENCE-AND-SETTLEMENT-GEOGRAPHY-DECISION-PACKAGE-2026-11-20.md`.
It records two explicit owner choices: (1) ratify the exact ICA Source@1 / Claim C@2 / EU-C@2 chain, or authorize a separately specified replacement/removal; and (2) approve or reject the proposed Eurostat 2026 Settlement Geography source replacement and its nine-record bounded scope, including the dependent cartography Relation reference alignment. This closure review is supplementary and does not supersede that decision package.

Evidence: SAA, “Disclaimer & Copyright Statement”: https://www2.archivists.org/disclaimer
