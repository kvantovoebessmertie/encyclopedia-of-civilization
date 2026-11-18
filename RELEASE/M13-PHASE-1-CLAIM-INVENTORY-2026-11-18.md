# M13 Phase 1 — Claim inventory checkpoint

Date: 2026-11-18  
Inventory source revision: `7123b44ce344190027c20e33c0d83675d5aa0768`  
Workflow: Reference implementation tests, run `44327025386`  
Artifact: `m13-claim-audit-worksheet`, artifact ID `14438475109`  
Artifact SHA-256: `2e097945e50288798ae5bf4b96d4153f9f91ae1adc1c621a325494f69e12c352`

## 1. Scope and reproducibility

This checkpoint records the read-only Phase 1 inventory generated from the exact source revision above. The workflow artifact contains both:

- `M13-CLAIM-AUDIT-WORKSHEET.json` — structured Claim inventory and linked Evidence Use/Source metadata.
- `M13-CLAIM-AUDIT-WORKSHEET.csv` — tabular worksheet.

The downloaded ZIP was re-hashed locally and matches the GitHub artifact digest. The JSON declares the same `source_revision` as the workflow run's `head_sha`. This is an inventory artifact, not an assessment: the generator explicitly states that machine flags are triage only, not semantic scores.

## 2. Corpus and Claim inventory

| Measure | Result |
|---|---:|
| Record JSON files scanned | 4,851 |
| Vertical-slice directories in the exact Git tree | 483 |
| Slices containing at least one Claim | 482 |
| Claim records | 1,494 |
| Unique Claim record IDs | 1,494 |
| Duplicate Claim IDs in the inventory | 0 |
| Claim version 1 | 1,478 |
| Claim version 2 | 16 |
| Claims with missing ID, version, slice, path, publication status, completion status, type or statement | 0 |
| Claims marked published | 1,494 |
| Claims marked complete | 1,494 |

The distinction between 483 total slices and 482 slices containing Claims is intentional; one slice has no Claim record in this inventory.

## 3. Claim → Evidence Use → Source linkage

| Measure | Result |
|---|---:|
| Claims with at least one Evidence Use | 1,494 / 1,494 |
| Total Claim-to-Evidence Use links | 1,679 |
| Unique Evidence Use IDs represented | 1,679 |
| Unique Source IDs represented | 627 |
| Evidence Use items with missing ID, role, Source ID, source identity or source URI | 0 |
| Mismatch between declared Evidence Use count and expanded evidence items | 0 |
| Evidence roles | 1,679 `supports` |
| Source record versions represented in linked metadata | 1,664 version 1; 15 version 2 |

Evidence Use links per Claim:

| Links per Claim | Claims |
|---:|---:|
| 1 | 1,314 |
| 2 | 175 |
| 3 | 5 |

The inventory records 584 distinct source URIs. URI uniqueness is not source independence: different URLs may identify the same underlying source, and repeated URLs may support multiple Claims. This count is not an evidence-diversity assessment.

## 4. Assessment state — deliberately blank

| Field | Current inventory result |
|---|---:|
| D scores populated | 0 / 1,494 |
| E scores populated | 0 / 1,494 |
| B scores populated | 0 / 1,494 |
| Human review status `NOT_YET_REVIEWED` | 1,494 / 1,494 |

This is the generated worksheet's assessment state. It must not be interpreted as proof that no historical report ever contained a provisional or desk score. Historical report provenance is a separate phase and must be reconciled by exact Claim ID and version.

## 5. Integrity checks performed on the generated inventory

The downloaded JSON was parsed and checked for:

1. 1,494 rows and unique Claim IDs.
2. Non-empty Claim ID, version, slice, file path, publication status, completion status, claim type and statement.
3. Declared Evidence Use count matching the expanded Evidence Use item count for every Claim.
4. Every expanded item carrying an Evidence Use ID, role, Source ID, Source identity and source URI.
5. No duplicate Evidence Use IDs within the generated cross-Claim inventory.
6. No missing Evidence Use or Source links in the generated Claim-to-Evidence Use-to-Source metadata.

All six checks returned zero exceptions.

## 6. Explicit limitations and next work

- This checkpoint does not independently re-open all 4,851 JSON files one by one; it validates the exact-revision inventory artifact produced by the repository's inventory generator and checks its internal consistency.
- It does not validate whether a Source passage substantively supports a Claim, whether the Evidence Use text is accurate, whether a locator is reproducible, or whether multiple sources are independent.
- It does not reconcile historical review rows, the seven repeated-score groups, the 14 unidentified IDs, or the prior REJECT provenance. Those are separate Phase 2–4 work.
- The 16 version-2 Claims and 15 linked version-2 Source metadata occurrences must be preserved as version-specific entries; do not collapse them into version 1.
- No canonical record, score, batch assignment, queue selection, workflow or `main` branch was changed by this inventory checkpoint.

**Phase 1 status: inventory generated and internal consistency checks passed.** The remaining phases are not thereby completed, and no Claim is certified or release-cleared by this document.
