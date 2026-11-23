# M13 — Batch 41 historical snapshot reconstruction for six current v2 Claims

Date: 2026-11-18  
Inspection branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: six versionless Batch 41 scored rows currently mapped to Claim@2.  
Disposition: **historical Claim/Evidence Use/Source version provenance recovered; current assessment still requires partial revalidation.**

## 1. Finding

The prior readiness reconciliation correctly withheld these six rows from automatic v2 reuse because their score-table IDs omit `@version`. A path-specific Git history reconstruction now resolves that uncertainty.

The Batch 41 scored-block commits and exact record snapshots establish that all six rows assessed Claim@1, linked Evidence Use@1, and Source@1. The current Claim statements are unchanged between @1 and @2. The current evidence chains have since been versioned, so this is not acceptance of a current D/E/B score.

| Current Claim key | Batch 41 report row | Historical snapshot commit | Historical chain | Current chain |
|---|---|---|---|---|
| `CLM-ASSET_MANAGEMENT_BASICS-A@2` | Block 04, row 56 | `cd1a9e2cf2640b1a1da39af0d2710da547ef302d` | Claim@1 / EU@1 / Source@1 | Claim@2 / EU@3 / Source@2 |
| `CLM-ASSET_MANAGEMENT_BASICS-B@2` | Block 04, row 57 | `cd1a9e2cf2640b1a1da39af0d2710da547ef302d` | Claim@1 / EU@1 / Source@1 | Claim@2 / EU@3 / Source@2 |
| `CLM-ASSET_MANAGEMENT_BASICS-C@2` | Block 04, row 58 | `cd1a9e2cf2640b1a1da39af0d2710da547ef302d` | Claim@1 / EU@1 / Source@1 | Claim@2 / EU@3 / Source@2 |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-A@2` | Block 05, row 74 | `14078b3994edec546f88e6d0f1181c7586611bc9` | Claim@1 / EU@1 / Source@1 | Claim@2 / EU@3 / Source@2 |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-B@2` | Block 05, row 75 | `14078b3994edec546f88e6d0f1181c7586611bc9` | Claim@1 / EU@1 / Source@1 | Claim@2 / EU@3 / Source@2 |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-C@2` | Block 05, row 76 | `14078b3994edec546f88e6d0f1181c7586611bc9` | Claim@1 / EU@1 / Source@1 | Claim@2 / EU@3 / Source@2 |

The Batch 41 report commits are:
- Block 04: `cd1a9e2cf2640b1a1da39af0d2710da547ef302d` (2026-10-11 07:11:31Z).
- Block 05: `14078b3994edec546f88e6d0f1181c7586611bc9` (2026-10-11 07:12:16Z).

At those exact commits, each listed Claim, its matching Evidence Use, and its linked Source was version 1. Path history confirms the Claim records were subsequently versioned on 2026-11-15 for provenance migration; the Evidence Use records were subsequently revised and migrated to the corrected Source@2. Direct comparison confirms all six Claim statement strings are unchanged between Claim@1 and current Claim@2.

## 2. Consequence for reuse

- **D/B:** the Batch 41 rationale may be reused as a prior assessment input because the Claim statement is unchanged. It is still a candidate requiring reviewer confirmation; it is not an accepted current score.
- **E:** must be revalidated against the current EU@3 → Source@2 chain. The old E score assessed EU@1 → Source@1 and cannot be copied into the current worksheet.
- Asset management: the 2026-11-15 Source identity correction and EU scope revisions are substantive evidence-chain changes. Reuse the existing ISO 55000/55001 identity and scope review; do not repeat source discovery.
- Behavioral biology: the 2026-11-15 Source correction and §45.7 Evidence Use pinpoint work are existing remediation inputs. Reuse those findings; independently verify whether each current EU supports its own Claim, especially the methodological boundary in Claim C.

This resolves the six **historical version-provenance** exceptions. It does not resolve source fit, locator sufficiency, independence, rights, specialist review, Human View, or current D/E/B acceptance.

## 3. Crosswalk impact

The six rows remain in `PARTIAL_REVALIDATION_REQUIRED`, but the reason is now known and bounded: historical @1 D/B work is reusable as an input; current @2/@3/@2 evidence chains require E revalidation. They must no longer be counted as unresolved historical snapshot-version cases.

The broader 1,494-row crosswalk remains:
- 888 exact-ID/exact-version Batch 44–52 candidates;
- 3 versioned path/internal-ID crosswalk cases;
- 9 explicit historical @1 rows for current Claim@2 (historical-only);
- 594 unique versionless Claim IDs, now with the six Batch 41 v2 snapshot cases resolved as above (the remaining cases still require exact report/snapshot validation).

No new score is assigned. No canonical Claim, Evidence Use, Source, Assessment, Relation, batch, or queue was changed. No Batch 55 was created. PR #21 remains Draft/unmerged; `main` remains untouched.
