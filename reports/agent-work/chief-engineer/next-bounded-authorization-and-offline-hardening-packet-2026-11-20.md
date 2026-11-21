# Next Bounded Authorization and Offline Hardening Packet

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Inspection branch: `mvp-public-contribution-design-2026-10-11`  
Exact inspected PR #22 HEAD: `6c33b415ffa1877e62fda83af20136a5a31046c0`  
Status: **RESEARCH / PROPOSAL ONLY — NO NEW CANONICAL AUTHORIZATION OR RIGHTS DECISION**

## 1. Exact-head technical checkpoint

All four required PR #22 workflows completed successfully on the same immutable HEAD `6c33b415ffa1877e62fda83af20136a5a31046c0`:

- Offline Edition — PASS (run 44731511140)
- MVP Contribution Form Browser Tests — PASS (run 44731511235)
- Reference implementation tests — PASS (run 44731511049)
- Release Conformance Gate — PASS (run 44731511130)

The associated push-triggered Offline Edition and Reference Tests also completed successfully on the same SHA. The PR remains OPEN / DRAFT / NOT MERGED. Its base is the merge-base `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`; `main` is `d58289f319993ede5294a46f4741a506fd2fd710`, eight commits ahead of that merge-base. The eight commits are the agent-reporting standard, agent instructions, Copilot instructions and report template. No branch update or merge was performed.

## 2. AMR–Plant Health — proposed FAO relation-evidence authorization

### Current exact graph at inspected HEAD

- `REL-CROSS-AMR-PLANT-HEALTH@2`
- `CTX-REL-CROSS-AMR-PLANT-HEALTH@1` targets Relation @2
- Endpoint 1: `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1`, supported by `EU-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` → WHO Source @1
- Endpoint 2: `CLM-PLANT_PATHOLOGY_BASICS-A@1`, supported by `EU-PLANT_PATHOLOGY_BASICS-A@1` → APS Source @1
- Both existing EU records have generic descriptions without pinpoint locators.
- The Relation's provenance currently identifies WHO and APS Sources; FAO is not in the canonical graph.

### Direct bridge and limits

FAO's official plant-health AMR page describes resistance of plant pathogens to antimicrobials used as pesticides, use of antibiotics against bacterial crop diseases, and pathways by which pesticide use in plant production can contribute to AMR in human/animal pathogens. This is a direct cross-domain mechanism, not merely topic similarity.

Official locator: https://www.fao.org/pest-and-pesticide-management/pesticide-risk-reduction/amr/en/

The page supports a plant-health AMR link. It does not turn the general phytopathology definition Claim into a detailed AMR mechanism, and it must not be represented as doing so. The proposed route therefore attaches the FAO source at the Relation level rather than silently rewriting either endpoint Claim.

### Proposed exact bounded change — pending owner authorization

1. Create one Source record in `cross-slice-linkage`: `SRC-FAO-AMR-PLANT-HEALTH@1`, identifying the exact FAO page, URI and a pinpoint textual locator.
2. Version `REL-CROSS-AMR-PLANT-HEALTH@2 → @3`; add only the FAO Source @1 to `provenance.created_from`. Preserve both participant Claims and their order, relation_type, roles, direction, frame_ref, and all semantics.
3. Version `CTX-REL-CROSS-AMR-PLANT-HEALTH@1 → @2`; add the same FAO Source @1 to provenance and update only target_ref to Relation @3. Preserve context content and epistemic status.
4. Do not change either endpoint Claim, either existing Evidence Use, either endpoint Source, any slice Context/Scope, status, allowlist or publication decision.

This is a relation-level evidence path, not a claim that the FAO page supports the generic APS phytopathology definition. Independent plant-health/AMR subject-matter review must confirm that the Relation's type and endpoints remain properly bounded before any status decision.

### Rights boundary

FAO terms permit certain attributed non-commercial uses of website content but require permission for translation/adaptation and resale/commercial uses; third-party components need separate clearance. The proposal uses only bibliographic identity, hyperlink, pinpoint locator and independently worded factual paraphrase. No FAO prose, tables, figures, images, photographs, logo or other expressive assets are proposed for reproduction. The final project distribution model remains undecided, so no blanket rights clearance is inferred.

