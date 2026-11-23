# M13 — Package 31 source-fit and rights follow-up

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Canonical records inspected at HEAD: `093e2d88f67012e9563930a79f5bb1a8b7678979`
Scope: Package 31 partial/HOLD Claims and candidate locators, including Manufacturing Systems B/C.

## 1. Status and guardrails

This is a noncanonical source-fit and rights review. It does not authorize canonical changes, D/E/B scoring, publication, or clearance of any Claim.

No canonical Claim, Evidence Use, Source, Context, Scope, Relation, provenance, risk metadata, or publication status is changed. Rights are assessed per source item, not inferred from public accessibility or institutional reputation.

## 2. Claim-level source findings

### 2.1 Maps and Navigation C — direct source candidates identified

Claim: `CLM-MAPS_AND_NAVIGATION_BASICS-C@1`

Statement: `Навигационный вывод зависит от качества карты, её масштаба, актуальности данных и условий на местности.`

Two USGS sources materially strengthen the registered map-and-compass source:

1. **US Topo accuracy FAQ** explains that map accuracy depends on the underlying source datasets, that individual-source accuracy is in attached metadata, and that there is no single accuracy statement for the entire map. It expressly says USGS maps/geospatial products are general reference and are not authoritative or official for navigation or regulatory purposes.
   - Exact locator: opening answer, especially the paragraphs on source-data accuracy, metadata, and non-authoritative navigation use.
   - URL: https://www.usgs.gov/faqs/how-accurate-are-us-topo-maps-and-why-dont-they-have-an-accuracy-statement

2. **USGS Topographic Mapping** explains that field surveys may be needed to establish control points and visually verify objects; horizontal and vertical control points position features and contours accurately. It also describes National Map Accuracy Standards.
   - Exact locator: “Information from field surveys” and “Rigorous standards ensure USGS map accuracy” sections.
   - URL: https://www.usgs.gov/educational-resources/topographic-mapping

A further USGS FAQ states that US Topo maps are updated on a three-year production cycle (one third of the country per year), subject to separate schedules such as Alaska:
- URL: https://www.usgs.gov/faqs/how-do-i-find-download-or-order-topographic-maps

Rights: USGS federal information is generally public domain unless marked otherwise or third-party material is present. These specific pages are official USGS informational pages; do not reuse embedded third-party media unless separately cleared.

Fit limitation: these sources establish U.S. US Topo accuracy/metadata/update/field-survey context. They do not establish that every map product worldwide has the same production cycle or accuracy characteristics. Keep the Claim’s generic wording appropriately qualified or document that USGS is an example rather than a universal map standard. No wording change is authorized here.

### 2.2 Materials A — NIST direct candidate found

Claim: `CLM-MATERIALS_BASICS-A@1`

Statement: “Materials science studies relationships among materials, measurements, models, data and performance.”

The NIST Materials Science and Engineering Division page directly describes development of measurements, models, data and standards, and identifies structure-property-processing relationships as a core disciplinary foundation. It also describes materials data/informatics, computational methods and measurement facilities for materials design and manufacturing.

Candidate:
- NIST Materials Science and Engineering Division: https://www.nist.gov/mml/materials-science-and-engineering-division

Exact locator:
- Opening division description: “development of measurements, models, data, and standards”.
- “Welcome to the Materials Science and Engineering Division”: structure-property-processing relationships.
- “Advanced Manufacturing”: materials data/informatics, computational methods and measurement facilities.

Rights: NIST states that information on its web pages is public information and may be distributed or copied except where material is marked copyrighted; attribution is requested. Review the specific page for any third-party marked content before use:
- https://www.nist.gov/copyrights-disclaimers

This is a substantially better fit than the previously registered opaque NIST Metallurgy root page. A bounded Source/Evidence Use addition can be prepared after exact path, rights and regression scope are frozen.

### 2.3 Materials C — NIST operating-condition and process/structure/performance candidates found

Claim: `CLM-MATERIALS_BASICS-C@1`

Statement: “Material behavior depends on composition, structure, processing and operating conditions.”

Candidate sources:

- NIST Thermodynamics and Kinetics Group: develops measurement methods, models, data and standards for thermodynamics, kinetics, phase transformations, microstructure evolution and material properties; uses this expertise to define processing, structure and performance relations.
  https://www.nist.gov/mml/materials-science-and-engineering-division/thermodynamics-and-kinetics-group

