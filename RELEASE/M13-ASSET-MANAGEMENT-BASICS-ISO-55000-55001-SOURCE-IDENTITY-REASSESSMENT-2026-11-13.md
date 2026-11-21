# M13 — asset management basics: ISO 55000 / ISO 55001 source identity reassessment

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Review class: follow-up source-identity and public-passage reassessment; **not new first-pass Claim coverage**. Batch 41, scored block 04, rows 56–58 already flagged a material mismatch between the Source identity and URI. This report confirms the mismatch against the official ISO catalogue and separates the scope of the two standards.

## 1. Exact records and reference-chain integrity

| Claim | Evidence Use | Current Source | Version |
|---|---|---|---|
| `CLM-ASSET_MANAGEMENT_BASICS-A` | `EU-ASSET_MANAGEMENT_BASICS-A` | `SRC-ASSET_MANAGEMENT_BASICS` | v1 / v1 / v1 |
| `CLM-ASSET_MANAGEMENT_BASICS-B` | `EU-ASSET_MANAGEMENT_BASICS-B` | `SRC-ASSET_MANAGEMENT_BASICS` | v1 / v1 / v1 |
| `CLM-ASSET_MANAGEMENT_BASICS-C` | `EU-ASSET_MANAGEMENT_BASICS-C` | `SRC-ASSET_MANAGEMENT_BASICS` | v1 / v1 / v1 |

All three EUs point to their intended Claim and the same Source ID/version. The chain is structurally valid. The Source record identity says:

`ISO 55000:2024 — Asset management — Vocabulary, overview and principles`

but its URI is `https://www.iso.org/standard/83054.html`, which is the official ISO page for **ISO 55001:2024 — Asset management system — Requirements**. This is a material bibliographic identity/locator mismatch, not a harmless alternate URL.

Official ISO pages:
- ISO 55000:2024, vocabulary, overview and principles: https://www.iso.org/standard/83053.html
- ISO 55001:2024, asset management system requirements: https://www.iso.org/standard/83054.html
- ISO/TC 251 explanation of ISO 55000: https://committee.iso.org/sites/tc251/home/projects/published/iso-55000.html
- ISO/TC 251 explanation of ISO 55001: https://committee.iso.org/sites/tc251/home/projects/published/iso-55001.html

## 2. Claim-by-claim source fit

### Claim A — asset lifecycle, value, risk and organizational goals

Claim: “Управление активами рассматривает активы с учетом их жизненного цикла, ценности, рисков и целей организации.”

**Assessment: DIRECT at the level of the official ISO 55000 public description.**
- ISO 55000:2024 is explicitly titled *Asset management — Vocabulary, overview and principles*.
- The official ISO 55000 page describes asset management as a systematic approach to managing assets over their life cycles and enhancing the value realized from assets in support of organizational objectives.
- The ISO/TC 251 page identifies ISO 55000 as the foundational part of the series and describes its overview, terminology, principles and context for ISO 55001/55002.

The public description supports the lifecycle, value and objectives frame. The risk component is consistent with the standard's stated asset-management scope but should receive an exact clause locator from the standard text before the EU claims full passage-level precision.

**Proposed source:** ISO 55000:2024, official standard record 83053.  
**Proposed locator:** official overview and principles sections; exact clause number to be checked against the licensed standard text.

### Claim B — balancing performance, risk, cost and opportunities

Claim: “Решения по активам связаны с балансированием производительности, риска, затрат и возможностей в течение жизненного цикла.”

**Assessment: PARTIAL on the public preview; HOLD for exact passage verification.**
- The current URI's actual target, ISO 55001:2024, states that asset-management decisions balance performance, risk and expenditure to meet organizational goals.
- The public ISO 55001 description also states that the standard specifies requirements for establishing, implementing, maintaining and improving an asset-management system.
- The public description does not itself establish the full Claim's explicit “opportunities” element or provide a clause-level locator for the four-factor formulation.

The prior Batch 41 review correctly observed that the current URI points to ISO 55001, which is substantively relevant to this Claim, while the Source record names ISO 55000. The source must be split/identified accurately; do not silently treat ISO 55000 and ISO 55001 as interchangeable.

**Proposed source:** ISO 55001:2024, official standard record 83054.  
**Proposed locator:** clause on asset-management decision-making and value (the ISO/TC 251 page identifies section 4.5 as a new 2024 section); exact clause/page and “opportunities” wording require licensed-text verification.

### Claim C — coordinated asset-management system

Claim: “Система управления активами задает согласованный подход к планированию, принятию решений и улучшению управления активами.”

**Assessment: PARTIAL / scope supported, exact wording not yet verified.**
- ISO 55001:2024 is explicitly a requirements standard for an asset management system and covers its establishment, implementation, maintenance and improvement.
- ISO/TC 251 describes ISO 55001 as specifying requirements for an asset management system and identifies its intended users and system lifecycle.
- The official public summary does not fully expose the exact requirements for planning and decision-making. Those parts need clause-level verification in the standard text.

**Proposed source:** ISO 55001:2024, official standard record 83054.  
**Proposed locator:** clauses covering the asset management system, planning and asset-management decision-making; exact clause/page to be checked against the licensed standard.

## 3. Rights, access and publication boundary

- ISO's official catalogue identifies both standards as published 2024 editions and displays purchase access/pricing. The public landing pages are not the complete standards.
- ISO material is copyrighted. The availability of a public preview or official metadata page is not permission to reproduce the standard's substantial text, tables or figures.
- A complete pinpoint review of requirements clauses may require lawful access to the licensed text. Do not infer exact clause support from marketing summaries or a preview page.
- The Source record's `availability: public` field should not be interpreted as an open licence or public-domain declaration.

## 4. Proposed canonical remediation — not applied

Subject to a separately bounded authorization and dependency checks:
1. Correct the bibliographic identity/URI for the current Source to ISO 55000:2024, official record 83053, if it remains the source for Claim A.
2. Create a separate Source record for ISO 55001:2024, official record 83054, for Claims B and C.
3. Update the relevant EUs to reference the source that actually supports each Claim, preserving exact versioned Claim → EU → Source linkage.
4. Add clause/page locators only after licensed-text review. If the exact wording of Claim B's “opportunities” or Claim C's planning/decision-making components cannot be verified, narrow the Claims or add an additional rights-compatible source.
5. Preserve the historical Batch 41 scores and all prior reports append-only; record any later adjudication as a new, attributable review.

## 5. Disposition and integrity

| Measure | Result |
|---|---:|
| Claims re-assessed | 3 |
| Previously scored in Batch 41 | 3 |
| New first-pass coverage | 0 |
| Confirmed Source identity/URI mismatch | 1 |
| Direct support from official public summaries | 1 Claim at stated scope |
| Partial / exact-clause verification outstanding | 2 Claims |
| Canonical Source/EU/Claim JSON changed | 0 |
| Canonical locators added | 0 |
| Historical D/E/B scores changed | 0 |
| Independent asset-management specialist review completed | 0 |
| Full ISO standard text rights/access cleared | 0 |
| Claims accepted or release-cleared | 0 |

All three Claims remain HOLD. The confirmed mismatch is a material evidence-provenance defect. This report does not authorize canonical correction, substitute one ISO standard for another, or clear publication.
