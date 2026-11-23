# First Edition — Priority Closure Board

Updated: 2026-11-19  
PR #22: mvp-public-contribution-design-2026-10-11  
Current status: OPEN / DRAFT / NOT MERGED

This board is the execution index for the remaining first-edition blockers. It distinguishes completed audits from owner decisions and canonical changes that still require bounded authorization.

## P0 — Relation graph and semantic closure

| Work item | Status | Closure evidence / next action |
|---|---|---|
| Inventory all cross-slice Relations | DONE | 63/63 inventoried |
| Exact participant identity/version/type | DONE | 126/126 participant references verified; includes 97 non-candidate refs / 82 unique Records |
| Relation-pair semantic review | DONE | 63/63 reviewed; 48 contextual-navigation candidates; 15 semantic HOLD |
| Non-candidate endpoint pair review | DONE | All 97 references and 82 unique endpoint Records considered in the 63 Relation reviews; standalone Claim/EU/source quality remains separate |
| Shared Context applicability | IMPLEMENTED — VALIDATION PENDING | Owner approved Option A on 2026-11-20. 61 target-specific Context records created; 61 Relations versioned and redirected. Shared Context retained only for REL-CROSS-WATER-CHEMICAL; water-storage local Context retained. Regression test added. See RELATION-CONTEXT-ISOLATION implementation report |
| Earthquake Event | OWNER DECISION RECORDED — HOLD / EXCLUDE | E-Q1 selected 2026-11-20: preserve Event @1 and aftershock Relation @2 unchanged and HOLD; exclude both from first-edition release scope absent a source for a specific occurrence |
| Container/water State Relation | OWNER DECISION RECORDED — HOLD / EXCLUDE | W-Q3 selected 2026-11-20: preserve Object, both States, Relation @1 and Context @1 unchanged; keep Relation HOLD and exclude it from first-edition release scope pending a valid model |
| 15 semantic HOLD Relations | REMEDIATION PLANS READY | Individual reason and repair route recorded. Two high-confidence alternative endpoints identified; evidence locator and authorization gaps remain |

Key documents:
- FIRST-EDITION-RELATION-SEMANTIC-REVIEW-BATCH1–9
- FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY
- FIRST-EDITION-RELATION-ARCHITECTURE-REMEDIATION-DECISION-PACKAGE
- FIRST-EDITION-RELATION-SEMANTIC-HOLD-REMEDIATION-REGISTER
- FIRST-EDITION-RELATION-CONTEXT-APPLICABILITY-AUDIT
- FIRST-EDITION-RELATION-FRAME-CONTEXT-CONFORMANCE-AUDIT
- FIRST-EDITION-WATER-STORAGE-STATE-RELATION-CONTEXT-CONFORMANCE-AUDIT

## P1 — Work Package 2: rights and editorial responsibility

| Work item | Status | Closure evidence / next action |
|---|---|---|
| Source-specific rights screens | SCREENED — NOT CLEARED | 50 table entries, 47 distinct slices across six screens; all retain HOLD |
| Project content/data licence | OPEN — OWNER DECISION R-02 | Select exact licence/version and coverage only after rights holder/authority is established |
| Software licence | OPEN — OWNER DECISION R-03 | Keep separate from content/data licence |
| Contributor terms | OPEN — OWNER DECISION R-04 | Define grant, attribution, warranties, third-party content, disputes and withdrawal |
| Source reuse policy | OPEN — OWNER DECISION R-05 | Separate paraphrase, quotation, image, table, dataset and derivative rules |
| Rights holder | OPEN — OWNER DECISION R-01 | Name legal person/entity or document ownership authority |
| Editor / release approver / correction contact | OPEN — OWNER DECISIONS R-06–R-09 | Name accountable roles and monitored contact; define correction/dispute/withdrawal |
| Rights evidence register | OPEN — OWNER DECISION R-10 | Versioned item-level rights record, territory, term, restrictions and evidence |

Key documents:
- FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS
- FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER
- Six source-specific rights and attribution screens

## P2 — Work Package 3: build and CI

Current latest PR head at board creation: bf1c5a69281aa87dab60686542d7eb920b6b721d.

Latest exact-head Actions state at inspection:
- Reference implementation tests — pending
- Offline Edition — in progress
- Release Conformance Gate — pending
- MVP Contribution Form Browser Tests — queued

No exact-head CI PASS is claimed. Recheck after runs complete and after any subsequent commit.

## Safety and change-control boundaries

- PR #22 remains Draft and unmerged; main is unchanged.
- All 15 semantic HOLD Relations and all screened candidate slices remain HOLD.
- No licence, rights holder, editor, release approver or public contact is invented.
- No canonical JSON, allowlist, or publication decision is changed without a matching bounded authorization.
- No Relation or Claim is automatically promoted to INCLUDE.
- Documentation and audit completion do not equal release approval.

## Next execution sequence

1. DONE: owner approved per-Relation Context strategy (Option A) on 2026-11-20; 61 Contexts and 61 Relation frame updates implemented. Exact-head CI validation is pending.
2. DONE: owner selected E-Q1 and W-Q3 on 2026-11-20; both model groups remain unchanged, Relations remain HOLD, and the specified items are excluded from first-edition release scope.
3. Resolve the exact-head CI failures recorded at `47f65a506bd13eaa913ba7ce1414c67e11d3714a`; rerun all four workflows on one immutable HEAD.
4. Execute the ready semantic endpoint substitutions only after exact Evidence Use and rights checks; Library/Archival alignment is implemented, while Emergency/Infrastructure still requires separate authorization.
5. Resolve Research Methods Evidence Use locators and obtain separate authorization before changing the Research/Statistics Relation.
6. Close R-01–R-10 with authorized owner decisions; continue item-level rights verification.


## Execution checkpoint — 2026-11-19, after Batch 2 and exact-head CI

- Batch 2 is complete: 5/5 explicit map-gap slices and 47/47 records screened; all five remain HOLD. The five slices are not pending screens.
- The 47 Batch 2 canonical JSON blob SHAs were compared between the Batch 2 inspection commit `c4fbc8d1d879ae0c14e2b0ceaba8899d4f6fef0d` and the then-current PR HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`: 47/47 unchanged.
- The exact-version master already contains all 47 Batch 2 rows: 1,119 unique exact-version rows (1,058 candidate + 61 dependency), 124/385 Part II slices represented, 261 not yet registered. The 261 unlisted slices remain outside the bounded first-edition map screen; no blanket audit is authorized.
- Added `FIRST-EDITION-BATCH2-EVIDENCE-REMEDIATION-RESEARCH-2026-11-19.md`: source/locator remediation plan for ancient civilizations, anthropology, linguistics, philosophy and ethics. It proposes Claim concepts and precise source locators but makes no canonical changes or decision changes. The report explicitly corrects the OpenStax Anthropology live licence to CC BY-NC-SA 4.0 and records the cloned-source limitation of the Linguistics OER.
- At HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`, all four exact-head CI workflows passed: Reference Tests (1,003 passed), Release Conformance Gate (CONFORMING; 0 blocking conditions in the checked scope), Offline Edition and Browser Tests. The later commits in this checkpoint are documentation-only; their exact-head CI must be checked separately.
- Owner decisions and canonical authorization remain required before any Batch 2 Claim/Source/Evidence Use correction. No Batch 2 slice is promoted; no allowlist created.

### Updated next actions

1. Obtain owner/editorial authorization for the Batch 2 record-level remediation scopes before changing any of the five slices.
2. Shared Relation Context strategy implemented under owner approval; separately resolve the earthquake Event and container/water State model.
3. Continue only bounded exact-version and dependency closure work that can be completed without re-adjudicating closed screens; do not expand to the 261 map-external slices without scope approval.
4. Close WP2 owner decisions R-01–R-10 and item-level rights decisions; none may be invented by the implementation team.
5. Re-run exact-head CI after any canonical or release-document changes; technical PASS does not confer publication approval.


### Additional WP2 consolidation and corpus integrity — 2026-11-19

- Batch 2 rights/attribution screening is now included in the consolidated WP2 status: seven source-specific screens, 55 table entries, 52 distinct slices (three repeated R9 rows removed). All screened slices remain HOLD; R-01–R-10 remain OPEN.
- The rights consolidation explicitly distinguishes the live OpenStax *Introduction to Anthropology* CC BY-NC-SA 4.0 notice from a separate UOT adaptation's CC BY 4.0 statement; it also records the OpenStax-derived Philosophy edition pin and the cloned-source provenance limitation of *Essentials of Linguistics*.
- Rights owner decision register updated to match the seven-screen / 52-distinct-slice consolidation. No owner decision was invented or closed.
- A whole-`CONTENT/` Git tree comparison between the last fully green CI HEAD `48c78389fb5345223627a687b22d51ee260b9d7d` and current documentation HEAD `a6616c84a2edc20b36177d80773377164bf0e1de` found 5,163 Content files, including 4,680 canonical record JSON files, with **zero changed Content blobs**. `RELEASE/EDITORIAL-CORRECTION.json` is also unchanged. The new commits are documentation-only.
- Exact-head CI on `a6616c84a2edc20b36177d80773377164bf0e1de` has been triggered. Offline Edition has completed preflight, record identity validation, offline tests, full build and manifest verification in one run; artifact upload is still in progress. Browser, Reference Tests and Release Gate have started; final conclusions are not yet available.


## Execution checkpoint — International Law v2 re-review — 2026-11-19

- Completed a bounded re-fetch and substantive dependency review of the 13 current `international-law-basics@2` records at PR HEAD `50d37a3da7c66fc383783d21cf3fd08d9aa6038f`.
- 13/13 exact IDs, versions and record types match; 9/9 Claim→EU→Source edges resolve to exact versions.
- The primary UN Charter locators were checked against the official full text. The ICRC Handbook locator was checked against the official PDF: §2.1.0.1 and §2.1.0.3 are on printed p. 45; §§2.1.0.5–2.1.0.6 are on printed p. 46.
- Findings: Claim B should be narrowed to principles governing the UN Organization and its Members; Claim C should preserve the UN Member boundary. Independent EU B is partial treaty-definition context and does not itself identify the UN Charter; independent EU C's source locator does not support Claim C's principles. The current Evidence Use Standard allows only `supports` / `contradicts`; no third “context” role is proposed.
- Context and Scope both target Claim A v2; no transfer to Claims B/C is inferred.
- New report: `FIRST-EDITION-INTERNATIONAL-LAW-V2-SUBSTANTIVE-DEPENDENCY-REREVIEW-2026-11-19.md`. Version-drift report and exact-version master register updated accordingly.
- All 13 v2 records remain HOLD. No canonical JSON, record version, Relation, allowlist or publication state changed. Remediation requires bounded authorization; source rights and qualified legal/editorial review remain open.
- This work closes the old “13 v2 pending substantive re-review” task. It does not close the underlying evidence-fit remediation or any WP2 rights decision.


## Execution checkpoint — Batch 9 locator research — 2026-11-19

- Researched all five unpinned Batch 9 EUs against official sources: Settlement Geography A/B/C, AMR C, Statistics C.
- Direct locator candidates identified for 5/5. Settlement Geography: six-partner 2021 Degree of Urbanisation manual, §§6.1–6.3 and Chapter 1; manual's CC BY-NC-SA 3.0 IGO terms and joint-publisher identity recorded. AMR: WHO fact sheet (updated 16 July 2026), Overview / A global concern / WHO response. Statistics: NIST/SEMATECH handbook §4.3.1.
- Statistics Claim wording may need narrowing; settlement Source identity/URI needs correction; rights checks remain open.
- Research report: `FIRST-EDITION-BATCH9-UNPINNED-EVIDENCE-LOCATOR-RESEARCH-2026-11-19.md`. Batch 9 audit report and exact-version master register updated.
- This closes locator discovery only. All affected records remain HOLD; no canonical JSON or version changed. Exact bounded authorization is required before applying any locator, Source metadata or Claim wording edits.


## Execution checkpoint — exact-version master count reconciliation — 2026-11-19

- Audited the exact-version table rather than relying on the Batch 9 narrative total.
- At PR HEAD `c209b90fbe542eeff08f46e6598ac1666b8dbaaa`, the table had 1,113 rows. Six dependency rows were subsequently added and verified: two missing Evidence Use records (AMR C and Statistics C) plus Context/Scope pairs for those two slices.
- All six canonical records were re-fetched at HEAD `4283b65031fe5d578aa4f92242b98b14fc392c94`; exact ID/version/type matches. The Context/Scope records target Claim A only; no applicability to Claim C is inferred.
- Current master: **1,119 unique exact-version rows = 1,058 candidate keys + 61 dependency records**. Master register and Batch 9 report now record the corrected count and provenance.
- No canonical content, disposition or release state changed. All six remain HOLD.


## Execution checkpoint — Batch 8 evidence/Claim remediation research — 2026-11-19

- Researched all 15 Batch 8 EUs and Claims across five slices; direct locator candidates identified for 15/15.
- Electromagnetism and Fluid Mechanics: three substantive Claim replacement proposals each, pinned to OpenStax §§13.1–13.3 and §§14.5–14.7 respectively. These replace six generic editorial placeholders if approved.
- Geometry: suitable OpenStax Contemporary Mathematics source and exact sections found; current Source identity/URL mismatch and Claim C wording issue recorded.
- Governance: OECD exact sections and printed pages located; Claim C needs narrower scope wording.
- Historical Geography: LOC map-analysis guide provides direct passages for map-as-source, map content, and date/scale/source/purpose interpretation; use beyond classroom and map-item rights require review.
- Research dossier: `FIRST-EDITION-BATCH8-EVIDENCE-AND-CLAIM-REMEDIATION-RESEARCH-2026-11-19.md`. Batch 8 report and master register updated.
- This is research closure only. No canonical JSON changed; all 15 Claims remain HOLD. OpenStax CC BY-NC-SA/AI-ingestion restrictions, OECD terms and LOC rights remain unresolved. No canonical edit is authorized.


## Execution checkpoint — Batch 7 locator and source-fit research — 2026-11-19

- Researched all six previously unpinned Batch 7 EUs.
- Cultural Anthropology A/B/C: exact AAA *Perspectives: An Open Introduction to Cultural Anthropology*, 2nd ed. passages found; Claim B should be narrowed to match the four-field model. CC BY-NC 4.0, non-commercial only.
- Education Systems A: direct UNESCO right-to-education opening locator found. B: direct 4A obligations locator found on the UNESCO state-obligations subpage. C: current single source is insufficient for the broad cross-country claim; recommended either narrow to UNESCO's country-tailored education-system review method or authorize additional comparative UNESCO/OECD evidence chains.
- Research dossier: `FIRST-EDITION-BATCH7-UNPINNED-EVIDENCE-AND-SOURCE-FIT-RESEARCH-2026-11-19.md`. Batch 7 report and master register updated.
- No canonical JSON changed; all 15 Claims remain HOLD. Rights and independent editorial review remain open.


## Final session checkpoint — PR #22 state and CI provenance — 2026-11-19

