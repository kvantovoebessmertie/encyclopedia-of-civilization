# Owner-Authorized FAO and ILO Cross-Slice Evidence Implementation — 2026-11-20

## Status

**IMPLEMENTED ON PR #22 BRANCH; ALL AFFECTED CONTENT REMAINS HOLD; NO RELEASE OR MERGE.**

Owner approval: explicit approval in the project conversation on 2026-11-20, following presentation of the exact bounded FAO Relation-evidence package and ILO additive Evidence Use package.

Implementation base: `01a4781fb72c0cefe0c20519c8a9b70a5253ef4b`.

## 1. FAO — AMR / Plant Health

Created:
- `SRC-FAO-AMR-PLANT-HEALTH@1` in `cross-slice-linkage`, with the official FAO plant-health AMR page and pinpointed mechanism locator.
- `REL-CROSS-AMR-PLANT-HEALTH@2 → @3`: added only the FAO Source @1 to `provenance.created_from`; aligned `frame_ref` to Context @2.
- `CTX-REL-CROSS-AMR-PLANT-HEALTH@1 → @2`: added only the FAO Source @1 to provenance and aligned `target_ref` to Relation @3.

The two participant Claims, participant order, relation type, roles, direction, Context condition and epistemic status are preserved. No endpoint Claim or endpoint Evidence Use was changed. FAO evidence is represented at the Relation level only; no claim is made that FAO supports the generic Plant Pathology Claim.

Rights boundary recorded: bibliographic identity, link, locator and independently worded factual paraphrase only; no FAO expressive text or assets reproduced. Commercial use, translation/adaptation and third-party components remain subject to permission/clearance. Project distribution rights remain open.

## 2. ILO — Migration / Labour Economics

Created:
- `SRC-MIGRATION-LABOUR-STATISTICS-ILO-GUIDE@1` in `migration-and-mobility-basics`.
- `EU-MIGRATION_AND_MOBILITY_BASICS-C-ILO-GUIDE@1` → existing Migration Claim C @2, with printed pp. 22–27 and 34–38.
- `EU-LABOR_ECONOMICS_BASICS-C-ILO-GUIDE@1` → existing Labour Economics Claim C @2, with printed pp. 30–33, 57–58 and 63–66.

The existing UNSD Migration Evidence Use and ILOSTAT Labour Economics Evidence Use remain unchanged. The new Guide is additive, not a replacement. It is not cited as evidence that labour productivity is automatically comparable for migrant groups.

Rights boundary recorded from the exact work-level notice on printed p. ii: CC BY 4.0 with attribution and indication of changes; third-party components excluded; ILO name/emblem/logo restrictions retained. No expressive text, tables, figures or third-party assets reproduced.

## 3. Exact preservation checks

- Both affected endpoint Claims remain byte-for-byte unchanged.
- Existing UNSD and ILOSTAT Evidence Use and Source records remain unchanged.
- FAO package changes only the named Source, Relation and Relation-specific Context.
- ILO package creates only the named Source and two additional Evidence Use records.
- Existing R7 Labour Economics ILO Path B 13-record authorization and graph are untouched.
- All affected records retain their existing publication/completion statuses; no HOLD was removed and no INCLUDE/EXCLUDE decision or allowlist was created.
- `RELEASE/EDITORIAL-CORRECTION.json` records both explicit bounded authorizations.
- `RELEASE/CONTENT-COVERAGE.json` derived counts updated from 4,742 to 4,746 total records; Source 590→592; Evidence Use 1,588→1,590. Slice count and all other type counts are unchanged.

## 4. Required independent review and remaining gates

1. Independent plant-health/AMR subject-matter review of the Relation's type, endpoint fit and Relation-level evidence boundary.
2. Independent migration/labour statistical review of the new ILO Guide locators and the boundary around productivity comparability.
3. Project-level rights/distribution review, including unresolved R-01–R-10 and third-party source restrictions.
4. Human View and exact-head CI across all four required workflows.
5. First-edition selection remains separate: no allowlist exists and no affected record is approved for publication.

## 5. Non-actions

No Claim wording, endpoint Evidence Use, endpoint Source, other Relation/Context/Scope, schema, validator, workflow, main branch or release disposition was changed. No PR was merged, no deployment or publication occurred.