Terms: https://www.fao.org/contact-us/terms/

### Authorization requested

Owner decision required for exactly the three records above and the specified fields only. Keep the Relation and both endpoint slices HOLD. Do not add a new Evidence Use, modify endpoint Claims, or make any release/allowlist change under this proposed authorization.

## 3. Migration–Labour — proposed ILO 2026 Guide evidence chain

### Current exact graph at inspected HEAD

- `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`
- `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@1` targets Relation @4
- Migration endpoint: `CLM-MIGRATION_AND_MOBILITY_BASICS-C@2`; current `EU-MIGRATION_AND_MOBILITY_BASICS-C@2` points to UNSD Recommendations 2025 rev. 2, pp. 17–22 and 7–10.
- Labour endpoint: `CLM-LABOR_ECONOMICS_BASICS-C@2`; current `EU-LABOR_ECONOMICS_BASICS-C@2` points to ILOSTAT resources covering employment, wages, working time, productivity and labour underutilization, with a warning that series and definitions are not interchangeable.
- The two endpoint Claims and Relation participants are exact and aligned. The Relation already represents the link between migration definitions/measurement and labour-market indicators.

### New direct source

ILO, *Mapping and assessing sources for statistics of international labour migration and temporary labour mobility: ILO practical guide*, June 2026.

PDF: https://www.ilo.org/sites/default/files/2026-07/ILO_Guide_Mapping_ILMS_2026_FINAL.pdf

Candidate locators:
- pp. 22–27: migration/mobility concepts, definitions, stocks and flows;
- pp. 30–33: labour-force status, employment, unemployment and underutilization;
- pp. 34–38: international labour migration and labour attachment;
- p. 43: minimum data items;
- pp. 57–58: core labour-market indicators for international migrants;
- pp. 63–66: source-specific coverage and limitations, including wages, contractual hours and administrative records.

**Critical support boundary:** this Guide is not being used to assert that labour productivity is automatically comparable for migrant groups. The existing ILOSTAT EU remains necessary for the productivity component of Labour Claim C. The new Guide is additive evidence for the migration/labour measurement intersection, not a replacement for the whole existing ILOSTAT chain.

### Proposed exact bounded additive change — pending owner authorization

1. Create one Source in `migration-and-mobility-basics`: `SRC-MIGRATION-LABOUR-STATISTICS-ILO-GUIDE@1`, identifying the exact June 2026 Guide and its work-level rights notice.
2. Create one additional Evidence Use for the existing migration Claim C: `EU-MIGRATION_AND_MOBILITY_BASICS-C-ILO-GUIDE@1`, linking Claim C @2 to the new Source @1 and using the migration concept/definition/stock-flow locators (pp. 22–27 and, where appropriate, pp. 34–38).
3. Create one additional Evidence Use for the existing labour Claim C: `EU-LABOR_ECONOMICS_BASICS-C-ILO-GUIDE@1`, linking Claim C @2 to the same Source @1 and using labour-status/indicator/coverage locators (pp. 30–33, 57–58, 63–66).
4. Do not replace or rewrite the current UNSD or ILOSTAT Evidence Use records. Do not claim Guide support for productivity.
5. Do not change `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`, its Context @1, participants, provenance, type or semantics. The new EU records provide source support to the existing endpoint Claims; no Relation version bump is required for this additive evidence path.
6. Do not change Claim statements, Context/Scope targets, publication/completion status, allowlist or release disposition.

### Rights boundary

The exact Guide PDF states CC BY 4.0 on printed p. ii. Attribution to ILO and indication of changes are required; third-party components are excluded; the ILO name/emblem/logo must not be used in a way prohibited by the notice. No third-party figure, image, map, table or logo is proposed for reuse. If adapting or translating the Guide itself, the work-specific disclaimer on p. ii must be followed; this proposal does not call for translating or reproducing the Guide.

General rights page: https://www.ilo.org/rights-and-permissions

