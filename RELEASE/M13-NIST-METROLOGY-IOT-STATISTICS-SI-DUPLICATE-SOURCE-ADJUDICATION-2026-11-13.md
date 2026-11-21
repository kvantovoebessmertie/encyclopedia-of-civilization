# M13 duplicate-source adjudication: NIST Metrology, IoT Cybersecurity, Statistics Handbook, and SI Units

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `1831b9399fc714a81e4b64dd7698a6c5967c8ae5`  
Scope: four shared-URI groups from the consolidated duplicate-source inventory. Source, Evidence Use and Claim records were inspected directly; public NIST pages and relevant handbook sections were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Linked Claims | Adjudication |
|---|---:|---:|---|
| NIST Metrology | 2 | 6 | One current NIST metrology page. It directly supports the metrology definition and traceability chain; some instrumentation-specific claims need more precise sources. |
| NIST Cybersecurity for IoT Program | 2 | 6 | One program landing page. It is relevant to IoT cybersecurity, especially lifecycle security, but does not establish general embedded-system architecture or sensor measurement claims. |
| NIST/SEMATECH Engineering Statistics Handbook | 3 | 8 | One handbook with useful claim-specific sections. Several Claims have good direct support once section locators are supplied; the three IDs are not independent publications. |
| NIST SI Units | 2 | 5 | One current NIST SI page. It directly supports the base/derived-unit Claims and the SI definition Claim; it does not by itself support measurement uncertainty or full measurement procedure. |

**Totals: 9 Source records, 25 linked Claims, four URI groups.** Repeated IDs do not create independent corroboration. Keep the distinct Claim/Evidence Use links until any deduplication is explicitly authorized and safely versioned.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed. This report is source-fit adjudication only.

## 2. NIST Metrology — two IDs, one current page

### Source identity

Both records point to `https://www.nist.gov/metrology`:

- `SRC-MEASUREMENT_INSTRUMENTATION_BASICS`
- `SRC-METROLOGY_BASICS`

Both identify “NIST — Metrology”. The current NIST page is retrievable and states that metrology is the science of measurement and its application. It also describes calibration, standard reference materials/data, measurement uncertainty resources, measurement quality assurance and metrological traceability as an unbroken chain of calibrations to specified reference standards.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-METROLOGY_BASICS-A` — metrology is the science of measurement and its application, including methods, standards and evaluation | Direct for the core definition. NIST page section “What is metrology?” states the definition. The broader list of methods/standards can be supported by the following NIST resource description; keep wording no broader than the cited passage. |
| `CLM-METROLOGY_BASICS-B` — traceability links a result to standards through a documented calibration chain | Direct. Use the NIST page’s “What is NIST’s role?” passage on an unbroken chain of calibrations to specified reference measurement standards. |
| `CLM-METROLOGY_BASICS-C` — measurement quality requires uncertainty, method, instrument, conditions and procedure, not only a number | Partial. NIST identifies uncertainty tools, calibration and measurement-quality assurance, but the complete multi-factor statement needs a specific uncertainty/measurement-process source. |
| `CLM-MEASUREMENT_INSTRUMENTATION_BASICS-A` — instrumentation obtains quantitative information about objects, processes or environment | Partial. The page supports measurement science and NIST measurement resources, but is not a direct definition of measurement apparatus or instrumentation. |
| `CLM-MEASUREMENT_INSTRUMENTATION_BASICS-B` — instrument selection depends on measurand, range, accuracy, uncertainty and conditions | Not directly established by the landing page. Add a measurement-instrument selection or measurement-process reference with a pinpoint. |
| `CLM-MEASUREMENT_INSTRUMENTATION_BASICS-C` — comparability depends on calibration, traceability, methods and equipment | Partial-to-direct for calibration and traceability; methods/equipment dependence needs a specific technical source. |

### Disposition

One NIST page, not two independent sources. Keep the current page as a valid source for metrology definition and traceability, but add specific technical publications for instrument selection and measurement uncertainty before treating all six Claims as fully supported.

## 3. NIST Cybersecurity for IoT — two IDs, one program page

### Source identity

Both records point to `https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program`:

- `SRC-EMBEDDED_SYSTEMS_BASICS`
- `SRC-SENSOR_SYSTEMS_BASICS`

Both identify “NIST IoT Cybersecurity”. The current page is retrievable and explicitly concerns cybersecurity guidance for IoT products. It links to the NISTIR 8259 and SP 800-213 publication series. It defines IoT products in the related NISTIR 8259r1 as digital equipment or systems that sense or actuate in the physical world and are connected or connectable to the Internet.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-EMBEDDED_SYSTEMS_BASICS-A` — an embedded system combines computation with a device or process | Partial at most. The NIST IoT definition covers connected digital equipment/systems that sense or actuate, but does not define embedded systems generally. |
| `CLM-EMBEDDED_SYSTEMS_BASICS-B` — resource and operating-environment constraints influence embedded-system architecture | Partial at most. NISTIR 8259r1 §1 describes strict cost limits and unusual operating environments as factors affecting IoT cybersecurity posture/expectations; it does not directly establish the general architecture claim. |
| `CLM-EMBEDDED_SYSTEMS_BASICS-C` — embedded-device security spans the whole lifecycle | Direct only if bounded to cybersecurity of IoT products. NISTIR 8259r1 (April 2026) explicitly separates pre-market and post-market manufacturer activities and includes support, updates and retirement. It is not evidence for every embedded device or every aspect of security. |
| `CLM-SENSOR_SYSTEMS_BASICS-A` — sensors obtain observations and transmit them for processing | Not supported by the IoT cybersecurity landing page. The fact that IoT products can sense/actuate does not establish a generic sensor-system signal/processing chain. |
| `CLM-SENSOR_SYSTEMS_BASICS-B` — measurement has range, accuracy and conditions of applicability | Not supported by the IoT cybersecurity page. Use a sensor/instrumentation or metrology source. |
| `CLM-SENSOR_SYSTEMS_BASICS-C` — sensor-data meaning depends on calibration, location and environment | Not supported by the IoT cybersecurity page. A NIST sensor-calibration publication is a more appropriate candidate, with the Claim narrowed to its demonstrated measurement context. |

