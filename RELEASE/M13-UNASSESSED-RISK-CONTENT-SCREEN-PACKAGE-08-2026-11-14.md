# M13 — unassessed-risk content screen, Package 08

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue basis: 711-row unassessed-risk inventory, source revision `f26820e59b08b4036ad78302dad8118c51dac540`  
Queue workflow artifact: `14128675169` (run `43631545843`, successful on generator revision `64517d688d4ea6bdc5bfc2e291014ab904989605`)  
Scope: 20 exact Claim IDs selected in the deduplicated 100-Claim queue and screened at desk level.  
State: **risk routing and source-fit triage only; no risk metadata, D/E/B scores, canonical records or publication state changed.**

## 1. Selection integrity and method

The queue generator previously returned 0 selected Claims because it excluded records already present in the D/E/B score ledger. That conflated evidence scoring with risk screening. The pipeline was corrected so that:
- risk-UNASSESSED state, not absence from the D/E/B ledger, determines candidate eligibility;
- exact previously screened Claim IDs are collected from prior M13 risk-screen reports, including compact grouped IDs such as `CLM-X-A/B/C`;
- the 14 unreconciled historical observations are protected by holding their topic families out of the new queue;
- selection remains deterministic, duplicate-free and divided into five equal lanes.

The successful queue artifact reports:
- 1,494 Claims inventoried;
- 711 Claims without recorded risk metadata;
- 236 previously screened exact IDs excluded;
- 17 claims in unresolved-observation holdout slices, 15 of which overlap the 236 reviewed IDs;
- 238 unique unassessed Claims excluded by the union of those two sets;
- 473 remaining eligible candidates;
- 100 selected, 0 unfilled, 100 unique Claim IDs, 20 per lane;
- 100 evidence packets generated.

All 20 Claims in this package are present in that exact 100-ID queue. They are outside the explicit prior-screen ID set and outside the holdout topic families. The 14 historical observations remain unnamed, so no cumulative unique-coverage total is claimed.

For these 20 records, Claim, Evidence Use and Source JSON records were inspected. The three Web Systems EUs are version 2 and already contain MDN section-level descriptions; the other 17 EUs are version 1 and remain generic/source-level without reproducible passage locators. All 20 Claim→EU→Source reference chains resolve and match.

## 2. Exact records reviewed

