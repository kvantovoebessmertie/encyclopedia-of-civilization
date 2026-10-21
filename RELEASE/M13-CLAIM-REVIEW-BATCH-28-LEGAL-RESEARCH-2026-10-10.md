# M13 Claim Review Batch 28 — Legal Research Foundations
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **3 additional Claims reviewed. This is a bounded review batch, not domain closure or corpus completion.**

## Method
Reviewed the three Claims and their linked Evidence Use records in `legal-research-basics`. The source record identifies Cornell Legal Information Institute's legal-research overview. D (explanatory depth), E (claim-specific evidence fit) and B (boundary discipline) are scored independently from 0–3. This is a general research-method review, not jurisdiction-specific legal advice.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-LEGAL_RESEARCH_BASICS-A` | 2 | 1 | 2 | Search, selection and analysis of relevant legal sources in light of a defined question is a sound high-level description. The linked Evidence Use text is generic and does not identify the part of Cornell LII's material supporting each research activity. Make the source-to-claim relation specific and avoid implying that a single overview supplies a complete legal research method. |
| `CLM-LEGAL_RESEARCH_BASICS-B` | 2 | 1 | 3 | Applicability of law, jurisdiction and currency are essential boundaries. The source locator is relevant to legal research, but the Evidence Use record does not identify specific support for jurisdiction or currency checks. This claim should remain a strong boundary rule and be developed with jurisdiction-specific examples in later practical guidance. |
| `CLM-LEGAL_RESEARCH_BASICS-C` | 2 | 1 | 3 | Distinguishing primary legal authority from secondary research aids is a useful method principle. The generic Evidence Use description does not show where the source establishes this distinction. The claim is not itself a taxonomy: a usable guide should define the source hierarchy for the jurisdiction and legal issue at hand, because what counts as binding authority varies by system. |

## Findings
1. **Confirmed generic Evidence Use debt:** all three Claims use the same generic source description, preventing a reviewer from seeing the specific support for the separate propositions.
2. **Strong jurisdiction boundary:** the claim about applicable law and jurisdiction is conceptually important; a general Cornell LII resource must not be presented as a universal account of every legal system.
3. **Operational usability gap:** the slice gives good principles but not a reproducible workflow for identifying governing law, checking current versions, tracing citations, distinguishing binding from persuasive authority, and recording unresolved uncertainty.
4. No content Records were changed. These three Claims remain within the frozen 1,494-Claim denominator. This batch does not close legal research, legal-information safety, high-consequence review, or M13.

## Records inspected
- `CONTENT/vertical-slices/legal-research-basics/records/CLM-LEGAL_RESEARCH_BASICS-A.json`
- `CONTENT/vertical-slices/legal-research-basics/records/CLM-LEGAL_RESEARCH_BASICS-B.json`
- `CONTENT/vertical-slices/legal-research-basics/records/CLM-LEGAL_RESEARCH_BASICS-C.json`
- `CONTENT/vertical-slices/legal-research-basics/records/EU-LEGAL_RESEARCH_BASICS-A.json`
- `CONTENT/vertical-slices/legal-research-basics/records/EU-LEGAL_RESEARCH_BASICS-B.json`
- `CONTENT/vertical-slices/legal-research-basics/records/EU-LEGAL_RESEARCH_BASICS-C.json`

## Source
- Cornell Legal Information Institute, “Legal research”: https://www.law.cornell.edu/wex/legal_research

## Acceptance status
Three additional Claim rows have explicit D/E/B scores and rationales. Follow-up actions: make Evidence Use descriptions claim-specific and add a jurisdiction-sensitive legal-research workflow during a separately authorized correction/usability pass. Full 1,494-Claim scoring, high-consequence recall, Human View, Relation endpoint review, independent scoring review, authorized corrections with regression tests, and final same-HEAD 3/3 CI remain open.
