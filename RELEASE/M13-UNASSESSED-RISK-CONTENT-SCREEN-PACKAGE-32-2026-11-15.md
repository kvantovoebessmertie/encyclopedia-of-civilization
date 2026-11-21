# M13 — Unassessed Risk Content Screen — Package 32

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Queue source revision: `8cf14e5045f7451ff577b33590f42a582f5f8bcd`
Queue workflow run: `43748097802`
Queue artifact: `14175530692` (`m13-review-queue-8cf14e5045f7451ff577b33590f42a582f5f8bcd`)
Artifact digest: `sha256:73ea3a03fa40cd86e0062b10dfa4f978b1b424f0db8e7c98447666fe39ba9cd6`
State: **content-level risk routing only; no canonical edits, no risk metadata assignment, no D/E/B scoring**

## 1. Queue integrity

- 4,851 records scanned; 1,494 Claims inventoried.
- 1,501 scored-report rows reconciled; zero Claims without a scored-report match.
- 751 Claims have no recorded risk-domain or machine-triage signal.
- 708 previously screened Claim IDs excluded.
- 17 unreconciled holdout Claims excluded; 15 overlap with reviewed holdouts; 710 unique exclusions.
- 41 candidates selected; 41 unique Claim IDs; 59 slots unfilled in the requested 100-Claim batch.
- Lane counts: Lane 1 = 20; Lane 2 = 20; Lane 3 = 1; Lanes 4–5 = 0.
- All selected Claims remain `UNASSESSED`, with empty `risk_domains` and `machine_triage_flags`, and `NOT_YET_REVIEWED`.
- Evidence packets contain 41 local Claim/Evidence Use/Source bundles. The queue generator did not fetch external source text, assign scores or modify canonical records.

Absence of risk metadata is not evidence of low risk. This is a qualitative routing screen, not a determination of likelihood, severity, exposure, jurisdiction, operational risk or publication suitability.

## 2. Screening method

Each Claim was screened at statement level for direct instructions or thresholds, proximity to health/clinical, laboratory, engineering, cybersecurity, legal/governance, environmental or consequential research decisions, whether it is descriptive or prescriptive, and whether prior source-passage work can be reused. Routes are work priorities only:
- **Elevated:** specialist review before clinical, laboratory, research or other consequential application.
- **Moderate:** contextual/domain review before operational or policy use.
- **Low direct consequence:** foundational/descriptive proposition without a direct action instruction in the wording reviewed.

No Claim is designated safe or finally low risk. No formal risk-domain metadata or D/E/B scores are assigned.

## 3. Results — 41 Claims

### Elevated — 7

| Claim | Topic and routing boundary |
|---|---|
| `CLM-ACID_BASE_BASICS-B` | pH and hydrogen-ion activity; chemistry/metrology review before laboratory or clinical interpretation; no clinical thresholds or universal concentration equivalence. |
| `CLM_PHYSIOLOGY_OF_SYSTEMS_BASICS_A` | Physiology and structure/function; physiology review before clinical or individualized advice. |
| `CLM_PHYSIOLOGY_OF_SYSTEMS_BASICS_B` | Organ-system regulation and feedback; no diagnostic or treatment inference. |
| `CLM_PHYSIOLOGY_OF_SYSTEMS_BASICS_C` | Interpretation of physiological indicators; clinical laboratory review; no individual result classification. |
| `CLM-PHYSIOLOGY_BASICS-B` | Homeostasis; physiology review before individual clinical application; no diagnostic thresholds. |
| `CLM-PHYSIOLOGY_BASICS-C` | Organ-system interaction; do not infer symptom causes, dysfunction or treatment needs. |
| `CLM-STATISTICS_BASICS-C` | Experimental design and causal inference; statistical-methodology review; randomization alone does not prove causality or eliminate bias, attrition, measurement error or external-validity limits. |

### Moderate — 17

| Claim | Topic and routing boundary |
|---|---|
| `CLM-CRITICAL_THINKING_BASICS-A` | Critical-thinking process; preserve domain expertise and verifiable evidence. |
| `CLM-CRITICAL_THINKING_BASICS-B` | Claims, opinions, assumptions and bias; identifying possible bias does not automatically invalidate a claim. |
| `CLM-CRITICAL_THINKING_BASICS-C` | Revising conclusions; distinguish new evidence from preference changes; document high-stakes review. |
| `CLM-COMPUTING_BASICS-A` | Computer systems; not a cybersecurity, reliability or safety-assurance specification. |
| `CLM-COMPUTING_BASICS-B` | Algorithms; a defined sequence is not proof of correctness, fairness, security or safety. |
| `CLM-COMPUTING_BASICS-C` | Digital representation; do not infer data integrity/security or universal coverage of computing models. |
| `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B` | Parliamentary systems; comparative concept, not country-specific legal advice. |
| `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C` | Semi-presidential systems; executive authority varies; require jurisdiction-specific constitutional sources. |
| `CLM-ECOSYSTEMS_BASICS-A` | Ecosystem definition; local ecological evidence before environmental intervention or land management. |
| `CLM-ECOSYSTEMS_BASICS-B` | Energy flow and matter cycles; no quantitative rates, thresholds or prescriptions inferred. |
| `CLM-ECOSYSTEMS_BASICS-C` | Ecosystem scale/environment; preserve context-specific definitions and avoid universal typologies. |
| `CLM-POLITICAL_SCIENCE_BASICS-B` | Empirical political inquiry; transparent methods, representative data and jurisdiction/time context; observation is not causation. |
| `CLM-POLITICAL_SCIENCE_BASICS-C` | Descriptive vs normative analysis; empirical findings do not alone determine normative choices or legal obligations. |
| `CLM-PROBABILITY_BASICS-MODEL` | Probability models; preserve assumptions and outcome space; probabilities are not guarantees. |
| `CLM-RATIOS_AND_PERCENTAGES-CONTEXT` | Ratios and percentages; state comparison base, units, denominator and reference population. |
| `CLM_SCIENTIFIC_METHOD_BASICS_D` | Scientific process; general model, not a rigid universal protocol. |
| `CLM-PHYSICAL_CHEMISTRY_BASICS-B` | Thermodynamic quantities vs process rate; specialist review before process design or safety decisions. |

