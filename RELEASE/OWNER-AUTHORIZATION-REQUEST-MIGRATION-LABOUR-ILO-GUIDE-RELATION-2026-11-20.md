# Owner Authorization Request — ILO 2026 Guide for Migration / Labour Economics Relation

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — `mvp-public-contribution-design-2026-10-11`  
Status: **REQUEST ONLY — NOT AUTHORIZED; NO CANONICAL CHANGES PERMITTED**

## 1. Decision requested

The owner is asked whether to authorize one bounded, relation-level source integration for:

- `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`
- `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@1`
- participant Claims `CLM-MIGRATION_AND_MOBILITY_BASICS-C@2` and `CLM-LABOR_ECONOMICS_BASICS-C@2`

The ILO June 2026 Practical Guide directly integrates migration definitions, stocks/flows and labour-force/labour-market indicators for international migrant populations. The evidence review is in `reports/agent-work/chief-engineer/migration-labour-measurement-relation-evidence-adjudication-2026-11-20.md`.

## 2. Exact proposed authorization scope

If approved, authorize only these operations:

1. Create one new Source record:
   - proposed ID: `SRC-ILO-INTERNATIONAL-LABOUR-MIGRATION-STATISTICS-GUIDE-2026`
   - version: `1`
   - path: `CONTENT/vertical-slices/cross-slice-linkage/records/SRC-ILO-INTERNATIONAL-LABOUR-MIGRATION-STATISTICS-GUIDE-2026.json`
   - source: ILO, *Mapping and assessing sources for statistics of international labour migration and temporary labour mobility: ILO Practical Guide* (June 2026), ISBN 9789220434925, DOI 10.54394/00034270
   - locator: Foreword p. 8; Chapter 2 §§2.2.4–2.2.5, pp. 30–37; Box 11, pp. 35–36; Chapter 3 Table 8, p. 57; Chapter 4 source-mapping and data-source assessment sections.
   - rights boundary: exact work-level CC BY 4.0; require ILO attribution and indication of changes; no ILO emblem/name/logo in derivative works; third-party materials excluded and separately screened. No third-party images/figures/tables proposed for reuse.

2. Create `REL-CROSS-MIGRATION-LABOR-ECONOMICS@5` as a new version:
   - preserve `relation_type=migration_and_labor_measurement_link`;
   - preserve both exact participant IDs and versions @2;
   - preserve roles, direction and all other semantic fields;
   - preserve existing provenance and add only the new ILO Source @1 to `provenance.created_from`;
   - update `frame_ref` to `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@2`.

3. Create `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@2`:
   - preserve the existing context condition and epistemic status unchanged;
   - update `target_ref` to Relation @5;
   - preserve existing provenance and add the new ILO Source @1 only if required by the established Relation/Context provenance convention.

4. Preserve **HOLD** and all publication/selection states. This is evidence/provenance integration only, not approval for first-edition inclusion.

## 3. Explicit exclusions

This request does NOT authorize:
- changing either participant Claim statement, Claim type, Scope, or existing Evidence Use;
- replacing UNSD or ILOSTAT Source/Evidence Use chains;
- adding new Claim or Evidence Use records;
- changing any other Relation or Context;
- changing Labour Economics Path B's 13-record authorization or its canonical records;
- INCLUDE/EXCLUDE, allowlist, candidate promotion, HOLD removal, licence adoption, permission declaration, or publication;
- merging PR #22 or changing `main`.

The new ILO Guide is a cross-slice relation-level source. It is not part of the prior Labour Economics ILO Path B authorization.

## 4. Evidence and rights basis

Official ILO PDF:
https://www.ilo.org/sites/default/files/2026-07/ILO_Guide_Mapping_ILMS_2026_FINAL.pdf

The copyright page (printed p. ii) explicitly grants CC BY 4.0 for this exact work, requires attribution and indication of changes, excludes third-party materials, and prohibits ILO emblem/name/logo use in connection with translations, adaptations or derivatives. No third-party component is proposed for reuse.

The Guide directly defines international labour migration statistics in terms of migrant labour-market characteristics, integrates labour-force status with migration criteria, and lists core labour-market indicators for international migrants. The existing participant Claims remain unchanged and within the Guide's stated statistical scope.

Project-level rights decisions R-01–R-10 remain OPEN. The exact work licence does not adopt the Encyclopedia's project licence or determine commercial compatibility of the full edition.

## 5. Acceptance checks if approved

- Source ID unique and exact source metadata/rights notice validated.
- Relation @5 preserves all existing participants and semantics, adding only Source @1 provenance.
- Context @2 points to Relation @5; no stale target reference remains.
- Existing participant Claim and Evidence Use records remain unchanged.
- HOLD remains unchanged.
- Reference Tests, Release Conformance Gate, Offline Edition and MVP Browser Tests run on the exact resulting HEAD.
- Independent migration-statistics / labour-statistics editorial review remains required before any first-edition selection decision.

## 6. Owner response

Select one explicit response in the conversation:

- **AUTHORIZE** the exact bounded operations in §2, with all exclusions in §3.
- **DECLINE**; leave canonical records unchanged and retain the current report-only evidence finding.
- **DEFER**; leave canonical records unchanged pending further review.

No action is authorized by silence, by the existence of this request, or by prior Labour Economics Path B authorization.

## 7. Current state

- Relation @4 and Context @1 remain unchanged.
- Existing participants remain Claim @2.
- ILO Guide is not yet a canonical Source record for this Relation.
- Relation and affected slices remain HOLD.
- No canonical changes have been made by this request.
