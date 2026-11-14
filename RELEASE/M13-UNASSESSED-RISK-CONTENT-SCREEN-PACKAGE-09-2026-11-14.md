# M13 — unassessed-risk content screen, Package 09

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue artifact: `14128127821` (workflow run `43631735557`, successful on revision `4670eadb158a8a124ba7d269fe4e1f51fee9607b`)  
Scope: the next 20 exact Claim IDs from Lane 1 of the refreshed deduplicated 100-Claim queue.  
State: **risk routing and source-fit triage only; no risk metadata, D/E/B scores, canonical records or publication state changed.**

## 1. Selection and record integrity

This is the next deterministic 20-Claim lane after Package 08. The latest queue artifact reports 711 Claims with no risk metadata; 256 previously screened explicit IDs excluded; 17 Claims held out by unresolved-observation topic family; 15 Claims overlap both exclusion sets; 258 unique Claims excluded; 453 eligible candidates; 100 selected; 0 unfilled slots; five lanes of 20; 100 evidence packets.

The 20 Claims below are the exact first lane of that artifact. All 20 Claim v1, Evidence Use v1 and Source v1 records were fetched and their IDs/version references checked. All 20 Evidence Use descriptions are generic or broad, without a reproducible Claim-specific passage locator. No canonical records were changed.

The 14 historical observations whose IDs were not recorded remain unreconciled; the queue generator holds their topic families out. No aggregate unique-coverage claim is made beyond the explicit ledger.

## 2. Exact records reviewed

| Claim | Evidence Use | Source | Slice |
|---|---|---|---|
| `CLM-COMPUTER_GRAPHICS_BASICS-A@1` | `EU-COMPUTER_GRAPHICS_BASICS-A@1` | `SRC-COMPUTER_GRAPHICS_BASICS@1` | computer-graphics-basics |
| `CLM-COMPUTER_GRAPHICS_BASICS-B@1` | `EU-COMPUTER_GRAPHICS_BASICS-B@1` | `SRC-COMPUTER_GRAPHICS_BASICS@1` | computer-graphics-basics |
| `CLM-COMPUTER_GRAPHICS_BASICS-C@1` | `EU-COMPUTER_GRAPHICS_BASICS-C@1` | `SRC-COMPUTER_GRAPHICS_BASICS@1` | computer-graphics-basics |
| `CLM-CONSERVATION_BIOLOGY_BASICS-A@1` | `EU-CONSERVATION_BIOLOGY_BASICS-A@1` | `SRC-CONSERVATION_BIOLOGY_BASICS@1` | conservation-biology-basics |
| `CLM-CONSERVATION_BIOLOGY_BASICS-B@1` | `EU-CONSERVATION_BIOLOGY_BASICS-B@1` | `SRC-CONSERVATION_BIOLOGY_BASICS@1` | conservation-biology-basics |
| `CLM-CONSTRUCTION_BASICS-B@1` | `EU-CONSTRUCTION_BASICS-B@1` | `SRC-CONSTRUCTION_BASICS@1` | construction-basics |
| `CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-B@1` | `EU-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-B@1` | `SRC-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS@1` | construction-project-management-basics |
| `CLM-CRITICAL_THINKING_BASICS-D@1` | `EU-CRITICAL_THINKING_BASICS-D@1` | `SRC-ACRL-CRITICAL-INQUIRY-2026@1` | critical-thinking-basics |
| `CLM-CRYPTOGRAPHY_BASICS-B@1` | `EU-CRYPTOGRAPHY_BASICS-B@1` | `SRC-CRYPTOGRAPHY_BASICS@1` | cryptography-basics |
| `CLM-CULTURAL_ANTHROPOLOGY-A@1` | `EU-CULTURAL_ANTHROPOLOGY-A@1` | `SRC-CULTURAL_ANTHROPOLOGY@1` | cultural-anthropology-basics |
| `CLM-CULTURAL_ANTHROPOLOGY-B@1` | `EU-CULTURAL_ANTHROPOLOGY-B@1` | `SRC-CULTURAL_ANTHROPOLOGY@1` | cultural-anthropology-basics |
| `CLM-CULTURAL_ANTHROPOLOGY-C@1` | `EU-CULTURAL_ANTHROPOLOGY-C@1` | `SRC-CULTURAL_ANTHROPOLOGY@1` | cultural-anthropology-basics |
| `CLM-CULTURAL_HERITAGE-A@1` | `EU-CULTURAL_HERITAGE-A@1` | `SRC-CULTURAL_HERITAGE@1` | cultural-heritage-basics |
| `CLM-CULTURAL_HERITAGE-B@1` | `EU-CULTURAL_HERITAGE-B@1` | `SRC-CULTURAL_HERITAGE@1` | cultural-heritage-basics |
| `CLM-CULTURAL_HERITAGE-C@1` | `EU-CULTURAL_HERITAGE-C@1` | `SRC-CULTURAL_HERITAGE@1` | cultural-heritage-basics |
| `CLM-CYBERSECURITY_BASICS-A@1` | `EU-CYBERSECURITY_BASICS-A@1` | `SRC-CYBERSECURITY_BASICS@1` | cybersecurity-basics |
| `CLM-CYBERSECURITY_BASICS-B@1` | `EU-CYBERSECURITY_BASICS-B@1` | `SRC-CYBERSECURITY_BASICS@1` | cybersecurity-basics |
| `CLM-DATA_ETHICS_BASICS-B@1` | `EU-DATA_ETHICS_BASICS-B@1` | `SRC-DATA_ETHICS_BASICS@1` | data-ethics-basics |
| `CLM-DATABASES_BASICS-A@1` | `EU-DATABASES_BASICS-A@1` | `SRC-DATABASES_BASICS@1` | databases-basics |
| `CLM-DATABASES_BASICS-B@1` | `EU-DATABASES_BASICS-B@1` | `SRC-DATABASES_BASICS@1` | databases-basics |

