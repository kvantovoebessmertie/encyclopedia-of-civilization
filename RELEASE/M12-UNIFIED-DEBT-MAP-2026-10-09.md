# M12 Unified Debt Map — 2026-10-09

## Current state

M12 addresses the human-factors findings carried forward as OPEN by M11. Content corrections are implemented on isolated branch `m12-human-factors-source-and-human-view-2026-10-09`, based on M11 candidate `d4b4b88d4a6cb1214e5fd1c87b42a468f4b117bb`.

The three required workflows passed on prior candidate HEAD `b619fb52331af399e954afa0c4881de4e6814750`: Reference implementation tests, Release Conformance Gate, and Offline Edition. The audit/debt-map status update creates a successor HEAD; therefore the three workflows must pass again on that same successor SHA before M12 can close CLEAN. PR #20 must remain open/draft/unmerged and `main` must remain untouched.

## Findings and disposition

- `M12-HF-001` — README was a machine-facing stub. **Correction implemented; prior candidate scope/tree verification passed. Successor-head acceptance pending.**
- `M12-HF-002` — three Evidence Use descriptions were generic. **Claim-specific descriptions implemented; prior candidate scope/tree verification passed. Successor-head acceptance pending.**
- `M12-HF-003` — Claim wording exceeded the previously recorded locator's independently verified support. **Claims narrowed to the current official NASA JSC page; prior candidate scope/tree verification passed. Successor-head acceptance pending.**
- `M12-HF-004` — dedicated regression did not protect reader-facing content or source boundaries. **Regression strengthened; Reference workflow passed on prior candidate. Successor-head rerun pending.**
- `M12-HF-005` — previous locator could not be independently retrieved. **Resolved within this correction scope by updating the existing Source record's locator to the verified official NASA JSC Human Factors & Performance page. The old locator is not declared broken.**

## Explicit residual limitations

- The slice uses one official NASA page for its three Claims. This is a bounded introductory slice, not independent multi-source triangulation.
- The NASA page is a Johnson Space Center capability overview with a human-spaceflight focus; do not present it as a universal standard across every industry or jurisdiction.
- Human View is desk-based; no live novice usability study is claimed.
- Domain-specific engineering decisions, certification, comprehensive risk assessment and local requirements remain outside this slice's scope.

## Protected invariants verified on prior candidate

No new/deleted Records, no new Record types, no Context/Scope changes, no Relation changes, no unrelated slice changes, and no architecture changes. Source record ID and provenance method, Claim IDs, Evidence Use IDs, claim/source refs, roles and other IDs remain unchanged. Independent base-to-candidate comparison found exactly 15 authorized changed paths. Coverage remained unchanged at 483 slices / 4,831 record JSONs / 19 Record types. The protected cross-slice Relation remained unchanged. These invariants must be rechecked on the successor HEAD after the status update.

## CI evidence on prior candidate

On exact HEAD `b619fb52331af399e954afa0c4881de4e6814750`:
- Reference implementation tests #2949: **PASS**
- Release Conformance Gate #2672: **PASS**
- Offline Edition #2439: **PASS**

All three passed on the same exact SHA. Earlier runs on intermediate SHAs are not acceptance evidence.

## Closure gates

M12 can close CLEAN only after:
1. all five findings are verified resolved within scope;
2. exact diff and all structural invariants are independently checked on the successor HEAD;
3. corpus coverage remains unchanged;
4. targeted regression and all three CI workflows pass on one identical successor HEAD;
5. PR base/head/state and unchanged `main` are independently verified.

Until those successor-head gates are complete: **M12 OPEN — content correction and prior-head CI PASS; final acceptance pending.**

## Preflight process deviation and disposition

An early CI attempt on an intermediate M12 HEAD failed the wave-safety preflight because the slice was missing from the top-level `authorized_slices` registry in `RELEASE/EDITORIAL-CORRECTION.json`. This was an authorization-manifest omission, not a content/schema failure. The manifest now includes `human-factors-basics` in the top-level list and the dedicated `m12_authorization` entry; existing registry ordering and previous entries were preserved. All three required workflows passed after that fix on `b619fb5`. The successor-head rerun remains mandatory because the status documentation has since changed.
