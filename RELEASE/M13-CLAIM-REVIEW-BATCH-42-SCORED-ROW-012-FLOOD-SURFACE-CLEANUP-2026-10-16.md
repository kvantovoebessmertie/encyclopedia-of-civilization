# M13 Batch 42 — Scored row 012: cleaning and disinfecting after floodwater contact

Date: 2026-10-16  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-FLOOD-CLEAN-DISINFECT@1`  
Evidence Use version: `EU-FLOOD-CLEAN-DISINFECT@1`  
Source version: `SRC-CDC-FLOOD-CLEANUP-2026@1`

## Claim under review

> После чрезвычайной ситуации поверхности, контактировавшие с паводковой водой, следует очистить и продезинфицировать в соответствии с официальными рекомендациями.

## Current record linkage

The canonical Source record identifies CDC — *Cleaning and Sanitizing With Bleach After an Emergency*:
https://www.cdc.gov/hygiene/about/cleaning-and-sanitizing-with-bleach-after-an-emergency.html

The current Evidence Use points to that Source but gives only a generic description (“CDC supports the documented recommendation”), without a pinpointed passage. The exact stored URI could not be directly inspected through the available page-opening path during this review. This is a retrieval limitation, not evidence that the source is offline; the exact current URI-to-passage match remains unverified.

## Corroborating passages checked

CDC, *Safety Guidelines: Floodwater*, says to clean walls, hard floors and other surfaces with soap and water and then disinfect them; it also warns that floodwater may contain multiple contaminants:
https://www.cdc.gov/floods/safety/floodwater-after-a-disaster-or-emergency-safety.html

U.S. EPA, *Flood Cleanup to Protect Indoor Air and Your Health*, says to clean surfaces first with water and detergent, then use an appropriate EPA-registered disinfectant/sanitizer on suitable surfaces and follow the product label. It explicitly warns not to mix cleaning products or add bleach to other chemicals:
https://www.epa.gov/emergencies-iaq/flood-cleanup-protect-indoor-air-and-your-health

These official passages directly corroborate the Claim's general recommendation. They do not establish that one disinfectant or dilution is suitable for every material, contamination type, or jurisdiction.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-FLOOD-CLEAN-DISINFECT` | 2 | 1 | 2 | **D=2:** practical cleanup recommendation after a flood. **E=1:** CDC and EPA guidance corroborate the proposition, but the exact currently linked CDC URI/passage was not directly verified and the Evidence Use is generic. **B=2:** the Claim appropriately defers to official guidance and does not assert one universal chemical or dilution. |

## Safety boundary

Follow local public-health guidance and the product label. Never mix bleach with other cleaning products. Do not apply a single dilution indiscriminately to all surfaces or materials.

## Disposition

**HOLD pending direct verification of the current Source URI, independent Human View, and the M13 high-consequence review gate.** This review is not specialist approval or publication clearance.

No canonical Claim, Evidence Use, or Source record changed. Any source-link or Evidence Use correction requires separate authorization and a versioned regression.

This is row 012 of Batch 42, not a release decision.
