# M13 — tranche 06: повторная проверка пяти частичных совпадений и точные локаторы источников

Дата: 2026-11-23  
Рабочая ветка: `m13-system-wide-depth-audit-2026-10-09`  
Исходный HEAD для чтения канонических записей: `b6c11385906cd73c907ddd9cf2fe7a37af76558f`  
Основание очереди: corrected residual-356 report-body reconciliation и tranche 05 source-identity crosswalk.

## 1. Назначение и границы

Пакет продолжает проверку пяти строк остаточной очереди, для которых в тематических отчётах найдены точные Claim@1 и Evidence Use@1, а идентичность Source была подтверждена отдельной сверкой названия/URI с канонической Source@1.

В этой tranche выполнены:
- повторное чтение 12 канонических записей Claim/Evidence Use/Source на актуальном M13 branch HEAD;
- сверка точных ID, версий и вложенных ссылок;
- повторная проверка прямых страниц NIST для конкретных утверждений;
- фиксация границ применимости и требуемых versioned remediation.

Это desk review и структурная перепроверка. Она НЕ является независимой метрологической/статистической экспертизой, D/E/B scoring, разрешением на изменение канонических записей, rights clearance, Human View или publication approval.

## 2. Повторная каноническая проверка

### Measurement Uncertainty

| Record | Expected identity/version | Current result |
|---|---|---|
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B` | Claim@1 | ID/version match |
| `EU-MEASUREMENT_UNCERTAINTY_BASICS-B` | Evidence Use@1 | ID/version match; claim_ref → Claim B@1; source_ref → `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-C` | Claim@1 | ID/version match |
| `EU-MEASUREMENT_UNCERTAINTY_BASICS-C` | Evidence Use@1 | ID/version match; claim_ref → Claim C@1; source_ref → `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` |
| `SRC-MEASUREMENT_UNCERTAINTY_BASICS` | Source@1 | ID/version match; URI = NIST TN 1297 landing page |

### Statistics Inference

| Record | Expected identity/version | Current result |
|---|---|---|
| `CLM-STATISTICS_INFERENCE_BASICS-A` | Claim@1 | ID/version match |
| `EU-STATISTICS_INFERENCE_BASICS-A` | Evidence Use@1 | ID/version match; exact Claim A@1 and Source@1 references |
| `CLM-STATISTICS_INFERENCE_BASICS-B` | Claim@1 | ID/version match |
| `EU-STATISTICS_INFERENCE_BASICS-B` | Evidence Use@1 | ID/version match; exact Claim B@1 and Source@1 references |
| `CLM-STATISTICS_INFERENCE_BASICS-C` | Claim@1 | ID/version match |
| `EU-STATISTICS_INFERENCE_BASICS-C` | Evidence Use@1 | ID/version match; exact Claim C@1 and Source@1 references |
| `SRC-STATISTICS_INFERENCE_BASICS` | Source@1 | ID/version match; URI = NIST/SEMATECH e-Handbook landing page |

All 12 fetched records resolve to the expected canonical IDs and versions. The five Evidence Use records still contain generic descriptions rather than claim-specific locators. No canonical record was written.

## 3. Claim-level source-passage findings

### 3.1 Measurement Uncertainty B — uncertainty is not measurement error

Claim:
> Неопределённость характеризует разброс значений, обоснованно приписываемых измеряемой величине, и не равна автоматически ошибке.

Current canonical Source chain:
- NIST TN 1297: `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`.
- The separate BIPM/VIM Evidence Use remains a distinct chain and must not be collapsed into the generic NIST EU.

Direct locators:
- NIST TN 1297 §2.3: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty
  - distinguishes uncertainty components from the familiar random/systematic error terminology;
  - explicitly warns that measurement error and uncertainty are different concepts;
  - gives the case where a corrected result may have negligible error while uncertainty remains large.
- NIST TN 1297 Appendix D1, terminology: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology
  - defines measurement error separately and notes that the measurement error is generally unknown while uncertainty may be evaluated.
- BIPM/JCGM VIM 2.26: https://jcgm.bipm.org/vim/en/2.26.html
  - gives the direct definition of measurement uncertainty as a non-negative parameter characterizing dispersion of quantity values attributed to a measurand, based on the information used.
- BIPM/JCGM VIM 2.16: https://jcgm.bipm.org/vim/en/2.16.html
  - defines measurement error separately as measured quantity value minus a reference quantity value.

Assessment:
- NIST TN 1297 §2.3 directly supports the distinction between error and uncertainty.
- VIM 2.26 is the strongest direct support for the Claim's dispersion wording; VIM 2.16 supplies the separate error definition.
- The current NIST EU alone should not be described as the source of the full VIM definition. The separately linked BIPM chain must remain independently version-pinned.
- The Russian wording is a reasonable explanatory paraphrase, but a final reviewer should compare it with the current VIM definition and avoid implying that uncertainty is simply a range or an error bar in every case.

Bounded remediation:
1. Keep NIST TN 1297 §2.3 as a direct locator for the error/uncertainty distinction.
2. Keep VIM 2.26 and 2.16 in the distinct BIPM chain with exact locators.
3. Do not merge the two Evidence Use chains or silently alter Source identities.
4. Any canonical EU update requires explicit bounded authorization and a new version.

Disposition: HOLD.

### 3.2 Measurement Uncertainty C — measurand and measurement model

Claim:
> Оценка неопределённости требует определения измеряемой величины и модели измерения.

Current canonical Source chain:
- `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` → NIST TN 1297.
- VIM 2.3 and 2.48 are conceptually relevant but are not currently linked through this Claim's canonical EU.

Direct locators:
- NIST TN 1297 Appendix A.1–A.3: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty
  - A.1 describes a measurand determined from input quantities through a functional relation and says the function should express the measurement process and include quantities contributing significant uncertainty;
  - A.2 describes the output estimate derived from input estimates;
  - A.3 gives the law of propagation of uncertainty and identifies the relevant sensitivity coefficients and covariance terms.
- BIPM/JCGM VIM 2.3: https://jcgm.bipm.org/vim/en/2.3.html
  - defines the measurand as the quantity intended to be measured.
- BIPM/JCGM VIM 2.48: https://jcgm.bipm.org/vim/en/2.48.html
  - provides the direct conceptual definition of a measurement model as the mathematical relation among quantities known to be involved in a measurement.

Assessment:
- NIST Appendix A.1–A.3 directly supports the operational relationship between measurand, input quantities, measurement function and uncertainty propagation.
- VIM 2.3 and 2.48 are the stronger direct definitional sources for the two key terms in the Claim.
- The NIST Source should not be presented as the sole definition of “measurement model.”
- The existing Claim is concise, but its evidence chain should distinguish the definition of the measurand/model from the NIST uncertainty-propagation method.

Bounded remediation:
1. Retain NIST Appendix A.1–A.3 as a direct practical support locator.
2. Prepare a distinct versioned BIPM/JCGM VIM Source/EU proposal for VIM 2.3 and 2.48.
3. Keep the current Claim wording under HOLD pending source-chain and scope review.
4. Do not repurpose the existing NIST Source ID to point to the VIM.

Disposition: HOLD.

### 3.3 Statistics Inference A — sample data and wider population

Claim:
> Статистический вывод использует данные выборки для получения информации о характеристиках более широкой совокупности или модели.

Direct locator:
- NIST/SEMATECH e-Handbook §7.1.4, “What are confidence intervals?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
  - explicitly describes taking a random sample, computing a statistic such as the sample mean, and using it to approximate the population mean;
  - explains that a confidence interval expresses uncertainty around the population parameter estimate.

Assessment:
- Directly supports the sample-to-population component.
- The locator is a concrete example from product/process comparisons, not a universal definition of every form of statistical inference.
- The Claim may remain as an introductory statement if its Context/Scope make clear that the source illustrates inference through estimation and interval procedures.

Bounded remediation:
- Version EU-A with §7.1.4 and a short description of sample statistic → population parameter estimation.
- Preserve the distinction between a population parameter and a fitted model parameter if the Claim is later broadened to models.

Disposition: HOLD.

### 3.4 Statistics Inference B — method-specific assumptions

Claim:
> Статистические методы требуют явных предположений о данных и модели, а их применимость зависит от выполнения этих условий.

Direct locator:
- NIST/SEMATECH e-Handbook §7.1.2, “What assumptions are typically made?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc12.htm
  - for the tests described in that chapter, identifies assumptions about a single process/distribution, normality and lack of temporal correlation;
  - explains that departures from assumptions should be examined before applying those tests.

Assessment:
- Directly supports the proposition that the validity of a particular statistical procedure depends on its assumptions.
- The source page is explicitly scoped to the tests in Chapter 7.1. It must not be used to imply that all statistical methods require normality or that one universal assumption set applies to all methods.
- The current Claim's phrase “статистические методы” is broader than the cited example. The reader-facing Context/Scope should preserve method-specific applicability, or the Claim should be narrowed in a separately authorized revision.

Bounded remediation:
- Version EU-B with §7.1.2 and state explicitly that its assumptions concern the procedures covered by that chapter.
- Do not universalize normality, independence or a single-process model across all statistical methods.

Disposition: HOLD.

### 3.5 Statistics Inference C — uncertainty in estimates and hypothesis tests

Claim:
> Неопределённость статистического вывода должна учитываться при интерпретации оценок и проверке гипотез.

Direct locators:
- NIST/SEMATECH e-Handbook §7.1.4, “What are confidence intervals?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
  - explains how sample estimates approximate population parameters and how confidence intervals characterize the uncertainty of that estimation procedure.
- NIST/SEMATECH e-Handbook §7.1.3, “What are statistical tests?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm
  - explains null and alternative hypotheses, significance level and the risks of Type I and Type II errors;
  - explicitly cautions that failure to reject a null hypothesis may indicate insufficient data, not proof of the null.
- NIST/SEMATECH e-Handbook §7.1.5, “Relationship between a test and a confidence interval”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc15.htm
  - explains the correspondence between a hypothesis test and whether the hypothesized parameter value lies within the corresponding confidence interval.

Assessment:
- The combined set directly supports the need to interpret estimation and hypothesis testing with their uncertainty and error risks.
- The Claim must not imply that a confidence interval and a significance test are interchangeable in every context, or that a non-significant result proves the null hypothesis.
- Practical significance, study design, model assumptions and effect size remain separate interpretive considerations.

Bounded remediation:
- Version EU-C with all three claim-specific section locators and distinguish interval estimation from hypothesis testing.
- Preserve the warning that “not rejected” does not mean “proven true.”

Disposition: HOLD.

## 4. Consolidated results

| Control | Result |
|---|---:|
| Partial report-body rows in scope | 5 |
| Canonical Claims fetched and ID/version checked | 5/5 |
| Canonical Evidence Use records fetched and ID/version checked | 5/5 |
| Canonical Source records fetched and ID/version checked | 2/2 |
| Evidence Use nested Claim/Source references checked | 5/5 |
| Direct NIST locator pages checked | 6 |
| Direct VIM locator pages checked | 4 |
| Claim-specific locators already stored in canonical EUs | 0/5 |
| Canonical records modified | 0 |
| New Source/EU records created | 0 |
| D/E/B scores assigned | 0 |
| Claims moved out of HOLD | 0 |
| Publication or rights decisions made | 0 |

## 5. What this tranche closes — and what it does not

This tranche strengthens the five partial rows from report-body identity matches to a fresh, current-HEAD canonical identity/reference check plus direct locator-level source research.

It does not convert them into the 19 explicit Claim@1/EU@1/Source@1 report-body triples. It does not change the corrected report-body count of 19 explicit triples plus five Source crosswalks. It does not reduce the 332-row residual group that lacks an EU@1 token in the inspected report bodies.

The five rows are now ready for a bounded, separately authorized versioned EU/Source remediation proposal. They are not ready for scoring or publication.

## 6. Protected state

- All five Claims remain HOLD.
- No historical evaluation was transferred.
- No canonical Claim, Evidence Use, Source, Context, Scope, Assessment, Relation, risk, allowlist or publication record was changed.
- No owner authorization was inferred.
- PR #21 remains Draft/open/unmerged.
- `main` was not modified.

## 7. References

- NIST TN 1297 §2.3: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty
- NIST TN 1297 Appendix A: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty
- NIST TN 1297 Appendix D1: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology
- NIST/SEMATECH e-Handbook §7.1.2: https://www.itl.nist.gov/div898/handbook/prc/section1/prc12.htm
- NIST/SEMATECH e-Handbook §7.1.3: https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm
- NIST/SEMATECH e-Handbook §7.1.4: https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
- NIST/SEMATECH e-Handbook §7.1.5: https://www.itl.nist.gov/div898/handbook/prc/section1/prc15.htm
- BIPM/JCGM VIM 2.16: https://jcgm.bipm.org/vim/en/2.16.html
- BIPM/JCGM VIM 2.26: https://jcgm.bipm.org/vim/en/2.26.html
- BIPM/JCGM VIM 2.3: https://jcgm.bipm.org/vim/en/2.3.html
- BIPM/JCGM VIM 2.48: https://jcgm.bipm.org/vim/en/2.48.html