- PR #22 remains OPEN / DRAFT / NOT MERGED. Current branch HEAD at this checkpoint: `5977125fa76bc48ae6b59b0e6d247507d140d6be`.
- Compared with the last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`, the PR is 27 commits ahead. The complete compare shows 13 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs were returned for the current documentation-only HEAD. Do not claim a new exact-head CI PASS. The four successful checks remain tied to HEAD `48c78389`; rerun after any authorized canonical changes and on the final immutable release HEAD.
- This session made documentation/research changes only. No canonical JSON, Relation, allowlist, preview, publication state or merge operation was changed.


## Execution checkpoint — Batch 1 / Batch 3 current-head evidence and dependency follow-up — 2026-11-19

- Re-fetched the non-overlapping Batch 1 candidate chains and the Batch 3 base chains from the current PR branch. Batch 2 and Batch 7–9 source work was not repeated.
- Batch 1 historical scope: 19 Claims / 15 slices. Five one-Claim slices overlap with Batch 2 and were not re-researched. The remaining 14 historical Claims across ten slices received claim-specific source/locator research. The current branch also contains 16 additional v1 Claims in eight of those slices that were not part of the historical Batch 1 denominator; they were researched for source/locator routes but remain outside the candidate master pending scope triage.
- Batch 3 historical scope: 11 Claims. The two SI Evidence Use records were already versioned to v2 under the existing bounded authorization and now contain exact NIST “Defining Constants” / “Base and Derived Units” references. The remaining nine Claims across soil microbiology, soil science, statistics, thermodynamics and water-resource management received direct locator/source-fit research.
- Six additional P9 Evidence Use records (Marine Biology A–C and Pathology A–C) were re-fetched and source-fit reviewed. NOAA “What is ecosystem science?” is partial for Marine A/C and does not support the food-web Claim B; a direct NOAA aquatic-food-web source is recommended. The NCBI Bookshelf item attached to Pathology is actually a Molecular Biology of the Cell chapter, not a general pathology source; it is inadequate for broad independent support of all three Claims.
- Measurement Uncertainty contains an additional BIPM/JCGM VIM Source/EU pair for Claim B. VIM 2.26 directly supports the formal uncertainty definition; the EU was missing a pinpoint locator.
- Ten exact dependency records absent from the 1,119-row master were verified and added: six P9 EUs, two P9 Sources, and the BIPM EU/Source pair. Updated exact-version total: **1,129 = 1,058 candidate keys + 71 dependency records**. Candidate denominator remains 1,058; Part II slice coverage remains 124/385.
- Twenty-one additional v1 Claims across 11 slices were found in current CONTENT but are absent from the candidate-key master. They remain outside the first-edition candidate denominator until explicit scope triage; see the follow-up dossier.
- New research dossier: `FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md`. Exact-version master register reconciled with ten additional dependencies.
- All affected Claims and slices remain HOLD. No canonical JSON, Relation, allowlist, publication state or release decision changed.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22: OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `b88cb6a350b65dd907c9daf749a48edcd730ea15`, 32 commits ahead of the last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Full compare: 15 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for this exact documentation-only HEAD. Do not claim a new exact-head CI PASS. The 4/4 PASS remains tied to `48c78389`.
- `main` remains untouched by this work. No merge, deployment or release approval was performed.

### Next execution sequence

1. Continue the Batch 4–6 gap/source-fit review against current authorization state; skip slices already covered by active bounded authorizations or existing research dossiers.
2. Reconcile any newly discovered exact dependency records into the master without expanding the candidate denominator by inference.
3. Prepare bounded implementation packets for locator-only changes that are well supported; keep Claim replacements, Source-graph expansions and rights-sensitive work separated for owner/editor decisions.
4. Resolve the 21 current-slice Claims outside the master through explicit first-edition scope triage; do not silently add them.
5. Keep R-01–R-10, rights, independent editorial review and Human View open; rerun all release gates only after authorized canonical changes on a frozen final HEAD.


## Execution checkpoint — Batch 4–6 residual locator and Claim remediation research — 2026-11-19

- Re-read the Batch 4, 5 and 6 dependency-closure reports and checked the live bounded authorizations in `RELEASE/EDITORIAL-CORRECTION.json`. Skipped slices already covered by chemistry, engineering/computing, legal/trade/institutional, R7 and R9 scopes; no authorization was broadened.
- Completed the residual six-slice review: accounting-basics, calculus-basics, climate-science-basics, computer-networks-basics, democratic-institutions-basics and demography-basics.
- Twelve substantive Claims have direct locator candidates: Accounting A–C (with A/C narrowing proposals), Calculus A–C, Democratic Institutions A–C and Demography A–C. Climate Science and Computer Networks each contain three generic editorial placeholders; six source-bounded replacement Claim proposals and direct source paths were prepared instead of treating the placeholders as factual Claims.
- IFRS Conceptual Framework locator map recorded with the boundary that it is not a complete bookkeeping manual; OpenStax Calculus Volume 1 sections 2.2, 3.2, 5.2 and 5.3 identified; International IDEA GSoD methodology v10 (2026) mapped to democratic-institution Claims; UN WPP 2024 Summary of Results p.9 and methodology mapped to demography Claims.
- Climate-science replacement route uses NASA Evidence, Causes and Effects pages. Computer-network replacement route uses NIST CSRC glossary entries “network” and “protocol” plus IETF RFC 1122 for layered Internet architecture. New Source/EU IDs are not invented; graph expansion awaits canonical ID allocation and owner approval.
- New dossier: `FIRST-EDITION-BATCH4-6-RESIDUAL-LOCATOR-AND-CLAIM-REMEDIATION-RESEARCH-2026-11-19.md`.
- No canonical JSON changed. No new dependency records were discovered in this six-slice residual pass. All six slices remain HOLD; IFRS/OpenStax/IDEA/UN rights review and all independent editorial/Human View gates remain open.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `3ee2f50792fe8a9b8d568c47a62c0dcaddbaabbc`, 34 commits ahead of green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 16 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for this exact documentation-only HEAD. The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed.
- The master register remains 1,129 exact-version rows = 1,058 candidate keys + 71 dependency records. Part II slice coverage remains 124/385. The 21 extra current Claims remain outside the candidate denominator pending explicit scope triage.

### Next execution sequence

1. Extract the next 15 not-yet-audited candidate Claims from the exact-version master using the same frozen-HEAD and no-duplicate selection rules as Batches 1–9; do not select any slice already covered by active bounded authorizations or a completed research dossier unless a new dependency/version change requires it.
2. Re-fetch exact Claim→EU→Source chains and source locators, then produce the next bounded research batch with direct support boundaries and rights notes.
3. Continue the 21-Claim scope triage separately; do not silently expand the 1,058 candidate-key denominator.
4. After owner approval, implement only explicitly authorized locator-only changes first; keep substantive Claim replacements and source-graph expansions separate.
5. Preserve HOLD and run affected tests/full release gates only after authorized canonical edits on a frozen final HEAD.


## Execution checkpoint — Batch 10, six-slice current-head review — 2026-11-19

- Completed the next candidate batch using the exact-version master as the scope authority: **20 Claims / 24 EUs / 9 Sources across six slices** — agricultural-engineering-basics, agrifood-systems-basics, ecophysiology-basics, food-distribution-basics, infrastructure-resilience-basics and magnetism-basics.
- Direct source/locator routes recorded for all 20 Claims. Material source-fit issues remain: Agricultural Engineering's FAO land/water Source is too narrow for the full discipline; Ecophysiology's current OpenStax URI is mismatched; Food Distribution's WFP URI points to an infographic rather than the Supply Chain page; Infrastructure Resilience's FEMA page was inaccessible (HTTP 403), while NIST SP 1190 Volumes I/II provide direct alternative support; Magnetism C needs a narrower force proposition.
- Agrifood includes a real independent World Bank EU; its URI should be corrected to the “About Us” page for direct system-level corroboration.
- All 53 exact record keys (20 Claims, 24 EUs, 9 Sources) are present in the exact-version master. No new dependency rows were needed; total remains **1,129 = 1,058 candidate keys + 71 dependencies**. Slice coverage remains 124/385.
- A preliminary extraction check incorrectly flagged Agricultural Engineering records as absent; direct row inspection of the exact-version master confirmed the three Claims, three EUs and Source are present. The Batch 10 report, Batch 1/3 follow-up and master note were corrected. The known out-of-master count remains **21 Claims across 11 slices**, not 24. No candidate denominator change was made.
- Batch 10 dossier: `FIRST-EDITION-BATCH10-EVIDENCE-LOCATOR-AND-SOURCE-FIT-RESEARCH-2026-11-19.md`. All six slices remain HOLD; no canonical JSON changed.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `d564ef01b256093e47bc8a00f8623cb307a5d495`, 41 commits ahead of green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 17 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for this exact documentation-only HEAD. The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed.
- `main` remains untouched. No merge, deployment or release approval was performed.

### Next execution sequence

1. Continue with the next 15 candidate Claims selected from unreviewed slices in the exact-version master; do not include out-of-master records or repeat any prior batch/authorization scope.
2. Re-fetch exact Claim→EU→Source chains and perform direct locator/source-fit checks, then update the master only if a genuinely missing exact dependency row is verified.
3. Prepare bounded implementation packets for locator-only work; keep source-graph expansion and Claim replacements separate for owner/editor approval.
4. Continue the 21 known out-of-master Claim scope triage separately; do not silently add them to the candidate denominator.
5. Preserve HOLD and rerun affected tests/full release gates only after authorized canonical edits on a frozen final HEAD.


## Execution checkpoint — Batch 11–12 completion — 2026-11-19

- Batch 11 completed: 15 Claims / 15 EUs across astronomy-observation, matter, optics, temperature and waves/sound. All records are present in the exact-version master. Key findings: Optics Source points to a waves chapter rather than optics; Astronomy needs direct NASA spectrum/telescope sources; Matter and Temperature have direct section-level locators; Waves/Sound requires exact book/section alignment.
- Batch 12 completed: 15 Claims / 15 EUs across macroeconomics, microeconomics, money-and-banking, organizational-behavior and public-budgeting. All records are present in the exact-version master. Key findings: narrow GDP/inflation/equilibrium wording; Money A needs a distinct IMF source; Organizational Behavior's APA Source should be replaced/aligned to OpenStax OB; Public Budgeting needs OECD/PEFA/IMF source separation.
- Batch 10–12 combined: **50 Claims / 54 EUs / 19 Sources across 16 candidate slices**. All exact records were found in the master; no dependency rows were added. Master remains **1,129 = 1,058 candidate keys + 71 dependencies**; Part II slice coverage remains 124/385. All affected Claims remain HOLD.
- Dossiers: `FIRST-EDITION-BATCH11-PHYSICAL-SCIENCES-AND-OBSERVATION-LOCATOR-RESEARCH-2026-11-19.md`; `FIRST-EDITION-BATCH12-ECONOMICS-AND-GOVERNANCE-LOCATOR-RESEARCH-2026-11-19.md`.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22: OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `b8d8c574a66d6b79299cee76933aea7a96b57c43`, 52 commits ahead of last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 20 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for the current HEAD. Runs on the immediately preceding HEAD `170ce7c` show Browser Tests and Reference Tests cancelled after subsequent commits; Offline Edition and Release Conformance Gate were still in progress on that older HEAD. These do not validate the current HEAD.
- The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed. `main` remains untouched by this work.

### Next execution sequence

1. Inspect all remaining domain-audit reports and active bounded authorizations before selecting Batch 13; choose only candidate Claims not already reviewed.
2. Continue in 15-Claim batches, with direct locators, support boundaries, source identity and rights checks.
3. Reconcile any genuinely missing exact dependency rows only after exact ID/version/type verification; do not expand the 1,058 candidate denominator by inference.
4. Keep substantive Claim replacements, Source graph expansions and rights-sensitive changes separate for owner/editor approval.
5. Preserve HOLD; run release gates only after authorized canonical changes on a frozen final HEAD.


## Execution checkpoint — Batch 10 supplement and Batch 12 corrections — 2026-11-19

- Added a focused Batch 10 supplement for `water-security-basics`: 3 Claims / 4 EUs, with direct UN-Water §1 and §3D locators and a bounded EPA contribution for contamination/disaster protection. This is an additional slice review, not a renumbering of the original Batch 10 (which remains 20 Claims / 24 EUs across its six original slices).
- Added a focused Batch 12 correction addendum; did not repeat the existing 15-Claim / 15-EU Batch 12 scope. Corrections: IMF “Micro and Macro” directly covers employment/GDP/inflation for Macro A; GDP wording should say monetary value rather than market value because some non-market government output is included; inflation can be narrowed to rate of increase over a period; Micro C should drop unsupported “chosen market definition”; Federal Reserve remains the right source for Money B/C while IMF “What Is Money?” is needed for Money A; OpenStax *Principles of Economics 3e* and *Organizational Behavior* are CC BY-NC-SA 4.0 and explicitly restrict LLM ingestion/generative-AI use without prior written permission.
- Dossiers: `FIRST-EDITION-BATCH10-SUPPLEMENT-WATER-SECURITY-2026-11-19.md`; `FIRST-EDITION-BATCH12-SOURCE-AND-RIGHTS-CORRECTION-ADDENDUM-2026-11-19.md`.
- No new candidate Claim or dependency node was added. Exact-version master remains 1,129 rows = 1,058 candidate keys + 71 dependencies; Part II coverage remains 124/385. No canonical JSON, versions, allowlists, publication states or dispositions changed. All affected records remain HOLD.

### PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Current docs-only research commits are confined to `RELEASE/`; no `CONTENT/` or `REFERENCE/` path was changed by this work.
- No exact-head CI PASS is claimed. The last confirmed 4/4 green content HEAD remains `48c78389fb5345223627a687b22d51ee260b9d7d`. Any workflow result from a prior HEAD does not validate the current docs-only HEAD.
- `main` was not modified. No merge, deployment or release approval was performed.

### Next execution sequence

1. Reconcile the bounded Batch 10–12 locator-only changes into one implementation packet with exact records, proposed next versions, locator text and source-rights flags.
2. Keep the Money A IMF source expansion and Macroeconomics source expansion separate from locator-only updates; allocate canonical IDs only through the established ID process.
3. Resolve OpenStax AI-ingestion restrictions before any project reuse of Principles of Economics 3e, Principles of Microeconomics 3e, Organizational Behavior, Biology 2e or other affected titles.
4. Continue with remaining candidate slices only after checking the full RELEASE tree and authorization register; do not select solely from a stale status label.
5. Preserve HOLD. Run affected-slice tests and all release gates only after authorized canonical edits on a frozen final HEAD.


## Execution checkpoint — consolidated Batch 1–12 implementation queue — 2026-11-19

- Created `FIRST-EDITION-BATCH1-16-CONSOLIDATED-IMPLEMENTATION-QUEUE-2026-11-19.md` to convert existing research into four controlled lanes: locator-only changes, Source identity/URI corrections, Source/EU graph expansions requiring canonical ID allocation, and substantive Claim replacements/narrowing requiring editorial approval.
- Consolidated only existing dossiers; did not count duplicate reviews as new batch work or add Claims/EUs to the candidate denominator.
- Reconfirmed bounded authorizations already documented in the project: Chemistry, Engineering/Computing, Human Sciences, Legal/Trade/Institutional, R7, R9 and SI. Spot-checked the current canonical engineering/computing outputs: Cybersecurity Claims/EUs/Source/Context/Scope are v2; Databases are v3; Distributed Systems are v2; AI Basics are v2. These are already remediated and must not be repeated. The engineering addendum reports 72 canonical records changed across eight authorized slices; all eight remain HOLD.
- Critical correction retained: OpenStax Principles of Economics 3e, Principles of Microeconomics 3e and Organizational Behavior have CC BY-NC-SA 4.0 terms and explicit LLM-ingestion/generative-AI restrictions without prior written permission. Do not treat them as cleared sources.
- Master remains 1,129 exact-version rows = 1,058 candidate keys + 71 dependencies; Part II coverage remains 124/385. All reviewed slices remain HOLD. No canonical record changed in this queue-consolidation step.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- The research/queue updates in this step are confined to `RELEASE/`; no `CONTENT/` or `REFERENCE/` path changed.
- The last confirmed 4/4 green content HEAD remains `48c78389fb5345223627a687b22d51ee260b9d7d`. No exact-head CI PASS is inferred for later documentation-only commits.
- No merge, deployment, release approval or main-branch modification was performed.

### Next execution sequence

1. Turn the implementation queue into exact per-record diff packets; start with source/locator changes that do not require new canonical IDs or Claim replacement.
2. Keep OpenStax rights-sensitive sources out of the implementation set until written permission or a rights-compatible substitute is approved.
3. Prepare the Source/EU ID allocation packet for macroeconomics, Money A, Marine Biology, Pathology, Water Resources, Astronomy Observation, Climate Science, Computer Networks and Education Systems C.
4. Obtain explicit editor/subject-matter approval for all placeholder Claim replacements and proposed narrowings.
5. Apply only the exact authorized changes, re-fetch current versions, verify dependency edges, and run exact-head release gates after the final canonical changes.


## Execution checkpoint — Batch 13 completion — 2026-11-19

- Batch 13 completed: **15 Claims / 15 EUs across five candidate slices** — history-of-science, history-of-technology, religious-studies, literature and oceanography. All 35 exact record keys are present in the master; no dependency rows were added.
- History/Culture work used the existing domain audit without repeating its broad review. Smithsonian/HSS/AHA source roles were separated; LOC Literary Research Guide was mapped to works, manuscripts/archives and criticism; Harvard Pluralism “Rivers of Faith” and the Religious Studies Project methodology article were mapped to internal diversity, historical change and non-confessional academic study.
- Oceanography A–C are editorial placeholders. Three substantive NOAA-backed replacement Claim proposals were prepared: oceanography's four disciplines; multiple mechanisms driving currents; CTD measurements of conductivity, temperature and depth/pressure. All require owner/editor approval before canonical replacement.
- Batch 10–13 combined: **65 Claims / 69 EUs / 24 current Sources across 21 candidate slices**. All exact records are already in the master; no new dependency rows. Master remains **1,129 = 1,058 candidate keys + 71 dependency records**; Part II coverage remains 124/385. All affected Claims remain HOLD.
- Batch 13 dossier: `FIRST-EDITION-BATCH13-HISTORY-LITERATURE-RELIGION-OCEANOGRAPHY-RESEARCH-2026-11-19.md`.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `78639d5bb2bf500e4f8f17e4bc17d828d82f5b6b`, 61 commits ahead of last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 23 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for this exact HEAD. The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed.
- `main` remains untouched by this work. No merge, deployment or release approval was performed.

### Next execution sequence

1. Inspect the remaining Society/Institutions, Earth/Space and History/Culture domain-audit reports against the exact-version master and active authorization scopes; do not repeat slices covered by Batches 1–13.
2. Select the next 15 candidate Claims from unreviewed slices; re-fetch exact Claim→EU→Source chains and prepare direct locator/source-fit research.
3. Keep placeholder Claim replacement proposals separate from locator-only work and source-graph expansions.
4. Reconcile only genuinely missing exact dependency rows after exact ID/version/type verification; preserve the candidate denominator and HOLD dispositions.
5. Continue owner decisions R-01–R-10, rights, independent editorial review and Human View; run release gates only after authorized canonical edits on a frozen final HEAD.


## Execution checkpoint — R9 remaining locator reconciliation — 2026-11-19

- Re-fetched all 12 canonical records in `food-systems-basics`: both Sources, Claims A–D, EUs A–D, Context and Scope are v2; all four EUs contain claim-specific locators. The R9 bounded food-systems remediation is already implemented. The older R9 addendum's statement that four food-systems EUs remained unpinned was stale.
- Re-fetched all nine canonical records in `settlement-geography-basics`: all remain v1; EUs A–C still have only generic descriptions and no `material.locator`. The Batch 9 locator research already found direct passages in the joint 2021 *Applying the Degree of Urbanisation* manual.
- Updated the R9 evidence-depth addendum: current remaining unpinned R9 count is **3 EUs in settlement geography**, not 7 across food systems and settlement geography.
- Prepared `R9-SETTLEMENT-GEOGRAPHY-BOUNDED-AUTHORIZATION-PROPOSAL-2026-11-19.md` with the exact nine-record v1→v2 scope, joint six-institution Source identity, proposed locator text, Context/Scope boundaries and prohibited changes. No active settlement-specific authorization was found, so canonical records were not changed.
- Rights blocker: the joint manual is CC BY-NC-SA 3.0 IGO; commercial reuse is not cleared and third-party maps/photos are excluded. Owner must decide compatibility with the project's distribution/licensing model.
- All ten R9 slices remain HOLD. No candidate denominator, allowlist or publication state changed.


## Execution checkpoint — Batch 13 integrated into implementation queue — 2026-11-19

- Found and reviewed the existing Batch 13 dossier: 15 Claims / 15 EUs across History of Science, History of Technology, Religious Studies, Literature and Oceanography. No re-research was performed.
- Incorporated Batch 13 into the consolidated implementation queue. Direct locator candidates: History of Technology A/B, Literature A/B and Religious Studies B. Source graph expansions: HSS for History of Science A; AHA methodology for History of Science/Technology C and Literature C; Religious Studies Project for Religious Studies A/C. Oceanography A–C are editorial placeholders and require substantive replacements plus three NOAA source/EU chains.
- All five Batch 13 slices remain HOLD. No canonical records or IDs were changed.
- The consolidated queue now covers Batches 1–13 plus bounded authorization tracks and identifies locator-only, source-graph, substantive-Claim and rights gates separately.


## Execution checkpoint — Batch 14 sociology/public administration — 2026-11-19

- Completed a current-canonical review of the two residual slices from the Society and Institutions gap audit: `sociology-basics` and `public-administration-basics`.
- Exact scope: 18 records (2 Sources, 6 Claims, 6 EUs, 2 Contexts, 2 Scopes). All are v1; no canonical record was changed.
- Sociology A–C are editorial/meta placeholders. ASA's 2023 *Sociology: A 21st Century Major* brochure, p. 1, directly supports three factual replacement proposals: definition/scope, research methods, and research contribution to theory/policy. All replacements require editor approval and rights review.
- Public Administration A–C are substantive. UN ECOSOC Committee of Experts on Public Administration E/C.16/2006/4 §III paras. 18–21, §I paras. 1–3 and §VI paras. 36–37 provide direct locator candidates for government functions/services, rules/procedures, and jurisdiction/context variation. Existing Claim wording can remain; Source/EUs/Context/Scope need versioned alignment.
- New dossier: `FIRST-EDITION-BATCH14-SOCIOLOGY-PUBLIC-ADMINISTRATION-REMEDIATION-RESEARCH-2026-11-19.md`, including the exact 18-record bounded authorization request and prohibited changes.
- Both slices remain HOLD. No canonical ID or candidate denominator changed.


## Execution checkpoint — Batch 15 hydrology and meteorology — 2026-11-19

- Reviewed the existing Hydrology/Meteorology/Oceanography domain audit and deliberately excluded Oceanography because Batch 13 already covers its three placeholder Claims.
- Re-fetched exact current Hydrology and Meteorology canonical records: 6 Claims, 6 EUs, all v1. The six EUs contain generic descriptions only; no claim-specific `material.locator` exists.
- Direct source routes verified: USGS “What is Hydrology?” for Hydrology A/B; its linked “Water cycle” page for runoff/infiltration/evaporation/evapotranspiration and the parent hydrology page for transpiration; NOAA “Weather and atmosphere” for Meteorology A; NOAA “Weather observations” → “Observation methods” and “Weather forecasting” for B/C.
- Hydrology C's four process terms require careful distinction: evapotranspiration is combined evaporation+transpiration, while the parent hydrology page separately describes plant transpiration. No technical equivalence is inferred.
- Prepared exact 12-record bounded authorization proposal (Hydrology Source/Claims/EUs/Context/Scope plus Meteorology EUs only). No active authorization exists for these slices; no canonical change performed.
- New dossier: `FIRST-EDITION-BATCH15-HYDROLOGY-METEOROLOGY-LOCATOR-REMEDIATION-RESEARCH-2026-11-19.md`. Both slices remain HOLD.
- Consolidated queue now extends through Batch 15 and contains Batches 13–15 as explicit addenda; no candidate denominator or dependency count changed.


## Final technical verification — 2026-11-19

- PR #22 exact HEAD: `bed0e7cf2fcca7f28a10f11f96b31b11024f6245`.
- PR state: OPEN / DRAFT / NOT MERGED.
- Compare against last confirmed green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`: 78 commits ahead; 28 changed paths; every changed path is under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs and no combined status checks were returned for this exact HEAD. Do not claim a new exact-head CI PASS. The previously reported 4/4 PASS remains tied to `48c78389` only.
- This work did not write to `main`, merge PR #22, deploy or approve publication.


