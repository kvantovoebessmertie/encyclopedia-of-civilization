# M13 Batch 53 — high-consequence source-passage review and D/E/B scoring block

Date: 2026-11-12
Branch: m13-system-wide-depth-audit-2026-10-09
Queue source revision: 33ef97e7ba6a9e91aebaee198cfead532faa4185
Scope: 13 high-consequence Claims from lanes 04 and 05. This is a scored sub-block, not completion of Batch 53.

## 1. Method

Exact Claim statements and linked Evidence Use and Source records were inspected. Official source passages were checked. Scores follow the locked M13 rubric: D explanatory depth; E claim-specific evidence fit; B boundary and epistemic discipline.

All 13 Evidence Use records inspected here contain generic descriptions without reproducible Claim-specific page/section/table/figure locators. Thus E=1 throughout, even where official source text directly supports the Claim. This is a corpus Evidence Use defect, not a judgement that the source institution is unreliable.

## 2. Source-passage findings

### Privacy and data protection — 2 Claims

The European Commission's official GDPR principles page lists accuracy, integrity and confidentiality, purpose limitation, data minimisation, storage limitation and accountability, and explicitly references GDPR Article 5 and Recital 39. It explains that data must be adequate, relevant and limited to what is necessary for the purpose, stored no longer than necessary, secured with appropriate technical and organisational measures, and that organisations must demonstrate compliance.

- Claim B is directly supported by the listed principles. It is explicitly scoped to GDPR, but the canonical Evidence Use lacks an Article 5 locator.
- Claim D is substantially supported by purpose limitation, data minimisation, storage limitation, integrity/confidentiality and accountability. The wording should not be treated as an exhaustive statement of all GDPR duties.
- Territorial/material scope must remain explicit: the Commission page describes organisations based in the EU or processing personal data of individuals in the EU. This is not universal privacy law.

### Public procurement — 2 Claims

The World Bank Procurement Framework page says mandatory Policy, Directive, Procedure and Regulations govern procurement of goods, works, non-consulting services and consulting services for Investment Project Financing operations, with flexibility for borrowers to design a market approach considering specific risks and opportunities.

- Claims A and B are supported only within the World Bank IPF framework.
- The canonical Claims are phrased generically as “procurement” and “project”; the linked source does not establish a universal definition or universal adaptation rule across jurisdictions.
- Keep HOLD until the scope is narrowed or independent jurisdictionally relevant sources are added. Do not imply that World Bank IPF rules apply to all public procurement.

### Reliability — 3 Claims

NIST/SEMATECH e-Handbook, Assessing Product Reliability:
- §8.1.2.2 defines reliability/survival function as the probability that a unit survives beyond time t.
- §8.1.2.3 defines failure/hazard rate as an instantaneous conditional failure rate among survivors.
- §8.1.3.1 explains censoring: at test end, some units may not have failed; it separately identifies the problem of a lack of failures and notes that heavy censoring limits information.
- §8.4.1 discusses graphical and maximum-likelihood methods for estimating life-distribution parameters from censored data.

These passages support Claims B and C. Claim A's definition needs a direct definition locator from the handbook's basic terms section, and the source is a statistical reliability handbook rather than a universal quality-management standard. The canonical EU records have no locators; all three remain HOLD. The warning that no observed failure does not prove no risk is a sound boundary and directly consistent with NIST's discussion of censoring and lack of failures.

### Safety engineering — 3 Claims

FAA Safety Risk Management Guidance for System Acquisitions (October 2022), Appendix C:
- §3.2.1.5 classifies operational hazards by severity and considers worst credible outcomes.
- §3.2.1.6 develops safety objectives and requirements from hazard classifications and explains that requirements establish hazard controls as product requirements.
- §3.2.1.7 documents hazards and associated objectives/requirements.
- §3.3 allocates safety objectives and requirements to system elements and responsible stakeholders, including procedural and architectural mitigations.
- The document is explicitly an FAA system-acquisition / air-traffic-operations guidance, not a universal safety-engineering code.

Claim B is directly supported in this specific system-acquisition context. Claim C's context dependence is supported by the document's repeated attention to system boundaries, operational environment, interfaces, architecture and requirements. Claim A is not fully established by these passages: FAA guidance treats safety risk management as an integrated process within system acquisition, but does not alone establish the broader disciplinary classification as worded. NASA's systems-engineering handbook may supply adjacent context, but not a precise safety-engineering taxonomy. All three remain HOLD; require exact FAA locators and a source directly defining the field for Claim A.

### Risk analysis — 3 Claims

NIST SP 800-30 Rev. 1 states that it provides guidance for preparing, conducting and maintaining risk assessments and explains how risk assessments inform other organizational risk-management processes. ISO/IEC 31010:2019's official catalogue description says it guides selection and application of risk-assessment techniques in many situations, to support decisions under uncertainty and inform risk management.

- Claim A is only partially supported by NIST's broad description; the full list of objective, scope, assumptions, limitations and information sources needs a specific passage from the guide.
- Claim B's decision-support purpose is supported by NIST and IEC. The warning against false precision is methodologically appropriate, but requires a passage explicitly addressing uncertainty/limitations to be fully evidenced.
- Claim C's maintain/update aspect is supported by NIST's stated prepare-conduct-maintain structure; the specific triggers (changed conditions, information or context) need direct section-level support.
- The canonical EU records have no locators. ISO's full standard is not freely available through the catalogue page. All three remain HOLD.