| Claim | Evidence Use | Source | Slice |
|---|---|---|---|
| `CLM-WEB_SYSTEMS_BASICS-A@1` | `EU-WEB_SYSTEMS_BASICS-A@2` | `SRC-WEB_SYSTEMS_BASICS@1` | web-systems-basics |
| `CLM-WEB_SYSTEMS_BASICS-B@1` | `EU-WEB_SYSTEMS_BASICS-B@2` | `SRC-WEB_SYSTEMS_BASICS@1` | web-systems-basics |
| `CLM-WEB_SYSTEMS_BASICS-C@1` | `EU-WEB_SYSTEMS_BASICS-C@2` | `SRC-WEB_SYSTEMS_BASICS@1` | web-systems-basics |
| `CLM-CLIMATE_ADAPTATION-A@1` | `EU-CLIMATE_ADAPTATION-A@1` | `SRC-CLIMATE_ADAPTATION@1` | climate-adaptation-basics |
| `CLM-CLIMATE_ADAPTATION-B@1` | `EU-CLIMATE_ADAPTATION-B@1` | `SRC-CLIMATE_ADAPTATION@1` | climate-adaptation-basics |
| `CLM-CLIMATE_ADAPTATION-C@1` | `EU-CLIMATE_ADAPTATION-C@1` | `SRC-CLIMATE_ADAPTATION@1` | climate-adaptation-basics |
| `CLM-CLIMATE_BASICS-A@1` | `EU-CLIMATE_BASICS-A@1` | `SRC-CLIMATE_BASICS@1` | climate-basics |
| `CLM-CLIMATE_BASICS-B@1` | `EU-CLIMATE_BASICS-B@1` | `SRC-CLIMATE_BASICS@1` | climate-basics |
| `CLM-CLIMATE_BASICS-C@1` | `EU-CLIMATE_BASICS-C@1` | `SRC-CLIMATE_BASICS@1` | climate-basics |
| `CLM-CLOUD_COMPUTING_BASICS-A@1` | `EU-CLOUD_COMPUTING_BASICS-A@1` | `SRC-CLOUD_COMPUTING_BASICS@1` | cloud-computing-basics |
| `CLM-CLOUD_COMPUTING_BASICS-C@1` | `EU-CLOUD_COMPUTING_BASICS-C@1` | `SRC-CLOUD_COMPUTING_BASICS@1` | cloud-computing-basics |
| `CLM-COMBINATORICS_BASICS-C@1` | `EU-COMBINATORICS_BASICS-C@1` | `SRC-COMBINATORICS_BASICS@1` | combinatorics-basics |
| `CLM-COMMUNICATION_BASICS-A@1` | `EU-COMMUNICATION_BASICS-A@1` | `SRC-COMMUNICATION_BASICS@1` | communication-basics |
| `CLM-COMMUNICATION_BASICS-B@1` | `EU-COMMUNICATION_BASICS-B@1` | `SRC-COMMUNICATION_BASICS@1` | communication-basics |
| `CLM-COMMUNICATION_BASICS-C@1` | `EU-COMMUNICATION_BASICS-C@1` | `SRC-COMMUNICATION_BASICS@1` | communication-basics |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-B@1` | `EU-COMPARATIVE_CIVILIZATIONS_BASICS-B@1` | `SRC-COMPARATIVE_CIVILIZATIONS_BASICS@1` | comparative-civilizations-basics |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-C@1` | `EU-COMPARATIVE_CIVILIZATIONS_BASICS-C@1` | `SRC-COMPARATIVE_CIVILIZATIONS_BASICS@1` | comparative-civilizations-basics |
| `CLM-COMPUTER_ARCHITECTURE_BASICS-A@1` | `EU-COMPUTER_ARCHITECTURE_BASICS-A@1` | `SRC-COMPUTER_ARCHITECTURE_BASICS@1` | computer-architecture-basics |
| `CLM-COMPUTER_ARCHITECTURE_BASICS-B@1` | `EU-COMPUTER_ARCHITECTURE_BASICS-B@1` | `SRC-COMPUTER_ARCHITECTURE_BASICS@1` | computer-architecture-basics |
| `CLM-COMPUTER_ARCHITECTURE_BASICS-C@1` | `EU-COMPUTER_ARCHITECTURE_BASICS-C@1` | `SRC-COMPUTER_ARCHITECTURE_BASICS@1` | computer-architecture-basics |

## 3. Claim-by-Claim findings

### 3.1 Web Systems A — client/server, protocols and resources

**Claim:** “Веб-система связывает клиентов и серверы, использует сетевые протоколы и ресурсы, а браузер получает и обрабатывает представления ресурсов.”

**Registered Source:** MDN, *How the Web Works*: https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works

**Finding: DIRECT CONCEPTUAL SUPPORT; EU v2 HAS PINPOINTS.** MDN sections “Clients and servers” and “The other parts of the toolbox” describe client/server roles, network protocols, DNS, HTTP, website files and browser receipt/assembly of resources. The EU correctly limits the source to a high-level model and does not claim that the page fully describes browser rendering.

**Risk route: MODERATE.** Foundational networking knowledge can underpin later operational or security advice, but this Claim itself is descriptive. Do not infer secure configuration or complete protocol behaviour from this overview.

**Disposition: ROUTING REVIEW COMPLETE; keep UNASSESSED until formal risk scoring.** Evidence locator quality is materially better than the generic-EU pattern in the other records.

### 3.2 Web Systems B — HTTP is not limited to HTML

**Claim:** “HTTP является протоколом прикладного уровня для обмена запросами и ответами между клиентом и сервером и используется не только для HTML.”

**Finding: DIRECT.** MDN “HTTP basics” describes HTTP as an application protocol and the request/response exchange; it distinguishes HTML, CSS and JavaScript code from other assets and documents. MDN's dedicated HTTP overview also explicitly describes HTTP as a client-server protocol for fetching resources beyond HTML documents: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview.

**Risk route: MODERATE.** Descriptive protocol statement. Do not turn it into a claim that HTTP is secure by itself or that every HTTP deployment uses the same transport/security configuration.

**Disposition: ROUTING REVIEW COMPLETE; EU v2 pinpoint retained; formal risk scoring still required.**

