# Первая редакция — Package K: rights and attribution screen для 19 глав

Дата: 2026-11-27  
PR #22: OPEN / DRAFT / NOT MERGED  
Исходный HEAD после Package J: `63b4fd00f410ddc603603dda1acfae0801a5056d`  
Статус: READ-ONLY SOURCE-RIGHTS SCREEN. Не является юридическим заключением, разрешением на использование, проектной лицензией, rights clearance или решением INCLUDE.

## 1. Назначение и границы

Package K начинает следующий запланированный этап — права и атрибуция. Он сводит к единому виду условия использования точных Source-кандидатов, связанных с 19-главной картой первой редакции, и отделяет:

- права на исходный материал;
- условия цитирования и атрибуции;
- условия использования текста, данных, изображений, карт, диаграмм и иных компонентов;
- ограничения, связанные с некоммерческим использованием и AI/LLM ingestion;
- ещё не принятые решения владельца проекта R-01–R-10.

Это предметный screen источников, а не проверка прав на весь корпус. Он использует существующие candidate chains и прежние source-specific screens; закрытые substantive audits не повторяются.

**Ни одна из 19 глав и ни одна запись не получает INCLUDE.** Все кандидатные записи остаются HOLD до завершения независимых правовых, редакционных и иных применимых release gates.

## 2. Главный вывод

Права источников неоднородны. Для 19 представительских цепочек выявлены четыре практических класса:

1. **Government-authored material с public-domain основанием в США:** USGS, NOAA, FEMA/Ready.gov, CDC, NIST, USDA, NIH/NIMH и NASA. Это не blanket clearance: необходимо исключать сторонние фото, иллюстрации, карты, данные, логотипы, подрядные материалы и компоненты с отдельной отметкой прав; учитывать территориальные различия и запрет на подразумеваемое одобрение ведомством.
2. **Разрешительная открытая лицензия:** OpenStax Physics — CC BY 4.0; PostgreSQL Documentation — PostgreSQL License; отдельные BIPM SI Brochure editions — CC BY 4.0. У каждой лицензии свои требования к атрибуции, уведомлениям и сторонним компонентам.
3. **Условное/ограниченное использование:** FAO handbook, American Red Cross и World Bank source page. Для этих источников нельзя предполагать свободное коммерческое распространение или копирование; необходимо сохранять ссылки, независимый пересказ фактов и точную атрибуцию, а для использования за пределами явно разрешённых условий — получать письменное разрешение или выбирать другой источник.
4. **Блокирующие условия OpenStax:** Chemistry 2e, Biology 2e и World History Volume 1 — CC BY-NC-SA 4.0, с явным требованием предварительного письменного разрешения OpenStax для ingestion/training/AI offerings. Не переносить на эти книги условия Physics. Для текущего AI-assisted workflow это release blocker до письменного разрешения или одобренной rights-compatible замены.

Даже когда источник имеет public-domain или CC BY статус, проект не может объявить материал cleared до принятия собственной лицензии, определения правообладателя и политики атрибуции/использования.

## 3. Exact-source screen по 19 главам

Уровни ниже описывают только видимые условия источника, а не законность конкретной публикации и не допуск Claim к выпуску:

- **PD-US / low source-rights friction:** федеральный материал США, если он действительно создан государственным сотрудником и не помечен как сторонний/ограниченный.
- **CC BY 4.0:** разрешено распространение и адаптация с выполнением условий атрибуции и указания изменений.
- **PostgreSQL License:** permissive, но при копировании документации/ПО должны сохраняться copyright notice, permission notice и disclaimer paragraphs.
- **Conditional:** условия зависят от некоммерческого характера, точного item-level use, permissions или distribution model.
- **AI/LLM restriction:** отдельное условие OpenStax о предварительном письменном разрешении на ingestion/training/AI offerings.
- **Unresolved:** конкретный материал, его авторство/компоненты или условия для выбранного способа распространения ещё не установлены.