## 3. Claim-by-Claim findings

### 3.1 Computer Graphics A — data, computation and graphics APIs

**Claim:** “Компьютерная графика использует данные, вычисления и графические API для формирования изображений.”

**Registered Source:** Khronos OpenGL: https://www.khronos.org/opengl/

**Finding: DIRECT CONCEPTUAL SUPPORT.** Khronos describes OpenGL as a cross-platform API for rendering 2D/3D graphics and exposes graphics-hardware features to applications. This supports the role of graphics APIs and computation in image formation. The Claim is broader than OpenGL alone; the source should not be treated as a universal description of every graphics pipeline.

**Risk route: MODERATE.** Foundational computing statement; avoid treating one API as representative of all raster, vector, offline or real-time rendering systems.

**Disposition: HOLD pending an exact OpenGL overview locator and a scope note that OpenGL is an example, not the whole field.**

### 3.2 Computer Graphics B — graphics API as an interface

**Claim:** “Графический API предоставляет интерфейс к возможностям графической подсистемы.”

**Finding: DIRECT.** Khronos describes OpenGL as an API that exposes graphics-hardware features. OpenGL ES is described as a flexible interface between software and graphics-acceleration hardware: https://www.khronos.org/opengles. This directly supports the Claim's interface role.

**Risk route: MODERATE.** API behaviour and available features vary by version, platform and implementation.

**Disposition: HOLD pending exact Khronos locator and version/platform qualification.**

### 3.3 Computer Graphics C — capabilities and performance vary

**Claim:** “Возможности и производительность зависят от API, оборудования и реализации.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** Khronos documents API versions, hardware capabilities and implementation-specific extensions. This supports variation in capability. The registered OpenGL overview does not fully establish every performance dependency or provide a controlled performance model.

**Risk route: MODERATE.** Avoid inferring comparative performance or benchmark outcomes without a defined workload, device, driver, API version and measurement method.

**Disposition: HOLD pending exact specification/implementation locators and a benchmark-scope note.**

### 3.4 Conservation Biology A — biodiversity, species and population change

**Claim:** “Биоразнообразие связано с разнообразием видов и изменением численности организмов во времени.”

**Registered Source:** OpenStax Biology 2e, section 47.4: https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity

**Finding: PARTIAL.** Section 47.4 discusses biodiversity measurement, cataloguing species, threatened-species status, populations and conservation outcomes. It supports species diversity and the need to monitor biodiversity. It is primarily a conservation section, not a precise definition of biodiversity or a full population-dynamics source; the time-change element needs a more direct locator/source.

