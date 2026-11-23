# M13 — unassessed-risk content screen, Package 13

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `98e1de42769222d90a6af1ae39791006cc404354`  
Queue artifact: `14144612725` (workflow run `43672614141`, successful)  
Scope: Lane 1, first 20 exact Claim IDs from the refreshed 100-Claim queue.  
State: **desk-level source-fit and risk-routing review. No D/E/B scores, canonical record edits, risk metadata changes, publication changes or specialist approvals.** This package records source-fit findings and follow-up work; it is not an M13 closure decision.

## 1. Queue and identity integrity

The exact queue artifact was downloaded and inspected. It reports 1,494 inventoried Claims, 337 previously screened Claims excluded, 17 unresolved-topic holdouts, 15 overlaps between those exclusion sets, 339 unique exclusions, 372 eligible unassessed candidates, 100 selected Claims, five lanes of 20 and 100 unique selected IDs. The Package 12 twenty Claims are all present in the new previously-screened exclusion list and absent from the selected queue. The separate unresolved holdout count remains 17.

The 20 Claims below are the exact Lane 1 records. Claim→Evidence Use→Source links were assembled in the CI evidence packets from repository records. Many EU descriptions are generic placeholders; a source URI alone is not a passage citation.

| # | Claim | Evidence Use | Source |
|---:|---|---|---|
| 1 | `CLM-GEOMETRY_BASICS-A@1` | `EU-GEOMETRY_BASICS-A@1` | `SRC-GEOMETRY_BASICS@1` |
| 2 | `CLM-GEOMETRY_BASICS-B@1` | `EU-GEOMETRY_BASICS-B@1` | `SRC-GEOMETRY_BASICS@1` |
| 3 | `CLM-GEOMETRY_BASICS-C@1` | `EU-GEOMETRY_BASICS-C@1` | `SRC-GEOMETRY_BASICS@1` |
| 4 | `CLM-GEOMORPHOLOGY_BASICS-A@1` | `EU-GEOMORPHOLOGY_BASICS-A@1` | `SRC-GEOMORPHOLOGY_BASICS@1` |
| 5 | `CLM-GEOMORPHOLOGY_BASICS-B@1` | `EU-GEOMORPHOLOGY_BASICS-B@1` | `SRC-GEOMORPHOLOGY_BASICS@1` |
| 6 | `CLM-GEOMORPHOLOGY_BASICS-C@1` | `EU-GEOMORPHOLOGY_BASICS-C@1` | `SRC-GEOMORPHOLOGY_BASICS@1` |
| 7 | `CLM-GEOSPATIAL_ANALYSIS_BASICS-A@1` | `EU-GEOSPATIAL_ANALYSIS_BASICS-A@1` | `SRC-GEOSPATIAL_ANALYSIS_BASICS@1` |
| 8 | `CLM-GEOSPATIAL_ANALYSIS_BASICS-B@1` | `EU-GEOSPATIAL_ANALYSIS_BASICS-B@1` | `SRC-GEOSPATIAL_ANALYSIS_BASICS@1` |
| 9 | `CLM-GEOSPATIAL_ANALYSIS_BASICS-C@1` | `EU-GEOSPATIAL_ANALYSIS_BASICS-C@1` | `SRC-GEOSPATIAL_ANALYSIS_BASICS@1` |
| 10 | `CLM-HISTORICAL_GEOGRAPHY-A@1` | `EU-HISTORICAL_GEOGRAPHY-A@1` | `SRC-HISTORICAL_GEOGRAPHY@1` |
| 11 | `CLM-HISTORICAL_GEOGRAPHY-B@1` | `EU-HISTORICAL_GEOGRAPHY-B@1` | `SRC-HISTORICAL_GEOGRAPHY@1` |
| 12 | `CLM-HISTORICAL_GEOGRAPHY-C@1` | `EU-HISTORICAL_GEOGRAPHY-C@1` | `SRC-HISTORICAL_GEOGRAPHY@1` |
| 13 | `CLM-HISTORY_OF_ENGINEERING-A@1` | `EU-HISTORY_OF_ENGINEERING-A@1` | `SRC-HISTORY_OF_ENGINEERING@1` |
| 14 | `CLM-HISTORY_OF_ENGINEERING-B@1` | `EU-HISTORY_OF_ENGINEERING-B@1` | `SRC-HISTORY_OF_ENGINEERING@1` |
| 15 | `CLM-HISTORY_OF_ENGINEERING-C@1` | `EU-HISTORY_OF_ENGINEERING-C@1` | `SRC-HISTORY_OF_ENGINEERING@1` |
| 16 | `CLM-HISTORY_OF_MATHEMATICS-A@1` | `EU-HISTORY_OF_MATHEMATICS-A@1` | `SRC-HISTORY_OF_MATHEMATICS@1` |
| 17 | `CLM-HISTORY_OF_MATHEMATICS-B@1` | `EU-HISTORY_OF_MATHEMATICS-B@1` | `SRC-HISTORY_OF_MATHEMATICS@1` |
| 18 | `CLM-HISTORY_OF_MATHEMATICS-C@1` | `EU-HISTORY_OF_MATHEMATICS-C@1` | `SRC-HISTORY_OF_MATHEMATICS@1` |
| 19 | `CLM-HISTORY_OF_SCIENCE-A@1` | `EU-HISTORY_OF_SCIENCE-A@1` | `SRC-HISTORY_OF_SCIENCE@1` |
| 20 | `CLM-HISTORY_OF_SCIENCE-B@1` | `EU-HISTORY_OF_SCIENCE-B@1` | `SRC-HISTORY_OF_SCIENCE@1` |