## Execution checkpoint — WP2 source-rights delta integrated — 2026-11-19

- Extended the consolidated WP2 rights status and owner decision register with source-specific findings from Batches 10–15.
- Corrected the earlier OpenStax *Principles of Economics 3e* CC BY 4.0 statement: the current preface says CC BY-NC-SA 4.0 and explicitly restricts LLM-ingestion/generative-AI use without prior written permission. The same restriction is present in *Principles of Microeconomics 3e* and *Organizational Behavior*.
- Added item-level flags for the CC BY-NC-SA 3.0 IGO Settlement Geography manual, copyrighted ASA Sociology brochure, public-access UN ECOSOC paper, and third-party media on USGS/NOAA pages.
- R-01–R-10 remain OPEN. No project licence or permission is adopted; no third-party expressive material is copied; all affected records remain HOLD.
- Updated documents: `FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md` and `FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER-2026-11-19.md`.


## Execution checkpoint — Batch 14–16 and candidate-pool reconciliation — 2026-11-19

- **Batch 14:** six candidate Claims / six EUs / two Sources in Remote Sensing and Solar System. Nine additional current Claims / nine EUs / three Sources in Climate Adaptation, Hydrology and Meteorology were researched as out-of-master supplemental material; they are not candidate keys. The out-of-master count is now **30 known Claims across 14 slices** (21 previously listed plus these nine). The Batch 14 report, master note and Batch 1/3 scope report were corrected to preserve this boundary.
- **Batch 15:** 15 candidate Claims / 15 EUs / five Sources across Law, Public Administration, Social Statistics, Sociology and Units/Measurement. All 35 exact keys are in the master. Sociology A–C are editorial placeholders with substantive ASA replacement proposals; Social Statistics and Measurement require additional source/EU chains.
- **Batch 16:** Migration Basics, three Claims / three EUs / one Source. All seven exact keys are in the master. IOM direct locators cover migration and drivers; UNHCR/UN Guiding Principles cover refugee/IDP distinctions.
- Batches 10–16 combined: **89 candidate Claims / 93 EUs / 32 current Sources across 29 candidate slices**, plus nine out-of-master supplemental Claims from Batch 14. Across Batches 1–16, **224 candidate Claims** have batch-level research; all remain HOLD pending approved implementation, rights and editorial gates.
- Exact-version master remains **1,129 = 1,058 candidate keys + 71 dependencies**; Part II slice coverage remains 124/385. No canonical JSON was changed by Batches 10–16.
- Candidate-pool reconciliation: all **121** candidate slices are now status-accounted for by Batches 1–16 (83 unique slices), active bounded authorizations, 17 prior-screened slices recorded in the master, or the separate P8 Water Security re-audit. The set reconciliation found **zero unclassified candidate slices**. This does not mean authorized edits, rights decisions, independent review or release gates are complete.
- Detailed dossiers: `FIRST-EDITION-BATCH14-EARTH-SYSTEMS-CLIMATE-REMOTE-SENSING-RESEARCH-2026-11-19.md`; `FIRST-EDITION-BATCH15-LAW-ADMINISTRATION-SOCIAL-STATISTICS-MEASUREMENT-RESEARCH-2026-11-19.md`; `FIRST-EDITION-BATCH16-MIGRATION-BASICS-EVIDENCE-AND-LEGAL-STATUS-RESEARCH-2026-11-19.md`.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `55ce58b9eb74f0f018b5d541e83ba0d3b31688a9`, 87 commits ahead of the last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 31 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for the current HEAD. The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed.
- `main` remains untouched by this work. No merge, deployment or release approval was performed.

### Next execution sequence

1. Stop expanding the broad batch queue: all 121 candidate slices are status-accounted for. Move to the next priority: reconcile the 94 active bounded authorization scopes against current canonical records and identify which authorized edits are still pending versus already applied.
2. Apply only changes that are both explicitly authorized and demonstrably pending at one frozen HEAD; do not reapply completed changes or widen any authorization.
3. Keep the 30 out-of-master Claims outside the candidate denominator until explicit owner scope decisions are recorded.
4. Resolve project-level rights/ownership decisions R-01–R-10 and the independent Human View/high-consequence review.
5. After authorized canonical edits, run exact graph preflight, affected tests and all release gates on one immutable final HEAD; preserve HOLD until all gates pass.


## Execution checkpoint — Batch 15 and Batch 16 migration evidence research — 2026-11-19

- Batch 15 completed a separate 15-Claim / 15-EU review across five candidate slices: `law-basics`, `public-administration-basics`, `social-statistics-basics`, `sociology-basics` and `units-and-measurement`. Direct locator candidates were mapped for all 15 EUs. Sociology A–C are editorial placeholders and require substantive replacement proposals. Public Administration requires a separate UN source chain; Social Statistics B/C need UN FPOS and Statistics Canada source chains; Units and Measurement A/C need BIPM VIM/NIST uncertainty sources. All five remain HOLD. Dossier: `FIRST-EDITION-BATCH15-LAW-ADMINISTRATION-SOCIAL-STATISTICS-MEASUREMENT-RESEARCH-2026-11-19.md`.
- Batch 16 completed the remaining migration-basics candidate slice: 3 Claims / 3 EUs / 1 current Source. IOM Toolkit provides direct locators for migration definition and drivers; Claim C needs separate UNHCR Refugee Convention and UN Guiding Principles dependencies to preserve the migrant/refugee/IDP legal distinctions. Current IOM Source points to a broad landing page; exact Toolkit identity/URI correction is proposed. All Claims remain HOLD. Dossier: `FIRST-EDITION-BATCH16-MIGRATION-BASICS-EVIDENCE-AND-LEGAL-STATUS-RESEARCH-2026-11-19.md`.
- Supplemental P4/P5 pinpoint pass: 15 existing Claims / 18 EUs / 8 Sources across disaster-response-logistics, disaster-recovery, water-quality and electrical-grid slices were re-fetched. This is **not a new candidate batch** and does not alter the P4/P5 historical denominators. Exact locators mapped to FEMA IS-52, WFP Logistics Cluster, FEMA NDRF Third Edition, UNDRR, EPA, WHO 2026 drinking-water guidelines, EIA and DOE. Material source/wording findings: (1) OCHA homepage is too broad for the primary disaster-logistics Source; (2) disaster-recovery FEMA Source points to an IS-2900 course overview rather than the NDRF publication; (3) current Disaster Recovery Claim B incorrectly implies recovery is a separate phase, while the NDRF says recovery begins during response and overlaps response/rebuilding/mitigation; (4) Water Quality A should narrow to pollutant-specific criteria and Claim C should state the U.S. Clean Water Act boundary; (5) WHO Source identity is generic and should identify the 2026 fourth edition with three addenda. All four slices remain HOLD. Dossier: `FIRST-EDITION-P4-P5-DISASTER-WATER-QUALITY-ELECTRICAL-GRID-PINPOINT-SUPPLEMENT-2026-11-19.md`.
- Exact-version master remains **1,129 rows = 1,058 candidate keys + 71 dependency records**; Part II coverage remains **124/385**. No new dependency row or candidate Claim was added by these passes.
- No canonical JSON, Relation, allowlist, publication state or disposition changed. No canonical IDs were invented. All affected records remain HOLD.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `1e673e66f995b02451304c5ae24da569e1fe8136`, 90 commits ahead of last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 31 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for this exact HEAD. The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed.
- `main` remains untouched by this work. No merge, deployment or release approval was performed.

### Next execution sequence

1. Continue from the consolidated implementation queue, not by re-running completed batches. Prioritize the owner-authorized locator-only lane; keep source-graph expansions and substantive Claim wording changes separate.
2. Reconcile the new Batch 15/16 proposals into the controlled implementation queue with exact record IDs, versions, proposed locators, Source corrections, new dependency requirements and rights flags.
3. Keep Disaster Recovery B, Water Quality A/C, Sociology A–C and any other Claim wording corrections in a separate editor-approval lane.
4. Continue with any genuinely unreviewed candidate slices only after checking the full RELEASE tree, exact-version master and active bounded authorizations.
5. Preserve HOLD. Apply canonical edits only under explicit bounded authorization, then run affected tests and exact-head release gates on a frozen final HEAD.


## Execution checkpoint — Batch 15–16 implementation queue and WP2 rights sync — 2026-11-19

