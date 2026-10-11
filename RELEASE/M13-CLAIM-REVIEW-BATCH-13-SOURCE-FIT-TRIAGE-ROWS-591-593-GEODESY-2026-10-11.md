# M13 Batch 13 — Source-fit triage (rows 591–593): geodesy

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional source-fit review; source broadly fits all three Claims, with missing pinpoints**

Scoring rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional triage assessments, not finalized scored-ledger rows. No canonical JSON changed.

## Source trail

All three Claims point to `SRC-GEODESY_BASICS`, “NOAA National Geodetic Survey — What is Geodesy?” (https://www.ngs.noaa.gov/INFO/facts/geodesy.shtml). The official NGS page defines geodesy as measuring and understanding Earth's geometric shape, orientation, and gravity field; it also explains assigning coordinates to points, consistent coordinates for mapping, and uses including shoreline mapping, land boundaries, and navigation safety. This is a direct topical match. However, the Evidence Use records provide only a broad generic description and no quote or pinpoint, so the score reflects the source's observable topical fit while recording a follow-up for traceable pinpoint support.

## 1. `CLM-GEODESY_BASICS-A` — **D2 / E3 / B2**

**Claim:** “Геодезия изучает геометрическую форму Земли, её ориентацию в пространстве и гравитационное поле с высокой точностью.”

**Assessment:** The statement captures the three core properties in the NGS definition, with a concise but limited explanation (D2). The linked official NGS page directly supports the substance of the claim (E3), although the Evidence Use does not identify the relevant passage. “С высокой точностью” is consistent with the page's description of accurate measurement but would benefit from a direct pinpoint; the statement is bounded to the discipline's focus (B2).

**Disposition:** Retain as provisionally well-supported; add a pinpoint/quote to the Evidence Use during an authorized evidence-editing pass.

## 2. `CLM-GEODESY_BASICS-B` — **D2 / E2 / B2**

**Claim:** “Геодезические измерения позволяют задавать согласованные координаты точек и формировать пространственную основу для карт и других геоданных.”

**Assessment:** This gives a useful consequence of geodetic measurement but does not explain reference systems, datums, or how consistency is maintained (D2). The NGS page explicitly describes assigning coordinates and how accurately measured points make different maps consistent; that directly supports the core, while “other geodata” extends slightly beyond the page's concise explanation (E2). The general statement is appropriately broad but does not specify a reference frame or geography (B2).

**Disposition:** Source fit is good for the core. Add a pinpoint and consider narrowing “других геоданных” or adding a more specific source on the relevant reference system.

## 3. `CLM-GEODESY_BASICS-C` — **D2 / E2 / B2**

**Claim:** “Геодезическая основа используется в картографии, навигации и определении границ; конкретные измерения требуют подходящих систем координат и методов контроля.”

**Assessment:** The claim combines applications with a methodological caution, without explaining which coordinate systems or controls apply (D2). The NGS page explicitly supports mapping, land boundaries, navigation safety, and consistent coordinates; it does not fully substantiate the broad final clause about suitable coordinate systems and control methods without further pinpointed material (E2). The word “конкретные” signals context dependence, but the required method is not specified (B2).

**Disposition:** Keep provisional. Add a second, specific NGS source for datums/reference systems and quality control, or narrow the final clause to what the current source states.

## Batch accounting

- Individual Claims reviewed in this checkpoint: **3**.
- Structural Claim → Evidence Use → Source references: present and ID-aligned.
- Source-fit follow-up: Evidence Use pinpoints missing; Claim C's methods/control clause needs more direct support.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