- NIST Mechanical Performance Group: develops measurement methods, models, data and standards for mechanical properties of advanced materials and materials under extreme environmental and operating conditions; evaluates performance within and outside design limits and conducts failure analysis.
  https://www.nist.gov/mml/materials-science-and-engineering-division/mechanical-performance-group

Exact locators:
- Thermodynamics and Kinetics Group: opening paragraph.
- Mechanical Performance Group: opening paragraph and group activities.

Rights: same NIST public-information exception and attribution conditions described in §2.2. Page-level third-party notices must still be checked.

Fit: together, these pages support composition/structure/process/property/performance relations and the importance of operating conditions. Preserve that the mechanical-performance source is specifically about mechanical properties and advanced materials; do not broaden its scope to every material property without additional support.

### 2.4 Materials Performance D — partial support improved, but application-specific selection framework remains open

Claim: `CLM-M5-MATERIALS-PERFORMANCE-D@1`

Statement: `Оценка материала связывает его свойства с требуемой работой и условиями эксплуатации; понимание причин отказа и потери долговечности является частью материаловедения, а пригодность для конкретного применения требует данных, соответствующих этому применению.`

NIST Mechanical Performance Group is a strong complementary candidate. It explicitly covers:
- measurement methods, models, data and standards for mechanical properties;
- advanced materials and materials under extreme environmental/operating conditions;
- determining materials and system performance within and outside design limits;
- reliable mechanical-property data;
- forensic analysis of failed components and investigations.

URL: https://www.nist.gov/mml/materials-science-and-engineering-division/mechanical-performance-group

This materially supports the conditions/performance/failure/data portions of the Claim. It does not, by itself, fully establish the complete general selection framework for every application or all material classes. Keep the Claim PARTIAL/HOLD pending a claim-specific materials-selection or failure-analysis source that explicitly connects required function, service conditions, failure mechanisms and application-relevant data.

### 2.5 Materials Science B — classification support improved; non-exhaustiveness and application caveat need explicit treatment

Claim: `CLM-MATERIALS_SCIENCE_BASICS-B@1`

Statement: `Материаловедение изучает, в частности, металлы, керамики, полимеры, полупроводники и композиты; эти классы имеют разные сочетания свойств, а название класса само по себе не определяет пригодность материала для конкретного применения.`

NSF’s Materials Research page identifies metals, ceramics, polymers and semiconductors in its accessible description, but does not explicitly list composites:
- https://www.nsf.gov/focus-areas/materials

NIST Mechanical Performance Group explicitly includes composites among advanced materials:
- https://www.nist.gov/mml/materials-science-and-engineering-division/mechanical-performance-group

NSF’s DMREF programme description supports the application-suitability caveat by describing design of materials for desired functions/properties through the interrelationships among composition, processing, structure, properties and performance, validated by measurement/experimentation:
- https://www.nsf.gov/funding/opportunities/dmref-designing-materials-revolutionize-engineer-our-future/nsf16-613/solicitation

Rights:
- NSF says most text on NSF webpages was prepared by federal employees or under contracts granting NSF the right to place the text in the public domain; copyrighted text is to be specifically identified. Check the individual page for any marked exceptions:
  https://www.nsf.gov/policies/digital
- NIST page rights follow §2.2.

Fit: these government sources together cover the five named classes and the principle that application suitability depends on material properties and design requirements. The classes should be described as examples, not a complete mutually exclusive taxonomy: semiconductors may overlap with other material categories, and composites are defined by combinations of constituents. Retain “в частности” and avoid implying that one category system is exhaustive.

### 2.6 Risk Management B — candidate identified, but exact ISO-derived wording remains rights-sensitive

Claim: `CLM-RISK_MANAGEMENT_BASICS-B@1`

Statement: `Риск связан с влиянием неопределённости на цели, поэтому оценка риска зависит от целей и контекста.`

The UK HM Treasury Orange Book contains a close definition in Annex 5 and the GOV.UK page states that the publication is under the Open Government Licence v3.0 except where otherwise stated. However, Annex 5 cites BS ISO 31000:2018 in its reference list. The wording “Risk is the effect of uncertainty on objectives” is therefore potentially derived from ISO 31000, which is on RIGHTS HOLD for this AI-assisted workflow.