### Authorization requested

Owner decision required for exactly one new Source and two new Evidence Use records, with the exact existing Claims and source locators above. Keep both slices and the Relation HOLD. No changes to the existing R7 Labour Economics 13-record Path B authorization are implied.

## 4. Offline Edition security — current acceptance and remaining hardening

### SEC-1 status

PR #41's offline HTML renderer fix was independently reviewed and ACCEPTED in report `reports/agent-work/security-offline/pr41-independent-html-escaping-review.md` at exact SHA `fcb365c9f5b28eff11c36fe0ebb18ab756cd6370`.

At the inspected PR #22 HEAD:
- `REFERENCE/src/encyclopedia_reference/offline_edition.py` has the exact same Git blob SHA as PR #41: `5979a55f71d14b41fe98177c2ac9e6982c4b65fa`.
- `REFERENCE/tests/test_offline_edition.py` has the same normalized line content as the PR #41 test file (Git blob SHA differs); it includes the SEC-1 regression fixture.
- Therefore the accepted record-controlled HTML escaping implementation is present in PR #22. The exact-head Offline Edition and full Reference Tests passed.

### Separate low-priority hardening remains open

Issue #43, “Harden offline edition_id in README and strengthen HTML regression tests”, remains OPEN. It tracks a separate `edition_id` sink in generated README.md and stronger parser-based adversarial regression assertions. The independent PR #41 review classified the README sink as Low, confirmed by source read but not exploit-tested, and recommended a separate follow-up; it did not reopen SEC-1 or require remediation for acceptance of PR #41.

Issue #43's boundaries require a separate branch and Draft PR targeting the M13 branch; do not modify PR #41 or #42, main, canonical records, schemas, workflows, governance, or unrelated files; do not add CSP; do not proceed if a safe compatible `--edition-id` identifier contract cannot be established from repository evidence.

**Disposition:** do not conflate Issue #43 with the accepted SEC-1 fix. It is a separate hardening task. It needs its own explicit execution scope and exact-head tests; no implementation is included in this report.

## 5. WP2 owner decisions remain open

The current owner decision register still marks R-01 through R-10 OPEN:
- R-01 rights holder;
- R-02 content/data licence;
- R-03 software licence;
- R-04 contributor terms;
- R-05 source reuse policy;
- R-06 accountable editor;
- R-07 release approver;
- R-08 correction/dispute/withdrawal process and public contact;
- R-09 authorship/attribution policy;
- R-10 rights evidence storage and validation.

No automated audit can choose the legal rights holder, licence, named editor, approver or public contact. The conservative proposed first-edition defaults in the Owner Decision Record remain proposals, not adopted policy. Do not mark WP2 complete or infer a decision from repository activity.

## 6. Recommended execution order

1. Owner approves or declines the exact three-record FAO relation-evidence package.
2. Owner separately approves or declines the exact three-record ILO Guide evidence package.
3. After approval only, implement one package at a time, re-fetch every exact record before writing, preserve HOLD and all unrelated fields, then run full exact-head CI.
4. Conduct independent subject-matter review of AMR/plant-health Relation fit and migration/labour statistical boundary.
5. Decide whether to authorize Issue #43 as a separate M13 hardening task; retain its own base/head and tests.
6. Continue R-01–R-10 owner decisions and source-specific rights checks. WP2 remains open until the actual owner choices and evidence are recorded.
7. For WP3, keep PR #22 Draft and unmerged. Before any future merge, first synchronize the branch with the eight documentation-only commits on main, inspect the exact integrated diff, re-run all four workflows on one final immutable HEAD, inspect the generated offline artifact, and obtain separate editorial/rights/release approval.

## 7. Explicit non-actions

- No canonical JSON was changed.
- No Source or Evidence Use record was added.
- No Relation, Context, Claim, Scope or version was changed.
- No HOLD was removed; no INCLUDE/EXCLUDE or allowlist decision was made.
- No licence, permission, rights holder, editor, approver or contact was invented.
- No PR was merged, closed, retargeted or marked ready.
- `main` was not changed.
