# First Edition — selection output symlink isolation hardening

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Implementation commits:
- `5843f112d5c77b32861de83cdc0471e066af5e8c`
- `40f498cdcf561d9449907682f6223c50bbccda65`
- `e41fecbdcfd7ca8200e370c3300ec04bf4311056`
- `a75a916dc61b2f881ec9ad2b0ebba9b1aa4e08ff`

## 1. Issue

The selected offline builder already refused a non-empty output directory and refused a regular file as the output path. An empty directory reached through a symbolic link could still pass those checks and redirect selected build output to an unexpected target.

Although the output path is operator-supplied, selection builds are a release-isolation boundary. The builder should fail closed rather than follow an unexpected output symlink.

## 2. Changes

- `REFERENCE/src/encyclopedia_reference/selection.py`: reject `output_dir.is_symlink()` before the existence/directory/emptiness checks and before any output is written.
- `REFERENCE/tests/test_selection_output_isolation.py`: add a regression test using a symlink to an empty target directory; the builder must raise and the target must remain empty.
- `REFERENCE/docs/SELECTED-OFFLINE-EDITION-MANIFEST.md`: document that symlinked output paths are rejected.
- `REFERENCE/SELECTION-MANIFEST.md`: update the fail-closed contract to include symlink rejection.

Existing protections remain:
- non-empty output directory is rejected without changing its contents;
- regular file output path is rejected without overwriting the file;
- absent or existing empty, non-symlinked directory is the only accepted output state.

## 3. Workflow trigger alignment

The browser workflow's `push.paths` already included the selection builder and its regression tests, but its `pull_request.paths` did not. The PR path filter now includes the same selection-builder, output-isolation test, manifest guide and builder entry-point paths. This prevents selection-related changes in a pull request from silently skipping the browser workflow and aligns the branch's four-workflow exact-head verification path.

Workflow change commit: `43f3ca61b3cd53ab56eba51c4678ca47ccfe2d34`.

## 4. Verification boundary

The new symlink regression is included in the existing explicit Offline Edition test command and full reference test discovery. Exact-head workflows must be checked on the final report commit; no CI result from an earlier commit is transferred to a later HEAD.

## 5. Protected state

- No canonical Claim, Evidence Use, Source, Context, Scope or Relation was changed.
- No production INCLUDE manifest or allowlist was created.
- No HOLD was promoted.
- No rights, editorial, specialist, Human View or owner gate was bypassed.
- No deployment, publication, merge, rebase, retarget or `main` change was performed.
- PR #22 remains Draft and unmerged.

## 6. Result

Selection output isolation now rejects non-empty directories, regular-file paths and symbolic-link paths before writing. The additional test protects the empty-target symlink case, which the previous non-empty-directory regression could not detect.
