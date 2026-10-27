# M13 Batch 13 — source-fit triage (rows 627–629): groundwater

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; USGS source directly supports core definition and aquifer function, with claim-specific Evidence Use pinpoints still absent**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON remains unchanged.

## Source trail and exact source locations

The three Claims reference `SRC-GROUNDWATER_BASICS@1`, USGS *Groundwater Basics*:
https://www.usgs.gov/mission-areas/water-resources/science/groundwater-basics

Relevant source passages:
- **Background**: groundwater is water in the ground that fully saturates pores or cracks in soils and rocks.
- **Background, aquifers**: most extracted groundwater is stored in and moves slowly through permeable rocks called aquifers; material must be saturated enough to yield significant quantities of water for extraction.
- **Information on Groundwater Quality and Quantity**: groundwater is replenished by precipitation; quantity and quality vary with local climate and geology; human activities and pollutants can degrade groundwater quality, and intensive pumping can lower water tables or cause saltwater intrusion and land subsidence.

The existing Evidence Use records have brief generic summaries but do not identify these exact passages. Public-source fit is strong for the basic propositions, but the canonical evidence chain still needs claim-specific pinpoints.

## 1. `CLM-GROUNDWATER_BASICS-A` — provisional **D2 / E3 / B2**

**Claim:** “Подземные воды находятся в насыщенных порах и трещинах грунтов и горных пород.”

**Assessment:** This is an accurate introductory definition but does not explain the water table, recharge, pressure, or variation with depth (D2). The USGS Background passage directly defines groundwater as water that fully saturates pores or cracks in soils and rocks, making the evidence fit strong (E3). The claim is appropriately bounded and does not imply a continuous underground lake or universal depth (B2).

**Disposition:** Retain provisionally. Pinpoint the USGS Background definition passage in Evidence Use.

## 2. `CLM-GROUNDWATER_BASICS-B` — provisional **D2 / E3 / B2**

**Claim:** “Водоносные горизонты способны хранить и передавать подземную воду в количествах, пригодных для использования.”

**Assessment:** The statement introduces aquifer function but does not distinguish permeability, transmissivity, storage, or yield testing (D2). USGS directly describes aquifers as permeable rocks through which groundwater moves and from which significant quantities may be extracted when sufficiently saturated; this is a strong fit (E3). “Пригодных для использования” could be misread as potable quality. The USGS notes groundwater may not be clean enough for use without treatment, so clarify that “usable quantities” concerns yield, not necessarily water quality (B2).

**Disposition:** Retain provisionally, preferably adjust wording to “в количествах, достаточных для отбора” and avoid equating aquifer yield with drinking-water safety. Pinpoint the aquifer paragraph.

## 3. `CLM-GROUNDWATER_BASICS-C` — provisional **D2 / E3 / B2**

**Claim:** “Качество и количество подземных вод зависят от геологии, пополнения, использования и загрязнения.”

**Assessment:** This is a broad synthesis and does not distinguish natural chemistry, recharge rates, abstraction, or contaminant pathways (D2). The USGS source directly discusses climate/geology-related variability, precipitation recharge, water-use demand, pollution, pumping-related declines and saltwater intrusion. The main relationship is supported (E3). “Зависят от” is appropriately general, but these factors vary by aquifer and locality; the statement should not imply the same influence or magnitude everywhere (B2).

**Disposition:** Retain provisionally. Add pinpoints to the recharge/variability and quality/quantity passages, and preserve the geographic/contextual limitation.

## Batch accounting

- Individual Claims reviewed in this note: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