## 3. D/E/B score table

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| CLM-PRIVACY_AND_DATA_PROTECTION_BASICS-B | 1 | 1 | 2 | Concise list of GDPR principles; context is explicitly GDPR, but the Claim has little explanation of their operation. |
| CLM-PRIVACY_AND_DATA_PROTECTION_BASICS-D | 2 | 1 | 2 | Connects purpose, data minimisation, retention, security and accountability; GDPR scope is explicit but the statement is not exhaustive. |
| CLM-PUBLIC_PROCUREMENT_BASICS-A | 1 | 1 | 1 | Basic definition; linked source is limited to World Bank IPF, not all procurement systems. |
| CLM-PUBLIC_PROCUREMENT_BASICS-B | 2 | 1 | 1 | Names rules, documents, roles and methods, but adaptation is only evidenced in the IPF framework and not bounded in the Claim. |
| CLM-RELIABILITY_BASICS-A | 2 | 1 | 2 | Definition includes function, conditions and time, and distinguishes reliability from quality; exact handbook definition locator still missing. |
| CLM-RELIABILITY_BASICS-B | 2 | 1 | 2 | Identifies lifetime models, survival and hazard functions and notes model dependence on conditions/data. |
| CLM-RELIABILITY_BASICS-C | 3 | 1 | 3 | Explains censoring and lack-of-failure limits and explicitly bounds inference by observation period/data quality. |
| CLM-SAFETY_ENGINEERING_BASICS-A | 1 | 1 | 1 | Broad disciplinary assertion; reviewed FAA source supports integrated safety management, not the precise taxonomy. |
| CLM-SAFETY_ENGINEERING_BASICS-B | 2 | 1 | 2 | Connects hazard analysis, safety objectives/requirements, design controls and allocation; source is FAA system-acquisition context. |
| CLM-SAFETY_ENGINEERING_BASICS-C | 2 | 1 | 3 | Explicitly bounds safety by context, architecture, operating conditions and applicable requirements. |
| CLM-RISK_ANALYSIS_BASICS-A | 2 | 1 | 2 | Identifies objective, scope, assumptions, limitations and information sources; NIST/IEC sources are relevant but precise passage chain incomplete. |
| CLM-RISK_ANALYSIS_BASICS-B | 2 | 1 | 3 | Clearly distinguishes decision support from false precision under uncertainty; NIST/IEC support purpose, but exact uncertainty passage still needed. |
| CLM-RISK_ANALYSIS_BASICS-C | 2 | 1 | 2 | Includes maintaining the assessment; NIST explicitly includes maintenance, but specific update triggers need pinpointing. |

## 4. Score summary and disposition

- Claims scored in this high-consequence sub-block: 13.
- D: score 1 = 3; score 2 = 9; score 3 = 1; mean = 1.85.
- E: score 0 = 0; score 1 = 13; score 2 = 0; score 3 = 0; mean = 1.00.
- B: score 1 = 3; score 2 = 6; score 3 = 4; score 0 = 0; mean = 2.08.
- Confirmed source-scope problems: both public-procurement Claims are overbroad relative to World Bank IPF source; safety-engineering Claim A lacks direct taxonomic support; risk Claims A/B/C need exact passages for specific components/triggers.
- No canonical Claim/Evidence Use/Source JSON changed.
- No Claim accepted or release-cleared.
- No specialist legal, procurement, reliability, safety-engineering or risk-methodology peer review completed.
- All 13 remain HOLD pending exact Evidence Use locators, source-scope resolution and specialist review.

## 5. Next actions

1. Add these 13 rows to the scored-report ledger and verify exact identifier reconciliation.
2. Continue the remaining 68 Claims in Batch 53; prioritize other high-consequence candidates from lanes 04 and 05.
3. Narrow or support procurement Claims with jurisdiction-appropriate evidence before any canonical correction.
4. Obtain direct source support for the safety-engineering taxonomy and risk-assessment details.
5. Keep all high-consequence Claims HOLD until expert review and Human View are separately completed.

## 6. Sources checked

- European Commission, Principles of the GDPR (Article 5 and Recital 39): https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
- World Bank Group, Project Procurement Framework: https://www.worldbank.org/ext/en/what-we-do/project-procurement/framework
- NIST/SEMATECH e-Handbook, Assessing Product Reliability, §§8.1.2.2, 8.1.2.3, 8.1.3.1 and 8.4.1: https://www.itl.nist.gov/div898/handbook/apr/apr.htm
- FAA, Safety Risk Management Guidance for System Acquisitions (October 2022), Appendix C §§3.2.1.5–3.3: https://www.faa.gov/air_traffic/publications/media/srmgsa.pdf
- NIST SP 800-30 Rev. 1, Guide for Conducting Risk Assessments: https://www.nist.gov/publications/guide-conducting-risk-assessments
- ISO/IEC 31010:2019, Risk management — Risk assessment techniques: https://www.iso.org/standard/72140.html
