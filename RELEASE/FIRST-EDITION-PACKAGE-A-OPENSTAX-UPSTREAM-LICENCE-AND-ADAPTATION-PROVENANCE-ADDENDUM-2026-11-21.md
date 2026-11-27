# Package A — upstream licence and adaptation provenance verification addendum

Date: 2026-11-21  
Scope: research-only follow-up to `FIRST-EDITION-PACKAGE-A-ANCIENT-CIVILIZATIONS-ALTERNATIVE-SOURCES-AND-RIGHTS-RESEARCH-2026-11-21.md`.

## 1. Purpose and boundary

This addendum verifies the upstream OpenStax source-version licence claim and tightens the remaining provenance limits for the Open Book Project adaptation. It does not authorize or perform canonical edits, source registration, Evidence Use versioning, Claim changes, INCLUDE/HOLD decisions, master-register or allowlist changes, or publication work.

## 2. Upstream OpenStax source version — licence evidence confirmed

The Open Book Project identifies its source version as `openstax/osbooks-world-history` commit `3e17beda91`.

GitHub resolves that abbreviated identifier to:

- Repository: https://github.com/openstax/osbooks-world-history
- Full commit: `3e17beda9130380d24be881e6d1942dfcc1be845`
- Commit date: 2025-12-05
- Commit message: `Add missing captions`
- Commit signature: GitHub reports the commit as unsigned / unverified.

At that exact commit:

- `README.md` states that *World History Volume 1, to 1500* and *World History Volume 2, from 1400* are available under the Creative Commons Attribution License and links to the repository's `LICENSE`.
- `LICENSE` is the full Creative Commons Attribution 4.0 International Public License text.
- The licence file is part of the repository tree at the identified commit.

Direct, immutable references:

- Commit: https://github.com/openstax/osbooks-world-history/commit/3e17beda9130380d24be881e6d1942dfcc1be845
- README at commit: https://github.com/openstax/osbooks-world-history/blob/3e17beda9130380d24be881e6d1942dfcc1be845/README.md
- LICENSE at commit: https://github.com/openstax/osbooks-world-history/blob/3e17beda9130380d24be881e6d1942dfcc1be845/LICENSE

**Finding:** the upstream OpenStax source version named by the Open Book Project is demonstrably labelled CC BY 4.0 in the source repository at that exact commit. This confirms the narrow upstream-version assertion; it does not independently prove every later adaptation step or clear third-party components.

## 3. Open Book Project adaptation — what is independently visible

The published book overview says the adaptation:

- is adapted from OpenStax *World History, Volume 1, to 1500*;
- is licensed under CC BY 4.0;
- was made from the OpenStax source version at commit `3e17beda91`;
- changed the presentation into the Open Book Project web-reading format, reorganized chapter reviews, and resized figures;
- retains figure credits in captions and says credited photographs/illustrations remain under their stated terms;
- does not use OpenStax name, logo or covers beyond the attribution and states OpenStax does not endorse the adaptation.

The book's preface repeats the CC BY 4.0 statement and describes art-attribution practice. The published pages carry the footer “© The authors of the books.”

References:

- Book overview and adaptation statement: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/index.html
- Preface, “Customization” and “Art attribution”: https://open-book-project.github.io/textbooks/social-science-textbooks/world_history_1/preface.html
- Public reading-site repository: https://github.com/open-book-project/textbooks

The public GitHub repository `open-book-project/textbooks` describes itself as “Reading site (built pages only)”; its visible repository metadata does not identify a repository-level licence. Its deployment history shows commits titled “Deployed with tools/publish.py”. Therefore this repository is evidence of the published rendering, not by itself the complete editable source history or a full provenance record for the adaptation.

## 4. Residual provenance and rights questions

The following remain unverified by the public materials inspected:

1. The identity of the adapter(s) who prepared the web adaptation and the precise scope of their own CC BY 4.0 grant.
2. The complete source repository / build inputs and change history for the adaptation, rather than the generated reading-site pages.
3. Whether every textual, tabular, map, image and other embedded component is covered by the upstream CC BY 4.0 grant or has a separate rights holder and licence.
4. Whether each third-party image or illustration is actually required for the proposed Encyclopedia use and, if so, its own caption-level licence and attribution requirements.
5. Whether the intended Encyclopedia distribution and any AI/data processing comply with all relevant licence conditions and applicable law.

The preface's art-attribution section says artwork has caption attribution and licence information and describes a default assumption for artwork without licensing information. This is not a reason to ingest or republish images with unclear provenance. The conservative route remains: do not copy images, figures, maps, tables or textbook prose into the Encyclopedia; use independently authored factual statements with precise citations, subject to editorial and legal review.

## 5. Updated Package A rights disposition

| Layer | Result | Status |
|---|---|---|
| OpenStax upstream commit `3e17beda9130380d24be881e6d1942dfcc1be845` | README and LICENSE at exact commit identify CC BY 4.0 | Confirmed at repository-file level |
| Open Book Project published adaptation | Book overview and preface expressly state CC BY 4.0 and identify upstream commit | Public licence assertion found; adapter authority / complete provenance not independently closed |
| Generated reading-site repository | Described as built pages only; repository metadata has no licence identifier | Not sufficient as the sole rights-chain record |
| Third-party images / figures | Captions reportedly preserve credits and separate terms | Must be excluded unless individually cleared |
| Encyclopedia incorporation | No copying or canonical source registration performed | Not authorized by this research-only scope |

**Decision recommendation:** keep the Open Book Project edition as the leading candidate for a locator-only, citation-based research route for Claims A–C, but do not treat this review as legal clearance to reproduce or ingest the adaptation. The most defensible immediate use remains citation to exact chapter/section locators and independent authoring of Encyclopedia wording. Any copying, translation, figure reuse, bulk extraction, or AI ingestion requires a separate rights assessment.

## 6. Repository execution boundary

This addendum is research documentation only. No canonical JSON, Claim, Evidence Use, Source, Context, Scope, Relation, master register, candidate denominator, allowlist, release manifest, preview, publication status, or `main` content is changed. The Ancient Civilizations slice remains HOLD. A separate explicit authorization is still required before any canonical @2 implementation.
