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
| Shared Context applicability | BLOCKED — OWNER DECISION | 62 Relations use one Context whose target_ref is one Relation. Recommended: target-specific Context for each Relation; 61 new Context records would be needed. Approve per-Relation Context or explicit transferability model, then authorize exact changes/tests |
| Earthquake Event | BLOCKED — DOMAIN MODEL | Generic shaking description stored as reported Event; its Context/Scope target a protective-action Claim, not the Event. Decide generic-knowledge representation vs actual occurrence and resolve target applicability |
| Container/water State Relation | BLOCKED — DOMAIN MODEL | Both States describe the same container Object; second participant is not a water State. Decide distinct water Object/State, accurate state-to-state relation, or authorized exclusion |
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

1. Obtain owner decision on the shared Context strategy and bounded authorization for the exact Relation/Context/test files.
2. Obtain bounded domain authorization for the Event and water-storage model corrections or explicit release exclusion.
3. Execute the ready semantic endpoint substitutions only after exact Evidence Use and rights checks; first candidates are library/archival preservation and emergency/infrastructure resilience.
4. Resolve research-methods Evidence Use locators from the National Academies source before changing the research/statistics Relation.
5. Close R-01–R-10 with authorized owner decisions; continue item-level rights verification.
6. Wait for exact-head CI and then rerun all release gates after canonical changes.


## Execution checkpoint — 2026-11-19, after Batch 2 and exact-head CI

- Batch 2 is complete: 5/5 explicit map-gap slices and 47/47 records screened; all five remain HOLD. The five slices are not pending screens.
- The 47 Batch 2 canonical JSON blob SHAs were compared between the Batch 2 inspection commit `c4fbc8d1d879ae0c14e2b0ceaba8899d4f6fef0d` and the then-current PR HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`: 47/47 unchanged.
- The exact-version master already contains all 47 Batch 2 rows: 1,119 unique exact-version rows (1,058 candidate + 61 dependency), 124/385 Part II slices represented, 261 not yet registered. The 261 unlisted slices remain outside the bounded first-edition map screen; no blanket audit is authorized.
- Added `FIRST-EDITION-BATCH2-EVIDENCE-REMEDIATION-RESEARCH-2026-11-19.md`: source/locator remediation plan for ancient civilizations, anthropology, linguistics, philosophy and ethics. It proposes Claim concepts and precise source locators but makes no canonical changes or decision changes. The report explicitly corrects the OpenStax Anthropology live licence to CC BY-NC-SA 4.0 and records the cloned-source limitation of the Linguistics OER.
- At HEAD `48c78389fb5345223627a687b22d51ee260b9d7d`, all four exact-head CI workflows passed: Reference Tests (1,003 passed), Release Conformance Gate (CONFORMING; 0 blocking conditions in the checked scope), Offline Edition and Browser Tests. The later commits in this checkpoint are documentation-only; their exact-head CI must be checked separately.
- Owner decisions and canonical authorization remain required before any Batch 2 Claim/Source/Evidence Use correction. No Batch 2 slice is promoted; no allowlist created.

### Updated next actions

1. Obtain owner/editorial authorization for the Batch 2 record-level remediation scopes before changing any of the five slices.
2. Obtain architecture-owner decision and bounded authorization for the shared Relation Context strategy; separately resolve the earthquake Event and container/water State model.
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
