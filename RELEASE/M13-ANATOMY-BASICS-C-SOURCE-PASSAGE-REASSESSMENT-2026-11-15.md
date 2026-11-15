# M13 — Anatomy Basics C: source-passage reassessment

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Records: `CLM-ANATOMY_BASICS-C@1`, `EU-ANATOMY_BASICS-C@1`, `SRC-ANATOMY_BASICS@1`
Status: **first source-passage desk review for this Claim; no canonical record, source or D/E/B score changed.**

## 1. Current chain and source status

Claim:
> Системы органов объединяют органы, взаимодействующие для выполнения связанных функций.

The Claim and Evidence Use both reference `SRC-ANATOMY_BASICS@1`; the internal Claim and Source references resolve correctly. The Evidence Use description is generic and contains no passage locator.

The registered Source identifies “NIGMS — Cells, tissues, organs and systems” and points to:
`https://www.nigms.nih.gov/education/fact-sheets/Pages/cells-tissues-organs-and-systems.aspx`

That legacy URL could not be fetched or independently confirmed in the current source check. Do not assume it remains current merely because the institution name and title are plausible.

## 2. Direct rights-compatible source passage

Candidate replacement/additional Source:

- **Open Resources for Nursing (Open RN), *Medical Terminology — 2e***, Chapter 2, §2.2 “Levels of Organization”.
- NCBI Bookshelf official PDF mirror: https://www.ncbi.nlm.nih.gov/sites/books/NBK607454/pdf/Bookshelf_NBK607454.pdf
- PDF printed page 40; PDF text lines 937–940.
- The book's Preface states that the textbook is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**, except where otherwise noted (PDF lines 301–316). The suggested attribution is given at lines 333–337.

The §2.2 passage defines a system as a group of organs that work together to perform major functions or meet physiological needs of the body. This directly supports the Claim's core statement that organs in an organ system interact to perform related functions.

### Rights and scope

- The cited Open RN textbook is CC BY 4.0; the section is part of the Open RN authored chapter and is not identified as third-party/OpenStax material in the section itself.
- Preserve attribution to the editors/authors and the CC BY 4.0 licence if the project later stores or adapts any material.
- The passage is specifically about human-body organization. It supports the Claim in a human-anatomy context; if the Claim is intended to cover all animal/plant anatomy, add a comparative source or narrow the Claim's scope.
- The old NIGMS URL remains unverified and should not be silently replaced. Add the Open RN Source as a distinct versioned Source, or replace the old Source only through the authorized Source-version process.

## 3. Assessment

**Passage status: DIRECT CONCEPTUAL SUPPORT — human anatomy scope.**

The source directly supports the group/function relationship. It does not establish a universal taxonomy of organ systems across all organisms, and it does not state that organ-system boundaries are always unambiguous. Those stronger propositions are outside the Claim and should not be inferred.

Proposed locator:
- Open RN, *Medical Terminology — 2e*, Chapter 2, §2.2 “Levels of Organization”, PDF p. 40, paragraph defining a system as a group of organs working together.

## 4. Proposed remediation — not applied

If separately authorized:
1. Add a distinct Source record for Open RN, *Medical Terminology — 2e*, with the editors, 2024 publication year, Chapter 2 §2.2, NCBI Bookshelf PDF URI and CC BY 4.0 licence.
2. Add a versioned Evidence Use for Claim C with the exact §2.2 locator and attribution/licence metadata.
3. Decide whether to retain the legacy NIGMS Source as a separate unverified reference or replace it through an authorized versioned Source update.
4. If the Claim is meant to cover more than human anatomy, add a comparative biology/anatomy Source or narrow the Claim.
5. Run Claim/EU/Source linkage, Source identity, offline edition and release-conformance regressions.

## 5. Disposition

| Measure | Result |
|---|---:|
| Claim source-passage review | 1 |
| Direct conceptual support at stated human-anatomy scope | 1 |
| Existing canonical EU locator added | 0 |
| New canonical Source added | 0 |
| Canonical Claim/EU/Source JSON changed | 0 |
| Historical D/E/B scores changed | 0 |
| Independent anatomy specialist review completed | 0 |
| Human View and publication clearance | 0 |

The Claim remains **HOLD** pending authorized versioned Source/EU remediation, final scope wording, independent specialist review and Human View. This desk review does not close M13 or authorize publication.
