# R9 Bounded-Authorization Conformance Reconciliation — 2026-11-19

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Inspection HEAD: `b79080e2e98ad951104f969b8298a1cb66e17d4a`  
Purpose: reconcile remaining R9 bounded authorizations against the exact current canonical tree, without repeating completed remediation or exceeding authorization.

## Executive result

The current branch contains the expected R9 remediation outputs for hydraulic engineering, cultural heritage, history of mathematics, cartography and food systems. The SI pinpoint records are present at Evidence Use v2. The archival-science corrective pass is present, but its ICA branch has an explicit unresolved authorization/provenance boundary.

Two owner-level authorization/provenance issues must remain open:

1. **History of Mathematics — Cambridge Source branch.** The active `R9-HISTORY-OF-MATHEMATICS-REMEDIATION-001` authorizes the MacTutor Source v1→v2 and creation of one additional Oxford Source. It does not name or authorize creation/use of `SRC-HISTORY_OF_MATHEMATICS-CAMBRIDGE@1`. Current Claim C@2 and Evidence Use C@2 point to that Cambridge Source. The R9 remediation addendum describes it as a third source, but that descriptive addendum is not itself an authorization. No canonical record was changed in this reconciliation. Obtain an explicit owner disposition and, if needed, a new bounded authorization covering the Cambridge source branch or a separately approved replacement/narrowing plan.
2. **Archival Science — ICA Source branch.** The active `R9-ARCHIVAL-SCIENCE-REMEDIATION-001` explicitly says the ICA ISAD(G) Source and Claim C/Evidence Use C branch are already present, but that the authorization does not retroactively authorize creation of that Source. The current Claim C@2 and Evidence Use C@2 point to `SRC-ARCHIVAL_SCIENCE-ICA@1`. The README and remediation addendum correctly preserve this as an unresolved authorization/provenance blocker. Obtain explicit owner disposition; do not infer authorization from the current graph or the corrective pass.

These findings do not establish that the source materials are inaccurate. They establish that the active bounded authorization record does not close the provenance/authorization question for these two branches.

## Exact-scope reconciliation

### R9 remediation outputs present

- **Hydraulic Engineering:** two-source profile present — HEC-HMS Source@1 and HEC-RAS Source@2; Claims A–C, Evidence Use A–C, Context and Scope at v2; README records the educational-only boundary and HOLD. The authorized new Source is reflected in coverage counts.
- **Cultural Heritage:** 1972 Convention Source@2 and 2003 Convention Source@1; Claims/Evidence Use A–C and Context/Scope at v2; README distinguishes the two legal instruments and retains community/consent boundaries and HOLD.
- **History of Mathematics:** MacTutor Source@2 and Oxford Source@1 are present; Claims A–C, Evidence Use A–C, Context and Scope at v2. Claim A points to MacTutor, Claim B to Oxford, and Claim C to the Cambridge Source@1 branch. The Cambridge branch is the authorization exception above.
- **Cartography:** USGS Mapping 101 Source@2 and Fact Sheet Source@1 are present; Claims A–C, Evidence Use A–C, Context and Scope at v2; README preserves U.S.-specific versus global-convention boundaries and HOLD.
- **Food Systems:** the 12-record, two-Source/four-Claim profile is present at v2; FAO supports Claims A–C and World Bank supports Claim D; Context/Scope target Claim A@2; rights restrictions and HOLD are retained. No extra Source or record was added by this authorization.
- **SI Units:** `EU-SI-SEVEN-BASE@2` and `EU-SI-DERIVED@2` are present, with NIST section references, attribution and the narrow “22 specially named derived units” boundary. Claim and Source versions remain unchanged, consistent with the authorization.

### Archival Science current state

- `SRC-ARCHIVAL_SCIENCE@2` (SAA) and `SRC-ARCHIVAL_SCIENCE-ICA@1` are present.
- Claim B@3 and Evidence Use B@3 implement the authorized SAA provenance/original-order correction; Context and Scope are v2.
- Claim C@2 and Evidence Use C@2 still depend on the ICA Source@1 branch. The README explicitly says the ICA Source creation is not retroactively authorized and the branch is an unresolved project-owner authorization/provenance blocker.
- The slice remains HOLD. No canonical change is authorized by this reconciliation.

## Coverage and scope observations

At inspection HEAD, `RELEASE/CONTENT-COVERAGE.json` reports:
- 4,680 total records;
- 589 Source records;
- 479 vertical slices;
- 19 registered record types, all directly covered.

Its `audit_touch` includes the R9 hydraulic, cultural-heritage, archival-science, history-of-mathematics and cartography source-expansion tokens. These are structural coverage figures only; they do not establish rights clearance, authorization, evidence quality or publication eligibility. No coverage field was changed in this pass.

The exact-version and authorization review must keep the two owner issues above separate from structural validity. Do not remove either Source branch, rewrite Claims/Evidence Use, or modify coverage counts without a new explicit bounded authorization.

## Work not repeated

- No canonical Content or Reference record was modified.
- No Relation was re-versioned.
- No first-edition candidate denominator, allowlist or INCLUDE/HOLD/EXCLUDE decision changed.
- No rights clearance, editorial approval or Human View was inferred.
- No change was made to `main`; PR #22 remains Draft and unmerged.

## Required next actions

1. Owner decision for the History of Mathematics Cambridge Source/Claim C/Evidence Use C branch: explicitly authorize the exact branch and scope, or authorize a bounded replacement/narrowing plan.
2. Owner decision for the Archival Science ICA Source/Claim C/Evidence Use C branch: establish the original authorization/provenance basis or authorize a bounded remediation plan.
3. Continue with Settlement Geography only after its separate rights-compatible source replacement authorization is explicitly granted; the current R9 authorization register does not grant that canonical change.
4. Reconcile the consolidated queue's historical out-of-master Claim count to the already verified 30, while keeping those records outside the candidate denominator pending owner scope decision.
5. Recheck exact-head CI; report each workflow independently and do not transfer earlier PASS results to a later HEAD.

## Exact-head CI snapshot

For HEAD `b79080e2e98ad951104f969b8298a1cb66e17d4a`:
- Offline Edition — completed, success.
- MVP Contribution Form Browser Tests — completed, success.
- Reference implementation tests — in progress at the final snapshot.
- Release Conformance Gate — in progress at the final snapshot.

No full CI PASS is claimed.
