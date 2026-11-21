# M13 source-identity adjudication — three EPA emergency-disinfection Source IDs

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: desk-review source-identity finding; no canonical records changed; no independent reviewer or specialist certification claimed.

## 1. Finding

Three distinct Source records resolve to the exact same URI:

`https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water`

| Source ID | Source identity | URI | Finding |
|---|---|---|---|
| `SRC-EPA-EMERGENCY-DISINFECTION-WATER` | U.S. EPA — Emergency Disinfection of Drinking Water | Same URI | Same EPA web page |
| `SRC-EPA-EMERGENCY-WATER-2026` | US EPA — Emergency Disinfection of Drinking Water | Same URI | Same EPA web page |
| `SRC-EPA-WATER-TREATMENT-2026` | US EPA — Emergency Disinfection of Drinking Water | Same URI | Same EPA web page |

The records differ in identifier, representation wording and preservation text, but not in the external publication identity. They are duplicate catalog entries for one page, not three independent sources and not three independent corroborations.

This finding is stronger than a URI-only heuristic because all three records were opened and their source identity, URI and linked Evidence Use records were compared.

## 2. Existing Evidence Use links

The three duplicate Source IDs are used by four Evidence Use records in three vertical slices:

| Evidence Use | Claim | Source ID | Relevance |
|---|---|---|---|
| `EU-CHEM-WATER-NO-BOIL-EPA` | `CLM-CHEM-WATER-NO-BOIL` | `SRC-EPA-EMERGENCY-DISINFECTION-WATER` | Relevant: EPA says boiling/disinfection does not remove heavy metals, salts and most other chemicals. |
| `EU-WATER-INDEPENDENT-CORROBORATION` | `CLM-WATER-INDEPENDENT-CORROBORATION` | `SRC-EPA-EMERGENCY-WATER-2026` | Relevant to the emergency boiling/disinfection limits, but it is one EPA source only. The word “independent” in the Claim/EU identifier does not make the evidence independent. |
| `EU-EPA-WATER-TREATMENT-B` | `CLM-WATER_TREATMENT_BASICS-B` | `SRC-EPA-WATER-TREATMENT-2026` | Scope concern: the linked Source is the emergency-disinfection page, not EPA's broader drinking-water treatment-technologies overview. It may support a narrow emergency-disinfection boundary, not the full general proposition about selecting treatment methods by source-water quality, target contaminants and required quality. |
| `EU-M5-WATER-EMERGENCY-DISINFECTION-D` | `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` | `SRC-EPA-WATER-TREATMENT-2026` | Relevant: the EPA emergency-disinfection page distinguishes microbial disinfection from chemical contaminants. |

## 3. Important distinction: a genuinely separate EPA source exists elsewhere

The water-treatment slice also contains `SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES`, whose URI is:

`https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies`

This is a different EPA publication/page. It is linked through separate Evidence Use records `EU-M5-EPA-DRINKING-WATER-A`, `-B` and `-C` to the corresponding three water-treatment Claims. It must not be merged with the emergency-disinfection page.

For `CLM-WATER_TREATMENT_BASICS-B`, the broader treatment-technologies source is the more relevant EPA source for the general treatment-selection proposition. The WHO source `SRC-WATER_TREATMENT_BASICS` is also separately linked. The separate `EU-EPA-WATER-TREATMENT-B` pointing to the emergency-disinfection page should not be counted as a third independent publication and should be scope-limited or editorially reconsidered.

For `CLM-CHEM-WATER-NO-BOIL`, the CDC Evidence Use `EU-CHEM-WATER-NO-BOIL` links a distinct CDC page, so the CDC and EPA sources are institutionally distinct. Their passages still need exact pinpoint verification before any E-score is raised.

## 4. Adjudication

1. Count the three EPA Source records as **one external publication identity** for source-independence and corroboration calculations.
2. Preserve the four existing Evidence Use records and their Claim links; do not delete or merge EUs merely because the Source catalog contains duplicate identities.
3. Do not count `CLM-WATER-INDEPENDENT-CORROBORATION` as independently corroborated on the basis of `EU-WATER-INDEPENDENT-CORROBORATION`: that chain currently contains one EPA publication only.
4. Review `EU-EPA-WATER-TREATMENT-B` for source-scope mismatch. The linked emergency-disinfection page is not equivalent to EPA's separate treatment-technologies overview.
5. Keep `SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES` distinct; it is a different URL/publication and is linked to the three general water-treatment Claims.
6. A canonical source-ID consolidation, EU source-ref change or Claim/EU identifier rename requires a separate bounded authorization and regression plan. This report makes no such changes.

## 5. Confidence and limits

- Exact URI identity: verified directly in all three canonical Source records.
- Linked EUs: verified directly in the three affected vertical-slice record directories.
- Claim scope: checked against the current canonical Claim statements.
- Passage-level locator verification: not completed in this identity review.
- Independent adjudication: not completed.
- Specialist review: not required to establish URL identity, but no specialist approval is claimed for water-treatment content.
- D/E/B scores changed: 0.
- Canonical records changed: 0.

M13 remains **IN PROGRESS**. This is a source-identity and linkage correction proposal, not a release decision.