## 2. Claim-by-Claim source-fit findings

### 2.1 Geometry A — geometric objects and their elements

**Claim:** “Геометрические объекты описываются через точки, линии, углы и фигуры.”

**Registered source:** OpenStax *Precalculus 2e*, `https://openstax.org/books/precalculus-2e/pages/10-introduction`.

**Finding: SOURCE MISMATCH / PARTIAL.** The registered URL resolves to *Precalculus 2e*, “Introduction to Analytic Geometry,” whose chapter concerns conic sections. It is not the basic-geometry chapter needed for this Claim. The correct OpenStax *Contemporary Mathematics* Chapter 10 introduction outlines points, lines, angles, triangles, polygons and area/perimeter; Section 10.1 defines points and lines.

**Follow-up:** Replace the Source identity/URI with the correct *Contemporary Mathematics* chapter and add Section 10.1 plus the angle/polygon sections as pinpoints. Do not retain the current Precalculus URL as support for basic geometry.

### 2.2 Geometry B — perimeter and area

**Claim:** “Периметр характеризует длину границы плоской фигуры, а площадь — размер её области.”

**Finding: SOURCE MISMATCH / PARTIAL.** The currently registered Precalculus URL is not the relevant basic-geometry text. OpenStax *Contemporary Mathematics* Section 10.4 addresses perimeter; Section 10.6 explicitly distinguishes linear units for perimeter from square units for area and describes area as the region within a boundary.

**Follow-up:** Replace the source with *Contemporary Mathematics* Sections 10.4 and 10.6 and add exact locators. The Claim is conceptually sound, but the current Source→EU relation is not.

### 2.3 Geometry C — definitions and units

**Claim:** “Измерительные свойства фигуры зависят от выбранных определений и единиц.”

**Finding: PARTIAL / WORDING NEEDS PRECISION.** OpenStax *Contemporary Mathematics* discusses the definitions of geometric concepts and the use of units; Section 10.6 distinguishes linear and square units. The current registered source points to the wrong book. The Claim also conflates the definition of a quantity with the numerical value obtained under a chosen unit.

**Follow-up:** Rewrite narrowly, for example: “Числовое значение геометрической величины зависит от выбранной единицы измерения, а сама величина определяется соответствующим геометрическим понятием.” Add the correct OpenStax sections.

### 2.4 Geomorphology A — landforms and processes

**Claim:** “Геоморфология относится к наукам о формах земной поверхности и процессах их формирования.”

**Registered source:** USGS Thesaurus.

**Finding: DIRECT CONCEPTUAL SUPPORT.** The USGS Thesaurus defines geomorphology as a branch of geology dealing with surface land features and the processes that create and change them. This closely matches the Claim.

**Follow-up:** Add the exact USGS thesaurus term locator. The full thesaurus endpoint may reject automated retrieval, so preserve a stable direct term URL or a captured public reference.

