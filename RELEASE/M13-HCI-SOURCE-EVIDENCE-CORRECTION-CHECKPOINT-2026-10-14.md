# M13 HCI Source/Evidence Correction Checkpoint — 2026-10-14

Authorization: M13-HCI-SOURCE-EVIDENCE-001
Branch: m13-system-wide-depth-audit-2026-10-09
Status: **bounded versioned metadata/evidence correction prepared; preflight authorization registry corrected; exact-head CI rerun pending**

## Change summary
- Source @2 identifies the actual NIST Human Centered Design page and points to its exact URL.
- Claims A/B/C are versioned to @2 only to preserve their provenance link to Source @2; their wording and Claim types are unchanged.
- Evidence Use A/B/C are versioned to @2 with Claim @2 and Source @2 references plus claim-specific descriptions.
- Context and Scope are versioned to @2 only to retarget Claim A @2.
- The dedicated regression checks record versions, reference alignment, the exact URI and the limitation language.
- README now discloses the source's stale-page warning and the support boundary.

## Claim-level disposition
- **A — HOLD:** NIST's page mentions self-descriptiveness and controllability but does not directly establish the complete statement that an interface provides means for perception and system control.
- **B — HOLD:** the source discusses users, tasks, environments and usability; independent review must confirm the complete formulation, including interface characteristics.
- **C — HOLD:** the source discusses user-centered evaluation and iterative activities; it does not prescribe one universal evaluation protocol.

## CI remediation note

The first exact-head CI attempt failed at content preflight because the slice was not yet listed in the registry's top-level authorized_slices and findings arrays, even though the bounded authorization object existed. Those registry entries were added. The next run then identified three Evidence Use provenance links still pointing to Source @1, which the repository resolver does not retain. All three Evidence Use records now point to Source @2 in provenance as well as in content.source_ref, and the dedicated regression now asserts this invariant. A fresh run on the resulting exact HEAD is required; earlier failed runs are not validation.

## Verification still required
1. Run preflight/schema and the dedicated HCI regression.
2. Run Reference Tests, Release Conformance Gate and Offline Edition on the same exact final HEAD.
3. Verify all nine slice records, provenance links, Context/Scope targets and the source page's current contents.
4. Obtain independent Human View and editorial review; no D/E/B scores or release eligibility are inferred here.
5. Reconcile current Source inventory/coverage and prior audit debts before M13 closure.

No main changes, publication allowlist, release approval, D/E/B score assignment, new/deleted records or Relations are authorized. PR #21 remains Draft/unmerged.
