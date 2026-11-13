# MVP Pilot Candidate Screening — Geomorphology Claim A

Date: 2026-10-11  
Canonical corpus revision: `203a7028e08da394fd44630fe38727be07bc8849` (`main`)  
Status: **HOLD — promising single-Claim pilot candidate; not approved for publication**

## Exact candidate set

- Claim: `CLM-GEOMORPHOLOGY_BASICS-A@1`
- Evidence Use: `EU-GEOMORPHOLOGY_BASICS-A@1`
- Source: `SRC-GEOMORPHOLOGY_BASICS@1`

Canonical record paths were checked on `main` at the revision above. This screening does not change those records and does not use provisional M13 scores as publication approval.

## Claim and evidence fit

Claim statement: “Геоморфология относится к наукам о формах земной поверхности и процессах их формирования.”

The stored Source record identifies the USGS Thesaurus and stores `https://apps.usgs.gov/thesaurus/thesaurus-full.php`. The exact USGS Thesaurus entry for geomorphology is available at:

- `https://apps.usgs.gov/thesaurus/term-simple.php?code=468&thcode=2`
- It defines geomorphology as a branch of geology dealing with surface land features and the processes that create and change them.

This directly supports the core statement. However, the existing Evidence Use description is boilerplate and contains no term-level pinpoint. For a reader pilot, the displayed evidence link should lead directly to the exact term, with the source identity and attribution visible. Do not silently rewrite the canonical Source record in this screening checkpoint.

## Rights and attribution

USGS states that USGS-authored or produced information is generally in the U.S. public domain and requests attribution, while warning that some third-party images, illustrations, and other materials on its pages may remain copyrighted. This candidate uses a short factual paraphrase and a text-only dictionary entry; no third-party media is proposed. The intended display should credit the U.S. Geological Survey and link to the exact term. This is a preliminary rights assessment, not legal advice or a repository-wide license decision.

Rights guidance: `https://www.usgs.gov/faqs/are-usgs-reportspublications-copyrighted`

## Gate results

| Gate | Decision | Reason |
|---|---|---|
| Canonical identity and revision | PASS for screening | Exact Claim/EU/Source set identified at the stated main SHA |
| Claim-specific source fit | PROVISIONAL PASS | USGS definition directly supports the Claim's core |
| Exact Evidence Use pinpoint | HOLD | Canonical Evidence Use has no term-level locator |
| Source link and attribution in reader | HOLD | Must be rendered and inspected in the actual preview |
| Rights for proposed text | PROVISIONAL PASS | Factual paraphrase of USGS entry; credit USGS; no media proposed |
| Human View / readability | NOT RUN | No real-record artifact has been built and inspected |
| Exact-version allowlist and reproducible hashes | NOT CREATED | No candidate is approved |
| Editorial approval | NOT RECORDED | Named owner decision is still required |

## Decision

- This is a stronger *next candidate to remediate* than a multi-Claim slice because the proposition is narrow and the source definition is direct.
- Current decision remains **HOLD**, not pilot-approved.
- Do not add it to the reader allowlist or change canonical JSON until the exact evidence locator, rendered navigation, Human View, and editorial approval are recorded.
- Keep the synthetic preview fixture as the only runnable preview input until that gate is closed.