### 2.5 Geomorphology B — processes changing relief

**Claim:** “Эрозия, выветривание, осаждение и тектонические процессы могут изменять рельеф.”

**Finding: PARTIAL.** The USGS Thesaurus defines erosion, sedimentation and tectonic processes. The British Geological Survey separately defines weathering, erosion, deposition and landforms. The current single USGS Source does not clearly cover all four named processes in one reproducible passage.

**Follow-up:** Add the BGS geological-processes page as a second Source or another authoritative source that explicitly covers weathering. Add pinpoints for erosion, weathering, deposition and tectonics. Avoid treating sedimentation and deposition as interchangeable in every technical context without definition.

### 2.6 Geomorphology C — process and scale of observation

**Claim:** “Форма рельефа должна рассматриваться вместе с действующими процессами и масштабом наблюдения.”

**Finding: PARTIAL / HOLD.** The USGS definition supports the link between landforms and the processes that create/change them. The additional requirement to account for observation scale is not established by the current Source/EU. It is an important methodological point but needs an explicit geomorphology reference on spatial and temporal scale.

**Follow-up:** Add an authoritative geomorphology text or review that discusses scale dependence, process rates and landform observation scales. Until then, do not treat the complete Claim as source-verified.

### 2.7 Geospatial Analysis A — location-linked data and spatial patterns

**Claim:** “Геопространственный анализ использует данные, связанные с местоположением, для изучения пространственных отношений и закономерностей.”

**Registered source:** USGS Geographic Information Systems.

**Finding: DIRECT CONCEPTUAL SUPPORT, LOCATOR/IDENTITY GAP.** The USGS GIS FAQ states that GIS analyzes and displays geographically referenced information attached to a unique location and gives examples of spatial pattern analysis. This directly supports the Claim. The currently registered Source URI is a broad GIS program page rather than the exact FAQ passage.

**Follow-up:** Add the USGS GIS FAQ as a distinct Source or update the Source URI after confirming its intended canonical identity; add pinpoints for the definition and spatial-pattern examples.

### 2.8 Geospatial Analysis B — GIS functions

**Claim:** “Географические информационные системы позволяют хранить, отображать, анализировать и сопоставлять пространственные данные.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** USGS describes GIS as analyzing and displaying geographically referenced data. NOAA's GIS definition explicitly lists capturing, storing, checking and displaying information related to positions on Earth's surface. The current registered USGS page does not by itself establish every verb in the Claim, particularly storage and comparison.

**Follow-up:** Add a distinct NOAA or other authoritative GIS Source for capture/storage/check/display and a precise USGS locator for analysis and spatial relationships. Keep “compare” only if the selected source passage demonstrates that operation.

### 2.9 Geospatial Analysis C — quality, scale, accuracy and provenance

**Claim:** “Результаты геопространственного анализа зависят от качества, масштаба, точности и происхождения исходных пространственных данных.”

**Finding: PARTIAL / HOLD.** The current USGS GIS page explains GIS functions, not all data-quality dimensions. USGS Information Quality Guidelines require documentation of methods, accuracy, precision, metadata and quality assurance. Library of Congress geospatial preservation guidance explains provenance, lineage, scale and accuracy metadata. These are relevant, but they are not currently linked in the registered Source/EU.

**Follow-up:** Add distinct Sources and pinpoints for data quality/accuracy/precision and provenance/lineage/scale. Preserve the distinction between data quality dimensions and the fitness of a dataset for a particular analytical use.

### 2.10 Historical Geography A — maps as spatial information tied to time and place

**Claim:** “Исторические карты являются источниками пространственной информации, связанной с определённым временем и местом.”

**Registered source:** Library of Congress map collections.

**Finding: DIRECT CONCEPTUAL SUPPORT.** The Library of Congress General Maps collection describes maps portraying the physical environment and cultural elements of a geographic area at a particular point in time. This supports the spatial and temporal framing.

**Follow-up:** Add the exact General Maps collection reference and collection-level metadata locator. Distinguish the map's production date from the date of the situation it depicts.

### 2.11 Historical Geography B — physical and cultural elements

**Claim:** “Картографические материалы могут показывать физическую среду и культурные элементы территории в конкретный исторический момент.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** The Library of Congress General Maps collection explicitly describes physical-environment and cultural-element coverage for a geographic area at a particular point in time.

