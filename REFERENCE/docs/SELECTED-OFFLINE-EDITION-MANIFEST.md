# Selected Offline Edition — manifest contract

## Purpose

A first-edition build must render only an explicit, approved, version-pinned allowlist. The complete-corpus offline build remains a separate engineering/recovery artifact and is not a public first-edition build.

## Selection manifest schema 1.1

Each record entry MUST pin:

- `record_id`;
- `record_version`;
- `record_type`;
- `type_version`;
- `schema`;
- `decision: INCLUDE`;
- explicit approval attestation (`status: APPROVED`, non-empty `approver`, non-empty decision `reference`);
- a complete list of direct dependencies, each pinned by the same five identity/profile fields.

The five pin fields distinguish record identity/version from its type profile and record schema. A record-version match alone is insufficient: a profile or schema change can alter interpretation while leaving the record version unchanged.

The builder rejects:

- HOLD/EXCLUDE or unknown decisions;
- absent approval attestations;
- missing, duplicate or stale record identities;
- multiple selected versions of one record;
- missing type/profile/schema pins;
- any type/profile/schema drift between the manifest and canonical record;
- unresolved, stale, omitted, undeclared or extraneous dependencies;
- Claim entries without selected Evidence Use;
- Evidence Use whose Claim or Source endpoint is not selected at its exact version.

Dependencies are never auto-added. The allowlist must explicitly enumerate the complete release closure.

## Build

Install and run tests:

```bash
pip install -e "REFERENCE[test]"
pytest -q REFERENCE/tests/test_selection_offline_edition.py
```

Build from an exact source revision:

```bash
python REFERENCE/build_offline_edition.py \
  --selection-manifest RELEASE/FIRST-EDITION-INCLUDE.json \
  --source-commit <full-40-character-git-sha> \
  --output first-edition
```

The CLI verifies that `--source-commit` exactly matches `git rev-parse HEAD` for the selected `--root` checkout before it reads or builds the selection. A mismatch, missing Git executable, or non-Git root is rejected; this prevents a caller-supplied SHA from being recorded as if it described different working-tree content. Build from the exact checkout revision, not from a modified or unversioned source tree.

The generated `edition-manifest.json` records the source commit, selection schema version, selection-manifest SHA-256, selected record identities, type/profile/schema pins, selected record count, and hashes for generated representations.

A successful build proves packaging and declared closure only. It does not prove factual truth, source passage support, rights clearance, editorial approval beyond the explicit attestation supplied, or public-release authorization. These remain separate release gates.

## Release boundary

No production INCLUDE manifest is supplied by this document. Synthetic fixtures and tests are not public content. Do not create an allowlist by inferring approval from repository publication status, CI, historical scores, or slice membership.
