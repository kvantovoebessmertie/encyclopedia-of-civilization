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