**Risk route: LOW direct consequence.** Basic ecological statement; avoid conflating species richness, abundance, genetic diversity and ecosystem diversity.

**Rights:** OpenStax Biology 2e has a CC BY-NC-SA license and states that its content may not be used for LLM training or otherwise ingested into LLM/generative-AI offerings without prior written permission. No such permission is recorded. Keep an explicit rights HOLD.

**Disposition: HOLD pending exact passage, scope refinement and rights resolution or a rights-compatible replacement source.**

### 3.5 Conservation Biology B — populations, habitats and ecosystems

**Claim:** “Сохранение биоразнообразия учитывает состояние популяций, местообитаний и экосистем.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** OpenStax 47.4 covers threatened populations, habitat protection, ecosystem preserves, habitat restoration and the limits of preserve-based conservation. This supports the multi-level framing. The EU remains generic and does not identify these passages.

**Risk route: LOW direct consequence.** Conservation decisions can be consequential in practice, but this Claim is a broad educational statement. Do not treat a single preserve model as universally optimal.

**Rights/disposition:** Same OpenStax AI-ingestion and CC BY-NC-SA HOLD as 3.4. No AI-enabled reuse is cleared.

### 3.6 Construction B — building safety depends on assemblies and loads

**Claim:** “Безопасность и эксплуатационные характеристики здания зависят не только от отдельных материалов, но и от их соединения, нагрузки и условий применения.”

**Registered Source:** NIST Building Science: https://www.nist.gov/building-science

**Finding: NOT ESTABLISHED; REGISTERED URI CURRENTLY RETURNS 404.** The exact registered URL could not be retrieved and returns a not-found response. The registered Source therefore cannot currently support this safety-related Claim. Other building-science materials may be relevant, but they are not the registered Source and must not be silently substituted.

**Risk route: ELEVATED — building safety and performance.** Incorrect or incomplete building guidance can affect structural integrity, fire safety, moisture performance and occupant safety. This Claim must not be used as a design rule.

**Disposition: HOLD.** Resolve the NIST Source identity/URI through an authorized, versioned correction or a separately registered replacement source; obtain building-science/structural specialist review.

### 3.7 Construction Project Management B — requirement changes and constraints

**Claim:** “Изменения требований проекта могут влиять на сроки, стоимость и другие проектные ограничения.”

**Registered Source:** Whole Building Design Guide: https://www.wbdg.org/

**Finding: PARTIAL.** The registered WBDG homepage is a broad portal. Supplementary WBDG material on construction-phase cost management describes change orders, scope changes, cost estimation and schedule impacts; WBDG project-performance requirements material connects scope, requirements, schedules and budgets. These related pages support the concept but are not the registered Source and are not pinpointed by the current EU.

**Risk route: MODERATE.** Project changes can have significant financial, contractual and safety implications; the effects are context- and contract-dependent.

**Disposition: HOLD.** Add the specific WBDG pages as separately versioned Sources/EUs, with a clear distinction between scope, cost, schedule and contractual constraints.

### 3.8 Critical Thinking D — authority is contextual and revisable

**Claim:** “Критическая оценка требует соотносить авторитет и качество источника с конкретным вопросом и контекстом, рассматривать альтернативные перспективы и быть готовым пересмотреть вывод.”

**Registered Source:** ACRL, *Framework for Information Literacy for Higher Education*: https://www.ala.org/acrl/standards/ilframework

**Finding: DIRECT.** The ACRL frame “Authority Is Constructed and Contextual” says resources should be evaluated against the information need and context of use, and encourages openness to new perspectives, additional voices, review of biases and changes in schools of thought. The registered EU is not pinpointed to the frame.

**Risk route: LOW direct consequence.** This is a methodological/educational principle; it should not be turned into relativism or an instruction to accept every source as equally credible.

**Disposition: HOLD pending a pinpoint to the ACRL frame and a distinction between contextual authority and evidential quality.**

### 3.9 Cryptography B — encryption limits disclosure

**Claim:** “Шифрование преобразует данные для ограничения раскрытия их содержания неавторизованным сторонам.”