| Глава | Representative chain из Package I | Источник и зафиксированные условия | Практическое решение для первой редакции |
|---:|---|---|---|
| 1. Чрезвычайные ситуации | `CLM-ALERTS-ENABLE-RESPOND@2` → `SRC-RED-CROSS-ALERTS-2026@2` | American Red Cross, *Be Informed*. Условия Red Cross дают личную, отзывную, непередаваемую лицензию для personal/non-commercial use; копирование downloadable materials также ограничено personal/non-commercial; запрещены отдельное распространение, создание intact page reproduction и производные/коммерческое использование без письменного разрешения. Прямую ссылку разрешено размещать честно и так, чтобы было ясно, что это ресурс Red Cross. | **Conditional / rights review required.** Не переносить текст, изображения или страницу в Reader. Для независимого factual summary и ссылки требуется owner/legal review с учётом фактической модели распространения. Никакого implied Red Cross endorsement. |
| 2. Вода | `CLM_WATER_RESOURCES_BASICS_A@1` → `SRC-WATER_RESOURCES_BASICS@1` | USGS Water Resources Mission Area. Авторский текст и данные USGS обычно public domain в США; сторонние изображения/данные и материалы с отдельным copyright исключаются. Сам Claim уже имеет substantive debt/source-fit issue. | **PD-US for eligible USGS-authored text; candidate still HOLD.** Не использовать общую отметку public в Source как доказательство rights clearance или научной пригодности. Содержательный blocker важнее правового. |
| 3. Пища и продовольственная устойчивость | `CLM-FOOD_SECURITY_BASICS-A@1` → `SRC-FOOD_SECURITY_BASICS@1` | FAO, *Handbook for Defining and Setting up a Food Security Information and Early Warning System* (2000). FAO website terms разрешают определённое копирование для private study/research/teaching и non-commercial products/services с attribution; translation/adaptation и resale/commercial use требуют обращения за разрешением. FAO publications отдельно подчиняются Open Access policy; точная страница Source — старый HTML-представитель handbook, не следует автоматически маркировать её CC BY. Третьи лица могут владеть отдельными таблицами, рисунками и изображениями. | **Conditional.** Оставить только независимую формулировку фактов, точную библиографию и ссылку; не копировать фрагменты, таблицы или изображения. До определения модели распространения не считать коммерческое/адаптационное использование разрешённым. |
| 4. Укрытие и жильё | `CLM-SHELTER_BASICS-A@1` → `SRC-SHELTER_BASICS@1` | Ready.gov / FEMA. FEMA сообщает, что большая часть материалов FEMA.gov не защищена авторским правом и может копироваться/распространяться, но отдельные фотографии и графика могут быть лицензированы или ограничены; проверять credit/copyright каждого элемента. Source сейчас указывает на широкую главную страницу Ready.gov, а не на конкретный документ. | **PD-US likely for FEMA-authored text; item-level unresolved.** Нужен точный target page и проверка его credits. Не использовать FEMA/DHS seals, logos или сторонние изображения; не создавать впечатление официального одобрения. |
| 5. Здоровье и гигиена | `CLM-HANDWASH-20SEC@1` → `SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1` | CDC, *Guidelines for Personal Hygiene During an Emergency*. Большая часть CDC/ATSDR information — public domain, но отдельные contractor/grantee/third-party images и materials могут быть ограничены. CDC требует attribution и prominently displayed non-endorsement disclaimer; международная охрана может отличаться. | **PD-US for eligible CDC-authored text; rights conditions manageable.** Использовать точный текстовый source citation, CDC attribution и disclaimer; не переносить картинки. Независимая qualified health/editorial review остаётся обязательной и не заменяется rights screen. |
| 6. Тепло, огонь и энергия | `CLM-ENERGY_BASICS-A@1` → `SRC-ENERGY_BASICS@1` | OpenStax *Physics*. Текущая Preface указывает CC BY 4.0 для книги Physics; разрешены распространение и адаптация с attribution OpenStax и contributors. Art credits различаются: часть иллюстраций предоставлена по отдельным разрешениям и имеет ограничения. В просмотренной Preface отдельного LLM restriction не обнаружено; это не отменяет проверки конкретных art credits и страницы. | **CC BY 4.0 for book text, subject to exact item/asset check.** Для фактического пересказа и цитирования сохранять attribution; не копировать art без проверки индивидуального credit. Не путать Physics с другими OpenStax titles. |
| 7. Инструменты и материалы | `CLM-MATERIALS_BASICS-A@1` → `SRC-MATERIALS_BASICS@1` | NIST Materials Science and Engineering Division. NIST сообщает, что информация на сайте, кроме отдельно отмеченной copyrighted material, является public information и может распространяться/копироваться; требуются соответствующие byline/photo/image credits. У отдельных research products и third-party components могут быть свои условия. | **PD-US for eligible NIST-authored text.** Не использовать сторонние figures, images или datasets без проверки. Указывать NIST как источник и сохранять non-endorsement. |
| 8. Сельское хозяйство и почва | `CLM-SOIL_BASICS-A@1` → `SRC-SOIL_BASICS@2` | USDA NRCS, *What is Soil?*. USDA указывает, что большая часть материалов сайта является public domain, но некоторые материалы защищены copyright/trademark/patent или предоставлены только для personal use; требуется проверять маркировку и credits. | **PD-US likely for USDA-authored text; item-level check.** Использовать текстовые факты и attribution USDA/NRCS; не копировать фотографии/диаграммы до проверки. Source@2 — актуальная версия после Package G/H, не восстанавливать старую версию ради прав. |
| 9. Природные опасности | `CLM-WEATHER_BASICS-A@1` → `SRC-WEATHER_BASICS@1` | NOAA, *Weather & Atmosphere*. Большая часть NOAA government content public domain; требуется credit NOAA/конкретной программы, нельзя подразумевать endorsement или выдавать изменённый материал за официальный. Сторонние credits и embedded media проверяются отдельно. | **PD-US for NOAA-authored text.** Допустимы независимый factual summary и ссылка при корректном credit/disclaimer. Не копировать media с третьими сторонами. Не выдавать общую статью за актуальный локальный прогноз. |
| 10. Связь и навигация | `CLM-MAPS_AND_NAVIGATION_BASICS-A@1` → `SRC-MAPS_AND_NAVIGATION_BASICS@1` | USGS, *Finding Your Way With Map and Compass*. USGS-authored information обычно public domain в США и требует credit. Сами USGS topographic maps в основном public domain, но для US Topo есть отдельные исключения по некоторым licensed road data и orthoimages. | **PD-US for USGS-authored text.** Package J уже уточнил EU@2 для двух Claim-specific passages. Не включать карты/изображения как assets без отдельной проверки; не делать вывода о currency или безопасности конкретного маршрута. |
| 11. Математика и измерения | `CLM-SI-SEVEN-BASE@1` → `SRC-NIST-SI-UNITS@1` | NIST SI Units page: NIST information public unless marked copyrighted; attribution requested. Отдельно: актуальная SI Brochure BIPM 9th edition (2019, updated 2026) обозначена CC BY 4.0. Однако текущая цепочка Claim A использует NIST Source, а не автоматически BIPM Source. | **PD-US for NIST source; CC BY 4.0 only if BIPM material is actually added.** Не подменять source chain без versioned approval. Существующая SI preview authorization остаётся private/non-release; public inclusion не разрешена этим screen. |
| 12. Физические науки | `CLM-MOTION_BASICS-A@1` → `SRC-MOTION_BASICS@1` | OpenStax *Physics*, тот же book-level CC BY 4.0 source, что и Energy A. Attribution OpenStax/contributors; art with separate permission must follow its own credit. Текущая canonical Source@1 остаётся исторической и version-pinned. | **CC BY 4.0 for book text, subject to item/asset check.** Package J намеренно не менял Motion Source: Source@1 используется несколькими ссылками; migration needs its own historical-version-preserving bounded package. |
| 13. Химические науки | `CLM-MIXTURES_AND_SOLUTIONS-A@1` → `SRC-MIXTURES_AND_SOLUTIONS@1` | OpenStax *Chemistry 2e*. CC BY-NC-SA 4.0; non-commercial use only, attribution and ShareAlike for adaptations. Preface explicitly says the book must not be used for LLM training/ingestion or generative-AI offerings without prior written permission. Commercial printing also requires approval; art and components have their own credits. | **AI/LLM RESTRICTION — BLOCKED pending written permission or rights-compatible source replacement.** Do not treat an exact locator or independent wording as a substitute for resolving the explicit ingestion condition. No content, images, exercises or diagrams to be reused. |
| 14. Науки о жизни | `CLM-CELL_BASICS-A@1` → `SRC-CELL_BASICS@1` | OpenStax *Biology 2e*. CC BY-NC-SA 4.0, with explicit prior-written-permission requirement for LLM ingestion/AI offerings; non-commercial and ShareAlike requirements; third-party art credits apply. | **AI/LLM RESTRICTION — BLOCKED pending written permission or rights-compatible source replacement.** No automatic promotion; no reproduction of text or art. |
| 15. Земля, климат и космос | `CLM-EARTH_SYSTEM_BASICS-A@1` → `SRC-EARTH_SYSTEM_BASICS@1` | NASA, *Earth*. NASA-authored material is generally public domain in the U.S. for factual/informational use, but third-party images/media are marked and remain with their owners. NASA insignia, logotype and identifiers are not public domain; commercial/editorial use must not imply NASA endorsement. | **PD-US for eligible NASA-authored text; third-party/brand exclusions.** Не использовать NASA logo/seal. Содержательная classification issue Earth System A (four-vs-five spheres) остаётся отдельным HOLD; права не исправляют её. |
| 16. Инженерия и вычисления | `CLM-DATABASES_BASICS-A@3` → `SRC-DATABASES_BASICS@3` | PostgreSQL 18.7 Documentation, §§2.2–2.6. PostgreSQL License распространяется на PostgreSQL software и documentation; разрешает use/copy/modify/distribute for any purpose без платы при сохранении copyright notice, permission paragraph и двух disclaimer paragraphs во всех копиях. Package H rights recheck не предполагает копирования документации или кода. | **Permissive PostgreSQL License for copied documentation/software, subject to notice retention.** Для независимого factual paraphrase + link не копировать expressive docs. В Reader явно назвать PostgreSQL 18.7 как version-pinned example, не как latest/current release. |
| 17. Науки о человеке | `CLM-LEARNING_BASICS-A@1` → `SRC-LEARNING_BASICS@1` | NIMH Learning and Memory Program. NIMH text is public domain and may be copied/reused unless otherwise indicated; cite NIMH and do not alter text misleadingly. NIMH images and publication images may not be reused, even with citation; no medical advice or endorsement may be implied. | **PD-US for NIMH text; no image reuse.** Package J added the exact NIMH locator and a representative/non-exhaustive program-scope boundary. Keep Claim out of universal taxonomy or clinical guidance. |
| 18. Общество и институты | `CLM-ECONOMICS_BASICS-A@1` → `SRC-ECONOMICS_BASICS@1` | World Bank, *Understanding Poverty*. Current World Bank terms allow access/use for personal, educational and non-commercial purposes with attribution; reproduction, redistribution or commercial use requires prior written permission unless explicitly stated otherwise. The exact page has no source-specific open license recorded in the Source. | **Conditional / permission required for redistribution or commercial use.** Source-fit is independently weak for the full economics Claim. Keep HOLD; do not infer CC BY from World Bank branding or general open-access statements elsewhere. |
| 19. История и культура | `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1` → `SRC-ANCIENT_CIVILIZATIONS_BASICS@1` | OpenStax *World History Volume 1, to 1500*. CC BY-NC-SA 4.0, explicit prior written permission for LLM training/ingestion/AI offerings, non-commercial and ShareAlike conditions; commercial printing needs approval; digital redistribution of book content has page-level attribution and ShareAlike requirements. A separate candidate Claim B has six additional CC BY 4.0 evidence sources, but Claim B@1 provenance still references this OpenStax Source@1; a separate provenance migration request is not approved. | **AI/LLM RESTRICTION — BLOCKED for OpenStax-dependent path pending written permission or approved migration/replacement.** Do not represent Claim B as CC BY-only while its exact provenance still requires Source@1. No source/Claim migration is authorized by Package K. |