### Better source candidates

- **NIST IR 8259r1, _Foundational Cybersecurity Activities for IoT Product Manufacturers_ (April 2026)**, DOI `10.6028/NIST.IR.8259r1`: a specific publication for the embedded/IoT cybersecurity lifecycle Claim. It explicitly covers pre-market and post-market activities and product retirement. Use this publication as a separate Source identity, not as an alias for the program landing page.
- **NIST, _Sensor Calibration and Characterization to Meet Climate Monitoring Requirements_ (2014)**: candidate support for calibration, environmental conditions and comparability of sensor measurements; it is climate-monitoring-specific.
- **NIST Special Publication 615, _Sensor Handbook for Automatic Test, Monitoring, Diagnostic, and Control Systems_**: candidate for sensor characteristics, measurement range and uncertainty; inspect its age and exact scope before use.

### Disposition

One IoT cybersecurity program page, not two independent sources. Only the lifecycle-security Claim has a clear, narrowly scoped route to direct support through NISTIR 8259r1. The sensor-system Claims require different sources. Do not use an IoT cybersecurity page as generic sensor metrology evidence.

## 4. NIST/SEMATECH Engineering Statistics Handbook — three IDs, one handbook

### Source identity

These three Source records all point to `https://www.itl.nist.gov/div898/handbook/`:

- `SRC-PROBABILITY_BASICS`
- `SRC-SAMPLING_BASICS`
- `SRC-STATISTICS_INFERENCE_BASICS`

They identify the NIST/SEMATECH Engineering Statistics Handbook with slightly different wording. This is one handbook, not three independent publications. The root page is a legacy frameset, but the relevant chapter pages remain individually retrievable and provide usable pinpoint locators.

### Claim-specific locator proposals

