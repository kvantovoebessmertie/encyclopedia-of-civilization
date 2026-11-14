# M13 Batch 13 — source-fit triage (rows 639–642): health-system resilience and HTA

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional assessment of four Claims; row 639 has a critical Evidence Use claim-reference mismatch and must remain HOLD**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores below are provisional triage estimates, not finalized ledger scores. Canonical JSON remains unchanged.

## 1. Row 639 — `CLM-M4-HEALTH-RESILIENCE-A` — provisional **D2 / E1 / B2 — HOLD**

**Claim:** “Устойчивость системы здравоохранения включает способность поддерживать основные медицинские услуги при нарушениях и адаптироваться к контексту.”

Source record `SRC-M4-HEALTH-RESILIENCE-WHO@1` identifies WHO *Health systems resilience toolkit*:
https://www.who.int/publications/i/item/9789240048751

The source is topically appropriate for continuity and adaptation during disruptions. However, the fetched Evidence Use record `EU-M4-HEALTH-RESILIENCE-WHO` points to **`CLM_HEALTH_SYSTEMS_BASICS_C@1`**, not `CLM-M4-HEALTH-RESILIENCE-A@1`. This is a material reference-chain mismatch: the evidence record does not link to the resilience Claim it is supposed to support (E1). The claim is broad and does not identify which essential services, disruption scenarios, or resilience capacities are meant (D2). Its general boundary is reasonable but should not imply all services can always be maintained under every disruption (B2).

**Disposition:** HOLD. Correct the Evidence Use claim reference through the project's authorized canonical-data remediation process; verify identity aliases, pinpoint the toolkit's relevant section, and rerun reference/conformance tests. Do not edit canonical JSON in this triage note.

## 2. Rows 640–642 — health technology assessment

Canonical source: `SRC-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS@1`, WHO *Health technology assessment*:
https://www.who.int/health-topics/health-technology-assessment

Direct public-source passages:
- WHO defines HTA as a systematic, multidisciplinary evaluation of the properties, effects and impacts of health technologies and interventions, covering direct and indirect consequences.
- The WHO Q&A describes clinical, social, economic, organizational and ethical dimensions, and says HTA informs policy decisions, particularly allocation of limited funds.
- The current Evidence Use records contain only generic summaries, without section/paragraph pinpoints.

### 2a. `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A` — provisional **D2 / E3 / B2**

**Claim:** “Health technology assessment is a systematic and multidisciplinary evaluation of health technologies and interventions.”

**Assessment:** A concise definition without detail on assessment methods or evidence dimensions (D2). It closely matches WHO's direct definition, so fit is strong (E3). Preserve the point that HTA assesses technologies/interventions for decision-making; it is not simply a clinical trial or regulatory authorization (B2).

**Disposition:** Retain provisionally. Pinpoint the WHO HTA overview definition.

### 2b. `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B` — provisional **D2 / E3 / B2**

**Claim:** “HTA can consider clinical, economic, organizational, ethical and social consequences.”

**Assessment:** The list identifies important dimensions but does not explain methods or how trade-offs are appraised (D2). WHO directly identifies clinical, social, economic, organizational and ethical issues, so fit is strong (E3). “Can consider” is appropriately bounded: the dimensions examined depend on the technology, decision question and HTA framework (B2).

**Disposition:** Retain provisionally. Pinpoint WHO's multidisciplinary-process description; keep the conditional wording.

### 2c. `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C` — provisional **D2 / E3 / B2**

**Claim:** “HTA informs health-system policy decisions and is not individualized medical advice.”

**Assessment:** The Claim states the decision level but does not describe how assessments translate into recommendations or coverage decisions (D2). WHO explicitly says HTA informs policy decision-making, especially allocation of limited health funds. The policy-level scope supports the first clause, and the distinction from individualized medical advice is consistent with that role, though the latter clause is a boundary statement rather than a verbatim WHO definition (E3). Preserve the distinction between evidence informing policy and an individual's clinician making a care decision (B2).

**Disposition:** Retain provisionally. Pinpoint the WHO HTA overview/Q&A and mark the medical-advice clause as an editorial scope clarification.

## Batch accounting

- Individual Claims reviewed in this note: **4**.
- New provisional D/E/B assessments recorded: **4**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/4**.
- Critical linkage defect identified: **1** (row 639 Evidence Use points to a different Claim).
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