### Low direct consequence — 17

| Claim | Topic and routing boundary |
|---|---|
| `CLM-CELL_BASICS-A` | Cell as structural/functional unit; foundational biology. OpenStax AI-ingestion rights hold remains separate. |
| `CLM-CELL_BASICS-B` | Prokaryotic vs eukaryotic cells; do not infer other properties from nucleus presence/absence. |
| `CLM-ENERGY_BASICS-A` | Kinetic energy; introductory physics only, no equipment sizing/safety advice. |
| `CLM-ENERGY_BASICS-B` | Potential energy; preserve position/configuration context; no storage-system design advice. |
| `CLM-ENERGY_BASICS-C` | Work as energy transfer; no machinery or occupational instruction. |
| `CLM-MECHANICS_BASICS-A` | Newton's first law; retain inertial-frame and zero-resultant-force conditions. |
| `CLM-MECHANICS_BASICS-B` | Newton's second law; retain constant-mass/classical-case boundary. |
| `CLM-MECHANICS_BASICS-C` | Newton's third law; force pair acts on different bodies; no structural calculation follows. |
| `CLM-MOTION_BASICS-B` | Average vector velocity; corrected Claim/EU version 2; do not repeat source search. |
| `CLM-OPTICS_BASICS-B` | Geometrical optics; retain regime boundary where wave effects are not dominant. |
| `CLM-OPTICS_BASICS-C` | Image formation by lenses/mirrors; no eye-care, laser-safety or device-design procedure. |
| `CLM-QUANTUM_PHYSICS_BASICS-A` | Quantum-mechanical domain; retain scale/model boundary. |
| `CLM-QUANTUM_PHYSICS_BASICS-B` | Quantum measurement; avoid overgeneralizing interpretations beyond the model/observable. |
| `CLM-QUANTUM_PHYSICS_BASICS-C` | Atomic structure/interactions; no radiation or device safety instruction. |
| `CLM-THERMODYNAMICS_BASICS-A` | Thermodynamics scope; no operating limits or process design guidance. |
| `CLM-THERMODYNAMICS_BASICS-B` | First law; specify system boundaries and sign conventions in calculations. |
| `CLM-THERMODYNAMICS_BASICS-C` | Second law and entropy; no process-specific efficiency or operating constraints inferred. |

## 4. Prior evidence review reused

Ten selected Claims have existing source-passage reviews or dedicated locator corrections. Their findings are reused, not re-searched:
- Cell A/B — Strict Passage Locator Review Package 05; OpenStax EU v2; AI-ingestion rights hold remains.
- Computing A — Batch 44 Lane 01; OpenStax EU v2.
- Computing B/C — Batch 44 Lane 02; OpenStax EU v2.
- Constitutional Systems B/C — Batch 44 Lane 02; OpenStax EU v2.
- Motion B — Batch 44 Lane 04 and average-velocity correction checkpoint; Claim and EU v2.

Prior evidence review is not completion of this risk screen. Existing HOLD, source-scope, rights and independent-review gates remain. `CLM-MATTER_BASICS-A` was in the earlier 42-Claim queue but is absent from this exact 41-Claim selection; do not carry it into Package 32.

## 5. Integrity and disposition

- Claims routed: 41/41 (7 elevated, 17 moderate, 17 low direct consequence).
- Risk metadata assigned: 0.
- D/E/B scores assigned: 0.
- External source text fetched by automation: 0.
- Specialist adjudications completed: 0.
- Canonical Claim/Evidence Use/Source records modified: 0.
- Claims accepted, release-cleared or Human View approved: 0.

This package closes only the statement-level routing pass for the exact 41-Claim queue. Every selected Claim remains UNASSESSED/HOLD pending exact source-passage verification, applicable specialist review, independent adjudication, Human View and release gates. The labels are not final risk ratings.

M13 remains **OPEN / NOT RELEASE-READY**. PR #21 remains Draft/unmerged; `main` remains unchanged.
