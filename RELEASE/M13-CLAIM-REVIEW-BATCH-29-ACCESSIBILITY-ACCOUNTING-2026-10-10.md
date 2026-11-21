# M13 Claim Review Batch 29 — Accessibility and Accounting Foundations
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **6 additional Claims reviewed. This is a bounded review batch, not domain closure or corpus completion.**

## Method
Reviewed three Claims each in `accessibility-basics` and `accounting-basics`, including linked Evidence Use and source records. Accessibility is grounded in the UN Convention on the Rights of Persons with Disabilities; accounting is linked to the IFRS Conceptual Framework. D (explanatory depth), E (claim-specific evidence fit) and B (boundary discipline) are scored independently from 0–3. This is not a building-accessibility certification, accounting opinion or jurisdiction-specific compliance assessment.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-ACCESSIBILITY_BASICS-A` | 2 | 3 | 3 | The claim connects accessibility with equal participation by people with disabilities. The Evidence Use record names the relevant UN Convention rights framework and explicitly says it does not establish the accessibility of a specific site. Strong boundary discipline; add practical examples in a later Human View pass. |
| `CLM-ACCESSIBILITY_BASICS-B` | 2 | 3 | 3 | The claim that barriers can limit independent and equal use is supported by the Convention's Article 9 framing across physical environment, transport, information and communications. The Evidence Use correctly avoids treating the source as an assessment of a specific user or location. |
| `CLM-ACCESSIBILITY_BASICS-C` | 2 | 3 | 3 | Correctly states that concrete requirements depend on purpose, users and jurisdiction. The Evidence Use distinguishes the international framework from local technical/legal requirements. For operational use, a checklist must cite current local standards and include user testing; this claim alone is not a compliance method. |
| `CLM-ACCOUNTING_BASICS-A` | 2 | 1 | 2 | Accounting as systematic information about transactions and financial position is a credible foundation, but the IFRS Conceptual Framework source is broad and the Evidence Use description does not identify specific support. Clarify whether the claim describes general accounting or financial reporting under a named framework, since scope differs across standards and entities. |
| `CLM-ACCOUNTING_BASICS-B` | 2 | 1 | 2 | Structured information for report users is consistent with the general purpose of financial reporting. The linked Evidence Use is generic and does not show which part of the IFRS framework supports the proposition. Preserve distinctions between general-purpose financial statements, management accounts and other reporting forms. |
| `CLM-ACCOUNTING_BASICS-C` | 2 | 1 | 3 | Correctly recognizes that estimates and classifications depend on standards and circumstances. The generic Evidence Use description prevents claim-specific traceability. The boundary is important: the record must not imply all entities use IFRS or that estimates are arbitrary; the applicable framework and facts constrain them. |

## Findings
1. **Accessibility slice has stronger boundary-aware evidence:** all three Evidence Use descriptions identify the contribution of the UN Convention and state that it is not a site-specific certification.
2. **Accounting slice has a confirmed Evidence Use documentation debt:** all three descriptions are generic and should be rewritten to identify the relevant conceptual-framework passages and the scope of the claim.
3. **Framework boundaries matter:** an international disability-rights convention and an accounting conceptual framework are different types of authority; neither replaces current local technical requirements, applicable accounting standards or professional review.
4. No content Records were changed. These six Claims remain within the frozen 1,494-Claim denominator. This batch does not close accessibility, accounting, Human View, or M13.

## Records inspected
- `CONTENT/vertical-slices/accessibility-basics/records/CLM-ACCESSIBILITY_BASICS-A.json`
- `CONTENT/vertical-slices/accessibility-basics/records/CLM-ACCESSIBILITY_BASICS-B.json`
- `CONTENT/vertical-slices/accessibility-basics/records/CLM-ACCESSIBILITY_BASICS-C.json`
- `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-A.json`
- `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-B.json`
- `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-C.json`
- `CONTENT/vertical-slices/accounting-basics/records/CLM-ACCOUNTING_BASICS-A.json`
- `CONTENT/vertical-slices/accounting-basics/records/CLM-ACCOUNTING_BASICS-B.json`
- `CONTENT/vertical-slices/accounting-basics/records/CLM-ACCOUNTING_BASICS-C.json`
- `CONTENT/vertical-slices/accounting-basics/records/EU-ACCOUNTING_BASICS-A.json`
- `CONTENT/vertical-slices/accounting-basics/records/EU-ACCOUNTING_BASICS-B.json`
- `CONTENT/vertical-slices/accounting-basics/records/EU-ACCOUNTING_BASICS-C.json`

## Sources
- United Nations, Convention on the Rights of Persons with Disabilities: https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html
- IFRS Foundation, Conceptual Framework for Financial Reporting: https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/

## Acceptance status
Six additional Claim rows have explicit D/E/B scores and rationales. Follow-up action: repair accounting Evidence Use descriptions to be claim-specific. Full 1,494-Claim scoring, high-consequence recall, Human View, Relation endpoint review, independent scoring review, authorized corrections with regression tests, and final same-HEAD 3/3 CI remain open.