**Follow-up:** Add a pinpoint to the General Maps collection description and one representative map record. Do not infer that every historical map contains both physical and cultural information.

### 2.12 Historical Geography C — date, scale, provenance and purpose

**Claim:** “Интерпретация исторической карты зависит от даты, масштаба, происхождения и назначения материала.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** Library of Congress teaching guidance asks users to compare maps by scale, point of view, detail, date, purpose and uses. LOC cataloging/guide materials also describe date, scale, special collection identifiers, descriptions and known map purpose. The current registered collections landing page is not enough to support provenance and all interpretive factors.

**Follow-up:** Add the LOC map-analysis guidance and a cataloging/metadata reference. Explicitly distinguish date of production from “date of situation” and identify map author/source where available.

### 2.13 History of Engineering A — technologies, artifacts and documentary collections

**Claim:** “История инженерии может изучаться через технологии, изобретения, инженерные артефакты и документальные коллекции.”

**Registered source:** Smithsonian Technology & Innovation.

**Finding: PARTIAL / BROKEN REGISTERED URL.** The registered `https://www.si.edu/explore/technology` URL currently returns 404. Smithsonian sources do establish relevant collections: the Collections Search Center includes science/technology objects and records; Smithsonian Archives hold technical drawings, photographs, letters, field notebooks, manuscripts and other documentary materials.

**Follow-up:** Replace or supplement the broken Source with stable Smithsonian Collections Search Center and Smithsonian Institution Archives records. Add direct collection examples relevant to engineering, not just a general technology topic page.

### 2.14 History of Engineering B — changing subject and organizational boundaries

**Claim:** “Инженерные и технологические коллекции Smithsonian отражают изменения организационных и предметных границ истории науки и технологии.”

**Finding: HOLD / CLAIM NOT ESTABLISHED.** Smithsonian collections cover multiple institutional units and subject areas, but that fact does not demonstrate historical change in the organizational or disciplinary boundaries of the history of science and technology. The current source is also broken.

**Follow-up:** Either rewrite as a narrower factual statement about the breadth and institutional distribution of Smithsonian collections, or provide a historiographical source that explicitly analyzes changing disciplinary/organizational boundaries. Do not infer historical change from a present-day collection taxonomy.

### 2.15 History of Engineering C — historical/material context and causality

**Claim:** “История инженерии связывает технические решения с их историческим и материальным контекстом, но описание такого контекста само по себе не доказывает причинность.”

**Finding: HOLD / METHODOLOGICAL INFERENCE.** The Smithsonian technology portal does not establish the methodological claim about causal inference. The second clause is a rule about reasoning, not a simple descriptive fact that can be verified by an artifact collection.

**Follow-up:** Treat the causal-inference caution as a methodological principle and support it with an explicit historical-methodology or causal-inference reference. If it is intended as an inference, document premises and inference status separately; do not attribute it to the Smithsonian source.

### 2.16 History of Mathematics A — ideas, methods, notation and transmission

**Claim:** “История математики включает развитие математических идей, методов, обозначений и способов их передачи между поколениями.”

**Registered source:** MacTutor History of Mathematics, University of St Andrews.

**Finding: DIRECT CONCEPTUAL SUPPORT.** The overview traces mathematical ideas and methods across historical periods and explicitly discusses notation and communication. It describes how Babylonian mathematical knowledge was inherited by the Greeks and how mathematical knowledge moved through Islamic scholarship into Europe.

**Follow-up:** Add pinpoints to the historical overview and its “Notation and communication” section. Avoid presenting the overview as exhaustive global coverage.

### 2.17 History of Mathematics B — multiple cultural and historical contexts

**Claim:** “Развитие математики происходило в разных культурных и исторических контекстах, включая Вавилонию, Грецию, исламский мир, Индию, Китай и Европу.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** MacTutor's overview discusses Babylonia, Greece, Islamic countries, Iran, Syria, India and Europe. The MacTutor topic index separately lists Ancient Chinese Mathematics. The current registered overview alone does not support the full enumerated set, particularly China.

**Follow-up:** Add the MacTutor topic index and the dedicated Chinese mathematics page as a separate Source/Evidence Use. Ensure the Claim does not imply that the listed cultures are exhaustive or that development was a single linear transfer.

