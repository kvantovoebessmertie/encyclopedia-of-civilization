# M13 — strict passage/locator review package 06

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: the six exact triples that were incorrectly counted as strict-review-complete through Package 07, which is a risk-screen report rather than a strict source-passage review.  
State: **six source-passage desk reviews completed; no canonical edits, no D/E/B changes, no rights clearance, no specialist sign-off, no publication clearance.**

## 1. Scope correction and method

The strict 47-row queue reconciliation had incorrectly assigned six rows to `M13-UNASSESSED-RISK-CONTENT-SCREEN-PACKAGE-07`. That report is a risk-screen artifact. It discusses some of the same Claims, but it does not provide the Claim-specific source-passage/locator review required by the strict queue.

The six rows are therefore reviewed here as a dedicated strict passage/locator package. Before this package, strict source-passage review coverage was **41/47**, not 47/47. With this package, all 47 exact queue rows have a desk-level strict source-passage review assignment. This is not evidence that all 47 sources fully support their Claims or that any HOLD is cleared.

All six Claim v1, Evidence Use v1 and Source v1 records were fetched. All exact IDs and version references resolve and match. Every EU description is generic and lacks a reproducible Claim-specific passage locator.

## 2. Exact triples

| Slice | Claim | Evidence Use | Source |
|---|---|---|---|
| behavioral-economics-basics | `CLM-BEHAVIORAL_ECONOMICS_BASICS-B@1` | `EU-BEHAVIORAL_ECONOMICS_BASICS-B@1` | `SRC-BEHAVIORAL_ECONOMICS_BASICS@1` |
| behavioral-economics-basics | `CLM-BEHAVIORAL_ECONOMICS_BASICS-C@1` | `EU-BEHAVIORAL_ECONOMICS_BASICS-C@1` | `SRC-BEHAVIORAL_ECONOMICS_BASICS@1` |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-A@1` | `EU-BIODIVERSITY_BASICS-A@1` | `SRC-BIODIVERSITY_BASICS@1` |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-B@1` | `EU-BIODIVERSITY_BASICS-B@1` | `SRC-BIODIVERSITY_BASICS@1` |
| calibration-basics | `CLM-CALIBRATION_BASICS-B@1` | `EU-CALIBRATION_BASICS-B@1` | `SRC-CALIBRATION_BASICS@1` |
| calibration-basics | `CLM-CALIBRATION_BASICS-C@1` | `EU-CALIBRATION_BASICS-C@1` | `SRC-CALIBRATION_BASICS@1` |

## 3. Claim-by-Claim findings

### 3.1 Behavioral Economics B — prospect theory and uncertainty

**Claim:** “Исследования Канемана и Тверски привели к формулировке теории перспектив как модели решений в условиях неопределённости.”

**Registered Source:** Nobel Prize, 2002 Economic Sciences press release: https://www.nobelprize.org/prizes/economic-sciences/2002/press-release/Orne/

**Passage result: DIRECT.** The press release section “Psychological and experimental economics” states that Kahneman and Amos Tversky formulated prospect theory as an alternative that better accounts for observed behaviour, in the context of decisions under uncertainty. The source is an official Nobel Prize page; direct retrieval returned 403 in this check, but the official indexed page text exposes the relevant passage. The EU should identify the exact section and paragraph rather than merely naming the Nobel source.

**Risk route: LOW direct consequence.** This is a historical/theoretical statement. Do not imply that prospect theory is a universal model for all decisions or a normative prescription.

**Disposition: HOLD pending EU pinpoint and a scope note that prospect theory is a descriptive model of choices under uncertainty.**

### 3.2 Behavioral Economics C — systematic departures from standard models

**Claim:** “Поведенческий подход показывает, что наблюдаемое принятие решений может систематически отличаться от предсказаний стандартных экономических моделей.”

**Passage result: DIRECT.** The same Nobel Prize press release states that Kahneman demonstrated human decisions may systematically depart from predictions of standard economic theory and that prospect theory better accounts for observed behaviour. The passage directly supports the Claim's qualified “may” formulation.

**Risk route: LOW direct consequence.** Avoid implying that every individual decision deviates or that all standard economic models are invalid.

**Disposition: HOLD pending EU pinpoint to the same “Psychological and experimental economics” section and preservation of the qualified scope.

### 3.3 Biodiversity A — species, genetic and ecosystem diversity

**Claim:** “Биоразнообразие включает разнообразие видов и генетических вариантов и связано с разнообразием экосистем.”

**Registered Source:** OpenStax, *Biology 2e*, section 47.4 “Preserving Biodiversity”: https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity

**Passage result: PARTIAL.** Section 47.4, “Measuring Biodiversity,” describes cataloguing species through molecular genetics and DNA barcoding (paras. 1–2). Later “Preserve Design” discusses the number of species, migration, speciation, extinction and ecosystem habitat (paras. 1–3). These passages support species-level and ecosystem-level dimensions and the use of genetic methods. They do not explicitly provide a complete three-level definition of biodiversity including variation within species. A direct definition source or a narrower Claim is needed.

**Risk route: MODERATE.** Biodiversity concepts inform conservation and environmental policy. Distinguish genetic diversity within species, species diversity and ecosystem diversity; do not collapse them into one metric.

**Rights:** OpenStax explicitly prohibits LLM/generative-AI ingestion without prior written permission and uses CC BY-NC-SA terms requiring noncommercial reuse, attribution and ShareAlike. No permission is recorded.

