# M13 Relation Audit — Inventory and Semantic Triage, Batch 01
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: metadata-level review of the 64 Relation records identified in the current repository tree.
Review type: full Relation-record inventory with initial semantic triage; this is not yet the final independent Relation acceptance.

## Method and limits
The tree inventory identified 64 JSON files whose records declare or are named as Relation records. Their `content` objects were inspected for relation type, participants, roles, direction and frame/context reference. The repository's existing CI preflight is passing on the last completed Offline Edition run for the current audit head, but full same-HEAD CI is not yet complete. This review does not treat schema validity as proof that a relationship is substantively useful.

## Structural observations
- The registered cross-slice-linkage README declares 57 Relation records plus its Context record. The broader corpus also contains seven additional Relation records in other slices, including emergency-management, water-storage, fire-safety, food-preservation, scientific-method, shelter and water-resources slices. This reconciles to 64 Relation records at the current tree.
- The inspected Relation records generally specify two participants, a `relation_type`, roles, direction and a frame reference.
- Most cross-slice links use `CTX-CROSS-SLICE-LINKAGE`; the container-state Relation uses the narrower `CTX-WATER-STORAGE-EMERGENCY` frame.
- The records do not consistently carry a separate natural-language rationale explaining why the specific endpoint claims are connected. For many records, the `relation_type` label is the only explicit semantic explanation. That is not automatically a schema violation, but it limits auditability and makes user value harder to judge.
- Some relations are directed and encode explicit role distinctions, e.g. earthquake event → aftershock expectation, and sanitized container state → stored-water state. Those should be assessed differently from undirected cross-domain navigation links.

## Initial semantic triage

### Strong practical candidates to preserve and test in Human View
- `REL-CROSS-CO-EMERGENCY-ESCALATION` and `REL-CROSS-CO-PREVENTION`: connect generator and heating-related carbon-monoxide emergency/prevention claims.
- `REL-CROSS-HOME-FIRE-ALERTS`, `REL-CROSS-ALERTS-WILDFIRE-SMOKE`, and `REL-CROSS-LIGHTING-HOME-FIRE`: connect warnings or outage lighting to emergency response.
- `REL-CROSS-WATER-CHEMICAL`, `REL-CROSS-WATER-FILTER`, and `REL-CROSS-WATER-QUALITY-TREATMENT`: connect water quality and treatment boundaries.
- `REL-CROSS-SANITATION-HYGIENE`, `REL-CROSS-SANITATION-WASTEWATER`, `REL-CROSS-SEPTIC-FLOOD-SANITATION`, and `REL-CROSS-FLOOD-HAZARDOUS-WASTE`: connect sanitation actions, waste, wastewater and flood cleanup.
- `REL-CROSS-TELECOM-ENERGY-RESILIENCE`, `REL-CROSS-SETTLEMENT-WATER`, `REL-CROSS-SETTLEMENT-ENERGY`, and `REL-CROSS-SETTLEMENT-INFRASTRUCTURE`: plausible dependencies for infrastructure-failure scenarios.
- `REL-CONTAINER-WATER-STORAGE`: explicit directed state relationship that can support a practical water-storage sequence.

These are plausible from their recorded endpoints and relation types; this triage does not certify that every endpoint proposition is correct or that each link improves navigation in the current Human View.

### Candidates requiring closer endpoint-level justification
- `REL-CROSS-AMR-PLANT-HEALTH`: the recorded type invokes a One Health link between antimicrobial resistance and plant health; verify the endpoint claims establish a meaningful connection rather than relying on topical proximity.
- `REL-CROSS-AIR-POWER-SYSTEMS`: broad “air quality and energy systems” relation; verify the two specific claims support a practical explanatory link.
- `REL-CROSS-INDUSTRIAL-PROCUREMENT`: systems/procurement link may be useful, but the relation label is broad; verify the endpoint propositions and intended user task.
- `REL-CROSS-HISTORY-GEOGRAPHY-ECONOMIC-HISTORY` and `REL-CROSS-MATH-ENGINEERING-HISTORY`: plausible conceptual links, but ensure the relation is more than generic topical adjacency.
- `REL-CROSS-FOOD-PUBLIC-HEALTH` and `REL-CROSS-FOOD-DISTRIBUTION-LOGISTICS`: likely useful cross-domain relationships; verify their exact endpoint claims and practical navigation purpose.
- `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY`, `REL-CROSS-GEODESY-SURVEYING`, and other foundational measurement links: verify that the endpoint claims identify a shared method or dependency rather than only neighboring disciplines.

The list above is a triage queue, not a claim that these Relations are defective. No Relation was deleted, rewritten or added.

## Findings and follow-up
1. **No obvious structural defect was established by this metadata-level pass alone.** The observed records generally carry two participants, a type label, direction and frame.
2. **Semantic rationale is often thin.** A machine-readable `relation_type` is useful but may not explain the causal, operational or conceptual reason a user should follow the link. Review whether endpoint-specific justification should be documented in an allowed field or audit artifact without inventing a new schema field.
3. **The endpoint-level review is still open.** Each of the 64 Relations must be checked against the actual endpoint record statements, target types/versions, duplicates and whether the relationship improves navigation, explanation or practical reasoning.
4. **Cross-domain omissions remain a separate question.** A valid current Relation set can still omit material dependencies; the system-wide audit must identify only omissions with demonstrated user or explanatory value.
5. **No changes to Relation records are authorized by this review.** Any future correction or new Relation requires a finding-specific scope and dedicated regression, consistent with M13's invariants.

## Audit boundary
This report is an inventory and triage artifact, not final Relation audit acceptance. It does not complete the 1,494-Claim D/E/B census, high-consequence overlay, Human View review, independent review or final exact-HEAD gate. M13 remains open.
