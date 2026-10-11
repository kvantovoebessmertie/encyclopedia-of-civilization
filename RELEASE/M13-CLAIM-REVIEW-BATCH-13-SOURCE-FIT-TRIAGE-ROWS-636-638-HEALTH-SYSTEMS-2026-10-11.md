# M13 Batch 13 — source-fit triage (rows 636–638): health systems

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; WHO directly supports definition and six building blocks, with interaction claim needing clearer evidence and all pinpoints absent**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON remains unchanged.

## Source trail and identity issue

The canonical source record is `SRC-HEALTH_SYSTEMS_BASICS@1`, WHO *Health systems*: https://www.who.int/health-topics/health-systems

Useful direct WHO materials:
- WHO definition of a health system: all organizations, people and actions whose primary intent is to promote, restore or maintain health.
- WHO's six building blocks: service delivery, health workforce, health information systems, medical products/vaccines/technologies, financing, and leadership/governance. A WHO handbook summarizes this framework: https://www.who.int/publications/b/31426
- WHO material on system interaction warns that the six-block framework is an analytical simplification; the blocks interact, and country context matters. WHO also notes that dividing a complex system into blocks can underplay cross-sector actions and social/economic determinants.

**Record identity discrepancy:** worklist labels these Claims with hyphenated IDs, while the canonical JSON `record_id` values use underscores (for example, worklist `CLM-HEALTH_SYSTEMS_BASICS-A` vs file `CLM_HEALTH_SYSTEMS_BASICS_A`). The record provenance and Evidence Use refs consistently use underscore IDs. Do not change IDs in this triage; reconcile inventory/worklist aliases separately.

The three Evidence Use records say only “Source supports the claim within the stated scope” and provide no pinpoint.

## 1. `CLM_HEALTH_SYSTEMS_BASICS_A` — provisional **D2 / E3 / B2**

**Claim:** “A health system includes organizations, people, and actions whose primary intent is to promote, restore, or maintain health.”

**Assessment:** This is a direct definitional statement but does not explain system boundaries or the relationship between health-sector and cross-sector actors (D2). The WHO definition explicitly matches the central wording (E3). Preserve the distinction between a health system and only publicly owned health facilities; the WHO definition is broader (B2).

**Disposition:** Strong candidate to retain. Add a pinpoint to the WHO definition paragraph.

## 2. `CLM_HEALTH_SYSTEMS_BASICS_B` — provisional **D2 / E3 / B2**

**Claim:** “Health systems depend on multiple functions, including service delivery, workforce, information, medicines, financing, and governance.”

**Assessment:** The list is an accessible overview but does not explain what each component does or how to assess it (D2). It maps closely to the WHO six building blocks; “medicines” is a narrower shorthand for medical products, vaccines and technologies (E3). State that this is WHO's analytical framework, not an exhaustive universal taxonomy of everything affecting health (B2).

**Disposition:** Retain provisionally. Add a pinpoint to the six-building-block list and align terminology with the WHO framework.

## 3. `CLM_HEALTH_SYSTEMS_BASICS_C` — provisional **D2 / E2 / B2**

**Claim:** “Health-system performance depends on interactions among its components and the context in which services are delivered.”

**Assessment:** The statement is conceptually useful but does not name mechanisms or measurable outcomes (D2). WHO material supports coordination among system components and context-sensitive analysis; however, the canonical source is a general health-systems topic page and Evidence Use does not pinpoint an interaction passage. The evidence fit is therefore partial pending a direct source locator/pinpoint (E2). The claim is appropriately non-deterministic, but should not imply the six-block model fully captures social determinants or cross-sector action (B2).

**Disposition:** Retain provisionally. Add a specific WHO source or handbook passage discussing interdependence/context; preserve the framework's stated limits.

## Batch accounting

- Individual Claims reviewed in this note: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