**Disposition: HOLD pending a direct three-level definition, precise locator and rights resolution or a rights-compatible replacement source.**

### 3.4 Biodiversity B — migration, speciation and extinction

**Claim:** “Численность видов может изменяться из-за соотношения процессов возникновения и исчезновения видов.”

**Passage result: DIRECT.** OpenStax 47.4, “Preserve Design,” states that biodiversity on an island is a function of species origin through migration, speciation and extinction (paragraph 1 of that subsection). It further describes immigration and extinction probabilities in relation to island size and population size. This directly supports the Claim's mechanism, although “численность видов” should be interpreted as number of species/richness rather than population abundance of individual organisms.

**Risk route: MODERATE.** This is an ecological mechanism; preserve the distinction between species richness and population size.

**Rights/disposition:** Same OpenStax AI-ingestion and CC BY-NC-SA HOLD as 3.3. No AI-enabled reuse is cleared.

### 3.5 Calibration B — calibration and metrological traceability

**Claim:** “Калибровка является частью системы измерительной прослеживаемости и требует документированных процедур и результатов.”

**Registered Source:** NIST Calibration Services: https://www.nist.gov/calibrations

**Passage result: PARTIAL / DIRECT SUPPORT IN A LINKED, DISTINCT NIST POLICY.** The registered NIST Calibration Services page says NIST calibration services help makers and users of precision instruments achieve measurement quality (page overview). It links to NIST Policy on Metrological Traceability: https://www.nist.gov/calibrations/traceability. That separate policy states that metrological traceability requires an unbroken chain of calibrations to specified reference standards (section “Introduction”) and defines traceability as a documented unbroken chain of calibrations, each contributing to measurement uncertainty (Policy Statement item 1). It also assigns responsibility for supporting traceability claims to the provider and assessment to the user (item 3). The current registered Source/EU does not identify this separate policy page or the exact VIM definition.

**Risk route: ELEVATED — measurement reliability.** Traceability is not a generic guarantee of instrument correctness or fitness for every purpose. Calibration certificates, reference standards, uncertainty and the intended measurement need matter.

**Disposition: HOLD.** Add the NIST traceability policy as a separately versioned Source/EU or explicitly version the linked resource relationship; add the precise policy/VIM locator. Do not silently treat the calibration services landing page as the full traceability policy.

### 3.6 Calibration C — traceability does not guarantee fitness for purpose

**Claim:** “Калибровка не означает автоматически, что измерительный прибор пригоден для любой задачи: пригодность зависит от требуемых характеристик и условий применения.”

**Passage result: DIRECT CONCEPTUAL SUPPORT IN THE LINKED NIST POLICY; PARTIAL AGAINST THE REGISTERED SOURCE RECORD.** NIST Policy on Metrological Traceability, Policy Statement item 5, explicitly says traceability alone does not signify or guarantee fitness for purpose because uncertainty must be sufficiently small to satisfy the particular measurement need. This is a close direct match. However, that is the linked traceability-policy page, not the currently registered Calibration Services landing page.

**Risk route: ELEVATED — measurement reliability.** Do not treat calibration as proof that an instrument is suitable for every range, matrix, environment or uncertainty requirement.

**Disposition: HOLD.** Version the traceability policy as a distinct Source/EU or update the registered chain through an authorized correction; record the exact item 5 locator.

## 4. Consolidated disposition

| Claims | Passage fit | Risk route | Main issue |
|---|---|---|---|
| Behavioral Economics B/C | Direct | Low | Nobel press-release section pinpoint missing; indexed official text used because page fetch returned 403 |
| Biodiversity A | Partial | Moderate | Registered OpenStax section lacks a complete three-level definition |
| Biodiversity B | Direct | Moderate | Direct passage on migration, speciation and extinction; distinguish species richness from abundance |
| Calibration B/C | Partial against registered Source; direct concept in linked NIST policy | Elevated | NIST traceability policy is a separate page and must be versioned in the evidence chain |

Counts:
- Direct against registered Source: **3** (Behavioral Economics B/C; Biodiversity B).
- Partial against registered Source: **3** (Biodiversity A; Calibration B/C).
- Not established: **0**.
- Low direct-consequence routing: **2**.
- Moderate routing: **2**.
- Elevated routing: **2**.

## 5. Integrity

- Exact Claim IDs reviewed: **6**.
- Claim records inspected: **6**.
- Evidence Use records inspected: **6**.
- Source records inspected: **3**.
- Claim→EU→Source exact identity/version chains resolving: **6/6**.
- Generic/non-pinpoint EUs: **6/6**.
- Canonical Claim/EU/Source JSON changes: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Risk metadata assigned or changed: **0**.
- Rights permissions obtained: **0**.
- Specialist approvals: **0**.
- Publication/Human View approval: **0**.

## 6. Strict queue status after correction

- The 47-row strict queue is now allocated across Packages 01–06: 7 + 6 + 9 + 3 + 16 + 6 = **47/47**.
- Package 07 is a separate unassessed-risk screen and is not counted as a strict source-passage package.
- The former allocation of these six rows to Package 07 was an accounting error. See the separate erratum and corrected exact-ID ledger.
- All six Claims remain HOLD. Desk-review coverage is not source clearance, rights clearance, specialist approval, D/E/B completion, canonical correction, M13 closure or release approval.

This package is a desk-level source-passage review only.
