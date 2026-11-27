# Selection-aware offline edition builder

Status: current implementation note. The normative machine-readable contract is
[Selected Offline Edition — manifest contract](docs/SELECTED-OFFLINE-EDITION-MANIFEST.md).

## Current manifest version

The builder accepts **schema_version 1.1 only**. The older 1.0 example previously
shown in this document is obsolete and is intentionally rejected by the current
implementation. Every selected record and every direct dependency must pin:

- record_id and record_version;
- record_type, type_version and schema;
- decision: INCLUDE;
- an explicit approval attestation with APPROVED status, approver and decision reference;
- the complete list of direct dependencies, each with the same identity/profile pins.

Do not infer approval from publication_status, completion_status, CI, historical
scores, or slice membership. Dependencies are not auto-added.

## Fail-closed behaviour

The builder rejects missing or duplicate canonical identities, stale versions,
multiple selected versions of one ID, missing approval, HOLD/EXCLUDE decisions,
type/profile/schema drift, unresolved or undeclared dependencies, unselected
dependencies, and incomplete Claim → Evidence Use → Source closure.

A selected build also requires a fresh or empty, non-symlinked output directory.
It refuses symlink paths and non-empty directories so an unexpected target or
files from an earlier full-corpus build cannot leak into a selection-only artifact.

## Invocation

Run from a clean Git checkout and keep the output directory outside the checkout:

```bash
python REFERENCE/build_offline_edition.py \
  --selection-manifest /path/to/approved-selection-1.1.json \
  --source-commit EXACT_FULL_40_CHARACTER_SHA \
  --edition-id first-edition-preview \
  --output /tmp/first-edition-preview
```

The CLI verifies that the supplied source commit exactly matches the checked-out
HEAD and rejects a dirty working tree. The generated edition manifest records the
source commit, selection-manifest digest, builder version and exact selected
record/profile identities.

A successful build proves only packaging and declared dependency closure. It does
not establish factual truth, source passage support, rights clearance, independent
expert review, Human View, or public-release authorization.

No production INCLUDE manifest is supplied here. No first-edition content is
approved by this implementation note.
