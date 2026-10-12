# M13 Record-Level Review: Filename/Internal-ID Mismatches — 2026-10-12

Status: **structural review completed for all six flagged rows; canonical remediation remains on hold**

## Scope and method

Reviewed the six `filename_internal_id_mismatch` rows from the static evidence-linkage audit against the actual JSON contents at M13 checkpoint `2349e6ff1b4c47ba6e99f0b5faff2f87f122792e`. All six are in `CONTENT/vertical-slices/web-systems-basics/records/`.

## Findings

| File path | Internal record ID | Record type |
|---|---|---|
| `CLM-A.json` | `CLM-WEB_SYSTEMS_BASICS-A` | Claim |
| `CLM-B.json` | `CLM-WEB_SYSTEMS_BASICS-B` | Claim |
| `CLM-C.json` | `CLM-WEB_SYSTEMS_BASICS-C` | Claim |
| `EU-A.json` | `EU-WEB_SYSTEMS_BASICS-A` | Evidence Use |
| `EU-B.json` | `EU-WEB_SYSTEMS_BASICS-B` | Evidence Use |
| `EU-C.json` | `EU-WEB_SYSTEMS_BASICS-C` | Evidence Use |

### Referential checks

- The three Evidence Use records each point to the matching fully qualified Claim ID: A → A, B → B, C → C.
- All three Evidence Use records point to `SRC-WEB_SYSTEMS_BASICS@1`; that Source record exists in the same slice.
- The three Claims' provenance also names `SRC-WEB_SYSTEMS_BASICS@1`.
- The referenced Source identifies MDN's “How the Web Works” page and stores its external URL.
- No broken internal `claim_ref` or `source_ref` was observed among these six records.

### Implementation check

Inspected `REFERENCE/preflight_content.py` and `REFERENCE/m13_evidence_linkage_audit.py` at the follow-up commit. Preflight loads JSON records and tracks duplicate identity by the internal `(record_id, record_version)` pair; it does not impose filename-equals-`record_id` as a release prerequisite. The linkage audit explicitly emits this finding when a file stem differs from the internal ID. Thus, these six rows are genuine path/ID discrepancies under the audit's naming heuristic, but are not by themselves proof of unresolved references or a failing preflight rule.

## Interpretation

The six findings are explained by abbreviated **filenames** (`CLM-A.json`, `EU-A.json`, etc.) paired with fully qualified internal IDs. The inspected references consistently use internal IDs rather than those abbreviated filenames. On this bounded sample, the finding is therefore a filename/identity convention mismatch, not evidence of a broken Claim → Evidence Use → Source link.

This does **not** establish that the evidence supports each Claim: each Evidence Use has only the generic description “Источник используется в пределах заявленного контекста и ограничений.” No exact passage, section locator, or Claim-specific support excerpt is recorded here. Source-fit review remains open for all three Claims.

## Disposition

1. **Do not rename files or rewrite canonical IDs in this pass.** First verify the repository's normative filename convention and every consumer that derives identity from a path (validators, manifests, reader/build scripts, indexes, and tests).
2. Keep this as a structural finding with a likely convention explanation, not a confirmed content defect or established release blocker.
3. Follow up with exact-passage validation for Claims A/B/C. Do not assign D/E/B ratings from this structural review alone.
4. No canonical JSON, Source record, Claim, Evidence Use, release allowlist, or publication status was changed by this review.

## Evidence boundary

This is a focused static record/link review at the stated commit. It is not an independent Human View, legal/rights review, complete source-fit assessment, or release approval.
