# PR #22 Status and Work Package 1 Handoff — Updated 2026-11-19

- **Agent:** chief-engineer
- **Task:** Continue the approved first-edition Work Package 1 from the existing Part II reconciliation point without repeating completed audits.
- **Repository:** `kvantovoebessmertie/encyclopedia-of-civilization`
- **Branch:** `mvp-public-contribution-design-2026-10-11`
- **Snapshot HEAD:** `6bbec38c0c3e262d332ef9c30a1798af500d6573`
- **PR state:** OPEN · DRAFT
- **Snapshot:** 487 changed files · 930 commits
- **Acceptance:** CONDITIONAL — corpus selection and screening advanced; dependency closure, rights/editorial approvals, Human View and final exact-head CI remain open.

## 1. Non-negotiable controls

- Do not modify `main`, merge PR #22, publish, or create a public allowlist/preview.
- Do not repeat completed Part I audits or previously closed domain audits.
- Do not start M13 batches as a substitute for the first-edition work plan.
- Do not promote HOLD automatically. Every disposition requires claim-level evidence, source-rights review, scope boundaries and editorial approval.
- Preserve canonical record IDs. Resolve malformed register references against canonical JSON; never silently rename a canonical record.

## 2. Verified completed work

### Part I — survival
- 94/94 slices reconciled.
- 980/980 canonical JSON records checked.
- No remaining Part I slice is verified only by filename.

### Part II — exact-version candidate register
- Ten domain addenda consolidated with the base candidate register.
- 621 exact-version rows from ten addenda.
- 197 raw base-register Part II references mapped to 37 slices; after correcting the duplicated water-quality alias, 196 distinct base canonical keys remain.
- Nine exact-version overlaps between the base register and addenda are represented once.
- Thirteen current `international-law-basics@2` records were added after version-drift review; their v1 rows remain historical and v2 remains HOLD pending substantive re-review.
- Batch 1 added 89 exact-version records from nine new structural-map slices.
- **Current master: 910 unique exact-version keys across 108/385 Part II slices.**
- **277 Part II slices remain unregistered.** They are not automatically release candidates.

### Cross-slice Relations
- All 63 canonical Relation record paths inventoried separately from the vertical-slice denominator.
- 126 declared participant references recorded.
- 29 participant references into the Part II candidate set (25 unique Claims) were verified against canonical JSON at the pinned relation-endpoint verification HEAD.
- The other 97 participant references point outside the current candidate set; their paths resolve, but exact participant version/type and semantic validity remain open.

### Structural scope triage
- The controlling Part II domain map names 69 structural examples.
- 37 were already represented in Part II candidates.
- 7 are already covered by the completed Part I inventory and must be reused, not re-audited.
- 25 were initially absent from both candidate registers (235 canonical JSON records).
- Batch 1 screened 9 of those slices / 89 records; 16 explicit map examples / 146 records remain unrepresented.
- The other 261 unregistered slices are not explicitly named by the current map examples. They remain an untriaged backlog; no blanket sweep is authorized.

### Batch 1 — foundations and natural sciences
Nine slices and 89 canonical JSON records were fetched, parsed and screened at `62c75dc7468e7b6d388eb99d39701019dd898248`. A tree comparison confirms all 89 record-file blob SHAs remain unchanged at the current branch snapshot. All nine received reasoned HOLD recommendations:
- ratios-and-percentages
- probability-basics
- algebra-basics
- matter-basics
- acid-base-basics
- analytical-chemistry-basics
- earth-system-basics
- oceanography-basics
- astronomy-observation-basics

Principal blockers: generic Evidence Use without claim-specific pinpoints; Source-to-Claim misalignment in ratios/probability; a Source URI/section mismatch in acid-base; inadequate direct evidence for parts of analytical chemistry, Earth-system science and observational astronomy; and three editorial placeholder Claims in oceanography. OpenStax noncommercial/share-alike and LLM-ingestion restrictions, IUPAC terms, and NIST/NASA/NOAA reuse conditions remain subject to item-specific rights review. No canonical JSON was changed.