## 4. Сводка правовых рисков и приоритетов

### 4.1 Условия с относительно низким трением источника

Для ограниченного текста и фактов, созданных соответствующим государственным ведомством США, наиболее понятные source-level основания есть у:
- USGS — Water Resources, Maps;
- FEMA/Ready.gov — Shelter;
- CDC — Emergency Hand Hygiene;
- NIST — Materials, SI Units;
- USDA NRCS — Soil;
- NOAA — Weather;
- NASA — Earth System;
- NIH/NIMH — Learning.

Это **не означает**, что любые материалы на этих сайтах public domain. В каждом случае исключаются third-party media, contractor/grantee work, trademarks, agency logos, restricted datasets and other marked content. Также учитывается, что U.S. public-domain status не автоматически решает вопросы защиты за пределами США.

### 4.2 Источники, требующие особой осторожности

- **American Red Cross:** личная/non-commercial license для использования сервиса; внешняя публикация/копирование содержимого не разрешены общей лицензией. Ссылка и независимое изложение — предпочтительный путь, но для выбранной модели распространения требуется review.
- **FAO Handbook:** старый web-hosted handbook не следует автоматически маркировать CC BY. Общие FAO conditions дают ограниченное non-commercial permission; translation/adaptation/resale/commercial use требуют отдельного разрешения.
- **World Bank:** текущие site terms ограничивают разрешённое использование personal/educational/non-commercial; reproduction, redistribution и commercial use требуют prior written permission, если нет явного исключения.
- **OpenStax Physics:** CC BY 4.0 — отдельный book-level case.
- **OpenStax Chemistry 2e, Biology 2e, World History Volume 1:** CC BY-NC-SA 4.0 плюс отдельное AI/LLM ingestion restriction. Не объединять эти три источника с Physics под одним общим label “OpenStax CC BY”.
- **PostgreSQL:** permissive license; если документация или код копируются, обязательны notices/disclaimers. Это не является основанием копировать больше текста, чем требуется.