- Consolidated implementation queue extended through Batch 16. The former Batch 1–15 filename was replaced with `FIRST-EDITION-BATCH1-16-CONSOLIDATED-IMPLEMENTATION-QUEUE-2026-11-19.md`; the queue now includes Batch 15 law/public administration/social statistics/measurement, Batch 16 migration, and the separate P4/P5 pinpoint supplement.
- WP2 rights status extended with source-specific flags for Cornell Wex, UN HRC/UN FPOS, Statistics Canada, ASA, BIPM/JCGM, NIST, IOM/UNHCR/UN Guiding Principles, FEMA, WFP Logistics Cluster, UNDRR, EPA, WHO 2026 drinking-water guidelines, EIA and DOE. Owner decision register cross-referenced to the expanded rights screen.
- R-01–R-10 remain OPEN. No project licence, permission, rights holder, editor, release approver or public contact is selected. No canonical record, candidate denominator, allowlist or disposition changed.
- All affected slices remain HOLD; no canonical JSON, Relation or publication state changed.


## Execution checkpoint — P4/P5 bounded pinpoint proposal prepared — 2026-11-19

- Prepared `FIRST-EDITION-P4-P5-DISASTER-WATER-QUALITY-ELECTRICAL-GRID-BOUNDED-AUTHORIZATION-PROPOSAL-2026-11-19.md` from exact current records and the supplemental source research.
- Proposed scope: 49 existing records across four already-audited slices; 36 existing-record version changes. No new candidate keys or dependency rows. One optional FEMA Distribution Management Plan Guide Source/EU pair is conditional on canonical ID allocation and explicit approval.
- Exact proposal separates locator-only changes from Source identity corrections and the three substantive Claim wording changes (Disaster Recovery B; Water Quality A/C). No changes to publication state, Relations, allowlists or candidate membership are proposed.
- No separate record-level P4/P5 bounded authorization was found in `EDITORIAL-CORRECTION.json`; therefore this is a proposal only. No canonical JSON changed. All four slices remain HOLD.
- Consolidated implementation queue now references the proposal. Exact-version master remains 1,129 = 1,058 candidate keys + 71 dependency records; Part II coverage remains 124/385.

### Current PR #22 provenance at pre-board-update HEAD

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Pre-board-update HEAD: `aff5f301e7dd8ca64b2524b5a25b9ed910090c1d`, 97 commits ahead of the last confirmed 4/4 green content HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 32 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` paths changed.
- No workflow runs or combined status checks were returned for this exact HEAD. The 4/4 PASS remains tied to `48c78389`; no new exact-head CI PASS is claimed.
- No merge, deployment, main-branch write or release approval occurred.


## Execution checkpoint — R9 Settlement Geography CC BY 4.0 alternative — 2026-11-19

- Re-fetched the current Settlement Geography canonical records: Claims A–C and EUs A–C remain v1; all three EUs still lack claim-specific locators. Source, Context and Scope remain v1. No canonical record changed.
- Found a rights-compatible alternative to the joint 2021 manual: Eurostat, *Review and implementation of the degree of urbanisation*, 2026 edition. It directly supports the urban–rural continuum, harmonised international comparison, Level 1/Level 2 classes, population-grid method and the “complements rather than replaces national definitions” boundary (§1.2 p.6; §2.1 p.7).
- The report's front matter explicitly licenses EU-owned content under CC BY 4.0 with attribution/change indication. Third-party cover photo, most maps, other photos and administrative-boundary content are excluded. Proposed use is text-only paraphrase and locators; no visual assets.
- The report is a Eurostat Statistical Report and states it is not representative of the European Commission's official position. That source-status boundary is preserved.
- Created `R9-SETTLEMENT-GEOGRAPHY-EUROSTAT-CC-BY-4-0-SOURCE-ALTERNATIVE-2026-11-19.md`; updated the earlier settlement bounded-authorization proposal, WP2 rights status, owner decision register and consolidated implementation queue.
- The exact nine-record v1→v2 scope remains a proposal, not an authorization. No new Source/EU ID is invented. All nine records remain HOLD pending owner approval and editorial review.


## Execution checkpoint — bounded diff packets, R7 reconciliation and Batch 16 authorization preparation — 2026-11-19

### Completed documentation work

- Prepared `FIRST-EDITION-BATCH15-LOCATOR-ONLY-DIFF-PACKET-2026-11-19.md`: four bounded candidate EU locator-only changes (Law A/B, Social Statistics A, Units and Measurement B). Law C excluded for insufficient comparative support; Units B retains a separate BIPM qualifier dependency. Owner approval remains required; no canonical edit.
- Prepared `R7-CIVIL-SOCIETY-BOUNDED-DIFF-PACKET-2026-11-19.md`: all 13 v1 records inventoried with exact SHAs; primary OECD/LEGAL/5021 and independent UN Civil Society Unit source identities and six claim-specific EU locators specified; Claim statements preserved. Existing bounded authorization applies; rights/editorial/Human View gates remain open.
- Prepared `R7-COMPARATIVE-CIVILIZATIONS-BOUNDED-DIFF-PACKET-2026-11-19.md`: all nine v1 records inventoried with exact SHAs; AHA 1998 source and claim-specific locators specified; MOE 2021 chronology/causation reference represented through the existing schema's `provenance.external_sources` on EU-C. No new canonical Source ID or schema change. The prior schema-model blocker is resolved; rights/editorial/Human View gates remain open.
- Prepared `R7-LABOUR-ECONOMICS-OPENSTAX-RIGHTS-DECISION-2026-11-19.md`: documents that the active authorization JSON still says CC BY 4.0 while the official OpenStax Preface states CC BY-NC-SA 4.0 and prior written permission for LLM training/ingestion and generative-AI offerings. The WP2 rights status and owner decision register now explicitly flag this active authorization inconsistency. No owner path selected; Labour Economics remains blocked/HOLD.
- Prepared `FIRST-EDITION-BATCH16-MIGRATION-BASICS-BOUNDED-AUTHORIZATION-REQUEST-2026-11-19.md`: exact seven-record SHA inventory; requests IOM Toolkit source alignment and two separate canonical Source plus two Evidence Use dependencies for UNHCR and UN Guiding Principles Claim C support. No IDs invented or allocated; owner authorization required; Migration Basics remains HOLD.
- Updated the consolidated Batch 1–16 queue, WP2 rights status, rights/editorial owner decision register and R7 authorization reconciliation to index the packets and preserve the corrected execution order.

### Reconciliation and control boundaries

- R9 and Legal/Trade already-applied samples and International Law's seven dependent alignment records were verified as current; they are not to be repeated. This remains a spot-check, not a complete certification of all 94 active bounded authorization scopes.
- No canonical `CONTENT/` or `REFERENCE/` files changed in this iteration. No record IDs were allocated; no Claim statement, Source/EU chain, Relation, allowlist, coverage denominator, publication/completion state or INCLUDE/HOLD/EXCLUDE disposition changed.
- `main` remains at `d58289f319993ede5294a46f4741a506fd2fd710`; no merge or deployment occurred.

### PR #22 exact-head checkpoint before this board update

- PR #22 remains OPEN / DRAFT / NOT MERGED; branch `mvp-public-contribution-design-2026-10-11`.
- Inspection HEAD: `906858b9eabd063b66c30fb2a1c0ac549a67417f`; 121 commits ahead of last confirmed green HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Compare: 39 changed paths, all under `RELEASE/`; zero `CONTENT/`, `REFERENCE/` or other paths changed.
- Workflow runs for the preceding documentation HEADs were queued/in progress; no final 4/4 PASS on the current inspection HEAD is claimed. The historical 4/4 PASS remains tied to `48c78389` only.
- After this board update, re-check the newly triggered workflows on the resulting immutable HEAD. Keep all affected slices HOLD.

### Next execution sequence

1. Continue exact reconciliation of the remaining active bounded authorization scopes against current canonical records; do not infer completion from a Source version alone.
2. Keep the Civil Society and Comparative Civilizations bounded packets in the authorized preparation lane; implementation only after applicable rights/editorial gates are resolved and the exact record SHAs are re-fetched.
3. Obtain an owner decision on the OpenStax authorization conflict; do not use the inaccurate CC BY 4.0 clause.
4. Obtain owner authorization for Batch 16's additional canonical IDs and Claim C dependencies before any graph expansion.
5. Resolve R-01–R-10 and independent Human View/high-consequence review.
6. After approved canonical edits, run affected-slice tests and all release gates on one immutable final HEAD; preserve HOLD until every independent gate closes.


## Execution checkpoint — R9 exact-version package — 2026-11-19

PR #22 pre-audit HEAD: `5ad42003540ae98a87a3f04be6ee5d018658cc79`.

- Exact-head CI on that HEAD completed **4/4 PASS**: Reference Tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests.
- Reconciled 33 canonical records across History of Mathematics (11), Cartography (10) and Food Systems (12).
- Cartography and Food Systems: current record graphs and the named bounded authorizations are aligned at the version/reference level. Both remain HOLD for rights, independent editorial review and Human View.
- History of Mathematics: all internal version references are coherent, but the live Claim B regional scope and Claim C calculus/Newton–Leibniz subject/source materially exceed/differ from the active authorization. The mismatch is recorded in the R9 evidence-depth follow-up and register addendum. No canonical correction is authorized by this audit; owner decision is required. History of Mathematics remains HOLD.
- No canonical JSON, allowlist, publication state, or release decision changed.

### Next execution order

1. Resolve the History of Mathematics authorization mismatch through an explicit owner decision; do not silently ratify the current graph.
2. Continue with Settlement Geography: inspect all nine exact-version records, validate UN-Habitat/Eurostat source alignment and close the three remaining Evidence Use pinpoint locators only within an approved bounded scope.
3. Reconcile the resulting cross-slice Relation dependency and rights boundaries; retain HOLD.
4. Continue remaining Chemistry and Human Sciences authorization/reference checks, then the legal/trade/institutional residuals.
5. Re-run all exact-head CI after documentation updates; the 4/4 PASS above applies only to pre-audit HEAD `5ad4200`, not to subsequent commits.


## Execution checkpoint — R7 exact-head rights and dependency reconciliation — 2026-11-19

Inspection baseline: PR #22 HEAD `531d4f57c8aed106e1f2b42bd5295752740e3545`; all subsequent commits in this checkpoint are documentation-only.

### Completed in this session

- Human Sciences exact graph spot-check: 27/27 records across Psychology, Neuroscience and Developmental Biology; current v2 provenance and Claim/Evidence Use/Source references align. No repeat remediation.
- Civil Society Basics: 13/13 canonical records re-fetched; all SHA values match the prepared bounded diff packet. Rights recheck added: OECD Legal Instrument permission is narrow and does not cover the UN page; UN site terms do not provide broad redistribution/derivative rights. Owner decision remains open.
- Comparative Civilizations Basics: 9/9 canonical records re-fetched; all SHA values match the prepared bounded diff packet. AHA source substance and MOE printed-p.5 chronology/causation locator were checked against official materials. AHA open licence not identified; MOE reproduction terms are limited to personal/non-commercial educational use. Owner decision remains open.
- Labour Economics Basics: 13/13 records re-fetched; all remain v1 and Claim/Evidence Use/Source/Context/Scope links align. OpenStax HTML Preface/help pages state CC BY-NC-SA 4.0 and an LLM-ingestion restriction, while a separate official PDF asset states CC BY 4.0. This asset-level conflict is now explicitly recorded; owner clarification or source replacement is required before implementation.
- Updated the R7 reconciliation, source rights screen, owner decision register, dedicated Labour Economics decision packet and consolidated implementation queue.
- Inspected the Part II exact-version master: 1,129 distinct exact-version rows = 1,058 candidate keys + 71 dependency records. The earlier 1,119-row state was followed by a ten-record dependency supplement. Part II coverage remains 124/385; the separate first-edition candidate-slice accounting classifies all 121 candidate slices. These counts must remain distinct.
- GitHub compare from `cbb620b1b2fc714414b57dc53ac7b8faba8980e1` to the current checkpoint showed 33 changed paths, all under `RELEASE/`; zero `CONTENT/` and zero `REFERENCE/` changes.

### Blockers and next actions

1. Civil Society and Comparative Civilizations remain prepared but blocked by owner-level rights/distribution decisions; do not apply canonical packets until the relevant gate is resolved.
2. Labour Economics remains blocked by the OpenStax asset/licence inconsistency; do not rely on the CC BY 4.0 clause in the active authorization.
3. Migration Basics Batch 16 remains a request only; do not allocate the additional UNHCR/UN Guiding Principles IDs without owner approval.
4. Continue exact-version/dependency reconciliation on the next uncovered authorized scope, using current canonical JSON and avoiding closed domain remediation.
5. Re-run and record Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests on one exact final HEAD after documentation changes.

### Safety and release state

No canonical JSON, Relation, allowlist, candidate membership, publication/completion state or INCLUDE/HOLD/EXCLUDE decision changed. All affected slices remain HOLD. PR #22 remains OPEN / DRAFT / NOT MERGED; `main` remains unchanged. No exact-head CI PASS is claimed for the resulting documentation HEAD until its workflows report final success.

## Execution checkpoint — 2026-11-20, current PR #22 head `3c195ffc6ae48540613ecc4e296d016f93951e4f`

### Completed bounded work since the previous board snapshot

- Relation/Context Option A: 61 target-specific Context records and 61 exact Relation frame updates are implemented under the owner's 2026-11-20 approval. The separate earthquake Event and water-storage model remain unchanged and HOLD.
- Infrastructure Resilience historical source: exact FEMA Source @1 snapshot restored as a separate versioned file alongside corrected CISA Source @2. Existing historical references were preserved; no dependent Claim/Evidence Use/Relation/Context was repointed. Coverage is 4,742 records / 590 Sources. Schema was not relaxed. See `R9-INFRASTRUCTURE-RESILIENCE-CISA-EVIDENCE-REMEDIATION-2026-11-20.md`.
- Research/statistics Relation locator research: all three Research Methods EUs now have exact National Academies locator candidates; Statistics Inference A has a direct NIST/SEMATECH §3.1.3.4 locator. The current Relation pair is semantically weak; a stronger existing endpoint pair is proposed, but no canonical records changed. See `FIRST-EDITION-RESEARCH-STATISTICS-RELATION-LOCATOR-RESEARCH-2026-11-20.md`.
- The stale Work Package 1 Batch 2 six-slice handoff was reconciled against current canonical state and prior audit reports. Cybersecurity is already @2 under engineering remediation; Psychology, Neuroscience and Developmental Biology were remediated under HUMAN-SCIENCES-REMEDIATION-001; Learning has a prior domain-expansion audit; Economics Basics has prior M1 and economic-systems screening. No duplicate screening was performed. Their prior HOLD decisions and rights/editorial gates remain in force.
- No owner-level rights/editorial decision R-01–R-10 was inferred or closed.

### Exact-head CI status at `f2c24fbac23c331461022b37f4d92bf8cf20bff9`

- Offline Edition — PASS (pull-request and push runs).
- MVP Contribution Form Browser Tests — PASS.
- Reference implementation tests — still in progress.
- Release Conformance Gate — still in progress.
- Content preflight completed successfully in the Release Gate and Reference Tests jobs.
- These results belong to HEAD `f2c24...`, not to this later documentation HEAD. All four required workflows must be rerun and verified together on one immutable final HEAD.

### Current execution order — preserved

1. Finish the exact-head Reference Tests and Release Conformance Gate; investigate any failure before further canonical changes.
2. Prepare bounded owner decision packets for the earthquake Event and water-storage State/Relation model. Current user direction is that both decisions remain open and all Relations remain HOLD; do not mutate either item.
3. Apply the research/statistics locator and endpoint proposal only after a matching bounded authorization; keep the Relation HOLD through independent review.
4. Execute the ready Library/Archival and Infrastructure semantic endpoint proposals only after exact evidence, rights and owner-authorization checks.
5. Continue item-level rights review and obtain owner decisions R-01–R-10; no legal entity, licence, editor or release approver is invented.
6. Re-run all four exact-head workflows after canonical or release-document changes. Technical CI does not grant release eligibility.

### Explicitly preserved boundaries

- PR #22 remains OPEN / DRAFT / NOT MERGED.
- `main` remains unchanged at `d58289f319993ede5294a46f4741a506fd2fd710` in the latest boundary check.
- All candidate slices and all 15 semantic HOLD Relations remain HOLD.
- No first-edition allowlist, publication, preview, deployment or release approval was created.
- The 261 Part II slices outside the bounded map remain outside the audit scope unless the owner authorizes expansion.

### Follow-on evidence closure — emergency / infrastructure Relation candidate — 2026-11-20

- The infrastructure-specific endpoint gap for `REL_M3_EMERGENCY_INFRASTRUCTURE@2` now has an existing candidate: `CLM-INFRASTRUCTURE_RESILIENCE-D@2`, supported by `EU-INFRASTRUCTURE_RESILIENCE-D@2` and CISA Source @2 with the exact locator p. 1, “Overview” and “Learn” module.
- The emergency-management endpoint `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1` has direct locator candidates from UNDRR's “Disaster management” terminology entry and FEMA IS-230.E course objectives. Its Evidence Use records remain generic and require authorized versioned locator work.
- Proposed endpoint pair: emergency-management Claim A @1 + infrastructure Claim D @2, with contextual/navigation semantics only. Proposed Relation @2→@3 and Context @1→@2 coordinated exact-version updates are documented in `FIRST-EDITION-INFRASTRUCTURE-EMERGENCY-RELATION-ENDPOINT-RESEARCH-2026-11-20.md`.
- This closes candidate discovery and source-locator research, not the owner authorization, rights clearance, independent semantic review or Human View. Relation remains HOLD; no canonical changes were made.
- The prior infrastructure endpoint statement in this board that a specific Claim D locator was still missing is superseded by this research result. The relation itself remains uncorrected and HOLD.

### Follow-on completion — Library / Archival Relation alignment — 2026-11-20

The previously pending Library/Archival endpoint substitution has now been explicitly authorized and implemented. The earlier board language that this alternative still required a new authorization is superseded.

Verified exact current records:
- `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@6`
- `CTX-REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3)
- Library endpoint `CLM-LIBRARY_SCIENCE-C@2)
- Archival endpoint `CLM-ARCHIVAL_SCIENCE-A@2)
- Relation @6 ↔ Context @3 exact reciprocal references.

