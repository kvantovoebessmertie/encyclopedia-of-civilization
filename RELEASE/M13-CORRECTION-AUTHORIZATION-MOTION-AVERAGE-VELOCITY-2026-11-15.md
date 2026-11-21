# M13 bounded correction authorization — motion basics average velocity terminology

Date: 2026-11-15
Authorization ID: M13-MOTION-AVERAGE-VELOCITY-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `16fbffd759f13c76f5039d15982d5e0b5ed6e2a6`

## Finding

`CLM-MOTION_BASICS-B@1` currently states: “Средняя скорость определяется отношением изменения положения к соответствующему интервалу времени.”

This conflates two distinct physical quantities. OpenStax Physics §2.2 “Speed and Velocity” defines average speed as distance traveled divided by elapsed time, and average velocity as displacement divided by elapsed time. It explicitly states that speed is scalar while velocity is a vector and that the two averages are not interchangeable.

Exact official section: https://openstax.org/books/physics/pages/2-2-speed-and-velocity

The canonical Source `SRC-MOTION_BASICS@1` is the same OpenStax Physics book and its chapter-level URI is retained. The Evidence Use will carry the exact §2.2 locator. No Source version is needed.

## Authorized exact scope

On branch `m13-system-wide-depth-audit-2026-10-09` only:

1. Version `CLM-MOTION_BASICS-B` from v1 to v2. Change only `record_version` and `content.statement`. The corrected statement is:
   “Средняя векторная скорость равна отношению перемещения тела к интервалу времени, за который это перемещение произошло.”
   Preserve Claim ID, type, provenance (Source v1), claim_type, publication/completion status, schema and all other fields.
2. Version `EU-MOTION_BASICS-B` from v1 to v2. Change only `record_version`, `content.claim_ref.version` to Claim v2, and `content.material.description`. Preserve Source v1 reference, evidence role, provenance, ID and all other fields. The description must identify OpenStax Physics §2.2 “Speed and Velocity”, explain that average velocity is displacement divided by elapsed time, distinguish it from average speed (distance divided by elapsed time), and avoid reproducing textbook prose.
3. Update only `CONTENT/vertical-slices/motion-basics/README.md` to identify §2.2 and the distinction between average speed and average velocity.
4. Strengthen only `REFERENCE/tests/test_content_motion_basics_vertical_slice.py` to assert the exact Claim v2 statement, EU v2 → Claim v2 and Source v1 links, §2.2 locator, the scalar/vector and distance/displacement distinction, and the unchanged nine-record slice structure.
5. Register this authorization and the `motion-basics` slice in `RELEASE/EDITORIAL-CORRECTION.json`.
6. Add `RELEASE/M13-MOTION-BASICS-AVERAGE-VELOCITY-CORRECTION-CHECKPOINT-2026-11-15.md` documenting the finding, exact version changes, source locator, exclusions and verification status.

## Explicit exclusions

No Source record/version, other Claim or Evidence Use, other slice, Context, Scope, Relation, risk metadata, D/E/B score, coverage count, schema, release allowlist, rights clearance, publication approval, `main`, or PR merge change is authorized. No other Claim statement may change. This correction does not close the motion slice or clear Claim B for publication.

## Acceptance

Run the dedicated motion regression, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently inspect the exact diff and confirm that only the six listed paths changed, the slice remains at nine records, other Claim statements are unchanged, and `main` is unchanged. Keep PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
