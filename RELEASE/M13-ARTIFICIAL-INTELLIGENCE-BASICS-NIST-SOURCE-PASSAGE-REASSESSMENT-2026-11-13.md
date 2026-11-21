# M13 — artificial intelligence basics: NIST source-passage reassessment

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Review class: follow-up source-passage reassessment; **not new first-pass Claim coverage**. The three Claims already received provisional scoring in Batch 41, scored block 04, rows 53–55. That review itself noted the broad NIST landing-page locator and the need for a direct AI RMF / technical source. This report adds passage-level source checks and does not create another D/E/B scoring row.

## 1. Exact records and prior-review reconciliation

| Claim | Evidence Use | Source | Version |
|---|---|---|---|
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-A` | `EU-ARTIFICIAL_INTELLIGENCE_BASICS-A` | `SRC-ARTIFICIAL_INTELLIGENCE_BASICS` | v1 / v1 / v1 |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-B` | `EU-ARTIFICIAL_INTELLIGENCE_BASICS-B` | `SRC-ARTIFICIAL_INTELLIGENCE_BASICS` | v1 / v1 / v1 |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-C` | `EU-ARTIFICIAL_INTELLIGENCE_BASICS-C` | `SRC-ARTIFICIAL_INTELLIGENCE_BASICS` | v1 / v1 / v1 |

The three Claim → EU → Source chains are internally consistent. The Source record's `source_identity` is a descriptive sentence rather than a bibliographic identity, and its URI (`https://www.nist.gov/artificial-intelligence`) is a broad topic landing page. Each EU uses a generic template and has no paragraph, section, figure or page locator. These are source-identity and evidence-locator defects, not broken reference chains.

Prior review: `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-04-ARCHITECTURE-ARCHIVES-ART-AI-ASSETS-ASTRONOMY-2026-10-11.md`, rows 53–55. That review gave provisional D/E/B values and narrative source-fit notes, but no canonical pinpoint was recorded. This reassessment must not be represented as a new Claim first-pass review or an independent specialist assessment.

## 2. Authoritative source passages examined

### NIST AI Risk Management Framework 1.0

Elham Tabassi, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023.  
Official PDF: https://doi.org/10.6028/NIST.AI.100-1  
Official NIST publication page: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10

Relevant passages:
- Executive Summary, printed p. 1: defines an AI system as an engineered or machine-based system that, for given objectives, generates outputs such as predictions, recommendations or decisions; describes data that can change over time and system/context complexity.
- Printed p. 1: explains that AI risks and benefits emerge from technical aspects together with societal factors, including how a system is used, its interactions, its operator and its social context.
- Printed pp. 7–8: discusses risk prioritization by context of use and the importance of sensitive datasets and downstream impacts.
- Printed p. 12, §3: identifies trustworthy-AI characteristics and says they must be balanced according to context of use; explains that trustworthiness is tied to datasets, model and algorithm selection, builder decisions, and human interaction/oversight.
- Printed pp. 13–14, §3.1: discusses validity, reliability, accuracy, robustness/generalizability and performance under varying circumstances.

### NIST CSRC glossary — artificial intelligence model

Official NIST CSRC glossary entry: https://csrc.nist.gov/glossary/term/artificial_intelligence_model

The entry defines an AI model as a component of an information system that implements AI technology and uses computational, statistical or machine-learning techniques to produce outputs from given inputs. The glossary identifies NIST SP 800-218A as the source document for that definition; the source document should be consulted before adopting the definition beyond the glossary-level summary.

### NIST CSRC glossary — artificial intelligence

Official NIST CSRC glossary entry: https://csrc.nist.gov/glossary/term/artificial_intelligence

The entry records multiple definitions from identified standards and publications, including a machine-based system that, for human-defined objectives, can make predictions, recommendations or decisions affecting real or virtual environments. Its multiple-source nature is important: do not treat the glossary page as one universal, exclusive definition.

## 3. Claim-by-claim reassessment

### Claim A — models/algorithms, data processing and outputs

Claim: “Системы искусственного интеллекта могут использовать модели и алгоритмы для обработки данных и получения результатов.”

