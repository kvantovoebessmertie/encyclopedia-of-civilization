# M13 bounded source-identity correction — behavioral biology

Date: 2026-11-15  
Authorization ID: `M13-BEHAVIORAL-BIOLOGY-OPENSTAX-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Finding

Package 06 identified a confirmed Source identity/URI mismatch. The registered Source points to OpenStax Biology 2e Chapter 46 (Ecology of Ecosystems), while the three linked Claims concern behavioural biology. The relevant OpenStax material is §45.7, “Behavioral Biology: Proximate and Ultimate Causes of Behavior”:

https://openstax.org/books/biology-2e/pages/45-7-behavioral-biology-proximate-and-ultimate-causes-of-behavior

The section defines behaviour as a change in an organism's activity in response to a stimulus and distinguishes innate behaviour with a strong genetic component from learned behaviour shaped by environmental conditioning.

## Authorized exact scope

On branch `m13-system-wide-depth-audit-2026-10-09` only:

1. Version `SRC-BEHAVIORAL_BIOLOGY_BASICS` from v1 to v2, changing its source identity and URI to the exact OpenStax Biology 2e §45.7 section.
2. Version the three existing Evidence Use records A/B/C from v1 to v2, updating only their source-version lineage/reference and claim-specific material descriptions with the §45.7 locator and explicit support limits.
3. Update only the behavioural-biology slice README.
4. Strengthen only `REFERENCE/tests/test_content_behavioral_biology_basics_vertical_slice.py` to assert the exact source identity/URI, versioned links, and the three claim-specific evidence descriptions and scope limits.
5. Add this authorization and the M13 source-fit checkpoint note; register this authorization ID and the slice slug in `RELEASE/EDITORIAL-CORRECTION.json`.

## Explicit exclusions

No Claim wording, Claim version, Claim provenance, Source additions/deletions, other slice, Context, Scope, Relation, risk metadata, D/E/B score, publication allowlist, schema, coverage count, release gate, `main`, or PR merge change is authorized. Claim C's methodological instruction about avoiding untestable motive attribution is not directly established by §45.7 and must remain explicitly marked as only partially supported. Do not imply independent corroboration from this single OpenStax source.

## Acceptance

Run the dedicated regression, Content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact changed paths, source/EU versions, unchanged Claim wording and unchanged `main`. This correction does not clear any Claim for publication and does not close M13.
