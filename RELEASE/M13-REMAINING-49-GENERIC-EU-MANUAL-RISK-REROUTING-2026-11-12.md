# M13 manual risk rerouting — remaining 49 generic-Evidence-Use Claims

Date: 2026-11-12
Basis: full-inventory audit at 2db3995b50c3b26179a341612c3aa1f3438551d1 and subsequent append-only source-passage reports.
Scope: the 49 Claims remaining in the machine high-consequence queue after 91/140 Claims received source-passage review. This is a content-based routing screen only; it does not alter machine metadata, score Claims, or clear any Claim for release.

## 1. Result

The 49 remaining Claims were read at statement level. None contains a direct operational procedure, dosage, design calculation, emergency instruction, eligibility determination or executable security configuration. The machine high-consequence flag is overinclusive for this residual set.

They are rerouted for review priority as follows:
- **23 MODERATE — jurisdiction/standard-sensitive:** legal, accounting, public finance, tax, constitutional, administrative and policy concepts. These require explicit jurisdiction/date/scope boundaries before applied use, but are not operational legal or financial advice as currently worded.
- **26 LOW DIRECT CONSEQUENCE — foundational or academic:** basic computing, cell/developmental biology, motion, matter, ecology, political science, history and social-science definitions. They still need source locators and normal editorial review, but do not warrant emergency/safety-specialist routing solely from their present wording.

This is a queue-priority correction, not removal of the `high_consequence_screen` machine flag. Canonical risk metadata is unchanged.

## 2. Moderate — 23 Claims

### Accounting and finance (4)
- `CLM-ACCOUNTING_BASICS-A`
- `CLM-ACCOUNTING_BASICS-B`
- `CLM-ACCOUNTING_BASICS-C`
- `CLM-FINANCE_BASICS-A`

Reason: foundational accounting/financial concepts can become jurisdiction- and standard-dependent when used in reporting or investment decisions. Keep accounting standards, instrument type and measurement basis explicit.

### Administrative, comparative and constitutional law (5)
- `CLM-ADMINISTRATIVE_LAW_BASICS-A`
- `CLM-COMPARATIVE_LAW_BASICS-A`
- `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-A`
- `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B`
- `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C`

Reason: descriptive classifications differ across constitutional arrangements and jurisdictions. Do not translate these general definitions into advice about a particular state's current legal powers or institutions without primary legal sources.

### Behavioral economics and construction project governance (2)
- `CLM-BEHAVIORAL_ECONOMICS_BASICS-A`
- `CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-C`

Reason: conceptual behavioural-economics framing is non-operational; project management plan details can have contractual and jurisdictional consequences, so retain contract, project scale, parties and legal setting boundaries.

### Diplomacy, human rights and international law/relations (6)
- `CLM-DIPLOMACY_BASICS-A`
- `CLM-DIPLOMACY_BASICS-B`
- `CLM-HUMAN_RIGHTS_BASICS-A`
- `CLM-HUMAN_RIGHTS_BASICS-B`
- `CLM-INTERNATIONAL_LAW_BASICS-A`
- `CLM-INTERNATIONAL_RELATIONS_BASICS-A`

Count correction: this subsection contains 6 Claims (not 4). They are foundational descriptions of conventions, declarations, the UN Charter and international legal subjects. Preserve the distinction between treaty text, non-binding declarations, customary law and domestic implementation.

### Labour relations (1)
- `CLM-LABOR_RELATIONS_BASICS-A`

Reason: collective bargaining is a general labour-relations mechanism; legal effects and bargaining rights depend on applicable labour law and the parties' status.

### Public administration, finance, policy and taxation (5)
- `CLM-PUBLIC_ADMINISTRATION_BASICS-C`
- `CLM-PUBLIC_FINANCE_BASICS-A`
- `CLM-PUBLIC_FINANCE_BASICS-C`
- `CLM-PUBLIC_POLICY_BASICS-A`
- `CLM-TAXATION_BASICS-A`

Reason: these are high-level descriptions, but public powers, fiscal arrangements, tax rules and policy evaluation are jurisdiction- and time-dependent. Require current primary government/statutory sources for applied claims.

The correct total for this section is **23 moderate Claims**: 4 accounting/finance + 5 administrative/comparative/constitutional + 2 behavioral/construction + 6 diplomacy/human-rights/international + 1 labour + 5 public administration/finance/policy/taxation.