### 3.3 Web Systems C — DNS name resolution

**Claim:** “DNS помогает сопоставлять доменные имена с сетевыми адресами, после чего клиент может установить необходимое сетевое взаимодействие с сервером.”

**Finding: DIRECT.** MDN section “DNS explained” and step 1 of “So what happens, exactly?” state that DNS maps a website name to an IP address so the browser can direct HTTP messages to the relevant server. The EU correctly notes that DNS resolution alone does not guarantee successful connection or server availability.

**Risk route: MODERATE.** Avoid implying DNS is a complete identity/authentication or security mechanism.

**Disposition: ROUTING REVIEW COMPLETE; EU v2 pinpoint retained; formal risk scoring still required.**

### 3.4 Climate Adaptation A — hazard, exposure and vulnerability

**Claim:** “Климатические риски связаны с взаимодействием опасных явлений, экспозиции и уязвимости.”

**Registered Source:** IPCC AR6 WGII: https://www.ipcc.ch/report/ar6/wg2/

**Finding: DIRECT CONCEPTUAL SUPPORT.** IPCC AR6 WGII Technical Summary, including Figure TS.AII.2 and its discussion of risk determinants, describes climate risk as arising from the interaction of changing hazards with exposure, vulnerability and adaptation conditions. It explicitly warns against treating hazard alone as the whole risk.

**Risk route: ELEVATED — climate policy/adaptation decisions.** The Claim is foundational, but it can inform consequential planning and public policy. Do not treat the three components as a complete universal risk equation or infer quantitative risk without context and data.

**Disposition: HOLD pending a precise Technical Summary locator and climate-risk specialist review.**

### 3.5 Climate Adaptation B — adaptation is context-dependent

**Claim:** “Адаптация рассматривается в контексте конкретных климатических воздействий, систем и условий.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** IPCC WGII assesses adaptation in relation to specific climate impacts, exposed systems, vulnerabilities, governance and regional conditions. The generic EU description does not identify the relevant chapter or section.

**Risk route: ELEVATED.** A context-free adaptation measure can be ineffective or maladaptive. Preserve regional, sectoral, social and temporal boundaries.

**Disposition: HOLD pending chapter/section pinpoint and specialist review.**

### 3.6 Climate Adaptation C — limits and residual risk

**Claim:** “Адаптационные меры имеют контекстные ограничения, а их эффекты и остаточные риски требуют отдельной оценки.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** IPCC WGII explicitly assesses limits to adaptation, adaptation effectiveness, and risks that remain after adaptation. The exact Claim wording is a synthesis of these concepts rather than a verbatim IPCC definition; the EU currently points only to the report landing page.

**Risk route: ELEVATED.** The statement can affect public infrastructure, livelihoods and climate adaptation choices. Avoid presenting any measure as eliminating risk.

**Disposition: HOLD pending exact section/figure locators and specialist review.**

### 3.7 Climate Basics A — climate as long-term characteristics

**Claim:** “Климат описывает долгосрочные характеристики и изменения погодных условий в системе Земли.”

**Registered Source:** NASA, *Climate Change*: https://science.nasa.gov/climate-change/

**Finding: DIRECT CONCEPTUAL SUPPORT.** NASA's “What Is Climate Change?” defines climate change as long-term change in average weather patterns that define Earth's local, regional and global climates. This supports the central long-term framing. The registered Source/EU should point to the exact NASA page, not only the topic landing page.

**Risk route: LOW direct consequence.** Foundational educational statement.

**Disposition: HOLD pending exact NASA subsection locator.**

### 3.8 Climate Basics B — observations, measurements and models

**Claim:** “Климатические выводы опираются на наблюдения, измерения и модели, рассматриваемые на длительных временных масштабах.”

**Finding: DIRECT.** NASA states that scientists use observations from the ground, air and space, together with computer models, to monitor and study past, present and future climate change. The source directly supports the methods in the Claim, but the current EU is generic.

**Risk route: LOW direct consequence.** Preserve the distinction between observations, model outputs and inferences; a model is not itself an observation.

**Disposition: HOLD pending a pinpoint to the NASA methods passage and an explicit evidence-type boundary.**

### 3.9 Climate Basics C — weather and climate timescales

