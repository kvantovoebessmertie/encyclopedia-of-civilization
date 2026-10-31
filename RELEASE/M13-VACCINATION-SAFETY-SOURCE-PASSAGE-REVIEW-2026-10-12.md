# M13 Vaccine-Safety Claim Source-Passage Review — 2026-10-12

## Scope and method

Reviewed the current versioned Claim → Evidence Use → Source chain for the vaccination-information-basics slice against the current WHO page “Vaccines and immunization: Vaccine safety” (23 September 2025).

- Claims reviewed: `CLM-VACCINATION_INFORMATION_BASICS-A` v1, `-B` v1, and `-C` v1.
- Evidence Use reviewed: `EU-VACCINATION_INFORMATION_BASICS-A` v1, `-B` v1, and `-C` v1.
- Source reviewed: `SRC-VACCINATION_INFORMATION_BASICS` v1.
- Source URI: https://www.who.int/news-room/questions-and-answers/item/vaccines-and-immunization-vaccine-safety
- Current page date: 23 September 2025.
- This is passage-level source review, not a final D/E/B score, independent corroboration assessment, or release approval.

## Claim-by-claim findings

### `CLM-VACCINATION_INFORMATION_BASICS-A` v1

**Statement:** “Безопасность вакцин оценивается до внедрения через последовательные этапы испытаний и оценку результатов.”

**Relevant WHO passage locators:**
- Heading: “How do we know that a vaccine is safe?”
- Heading: “How are vaccines tested?”
- Heading: “How are vaccines approved for public use?”
- Under “How are vaccines tested?”, the page describes laboratory testing followed by clinical-trial phases I, II, and III, and says study results are assessed by regulators when deciding whether to approve a vaccine.

**Finding:** Directly supported at the stated general level. “До внедрения” should be understood as before authorization/introduction for use; the claim should not imply that pre-introduction trials can identify every rare or delayed adverse event. WHO separately describes additional studies and continued monitoring after introduction.

**Disposition:** Passage support found; retain HOLD for public-pilot clearance until the Evidence Use record has a reproducible locator and independent Human View is complete.

### `CLM-VACCINATION_INFORMATION_BASICS-B` v1

**Statement:** “После внедрения вакцины продолжают находиться под мониторингом безопасности со стороны органов здравоохранения и специалистов.”

**Relevant WHO passage locators:**
- Heading: “How do we know that a vaccine is safe?”
- Heading: “How is vaccine safety monitored?”
- Under “How is vaccine safety monitored?”, WHO states that safety monitoring continues after clinical trials and introduction for public use, and describes monitoring at local, national, regional, and global levels.
- The page describes national authorities, WHO, vaccine manufacturers, national advisory committees, and independent experts as participants in monitoring/review.

**Finding:** Directly supported. The statement is appropriately general and does not claim that monitoring guarantees detection of every adverse event or establishes causality from a report alone.

**Disposition:** Passage support found; retain HOLD for public-pilot clearance until the Evidence Use record has a reproducible locator and independent Human View is complete.

### `CLM-VACCINATION_INFORMATION_BASICS-C` v1

**Statement:** “Информация о безопасности и эффективности вакцинации должна интерпретироваться в контексте конкретной вакцины, популяции и доступных данных.”

**Relevant WHO passage locators:**
- Heading: “How are vaccines tested?” — the page describes trial phases and the intended recipient group for Phase II.
- Heading: “How are vaccines approved for public use?” — the page describes national/regional regulators and national decisions on introduction.
- Heading: “How is vaccine safety monitored?” — the page distinguishes monitoring levels and describes assessment of possible safety concerns.
- The page discusses the need for additional studies after introduction and assessment of safety/efficacy evidence over a longer timeframe.

**Finding:** Reasonable synthesis of the page’s context-dependent discussion, but the current WHO page does not appear to state the exact general principle in the Claim’s wording as one directly quotable sentence. This is a broader interpretive claim than A or B. A single general Q&A page is not enough to characterize it as independently corroborated.

**Disposition:** HOLD. Either narrow the Claim to a directly evidenced proposition or add suitable authoritative sources with claim-specific locators; do not treat the present generic Evidence Use description as sufficient proof of the full statement.

## Evidence Use and source-chain findings

All three Evidence Use v1 records use the same generic description: the WHO page is used “без расширения за пределы указанного материала.” None records a specific heading, subsection, paragraph, or excerpt. The source identity and URI are coherent, but the current Evidence Use records are not reproducible enough for independent review.

- One source linked to three Evidence Use records is not three independent sources.
- The WHO page is current enough for this review and dated 23 September 2025; this review does not establish ongoing future currentness.
- No unsupported inference should be added that safety monitoring guarantees zero risk or that an adverse event after vaccination necessarily was caused by a vaccine.
- Rights/attribution and Human View remain separate release gates.

## Required follow-up

1. Make a bounded, versioned correction to each Evidence Use record only after confirming the repository’s applicable correction-authorization requirements. Record the exact WHO heading and the passage-level locator; retain record history.
2. For Claim C, decide whether to narrow the proposition to the exact supported scope or supplement the evidence chain with appropriate authoritative references.
3. Have an independent reviewer verify the passage-to-Claim mapping and assess the medical-information boundary before any public pilot.
4. Reconcile any later score against the current scored-report ledger; this report itself adds no score.

## Controls

- No canonical JSON was changed by this review.
- No D/E/B score was assigned, altered, or inferred.
- No public allowlist or publication decision was changed.
- M13 remains open.
