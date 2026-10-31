# M13 Batch 41 — Evidence-Linkage Checkpoint 11 — 2026-10-11

## Scope and gate
Diagnostic review of Artificial Intelligence Basics Claims A–C. Verified Claim record types/internal IDs, Evidence Use links, stored Source identity/URI, and current NIST AI definitions/evaluation materials. No D/E/B scores assigned; no content records modified. Batch 41 remains open.

## Findings

### A — `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-A`
- Claim: “Системы искусственного интеллекта могут использовать модели и алгоритмы для обработки данных и получения результатов.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARTIFICIAL_INTELLIGENCE_BASICS-A` points to the intended Claim and `SRC-ARTIFICIAL_INTELLIGENCE_BASICS`; role `supports`.
- NIST's AI definition describes machine-based systems that make predictions, recommendations or decisions for human-defined objectives; its glossary definitions cover systems and techniques using learning, data and computation. This is compatible with the Claim's broad wording, but the linked high-level NIST AI page is a broad topic landing page and the exact phrase “models and algorithms to process data and obtain results” is a synthesis rather than a directly quoted definition.
- **Disposition:** partial-to-adequate source fit for a broad, qualified statement; evidence traceability is weak because the Evidence Use record gives no exact NIST definition or locator. Avoid implying every AI system necessarily uses a learned model or the same processing pipeline.

### B — `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-B`
- Claim: “Поведение системы зависит от данных, модели, целей и условий применения.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARTIFICIAL_INTELLIGENCE_BASICS-B` points to the intended Claim and Source; role `supports`.
- NIST's AI measurement and evaluation material explicitly states that how a component is measured/evaluated changes with the context in which the system operates. NIST's AI Risk Management Framework Playbook also describes AI as socio-technical, affected by data quality/representativeness, use, operators and social context. The current source landing page alone does not directly support every component (especially “goals” and “model”), but the official NIST measurement/evaluation material supports the context-dependent core.
- **Disposition:** partial source fit; current source record is too broad to show direct support for all four factors. A precise NIST source and locator would be required to mark the full synthesis as well supported.

### C — `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-C`
- Claim: “Оценка ИИ-системы должна учитывать контекст, ограничения данных и критерии качества.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARTIFICIAL_INTELLIGENCE_BASICS-C` points to the intended Claim and Source; role `supports`.
- NIST's AI Measurement and Evaluation page directly says context is crucial, evaluation characteristics require distinct measurement approaches, and datasets/metrics and technical limitations must be considered. The AI RMF Playbook further addresses data quality and representativeness and evaluation under conditions similar to deployment.
- **Disposition:** substantive source fit PASS for the main synthesis, though the stored broad NIST AI page is not a pinpoint and “quality criteria” could be specified more precisely as metrics/characteristics relevant to intended use.

## Structural and metadata observations
- All Claim IDs match filenames and all Claim → Evidence Use → Source pointers resolve correctly.
- All three Evidence Use descriptions are generic and do not cite a NIST definition, AI RMF function, page section or measurement criterion.
- Stored Source URI https://www.nist.gov/artificial-intelligence is a general NIST AI landing page. More directly relevant official sources consulted:
  - NIST, “AI measurement and evaluation”: https://www.nist.gov/ai-measurement-and-evaluation
  - NIST AI RMF Playbook, “Measure”: https://airc.nist.gov/airmf-resources/playbook/measure/
  - NIST CSRC AI glossary: https://csrc.nist.gov/glossary/term/AI
- No D/E/B scores assigned. No content JSON changed. Adding/replacing Source records or updating locators requires a separately authorized correction scope.

## Public sources consulted
- NIST, “Artificial Intelligence”: https://www.nist.gov/artificial-intelligence
- NIST, “AI measurement and evaluation”: https://www.nist.gov/ai-measurement-and-evaluation
- NIST AI RMF Playbook, “Measure”: https://airc.nist.gov/airmf-resources/playbook/measure/
- NIST CSRC, “AI” glossary: https://csrc.nist.gov/glossary/term/AI
