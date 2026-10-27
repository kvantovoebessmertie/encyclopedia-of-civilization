# M13 Batch 13 — Claim-type and duplicate triage (rows 603–605): geology basics

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional triage; three generic editorial/methodology Claims flagged**

Scoring rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional audit notes, not finalized ledger scores. No canonical JSON changed.

## Source trail and duplicate context

All three Claims reference `SRC-GEOLOGY_BASICS`, labelled “USGS — Geology” at https://www.usgs.gov/programs/water-resources/science/geology. The linked Evidence Use records contain only boilerplate descriptions and no specific passage or locator.

The Claims themselves describe the purpose of the encyclopedia slice, general epistemic methodology, and a general caution about specialist review. These are not substantive geology propositions. They are semantically parallel to the generic editorial Claims already triaged in genetics-basics (rows 582–584) and genomics-basics (rows 585–587). Treat this as a cross-slice duplicate/placement issue pending the formal duplicate pass, not as a declaration that the Claims are exact duplicates. The current Source record may be useful for geology facts, but the source's presence does not establish these generic statements.

## 1. `CLM-GEOLOGY_BASICS-A` — **D0 / E0 / B1**

**Claim:** “Срез geology-basics вводит базовые понятия и отношения, необходимые для ориентации в предметной области.”

**Assessment:** This describes the purpose and intended contents of a slice, not a geology proposition (D0). A general USGS geology page cannot establish what this specific encyclopedia slice contains, and the Evidence Use gives no claim-specific support (E0). “Базовые понятия” and “необходимые для ориентации” are broad and not operationally bounded (B1).

**Disposition:** Route to editorial/Claim-type review. Move to approved slice metadata or reader guidance, or replace with a substantive geology Claim tied to a precise source passage.

## 2. `CLM-GEOLOGY_BASICS-B` — **D1 / E0 / B2**

**Claim:** “Интерпретация сведений по geology-basics зависит от источника, контекста и границ применимости утверждения.”

**Assessment:** This is a generic epistemic reminder without a geology-specific explanation or review procedure (D1). The linked USGS source and boilerplate Evidence Use do not substantiate this cross-cutting editorial rule (E0). It names source, context, and applicability boundaries but does not operationalize them (B2).

**Disposition:** Move to an approved cross-cutting methodology layer or cite the encyclopedia's editorial policy. Do not use the geology source as evidence for this general rule.

## 3. `CLM-GEOLOGY_BASICS-C` — **D1 / E0 / B2**

**Claim:** “Базовое знание по geology-basics не заменяет специализированную проверку, когда вывод зависит от условий, измерений или профессиональной оценки.”

**Assessment:** This is a broad caution rather than a geology-specific fact and provides no concrete geology example of a condition, measurement, or professional assessment (D1). The linked source does not establish this general rule, and the Evidence Use is boilerplate (E0). The conditional clause provides a useful boundary but no decision procedure (B2).

**Disposition:** Move to approved reader guidance/editorial methodology or support with an explicit review-policy source.

## Batch accounting

- Individual Claims triaged in this checkpoint: **3**.
- Prior-score eligibility: **must be checked before final ledger inclusion**.
- Cross-slice semantic duplicate/placement review: **open**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
