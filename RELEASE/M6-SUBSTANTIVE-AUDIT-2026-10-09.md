# M6 Substantive Audit — 2026-10-09

## Status
**SUBSTANTIVE AUDIT RECORDED — M6 NOT CLEAN.** This is a claim-by-claim screening audit of the six scope-locked candidates. It does not authorize edits by itself. M4 and M5 remain closed; `main` is unchanged.

## Method
Read the three Claims, Source, three Evidence Use records, Context, and Scope for each candidate at the M6 branch HEAD. Checked the listed source pages where accessible. Findings distinguish direct support, partial/uncertain support, and presentation defects. This is not yet the independent evidence-diversity, Human View/adversarial, or complete Relation endpoint audit.

## Claim-level findings

| Slice / Claim | Finding | Disposition |
|---|---|---|
| `sleep-basics` A | NHLBI page directly describes predictable cycles of sleep stages. | No substantive defect confirmed. |
| `sleep-basics` B | NHLBI page directly describes approximately 24-hour internal clocks regulated by light and darkness. | No substantive defect confirmed. |
| `sleep-basics` C | NHLBI page directly states that insufficient/poor-quality sleep affects health and ability to think clearly and focus. The current wording is broad but appropriately says “may”. | No substantive defect confirmed; evidence-independence review remains due to health relevance. |
| `learning-basics` A | NIMH source explicitly names working memory, encoding, consolidation, and retrieval. | Direct support. |
| `learning-basics` B | NIMH source explicitly discusses interacting neural systems. | Direct support. |
| `learning-basics` C | The source discusses research questions, experimental systems, individual differences, and rigorous study design, but the exact generalization “findings depend on task, population and experimental design” is not stated as a clear, direct proposition on the source page. | **Confirmed traceability gap (M6-SUB-01):** narrow the wording to what the source states or add a suitable methods/research source. Do not convert this into a universal learning prescription. |
| `law-basics` A | Cornell LII/Wex defines jurisdiction as court power and/or territory within which legal power is exercised. | Direct support. |
| `law-basics` B | Cornell LII/Wex discusses personal, subject-matter, and territorial jurisdiction. | Direct support, with wording kept at a general explanatory level. |
| `law-basics` C | “Legal rules and procedures are jurisdiction-specific” is broader than the cited jurisdiction definition alone. Context correctly identifies the source as a US-law teaching example and requires applicable jurisdiction/date for real questions. | **Confirmed traceability gap (M6-SUB-02):** add an authoritative source or narrow the claim to the jurisdiction-specific nature of the jurisdiction examples actually discussed. Preserve the US-law boundary. |
| `demography-basics` A | World Population Prospects is an appropriate source family for population change components; the source record alone does not identify a passage supporting all three components. | Provisional support; record precise source fit during evidence audit. |
| `demography-basics` B | Age structure and population momentum are relevant to demographic projection, but the single source record does not identify the supporting passage. | Provisional support; verify against the report's methods/concepts before accepting. |
| `demography-basics` C | The report is explicitly projection-oriented; estimates/projections and assumptions need careful separation. Current claim is plausible but not tied to a specific source passage. | Provisional support; add traceable source material if retained. |
| `governance-basics` A | OECD framework is relevant to public governance, but the current generic definition is not tied to a precise source passage. | Provisional support; improve source traceability. |
| `governance-basics` B | The OECD framework explicitly organizes sound public governance around interconnected components; current wording is a reasonable summary. | Provisional support; retain as an attributed OECD framework rather than a universal taxonomy. |
| `governance-basics` C | Variation by institutional and national context is a broad comparative claim not demonstrated by the single framework locator alone. | **Confirmed traceability gap (M6-SUB-03):** add comparative support or narrow the statement. Keep the slice descriptive and non-ranking. |
| `education-systems` A | UNESCO page directly frames education as a human right. | Direct support. “Lifelong learning” must remain within the exact UNESCO framing and not imply every specific service is an identical legal entitlement. |
| `education-systems` B | UNESCO’s right-to-education material describes state obligations and the 4-A framework. | Direct support, subject to jurisdiction and applicable legal framework. |
| `education-systems` C | The UNESCO right-to-education page is not, by itself, a sufficiently specific source for the comparative claim that systems differ in financing, governance, curriculum, and delivery. | **Confirmed source-fit gap (M6-SUB-04):** add an education-systems comparative source or narrow the claim to what UNESCO actually documents. Preserve country/period boundaries. |

## Cross-cutting observations
1. All six slices have three claim-linked Evidence Use records, but the descriptions are formulaic and do not identify passages, sections, data tables, or the exact inferential role. Claim-to-source linkage exists; material support is not thereby proven.
2. Each slice currently has one Source for all three Claims. This is a verified lack of source diversity, not an automatic defect in every Claim. The next evidence-independence pass must decide per Claim whether independent corroboration is materially necessary and record a rationale either way.
3. `demography-basics` Context mixes Russian and English (“projections are not observations”). This is a confirmed Human View consistency defect to correct in the controlled correction pass.
4. All six Context and Scope records target Claim A only. This may be a valid slice-level anchor under the current schema; do not duplicate records mechanically. Human View audit must determine whether readers can discover the scope/limits for Claims B and C.
5. The filename scan found no Relation records inside the six candidate directories. This is not proof that no other slice points to these Claims. Full corpus-wide endpoint and duplicate audit remains outstanding.

## Confirmed debt register for M6
- **M6-SUB-01 — learning-basics / Claim C:** source traceability is too indirect.
- **M6-SUB-02 — law-basics / Claim C:** jurisdiction-specific generalization exceeds the locator’s directly visible proposition.
- **M6-SUB-03 — governance-basics / Claim C:** comparative variation claim lacks precise support in the single locator.
- **M6-SUB-04 — education-systems / Claim C:** cited right-to-education page does not adequately support the broad comparative systems claim on its own.
- **M6-HV-01 — demography-basics Context:** mixed-language presentation.

These are confirmed traceability/source-fit debts, not proof that the claims are false. No other claim is marked defective solely because its slice has one Source.

## Next required stages
1. Per-Claim evidence independence/diversity audit and precise support mapping.
2. Human View/adversarial audit, including scope visibility and language consistency.
3. Corpus-wide Relation endpoint, justification, and duplicate audit.
4. Merge only confirmed findings into one Unified M6 Debt Map.
5. Controlled correction pass; then post-correction audit.
6. Synchronize registry/coverage/regressions as required by actual changes.
7. Run Reference tests, Release Conformance Gate, and Offline Edition on the exact same HEAD; CLEAN only after 3/3 green and independent verification.

No mass rewrite, quota-driven expansion, new Record type, speculative Relation, or weakened validation is authorized.