### 4.3 Attribution minimums

Reader-facing citation для каждого фактически использованного источника должна содержать, где применимо:
- организацию/автора;
- точное название материала, книгу или edition;
- дату/версию публикации, если доступна;
- точный section/page/paragraph locator;
- canonical URL/DOI и дату обращения;
- точное обозначение лицензии и ссылку на неё, если материал действительно используется под лицензией;
- указание изменений, если этого требует лицензия;
- source-specific disclaimer/non-endorsement;
- credit для отдельного автора фотографии/рисунка/карты, если такой asset вообще включён.

Нельзя подменять item-level attribution ссылкой только на главную страницу организации. Не следует добавлять логотипы организаций в качестве декоративных значков или создавать видимость официального партнёрства.

## 5. Проектные решения R-01–R-10 — состояние не изменилось

Авторитетным остаётся `FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER-2026-11-19.md`. Все десять owner decisions остаются OPEN:

| ID | Что должен решить уполномоченный владелец | Что необходимо зафиксировать |
|---|---|---|
| R-01 | Правообладатель оригинального корпуса и редакционных материалов | Конкретное физическое/юридическое лицо или документированная коллективная модель и основание полномочий |
| R-02 | Лицензия оригинального текста и структурированных данных | Точное название/версия лицензии, canonical text/URI, covered material, exclusions, attribution и compatibility review |
| R-03 | Лицензия программного кода | Отдельная лицензия кода или явное разделение с content/data license |
| R-04 | Условия для будущих contributors | Grant/permission, выбор attribution, warranties, third-party rules, withdrawal/dispute |
| R-05 | Source reuse policy | Раздельные правила для factual paraphrase/link, quotation, text, images, maps, diagrams, tables, datasets |
| R-06 | Ответственный редактор | Назначенное лицо/роль/организация, полномочия, review duties и escalation |
| R-07 | Release approver | Назначенный approver и отдельная approval record для выпуска |
| R-08 | Correction/dispute/withdrawal | Публичный контакт, владелец обработки, triage, response target, restriction, appeal и version history |
| R-09 | Authorship/attribution | Авторы, редакторы, переводчики, reviewers, contributors, AI/tool assistance, collective/anonymous credit |
| R-10 | Хранение и проверка rights evidence | Versioned evidence, item/source, rights holder, territory, term, restrictions, expiry/review date и evidence reference |

