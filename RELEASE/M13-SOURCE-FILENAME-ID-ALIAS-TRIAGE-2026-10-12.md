# M13 Source Filename/ID Alias Triage — 2026-10-12

Status: **61 Source alias rows reconciled structurally; no canonical ID migration authorized**

## Scope

Reviewed the Source-record subset of the M13 evidence-linkage audit artifact generated from the 4,832-record corpus snapshot.

## Results

- **61 Source records** are flagged as `separator_only_filename_id_alias`, distributed across **57 slices**.
- All 61 rows normalize to the same identity after removing hyphens and underscores. The recurring shape is a hyphenated filename stem (for example, `SRC-AGRICULTURAL_ENGINEERING_BASICS`) and an underscore-form internal `record_id` (for example, `SRC_AGRICULTURAL_ENGINEERING_BASICS`).
- Distribution: one alias each in 54 slices; two each in `fire-safety-basics` and `water-quality-basics`; three in `human-settlement-systems-basics`.
- The same static audit reported **zero unresolved `source_ref` targets** and zero `source_ref` targets resolving to the wrong record type across the corpus snapshot.
- The 618 referenced Source IDs and 618 Source record IDs match as a set after separator normalization. This is normalized identity reconciliation, not literal byte-for-byte ID equality.

## Interpretation

These 61 rows are systematic filename/internal-ID separator aliases, not 61 distinct missing-source defects. The audit's own implementation explicitly classifies a path stem/internal ID difference as this finding when the two normalize equally. The inspected preflight validates record identity and duplicate versions using the internal `(record_id, record_version)` pair; it does not require a filename stem to equal `record_id`.

That does not make the naming convention ideal or prove every reader/index/build consumer is path-independent. Before changing filenames or canonical IDs, inspect all path consumers and the repository's normative naming policy. Preserve stable internal IDs unless a separately bounded migration demonstrates necessity.

## Disposition

1. Keep the 61 rows as a documented naming-convention cleanup/reconciliation queue, not as evidence that the underlying Sources are false, missing, or unusable.
2. Do not mass-rename files, rewrite Source IDs, or rewrite Evidence Use references based only on these findings.
3. Continue source identity, URI duplication, exact-passage, source-independence, rights/attribution, and Human View checks separately. A valid link to a Source is not proof that the Source supports a Claim.
4. No canonical JSON, Source ID, Evidence Use, release allowlist, or publication status was changed by this triage.

## Evidence boundary

This is a structural review of the static audit output and the relevant preflight/audit code. It is not a full inspection of every reader/index consumer, a content-quality verdict, or release approval.