The semantic endpoint mismatch and version-cycle blocker are closed for this Relation. It remains HOLD with both slices pending item-level rights/distribution review, independent editorial review and Human View. No INCLUDE or allowlist decision was made. See `R9-LIBRARY-ARCHIVAL-RELATION-ALIGNMENT-2026-11-20.md`.

### Model-level owner decision packet completed — 2026-11-20

The earthquake and water-storage blockers have now been re-fetched at exact canonical versions and documented without changing any records. See `FIRST-EDITION-EARTHQUAKE-WATER-STATE-MODEL-OWNER-DECISION-PACKET-2026-11-20.md`.

- Earthquake: `EVT-EARTHQUAKE-SHAKING@1` is a generic ground-shaking description with no identified occurrence or sufficient temporal/event attribution under `STANDARD/009-EVENT.md`. FEMA/Ready.gov source is general safety guidance, not a report of a specific occurrence. Recommended owner path: preserve Event and `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2` unchanged on HOLD and exclude from first-edition release scope unless a specific occurrence source is supplied.
- Water storage: both State participants in `REL-CONTAINER-WATER-STORAGE@1` refer to `OBJ-WATER-CONTAINER@1`; the second participant is not a State of a separately represented water Object. Three owner choices are documented: add an explicit water Object/State, recast the Relation as a supported container-state transition, or preserve and exclude the Relation while it remains HOLD.
- The owner-selected conservative paths are now recorded. Both Relations remain HOLD; no canonical mutation, deletion, allowlist change or release approval was made.

The next action is owner selection of the bounded paths, not autonomous canonical editing.


## Execution checkpoint — owner decisions and exact-head CI diagnosis — 2026-11-20

- Owner confirmed **E-Q1**: preserve `EVT-EARTHQUAKE-SHAKING@1` and `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2` unchanged and HOLD; exclude both from first-edition release scope unless a specific-occurrence source and new bounded authorization are supplied.
- Owner confirmed **W-Q3**: preserve `OBJ-WATER-CONTAINER@1`, both existing State records, `REL-CONTAINER-WATER-STORAGE@1` and its Context unchanged; keep the Relation HOLD and exclude it from first-edition release scope pending a valid model.
- These are owner scope/disposition decisions. No canonical Event, Object, State, Relation, Context, Claim, Source or Evidence Use record was changed. No allowlist was created or modified.
- Exact-head CI at `47f65a506bd13eaa913ba7ce1414c67e11d3714a`: Offline Edition PASS; MVP Contribution Form Browser Tests PASS; Reference implementation tests FAIL (1,002 passed / 4 failed); Release Conformance Gate FAIL (final conformance PARTIAL).
- Failure diagnosis: two adversarial corpus tests incorrectly treated `record_id` alone as unique despite the Standard's versioned-record identity model and exact versioned Source @1/@2 coexistence; a Relation/Context regression hard-coded Context @1 although Library/Archival is now Context @3; the cross-slice audit JSON still reported 4,741 records while the coverage manifest and actual corpus contain 4,742.
- Bounded remediation in this checkpoint updates identity assertions to unique `(record_id, record_version)` pairs, makes the Relation/Context regression resolve the exact version in `frame_ref`, and synchronizes the cross-slice audit count. It does not relax schema or semantic validation.
- The four workflow checks must be rerun on the new exact HEAD. No CI PASS is claimed for the remediation commit until all four complete successfully.


## Execution checkpoint — relation/reference closure and exact-head CI — 2026-11-20

Verified against the current PR #22 branch HEAD `03e58490241904eb572b2980beca97873a9860f8`.

### Completed and verified

- Research Methods / Statistics cross-slice reference remediation is implemented under the two bounded authorizations recorded in `RELEASE/EDITORIAL-CORRECTION.json`.
- `REL-CROSS-M2-STATISTICS-RESEARCH@3` now references `CLM-RESEARCH_METHODS_BASICS-B@2` and `CTX-REL-CROSS-M2-STATISTICS-RESEARCH@2`; the Context points back to Relation @3.
- `REL_M3_SCIENTIFIC_METHOD_RESEARCH@3` now references `CLM-RESEARCH_METHODS_BASICS-B@2` and `CTX-REL_M3_SCIENTIFIC_METHOD_RESEARCH@2`; the Context points back to Relation @3.
- `REL-CROSS-RESEARCH-STATISTICS@3` and `CTX-REL-CROSS-RESEARCH-STATISTICS@2` retain reciprocal exact-version alignment.
- All four records in the two newly aligned Relation/Context pairs were re-fetched at the current branch HEAD. Their record versions, participant versions, frame_ref and reciprocal target_ref are coherent. Relation semantics, roles, provenance, publication/completion states and HOLD decisions were preserved.
- The shared-Context isolation implementation (61 target-specific Contexts and 61 corresponding Relation frame updates) is now covered by the successful current exact-head preflight and full Reference test run. This validates technical conformance; it does not independently approve the semantics or release status of those Relations.
- Current exact-head CI ran against PR merge commit `8fbf2a2f9a2c2f6cba1e7c984b7e9c870fac4a2c`, which checks out PR head `03e58490241904eb572b2980beca97873a9860f8` merged with base `d58289f319993ede5294a46f4741a506fd2fd710`:
  - Offline Edition — PASS; preflight 4,742 records / 479 slices / 19 record types; offline tests 3 passed; edition built and artifact uploaded.
  - MVP Contribution Form Browser Tests — PASS; browser inspection passed.
  - Reference implementation tests — PASS; 1,006 passed.
  - Release Conformance Gate — PASS; `final_conformance_state=CONFORMING`, zero blocking or limiting gates in the report; report artifact uploaded.
- PR #22 remains OPEN / DRAFT / NOT MERGED. `main` remains unchanged. No allowlist, publication, deployment or release approval was created.

### Superseded status

The earlier statement that Research/Statistics exact-version Relation alignment and the shared-Context implementation were awaiting CI validation is superseded by this checkpoint. The earlier failing CI snapshot at `47f65a506bd13eaa913ba7ce1414c67e11d3714a` is historical and is not the current branch status.

### Next execution sequence

1. Continue exact reconciliation of the remaining bounded authorizations against current canonical records; do not infer completion from a Source version or a passing global preflight alone.
2. Continue the 15 semantic-HOLD Relation remediation queue only where an exact endpoint, Evidence Use support and applicable rights basis are verified and the corresponding bounded authorization exists. The emergency/infrastructure alternative remains a research proposal pending its own authorization; Library/Archival alignment is already implemented and must not be repeated.
3. Keep the earthquake Event and water-storage State/Relation models unchanged and excluded as owner-directed; do not reopen their decisions without new evidence and authorization.
4. Continue WP2 R-01–R-10 and item-level rights review. All screened candidates remain HOLD; technical conformance is not rights clearance or editorial approval.
5. Continue WP1 candidate closure and exact-version register reconciliation within the approved first-edition map; do not expand to the 261 map-external Part II slices without explicit scope approval.
6. Any subsequent canonical or release-document commit requires all four workflows to be rechecked on one immutable final PR HEAD. Preserve Draft/unmerged status and keep `main` unchanged.


## Execution checkpoint — current-head Relation, Part II register and CI reconciliation — 2026-11-20

Inspection baseline for canonical checks: PR HEAD `9a933f272f2124a7748ab0d184de465e84bddee4`. Three later commits add only chief-engineer reports; compare from that baseline confirms exactly three added report files and no canonical/implementation paths changed.

### Exact-head CI

All four required workflows completed SUCCESS on the same canonical/implementation HEAD `9a933f272f2124a7748ab0d184de465e84bddee4`:
- Reference implementation tests — PASS.
- Release Conformance Gate — PASS.
- Offline Edition — PASS.
- MVP Contribution Form Browser Tests — PASS.

The three subsequent documentation-only report commits have no workflow runs returned by the commit-workflow query. Therefore the 4/4 PASS is attributed to `9a933f2`, not misrepresented as a newly executed CI result on the later documentation-only tip. No canonical or implementation files changed after the tested HEAD.

### Superseding Relation status

A current-head read-only reconciliation re-fetched all 15 semantic-HOLD Relation records and their referenced Contexts:
- 14/15 Relation-specific Context target cycles resolve to the exact current Relation version.
- The only exception is `REL-CONTAINER-WATER-STORAGE@1`, whose Context still targets a Claim; this remains the owner-directed W-Q3 HOLD/exclusion and must not be mutated.
- The earthquake Relation @2 has its own exact Relation-specific Context @1 → Relation @2. Its separate Event Context/Scope model issue remains covered by E-Q1; preserve and exclude as directed.
- `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@6` is now aligned to Library Science C@2 and Archival Science A@2 with Context @3. Its endpoint-specific semantic mismatch is superseded; rights, editorial and Human View gates remain open.
- `REL_M3_EMERGENCY_INFRASTRUCTURE@3` is now aligned to Emergency Management A@1 and Infrastructure Resilience D@2 with Context @2 and UNDRR @1 / CISA @2 provenance. This is the exact previously authorized bounded correction; preserve HOLD.
- `REL-CROSS-M2-STATISTICS-RESEARCH@3`, `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`, and `REL-CROSS-RESEARCH-STATISTICS@3` have their current endpoint/version alignments recorded, but semantic and/or evidence review remains open as specified in the current-head Relation reconciliation report.
- The remaining CO, Air/Power, AMR/Plant, Groundwater/Soil, Food/Public Health, PlantPath/Entomology, Quantum/Measurement and Settlement/Public Health findings remain HOLD.

See `reports/agent-work/chief-engineer/current-head-reconciliation-of-15-semantic-hold-relations-2026-11-20.md` and `reports/agent-work/chief-engineer/exact-head-ci-and-emergency-infrastructure-relation-checkpoint-2026-11-20.md`. These reports supersede stale @1/@2/@3 intermediate version references in the earlier 2026-11-19 remediation descriptions only for the exact records they identify.

### Part II master integrity

The Part II exact-version Markdown master was structurally rechecked:
- 1,130 exact-version rows; 1,130 unique compound `record_id@version` keys; zero duplicates.
- 1,058 candidate keys + 72 dependency records.
- 124/385 Part II slices represented; 261 map-external slices remain outside the bounded scope.
- Record types: 352 Claims, 400 Evidence Use, 163 Sources, 107 Contexts, 108 Scopes.
- 1,130/1,130 decisions are HOLD; zero INCLUDE and zero EXCLUDE.
- 30 known current Claims across 14 slices remain outside the candidate denominator pending scope triage.

This is a register-table integrity result, not canonical JSON certification or complete dependency closure. See `reports/agent-work/chief-engineer/part-ii-exact-version-master-structural-integrity-recheck-2026-11-20.md`.

### Updated next execution sequence

1. Do not repeat closed Relation semantic reviews, the Library/Archival alignment, Emergency/Infrastructure alignment, E-Q1 or W-Q3.
2. Continue targeted evidence/semantic review of AMR/Plant, Research/Statistics, Migration/Labor and the remaining semantic HOLD pairs. No endpoint or Claim changes without a matching bounded authorization.
3. Keep all 15 Relations HOLD; the corrected endpoint pairs are not release approvals.
4. Continue WP2 item-level rights work and obtain owner decisions R-01–R-10. All ten remain OPEN; do not invent a rights holder, licence, editor, approver or contact.
5. Continue WP1 dependency closure within the approved first-edition map. Do not add the 30 out-of-master Claims or 261 map-external slices without scope authorization.
6. WP3 remains integration/release preparation only: no rebase, merge, deployment, allowlist or public release without separate owner authorization and a new exact-head review.

### Boundaries reaffirmed

PR #22 remains OPEN / DRAFT / NOT MERGED. `main` remains at `d58289f319993ede5294a46f4741a506fd2fd710`. No canonical Content, implementation, candidate membership, allowlist, publication state or owner decision was changed by this checkpoint.


## Execution checkpoint — targeted Relation evidence and rights update — 2026-11-20

Inspection baseline for canonical records: PR HEAD `c177cbf0def595b4d478d0eddb512db5b33c18d4`. Three new/updated documents on the branch are documentation-only; no canonical records or implementation paths changed.

### WP1 — new evidence findings

- **AMR / Plant Health @2:** FAO's official plant-health AMR page directly describes resistance of plant pathogens to antimicrobials used as pesticides and plant-production contributions to AMR in human/animal pathogens. WHO's 16 July 2026 fact sheet independently describes plant-health and farm-productivity impacts. This supersedes “no direct mechanism found” but does not close the canonical evidence gap: FAO is not yet represented in the current canonical evidence path, and Plant Pathology A@1 remains a general discipline definition. HOLD.
- **Research / Statistics @3:** National Academies Chapter 2 (pp. 27–29) directly discusses statistical inference within scientific methods/knowledge, while NIST §3.1.3.4 supports sample/population inference. This is a high-confidence contextual-navigation candidate, pending independent boundary review. HOLD.
- **Migration / Labour @4:** ILO's June 2026 practical guide directly integrates migration and labour-market statistics. Useful exact locators include printed pp. 10–12, 22–27, 30–33, 34–38, 43, 57–58 and 63–66. It covers migration stocks/flows, labour-force status, employment, wages, hours and underutilization, but does not establish that productivity is automatically comparable for migrant groups. Strong direct source candidate; canonical source/provenance linkage and independent review remain open. HOLD.

See `reports/agent-work/chief-engineer/targeted-cross-slice-relation-evidence-and-rights-audit-2026-11-20.md` and the updated `FIRST-EDITION-RELATION-SEMANTIC-HOLD-REMEDIATION-REGISTER-2026-11-19.md`.

### WP2 — source-rights follow-up

- FAO web content: non-commercial use with attribution is permitted within its terms; adaptation/translation and resale/commercial use require permission; third-party components separately cleared.
- National Academies Press: all-rights-reserved; PDF distribution/copying requires written permission; expressive reuse requires rights review.
- ILO 2026 Guide: exact work-level CC BY 4.0 at printed p. ii, with attribution/change indication and third-party exclusions.
- WHO AMR fact sheet: exact work-level copyright notice and third-party material still need verification before expressive reuse; general WHO publication policy is not blanket commercial permission.