Package K не назначает правообладателя, не выбирает лицензию, не назначает редактора/approver и не создаёт публичный контакт. Эти решения нельзя вывести из GitHub, названия проекта, авторства commit или наличия Source records.

## 6. Практический operating baseline до решения владельца

Пока R-01–R-10 открыты, самый безопасный рабочий baseline для подготовки release candidate:

1. В Reader использовать только самостоятельно написанные factual summaries, точные ссылки и bibliographic locator metadata.
2. Не переносить в bundle сторонние абзацы, учебные страницы, таблицы, рисунки, карты, фото, диаграммы или datasets, пока не существует item-specific permission/license evidence.
3. Для CC BY источников сохранять attribution и indicate changes; проверять отдельно лицензии на art/media.
4. Для CC BY-NC-SA + AI/LLM restriction источников не продолжать использование в AI-assisted release workflow без письменного разрешения либо approved rights-compatible replacement.
5. Для Red Cross, FAO и World Bank не предполагать коммерческую/перераспространяемую лицензию; ограничиться ссылкой и независимо сформулированными фактами только после review выбранной модели распространения.
6. Для public-domain government sources проверять авторство конкретного текста и каждый отдельный asset; сохранять attribution и non-endorsement.
7. Не размещать логотипы ведомств/организаций как знаки партнёрства или одобрения.
8. Сохранять HOLD до появления versioned rights evidence и отдельного editorial/release approval.