### 2.18 History of Mathematics C — long development beyond a single discovery date

**Claim:** “Современные математические идеи часто имеют более длинную историю развития, чем позволяет предположить привязка открытия к одному автору или дате.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** MacTutor's “Brilliant discoveries?” section explicitly notes that major discoveries often culminate from work by many mathematicians over long periods and illustrates this with the development of calculus before Newton and Leibniz.

**Follow-up:** Add the exact “Brilliant discoveries?” locator. Preserve “often” rather than universalizing the point to every mathematical idea.

### 2.19 History of Science A — development of scientific fields, ideas and practices

**Claim:** “История науки исследует развитие научных областей, источников, идей и практик во времени.”

**Registered source:** Smithsonian Libraries and Archives — History of Science and Technology Research Guide.

**Finding: PARTIAL / RELEVANT RESEARCH GUIDE, NOT A FORMAL DEFINITION.** The guide presents resources for research in the history of science and technology and includes catalogs, historical books, collections, archives and named research projects. It is relevant to the study of the field but does not itself provide a formal definition of the discipline.

**Follow-up:** Add the Smithsonian guide as a research-resource source, plus a scholarly introduction to the history of science for the definitional wording. The guide is accessible in search results but automated page retrieval returned a service rejection; retain an alternate stable Smithsonian Archives/Collections reference if needed.

### 2.20 History of Science B — documentary and archival source types

**Claim:** “Историческое изучение науки использует книги, архивы, биографические материалы и другие источники, относящиеся к определённым периодам и областям.”

**Finding: DIRECT CONCEPTUAL SUPPORT, SOURCE CHAIN NEEDS REPAIR.** The Smithsonian guide lists library catalogs, early scientific books, collections, biographical resources, manuscripts and archives. Smithsonian Archives also describes official records, personal papers, special collections and oral/video histories. This supports the source types used in historical research.

**Follow-up:** Replace the current inaccessible guide-only chain with stable Smithsonian Archives and Collections Search Center sources; add one or more precise examples and pinpoints. Avoid suggesting that the listed source types are exhaustive.

## 3. Cross-cutting findings and remediation

1. **One material source mismatch:** the Geometry Source points to OpenStax *Precalculus 2e* analytic geometry, while the Claims require the basic-geometry chapter in *Contemporary Mathematics*. Correct the book identity and URL before treating those Claims as supported.
2. **One broken registered URL:** Smithsonian Technology & Innovation (`si.edu/explore/technology`) returns 404. Replace it with stable Smithsonian Archives and Collections Search Center records.
3. **Generic EU text is not evidence.** Most EU records state only that a source is used to represent the Claim. Each needs a concise source-specific description and a reproducible pinpoint.
4. **Several Claims are broader than their registered Sources:** geomorphology scale, geospatial data quality/provenance, historical-map provenance, Smithsonian disciplinary-boundary change and engineering causality all need further evidence or narrower wording.
5. **Inference must remain distinct from source fact.** History of Engineering C includes a methodological causal-inference rule; document its inference status rather than presenting it as a fact stated by a museum source.
6. **Source independence is not established by multiple URLs alone.** Smithsonian collections and archives may be different catalogs within one institution; MacTutor overview and topic index are part of one archive. Record source relationships accurately.
7. **No D/E/B score is assigned.** Source-fit labels above are descriptive triage findings, not M13 assessment grades.
8. **No canonical Claim, EU or Source record was edited.** No risk metadata, publication status, rights status or specialist approval was changed.

## 4. Disposition

- 20/20 Claims inspected at desk level against their registered Claim/EU/Source packet.
- 6 Claims have direct conceptual support, subject to exact locator and source-chain remediation.
- 12 Claims remain partial or require additional/narrower source support.
- 2 Claims remain on HOLD because their methodological/historiographical content is not established by the registered source.
- 20/20 remain unclosed for M13; no D/E/B score or specialist approval is inferred.
- Next work: repair the geometry and Smithsonian Source identities, add precise EU locators for the direct cases, source the partial cases, and keep the two HOLD Claims open pending methodological/historiographical evidence.

**Package 13 is a source-fit checkpoint, not a closure certificate. HOLD remains in force.**
