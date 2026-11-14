# M13 Batch 53 — Lane 04 content-based risk screen and source-fit precheck

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `33ef97e7ba6a9e91aebaee198cfead532faa4185`  
Scope: lane 04, 20 Claims. This is a content-based routing and source-fit precheck, not final D/E/B scoring, legal advice, independent peer review, Human View, or release clearance.

## 1. Method and boundary

All 20 exact Claim statements were inspected. Evidence Use and Source records were inspected for privacy, procurement, quality-control and reliability Claims. Official source pages and relevant handbook passages were checked. Risk categories route specialist review; they do not certify correctness. Evidence Use descriptions without a reproducible page/section locator do not earn full evidence precision.

## 2. Risk routing

| Claim IDs | Route | Reason / required review |
|---|---|---|
| `CLM-PRIVACY_AND_DATA_PROTECTION_BASICS-B/D` | HIGH CONSEQUENCE — legal/privacy | GDPR processing principles affect legal duties and individual rights. Require data-protection specialist/legal review; state territorial and material scope precisely. |
| `CLM-PUBLIC_PROCUREMENT_BASICS-A/B` | HIGH CONSEQUENCE — public finance/procurement | Procurement guidance may affect public spending, fairness and legal compliance. Require procurement/legal review and jurisdiction-specific scope. |
| `CLM-RELIABILITY_BASICS-A/B/C` | HIGH CONSEQUENCE — engineering reliability | Reliability models and censored data can influence engineering and safety decisions. Require reliability/statistical engineering review and assumptions disclosure. |
| `CLM-QUALITY_CONTROL_BASICS-A/B/C` | ELEVATED — process/industrial quality | Control limits, corrective actions and process acceptability can affect manufacturing and safety-critical processes. Require quality/statistical review; distinguish process stability from product acceptance. |
| `CLM-PUBLIC_DATA_BASICS-A/B/C` | MODERATE — statistics/data interpretation | Statistical definitions and data fitness affect downstream public decisions. Require statistical-method and provenance review. |
| `CLM-POLITICAL_ECONOMY_BASICS-B/C` | MODERATE — policy/social interpretation | Institutional and causal claims require contextual evidence and care not to universalize political mechanisms. |
| `CLM-PROJECT_MANAGEMENT_BASICS-B/C` | MODERATE — operational governance | General management claims can be misapplied as universal prescriptions; check source scope and context. |
| `CLM-QUEUEING_THEORY_BASICS-A/B/C` | LOW direct consequence / elevated when operationalized | Foundational mathematical model statements; real-world capacity and service decisions require assumptions, data and domain validation. |

## 3. Source-passage findings

### Privacy and data protection

- The European Commission's official GDPR principles page directly lists accuracy; integrity and confidentiality; purpose limitation; data minimisation; storage limitation; and accountability (page lines 42–49). It explicitly explains purpose (44), data minimisation (45), storage limitation (46), accuracy (47), integrity/confidentiality (48), and accountability (49).
- The European Data Protection Board's “Basic principles” page independently lists the same core principles and the accountability requirement (lines 8–9).
- This supports Claim B's core list. Claim D's specific set of purpose, necessary data volume, storage period, security, and demonstrable compliance is also directly reflected in the Commission page.
- Important scope: the Commission page states that these principles apply to organisations based in the EU or processing personal data of individuals in the EU (lines 33–35). The Claims must not be presented as a universal privacy law outside GDPR scope.
- The linked Evidence Use records do not store the exact Article 5/page pinpoints. Source identity and broad descriptions are relevant but not reproducible locators. Both Claims remain HOLD pending bounded pinpoint documentation and specialist legal review.

### Public procurement

- The World Bank Procurement Framework page says it governs projects financed by Investment Project Financing and covers procurement of goods, works, non-consulting services and consulting services, with mandatory requirements in policy, directive, procedure and regulations (lines 47–48, 60–62).
- This supports a description of the World Bank's own IPF procurement framework, not an unqualified general statement about all public procurement systems.
- The two Evidence Use records lack pinpointed clauses and do not identify a jurisdictional limitation in their descriptions. Claims A and B remain HOLD pending explicit IPF scope, exact policy/procedure references, and procurement/legal review.

