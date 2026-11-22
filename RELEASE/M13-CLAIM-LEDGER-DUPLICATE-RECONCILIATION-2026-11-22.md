# M13 scored-Claim ledger duplicate reconciliation — 2026-11-22

## Status

**RECONCILIATION REQUIRED — no score adjudication performed.**

This report reconciles the generated scored-Claim ledger and audit worksheet from the exact M13 source revision `8ad7c00020c9a85a5f916987dc2939a18bd11807`. It is a report-only audit artifact. It does not alter canonical records, historical review reports, D/E/B scores, risk status, Relations, publication status, or release decisions.

## Evidence snapshot

Source revision: `8ad7c00020c9a85a5f916987dc2939a18bd11807`.

Exact-head GitHub Actions:
- Reference implementation tests: run [45060967944](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45060967944) — PASS.
- Release Conformance Gate: run [45060967951](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45060967951) — PASS.
- Offline Edition: run [45060967899](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45060967899) — PASS.

The Reference Tests run generated the following artifacts:
- `m13-scored-claim-reconciliation-ledger` (artifact 14769571064)
- `m13-claim-audit-worksheet` (artifact 14768673939)
- `m13-evidence-linkage-audit` (artifact 14768539359)

The generated snapshots report:
- 4,865 record files scanned; 1,494 Claim records.
- 1,501 scored report rows and 1,494 unique normalized report IDs.
- All 1,494 inventory Claims have at least one scored-row match; zero unmatched report rows.
- Seven duplicate-ID groups containing 14 report rows.
- One separator-normalized match requiring manual identity confirmation.
- Evidence-linkage structural triage: 1,117 findings across 4,865 record files, including 496 generic-material-description candidates, 493 separator-only filename-ID aliases, 75 duplicate-Source-URI candidates, 47 Source-identity-sentence candidates and 6 documented filename-ID aliases.

These are generated accounting and triage outputs. They do not establish semantic duplicate identity, validate evidence, certify prior scores, or prove that every Claim received a final independent assessment.

## Duplicate scored-report groups

Seven Claim IDs occur in two scored reports each. Six groups contain different D/E/B vectors; one group has identical vectors.

| Claim ID | Reports | First vector | Second vector | Difference |
|---|---|---:|---:|---|
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A` | Batch 12 / Batch 17 | 1/1/2 | 2/1/2 | D +1 |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B` | Batch 12 / Batch 17 | 2/1/3 | 2/1/2 | B −1 |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C` | Batch 12 / Batch 17 | 1/1/3 | 2/1/2 | D +1; B −1 |
| `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` | Batch 21 / Batch 27 | 3/3/3 | 3/3/3 | Identical |
| `CLM-WATER_TREATMENT_BASICS-A` | Batch 21 / Batch 27 | 2/2/3 | 2/3/3 | E +1 |
| `CLM-WATER_TREATMENT_BASICS-B` | Batch 21 / Batch 27 | 2/3/3 | 3/3/3 | D +1 |
| `CLM-WATER_TREATMENT_BASICS-C` | Batch 21 / Batch 27 | 2/2/3 | 2/3/3 | E +1 |

Exact report paths:
- Nuclear physics: `RELEASE/M13-CLAIM-REVIEW-BATCH-12-NUCLEAR-PHYSICS-2026-10-09.md` and `RELEASE/M13-CLAIM-REVIEW-BATCH-17-NUCLEAR-AND-WATER-2026-10-10.md`.
- Water treatment: `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` and `RELEASE/M13-CLAIM-REVIEW-BATCH-27-WATER-TREATMENT-2026-10-10.md`.

### Interpretation

1. The three nuclear-physics Claims have score-vector disagreement between two reports. The rationales also differ in emphasis, especially on claim depth and whether generic IAEA Evidence Use descriptions demonstrate claim-specific support.
2. The emergency water-disinfection Claim has identical scores in both reports, but duplicate provenance still needs an explicit disposition so the ledger does not silently count two report rows as two independently assessed Claims.
3. The three water-treatment Claims have one-dimension score changes between the two reports. Batch 27 rationales cite a more differentiated WHO/EPA evidence framing; this observation is not, by itself, authorization to overwrite Batch 21 or designate Batch 27 as canonical.
4. No "latest report wins" rule is evidenced in the ledger contract. Therefore no row is selected, averaged, or deleted here.

## Identifier requiring manual confirmation

The ledger contains one separator-normalized match:
- Report ID: `CLM-POWER_ELECTRONICS_BASICS_B@1`
- Inventory file: `CONTENT/vertical-slices/power-electronics-basics/records/CLM-POWER_ELECTRONICS_BASICS-B.json`
- Internal ID: `CLM_POWER_ELECTRONICS_BASICS_B`

The match is comparison-only. Stored identifiers must remain unchanged until a human verifies that the report row and inventory Claim are the same record. Do not normalize or rewrite the canonical identifier to force a match.

## Required disposition before claiming a reconciled final score ledger

1. Review each of the seven groups against the source Claim version and the complete two report rows.
2. Record whether the reports are duplicate coverage, a deliberate reassessment, or a superseding review. Cite the exact reason and source revision; do not infer this from batch number alone.
3. For the six differing vectors, obtain an explicit reviewer/editor adjudication identifying the accepted assessment or a new reassessment. Preserve both historical reports and their rationales.
4. For the identical emergency-water row, record one assessment identity and explain how the duplicate report provenance is represented.
5. Manually confirm the separator-normalized power-electronics ID match without changing stored identifiers.
6. Regenerate the scored ledger and assert: 1,494 inventory Claims, 1,494 reconciled Claim identities, zero unresolved duplicate groups, zero unmatched report rows, and a traceable provenance decision for every previously duplicated row.
7. Keep the evidence-linkage flags as a separate human-review queue. In particular, generic-material-description and duplicate-URI candidates are not automatic proof of invalid evidence.

## Boundaries preserved

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope record changed.
- No historical report was edited or removed.
- No D/E/B score was assigned or changed.
- No Relation semantics or count was changed.
- No identifier normalization was written back to canonical data.
- No publication or release decision was made.
- `main` was not modified; PR #21 remains Draft/unmerged.

## Acceptance

**Accounting coverage: PASS (all 1,494 Claims have at least one scored-row match).**

**Duplicate reconciliation: OPEN (7 groups / 14 rows; six score-vector disagreements).**

**Identifier confirmation: OPEN (one separator-normalized match).**

**M13 substantive audit: NOT CLOSED by this report.** This artifact narrows the remaining ledger-reconciliation work; it does not certify the epistemic quality of the underlying assessments or replace high-consequence, evidence-independence, Human View, Relation and independent-audit gates.