Это рекомендуемый временный operating baseline, а не принятое решение владельца и не юридическое заключение.

## 7. Точный выход Package K

- Source-level rights screen составлен для всех 19 representative chapter candidates.
- Условия OpenStax Physics отделены от OpenStax Chemistry 2e, Biology 2e и World History Volume 1.
- Выделены источники с public-domain основаниями, CC BY 4.0, PostgreSQL License и условными/non-commercial restrictions.
- Уточнены минимальные attribution/disclaimer требования для государственных и институциональных источников.
- Зафиксировано, что project-level R-01–R-10 остаются OPEN.
- Ни один Claim, Evidence Use, Source, Context, Scope, Relation, candidate disposition, allowlist, coverage value или publication status не меняется.
- Ни одно permission request не отправлено; ни одна лицензия/правообладатель/редактор/approver не назначены.

**Package K завершён как read-only source-rights and attribution screen.** Следующий необходимый шаг — получить owner decisions по R-01–R-10 и выбрать фактическую модель распространения. После этого можно закрывать rights compatibility для exact-version candidate set и переходить к финальному составу/manifest. До этих решений нельзя объявлять права очищенными или формировать публичный INCLUDE из кандидатов, которые зависят от ограниченных источников.

## 8. Official source terms inspected

- FAO website terms: https://www.fao.org/contact-us/terms/en/
- FAO publications rights and permissions: https://www.fao.org/publications/about-fao-publishing/permissions/
- American Red Cross Terms of Use: https://www.redcross.org/terms-of-use.html
- USGS copyright and credits: https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits
- USGS topographic map copyright FAQ: https://www.usgs.gov/faqs/are-usgs-topographic-maps-copyrighted
- FEMA website information: https://www.fema.gov/about/website-information
- CDC Use of Agency Materials: https://www.cdc.gov/other/agencymaterials.html
- USDA Policies and Links: https://www.usda.gov/policies-and-links
- NOAA Education and Outreach FAQ: https://www.noaa.gov/office-education/outreach-communication/faq
- NIST Copyrights & Disclaimers: https://www.nist.gov/copyrights-disclaimers
- NIMH Website Policies: https://www.nimh.nih.gov/site-info/policies
- NASA Images and Media Usage Guidelines: https://www.nasa.gov/nasa-brand-center/images-and-media/
- OpenStax Physics Preface: https://openstax.org/books/physics/pages/preface
- OpenStax Chemistry 2e Preface: https://openstax.org/books/chemistry-2e/pages/preface
- OpenStax Biology 2e Preface: https://openstax.org/books/biology-2e/pages/preface
- OpenStax World History Volume 1 Preface: https://openstax.org/books/world-history-volume-1/pages/preface
- PostgreSQL License: https://www.postgresql.org/about/licence/
- World Bank Reproduction and Use: https://www.worldbank.org/ext/en/legal/terms-conditions/reproduction-and-use
- BIPM SI Brochure: https://www.bipm.org/en/publications/si-brochure

All rights statements above are limited to the official terms/pages inspected and the source material identified in the candidate chain. Recheck the exact item and terms at release time; web terms can change.