## 3. Current master and durable reports

- `RELEASE/FIRST-EDITION-PART-II-EXACT-VERSION-MASTER-REGISTER-2026-11-19.md` — 910 unique exact-version keys; Batch 1 rows added; water-quality alias duplicate removed.
- `RELEASE/FIRST-EDITION-PART-II-INVENTORY-RECONCILIATION-2026-11-19.md` — 108/385 represented; 277 unregistered; nine Batch 1 slices removed from the unregistered list.
- `RELEASE/FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY-2026-11-19.md` — 63 Relations / 126 participant references; candidate endpoint checks recorded.
- `RELEASE/FIRST-EDITION-PART-II-STRUCTURAL-GAP-TRIAGE-2026-11-19.md` — initial map-gap inventory and post-Batch 1 status.
- `RELEASE/FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md` — nine-slice substantive screen and preliminary rights findings.
- `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-FULL-SLICE-INVENTORY-2026-11-18.md` — completed Part I evidence.
- `RELEASE/ENGINEERING-COMPUTING-REMEDIATION-ADDENDUM-2026-11-19.md` and `RELEASE/ENGINEERING-COMPUTING-RIGHTS-AND-ATTRIBUTION-SCREEN-2026-11-19.md` — eight-slice/72-record remediation remains HOLD.

## 4. Next bounded actions

1. **Continue Batch 2 only:** cybersecurity-basics, psychology-basics, neuroscience-basics, learning-basics, developmental-biology-basics and economics-basics (6 slices / 54 canonical JSON records). First check for any pre-existing domain work and current exact versions; do not assume standard filenames or versions.
2. Re-read the 197 raw base-register references at one frozen HEAD; verify canonical `record_id`, `record_version` and type. Retain the corrected water-quality canonical identity once.
3. Complete Claim → exact Evidence Use → exact Source dependency closure across all 910 keys; verify Context/Scope target coverage and applicability.
4. Re-review the 13 current `international-law-basics@2` records as one coherent dependency unit; preserve v1 as historical HOLD.
5. Finish exact participant version/type and semantic review for the 97 non-candidate Relation endpoints. Do not add Relations to the 910-record vertical-slice denominator.
6. Close source-specific rights, project-level licence/distribution policy, accountable editorial ownership, independent editorial review, Human View and consequence review.
7. Only after the corpus and all dependencies are frozen, prepare a record-exact allowlist and run the final release gates on one immutable HEAD.

## 5. CI snapshot and release gate

- The latest workflow snapshot available for commit `9dd42f9088125410fde47aebf314812c08c1cf79` was:
  - Offline Edition: **SUCCESS**
  - Reference implementation tests: **CANCELLED**
  - Release Conformance Gate: **CANCELLED**
  - MVP Contribution Form Browser Tests: **CANCELLED**
- No workflow runs were returned for the current docs-only snapshot HEAD `6bbec38c0c3e262d332ef9c30a1798af500d6573`.
- Therefore **there is no final exact-HEAD PASS**. Re-run all required gates on the eventual content-bearing final HEAD; do not infer PASS from an earlier commit.

## 6. Not done / not approved

- No canonical content was changed during the register, relation, scope-triage or Batch 1 report work.
- No HOLD was promoted to INCLUDE.
- No EXCLUDE decision, public allowlist, release preview or release packet was created.
- No legal clearance, editorial sign-off, Human View approval or publication authorization was obtained.
- PR #22 remains Draft; `main` remains untouched.

## 7. Handoff

**Next owner/action:** Chief Engineer — execute Batch 2 as a bounded 6-slice / 54-record screen, while parallel work continues on the 197 base-reference revalidation and the 910-key dependency closure. Do not repeat Batch 1 or closed Part I/engineering audits.

PR: https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