**Registered Source:** NIST Cryptography: https://www.nist.gov/cryptography

**Finding: PARTIAL.** The NIST page says cryptography uses mathematical techniques to protect information security and describes block ciphers as encrypting data in blocks. It does not, at the landing-page level, define the full transformation process or establish all conditions under which only authorized parties can recover plaintext. A dedicated NIST encryption definition or standard is needed.

**Risk route: ELEVATED — security-sensitive.** Encryption alone does not guarantee confidentiality if keys, endpoints, algorithms, modes, implementation or access controls are compromised.

**Disposition: HOLD.** Add a specific NIST glossary/standard passage and keep the Claim distinct from authentication, integrity and key-management claims.

### 3.10 Cultural Anthropology A — cultural anthropology as a field

**Claim:** “Культурная антропология является одной из традиционных областей антропологии, изучающей человеческие сообщества и культурные практики.”

**Registered Source:** American Anthropological Association, *What is Anthropology?*: https://americananthro.org/practice-teach/what-is-anthropology/

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** The AAA page describes anthropology's broad study of human experience and identifies cultural anthropology among the four fields, including observation of communities and their practices. Direct retrieval of the page was blocked during this check, so the current verification relies on the indexed official page text rather than a complete page read.

**Risk route: LOW direct consequence.** Introductory disciplinary statement; disciplinary traditions and institutional classifications vary.

**Disposition: HOLD pending a stable accessible passage locator and a scope note for the four-field US tradition.

### 3.11 Cultural Anthropology B — multidimensional human experience

**Claim:** “Антропологические подходы рассматривают человеческий опыт с учётом социальных, языковых, биологических и исторических аспектов.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** The AAA source describes biological bodies and genetics, historical study of past groups, contemporary community practices and language/meaning/social action. This supports the multidimensional framing, but the source's direct retrieval was blocked and the EU remains generic.

**Risk route: LOW direct consequence.** Do not imply that every anthropological study uses all four approaches or that one US disciplinary taxonomy is universal.

**Disposition: HOLD pending accessible passage locator and an explicit disciplinary-scope note.**

### 3.12 Cultural Anthropology C — insider observation and research limitations

**Claim:** “Наблюдение сообщества изнутри исследовательской перспективы является методом получения данных, но не устраняет необходимость описывать контекст и ограничения исследования.”

**Finding: PARTIAL.** The AAA page describes observing contemporary communities from an insider perspective. It does not directly establish the complete methodological caveat about contextual description and research limitations. A dedicated ethnographic-methods source is required.

**Risk route: MODERATE.** Insider/participant observation can involve positionality, access, consent, power relations, translation and researcher bias.

**Disposition: HOLD.** Add an ethnographic-methods source with explicit treatment of positionality, reflexivity, consent and limitations.

### 3.13 Cultural Heritage A — intergenerational legacy

**Claim:** “Культурное наследие включает передаваемые между поколениями материальные объекты, традиции и практики.”

**Registered Source:** UNESCO Cultural Heritage: https://www.unesco.org/en/query-list/c/cultural-heritage

**Finding: DIRECT.** The registered UNESCO page defines cultural heritage as a legacy of physical artefacts, traditions and practices passed down through generations within a community. It directly supports the Claim. The page explicitly states that it is introductory information and not a complete statement of UNESCO's official position.

**Risk route: LOW direct consequence.** Avoid reducing cultural heritage to a closed list or treating communities as internally uniform.

**Disposition: HOLD pending exact page locator and an introductory-definition scope note.**

### 3.14 Cultural Heritage B — tangible and intangible forms

**Claim:** “Культурное наследие включает как материальные элементы, такие как памятники и произведения, так и нематериальные формы, такие как традиции и ритуалы.”

**Finding: DIRECT.** The registered UNESCO page explicitly distinguishes tangible elements such as monuments and artworks from intangible aspects such as folklore and rituals.

**Risk route: LOW direct consequence.** This is a broad educational classification; real heritage practices can combine tangible and intangible dimensions.

**Disposition: HOLD pending exact locator and rights review for any reuse beyond citation.

### 3.15 Cultural Heritage C — community-recognized intangible heritage

