# M13 bounded correction authorization — electrical safety Evidence Use

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Finding: `M13-ELECTRICAL-SAFETY-EVIDENCE-001`  
Status: **AUTHORIZED FOR CONTROLLED EVIDENCE-USE CORRECTION ONLY**

## Authorization basis

The project owner gave explicit approval in the current project conversation to proceed with the accumulated M13/MVP remediation work. This file narrows that approval to one auditable correction package.

## Exact scope

Only the following existing Evidence Use records may be versioned from v1 to v2:
- `CONTENT/vertical-slices/electrical-safety-basics/records/EU-ELECTRICAL_SAFETY_BASICS-A.json`
- `CONTENT/vertical-slices/electrical-safety-basics/records/EU-ELECTRICAL_SAFETY_BASICS-B.json`
- `CONTENT/vertical-slices/electrical-safety-basics/records/EU-ELECTRICAL_SAFETY_BASICS-C.json`

Permitted change: replace only `content.material.description` with a Russian, Claim-specific evidence-use description naming the exact NIOSH page sections and the limits of what those sections establish. Preserve each record ID, record type, schema, type version, Claim reference, Source reference, evidence role, provenance method, created_from link, publication status and completion status.

Supporting non-canonical files permitted:
- `REFERENCE/tests/test_content_electrical_safety_basics_vertical_slice.py` — add assertions for the three v2 EU descriptions and preserved exact references;
- `CONTENT/vertical-slices/electrical-safety-basics/README.md` — document the source sections and the U.S. workplace-guidance boundary;
- `RELEASE/M13-ELECTRICAL-SAFETY-EVIDENCE-REMEDIATION-2026-11-13.md` — record passage review, rights/attribution screen, scope limitations and disposition;
- `RELEASE/M13-EXECUTION-RECONCILIATION-2026-11-13.md` — record the bounded result.

## Source and passage basis

Official source: CDC/NIOSH, *Electrical Safety in the Workplace*, https://www.cdc.gov/niosh/electrical-safety/about/

Verified sections:
- “Electrical hazards” and “Electrical injuries” — electric shock, burns, arcing, fire, electrocution and falls;
- “Key points” and “Recommendations” — qualification, appropriate PPE, energy-control procedures and verification of de-energization;
- “Qualified vs. unqualified persons” — only qualified persons should do electrical work; unqualified persons should not work on energized parts.

The correction may use short section titles and project-authored paraphrases only. Do not reproduce page text, images or third-party content. The source is U.S. workplace guidance; do not present it as universal law or as a complete electrical safety code.

## Explicit exclusions

This authorization does **not** permit:
- any Claim wording, Claim version, Claim type or provenance change;
- any Source record, Source identity or URI change;
- new or deleted records, Relations, Context, Scope or record types;
- changes to D/E/B scores, historical score rows, assessment ledgers or review history;
- changing publication status, creating a release allowlist, Human View approval, publication, deployment or merging;
- edits to other slices or `main`.

Claim C's wording about “independent repair” is broader than the NIOSH passage. Its Evidence Use v2 must state that the source directly supports the qualified-person / energized-parts boundary but does not establish a universal prohibition on every form of repair. Claim C remains HOLD for separate editorial review; this authorization does not narrow it.

## Required acceptance

1. Exact source passage and section names rechecked against the official NIOSH page.
2. Each v2 EU points to the unchanged exact Claim v1 and Source v1.
3. Dedicated regression verifies v2, exact references, claim-specific descriptions and unchanged slice inventory counts.
4. JSON/schema preflight, Reference Tests, Release Conformance Gate and Offline Edition pass on the same final HEAD.
5. A post-correction report confirms only the three authorized EU records changed.
6. All three Claims remain publication HOLD pending current-rubric assessment, independent electrical-safety review and Human View.

No other content change is implied by this authorization.
