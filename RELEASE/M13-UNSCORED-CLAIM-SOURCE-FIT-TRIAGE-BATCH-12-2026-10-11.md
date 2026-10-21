# M13 Unscored Claim Source-Fit Triage — Batch 12

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **source-fit triage only; no D/E/B scores assigned**

## Scope and controls

- Frozen corpus denominator: **1,494 Claims**.
- Inventory rows reviewed: **511–540 inclusive (30 Claims)**.
- All 30 rows are currently marked `NOT_INSPECTED / UNSCORED` in the inventory.
- Claims without scored rows remain **1,242**; this pass does not modify the scoring ledger.
- This is a source-fit and record-integrity triage. It does not establish that each source passage supports the complete Claim; exact passage verification remains necessary.
- No canonical Claim, Evidence Use, Source, Context, or Relation JSON was changed.

## Findings by Claim

| Inventory row(s) | Claim ID(s) | Source-fit / integrity finding | Disposition |
|---|---|---|---|
| 511–512 | `CLM-FINANCIAL_MARKETS_BASICS-B/C` | The Claims cover differences among financial instruments/participants and a framework for assessing markets. Both EUs use the same generic description for IMF's broad “Financial Markets” topic page, with no section or paragraph locator. | Find exact IMF passages or more suitable sources for each proposition; distinguish descriptive framework from a universally complete checklist. |
| 513–515 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A/B/C` | The NIST source is an official, relevant program page, but EUs provide title-level descriptions only. A lists overall building fire-safety aims, B gives a non-exhaustive set of measures, and C makes a jurisdiction-dependent regulatory claim. | Pinpoint program guidance and relevant codes/authority for C; preserve “may include” and jurisdictional scope. High-consequence building-safety material should not enter a public pilot without specialist review. |
| 516–518 | `CLM-FIRE_SAFETY_BASICS-A/B/C` | **Identifier alias discrepancy:** filenames use hyphenated separators, while the embedded `record_id` values use underscore-separated forms (`CLM_FIRE_SAFETY_BASICS_A`, etc.); linked EUs and Source also use underscore IDs. The primary U.S. Fire Administration source is a broad prevention landing page. Claim B has a separate NFPA EU/Source, but that source's locator is a home-escape-planning page and does not automatically support all listed categories. | Preserve exact IDs and reconcile aliases across all linked records; do not rename/merge by inference. Verify each claim against the correct source passage. |
| 519–521 | `CLM-FIRE-A/B/C` | Ready.gov/FEMA wildfire page is official and relevant to evacuation, planning, and residual hazards. EUs are generic, with no exact section. A/B/C cover distinct contexts and safety steps, so a single broad page cannot be assumed to support all details. | Pinpoint the matching wildfire guidance; confirm the “shelter locations,” pets/accessibility, and post-fire hot-ash details are stated in the linked official guidance. Treat as high-consequence safety content. |
| 522–524 | `CLM-FISHERIES_BASICS-A/B/C` | FAO's fisheries reference is a plausible subject source, but the EU text is generic. A is a broad socioeconomic proposition; B covers management; C lists factors affecting individual fisheries. One cited page may not support the full breadth of all three. | Locate the exact FAO sections and check geographic/temporal scope; split or narrow propositions if the evidence only supports part of them. |
| 525 | `CLM-FLOOD-CLEAN-DISINFECT` | CDC's “Cleaning and Sanitizing With Bleach After an Emergency” is specific and relevant, but the claim says all surfaces that contacted floodwater should be cleaned and disinfected according to official guidance. The EU merely says CDC supports the recommendation. | Verify the exact scope, surface types, and product/procedure caveats; avoid a universal interpretation beyond CDC guidance. |
| 526 | `CLM-FLOOD-CLEAN-PROTECT` | CDC source is relevant to post-emergency cleaning, but the claim combines PPE and avoiding skin/eye contact. The EU description is generic. | Pinpoint both parts of the recommendation; check that the PPE language matches the applicable task and exposure conditions. |
| 527–528 | `CLM-FLOOD-REENTRY-HAZARD-ESCALATION`, `CLM-FLOOD-REENTRY-SAFE` | EPA “Flooded Home” is relevant to electrical/structural hazards and cleanup. Both claims give consequential re-entry advice; EUs are brief and lack exact locators. Their scopes overlap and should be compared for duplication and distinct escalation criteria. | Priority exact-passage and safety-language review; verify the threshold for professional inspection and ensure no wording encourages entry into a hazardous structure. |
| 529 | `CLM-FLOOD-FOOD-CONTACT` | CDC's food-safety-after-emergency page directly concerns food that may have contacted flood/sewage water; the EU is more specific than several earlier entries but still lacks a pinpoint locator. | Verify the official wording and boundary conditions; preserve distinctions among types of packaging and food. |
| 530 | `CLM-FLOOD-FOOD-FDA-CONTACT` | The Claim is in English and combines the general no-consumption rule with a narrow exception for certain undamaged waterproof commercial packages. The FDA source is directly relevant; the EU describes an independent corroboration and a packaging-specific distinction. | Check exact FDA procedure and scope. Keep the exception inseparable from its conditions; do not broaden it into a general salvage rule. |
| 531 | `CLM-FLOOD-FOOD-OPEN-PACKAGE` | CDC source is relevant and the EU directly mentions non-waterproof packaging, but the claim includes both non-hermetic packaging and possible contact with flood/sewage water. | Verify packaging terminology and the exact disposal rule; distinguish this CDC rule from the more conditional FDA salvage procedure in row 530. |
| 532–534 | `CLM-FLOOD-A/B/C` | Ready.gov/FEMA flood page is relevant to alerts, avoiding moving water, and flood impacts. EUs use a generic source description; the propositions differ in immediacy and operational consequence. | Pinpoint each official passage and verify the wording against current guidance. Treat A/B as high-consequence advice, not as fully supported solely by the source URL. |
| 535–537 | `CLM-FLUID_MECHANICS_BASICS-A/B/C` | A is a slice-description/template statement; B and C are source/context/specialist-review guidance rather than fluid-mechanics domain propositions. The linked OpenStax section is specifically “Fluid Dynamics,” but EUs are generic. | Adjudicate A/B/C with the cross-slice methodology-template family; do not score them as three independent domain facts. If retained as editorial context, classify them consistently and separately from domain Claims. |
| 538–540 | `CLM-FOOD_DISTRIBUTION_BASICS-A/B/C` | FAO's broad “Food Systems” page is relevant to food distribution in general, but the EUs are title-level and no passage is identified. A covers system links, B lists influencing factors, C rejects production volume as the sole determinant of local availability. | Find precise FAO passages or other suitable sources for each claim; particularly substantiate C's “not determined solely” wording and avoid implying production is irrelevant. |

## Cross-cutting findings

1. **Identifier consistency:** Fire Safety Basics uses underscore-style internal IDs against hyphenated filenames. This must be handled as an alias/integrity issue; no automatic renaming is authorized.
2. **Template family:** Fluid Mechanics Basics A/B/C appear to be slice-introduction, source/context, and specialist-review guidance, not three independent domain facts. Review together with the existing cross-slice template adjudication.
3. **High-consequence content:** Building fire protection, wildfire response, flood re-entry, flood cleanup, and flood-food safety require exact official passage checks and relevant specialist review before any public pilot.
4. **Generic EUs:** Several EUs say only that a source “supports” the claim or is used within scope. That language is not a reproducible locator and cannot substitute for exact-passage verification.
5. **Source scope:** Broad official pages may be credible but still insufficient for detailed lists, exceptions, regulatory claims, and operational safety advice.

## Batch outcome

- Claims triaged: **30**.
- D/E/B scores assigned: **0**.
- Canonical JSON edits: **0**.
- Claims without scored rows: **1,242 (unchanged)**.
- M13 status: **OPEN**. Exact-passage verification, template-family adjudication, scoring, independent review, and final exact-head CI remain required.