See updated `FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md`. R-01–R-10 remain OPEN; no project licence or owner role has been inferred.

### Required sequence

1. Obtain separate bounded authorization before adding FAO/ILO Source records, Evidence Use locators or Relation provenance references.
2. Have an independent reviewer confirm Research/Statistics boundary and Migration/Labour integrated-measurement link.
3. Keep all three Relations and affected slices HOLD pending semantic, rights, editorial and Human View gates.
4. Continue WP1 exact dependency closure within the bounded map; continue WP2 source-specific rights review and owner decisions; keep WP3 release work private and non-publishing.
5. No canonical mutation, allowlist, INCLUDE/EXCLUDE, preview publication, deployment, merge or main-branch change was made.

PR #22 remains OPEN / DRAFT / NOT MERGED. The last 4/4 exact-head CI PASS remains attributed to canonical/implementation HEAD `9a933f272f2124a7748ab0d184de465e84bddee4`; subsequent branch changes documented here are documentation-only and do not claim a new exact-head CI run.


## Execution checkpoint — Labour Economics ILO Path B verification — 2026-11-20

The prior 2026-11-19 OpenStax decision packet stated that the owner had not yet selected Path A/B/C. That status is superseded for `labor-economics-basics`: the owner selected **ILO Path B** on 2026-11-20 and the bounded authorization is recorded in `RELEASE/EDITORIAL-CORRECTION.json`.

Read-only verification at canonical baseline HEAD `c177cbf0def595b4d478d0eddb512db5b33c18d4` confirms:
- 13/13 authorized Labour Economics records are current @2: 2 Sources, 3 Claims, 6 Evidence Use, 1 Context, 1 Scope.
- All primary Evidence Use records @2 resolve to the exact Claim @2 and ILOSTAT Source @2; all independent Evidence Use records @2 resolve to the exact Claim @2 and WESO Source @2.
- Context and Scope @2 target Claim A@2.
- The two explicitly named dependent Relations are @4 and both relation-specific Context @1 records target the exact Relation @4.
- The current ILOSTAT Source @2 explicitly does not assert CC BY 4.0 for its referenced pages because item-level publication dates/licences are not established. The WESO 2023 independent report has an explicit CC BY 4.0 notice in its own PDF, with third-party assets excluded.

The OpenStax-specific blocker is superseded for this Labour Economics source chain. The ILOSTAT item-level rights question and project distribution compatibility remain open. Labour Economics and both Relations remain HOLD.

Verification: `reports/agent-work/chief-engineer/r7-labour-economics-ilo-path-b-exact-record-and-rights-verification-2026-11-20.md`. The historical decision packet is superseded in its final section and must not be read as the current pending owner decision.

The separate ILO 2026 migration/labour measurement guide is a promising additional source for `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`, but is not part of the 13-record Path B authorization and is not in the canonical graph. Adding it requires separate bounded authorization. The existing direct Claim provenance for the two dependent Labour Relations was expressly included in the owner-approved Path B authorization; this specific pattern is not an unapproved change.

No canonical record changed in this verification. No candidate disposition, allowlist, publication state, merge, deployment or main-branch state changed.


## Execution checkpoint — FAO / ILO evidence verification and exact-head CI — 2026-11-20

Canonical and implementation baseline: PR branch HEAD `0386a0ebaadcf023c9ec03438c5b153d79e67f95`.

### Completed

- Re-fetched the exact FAO Source @1, AMR/Plant Health Relation @3 and its Context @2. Relation @3 → Context @2 → Relation @3 is reciprocal; the original Claim participants, order, type, roles and direction remain unchanged.
- Re-fetched the exact ILO Guide Source @1 and both additive Evidence Use @1 records. Both resolve to the intended existing Claims @2 and Source @1.
- Re-fetched Migration/Labour Relation @4 and Context @1; the Context targets Relation @4 exactly. Existing UNSD and ILOSTAT Evidence Use @2 records remain intact.
- Verified the ILO Guide's work-level CC BY 4.0 notice on printed p. ii and confirmed the exact migration, labour-force and migrant-indicator printed-page locators against the official PDF.
- Completed a bounded semantic desk review: FAO supports the AMR/plant-health Relation as contextual navigation only; the ILO Guide supports the migration/labour measurement intersection, while productivity comparability remains outside its asserted support and the ILOSTAT path remains necessary.
- Durable report: `reports/agent-work/chief-engineer/fao-ilo-current-head-evidence-and-semantic-desk-review-2026-11-20.md`.

### Exact-head CI

All four required workflows passed on the same immutable canonical/implementation HEAD `0386a0ebaadcf023c9ec03438c5b153d79e67f95`:
- Offline Edition — PASS (run 44737912286).
- MVP Contribution Form Browser Tests — PASS (run 44737912271).
- Reference implementation tests — PASS (run 44737912270).
- Release Conformance Gate — PASS (run 44737912273).

A later report-only commit `565b75e46d5d90b06306f165bbd49e4587e1b0ae` adds the desk-review report. No workflow runs were returned for that documentation-only commit. Do not misattribute the 4/4 result to `565b75e`; the tested canonical/implementation baseline is `0386a0e`.

### Disposition and next work

- FAO/AMR–Plant Health and Migration/Labour remain HOLD. The desk review is not independent subject-matter approval, rights clearance, Human View or release approval.
- ILO Guide CC BY 4.0 does not transfer to ILOSTAT pages; item-level ILOSTAT rights and project-level distribution compatibility remain open.
- R-01–R-10 remain owner decisions; no licence, rights holder, editor, release approver or public contact is inferred.
- Continue targeted WP1 closure within the approved map and the remaining semantic-HOLD Relation queue. Do not repeat the FAO/ILO implementation, the closed exact-head CI diagnosis, E-Q1, W-Q3, Library/Archival alignment or Emergency/Infrastructure alignment.
- Keep all affected records and Relations HOLD; no allowlist, INCLUDE/EXCLUDE, merge, deployment or publication is authorized.
- PR #22 remains OPEN / DRAFT / NOT MERGED. `main` remains `d58289f319993ede5294a46f4741a506fd2fd710`.


## Execution checkpoint — Plant Pathology / Entomology and Quantum / Measurement evidence follow-up — 2026-11-20

Inspection baseline: PR branch HEAD `cdf8d0b132fd1b5de3b76e23fdd4bf05cf205f6c`.

### New report-only findings

- `REL-CROSS-PLANTPATH-ENTOMOLOGY@2` and Context @1 have an exact reciprocal reference cycle. Current A/A participant Claims remain generic discipline definitions and both EUs lack pinpoint locators. Official APS material documents insect vectors of plant viruses; ESA describes crop damage, pollination and agricultural entomology. This strengthens the case for contextual navigation but does not authorize a Source/EU/endpoint change. HOLD.
- `REL-CROSS-QUANTUM-MEASUREMENT@2` and Context @1 have an exact reciprocal reference cycle. The current NIST Source @1 URI `https://www.nist.gov/topics/quantum-information-science` returns 404. NIST's current Quantum Information Science page at `https://www.nist.gov/quantum-information-science` directly discusses quantum sensors, precision measurements and quantum measurement standards. The current quantum and BIPM Evidence Use descriptions lack pinpoint locators. A Source version / dependent-reference correction requires separate bounded authorization. HOLD.
- Durable report: `reports/agent-work/chief-engineer/plantpath-entomology-and-quantum-measurement-relation-followup-2026-11-20.md`.

### Next bounded WP1 actions

1. Request exact bounded owner authorization for the Plant Pathology / Entomology evidence route; do not infer whether the correct route is Relation-level evidence, Claim-level Evidence Use or endpoint revision.
2. Request exact bounded owner authorization for the Quantum / Measurement stale NIST Source URI and locator remediation.
3. Obtain independent subject-matter review for both Relations.
4. Continue remaining semantic-HOLD Relation review and exact Claim → Evidence Use → Source dependency closure within the approved map.
5. Keep both Relations and all affected slices HOLD; no allowlist, INCLUDE/EXCLUDE, publication, merge or deployment is authorized.

This checkpoint is research/report-only. No canonical Content or implementation files changed. The exact-head 4/4 CI result remains attributed to HEAD `0386a0ebaadcf023c9ec03438c5b153d79e67f95`; the subsequent report and board commits are documentation-only and have no new workflow runs. PR #22 remains Draft/unmerged; `main` remains `d58289f319993ede5294a46f4741a506fd2fd710`.


## Execution checkpoint — CO heating / generator emergency-escalation Relation — 2026-11-20

- Re-fetched `REL-CROSS-CO-EMERGENCY-ESCALATION@2`, its Relation-specific Context @1, both endpoint Claims @1, both Evidence Uses @1 and both official Sources @1 at branch HEAD `302f1082f0b9de08b71553a80f59dbc9682c9a55`.
- Relation @2 ↔ Context @1 is an exact reciprocal cycle. The endpoint Claims substantially overlap in their immediate protective action (fresh air, emergency/medical help, no re-entry before safety confirmation); their distinct navigation value is general residential CO alarm response vs generator/outage exposure context.
- Current EUs contain narrative summaries but no pinpoint locators. CPSC's current CO guidance directly supports alarm response; CDC/NIOSH supports fresh air and immediate medical help for symptoms. Generator-specific locator-level support and independent emergency/clinical boundary review remain open.
- Durable report: `reports/agent-work/chief-engineer/co-heating-generator-emergency-relation-desk-review-2026-11-20.md`.
- Disposition: Relation, Context, both Claims, EUs, Sources and slices remain HOLD. No canonical records, versions, claims, provenance, publication states or allowlists changed. This is a report-only review; no CI PASS is claimed for the docs-only commit.

### Next bounded sequence

1. Continue report-only evidence/semantic review of Air/Power, Groundwater/Soil, Food/Public Health and Settlement/Public Health without reopening closed audits.
2. Keep the CO Relation as a navigation candidate only pending independent review and exact CDC locator confirmation; do not collapse or rewrite overlapping Claims without authorization.
3. Continue WP2 item-level rights and owner decisions R-01–R-10; continue WP1 exact dependency closure within the approved map.
4. Preserve PR #22 Draft/unmerged and `main` unchanged. Recheck exact-head CI after canonical/implementation changes; documentation-only commits must not inherit earlier CI claims.


### Additional Relation review — Air Quality / Power Systems — 2026-11-20

- Re-fetched Relation @2, exact Context @1, both participant Claims @1, both Evidence Uses @1 and both Sources @1 at inspection HEAD `302f1082f0b9de08b71553a80f59dbc9682c9a55`.
- The endpoint Claims independently describe ambient-air monitoring and the generic electricity-system chain (generation/transmission/distribution/load). The pair does not currently state a demonstrated cross-domain mechanism. EPA distinguishes ambient concentration monitoring from power-sector emissions/operations data; that broader relationship does not by itself prove the current Relation's endpoint pairing.
- Plausible future routes (not authorized): power-sector emissions ↔ ambient air quality, or electricity dependency ↔ monitoring infrastructure. Each requires an explicit endpoint Claim and direct source support.
- Durable report: `reports/agent-work/chief-engineer/air-quality-power-systems-relation-desk-review-2026-11-20.md`.
- Disposition: all records and slices remain HOLD; no canonical changes or release decisions. Report-only; no CI PASS claimed for docs-only commits.


### Additional Relation review — Groundwater / Soil Microbiology — 2026-11-20

- Re-fetched Relation @2, exact Context @1, both endpoint Claims @1, EUs @1 and Sources @1 at inspection HEAD `302f1082f0b9de08b71553a80f59dbc9682c9a55`.
- New direct USGS evidence establishes the cross-domain mechanism: soil microorganisms affect water chemistry during infiltration, while microbial processes also alter groundwater chemistry and aquifer hydraulic properties. This supports a genuine hydrogeology/microbial ecology navigation link, beyond simple domain adjacency.
- Boundary: distinguish soil-zone microbial effects during recharge from microbial communities/processes inside aquifers; do not imply all soil microbes enter groundwater or that microbial activity guarantees safe drinking water.
- Durable report: `reports/agent-work/chief-engineer/groundwater-soil-microbiology-relation-evidence-review-2026-11-20.md`.
- Disposition: strong contextual-navigation candidate, still HOLD. The newly found USGS bridge source is not yet in the canonical graph; Source/Evidence Use addition, locator and rights/attribution checks require bounded authorization. Independent hydrogeology/microbial ecology review and Human View remain open. No canonical changes or CI PASS claimed.


## Execution checkpoint — Food/Public Health and Settlement/Public Health Relation reviews — 2026-11-20

Inspection baseline for canonical records: PR HEAD `97d5b08b520c2bd785ed1a1b12a808a70ebb1dbc`. The two new reports and this board update are documentation-only.

### Food Security / Public Health

- Re-fetched Relation @2, exact Context @1, household food-security Claim D@1 / EU D@1 / USDA ERS Source @1, and public-health Claim A@1 / EU A@1 / WHO public-health Source @1.
- WHO's 4 June 2026 Food Safety fact sheet directly links food security, nutrition and health; it documents foodborne disease burden and the role of national food-control systems and surveillance. This provides a strong Relation-level bridge, while the existing endpoint EUs remain broad and lack pinpoint locators.
- Scope boundary: the current food endpoint is a household food-access definition; the new WHO source supports the broader cross-domain relation but does not establish that every food-insecurity condition causes a specific disease.
- WHO website terms and publication licensing are distinct. No CC licence is inferred for the fact-sheet web page; non-commercial/commercial reuse and substantial reproduction require item-level rights assessment.
- Durable report: `reports/agent-work/chief-engineer/food-security-public-health-relation-evidence-review-2026-11-20.md`.
- Disposition: strong contextual-navigation candidate, still HOLD; WHO Source/Evidence Use addition requires bounded authorization, independent food-safety/public-health review, rights review and Human View.

### Human Settlement Systems / Public Health

- Re-fetched Relation @2, exact Context @1, settlement Claim C@1 / EU C@1 / OECD Source @1, and public-health Claim A@1 / EU A@1 / WHO Source @1.
- WHO urban-health sources directly connect housing, transport, energy, spatial planning, water/sanitation, waste management and built-environment conditions with population health and health inequities. This is a strong systems-level Relation bridge.
- Traceability issue recorded: Relation provenance lists UN Human Settlements Source @1, while the actual settlement endpoint Claim C and its EU point to OECD Source @1. This may reflect broader Relation framing, but the current provenance chain is not a mirror of the endpoint Claim/EU chain. Do not silently rewrite it.
- WHO website-page terms and UN website copyright do not establish a broad reusable licence. OECD item-level terms and project distribution compatibility also remain open.
- Durable report: `reports/agent-work/chief-engineer/settlement-public-health-relation-evidence-review-2026-11-20.md`.
- Disposition: strong contextual-navigation candidate, still HOLD; authorize a WHO urban-health Relation-level evidence path and separately resolve the UN/OECD provenance question before any canonical changes.

### Current status and next actions

1. Both Relations and all endpoint records/slices remain HOLD. No canonical JSON, Source/EU, provenance, publication state, allowlist or release scope was changed.
2. Prepare exact bounded authorization proposals for the Food/Public Health WHO bridge and Settlement/Public Health WHO bridge, including item-level rights and exact locators; keep the Settlement UN/OECD provenance question separate.
3. Continue the remaining unreviewed semantic-HOLD queue, then consolidate authorization requests rather than making speculative endpoint or provenance edits.
4. Continue WP2 R-01–R-10 and item-level rights review. The WHO web-page restrictions are not a project-wide licence decision.
5. PR #22 remains OPEN / DRAFT / NOT MERGED; `main` remains unchanged. These are documentation-only commits; no CI PASS is claimed for their new HEAD.


### Consolidated bounded authorization packet prepared — 2026-11-20

Created `RELEASE/OWNER-AUTHORIZATION-REQUEST-RELATION-EVIDENCE-PROVENANCE-2026-11-20.md`.

