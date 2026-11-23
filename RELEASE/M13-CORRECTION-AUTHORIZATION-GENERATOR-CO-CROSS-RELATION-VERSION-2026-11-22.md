# M13 Controlled Correction Authorization — Generator CO Cross-slice Relation Version — 2026-11-22

## Authorization

Owner approval received in the project conversation on 2026-11-22. This authorization is distinct from and additive to `M13-GENERATOR-CO-VERSION-LINEAGE-002`. Machine-readable authorization is recorded in `RELEASE/EDITORIAL-CORRECTION.json` as `M13-GENERATOR-CO-CROSS-RELATION-VERSION-003`.

## Finding

The current offline preflight reported `VAL-L3-REFERENCE-VERSION` for `REL-CROSS-CO-EMERGENCY-ESCALATION@1`: its participant reference points to `CLM-GENERATOR-CO-ALARM-EMERGENCY@1`, while the canonical current Claim is now version 2. The storage adapter correctly requires the referenced version to be present in the active record-version store. Historical Claim@1 remains preserved in Git history, not as an active versioned storage object.

## Exact authorized changes

1. Create `REL-CROSS-CO-EMERGENCY-ESCALATION@2` by preserving every field and semantic value from Relation @1 except:
   - set `record_version` to `2`;
   - update only the generator emergency Claim participant version from `1` to `2`.
2. Preserve the other participant, participant order, roles, relation_type, undirected direction, frame_ref, provenance and both existing Source provenance references unchanged.
3. Add one targeted regression that asserts the Relation @2 participant references the Claim @2 and that all other Relation semantics and participants are preserved.
4. Update this authorization, the machine-readable authorization registry, and PR #21 checkpoint documentation.

## Exact files

- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-EMERGENCY-ESCALATION.json`
- `REFERENCE/tests/test_m13_evidence_linkage_audit.py`
- `RELEASE/EDITORIAL-CORRECTION.json`
- `RELEASE/M13-CORRECTION-AUTHORIZATION-GENERATOR-CO-CROSS-RELATION-VERSION-2026-11-22.md`
- PR #21 description/checkpoint only

## Explicit exclusions

No other Relation, Claim, Evidence Use, Source, Context, Scope, slice, record count, coverage field, D/E/B score, risk status, publication allowlist, schema, validator, or release gate is changed. No main update, branch synchronization, PR merge, deployment, or publication approval is authorized.

## Acceptance

- Preserve Relation @1 unchanged in Git history.
- Verify Relation @2 differs only in record_version and the single authorized participant version.
- Run the targeted regression and full content preflight.
- Require Reference Tests, Release Conformance Gate, Offline Edition and M13 audit workflows to complete on one identical final HEAD.
- Verify PR #21 remains open/draft/unmerged and main remains unchanged.
- This correction only restores a resolvable cross-slice link; it does not establish publication approval or change epistemic assessment.