| Claim | Assessment and proposed pinpoint |
|---|---|
| `CLM-PROBABILITY_BASICS-A` — event probability is between 0 and 1 in a standard probability model | Direct for the discrete probability-function case. Handbook §1.3.6.1 states non-negativity, normalization and that each discrete probability is between 0 and 1. Avoid implying that a probability density for a continuous variable must itself be at most 1. |
| `CLM-PROBABILITY_BASICS-B` — event and its complement have probabilities summing to 1 | Partial. §1.3.6.1 states that the probabilities over all discrete outcomes sum to 1. The event/complement identity is a consequence of a partition, but is not stated explicitly in the reviewed passage. Add a direct probability-axioms source or identify an explicit handbook passage before treating it as directly evidenced. |
| `CLM-SAMPLING_BASICS-A` — a sample uses part of a population to infer about the wider population | Direct. §3.1.3.4 “Populations and Sampling” explicitly describes drawing a sample from a target population and making inferences. |
| `CLM-SAMPLING_BASICS-B` — the sampling method affects representativeness | Direct. §§3.1.3.4 and 3.3.3.2 address representativeness, sampling schemes, systematic sampling error, stratification and randomization. |
| `CLM-SAMPLING_BASICS-C` — interpretation must account for variability, sample size, selection method and bias | Direct within the handbook’s production-process context. §§3.1.3.4, 3.3.3.2 and 3.3.3.3 cover sample adequacy, variability, precision, sample size and systematic sampling error. |
| `CLM-STATISTICS_INFERENCE_BASICS-A` — sample data support inference about population/model characteristics | Direct. §1.3.5 “Quantitative Techniques” explains sample estimates of population parameters and interval estimates. |
| `CLM-STATISTICS_INFERENCE_BASICS-B` — statistical methods rely on assumptions and applicability depends on those assumptions | Direct. §1.2.1 “Underlying Assumptions” and §1.2.3 “Techniques for Testing Assumptions” address the assumptions and their testing. |
| `CLM-STATISTICS_INFERENCE_BASICS-C` — uncertainty must be considered when interpreting estimates and tests | Direct. §1.3.5 discusses interval estimates, uncertainty of sample estimates and hypothesis testing; §1.2.3 discusses the validity of conclusions when assumptions fail. |

### Disposition

One handbook, three Source IDs. The existing NIST/SEMATECH source is materially relevant and supports most linked Claims when section-level locators are supplied. Do not count the three Source IDs as independent corroboration. The probability complement Claim needs a more explicit passage or a second probability-axioms source.

## 5. NIST SI Units — two IDs, one current page

### Source identity

Both records point to `https://www.nist.gov/pml/owm/metric-si/si-units`:

- `SRC-NIST-SI-UNITS`
- `SRC-UNITS_AND_MEASUREMENT`

Both identify the same NIST SI Units page. The page is current and retrievable. It states that the SI has seven base units defined using seven defining constants; the seven base units define 22 derived units with special names and symbols; and it provides definitions of quantity, unit and value.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-SI-SEVEN-BASE` — SI has seven base units defined through fixed defining constants | Direct. Use the page’s “Defining Constants” and “Base and Derived Units” sections. |
| `CLM-SI-DERIVED` — SI includes 22 derived units with special names and symbols | Direct. The page explicitly states that the seven base units define 22 derived units with special names and symbols. |
| `CLM-UNITS_AND_MEASUREMENT-A` — measurement expresses a quantity relative to a unit and procedure | Partial. The page’s “Useful Definitions” section defines quantity, unit and value, including the numerical value/unit relationship. It does not fully establish the measurement procedure part. |
| `CLM-UNITS_AND_MEASUREMENT-B` — SI provides a consistent set of units for physical quantities | Direct. The page describes SI as the international standard and explains the base/derived unit structure. |
| `CLM-UNITS_AND_MEASUREMENT-C` — a measurement result is not exact knowledge without method and uncertainty | Partial. The page establishes that numerical values depend on the unit, but it does not substantiate measurement uncertainty or the method dependence. Use a metrology/measurement-uncertainty source as well. |

### Disposition

One NIST SI page, not two independent sources. It is a good direct source for the SI-specific Claims and partial support for general measurement concepts. Preserve the distinction between SI unit definitions and metrological uncertainty.

## 6. Consolidated audit decision and next actions

1. Count each shared URI as one source identity for independence analysis: Metrology = 1; IoT Cybersecurity = 1; NIST/SEMATECH Handbook = 1; SI Units = 1.
2. Keep all 25 Claim/Evidence Use chains in the audit denominator. Do not delete or merge records based on URI equality.
3. Prepare bounded correction proposals:
   - Metrology: retain the current NIST page for definition and traceability; add precise metrology publications for instrument selection and uncertainty.
   - IoT: use NISTIR 8259r1 for IoT cybersecurity lifecycle only; add sensor-specific references for measurement-system Claims.
   - Statistics: add exact handbook section locators; supplement the event/complement probability rule with a direct axioms source if needed.
   - SI: add exact NIST SI page sections; supplement measurement procedure and uncertainty with a metrology source.
4. Distinguish same-publication duplicate IDs from distinct publications produced by the same institution. Institutional diversity is not the same as publication independence.
5. After any later authorized canonical correction, run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA.

## 7. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records source identity, current retrievability and Claim-level fit. It is not a release approval or an authorization to edit canonical records.