It requests independent, exact-scope owner decisions for:
- A. Groundwater / Soil Microbiology: add one USGS groundwater–microbial-processes Source @1; version Relation @2→@3 and Context @1→@2; preserve both endpoint Claims and all Relation semantics.
- B. Food Security / Public Health: add one WHO Food Safety Source @1; version Relation @2→@3 and Context @1→@2; preserve both endpoint Claims and all Relation semantics.
- C. Settlement / Public Health: add one WHO urban-health Source @1; version Relation @2→@3 and Context @1→@2; resolve the UN/OECD provenance traceability issue through explicit option C1 (add existing OECD Source @1 plus WHO Source @1) or C2 (add only WHO Source and defer the UN/OECD question).

The packet explicitly prohibits endpoint/Claim/Evidence Use changes, INCLUDE/EXCLUDE, allowlist changes, publication, deployment, merge or main-branch changes. Each Relation remains HOLD after any approved provenance addition. Rights and independent expert/Human View gates remain separate. No authorization is assumed and no canonical changes have been made.

### Current execution sequence

1. Await only the bounded owner decision for the three optional Relation-level provenance additions; continue report-only review elsewhere.
2. Continue unresolved semantic-HOLD work without repeating completed audits; keep Air/Power as mismatch, CO emergency as overlap/navigation-only, and the owner-directed E-Q1/W-Q3 exclusions unchanged.
3. Continue WP2 R-01–R-10 and item-level rights verification.
4. Recheck exact-head CI after any canonical changes; documentation-only commits do not inherit CI PASS.


### WP2 — WHO page-level rights distinction recorded — 2026-11-20

- Added §10 to `FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md` and indexed it in the R-01–R-10 owner decision register.
- The proposed WHO Food Safety fact sheet and WHO urban-health page are web pages; WHO's general publication CC BY-NC-SA 3.0 IGO policy is not automatically assigned to either page. Website terms restrict sale/commercial use and require prior written authorization for substantial reproduction or uses outside educational/non-commercial purposes.
- Proposed canonical use remains limited to source identity, locators and independently worded factual paraphrase; no WHO text, images or tables are copied.
- R-01–R-10 remain OPEN. Both Relations remain HOLD. No rights clearance, permission or licence decision is inferred.


## Execution checkpoint — 2026-11-20, current PR head reconciliation

This checkpoint supersedes earlier “current/latest HEAD” and pending-CI statements above where they refer to an older inspection.

### WP1 — first-edition candidate selection and dependency closure
- The five Part II slices in Batch 2 (Ancient Civilizations, Anthropology, Linguistics, Philosophy, Ethics) were already screened in Batch 2; the 2026-11-20 work was a current-head revalidation of 47/47 exact record files, not a first-time audit. All five remain HOLD.
- The Archival Science owner explicitly ratified only the existing exact dependency `SRC-ARCHIVAL_SCIENCE-ICA@1 → CLM-ARCHIVAL_SCIENCE-C@2 → EU-ARCHIVAL_SCIENCE-C@2`. The README and R9 rights screen now reflect that the narrow authorization/provenance mismatch is closed. No canonical JSON changed; Archival Science remains HOLD pending project-level rights compatibility, independent archival editorial review, privacy/donor/access and cultural-protocol review, and Human View.
- Settlement Geography's owner-approved Eurostat remediation is already implemented and registered: nine slice records @2 and dependent Cartography Relation @3 with only the two authorized endpoint references advanced. Both affected slices/Relation remain HOLD.
- The 15 semantic-HOLD Relation decisions remain HOLD; no INCLUDE or allowlist was created. The 261 map-external slices remain outside the bounded map screen.

### WP2 — rights, attribution and accountable operations
- R-01–R-10 remain OPEN. No project content licence, software licence, rights holder, editor, release approver, contributor terms or public correction contact has been selected by this work.
- Source-specific screens are evidence records, not legal clearance. The Archival Science ratification does not widen ICA's attribution-conditioned reproduction permission or resolve SAA restrictions and project-level distribution compatibility.

### WP3 — offline builder and exact-head CI
- The selection-aware offline builder and its synthetic fail-closed tests are implemented in PR #22. The additional CLI test commit is `350961c332346f2e3621f01893fee278a5448f67`.
- The subsequent two commits update only the Archival Science README and R9 rights screen; compare from the CLI-test commit to `933f10af037bb50f84feb5d3a6062f8490ba7054` shows exactly those two documentation paths.
- At exact HEAD `933f10af037bb50f84feb5d3a6062f8490ba7054`, the latest observed required workflow state is:
  - Offline Edition — PASS
  - MVP Contribution Form Browser Tests — PASS
  - Release Conformance Gate — PASS
  - Reference implementation tests — IN PROGRESS
- This is 3/4 completed PASS with one workflow still running, not a full exact-head CI PASS. Re-poll this exact SHA and rerun all required gates after any further commit.
- PR #22 remains OPEN / DRAFT / UNMERGED; base `main` SHA remains `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`. No merge, deployment, publication, allowlist or release action was performed.

### Next execution order
1. Finish/poll Reference implementation tests on the exact current HEAD; inspect logs if it fails.
2. If all four checks pass, record technical conformance only; keep PR #22 Draft and unmerged.
3. Continue only the next explicitly authorized WP1 record/dependency work; do not repeat closed screens or expand to the 261 out-of-map slices.
4. Keep WP2 owner decisions open until the owner makes them explicitly; technical work cannot close them.
5. Re-run all four checks on one immutable exact HEAD after any additional change.


## Execution checkpoint — bounded foundational candidate closure — 2026-11-23

Read-only exact-version candidate package: [First Edition — Bounded Foundational Candidate Closure and Next Release Queue](FIRST-EDITION-BOUNDED-FOUNDATIONAL-CANDIDATE-CLOSURE-AND-QUEUE-2026-11-23.md).

- SI units is the strongest existing private-review candidate: exact seven-record Claim/EU/Source/Context/Scope closure re-fetched; EU v2 pinpoints and boundaries verified; Claim-A-only Context/Scope target preserved; existing private preview builder and browser suite reused. **HOLD remains** because the preview authorization is private/non-redistributable, independent three-reader review is not run, and project rights/editorial owner decisions remain open.
- Climate basics Claim A: exact five-record subgraph re-fetched; NASA locator research exists, but canonical EU v1 remains generic and needs a bounded versioned remediation authorization. **HOLD**.
- Measurement uncertainty Claim A: exact five-record subgraph re-fetched; NIST TN 1297 §2.1/§7 research exists, but legacy/current guidance boundary and the complete slice's additional BIPM track require closure. **HOLD**.
- Queue order: SI private preview → climate Claim A → measurement-uncertainty Claim A → statistics → motion/cell. High-consequence water/fire/electrical/chemical/sanitation procedures remain outside the fast-track pending qualified review.
- No canonical JSON, candidate disposition, allowlist, rights decision, publication state or main-branch file changed.
- No new INCLUDE is assigned. R-01–R-10 remain owner decisions.


## Execution checkpoint — 19-chapter editorial architecture — 2026-11-23

### Completed

Added `RELEASE/FIRST-EDITION-19-CHAPTER-EDITORIAL-TOC-AND-READER-STRUCTURE-2026-11-23.md`.

The document fixes the first-edition reader architecture as two parts and 19 numbered chapters:
- Part I, Chapters 1–10: emergency response; water; food; shelter/construction; health/hygiene/sanitation; heat/fire/electricity/energy; tools/materials/repair; agriculture/ecology; natural/environmental hazards; communication/navigation/transport/logistics.
- Part II, Chapters 11–19: mathematics/measurement; physical sciences; chemistry; life sciences; Earth/climate/space; engineering/computing; human sciences; society/institutions; history/culture.

Each chapter now has a numbered subsection outline, explicit high-consequence/editorial boundaries, and cross-chapter reading pathways. The document defines how partially populated chapters may be presented without implying that an unreviewed topic is available or complete.

### Change-control boundary

This is a reader/editorial structure, not a record selection. It does not alter canonical JSON, Claim wording, exact-version candidate denominators, Context/Scope applicability, Relations, publication states, rights, or the allowlist. No INCLUDE decision is inferred. HOLD remains HOLD.

### Exact-head technical verification

- Before this documentation commit, PR #22 HEAD `e656620fe7910d099fae6de9f8f933f89922b4c8` had all four required workflows complete successfully: Reference implementation tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests.
- The Release Conformance Gate run `45169717227` completed successfully after the initial poll.
- This editorial document commit advanced the branch to `0c28d8612da8fa5bb2206cd0d638486b33584ed7`. The prior four successes do not automatically certify this newer HEAD; exact-head checks must be reconciled again.

### Next package

1. Map each of the 19 chapters against the current Part I and Part II exact-version registers, distinguishing candidate records, HOLD, missing dependencies and unrepresented subtopics.
2. Select a bounded first-edition set from both parts; do not require full coverage of every subsection.
3. Prepare only authorized, versioned evidence/locator remediation; keep substantive Claim changes and rights-sensitive graph changes separate.
4. Close project-level owner decisions R-01–R-10 before any public INCLUDE manifest or release.
5. Build and inspect the production reader and offline artifact only against the eventual approved exact-version manifest.

PR #22 remains OPEN / DRAFT / NOT MERGED. No publication, deployment, merge or `main` change was performed.


## Execution checkpoint — 19-chapter candidate-to-slice mapping — 2026-11-23

### Completed

Added `RELEASE/FIRST-EDITION-19-CHAPTER-CANDIDATE-SLICE-MAPPING-AND-COVERAGE-2026-11-23.md`.

The mapping:
- connects all ten Survival chapters to the existing opening-section candidate slice map;
- extracts the 124 distinct topical Part II slice IDs from the exact-version master, excluding the service-only `cross-slice-linkage` label;
- assigns every Part II slice one primary chapter across the nine Part II chapters or an explicit cross-part entry point in Survival Chapters 1, 3, 8 or 10;
- preserves one primary slice identity even where the reader may expose more than one navigation route;
- states the current exact-version table composition: 1,146 unique record/version rows (352 Claims, 408 Evidence Uses, 171 Sources, 107 Contexts, 108 Scopes), all HOLD;
- preserves the Part I structural inventory of 94/94 slices and 980/980 screened record files without treating screening as publication approval.

The Part II mapping checksum is 118 primary entries in Chapters 11–19 plus six Part II-inventory slices whose reader entry point belongs in Part I, for 124 unique Part II slice IDs. The separate `cross-slice-linkage` label is not counted as a topic.

### Important interpretation

This is a candidate coverage map, not a statement that every mapped slice is publishable or must appear in the first release. The first edition may show a chapter with only a few verified entries and clearly marked unavailable subtopics. All current Part II master rows remain HOLD; no production INCLUDE manifest exists.

### Exact-head status

- The mapping document was committed as `986bb0a858241121584d5f3f21faec5d9e5e3cc7`.
- GitHub returned no PR-triggered workflow runs for this documentation-only commit. No CI result is claimed for this HEAD.
- The previous exact HEAD `e656620fe7910d099fae6de9f8f933f89922b4c8` had all four required workflows complete successfully, including Release Conformance Gate run `45169717227`. Those results do not certify the newer documentation HEAD.

### Next execution package

1. Build a compact, evidence-led first-edition candidate shortlist across both parts, reusing existing completed reviews and current exact-version records.
2. For each shortlisted Claim, verify the exact Claim → Evidence Use → Source chain, Context/Scope applicability, consequence level and source-specific rights status.
3. Separate low-consequence explanatory candidates from high-consequence procedures and rights-incompatible material.
4. Prepare bounded owner/editor decisions only where an actual decision is necessary; do not create INCLUDE by recommendation.
5. Keep the 19-chapter reader structure stable while freezing only the exact records that pass all publication gates.

No canonical JSON, candidate decision, rights decision, publication state, allowlist, coverage manifest, merge, deployment or main-branch file changed.


## Execution checkpoint — representative Claim shortlist across 19 chapters — 2026-11-23

### Completed

Added `RELEASE/FIRST-EDITION-19-CHAPTER-REPRESENTATIVE-CLAIM-CANDIDATE-SHORTLIST-2026-11-23.md`.

A first representative Claim was identified for each of the 19 reader chapters. Exact current Claim/Evidence Use/Source versions were re-fetched for the selected examples. The shortlist explicitly distinguishes:
- candidates with substantive, claim-specific evidence descriptions (e.g. emergency alerts v2; SI units Claim A / EU v2; PostgreSQL databases v3);
- low-consequence candidates whose Evidence Use still needs exact source pinpoints (e.g. food security, shelter, weather, soil, maps, learning);
- candidates with substantive, source-fit or rights blockers (e.g. water resources, cell biology, economics, ancient civilizations);
- high-consequence topics that cannot be accelerated without qualified review.

The hand-hygiene candidate was checked against both its CDC-linked Evidence Use and the additional WHO Evidence Use. The SI Context/Scope and the database Context/Scope target boundaries were re-read and preserved. The shortlist does not infer that a whole slice is ready because one Claim has a promising chain.

### Candidate priority lanes

- **Package A:** SI private preview only; databases Claim A; emergency hand hygiene; emergency alerts; food security Claim A; weather Claim A.
- **Package B:** motion A, materials A, soil A, maps A, energy A, shelter A, Earth-system A, learning A.
- **Package C / retain HOLD:** water-resources A, mixtures-and-solutions A pending visible locator, cell A pending OpenStax rights/AI-ingestion resolution, economics A pending source-fit correction, ancient-civilizations A pending full multi-EU review.

These are work priorities only, not truth rankings or publication decisions. All 19 candidates remain HOLD. No canonical JSON, Claim/EU/Source version, candidate disposition, project licence, owner decision, allowlist or production manifest changed.

### Current exact-head status

The shortlist commit is `0df299643eb25af04436fa6d4f06eccc77c54808`. The immediately preceding mapping commit had no PR-triggered workflow runs; the shortlist is also documentation-only. No exact-head CI PASS is claimed for the current documentation HEAD. The four workflow successes recorded for `e656620...` remain historical to that exact SHA only.

### Next package

1. Work Package A in bounded groups, beginning with exact source locator and rights evidence for the strongest low-consequence candidates.
2. Reconcile each proposed edit against existing bounded owner authorizations; apply only changes already authorized.
3. Keep rights-sensitive and substantive Claim rewrites separate from locator-only remediation.
4. Prepare owner decisions R-01–R-10 for the user's explicit adoption; do not invent rights holder, licence, editor, release approver or correction contact.
5. Once the owner decisions and item-level rights gates close, create the actual INCLUDE manifest and build the production reader/offline edition from its immutable exact-version selection.

PR #22 remains OPEN / DRAFT / NOT MERGED. No publication, deployment, merge or main-branch change was performed.


## Execution checkpoint — Package A exact source locators and rights screen — 2026-11-23

### Completed

Added `RELEASE/FIRST-EDITION-PACKAGE-A-EXACT-SOURCE-LOCATOR-AND-RIGHTS-SCREEN-2026-11-23.md`.

Official source locator research was completed for ten representative candidates:
- Red Cross emergency alert preparedness;
- CDC emergency hand hygiene, with the separate WHO corroboration track preserved;
- FAO food-security definition (§1.4);
- NOAA weather definition;
- NIST materials science;
- USDA NRCS soil definition;
- USGS topographic maps/navigation;
- OpenStax Physics §2.1 for reference frames;
- NIST SI Units (existing “Defining Constants” and “Base and Derived Units” locators revalidated);
- PostgreSQL 18.7 documentation §2.2 Concepts.

The package records the precise claim support boundary, versioned remediation target, source-specific rights issue and whether the work can reuse a completed prior audit. Important distinctions preserved:
- the CDC Claim is linked to CDC Evidence Use, while WHO remains a separate corroboration track;
- FAO §1.4 directly supports the food-security definition;
- NOAA directly defines weather by time and geographic location;
- USDA's soil definition includes SSSA/Soil Taxonomy attribution that must not be silently treated as USDA-only content;
- old USGS map PDFs may be archived; current educational pages should be preferred;
- OpenStax Physics terms do not transfer to other OpenStax titles;
- PostgreSQL 18.7 remains version-specific; PostgreSQL 19 was released 19 November 2026;
- NIST materials source URI in canonical v1 appears old and needs a separately authorized versioned Source correction.