### Quality control

- NIST/SEMATECH e-Handbook chapter 6 describes process/product monitoring and control techniques and signalling when corrective action is necessary (chapter overview, lines 2–5).
- Section 6.3.1 explains that control charts monitor quality characteristics over time and use centre and control-limit lines (lines 4–8). It also warns that limits depend on assumptions and distributions (lines 10–18).
- Section 6.1.5 explicitly distinguishes a statistically predictable process from one that is acceptable: a process can be in control but have an average or variability that is unacceptable (lines 4–13). This directly supports Claim C's distinction and is relevant to Claim B's control-limit concept.
- The source is relevant and has precise subpages available, but the Evidence Use records have no page/section locator. Claim A's “change the process” wording also needs careful qualification: the source describes investigation and corrective action, not indiscriminate adjustment after every signal. All three remain HOLD until pinpoints and scope are recorded.

### Reliability

- NIST/SEMATECH e-Handbook chapter 8 covers terms, models and techniques for evaluating and predicting product reliability, including lifetime distributions, repairable systems, censored data and reliability data analysis (chapter overview, lines 2–31).
- Section 8.3.1 says reliability-test planning begins with assumptions and the question to be answered; decisions depend on assumed models, desired conclusions and the risk of wrong decisions (lines 4–18).
- Section 8.4.1 describes graphical estimation and maximum-likelihood methods for censored data and notes limitations and software requirements (lines 4–12).
- These passages support the broad methodological direction of Claims B and C. Claim A's definition should be checked against the handbook's “Basic terms and models” section, not inferred from the chapter index alone.
- The handbook is an official statistical reference, but Evidence Use records currently contain no precise section locators. All three remain HOLD pending pinpointed review and reliability/statistical engineering review.

### Remaining lane 04 claims

- Political economy, project management, public data, and queueing theory Claims are moderate/low routing categories based on their statements, not acceptance decisions.
- Their linked Evidence Use and Source records still require claim-specific passage checks. Public-data comparability and fitness statements in particular need methodological support, not only general source descriptions.
- All remaining Claims in lane 04 remain HOLD until the exact Claim → Evidence Use → Source passage chain is verified.

## 4. Lane 04 disposition

- Claims statement-screened for routing: 20/20.
- High-consequence routes: 7 (2 privacy, 2 public procurement, 3 reliability).
- Elevated routes: 3 quality-control Claims.
- Moderate routes: 7 (3 public data, 2 political economy, 2 project management).
- Low direct-consequence foundational queueing theory: 3.
- D/E/B scores assigned in this screen: 0.
- Claims accepted or release-cleared: 0.
- Canonical Claim/Evidence Use/Source JSON changed: 0.
- Human expert review completed: 0.
- Lane status: RISK SCREEN COMPLETE FOR ROUTING; SUBSTANTIVE SCORING HOLD.


## 5. Required next work

1. Continue the same content-based risk screen for lanes 01–03.
2. Add exact GDPR Article 5 and relevant handbook section locators to the audit evidence, without editing canonical records absent bounded authorization.
3. Keep procurement claims jurisdiction-limited to the World Bank IPF framework unless independent applicable public-procurement sources are added.
4. Route privacy, procurement and reliability Claims to qualified specialist review; keep all HOLD until those gates are met.
5. Proceed to D/E/B scoring only after risk screening and exact source-passage verification.

## 6. Sources consulted

- European Commission, Principles of the GDPR: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
- European Data Protection Board, Basic principles: https://www.edpb.europa.eu/topics/key-gdpr-concepts/basic-principles_en
- World Bank, Procurement Framework: https://www.worldbank.org/ext/en/what-we-do/project-procurement/framework
- NIST/SEMATECH e-Handbook, Process or Product Monitoring and Control: https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm
- NIST/SEMATECH e-Handbook, Assessing Product Reliability: https://www.itl.nist.gov/div898/handbook/apr/apr.htm