Relevant locators:
- Orange Book Annex 5, “Definitions and Supportive Concepts”: https://www.gov.uk/government/publications/orange-book/the-orange-book-management-of-risk-principles-and-concepts
- OGL notice: same page, publication copyright/licence notice.
- Annex 6 reference 1 explicitly cites BS ISO 31000:2018.

Do not treat the OGL notice as automatically clearing third-party ISO-derived text. Do not use Annex 5’s definition as an alternative evidence passage unless the third-party rights status is resolved. The Orange Book’s broader, independently worded discussion of uncertainty, options, objectives and public-sector risk management may be considered separately, with UK central-government/public-sector scope preserved, but it does not by itself establish the exact definitional proposition.

Disposition: keep RIGHTS HOLD. No ISO content was used in this review. No replacement source is yet cleared for the exact Claim wording. Do not promote this Claim.

## 3. National Academies source exclusion

The National Academies Press chapter previously proposed for materials science explains the four elements of materials science (properties, performance in application, structure/composition, synthesis/processing), but NAP states that its books are copyrighted with all rights reserved and that reuse/distribution requires permission. It is not a rights-cleared replacement source for this workflow.

Rights references:
- https://www.nationalacademies.org/request-rights-and-permissions
- https://www.nationalacademies.org/legal-information

Do not register the NAP chapter as an approved AI-assisted evidence source without permission or a qualifying rights basis.

## 4. Proposed disposition summary

| Claim | Best current source candidate | Content fit | Rights / remaining issue |
|---|---|---|---|
| Maps and Navigation C | USGS accuracy FAQ + Topographic Mapping + map currency FAQ | Strong conceptual fit for accuracy, metadata, updates and field verification | U.S. US Topo context; preserve navigation disclaimer and scope |
| Materials A | NIST Materials Science and Engineering Division | Direct conceptual fit | Verify page-level third-party markings; NIST public-information policy |
| Materials C | NIST Thermodynamics and Kinetics + Mechanical Performance groups | Strong fit for process/structure/performance and operating conditions | Preserve mechanical-property scope |
| Materials Performance D | NIST Mechanical Performance Group | Partial/strong complementary support | Still needs application-specific selection and required-function source |
| Materials Science B | NSF Materials Research + NSF DMREF + NIST Mechanical Performance | Supports named examples and application-design caveat | Preserve overlap/non-exhaustive classification; verify page-specific copyright markings |
| Risk Management B | UK HM Treasury Orange Book | Conceptual fit, but exact definition is ISO-derived | RIGHTS HOLD until ISO-derived passage rights are resolved |

## 5. Next controlled actions

1. Prepare exact bounded authorizations for the NIST/NSF/USGS source additions and versioned Evidence Use records only after the complete list of canonical paths, versions, README changes, coverage updates and regression tests is frozen.
2. For Maps and Navigation C, keep USGS’s explicit “not authoritative for navigation” limitation in the Evidence Use description; do not overstate it as a navigation guarantee.
3. For Materials A/C and Materials Science B, use NIST/NSF sources only within their explicit subject scope and preserve category overlap/non-exhaustiveness.
4. Keep Materials Performance D PARTIAL/HOLD until a second source directly supports application-specific selection and required-function criteria.
5. Keep Risk Management B RIGHTS HOLD; do not use ISO-derived Orange Book Annex 5 wording as a workaround.
6. Re-fetch every canonical record at the then-current HEAD before any authorized write. No batch write is permitted from this report alone.

## 6. Disposition

This report is a noncanonical source-fit and rights review. It grants no canonical write permission and makes no D/E/B, specialist, Human View, publication or release decision.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged; `main` must remain unchanged.


## 7. Manufacturing Systems B/C — NIST sources directly improve the evidence fit

### 7.1 Manufacturing Systems B — measurement, repeatability, quality and performance

Claim: `CLM-MANUFACTURING_SYSTEMS_BASICS-B@1`

Statement: `Современное производство использует измерение и управление процессами для повышения воспроизводимости, качества и эффективности.`

Useful NIST sources:

- **NIST/SEMATECH Engineering Statistics Handbook, Chapter 2 — Measurement Process Characterization** discusses data collection and statistical analyses for characterizing repeatability, reproducibility and stability of measurement processes, controlling measurement processes, calibration, and uncertainty.
  https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-2-measurement-process