### Work priority

1. Databases Claim A — strongest technical candidate, direct PostgreSQL 18.7 §2.2.
2. Emergency hand hygiene — direct CDC support plus WHO corroboration.
3. Food security Claim A — direct FAO §1.4; reuse closed P2 audit.
4. Weather Claim A — direct NOAA definition.
5. Emergency alerts — current Red Cross section directly supports the existing EU v2.
6. Motion Claim A — OpenStax §2.1 directly supports reference frames; keep the separate Claim B terminology defect visible.
7. Maps, soil and materials — direct official source paths found, but Source/EU and attribution/rights issues remain.
8. SI — no repeated content audit; complete the authorized private preview/review only.

### Authorization and release boundary

No canonical EU/Source/Claim record was changed. No Source URI, record version, disposition, INCLUDE allowlist, licence, owner decision or publication state was altered. Proposed EU/Source corrections require exact bounded authorization; a new Source graph or Claim wording change requires separate authorization. R-01–R-10 remain open.

### Exact-head technical status

The Package A research report commit is `26863a58bde73598eee3b9f8ba705e70c616b681`. It is documentation-only; GitHub returned zero PR-triggered workflow runs for that exact commit. No CI PASS is claimed for this HEAD. The earlier four-workflow success remains limited to `e656620...`.

### Next action

Prepare and apply only the versioned locator/Source corrections that fall within an existing explicit bounded authorization. Keep rights-sensitive, substantive Claim and Source-graph changes in separate approval lanes. Continue to preserve HOLD until all publication gates are closed.


## Execution checkpoint — Packages A–D and first-edition reader shell — 2026-11-23

### Package A — six Claim evidence and rights remediation
Created `RELEASE/FIRST-EDITION-PACKAGE-A-SIX-CLAIM-EVIDENCE-AND-RIGHTS-REMEDIATION-2026-11-23.md`.

Verified source locators and terms for:
- NIST SI Units: “Defining Constants” and “Base and Derived Units”.
- PostgreSQL 18.7 documentation §2.2 “Concepts”; PostgreSQL License.
- CDC emergency handwashing page, “Wash your hands”; CDC public-domain exceptions, attribution, disclaimer and international caveat.
- American Red Cross “Be Informed”; factual support confirmed, reuse/brand permission not cleared.
- FAO handbook §1.4; commercial use/adaptation permission requirements recorded.
- NOAA weather/climate explainer; direct definition of weather as short-term atmospheric state at a location.

All six remain HOLD. This package proposes versioned remediation; it does not edit canonical records.

### Package B — scientific Claim repair and source reuse boundaries
Created `RELEASE/FIRST-EDITION-PACKAGE-B-SCIENCE-CLAIM-REPAIR-AND-REUSE-BOUNDARIES-2026-11-23.md`, with title-specific OpenStax license addendum.

Key findings:
- Motion Claim B still requires an explicit semantic choice: average velocity (displacement/time) or average speed (distance/time). Do not silently rewrite.
- Motion Claim C must retain vector meaning for acceleration.
- Mixtures Claim A has a direct OpenStax Chemistry 2e §11.1 locator; the book is CC BY-NC-SA 4.0 and prohibits LLM/generative-AI ingestion/use without prior written permission.
- Cell Claim A has direct Biology 2e §4.1 support, but the same NC-SA / AI-use restriction blocks unapproved reuse.
- Ancient civilizations Claim A has direct World History Volume 1 §3.1 support, but that title is also NC-SA / AI-use restricted.
- Statistics and measurement uncertainty still need precise NIST locators and the distinction between error and uncertainty.

No candidate status or canonical record changed.

### Package C — internal offline reader shell implemented
Created:
- `REFERENCE/first_edition_shell/index.html`
- `REFERENCE/first_edition_shell/reader.css`
- `REFERENCE/first_edition_shell/reader.js`
- `REFERENCE/first_edition_shell/README.md`
- `REFERENCE/tests/test_first_edition_shell.py`
- `RELEASE/FIRST-EDITION-PACKAGE-C-PRIVATE-READER-SHELL-IMPLEMENTATION-AND-VALIDATION-2026-11-23.md`

The shell has 19 chapters, two parts, subsection navigation, local search, responsive layout, keyboard focus, reduced-motion support, local-only assets, CSP and explicit empty states. It does not load corpus records and does not claim any content is approved. The pytest suite is included in the existing REFERENCE test suite.

### Package D — bounded v0.1 first-edition blueprint
Created `RELEASE/FIRST-EDITION-PACKAGE-D-V0-1-CORE-EDITION-SELECTION-AND-RELEASE-BLUEPRINT-2026-11-23.md`.

The proposed seed set has five exact Claim entry points across both parts:
- emergency alerts;
- emergency hand hygiene;
- weather definition;
- SI base units;
- PostgreSQL relational model.

All remain HOLD. The document defines a release path, minimum criteria, offline artifact structure, inspection and approval requirements. It explicitly excludes NC-SA/AI-restricted sources and high-consequence procedures unless their blockers are resolved.

### Owner rights decision packet updated
`RELEASE/FIRST-EDITION-OWNER-DECISION-PACKET-R01-R10-2026-11-23.md` now maps verified source terms to first-edition consequences, especially project distribution model, item-level rights, exact artifact approval and correction/takedown operations. R-01–R-10 remain OPEN.

### Current exact-head status
- Latest PR #22 HEAD after Package D: `520546f7a2d49b429d6d4d96a0270e0973eea38e`.
- PR #22 remains OPEN / DRAFT / NOT MERGED.
- No workflow runs or commit statuses were returned for this exact HEAD. Do not infer CI PASS from prior commits. The latest shell pytest file is committed but its execution is not yet confirmed.
- No production INCLUDE manifest exists. The selection-aware offline builder remains fail-closed.
- The shell is internal-only and must not be deployed or described as the released first edition.

### Next execution block
1. Run/reconcile exact-head Reference Tests, Offline Edition and Release Conformance Gate using an authorized workflow dispatch or a normal PR-triggered CI event; do not change code merely to manufacture a green check.
2. Prepare exact versioned EU/Source remediation for the four most promising public candidates (PostgreSQL, NOAA, CDC and Red Cross), keeping rights blockers visible.
3. Complete SI private review only within its existing authorization; obtain three independent readers before any separate public-release decision.
4. Prepare the production reader layer that consumes only the approved schema-1.1 manifest, with chapter mapping and no corpus-wide fallback.
5. Freeze the smallest cross-part selection only after R-01/R-02/R-05/R-06/R-07/R-08/R-09/R-10 and item-level rights are resolved.

No main-branch file, merge, deployment, canonical record, publication decision or release authorization changed.


## Execution checkpoint — Package E: exact chapter assignment validator — 2026-11-23

### Completed

Added:
- `REFERENCE/src/encyclopedia_reference/first_edition.py`
- `REFERENCE/tests/test_first_edition_chapter_map.py`
- `REFERENCE/first_edition_shell/chapter-map-template.json`
- `RELEASE/FIRST-EDITION-PACKAGE-E-EXACT-CHAPTER-MAP-AND-APPROVED-SELECTION-VALIDATION-2026-11-23.md`

The new validator requires exactly 19 ordered chapters and assigns every selected Claim to exactly one chapter. It rejects stale/unselected references, non-Claim assignments, duplicate placement, missing chapter assignments and unsupported chapter-map schema versions. The checked-in template has 19 empty chapters and an explicit `template_not_approved` state.

The chapter map is separate from selection approval. It cannot add records or dependencies, change a HOLD decision, or make a record eligible for release. The existing schema-1.1 selection builder remains the sole gate for exact-version INCLUDE, explicit approval, profile pins and dependency closure.

### Current PR #22 status

- Latest PR #22 HEAD: `d8d224673517b36c02743ad1d4a99616cd7d6635` before this board update; board update itself creates a new HEAD.
- PR #22 remains OPEN / DRAFT / NOT MERGED.
- No CI result is claimed for documentation/code commits unless a workflow run is associated with the exact current HEAD.
- No production INCLUDE manifest exists; the chapter map template is empty and unapproved.
- No public artifact, deployment or merge was created.

### Next integration block

1. Reconcile the complete Reference Tests, Release Conformance Gate and Offline Edition on one immutable PR head.
2. Integrate the chapter-map validator into a production reader builder that consumes only the approved schema-1.1 selection output.
3. Add synthetic integration tests proving that unselected Claims and non-Claim dependencies cannot render as articles.
4. Resolve the first-edition owner rights decisions and item-level permissions.
5. Freeze the smallest cross-part seed set only after all required gates pass.

No main-branch files or canonical content records were changed.


## Final exact-head reconciliation — 2026-11-23

After the execution-plan addendum, PR #22 HEAD is `cfed0b759c429391d95b8dc11e7f7283f778f739`. PR remains OPEN / DRAFT / NOT MERGED. GitHub returned no workflow runs and no commit statuses for this exact SHA. The newly added Reference tests are therefore unverified by CI on this HEAD. The prior successful workflows on earlier exact commits are not carried forward. PR #21 M13 remains OPEN / DRAFT at `b6c11385906cd73c907ddd9cf2fe7a37af76558f`, with the previously recorded Reference Tests, Offline Edition and Release Conformance Gate successes on that exact M13 HEAD. No new M13 content change was made in this package.


## Execution checkpoint — exact locator reinspection and ancient-civilizations rights dependency — 2026-11-23

### Canonical reinspection corrections

Full-field canonical JSON inspection confirmed that two candidates already contain exact structured locators; no new canonical edit is required:

- `EU-DATABASES_BASICS-A/B/C@3` each has a claim-specific locator for PostgreSQL 18.7 §§2.2, 2.5 or 2.6. `SRC-DATABASES_BASICS@3` pins PostgreSQL 18.7 and §§2.2–2.6. `CTX-DATABASES_BASICS@3` and `SCP-DATABASES_BASICS@3` correctly target Claim A@3 and limit the slice to PostgreSQL 18.7. This work is already within the bounded Engineering/Computing authorization.
- `EU-MIXTURES_AND_SOLUTIONS-A@2` has a structured `material.locator` for OpenStax Chemistry 2e §11.1, “The Dissolution Process”, opening definition paragraph. The prose description is generic, but the locator field is exact. This work is already within the bounded Chemistry authorization.
- `EU-CHEMICAL_REACTIONS_BASICS-A@4` and `SRC-CHEMICAL_REACTIONS_BASICS@2` already contain the authorized §4.3 locator and exact source identity.
- The Red Cross emergency-alert Claim/EU/Source are already at @2 under their separate owner-approved correction; the six cross-slice Relation/Context references were separately aligned. No additional Red Cross canonical correction is indicated.

The representative shortlist has an append-only correction reflecting these exact-field findings.

### Ancient Civilizations — precise remaining provenance blocker

Re-fetched the complete current slice: 23 records (3 Claims, 10 Evidence Uses, 8 Sources, 1 Context, 1 Scope). The owner-approved Package A six-source/six-EU implementation is present; its six new CC BY 4.0 tracks have exact section locators and are represented in the 1,146-row Part II master. All records remain HOLD.

Claim B@1 still has `provenance.created_from → SRC-ANCIENT_CIVILIZATIONS_BASICS@1`, which points to OpenStax *World History Volume 1, to 1500*. OpenStax's own pages state that this specific title is CC BY-NC-SA 4.0 and prohibit LLM/generative-AI ingestion without prior written permission. The selection builder recursively checks structured references in provenance, so the old Source is a required dependency if Claim B@1 is selected. The six new CC BY 4.0 EUs do not remove that dependency.

Prepared a separate request:
`RELEASE/OWNER-AUTHORIZATION-REQUEST-ANCIENT-CIVILIZATIONS-CLAIM-B-CC-BY-PROVENANCE-MIGRATION-2026-11-23.md`.

It proposes only Claim B@1→@2 with identical wording and new provenance to the three approved CC BY 4.0 Sources, plus three EU v1→v2 claim_ref alignments. Old @1 records remain historical; Claim A/C, Context/Scope and Source records are untouched. This request is NOT APPROVED and nothing has been implemented. It is the next owner decision if Claim B is to be considered for a CC BY-only first-edition selection.

### Exact-head CI

- Current PR #22 HEAD observed during this checkpoint: `fba2a8b9f4d47a89c552fced7812f18f712427f7`.
- Push-triggered Reference implementation tests run `45173229571`: queued/pending at last poll.
- Push-triggered Offline Edition run `45173229859`: in progress at Content preflight; no result yet.
- No current-head Release Gate or Browser Tests success is claimed. The previous four-workflow PASS remains limited to exact HEAD `e656620...`.

PR #22 remains OPEN / DRAFT / NOT MERGED. No canonical record, disposition, project licence, allowlist, publication state, merge, deployment or main-branch file changed.


## Execution checkpoint — source-rights compatibility screen — 2026-11-23

### Completed

Added `RELEASE/FIRST-EDITION-SOURCE-RIGHTS-COMPATIBILITY-SCREEN-2026-11-23.md` after checking official title-specific licensing and source terms for the current representative candidates.

Key findings:
- OpenStax Chemistry 2e, Biology 2e and World History Volume 1 are CC BY-NC-SA 4.0 and have explicit restrictions on LLM/generative-AI ingestion without prior written permission.
- OpenStax Physics has a more complicated title-specific notice: its Customization section says CC BY 4.0, while the reuse notice separately restricts LLM ingestion and includes TEA attribution/non-commercial language for certain material/assets. Do not treat it as a simple CC BY 4.0 clearance without written clarification.
- PostgreSQL documentation is covered by the PostgreSQL License, which permits copying, modifying and distributing software and documentation for any purpose if the required notices are retained. This is currently the cleanest rights path among the inspected technical candidates.
- Red Cross Terms of Use grant personal non-commercial use and restrict copying/distribution and intact page reproduction; independent factual paraphrase plus a link is not blanket commercial clearance.
- FAO publications are copyrighted; the general permission policy allows specified non-commercial use with attribution, while reuse/adaptation permissions are handled separately.
- World Bank terms generally limit use to personal/educational/non-commercial purposes and require written permission for commercial redistribution unless otherwise stated.
- U.S. federal sources (CDC, NOAA, NIST, USGS, USDA) are promising for factual paraphrase, but federal websites can contain third-party material. Exclude third-party images/maps/tables/logos and check the exact page.
- USDA soil material requires special attribution care because the page includes Soil Science Society of America and Soil Taxonomy definitions.

### First-edition consequence

A source may have a precise locator and still be unsuitable for the project's intended distribution or AI-assisted workflow. The rights screen therefore changes the practical priority:
- strongest current compatibility candidate: PostgreSQL documentation / databases-basics;
- potentially favorable after page-level checks: CDC, NOAA, NIST, USGS, USDA factual government material;
- conditional or blocked pending permission/alternative: OpenStax NC-SA titles, OpenStax Physics ambiguity, Red Cross, FAO and World Bank sources.

This does not establish the project's intended licence or resolve R-01–R-10. No permission request has been sent. No rights status has been changed in canonical records. All candidates remain HOLD.

### Exact-head CI

The rights-screen report commit is `43094b0b5283b6785551b44eb85c4ae8dc6f5f90`. At the latest poll, all four required PR workflows were triggered on this exact HEAD:
- Reference implementation tests run `45173624582` — pending.
- Release Conformance Gate run `45173624636` — pending.
- Offline Edition run `45173624844` — in progress.
- MVP Contribution Form Browser Tests run `45173624571` — in progress.

No PASS is claimed until all four complete successfully on this exact SHA.

### Next work

1. Reconcile the shortlist against this rights screen; remove any assumption that an exact locator implies rights clearance.
2. Prioritize PostgreSQL and government factual sources with page-level asset exclusions.
3. Keep OpenStax/Red Cross/FAO/World Bank dependencies out of any public manifest until permission, source replacement or an owner-approved compatible distribution model is documented.
4. Resolve the prepared Ancient Civilizations Claim B provenance request separately.
5. Close R-01–R-10 before creating a production INCLUDE manifest.
