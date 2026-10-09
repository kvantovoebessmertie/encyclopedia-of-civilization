# M12 Unified Debt Map — 2026-10-09

## Current state

M12 addresses the human-factors findings carried forward as OPEN by M11. Content corrections are implemented on isolated branch `m12-human-factors-source-and-human-view-2026-10-09`, based on M11 candidate `d4b4b88d4a6cb1214e5fd1c87b42a468f4b117bb`.

The pre-closure candidate `e319de7aed72a17117eb41a2da2ba3689468612b` passed Reference implementation tests (#2953), Release Conformance Gate (#2673), and Offline Edition (#2443) on the same exact SHA; independent tree verification also passed. This closure-record commit creates a successor HEAD, so those results are historical evidence only. M12 is CLEAN only if all three workflows pass on the exact HEAD containing this debt map and the independent final-state checks pass. PR #20 must remain open/draft/unmerged and `main` must remain untouched.

## Findings and disposition

- `M12-HF-001` — README was a machine-facing stub. **Resolved within the authorized scope; final exact-head CI and closure checks apply to the candidate as a whole.**
- `M12-HF-002` — three Evidence Use descriptions were generic. **Resolved: claim-specific descriptions and explicit evidence boundaries are in place.**
- `M12-HF-003` — Claim wording exceeded the previously recorded locator's independently verified support. **Resolved within scope: Claims are bounded to the verified official NASA JSC page.**
- `M12-HF-004` — dedicated regression did not protect reader-facing content or source boundaries. **Resolved: dedicated regression strengthened; final exact-head Reference workflow remains a closure gate.**
- `M12-HF-005` — previous locator could not be independently retrieved. **Resolved within this correction scope by updating the existing Source record's locator to the verified official NASA JSC Human Factors & Performance page. The old locator is not declared broken.**

## Explicit residual limitations

- The slice uses one official NASA page for its three Claims. This is a bounded introductory slice, not independent multi-source triangulation.
- The NASA page is a Johnson Space Center capability overview with a human-spaceflight focus; do not present it as a universal standard across every industry or jurisdiction.
- Human View is desk-based; no live novice usability study is claimed.
- Domain-specific engineering decisions, certification, comprehensive risk assessment and local requirements remain outside this slice's scope.

## Protected invariants verified on pre-closure candidate `e319de7`

No new/deleted Records, no new Record types, no Context/Scope changes, no Relation changes, no unrelated slice changes, and no architecture changes. Source record ID and provenance method, Claim IDs, Evidence Use IDs, claim/source refs, roles and other IDs remain unchanged. Independent base-to-candidate comparison found exactly 15 authorized changed paths. Coverage remained unchanged at 483 slices / 4,831 record JSONs / 19 Record types. The protected cross-slice Relation remained unchanged. These invariants were rechecked on `e319de7`; after this documentation-only commit, confirm the final successor still has exactly 15 changed blob paths, the same corpus counts, unchanged coverage, unchanged Context/Scope, unchanged protected Relation, and unchanged record shape.

## CI evidence on pre-closure candidate `e319de7`

On exact HEAD `e319de7aed72a17117eb41a2da2ba3689468612b`:
- Reference implementation tests #2953: **PASS**
- Release Conformance Gate #2673: **PASS**
- Offline Edition #2443: **PASS**

All three passed on the same exact SHA. The successor HEAD containing this debt map must pass all three workflows again on the same SHA; earlier intermediate runs are not acceptance evidence.

## Closure gates

M12 can close CLEAN only after:
1. all five findings are verified resolved within scope;
2. exact diff and all structural invariants are independently checked on the successor HEAD;
3. corpus coverage remains unchanged;
4. targeted regression and all three CI workflows pass on one identical successor HEAD;
5. PR base/head/state and unchanged `main` are independently verified.

**Closure decision rule: M12 is CLEAN if and only if all five closure gates below pass on the exact final HEAD containing this debt map.** Do not create another commit after those gates pass unless all three CI workflows are rerun on that new HEAD.

## Preflight process deviation and disposition

An early CI attempt on an intermediate M12 HEAD failed the wave-safety preflight because the slice was missing from the top-level `authorized_slices` registry in `RELEASE/EDITORIAL-CORRECTION.json`. This was an authorization-manifest omission, not a content/schema failure. The manifest now includes `human-factors-basics` in the top-level list and the dedicated `m12_authorization` entry; existing registry ordering and previous entries were preserved. All three required workflows passed after that fix on `b619fb5` and passed again on pre-closure HEAD `e319de7`. A new exact-head run is mandatory after this closure-record commit.
