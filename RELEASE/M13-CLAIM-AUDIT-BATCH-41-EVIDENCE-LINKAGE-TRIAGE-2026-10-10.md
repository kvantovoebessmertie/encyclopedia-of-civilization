# M13 Batch 41 — Evidence-Linkage Triage (Three-Slice Diagnostic)

Date: 2026-10-10  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: structural and locator triage only; **not** a scored Batch 41 review.

## Inspected examples

### 1. `acid-base-basics`

- `EU-ACID_BASE_BASICS-A` links Claim A to `SRC-ACID_BASE_BASICS`, with role `supports`.
- Source points to the OpenStax Chemistry 2e summary page on acid-base equilibria.
- EU description is generic and does not identify a section, equation, page, quotation, or other pinpoint locator for the Brønsted–Lowry definition in Claim A.
- A separate EU record, `EU-ACID-BASE-IUPAC-CORROBORATION`, links Claim B to IUPAC Gold Book pH terminology. This is a distinct Claim B link and must not be counted as direct corroboration for Claim A.

**Triage:** structural link present; Claim A pinpoint support not demonstrated by the local evidence description.

### 2. `acoustics-basics`

- `EU-ACOUSTICS_BASICS-A` links Claim A to `SRC-ACOUSTICS_BASICS`, with role `supports`.
- Source points to the WHO Environmental Noise Guidelines landing page.
- EU description does not name the relevant recommendation, chapter, table, or passage. A landing-page link alone does not establish which portion supports the specific claim.

**Triage:** structural link present; claim-specific support remains unverified.

### 3. `administrative-law-basics`

- `EU-ADMINISTRATIVE_LAW_BASICS-A` links Claim A to a Cornell Legal Information Institute administrative-law reference, with role `supports`.
- `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-A` also links Claim A to an OECD Public Integrity Handbook page, described as an independent institutional source.
- Both local EU descriptions are generic; neither identifies the exact passage or legal jurisdiction/context that supports Claim A.
- The existence of two source records is not, by itself, proof of independence or substantive corroboration. The source content and relevant passages still need to be compared.

**Triage:** two declared source links present; pinpoint support, scope/jurisdiction fit, and substantive independence remain unverified.

## Cross-cutting finding

In these three slices, Claim → Evidence Use → Source pointers are structurally present for the inspected examples. However, the local evidence descriptions generally lack pinpoint locators needed for another reviewer to reproduce the support check. This is an evidence traceability finding, **not a finding that the claims are false**.

## Required next actions

1. Continue the same check across all 100 Batch 41 candidates: resolve each Claim to every applicable Evidence Use and Source record, validate reference IDs, and record locator specificity.
2. For high-consequence claims, inspect the actual source passage and its date, jurisdiction, population, and conditions rather than relying on landing-page identity.
3. Only after the complete linkage and source-fit checks, assign D/E/B with a rationale per claim. Do not infer scores from record structure alone.

## Status

- Identity/type gate: **100/100 candidates inspected**, 91 exact filename/internal-ID matches and 9 separator-only variants (see identity checkpoint).
- Prior scored-report text overlap: no exact or separator-insensitive IDs found in the inspected Batch 12 and 16–40 reports (see overlap scan).
- Evidence linkage: **diagnostic triage in progress**; Batch 41 remains unscored and incomplete.
- No Claim, Source, Evidence Use, or other content records were modified.
