# First Edition — Cross-Slice Relation Semantic Review Batch 2

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `80b4b11f7df2c193f365e8db660ab7f53076d305`  
Status: **6/63 ADDITIONAL RELATIONS REVIEWED; 10 DISTINCT PARTICIPANT CLAIMS AND 9 SOURCE REFERENCES EXACT-VERIFIED; ALL LINKS CONTEXTUAL ONLY**

## 1. Scope

This bounded pass reviews six cross-slice Relations connecting the opening survival/safety domains:

- `REL-CROSS-LIGHTING-HOME-FIRE@1`
- `REL-CROSS-CO-EMERGENCY-ESCALATION@1`
- `REL-CROSS-CO-PREVENTION@1`
- `REL-CROSS-HOME-FIRE-ALERTS@1`
- `REL-CROSS-FLOOD-SAFETY@1`
- `REL-CROSS-ALERTS-WILDFIRE-SMOKE@1`

The ten distinct participant Claims and nine unique provenance Sources were fetched from their canonical slice paths. Each matched its declared exact ID, version 1 and record type. The six Relation records each contain two participants, two matching `linked_record` roles, undirected direction and the shared `CTX-CROSS-SLICE-LINKAGE@1` frame.

## 2. Semantic decisions

| Relation | Semantic assessment | Release-use status |
|---|---|---|
| lighting ↔ home-fire response | Temporary lighting choices and home-fire escape precautions share a credible fire-prevention context. The link does not make candles a safe backup or replace either Claim's instructions. | ACCEPT AS CONTEXTUAL NAVIGATION |
| CO emergency escalation | Both Claims describe the same emergency escalation sequence, with one focused on heating and the other on generator exposure. The relation is relevant but the Claims substantially overlap; retain as a navigation link only and flag for editorial deduplication/clear distinction. | HOLD — REDUNDANCY REVIEW |
| CO prevention | Generator placement outdoors and the prohibition on using fuel-burning devices indoors are directly related CO-prevention boundaries. Preserve the CDC-specific 20-foot rule as source/jurisdiction-specific; do not generalize it as a universal code requirement. | ACCEPT AS CONTEXTUAL NAVIGATION |
| home-fire response ↔ emergency alerts | Fire escape response and advance awareness of emergency alerts are complementary preparedness/response topics. The relation does not imply that a phone alert substitutes for smoke alarms or immediate evacuation. | ACCEPT AS CONTEXTUAL NAVIGATION |
| flood food safety ↔ flood cleanup protection | Food contamination after floodwater contact and personal protection during cleanup share a flood-recovery hazard context. The link must not be read as a complete cleanup protocol or food-disposal decision tree. | ACCEPT AS CONTEXTUAL NAVIGATION |
| alerts ↔ wildfire smoke | Emergency warning preparedness and local air-quality monitoring during wildfire smoke are directly related public-warning and protective-action topics. The relation does not replace current local instructions or health guidance. | ACCEPT AS CONTEXTUAL NAVIGATION |

## 3. Integrity and safety boundaries

- 6/6 Relation records fetched and parsed.
- 10/10 distinct participant Claim records fetched and parsed; all exact IDs, versions and types match.
- 9/9 unique provenance Source records fetched and parsed; all exact IDs, versions and types match.
- All 6 Relations use the exact shared Context frame and the declared two-role undirected structure.
- These checks establish graph integrity and semantic navigability only. They do not establish that the underlying safety Claims are sufficiently evidenced, current in every jurisdiction, or independently approved.
- All high-consequence safety content remains subject to its own evidence, applicability, rights and qualified-review gates.

## 4. Decision

- Five Relations are accepted as contextual navigation links only.
- One Relation (CO emergency escalation) remains HOLD for release use pending review of substantial Claim overlap.
- No canonical Relation, Claim, Source or Context was changed.
- No publication state, INCLUDE/HOLD/EXCLUDE decision, allowlist or release authorization was changed.
- This batch reviews 6 of 63 Relations; the wider 97 non-candidate endpoint reconciliation remains open and must be updated only after exact overlap accounting.