**Claim:** “Климат и отдельная погода относятся к разным временным масштабам, поэтому единичное погодное событие само по себе не описывает весь климат.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** NASA's “What's the difference between weather and climate?” distinguishes local short-term weather conditions from climate averages over several decades. NOAA independently explains that individual weather days and short-term swings do not by themselves establish long-term climate patterns: https://www.noaa.gov/explainers/what-s-difference-between-climate-and-weather.

**Risk route: LOW direct consequence.** Educational epistemic boundary; avoid using it to dismiss an event's relevance to climate attribution, which requires separate analysis.

**Disposition: HOLD pending exact NASA FAQ locator and clear distinction between event description and attribution analysis.**

### 3.10 Cloud Computing A — shared configurable resource pool

**Claim:** “Облачная модель предоставляет сетевой доступ к общему пулу конфигурируемых вычислительных ресурсов.”

**Registered Source:** NIST SP 800-145: https://www.nist.gov/publications/nist-definition-cloud-computing

**Finding: DIRECT.** NIST SP 800-145 defines cloud computing in substantially the same terms: network access to a shared pool of configurable computing resources that can be provisioned and released. The NIST publication page provides a stable official identity and abstract.

**Risk route: MODERATE.** This definition does not certify security, availability, privacy, sovereignty, resilience or suitability of any particular cloud service.

**Disposition: HOLD pending exact NIST SP 800-145 abstract/section locator and an explicit non-certification boundary.**

### 3.11 Cloud Computing C — provider/user responsibility

**Claim:** “Облачные сервисы различаются моделью предоставления и уровнем ответственности поставщика и пользователя.”

**Finding: PARTIAL.** NIST SP 800-145 distinguishes service models (SaaS, PaaS, IaaS) and deployment models. That supports variation in service arrangements. The registered source does not by itself fully establish how responsibility is divided between provider and customer for particular controls, data, security or operations.

**Risk route: MODERATE.** Incorrect responsibility assumptions can create security, privacy, continuity and compliance gaps.

**Disposition: HOLD.** Add a separately versioned shared-responsibility source (with model-specific scope) rather than implying NIST SP 800-145 establishes every provider/customer control boundary.

### 3.12 Combinatorics C — sum and product counting rules

**Claim:** “Правила суммы и произведения позволяют разлагать конечные задачи подсчёта на простые случаи.”

**Registered Source:** Wolfram MathWorld, *Combinatorics*: https://mathworld.wolfram.com/Combinatorics.html

**Finding: PARTIAL.** The registered MathWorld page defines combinatorics and enumerative combinatorics, including counting finite sets. It does not state the sum and multiplication principles. MathWorld's separate *Multiplication Principle* page directly supports the product rule: https://mathworld.wolfram.com/MultiplicationPrinciple.html. A separate direct source is still needed for the sum rule and for the combined formulation.

**Risk route: LOW direct consequence.** Foundational mathematics. Preserve conditions such as disjoint cases for the sum rule and correctly defined sequential choices for the product rule.

**Disposition: HOLD pending a distinct Source/EU for the sum rule and exact locator for the multiplication principle.**

### 3.13 Communication A — goal, content, format and audience

**Claim:** “Эффективная коммуникация — это передача и обсуждение информации с учётом цели, содержания, формата и характеристик аудитории; выбор сообщения и канала зависит от задачи и получателя.”

**Registered Source:** National Academies, *Communicating Science Effectively: A Research Agenda*, Chapter 2: https://www.nationalacademies.org/read/23674/chapter/4

**Finding: DIRECT CONCEPTUAL SUPPORT.** Chapter 2 states that science communication depends on goals, content, format, individuals and organizations, and that communication involves communicators, audiences and channels in a social context. This supports the Claim's multi-factor model. The Claim is about communication generally, while the source is specifically science communication.

**Risk route: MODERATE.** Communication choices can affect public understanding of health, environment and policy. Do not universalize findings from science communication to every interpersonal or organizational setting without qualification.

**Disposition: HOLD pending a pinpoint and an explicit science-communication scope note.**

### 3.14 Communication B — prior knowledge, expectations and values

**Claim:** “Коммуникационный контекст включает исходные знания, ожидания и ценности участников; поэтому одинаковая формулировка может давать разное понимание у разных аудиторий, но это не делает любое толкование равно исходному смыслу.”