**Assessment: DIRECT at the stated, non-exclusive level.**
- NIST AI RMF 1.0, Executive Summary, printed p. 1, defines an AI system by its ability to generate outputs for given objectives.
- NIST AI RMF 1.0, printed p. 12, §3, explicitly connects trustworthy-AI characteristics to datasets and the selection of AI models and algorithms.
- NIST CSRC's “artificial intelligence model” entry describes computational, statistical and machine-learning techniques producing outputs from inputs.

The Claim uses “могут использовать” and does not assert that every AI system has the same architecture. That qualification is appropriate. Editorial precision: “processing data” is an accessible summary of inputs/model techniques/outputs, not a verbatim NIST definition.

**Proposed locator:** NIST AI RMF 1.0, Executive Summary, printed p. 1; §3, printed p. 12; NIST CSRC Glossary, “artificial intelligence model” (definition and cited NIST SP 800-218A).

### Claim B — data, model, goals and conditions

Claim: “Поведение системы зависит от данных, модели, целей и условий применения.”

**Assessment: DIRECT as a synthesis of the framework, with one wording note.**
- Executive Summary, printed p. 1, ties system outputs to objectives, notes that training data may change and affect functionality/trustworthiness, and explains the influence of deployment context and use.
- Printed p. 12, §3, explicitly identifies datasets, model/algorithm selection, builder decisions and human interactions as interrelated influences on trustworthiness.
- Printed pp. 7–8 explain why risk prioritization and controls must reflect the specific context of use.

The four-factor list is a concise synthesis rather than a quoted NIST taxonomy. “Поведение” is broad; “функционирование и результаты” would be more precise and closer to the source language.

**Proposed locator:** NIST AI RMF 1.0, Executive Summary, printed p. 1; §§1.2.3–1.2.4, printed pp. 7–8; §3, printed p. 12.

### Claim C — context, data limitations and quality criteria

Claim: “Оценка ИИ-системы должна учитывать контекст, ограничения данных и критерии качества.”

**Assessment: DIRECT.**
- NIST AI RMF 1.0, printed p. 12, §3, lists trustworthiness characteristics and explicitly relates them to context of use, datasets, model/algorithm selection and human decisions.
- Printed pp. 13–14, §3.1, describes validity, reliability, accuracy and robustness/generalizability as relevant quality characteristics.
- Executive Summary, printed p. 1, notes that changing training data can affect functionality and trustworthiness and that deployment context affects risks and benefits.

This is a bounded statement about evaluation criteria, not a claim that NIST's framework is the only possible evaluation standard or that the listed characteristics exhaust all domain-specific quality requirements.

**Proposed locator:** NIST AI RMF 1.0, §3, printed p. 12; §3.1, printed pp. 13–14; Executive Summary, printed p. 1.

## 4. Source identity, scope and rights

The existing NIST topic landing page is not a sufficiently precise bibliographic source for the three propositions. Proposed remediation, subject to bounded authorization:
1. Add a bibliographic Source for Tabassi, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (January 2023), using the DOI/official PDF.
2. Add a distinct Source for the NIST CSRC “artificial intelligence model” glossary entry, retaining the entry URI and the cited underlying NIST SP 800-218A as the definition's source.
3. If the general “AI” glossary entry is retained, preserve its multiple-definition and source-attribution structure; do not flatten its several definitions into one.
4. Add exact locators to the three EUs and, if approved editorially, tighten Claim B's “поведение” to “функционирование и результаты”.

The AI RMF is available free of charge from NIST. Free access does not itself establish blanket permission for unrestricted reproduction or every downstream use. The NIST publication page and document rights/attribution terms, plus any third-party incorporated material, must be checked for the intended redistribution model. This report paraphrases and cites rather than reproduces substantial passages.

## 5. Disposition and integrity

| Measure | Result |
|---|---:|
| Claims re-assessed against pinpoint passages | 3 |
| Previously scored in Batch 41 | 3 |
| New first-pass Claim coverage | 0 |
| Direct support at stated scope | 3 |
| Canonical Source/EU/Claim JSON changed | 0 |
| Canonical pinpoint locators added | 0 |
| Historical D/E/B scores changed | 0 |
| New D/E/B scoring rows created | 0 |
| Independent specialist review completed | 0 |
| Rights clearance completed | 0 |
| Claims accepted or release-cleared | 0 |

All three remain HOLD pending bounded authorization for versioned Source/EU remediation, final editorial precision, rights/attribution verification, independent AI specialist review and Human View. This reassessment improves the desk-review record; it does not close M13 or approve publication.
