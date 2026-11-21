# M13 bounded correction authorization — Evidence Use provenance lineage

Date: 2026-11-15
Authorization ID: M13-EU-PROVENANCE-LINEAGE-001
Branch: m13-system-wide-depth-audit-2026-10-09
Status: AUTHORIZED FOR FOUR EXACT PROVENANCE-FIELD CORRECTIONS ONLY

## Basis

The project owner has explicitly directed that known M13 defects be consolidated and corrected in bounded batches before final consolidated verification. This authorization narrows that direction to four exact, independently verified Evidence Use records.

The accepted provenance standard requires represented lineage to preserve the material origin of the target. The same risk-management slice contains EU-RISK_MANAGEMENT_COSO with created_from correctly pointing to its Source, while the two ISO Evidence Use records point to their Claims. Package 30 identifies the same defect pattern in International Trade B and Labor Law B.

## Exact authorized records and paths

Only the following four existing Evidence Use records may be versioned from record_version 1 to 2:

1. CONTENT/vertical-slices/international-trade-basics/records/EU-INTERNATIONAL_TRADE_BASICS-B.json
   - record ID: EU-INTERNATIONAL_TRADE_BASICS-B
   - current incorrect created_from: CLM-INTERNATIONAL_TRADE_BASICS-B@1
   - authorized created_from: SRC-INTERNATIONAL_TRADE_BASICS@1

2. CONTENT/vertical-slices/labor-law-basics/records/EU-LABOR_LAW_BASICS-B.json
   - record ID: EU-LABOR_LAW_BASICS-B
   - current incorrect created_from: CLM-LABOR_LAW_BASICS-B@1
   - authorized created_from: SRC-LABOR_LAW_BASICS@1

3. CONTENT/vertical-slices/risk-management-basics/records/EU-RISK_MANAGEMENT_BASICS-B.json
   - record ID: EU-RISK_MANAGEMENT_BASICS-B
   - current incorrect created_from: CLM-RISK_MANAGEMENT_BASICS-B@1
   - authorized created_from: SRC-RISK_MANAGEMENT_BASICS@1

4. CONTENT/vertical-slices/risk-management-basics/records/EU-RISK_MANAGEMENT_BASICS-C.json
   - record ID: EU-RISK_MANAGEMENT_BASICS-C
   - current incorrect created_from: CLM-RISK_MANAGEMENT_BASICS-C@1
   - authorized created_from: SRC-RISK_MANAGEMENT_BASICS@1

The Risk Management C record above is the ISO-linked Evidence Use. The separate EU-RISK_MANAGEMENT_COSO record is not defective and is expressly excluded; it already points to SRC-COSO-ERM-RISK-MANAGEMENT@1.

## Permitted change

For each of the four named files, change only:
- record_version: "1" to "2";
- provenance.created_from[0].record_id: from the Claim ID to the exact Source ID stated above;
- preserve provenance.created_from[0].version as "1".

The record ID, type_version, record_type, schema, publication_status, completion_status, provenance.method, all content fields, claim_ref, source_ref, evidence_role and material description MUST remain byte-for-byte semantically unchanged.

No other field or file is authorized for canonical modification.

## Rights hold and semantic separation

The two Risk Management Evidence Use records remain associated with the ISO 31000 Source, which is under RIGHTS HOLD for this AI-assisted evidence workflow. This metadata-only provenance correction does not access, quote, summarize, prompt with, or rely on ISO content; it does not clear rights, permit AI use of ISO content, or make ISO evidence admissible.

Risk Management C's separate COSO Evidence Use remains unchanged and is the only evidence path used for the Package 31 direct conceptual-support finding.

## Required regression and acceptance

Add or extend regression coverage to assert:
- all four records are version 2;
- each created_from points to the exact authorized Source@1;
- content.claim_ref and content.source_ref remain unchanged and resolve to the exact version-1 records;
- provenance.method remains unchanged;
- the separate EU-RISK_MANAGEMENT_COSO record is unchanged and still points to SRC-COSO-ERM-RISK-MANAGEMENT@1;
- no unrelated records or slice inventories changed.

After correction:
1. Run JSON/schema preflight and the dedicated regression.
2. Run Reference Tests, Release Conformance Gate and Offline Edition on the same exact final HEAD.
3. Inspect the diff to prove only the four authorized JSON fields plus the explicitly authorized test/checkpoint files changed.
4. Preserve prior versions/history.
5. Keep all four Claims UNASSESSED/HOLD as applicable; no D/E/B changes, rights clearance, specialist approval, Human View, publication or release approval is implied.

This authorization does not permit changes to Claim wording, Source identity/URI, Evidence Use content, Context, Scope, Relation, D/E/B, any other record, main, or PR merge.
