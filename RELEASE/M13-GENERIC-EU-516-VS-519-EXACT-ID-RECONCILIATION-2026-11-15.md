# M13 — exact generic Evidence Use denominator reconciliation (519 → 516)

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reconciliation HEAD before this report: `163db04bfe44e879ff6ec9515d95432276656bcc`  
State: **denominator discrepancy resolved by exact EU-ID set difference; no canonical changes in this report.**

## 1. Result

The apparent 519-versus-516 discrepancy is fully explained. The exact current 516-candidate set is a strict subset of the earlier 519-EU generic-material finding set. The only three IDs in the older set and absent from the current generic-EU scan are:

| Historical generic EU ID | Current canonical version | Claim | Source | Disposition |
|---|---:|---|---|---|
| `EU-ELECTRICAL_SAFETY_BASICS-A` | 2 | `CLM-ELECTRICAL_SAFETY_BASICS-A@1` | `SRC-ELECTRICAL_SAFETY_BASICS@1` | Generic material description replaced by Claim-specific locator/limits |
| `EU-ELECTRICAL_SAFETY_BASICS-B` | 2 | `CLM-ELECTRICAL_SAFETY_BASICS-B@1` | `SRC-ELECTRICAL_SAFETY_BASICS@1` | Generic material description replaced by Claim-specific locator/limits |
| `EU-ELECTRICAL_SAFETY_BASICS-C` | 2 | `CLM-ELECTRICAL_SAFETY_BASICS-C@1` | `SRC-ELECTRICAL_SAFETY_BASICS@1` | Generic material description replaced by Claim-specific locator/limits; Claim remains editorial HOLD |

Exact set arithmetic:

- Earlier generic-EU inventory: **519 unique EU IDs**.
- Current generic-EU coverage artifact: **516 unique EU IDs**.
- Earlier IDs absent from current generic set: **3**.
- Current IDs absent from earlier inventory: **0**.
- Therefore: **519 = 516 current generic candidates + 3 versioned electrical-safety EU remediations**.
- No orphan or ambiguous mapping is reported in the current artifact.

## 2. Evidence and provenance

### Earlier 519-row source inventory

- Reference implementation workflow run: `43262022587`.
- Artifact: `m13-evidence-linkage-audit`, ID `13964491415`.
- SHA-256: `sha256:d1ab1470fc0a6ff6d4866a8e0e870afb585f7c5cc4725bd2b8a0e28dabb365b0`.
- Its `evidence-linkage-findings.csv` contains 519 rows with finding `generic_material_description`.

### Current 516-row exact mapping

- Generic Evidence Use Report Coverage workflow run: `43682279201`.
- Artifact: `m13-generic-eu-report-coverage`, ID `14148673422`.
- SHA-256: `sha256:88fc30f9d8a1aa75fc6607d08008434d4fdb8308b5bb6b4b0b0face3de620dfc`.
- Its JSON contains 516 unique EU IDs, each mapped to one Claim; 0 unmapped and 0 ambiguous.
- The current artifact reports 516/516 exact Claim-ID text mentions and 516/516 source-review filename mentions.

### Why exactly three disappeared from the generic set

The three electrical-safety EU records are now version 2. The bounded authorization is recorded in `RELEASE/M13-CORRECTION-AUTHORIZATION-ELECTRICAL-SAFETY-2026-11-13.md`; the controlled result is documented in `RELEASE/M13-ELECTRICAL-SAFETY-EVIDENCE-REMEDIATION-2026-11-13.md`.

That correction:
- changed only the three named EU records from v1 to v2;
- preserved Claim v1 and Source v1 references;
- added Claim-specific NIOSH section references and explicit support limits;
- changed no Claim wording, Source record, score, or publication decision.

The current canonical files confirm all three EU records are v2, and all three linked Claims remain v1. In particular, Claim C remains broader than its source and is still HOLD; its EU v2 explicitly records that limitation. The three records are therefore **remediated out of the generic-description finding**, not accepted or release-cleared.

## 3. Reconciled work populations

The earlier 519 set was divided into a 140-Claim high-consequence subset and a 379-Claim residual set. The three electrical-safety EU IDs belong to the 140 high-consequence subset, not the residual 379.

| Population | Earlier count | Current disposition |
|---|---:|---|
| High-consequence generic EU | 140 | 3 electrical-safety EU records versioned; 137 remain in current generic-EU set |
| Residual generic EU | 379 | 379 remain; unchanged by the three electrical-safety corrections |
| Priority second-pass subset of residual 379 | 20 | All 20 are present in the current 516 artifact; reuse prior passage review, do not repeat source search |
| Residual records still awaiting the deeper second-pass work | 359 | 379 − 20; next exact remediation-ledger population |

The 20 priority Claims were checked against the current 516-candidate artifact by exact Claim ID: **20/20 present**. Their report remains a deeper second-pass review, not a new or disjoint population. Existing findings, partial-support cases and rights holds must be imported into the next ledger.

The 47 strict passage/locator Claims are a separate overlapping set, not an additional population. Their corrected exact-ID ledger and Packages 01–06 remain authoritative; all 47 remain HOLD. Do not add 47 to 516 or re-run their reviews.

## 4. Interpretation boundary

The current artifact's 516/516 report mentions are text/filename coverage only. They are not semantic confirmation that the exact Claim version, EU version, Source version and source passage were substantively reviewed. Its `human_confirmation_required` flag remains true for every candidate.

The 516 count is a current structural generic-EU candidate count, not a count of invalid Claims and not a count of unreviewed Claims. A prior report mention does not itself clear a case. Rights, exact passage support, source identity/independence, canonical locator, specialist review and Human View remain separate gates.

## 5. Next controlled action

Build the deduplicated **359-row residual remediation ledger** from the exact 379 residual EU-ID population, excluding the already reviewed priority 20 and importing prior reports, exact proposed locator text, support disposition, source identity/independence, rights state and any existing HOLD. Reuse existing work; do not repeat source searches. The ledger is a proposal/routing artifact only.

No canonical Claim/Evidence Use/Source changes are authorized by this reconciliation. The three electrical-safety v2 corrections are already covered by their own bounded authorization. Any new canonical changes require a separate bounded authorization and versioned regression plan.

## 6. Overall status

The 516-versus-519 denominator discrepancy is **RESOLVED**. The residual remediation ledger, canonical locator corrections, rights adjudication, semantic human confirmation, independent specialist review and Human View remain open. M13 remains **OPEN / NOT RELEASE-READY**; PR #21 remains Draft/unmerged and `main` is unchanged.
