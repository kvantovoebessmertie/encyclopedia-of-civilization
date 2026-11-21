# M13 Claim Review Batch 32 — Agriculture Foundations
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **3 additional Claims reviewed. This is a bounded review batch, not domain closure or corpus completion.**

## Method
Reviewed three Claims and all four directly relevant Evidence Use/source records in `agriculture-basics`. D (explanatory depth), E (claim-specific evidence fit) and B (boundary discipline) are scored independently from 0–3. This is a desk review of the corpus's own claim-to-source traceability, not a full agronomic validation or local growing recommendation.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-AGRICULTURE_BASICS-A` | 1 | 1 | 2 | The statement is a broad definition of agriculture, but the linked FAO Evidence Use record only says the source is used without going beyond its material. It does not point to a specific FAO passage or identify which activities/resources are included. Add source-specific traceability and avoid implying the short definition exhausts the scope of agriculture. |
| `CLM-AGRICULTURE_BASICS-B` | 2 | 2 | 2 | The interaction of soil, water, biological factors, climate and management is plausible and receives corroboration from a USDA-linked Evidence Use record. However, the primary FAO Evidence Use description is generic, and the USDA record broadly describes overlapping factors rather than identifying a passage or distinguishing crop from livestock productivity. Keep this as a general systems statement, not a quantified or universal causal model. |
| `CLM-AGRICULTURE_BASICS-C` | 2 | 1 | 3 | The local-applicability boundary is appropriately cautious and avoids promising that a practice transfers unchanged between places. Its only linked Evidence Use record is a generic FAO description that does not directly substantiate the transferability caveat. Support the boundary with specific agronomic guidance and state which local variables need assessment; do not turn this general caution into a substitute for crop-, soil- and climate-specific advice. |

## Findings
1. **Confirmed generic Evidence Use debt:** all three primary Evidence Use records repeat the same non-specific FAO description. It does not tell a reviewer what source material supports each Claim.
2. **Partial independent corroboration:** Claim B has a USDA-linked Evidence Use record with more relevant material. This is a useful second institutional source, but a second institution alone does not establish source independence for every underlying proposition or supply precise passage-level traceability.
3. **Practical depth gap:** a usable agriculture guide should direct readers to assess local soil, water availability and quality, climate/seasonality, species or cultivar, pests and diseases, available inputs, and local regulations before transferring a practice. Those variables should be developed with suitable sources rather than silently added to the current Claims.
4. No content Records were changed. These three Claims remain within the frozen 1,494-Claim denominator. This batch does not close agriculture, cross-domain review, high-consequence recall, Human View, or M13.

## Records inspected
- `CONTENT/vertical-slices/agriculture-basics/records/CLM-AGRICULTURE_BASICS-A.json`
- `CONTENT/vertical-slices/agriculture-basics/records/CLM-AGRICULTURE_BASICS-B.json`
- `CONTENT/vertical-slices/agriculture-basics/records/CLM-AGRICULTURE_BASICS-C.json`
- `CONTENT/vertical-slices/agriculture-basics/records/EU-AGRICULTURE_BASICS-A.json`
- `CONTENT/vertical-slices/agriculture-basics/records/EU-AGRICULTURE_BASICS-B.json`
- `CONTENT/vertical-slices/agriculture-basics/records/EU-AGRICULTURE_BASICS-C.json`
- `CONTENT/vertical-slices/agriculture-basics/records/EU-AGRICULTURE-USDA-CORROBORATION.json`
- `CONTENT/vertical-slices/agriculture-basics/records/SRC-AGRICULTURE_BASICS.json`

## Sources
- FAO, Agriculture: https://www.fao.org/agriculture/
- USDA-linked source identity as recorded in `SRC-USDA-AGRICULTURE-CONTEXT` (the locator and source record must be checked during the full source-preservation pass).

## Acceptance status
Three additional Claim rows have explicit D/E/B scores and rationales. Follow-up action: make the FAO Evidence Use descriptions claim-specific and verify the exact USDA source locator during source-preservation review. Full 1,494-Claim scoring, high-consequence recall, Human View, Relation endpoint review, independent scoring review, authorized corrections with regression tests, and final same-HEAD 3/3 CI remain open.
