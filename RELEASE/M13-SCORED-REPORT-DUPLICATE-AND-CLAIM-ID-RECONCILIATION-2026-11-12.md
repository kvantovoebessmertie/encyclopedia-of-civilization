# M13 scored-report duplicate and Claim-ID reconciliation

Date: 2026-11-12
Source revision: e5d1dcf07c6fa800c30729c220bbd945c1edb99b
Scope: full 1,494-Claim inventory and all 1,501 extracted scored-report rows. This is an identifier/accounting reconciliation, not semantic duplicate adjudication or acceptance of any score.

## 1. Reconciled coverage

The exact-head ledger artifact reports:
- Canonical Claim inventory: 1,494.
- Scored-report rows: 1,501.
- Unique normalized report IDs: 1,494.
- Claims with at least one scored-row match: 1,494/1,494.
- Claims without a scored-row match: 0.
- Unmatched scored-report rows: 0.
- Duplicate groups: 7, containing 14 rows.
- Separator-normalized report aliases requiring manual confirmation: 1.
- No canonical Claim/Evidence Use/Source record was changed by this reconciliation.

The inventory now has full scored-report coverage, but duplicate groups and the alias still require human adjudication. “100% matched” is not the same as “100% evidence validated” or “100% accepted”.

## 2. Seven duplicate report groups

The ledger preserves both rows in every group. It does not silently select the later report.

| Claim ID | Earlier row | Later row | Difference |
|---|---|---|---|
| CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A | Batch 12: D1/E1/B2 | Batch 17: D2/E1/B2 | D differs |
| CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B | Batch 12: D2/E1/B3 | Batch 17: D2/E1/B2 | B differs |
| CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C | Batch 12: D1/E1/B3 | Batch 17: D2/E1/B2 | D and B differ |
| CLM-M5-WATER-EMERGENCY-DISINFECTION-D | Batch 21: D3/E3/B3 | Batch 27: D3/E3/B3 | Scores identical; duplicate report row |
| CLM-WATER_TREATMENT_BASICS-A | Batch 21: D2/E2/B3 | Batch 27: D2/E3/B3 | E differs |
| CLM-WATER_TREATMENT_BASICS-B | Batch 21: D2/E3/B3 | Batch 27: D3/E3/B3 | D differs |
| CLM-WATER_TREATMENT_BASICS-C | Batch 21: D2/E2/B3 | Batch 27: D2/E3/B3 | E differs |

### Context and proposed adjudication route

- Batch 12 is a bounded purposive review of three foundational nuclear-physics Claims. Batch 17 is a later four-Claim desk review that revisits those same three Claims alongside an emergency-water Claim. Batch 17's rationales are more detailed, but the D/B differences are real scoring changes, not formatting duplicates. A reviewer must decide whether Batch 17 supersedes Batch 12, whether scores should be reconciled, or whether both are retained as separate historical assessments.
- Batch 21 reviews water treatment, emergency disinfection, water security, burns and electrical safety. Batch 27 is a later, narrower water-treatment/emergency-disinfection review with more specific WHO/EPA evidence descriptions. The improved E scores in Batch 27 may reflect a better-specified evidence chain; they must not be treated as an automatic override without verifying the exact Claim/EU/Source versions and the scoring rubric at each review date.
- The M5 emergency-disinfection Claim has identical D/E/B scores in both reports. It is still a duplicate report row and should be explicitly marked as a repeated corroborating review or a superseded duplicate in the adjudication record.
- Do not delete either report or collapse duplicate rows. Preserve the audit trail and record an explicit adjudication decision for each Claim ID.

## 3. Separator-normalized alias

One report row uses:
- Report ID: CLM-POWER_ELECTRONICS_BASICS_B@1
- Report: Batch 44, lane 01.
- Inventory filename: CONTENT/vertical-slices/power-electronics-basics/records/CLM-POWER_ELECTRONICS_BASICS-B.json
- Internal record ID: CLM_POWER_ELECTRONICS_BASICS_B

The match depends on separator normalization and stripping the version suffix. The stored identifiers are preserved. A human must confirm that this report row refers to the intended canonical Claim before the alias is accepted as a match.

## 4. Filename/internal-ID differences: corrected interpretation

The earlier ledger field counted 163 raw filename/internal-ID string differences as “mismatches”. Inspection of the worksheet shows:
- 160 are separator-only differences: hyphen versus underscore. After the documented comparison-only separator normalization, filename and internal ID match.
- 3 are genuine filename/internal-ID mismatches, all in web-systems-basics:
  - file CLM-A.json; internal ID CLM-WEB_SYSTEMS_BASICS-A
  - file CLM-B.json; internal ID CLM-WEB_SYSTEMS_BASICS-B
  - file CLM-C.json; internal ID CLM-WEB_SYSTEMS_BASICS-C

The 160 separator-only differences should be reported as naming-format variation, not semantic identity errors. The three web-systems-basics paths are genuine structural mismatches. Their internal record IDs are full, but filenames are generic. Do not rename files or alter references without bounded authorization, reference/Relation checks and regression tests.

The ledger implementation is being corrected to report raw differences, separator-only differences and genuine normalized mismatches separately.

## 5. Required next actions

1. Human-adjudicate the seven duplicate Claim groups; retain all historical rows until a decision is recorded.
2. Confirm the single Batch 44 separator-normalized alias against the canonical Claim and version.
3. Review the three web-systems-basics filename/internal-ID mismatches and authorize any path/reference correction separately.
4. Keep comparison normalization read-only. Never rewrite stored record IDs merely to make them match a report or filename.
5. Keep all Claims HOLD where evidence-use locators, source fit, specialist review or Human View remain unresolved.

## 6. Acceptance boundary

This reconciliation establishes 1,494/1,494 inventory Claims have at least one scored-report row and identifies the 7 duplicate groups, one alias and 3 genuine path/ID mismatches. It does not establish semantic correctness, source independence, Evidence Use precision, specialist approval, editorial/rights clearance, Human View or release readiness. M13 remains open.
