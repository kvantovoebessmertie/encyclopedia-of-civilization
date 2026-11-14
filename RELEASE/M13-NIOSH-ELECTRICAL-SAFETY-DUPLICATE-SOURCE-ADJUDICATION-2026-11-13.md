# M13 source-identity adjudication — duplicate CDC/NIOSH electrical-safety Source records

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: desk-review source-identity and claim-linkage finding; no canonical records changed; no independent reviewer or specialist certification claimed.

## 1. Exact duplicate Source identity

Two Source records resolve to the exact same URI:

`https://cdc.gov/niosh/electrical-safety/about/`

| Source ID | Source identity | Linked Evidence Use |
|---|---|---|
| `SRC-ELECTRICAL_SAFETY_BASICS` | Электробезопасность: CDC/NIOSH | `EU-ELECTRICAL_SAFETY_BASICS-A`, `-B`, `-C` |
| `SRC_ELECTRICAL_SAFETY_NIOSH` | CDC/NIOSH — Electrical Safety | `EU-ELECTRICAL_SAFETY_NIOSH-A` |

Both records identify the same CDC/NIOSH electrical-safety page. The title language differs, but issuer and URI are the same. These are duplicate catalog identities, not two independent publications or authorities.

## 2. Claim and Evidence Use relationship

The first Source record supports three Claims:
- `CLM-ELECTRICAL_SAFETY_BASICS-A`: electrical hazards include shock, burns, arcing and fires.
- `CLM-ELECTRICAL_SAFETY_BASICS-B`: energized electrical work should be performed by qualified persons using appropriate procedures and protective equipment.
- `CLM-ELECTRICAL_SAFETY_BASICS-C`: unqualified people should treat electrical systems as hazardous, not as objects for self-repair.

The second Source record supports a separate Claim:
- `CLM-ELECTRICAL_SAFETY_NIOSH_A`: NIOSH identifies shock, burns, arcing and fire as hazards and says electrical work should be performed by qualified persons.

The latter Claim substantially overlaps the subject matter of Claims A/B, but it is a separate Claim record and does not constitute independent corroboration for them: its Evidence Use points to the same CDC/NIOSH page under a second Source ID. The phrase “Independent occupational-safety research authority” in `EU-ELECTRICAL_SAFETY_NIOSH-A` is misleading as an independence statement in this context. NIOSH is the authority publishing the same page, not a second source independent of the other NIOSH Source record.

## 3. Adjudication

1. Count the two Source IDs as one external publication identity for source independence and corroboration.
2. Preserve all four Evidence Use records and their Claim links; different Claims may use different passages from one page.
3. Do not count `EU-ELECTRICAL_SAFETY_NIOSH-A` as independent corroboration of Claims A/B/C.
4. Review whether `CLM-ELECTRICAL_SAFETY_NIOSH_A` is substantively redundant with Claims A/B. Any merge, narrowing or cross-reference is an editorial decision requiring authorization; do not delete or silently collapse Claims.
5. Replace the misleading “independent” wording in the EU description only after bounded authorization. The current text can be read as claiming source independence where none exists.
6. Add exact page/section locators to each relevant EU after verifying the current CDC/NIOSH page content. Do not infer pinpoint support from the landing-page URL alone.
7. Preserve both historical Source IDs and their history until a versioned consolidation is authorized and tested.

## 4. Verification boundary

- Exact URI equality: verified directly in both canonical Source records.
- Claim/EU links: verified directly in the electrical-safety slice.
- Substantive overlap: visible in the current Claim statements; full editorial deduplication not performed.
- Exact passage/locator verification: not completed in this source-identity pass.
- D/E/B scores changed: 0.
- Canonical records changed: 0.
- Independent adjudication: not completed.

M13 remains **IN PROGRESS**. This is a source-identity and Claim-overlap finding, not release clearance.
