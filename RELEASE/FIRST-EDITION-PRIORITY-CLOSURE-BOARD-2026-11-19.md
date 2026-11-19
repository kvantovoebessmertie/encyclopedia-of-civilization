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
