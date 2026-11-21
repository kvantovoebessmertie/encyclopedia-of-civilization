# M13 Batch 13 — source-fit triage (rows 643–650): heat transfer, historical geography and history methods

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **eight Claims reviewed provisionally; heat-transfer definitions strongly fit the stored source, historical-map caveats need pinpoints, and history-methods source scope is weak**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores below are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON remains unchanged.

## A. Rows 643–645 — heat transfer

Stored source: U.S. Department of Energy, Building Science Education, *Heat Transfer*: https://bsesc.energy.gov/training-modules/heat-transfer

The page directly defines heat transfer as thermal energy transfer due to a temperature difference, names conduction/convection/radiation, and says building systems often experience a combination of all three.

### 1. `CLM-HEAT_TRANSFER_BASICS-A` — provisional **D2 / E3 / B2**

**Claim:** “Теплопередача — перенос тепловой энергии, обусловленный разностью температур.”

**Assessment:** A concise definition, without mechanism or rate law (D2). The DOE page directly matches the definition (E3). The wording is appropriate as a basic definition, although the details of transfer depend on the physical system and conditions (B2).

**Disposition:** Retain provisionally; pinpoint the source's opening definition.

### 2. `CLM-HEAT_TRANSFER_BASICS-B` — provisional **D2 / E3 / B2**

**Claim:** “К основным механизмам теплопередачи относятся теплопроводность, конвекция и излучение.”

**Assessment:** Correct core taxonomy but without mechanism-level explanation (D2). The source explicitly lists conduction, convection and radiation (E3). “Основным” is a standard introductory framing; do not imply these modes are always isolated from one another (B2).

**Disposition:** Retain provisionally; pinpoint the source sentence listing the three modes.

### 3. `CLM-HEAT_TRANSFER_BASICS-C` — provisional **D2 / E3 / B2**

**Claim:** “В реальных строительных системах несколько механизмов теплопередачи часто действуют одновременно.”

**Assessment:** A useful systems-level observation but does not explain coupled heat/air/moisture flows or how to calculate them (D2). The DOE page explicitly says building systems commonly experience a combination of all three forms and other energy flows (E3). “Часто” is appropriately bounded; not every simplified model must include all three mechanisms at equal importance (B2).

**Disposition:** Retain provisionally; pinpoint the page's statement on combinations in building systems.

All three heat-transfer Evidence Use records currently have generic descriptions and no exact pinpoint.

## B. Rows 646–648 — historical geography

Stored source: Library of Congress, *Collections with Maps*: https://www.loc.gov/maps/collections/

The collection directly documents historical maps for specific places and periods. The “General Maps” description says these maps depict the physical environment and cultural elements of a geographic area at a particular point in time. The collection is an appropriate source for what historical maps can contain, but it is not by itself a complete methodological guide to evaluating every map's scale, provenance or intended purpose.

### 4. `CLM-HISTORICAL_GEOGRAPHY-A` — provisional **D2 / E3 / B2**

**Claim:** “Исторические карты являются источниками пространственной информации, связанной с определённым временем и местом.”

**Assessment:** A useful description but without discussing map-making conventions or historical change (D2). LOC's historical collections directly support the link between maps, geographic areas and specific dates/periods (E3). The claim correctly calls maps “sources” rather than transparent, unmediated copies of reality (B2).

**Disposition:** Retain provisionally; add a pinpoint to LOC's “General Maps” description and a dated example.

### 5. `CLM-HISTORICAL_GEOGRAPHY-B` — provisional **D2 / E3 / B2**

**Claim:** “Картографические материалы могут показывать физическую среду и культурные элементы территории в конкретный исторический момент.”

**Assessment:** This identifies two broad content categories but does not explain how selection, symbolization or intended use shape representation (D2). LOC's “General Maps” description directly mentions physical environment and cultural elements for a geographic area at a particular time (E3). “Могут” is appropriately conditional; not every map depicts both categories (B2).

**Disposition:** Retain provisionally; pinpoint the LOC collection description.

### 6. `CLM-HISTORICAL_GEOGRAPHY-C` — provisional **D2 / E2 / B2**

**Claim:** “Интерпретация исторической карты зависит от даты, масштаба, происхождения и назначения материала.”

**Assessment:** The methodological caution is useful but does not explain how each factor affects interpretation (D2). LOC collection entries provide dates, collection histories and in some cases intended purpose, but the broad collection landing page does not establish scale and provenance as a general methodological rule for all historical maps. Source fit is partial (E2). The caveat is sound, but these variables should be checked on the individual map or catalogue record, not assumed from collection membership (B2).

**Disposition:** Retain provisionally with follow-up. Add a specific map catalogue record that exposes date, scale, creator/source and stated purpose, or cite a cartographic-methodology source.

The three LOC Evidence Use records contain summaries but no item-level pinpoints.

## C. Rows 649–650 — history methods

Stored source record: `SRC-HISTORY_METHODS_BASICS@1` is labelled “Исторические методы устанавливают и интерпретируют свидетельства о прошлом,” but its URI is the American Historical Association teaching-and-learning page:
https://www.historians.org/teaching-learning/

This is a weak match to the source identity and does not directly identify a historical-methods guide, archival-source evaluation standard, or claim-specific page. The generic Evidence Use descriptions do not supply the missing support.

### 7. `CLM-HISTORY_METHODS_BASICS-A` — provisional **D2 / E1 / B2**

**Claim:** “Историческое исследование использует источники для реконструкции и интерпретации прошлого.”

**Assessment:** This is a basic description but does not distinguish primary/secondary sources, corroboration or historiographical debate (D2). The stored locator is a broad teaching-and-learning landing page rather than a clearly identified methods resource; current canonical evidence does not pinpoint support for the claim (E1). The wording is appropriately broad and does not imply that sources provide direct, complete access to the past (B2).

**Disposition:** **HOLD for release-grade evidence.** Identify a direct source-methods page or authoritative guide, record its exact identity/locator and add a claim-specific Evidence Use pinpoint. Do not treat the AHA homepage as sufficient evidence solely because the organization is reputable.

### 8. `CLM-HISTORY_METHODS_BASICS-B` — provisional **D2 / E1 / B2**

**Claim:** “Источник имеет происхождение и контекст, которые влияют на его использование как свидетельства.”

**Assessment:** The claim captures a sound principle but does not explain provenance, audience, purpose, transmission, bias or corroboration (D2). The stored source locator does not clearly establish this methodological proposition, and Evidence Use is generic (E1). The boundary is appropriate; context informs evaluation but does not automatically invalidate a source (B2).

**Disposition:** **HOLD for release-grade evidence.** Replace or supplement the broad AHA locator with a specific source-evaluation / historical-methods resource and pinpoint the relevant section.

## Batch accounting

- Individual Claims reviewed in this note: **8**.
- New provisional D/E/B assessments recorded: **8**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/8**.
- Release holds explicitly flagged: **2** (history-methods rows 649–650); row 646–648 Claim C requires stronger methodological evidence.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete as an initial 100-candidate triage pass: **YES, provisional reviews recorded for all 100 selected candidates**. The batch is **not audit-closed**: source pinpoint follow-ups, critical linkage defects, duplicate/type checks, high-consequence review, Human View review, and finalized ledger scoring remain open.
