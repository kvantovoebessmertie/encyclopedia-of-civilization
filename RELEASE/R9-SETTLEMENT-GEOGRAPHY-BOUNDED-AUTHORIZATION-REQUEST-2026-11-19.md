# R9 Settlement Geography — bounded authorization request

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: REQUEST ONLY — NOT AUTHORIZED

## Purpose

Request an explicit, bounded owner decision before correcting the three generic Evidence Use records in `settlement-geography-basics`. This document does not itself authorize canonical changes.

## Exact current inventory

At PR #22 HEAD `42e698407853e257ef6b2fc70400f914e58240a6`, the slice contains nine records, all at v1:

| Record | Current version | Blob SHA | Finding |
|---|---:|---|---|
| `SRC-SETTLEMENT_GEOGRAPHY` | 1 | `bba3e8a072d8242a51711278030dd0906f19c08a` | UN-Habitat, *Applying the Degree of Urbanisation*; no pinpoint locator |
| `CLM-SETTLEMENT_GEOGRAPHY-A` | 1 | `23f8f7566179e2381341bc55814e552324082f10` | Broad urban-to-rural continuum proposition |
| `CLM-SETTLEMENT_GEOGRAPHY-B` | 1 | `a4f15442b9488b3994447708c1815faf5e1510b4` | Consistent criteria for cities, towns and rural areas |
| `CLM-SETTLEMENT_GEOGRAPHY-C` | 1 | `31169d48ac948348f884b0b0ee2993936abf850e` | Statistical comparison does not replace national definitions |
| `EU-SETTLEMENT_GEOGRAPHY-A` | 1 | `ff83bf12f77fb50616a2393d0d569f5abb17c063` | No claim-specific locator |
| `EU-SETTLEMENT_GEOGRAPHY-B` | 1 | `100fdf09f180c6179e774c693181a300163e4823` | No claim-specific locator |
| `EU-SETTLEMENT_GEOGRAPHY-C` | 1 | `2ace0f72d9308b37692cda2cf90a0cc3b2012310` | No claim-specific locator |
| `CTX-SETTLEMENT_GEOGRAPHY` | 1 | `5b2a2dab427ec3b5c312c1d0886ca0953cbbce75` | Targets Claim A v1 |
| `SCP-SETTLEMENT_GEOGRAPHY` | 1 | `756a0eb17b31c025f209c6f1e80a28db46bdcaf2` | Targets Claim A v1 |

All current Claim provenance references point to Source v1; all three EU records point to the matching Claim v1 and Source v1. The graph is internally version-consistent but the Evidence Use records lack pinpoint support.

## Source and rights decision required

The current Source is the UN-Habitat methodological manual:
https://unhabitat.org/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas

The consolidated rights screen identifies a preferred text-only alternative:
Eurostat, *Review and implementation of the degree of urbanisation*, 2026 edition, Statistical Reports, DOI 10.2785/3471430:
https://doi.org/10.2785/3471430

The report's front matter states CC BY 4.0 for EU-owned content, with attribution and change indication, while excluding third-party cover photography, most maps, other photos and administrative-boundary content. No such assets are proposed for reuse. The report also states that it is not representative of the European Commission's official position.

The project must decide whether to:
1. retain UN-Habitat as the canonical source and authorize precise section/page locators after source-specific rights review; or
2. add a separate Eurostat Source record and authorize the relevant Evidence Use records to cite it; or
3. use a controlled source substitution, with explicit versioned provenance changes.

No option is selected in this request. Do not silently replace the current Source identity or infer that the Eurostat report's licence resolves the Encyclopedia's own content licence or all third-party asset rights.

## Proposed bounded work if owner approves option 2

Candidate changes for explicit approval only:

- Create a separately identified Eurostat Source record (candidate identifier only; final canonical ID must be owner-approved).
- Version Claims A–C only if necessary to align provenance with the approved source chain; preserve their current narrow propositions unless editorial review requires an explicitly approved wording change.
- Version EU-A/B/C with claim-specific locators using Eurostat §1.2 (printed p. 6) and §2.1 (printed p. 7), after direct source-page verification:
  - EU-A: urban–rural continuum and international comparability.
  - EU-B: population-grid method and Degree of Urbanisation classification levels.
  - EU-C: methodology complements rather than replaces national definitions.
- Version Context and Scope only if required to align target versions or preserve the explicit national-definition boundary.
- Update only this slice README, R9 follow-up/register, the rights/attribution screen and the relevant coverage fields if a new Source record is approved.
- Preserve the nine-record profile if option 1 or 3 is selected; if option 2 adds a Source, request explicit approval for the resulting record-count/source-count delta before changing the coverage manifest.

## Prohibited pending approval

- No canonical JSON changes, Source IDs, Claim rewrites, EU locator changes or coverage-manifest changes.
- No publication/completion status changes.
- No allowlist or INCLUDE/EXCLUDE decision.
- No relation edits, validator changes, release-gate changes, deployment or merge.
- Do not treat the Degree of Urbanisation as a replacement for national legal or statistical definitions.
- Do not reproduce report text, tables, maps, figures, photos or third-party material.

## Release boundary

The slice remains HOLD pending explicit authorization, source-specific rights review, independent settlement-geography editorial review, Human View and exact-head CI. This request is not publication approval.
