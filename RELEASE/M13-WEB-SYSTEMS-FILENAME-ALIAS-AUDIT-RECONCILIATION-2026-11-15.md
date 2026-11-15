# M13 web-systems filename alias audit reconciliation

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Finding

The exact-head M13 evidence-linkage artifact at the 2e7c9d3 checkpoint reported six high-severity `filename_internal_id_mismatch` rows in `web-systems-basics`:

- `CLM-A.json` → `CLM-WEB_SYSTEMS_BASICS-A`
- `CLM-B.json` → `CLM-WEB_SYSTEMS_BASICS-B`
- `CLM-C.json` → `CLM-WEB_SYSTEMS_BASICS-C`
- `EU-A.json` → `EU-WEB_SYSTEMS_BASICS-A`
- `EU-B.json` → `EU-WEB_SYSTEMS_BASICS-B`
- `EU-C.json` → `EU-WEB_SYSTEMS_BASICS-C`

The slice's dedicated regression already verifies the six internal IDs, Claim-to-Evidence Use links, and Evidence Use-to-Source links. The checkpoint `M13-WEB-SYSTEMS-EVIDENCE-PINPOINT-CHECKPOINT-2026-10-12.md` records the slice's short filenames and the prior decision not to mass-rename canonical records without a bounded migration. The names are therefore documented legacy filename aliases, not evidence of six broken references.

## Correction

The static evidence-linkage audit now carries an exact six-entry path-to-record-ID allowlist for these documented aliases. A matching entry is emitted as `documented_filename_id_alias` at medium severity, preserving visibility for future naming cleanup without inflating the high-severity defect count. A changed internal ID, an unexpected path, or any other unrecognized mismatch continues to produce the original high-severity `filename_internal_id_mismatch`.

The regression asserts exactly these six aliases, their expected internal IDs, their medium severity, and that the slice has no residual high-severity filename mismatch. The existing generic fixture still asserts that an unrecognized mismatch remains high severity.

## Scope and limits

No canonical JSON record, filename, Claim, Evidence Use, Source, reference, Relation, coverage count, publication status, score, or release allowlist was changed. No path migration is performed. This is an audit-classification correction only; it does not establish source passage support, rights clearance, D/E/B scores, Human View, or publication readiness.

## Verification required

Run the dedicated evidence-linkage regression, full Reference Tests, content preflight, Release Conformance Gate, and Offline Edition on one identical final HEAD. Reconcile the new audit artifact and verify that only the six documented aliases changed classification while all other high-severity findings remain visible. Keep PR #21 Draft/unmerged and `main` unchanged.
