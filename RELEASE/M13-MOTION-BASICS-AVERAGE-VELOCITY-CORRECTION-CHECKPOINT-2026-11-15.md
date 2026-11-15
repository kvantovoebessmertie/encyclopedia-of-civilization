# M13 motion-basics — average-velocity correction checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Authorization: `M13-MOTION-AVERAGE-VELOCITY-001`
Basis HEAD: `16fbffd759f13c76f5039d15982d5e0b5ed6e2a6`
State: **bounded canonical correction implemented; exact-head verification pending**

## Finding and source fit

The former `CLM-MOTION_BASICS-B@1` called the quantity “средняя скорость” while defining it as change in position (displacement) divided by elapsed time. That is average vector velocity, not scalar average speed.

OpenStax Physics §2.2 “Speed and Velocity” directly distinguishes:
- average speed = distance traveled / elapsed time (scalar);
- average velocity = displacement / elapsed time (vector).

Official section: https://openstax.org/books/physics/pages/2-2-speed-and-velocity

## Exact changes

- `CLM-MOTION_BASICS-B@2`: corrected the statement to “Средняя векторная скорость равна отношению перемещения тела к интервалу времени, за который это перемещение произошло.” Claim ID/type and Source v1 provenance are preserved.
- `EU-MOTION_BASICS-B@2`: points to Claim B v2 and preserves Source v1; its description records the §2.2 locator and distinguishes average velocity from average speed.
- `CONTENT/vertical-slices/motion-basics/README.md`: records the section locator and scalar/vector distinction.
- `REFERENCE/tests/test_content_motion_basics_vertical_slice.py`: asserts the nine-record slice, exact versioned references, exact Claim wording, unchanged Source v1 locator, and both distance/time versus displacement/time distinctions.
- `RELEASE/EDITORIAL-CORRECTION.json`: registers the exact authorization and motion-basics scope.
- This authorization and checkpoint document the bounded correction.

No Source record was versioned; no record was added or deleted. Slice record count remains 9. No other Claim, Evidence Use, Context, Scope, Relation, score, risk metadata or coverage count was changed.

## Limitations and status

This correction resolves the terminology mismatch for Claim B only. It does not establish final D/E/B scores, independent review, rights clearance, specialist approval, Human View, or publication eligibility. All three motion-basics Claims remain subject to the wider M13 review.

Exact-head Reference Tests, Release Conformance Gate and Offline Edition must all pass on the same final HEAD. M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged; `main` must remain unchanged.
