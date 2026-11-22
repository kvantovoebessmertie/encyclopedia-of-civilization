# M13 scored-Claim ledger duplicate reconciliation — 2026-11-22

## Status

**HISTORICAL RECONCILIATION PARTIAL — existing adjudications incorporated; two historical E conflicts remain unresolved.**

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
- Seven duplicate-ID groups containing 14 report rows. Six groups have different historical score vectors; one has identical vectors.
- One separator-normalized match, manually confirmed against the exact Claim → Evidence Use → Source references (details below).
- Evidence-linkage structural triage: 1,117 findings across 4,865 record files, including 496 generic-material-description candidates, 493 separator-only filename-ID aliases, 75 duplicate-Source-URI candidates, 47 Source-identity-sentence candidates and 6 documented filename-ID aliases.

These are generated accounting and triage outputs. They do not establish semantic duplicate identity, validate evidence, certify prior scores, or prove that every Claim received a final independent assessment.

## Duplicate scored-report groups

Seven Claim IDs occur in two scored reports each. Six groups contain different historical D/E/B vectors; one group has identical vectors. These are not six newly open adjudications: the existing comparison and successor disposition resolve five disputed dimensions, leaving only Water A-E and Water C-E unresolved.

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

### Interpretation and existing adjudication

The repository already contains a row-level historical comparison and an explicit independent AI rubric adjudication in `RELEASE/M13-REPEATED-ASSESSMENT-COMPARISON-2026-11-18.md`, followed by the bounded Water A/C evidence-recovery disposition in `RELEASE/M13-WATER-A-C-HISTORICAL-EVIDENCE-RECOVERY-DISPOSITION-2026-11-18.md`. This report incorporates those decisions and does not reopen them.

- **Five disputed dimensions are adjudicated for historical reconciliation:** Nuclear A D1; Nuclear B B3; Nuclear C D2/B2; Water B D2. These are separate successor decisions. Both original rows remain preserved; the current Claim worksheet remains blank.
- **Two disputed dimensions remain unresolved:** Water A E2/E3 and Water C E2/E3. The historical WHO passages and reviewer-use evidence were not recoverable to the required provenance standard. Preserve both rows and do not select E2 or E3.
- **Emergency-disinfection D** has identical 3/3/3 rows. Preserve both rationales but count this as one repeated assessment identity, not two independent votes.
- The differences in Batch 12/17 and Batch 21/27 do not establish a general "latest report wins" rule. The explicit successor adjudications above govern only the five named dimensions.

No score was selected, averaged, deleted, or overwritten by this new ledger-reconciliation package. It records the already documented adjudications and remaining open dimensions.

## Identifier reconciliation — manual confirmation completed

The ledger contains one separator-normalized match:
- Report ID: `CLM-POWER_ELECTRONICS_BASICS_B@1`
- Inventory file: `CONTENT/vertical-slices/power-electronics-basics/records/CLM-POWER_ELECTRONICS_BASICS-B.json`
- Internal ID: `CLM_POWER_ELECTRONICS_BASICS_B`

**Identity confirmed; stored identifiers preserved.**

The report row is the same canonical Claim, based on the following independent, exact repository evidence:
- The report's row 9 is in the `power-electronics-basics` lane and describes the Claim as the statement about power-electronic converters and AC/DC quantities.
- The canonical file `CONTENT/vertical-slices/power-electronics-basics/records/CLM-POWER_ELECTRONICS_BASICS-B.json` contains internal ID `CLM_POWER_ELECTRONICS_BASICS_B@1` and the matching statement: “Power-electronic converters can change electrical quantities such as voltage, current, frequency, or the form of AC and DC power.”
- The corresponding canonical Evidence Use `EU_POWER_ELECTRONICS_BASICS_B@1` explicitly references `CLM_POWER_ELECTRONICS_BASICS_B@1` and `SRC_POWER_ELECTRONICS_BASICS@1`.
- That Source is the U.S. Department of Energy “Power Electronics” reference, matching the source described in the Batch 44 review row.
- The ledger reports exactly one inventory candidate for this separator-normalized report ID; no competing canonical Claim match was found.

Disposition: treat the report identifier and canonical identifier as a confirmed separator-only alias for accounting purposes. Preserve the exact stored report ID and canonical record ID; do not rewrite either identifier and do not create a normalized ID in canonical content. This confirmation resolves identity only; it does not change the report's D/E/B assessment, evidence-quality finding, or HOLD status.

## Required disposition before claiming a reconciled final score ledger

1. DONE: the seven groups and 14 report rows have been compared against exact Claim@1 / EU@1 / Source@1 historical provenance in `M13-REPEATED-ASSESSMENT-COMPARISON-2026-11-18.md`.
2. DONE: five disputed dimensions have separate historical successor adjudications: Nuclear A-D1, Nuclear B-B3, Nuclear C-D2/B2, Water B-D2. Preserve both source rows and do not copy these results into the current worksheet.
3. OPEN: Water A-E and Water C-E remain `UNRESOLVED — HISTORICAL EVIDENCE NOT RECOVERABLE`; preserve E2 and E3 without choosing a winner. The bounded recovery disposition is documented in `M13-WATER-A-C-HISTORICAL-EVIDENCE-RECOVERY-DISPOSITION-2026-11-18.md`.
4. DONE: Emergency-disinfection D's identical 3/3/3 rows are one repeated assessment identity, not two independent votes; retain both rationales.
5. DONE: manually confirm the separator-normalized power-electronics ID match against the exact Claim statement, Evidence Use references and DOE Source identity; preserve both stored identifiers unchanged.
6. Regenerate the scored ledger and assert: 1,494 inventory Claims, 1,494 reconciled Claim identities, zero unmatched report rows, seven preserved repeat groups with linked adjudication status, and no unresolved identity aliases.
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

**Historical repeat reconciliation: PARTIAL — five disputed dimensions adjudicated; Water A-E and Water C-E remain unresolved; Emergency D retained as one repeated assessment identity.**

**Identifier confirmation: PASS (one separator-normalized alias manually confirmed; no stored identifier changed).**

**M13 substantive audit: NOT CLOSED by this report.** This artifact narrows the remaining ledger-reconciliation work; it does not certify the epistemic quality of the underlying assessments or replace high-consequence, evidence-independence, Human View, Relation and independent-audit gates.
