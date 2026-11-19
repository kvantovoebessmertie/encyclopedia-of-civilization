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