**Finding: PARTIAL.** National Academies Chapter 2 describes starting points shaped by expectations, knowledge, skills, beliefs and values, and Chapter 1 describes differences in audience prior knowledge and ways of interpreting information. This supports the first part. The normative/semantic boundary that not every interpretation is equally faithful to the original meaning is not directly established by these passages.

**Risk route: MODERATE.** Preserve the distinction between audience variation and the evidential/semantic validity of an interpretation.

**Disposition: HOLD.** Either add a separate source for interpretation/meaning fidelity or narrow the Claim to what the National Academies report directly supports.

### 3.15 Communication C — accessibility without loss of accuracy

**Claim:** “Качество коммуникации оценивают относительно задачи и аудитории: упрощение терминов может повысить доступность, но не гарантирует корректного понимания и не должно удалять существенную точность.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** National Academies Chapter 2 says effective science communication is more complex than simply translating scientific jargon into accessible language and identifies goals, content, format and audience needs as interacting factors. This supports the warning against equating simplification with successful understanding. The final normative clause about preserving essential precision is a reasonable editorial principle but needs a more direct passage or a clearly marked inference.

**Risk route: MODERATE.** Poor simplification can mislead, particularly in science and public-health communication.

**Disposition: HOLD pending exact locator and an explicit distinction between source-supported findings and editorial inference.**

### 3.16 Comparative Civilizations B — contacts and mutual influence

**Claim:** “История цивилизаций требует учитывать контакты, обмены и взаимное влияние между различными обществами.”

**Registered Source:** UNESCO Multimedia Archives, *History of Civilizations of Central Asia*: https://www.unesco.org/archives/multimedia/document-1595

**Finding: PARTIAL.** The registered UNESCO archive page identifies a multi-volume history of Central Asian civilizations and includes a volume titled “The crossroads of civilizations.” It establishes broad historical coverage but does not, at the page level, directly prove the Claim's methodological proposition about contacts and mutual influence. UNESCO's Silk Roads Programme separately documents long-standing commercial, cultural and scientific exchanges, but that is a different Source and must not be silently substituted: https://www.unesco.org/en/silkroads/about-programme.

**Risk route: LOW direct consequence.** Historiographic framing; avoid presenting “civilization” as a single fixed or homogeneous unit.

**Disposition: HOLD.** Add a separate versioned UNESCO Silk Roads Source/EU or a specific volume/page locator that directly supports interaction and exchange.

### 3.17 Comparative Civilizations C — sequence is not proven causality

**Claim:** “Историческое сравнение должно различать наблюдаемую последовательность событий и доказанную причинность.”

**Finding: NOT ESTABLISHED BY REGISTERED SOURCE.** The UNESCO archive landing page identifies the subject and volume structure but does not provide a methodological passage about causal inference in historical comparison. The Claim needs a historiography/methods source on causal explanation and comparative historical analysis.

**Risk route: LOW direct consequence, MODERATE epistemic importance.** This is a useful methodological safeguard, but it should not be presented as a universal formal test of causality without a defined method.

**Disposition: HOLD.** Add a directly relevant historical-methods Source/EU; do not infer the rule from a multi-volume history title.

### 3.18 Computer Architecture A — processor, memory and I/O

**Claim:** “Процессор выполняет инструкции и взаимодействует с памятью и устройствами ввода-вывода.”

**Registered Source:** NIST Information Technology Laboratory: https://www.nist.gov/itl

**Finding: NOT ESTABLISHED BY REGISTERED SOURCE.** The NIST ITL landing page describes the laboratory's mission and divisions; it does not define processor instruction execution or CPU/memory/I/O interaction. Educational and university materials can support the Claim, but they are not the registered Source and must be proposed separately.

**Risk route: MODERATE.** Foundational computing concepts can underpin later system design and security guidance; the present Claim is descriptive.

**Disposition: HOLD.** Replace or supplement the Source with a specific computer-architecture textbook or university resource and record the exact chapter/figure.

### 3.19 Computer Architecture B — memory and storage

**Claim:** “Память и хранилище выполняют разные функции в компьютерной системе.”