**Claim:** “Нематериальное культурное наследие связано с знаниями, навыками и практиками, которые сообщества признают частью своего наследия.”

**Finding: PARTIAL / DIRECT SUPPORT IN A SEPARATE UNESCO LEGAL SOURCE.** The registered introductory UNESCO page supports traditions and practices passed down within a community. UNESCO's Convention text defines intangible cultural heritage through practices, knowledge and skills that communities/groups/individuals recognize as part of their heritage: https://www.unesco.org/en/legal-affairs/convention-safeguarding-intangible-cultural-heritage. The Convention text is a separate Source and must be added through a versioned Source/EU chain if used as the direct legal/definitional basis.

**Risk route: LOW direct consequence.** Community recognition is central; do not impose an external universal list or erase living reinterpretation.

**Disposition: HOLD pending separate Convention Source/EU and a locator to Article 2.

### 3.16 Cybersecurity A — risk to systems, data and processes

**Claim:** “Кибербезопасность рассматривает риски для систем, данных и связанных с ними процессов.”

**Registered Source:** NIST Cybersecurity Framework: https://www.nist.gov/cyberframework

**Finding: DIRECT CONCEPTUAL SUPPORT.** NIST describes CSF 2.0 as helping organizations understand and improve cybersecurity risk management. This supports the broad risk-management framing. The page is a framework landing page, not a complete definition of cybersecurity.

**Risk route: ELEVATED — security-sensitive.** The Claim is high-level and must not be mistaken for an implementation standard or a complete risk model.

**Disposition: HOLD pending a pinpoint to CSF 2.0 and a scope note distinguishing cybersecurity from information security and operational resilience.

### 3.17 Cybersecurity B — confidentiality, integrity and availability

**Claim:** “Конфиденциальность, целостность и доступность являются базовыми свойствами информационной безопасности.”

**Finding: PARTIAL / DIRECT SUPPORT IN A SEPARATE NIST GLOSSARY.** NIST CSRC's security and information-security glossary entries define confidentiality, integrity and availability, but the registered NIST Cybersecurity Framework landing page does not itself provide those definitions: https://csrc.nist.gov/glossary/term/security and https://csrc.nist.gov/glossary/term/information_security. The current EU does not identify those glossary entries.

**Risk route: ELEVATED.** CIA is a foundational security model, but it is not a complete cybersecurity model and does not subsume authenticity, accountability, privacy, safety or resilience.

**Disposition: HOLD.** Add a distinct NIST glossary Source/EU with exact definition and scope note.

### 3.18 Data Ethics B — fairness, accountability, transparency and oversight

**Claim:** “Ethical frameworks emphasize fairness, accountability, transparency and human oversight.”

**Registered Source:** UNESCO, Recommendation on the Ethics of Artificial Intelligence: https://www.unesco.org/en/artificial-intelligence/recommendation-ethics

**Finding: DIRECT.** UNESCO's Recommendation identifies fairness, transparency, accountability and human oversight as core principles/values of ethical AI. It also emphasizes that human responsibility remains ultimate. The EU is generic and should point to the relevant Recommendation sections.

**Risk route: ELEVATED — AI governance, rights and privacy.** These are governance principles, not a complete operational compliance checklist or guarantee that an AI system is safe or fair.

**Disposition: HOLD pending exact Recommendation sections and a specialist governance review.

### 3.19 Databases A — organized data repository

**Claim:** “База данных хранит организованные данные, которыми можно управлять с помощью определённой системы.”

**Registered Source:** NIST Information Technology Laboratory: https://www.nist.gov/itl

**Finding: NOT ESTABLISHED BY REGISTERED SOURCE.** The NIST ITL homepage describes the laboratory's mission and research domains; it does not define a database. NIST CSRC's separate glossary entry describes a database as a repository of information or data: https://csrc.nist.gov/glossary/term/database. That glossary entry is not the registered Source.

**Risk route: MODERATE.** A broad definition should not conflate database, database management system, data warehouse, file store and data model.

**Disposition: HOLD.** Add the NIST CSRC glossary or a database textbook as a separately versioned Source/EU.

### 3.20 Databases B — schema and relationships

**Claim:** “Схема базы данных описывает структуру данных и связи между их элементами.”