## 3. Low direct consequence — 26 Claims

### Cell and developmental biology (5)
- `CLM-CELL_BASICS-A`
- `CLM-CELL_BASICS-B`
- `CLM-CELL_BASICS-C`
- `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A`
- `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B`

Reason: foundational descriptions of cells, prokaryotes/eukaryotes and differentiation; no clinical diagnosis, treatment or laboratory protocol is stated.

### Computing and general digital concepts (3)
- `CLM-COMPUTING_BASICS-A`
- `CLM-COMPUTING_BASICS-B`
- `CLM-COMPUTING_BASICS-C`

Reason: basic definitions of systems, algorithms and digital representation; no exploit, deployment, configuration or security procedure is provided.

### Civil society, comparative civilizations and development economics (3)
- `CLM-CIVIL_SOCIETY_BASICS-A`
- `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A`
- `CLM-DEVELOPMENT_ECONOMICS_BASICS-A`

Reason: broad descriptive social-science concepts, not operational interventions or eligibility advice.

### Ecophysiology and history methods (5)
- `CLM-ECOPHYSIOLOGY_BASICS-A`
- `CLM-ECOPHYSIOLOGY_BASICS-B`
- `CLM-ECOPHYSIOLOGY_BASICS-C`
- `CLM-HISTORY_METHODS_BASICS-A`
- `CLM-HISTORY_METHODS_BASICS-C`

Reason: general research and organism-environment concepts. Measurement comparability and causal inference remain methodological caveats, not direct safety instructions.

### Matter, motion and basic economics/biology (6)
- `CLM-MATTER_BASICS-A`
- `CLM-MICROECONOMICS_BASICS-A`
- `CLM-MOTION_BASICS-A`
- `CLM-MOTION_BASICS-B`
- `CLM-MOTION_BASICS-C`
- `CLM-VIROLOGY_BASICS-A`

Reason: foundational definitions of matter, supply/demand, kinematics and viruses. The virology Claim is a basic description of viral dependence on host cells, not a health recommendation or pathogen-handling protocol.

### Political science (3)
- `CLM-POLITICAL_SCIENCE_BASICS-A`
- `CLM-POLITICAL_SCIENCE_BASICS-B`
- `CLM-POLITICAL_SCIENCE_BASICS-C`

Reason: general academic distinctions between descriptive and normative analysis and empirical methods.

Total: 5 + 3 + 3 + 5 + 6 + 3 = **25**. One additional low-direct-consequence Claim is `CLM-LABOR_ECONOMICS_BASICS-A`, a foundational description of labour markets, employment, wages and institutions. The correct low-priority total is **26 Claims**.

## 4. Full-inventory priority position

- Machine high-consequence generic-EU worklist: 140 Claims.
- Source-passage reviews completed in append-only reports: 91/140.
- Remaining at statement-level content risk screen: 49/140.
- Residual queue manually rerouted: 23 moderate + 26 low direct consequence.
- Additional emergency/operational priority in the residual 49: none identified from the statement-level screen; all 49 still require source-passage review in the normal thematic queue.
- Generic Evidence Use records across the full inventory: 519. All 519 remain candidates for exact-locator remediation; source-passage review does not automatically rewrite canonical Evidence Use.
- Canonical Claim/Evidence Use/Source JSON changed: 0.
- D/E/B scores changed: 0.
- Claims accepted or release-cleared: 0.

## 5. Safeguards and next work

1. Do not remove or rewrite the machine `high_consequence_screen` flags on the basis of this report alone.
2. Keep the 23 legal/financial/policy Claims on HOLD until source locators, jurisdiction, date and standard boundaries are explicit.
3. Keep the 26 foundational Claims on HOLD until exact evidence locators and source fit are recorded.
4. Continue the 519-item generic-Evidence-Use remediation by exact Claim→EU→Source passage, prioritizing the 91 already reviewed for bounded correction proposals.
5. Do not create another nominal D/E/B batch: all 1,494 Claims already have score-report coverage. The remaining work is evidence-chain remediation, duplicate/alias adjudication, specialist review, Human View and release gates.

## 6. Counting note

The risk-domain counts in the full-inventory report are non-exclusive. This report counts each Claim once, by its primary consequence route. The explicit arithmetic above is retained so the routing totals can be independently checked.