**Finding: NOT ESTABLISHED BY REGISTERED SOURCE.** The NIST ITL homepage does not support the memory/storage distinction. This is a standard computing concept, but correctness cannot be certified from the registered Source URI.

**Risk route: MODERATE.** Avoid conflating volatile main memory, persistent storage, caches and other storage hierarchies.

**Disposition: HOLD.** Add a specific architecture source and pinpoint that distinguishes memory hierarchy and persistent storage.

### 3.20 Computer Architecture C — component interaction principles

**Claim:** “Архитектура определяет принципы взаимодействия компонентов для выполнения программ.”

**Finding: NOT ESTABLISHED BY REGISTERED SOURCE.** The registered NIST ITL landing page is too broad to support this definition. A dedicated computer-architecture source is required.

**Risk route: MODERATE.** The Claim is broad and could be mistaken for a complete architecture definition; preserve the distinction between instruction-set architecture, microarchitecture and system organization.

**Disposition: HOLD.** Replace or supplement the registered Source through a separately versioned Source/EU proposal.

## 4. Consolidated routing

| Claims | Passage fit | Risk route | Main issue |
|---|---|---|---|
| Web Systems A/B/C | Direct; EUs v2 contain section locators | Moderate | Preserve high-level scope; no security inference |
| Climate Adaptation A/B/C | Direct conceptual support | Elevated | IPCC chapter/figure pinpoints and specialist review |
| Climate Basics A/B/C | Direct conceptual support | Low | NASA exact-page locators; distinguish observations/models/events |
| Cloud Computing A | Direct | Moderate | NIST SP 800-145 pinpoint; no security certification |
| Cloud Computing C | Partial | Moderate | Shared-responsibility boundaries need another source |
| Combinatorics C | Partial | Low | Registered page lacks sum/product rule passages |
| Communication A | Direct conceptual support | Moderate | Source is specifically science communication |
| Communication B/C | Partial | Moderate | Interpretive and normative clauses need additional evidence |
| Comparative Civilizations B | Partial | Low | Registered source is broad; separate UNESCO exchange source |
| Comparative Civilizations C | Not established | Low / epistemic | Needs historical-methods source |
| Computer Architecture A/B/C | Not established | Moderate | Registered NIST ITL homepage is not a computer-architecture source |

Counts:
- Direct conceptual support: **11**.
- Partial support: **5**.
- Not established by registered Source: **4**.
- Elevated routing: **3**.
- Moderate routing: **11**.
- Low direct-consequence routing: **6**.

These are desk-level evidence-fit and routing labels only. They are not final risk classes or D/E/B scores.

## 5. Integrity

- Exact Claim IDs screened: **20**.
- Claim records inspected: **20**.
- Evidence Use records inspected: **20**.
- Source records inspected: **8**.
- Claim→EU→Source exact identity/version chains resolving: **20/20**.
- EUs with current section-level locator: **3** (Web Systems A/B/C, v2).
- Generic/source-level EUs without reproducible pinpoint: **17**.
- Canonical Claim/EU/Source JSON changes: **0**.
- Risk metadata assigned or changed: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Specialist approvals: **0**.
- Rights/reuse permissions assessed or granted: **0**.
- Publication/Human View approval: **0**.

National Academies content is a copyrighted publication; no reuse or AI-ingestion permission is asserted. The same applies to all other sources unless separately verified under the relevant rights terms. Citation or public accessibility alone is not reuse permission.

## 6. Required next work

1. Continue the deduplicated 100-Claim queue in five 20-record lanes; preserve exact ID/version, reviewer and disposition for every Claim.
2. Resolve the 14 unnamed historical observations if original notes/artifacts can be recovered; otherwise keep the unreconciled holdout register and never report them as unique IDs.
3. Prepare bounded Source/EU proposals for Climate Adaptation, Climate Basics, Cloud Computing C, Combinatorics C, Communication B/C, Comparative Civilizations B/C and Computer Architecture A/B/C.
4. Route Climate Adaptation to climate-risk specialists; Computer Architecture to a computing specialist; Communication B/C to a science-communication/methodology reviewer.
5. Keep all 20 Claims UNASSESSED/HOLD until the formal risk protocol, rights review and authorized metadata process are completed.

This package is not a final risk classification, technical/safety certification, legal opinion, source-rights clearance, canonical correction, independent peer review or M13 closure.