- **NIST Smart Manufacturing Systems Test Bed** documents a manufacturing lab with machine tools and inspection equipment, data collection from the manufacturing lab using MTConnect, and the use of the test bed for developing and validating technologies that improve manufacturing process and product performance. It also describes integration of design, fabrication and inspection and the “digital thread” for product design, quality, equipment performance and health.
  https://www.nist.gov/laboratories/tools-instruments/smart-manufacturing-systems-sms-test-bed

- **NIST AMS 200-2, Connecting, Deploying, and Using the Smart Manufacturing Systems Test Bed** describes integration of MTConnect and other standards/technologies to collect, curate and reuse manufacturing data from equipment on the shop floor to improve production-system performance.
  https://www.nist.gov/publications/connecting-deploying-and-using-smart-manufacturing-systems-test-bed

- **NIST Operations-driven Performance Measurement for Smart Manufacturing Systems** describes collecting and analysing operational data to identify performance issues and improve system performance, using system characterization and data analysis to evaluate a system against a norm.
  https://www.nist.gov/programs-projects/operations-driven-performance-measurement-smart-manufacturing-systems

These sources together support measurement/process control, reproducibility of measurement processes, quality/inspection, operational data and performance improvement. The measurement handbook concerns measurement-process repeatability/reproducibility, not a universal guarantee of repeatable manufactured products. Keep that distinction explicit. The NIST test-bed evidence is an example of modern smart-manufacturing practice, not proof that every manufacturer uses the same architecture.

Rights:
- NIST general web-page information is public information except where marked copyrighted; attribution is requested.
- NIST Technical Series policy states that works authored by NIST employees are not subject to copyright protection within the United States and, to the extent NIST asserts rights outside the U.S., the public receives a non-exclusive, perpetual, paid-up, royalty-free, worldwide right to reprint and create derivative works. NIST AMS 200-2 lists Moneer Helu and Thomas Hedberg Jr. as authors from the NIST Systems Integration Division; verify the final publication's author/copyright page before registration.
- NIST technical-series policy: https://www.nist.gov/nist-research-library/nist-publications
- NIST general page rights: https://www.nist.gov/copyrights-disclaimers

Disposition: source fit materially improved. A bounded addition of the NIST source(s) and claim-specific Evidence Use may be prepared after the exact selected source set and locators are frozen. Do not change the Claim wording.

### 7.2 Manufacturing Systems C — integrated digital operations, monitoring and analysis

Claim: `CLM-MANUFACTURING_SYSTEMS_BASICS-C@1`

Statement: `Цифровые технологии и данные могут связывать производственные операции, мониторинг и анализ для поддержки управления производственной системой.`

Useful NIST sources:

- **NIST Smart Manufacturing Systems Test Bed** directly describes manufacturing equipment, inspection equipment, MTConnect data collection, data publication services, and integration across design, fabrication and inspection. It explicitly describes a digital thread for product design and quality, equipment performance and health across the product lifecycle.
  https://www.nist.gov/laboratories/tools-instruments/smart-manufacturing-systems-sms-test-bed

- **NIST AMS 200-2** describes integration of smart-manufacturing standards and technologies to support collecting, curating and reusing manufacturing data.
  https://www.nist.gov/publications/connecting-deploying-and-using-smart-manufacturing-systems-test-bed

- **NIST Systems Analysis Integration for Smart Manufacturing Operations** describes integration of smart-manufacturing system models with engineering-analysis models, addressing redundant and incompatible representations across engineering disciplines.
  https://www.nist.gov/programs-projects/systems-analysis-integration-smart-manufacturing-operations

- **NIST Model-Based Systems Definition and Analysis Integration for Smart Manufacturing** describes unifying domain-specific analysis information and integrating it with systems-model information.
  https://www.nist.gov/programs-projects/model-based-systems-definition-and-analysis-integration-smart-manufacturing

These sources directly support the possibility of linking operational data, monitoring, analysis models and system-level management. Preserve the distinction between a demonstrated NIST test-bed architecture and a universal statement about every production system.

Rights:
- The NIST test-bed page is an official NIST page subject to the NIST public-information policy except for marked third-party material.
- NIST AMS 200-2 is a NIST Technical Series publication. Its authors are identified as NIST staff; apply the NIST Technical Series rights notice and cite the work as requested.
- Project pages are NIST information pages; review page-specific notices and any third-party material before use.

Disposition: source fit materially improved. A bounded addition of the selected NIST Source/Evidence Use records can be prepared after the exact paths, source locators, coverage updates and regression tests are fixed. No canonical write is authorized by this report.

