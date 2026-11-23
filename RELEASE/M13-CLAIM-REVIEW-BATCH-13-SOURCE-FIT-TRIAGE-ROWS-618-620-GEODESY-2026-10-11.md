# M13 Batch 13 — source-fit triage (rows 618–620): geodesy

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; source identity and core definitions fit, claim-specific pinpoints still missing**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional, not finalized ledger scores. No canonical JSON changed.

## Source trail

The three Claims cite `SRC-GEODESY_BASICS`, identified as NOAA National Geodetic Survey “What is Geodesy?” with stored URI `https://www.ngs.noaa.gov/INFO/facts/geodesy.shtml`. The destination is accessible and directly defines geodesy as measuring and understanding Earth's geometric shape, orientation in space, and gravity field. It further explains that geodesists assign consistent coordinates to points, and that these points form the basis of a spatial reference system that makes different maps consistent. NOAA also lists mapping, land boundaries, transportation and navigation safety as applications. citeturn212413search0

The source is a good overall match, but the three Evidence Use records currently contain only generic descriptions, without exact paragraph or section pinpoints. Therefore source-fit can be assessed provisionally from the public source, but the canonical evidence chain is not yet release-grade.

## 1. `CLM-GEODESY_BASICS-A` — **D2 / E3 / B2**

**Claim:** “Геодезия изучает геометрическую форму Земли, её ориентацию в пространстве и гравитационное поле с высокой точностью.”

**Assessment:** The definition captures the field's three core properties but does not explain how measurements and models are used (D2). The NOAA source explicitly identifies all three properties and accurate measurement/understanding, so fit is strong (E3). “С высокой точностью” is consistent with the source's emphasis on accurate measurement, though the claim does not specify that precision varies by method and application (B2).

**Disposition:** Strong candidate to retain. Add an exact pinpoint to the definition paragraph in Evidence Use.

## 2. `CLM-GEODESY_BASICS-B` — **D2 / E3 / B2**

**Claim:** “Геодезические измерения позволяют задавать согласованные координаты точек и формировать пространственную основу для карт и других геоданных.”

**Assessment:** Explains the practical result of geodetic measurement but not the reference-frame mechanics or uncertainty (D2). NOAA directly states that geodesists assign coordinates consistently and that accurately measured points form the basis of a spatial reference system used to make maps consistent (E3). “Других геоданных” is broader than the source's explicit example of maps, but remains plausible; avoid implying every dataset is automatically consistent without shared reference definitions (B2).

**Disposition:** Strong fit with a boundary clarification: consistency depends on using a common spatial reference system. Add a pinpoint to the coordinate / spatial-reference-system paragraphs.

## 3. `CLM-GEODESY_BASICS-C` — **D2 / E2 / B2**

**Claim:** “Геодезическая основа используется в картографии, навигации и определении границ; конкретные измерения требуют подходящих систем координат и методов контроля.”

**Assessment:** Gives practical applications and a methodological caution but does not explain the role of reference frames, datums, or control (D2). NOAA directly supports mapping, navigation safety and land boundaries; its explanation of consistent coordinates supports the first part of the second sentence, but “методы контроля” is not specifically established by the generic Evidence Use record (E2). The wording is appropriately general, though the measurement-control requirement needs a more specific supporting passage (B2).

**Disposition:** Retain provisionally. Pinpoint the NOAA application examples and coordinate consistency discussion; add a specific geodetic-control/datum source if “методы контроля” is intended as a technical requirement.

## Batch accounting

- Individual Claims triaged: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Stored source locator: accessible and on-topic.
- Exact source pinpoints recorded in canonical Evidence Use: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