**Finding: NOT ESTABLISHED BY REGISTERED SOURCE.** The NIST ITL landing page does not define database schemas or relational constraints. A separate source on database design/data modelling is required.

**Risk route: MODERATE.** Do not imply every database is relational or that every schema captures all semantic constraints and relationships.

**Disposition: HOLD.** Add a dedicated database-design source and an exact section/figure locator.

## 4. Consolidated routing

| Claims | Passage fit | Risk route | Main issue |
|---|---|---|---|
| Computer Graphics A/B | Direct | Moderate | Khronos overview locator and API scope |
| Computer Graphics C | Partial | Moderate | Performance dependencies need defined conditions |
| Conservation Biology A | Partial | Low | Source supports measurement/management, not complete population-time definition |
| Conservation Biology B | Direct conceptual | Low | OpenStax pinpoint and rights hold |
| Construction B | Not established | Elevated | Registered NIST URL returns 404 |
| Construction Project Management B | Partial | Moderate | WBDG homepage vs relevant change/cost/schedule pages |
| Critical Thinking D | Direct | Low | ACRL frame pinpoint |
| Cryptography B | Partial | Elevated | Encryption transformation and authorization details need a precise NIST source |
| Cultural Anthropology A/B | Partial | Low | AAA page retrieval blocked; indexed source content only |
| Cultural Anthropology C | Partial | Moderate | Ethnographic method/positionality source needed |
| Cultural Heritage A/B | Direct | Low | UNESCO page is introductory, not exhaustive official position |
| Cultural Heritage C | Partial | Low | Direct definition resides in separate Convention Source |
| Cybersecurity A | Direct conceptual | Elevated | CSF landing page scope |
| Cybersecurity B | Partial | Elevated | CIA definitions are in a separate NIST glossary |
| Data Ethics B | Direct | Elevated | Recommendation pinpoint and governance scope |
| Databases A/B | Not established | Moderate | NIST ITL landing page is not a database/schema source |

Counts:
- Direct conceptual support: **8**.
- Partial support: **10**.
- Not established by registered Source: **2**.
- Elevated routing: **5**.
- Moderate routing: **6**.
- Low direct-consequence routing: **9**.

These are desk-level evidence-fit and routing labels only. They are not final risk classes or D/E/B scores.

## 5. Integrity

- Exact Claim IDs screened: **20**.
- Claim records inspected: **20**.
- Evidence Use records inspected: **20**.
- Source records inspected: **11**.
- Claim→EU→Source exact identity/version chains resolving: **20/20**.
- Generic/broad EUs without reproducible Claim-specific locator: **20/20**.
- Material source identity/access defects: **1 confirmed 404** (NIST Building Science); **1 broad portal mismatch** (NIST ITL used for database/schema Claims); other EUs need pinpoints or separate Sources.
- Canonical Claim/EU/Source JSON changes: **0**.
- Risk metadata assigned or changed: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Specialist approvals: **0**.
- Rights/reuse permissions assessed or granted: **0**.
- Publication/Human View approval: **0**.

OpenStax Biology 2e carries CC BY-NC-SA terms and an explicit restriction on LLM/generative-AI ingestion without prior written permission; no permission is recorded. ACRL's Framework is CC BY-NC-SA 4.0; any reuse must preserve the license conditions. No AI-ingestion or commercial-reuse clearance is asserted for any source in this package.

## 6. Required next work

1. Continue the refreshed 100-Claim queue with the next lane; preserve the deterministic ID ledger and evidence packets.
2. Correct the NIST Building Science Source identity/URI or replace it only through a versioned proposal; route to a building-science specialist.
3. Prepare separate Source/EU proposals for WBDG change-management material, NIST encryption definitions, NIST CIA glossary entries, UNESCO Convention Article 2 and NIST database/schema definitions.
4. Resolve OpenStax AI-use rights before any AI ingestion or generated derivative; otherwise use a rights-compatible replacement source.
5. Keep all 20 Claims UNASSESSED/HOLD until formal risk scoring, rights review, specialist checks and authorized metadata changes are completed.

This package is not a final risk classification, building/security certification, legal opinion, source-rights clearance, canonical correction, independent peer review or M13 closure.
