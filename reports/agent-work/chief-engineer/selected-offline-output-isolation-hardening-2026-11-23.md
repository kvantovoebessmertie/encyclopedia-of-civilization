# First Edition — selection-build isolation hardening and manifest contract alignment

Date: 2026-11-23
Repository: kvantovoebessmertie/encyclopedia-of-civilization
Branch: mvp-public-contribution-design-2026-10-11
Starting verified MVP baseline: 49c117968b30d2b15c5d4d756046ee83886da5b4
Implementation commits: 19915b67cd5121f29b70160b10eb3766c0cc79f7; b30308fb5a1abd96e37bc8988ce4ad091a3560b1; 213a824e31cb68604d4c549c0a3a0276ae81f15c; 6934cac057d5b4df1cf452d1a3ab302abc8a3928; 55535a4231841c1fd57ac06f4064553a8c546e32
Report status: committed on this branch; exact-head verification is tracked in GitHub Actions.
Status: IMPLEMENTATION COMPLETE; exact-HEAD CI verification required

## 1. Problem found

The selection-aware offline builder already enforced exact record/version/profile pins, explicit INCLUDE approval attestations, declared dependency closure, Claim → Evidence Use → Source closure, and source-commit/clean-tree verification.

However, its final build delegated to the shared offline writer, which creates the output directory with exist_ok=True and overwrites its standard output files without checking for unrelated files already present. Reusing an output directory that previously held a full-corpus build could therefore leave stale or unselected files alongside the selected artifact. This is a release-isolation risk even though records.json itself is regenerated from the approved selection.

A second documentation inconsistency was found: REFERENCE/SELECTION-MANIFEST.md still described obsolete schema 1.0 and omitted the type/profile/schema pins required by the current schema 1.1 implementation.

## 2. Changes implemented

### Selection output isolation
File: REFERENCE/src/encyclopedia_reference/selection.py

Before any selected artifact is written, the builder now:
- accepts an output path that does not exist;
- accepts an existing empty directory;
- rejects a non-directory output path;
- rejects any non-empty output directory.

The rejection occurs after manifest and dependency validation but before the writer creates or changes any output. This prevents stale full-corpus artifacts, unrelated files, and residual data from being silently carried into a selection-only build.

### Regression coverage
New file: REFERENCE/tests/test_selection_output_isolation.py

Two tests verify:
- a non-empty output directory is rejected and its existing file remains byte-for-byte unchanged;
- a regular file cannot be used as the output directory and is not overwritten.

### CI gate
File: .github/workflows/offline-edition.yml

The Offline Edition workflow now explicitly runs:
- the existing full-corpus offline edition tests;
- selection-aware builder tests;
- output-isolation regression tests.

The diagnostic full-corpus build remains separate from the opt-in selection build. No production selection manifest was introduced.

### Documentation consistency
Files:
- REFERENCE/SELECTION-MANIFEST.md
- REFERENCE/docs/SELECTED-OFFLINE-EDITION-MANIFEST.md

The quick guide now states that schema 1.1 is the only accepted version and that the former 1.0 example is obsolete. It describes all five identity/profile pins, explicit approval, dependency closure, clean Git/source-commit checks, and fresh/empty output-directory requirements. The detailed contract also documents output isolation.

## 3. Verification boundary

On intermediate HEAD 6934cac057d5b4df1cf452d1a3ab302abc8a3928, the Offline Edition workflow completed successfully. Its job log confirms that the new “Test selection-aware offline edition and output isolation” step passed, followed by the full-corpus diagnostic build, manifest verification and artifact upload.

The subsequent documentation-only correction advanced the branch to 55535a4231841c1fd57ac06f4064553a8c546e32. Final verification must be read from Actions runs attached to the final report commit, not transferred from the intermediate HEAD.

Required exact-head workflows:
- Offline Edition
- Reference implementation tests
- Release Conformance Gate
- MVP Contribution Form Browser Tests

## 4. Scope and safety

- No canonical Claim, Evidence Use, Source, Context, Scope or Relation was changed.
- No production INCLUDE manifest, allowlist or publication decision was created.
- No HOLD record was promoted.
- No rights, editorial, specialist, Human View or owner release gate was bypassed.
- The full-corpus offline artifact remains diagnostic only.
- PR #22 remains Draft and unmerged.
- PR #22 base is not changed or rebased in this work.
- main is not modified.

## 5. Result

The selection-only builder now fails closed when an output directory could carry stale files from another build. The risk is covered by explicit regression tests and the Offline Edition workflow. The manifest documentation matches the implemented schema 1.1 contract. This is a technical hardening result, not a first-edition content approval or public-release authorization.
