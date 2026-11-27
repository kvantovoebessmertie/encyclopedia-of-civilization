# Первая редакция — Package I: перспективные разделы и приоритет продвижения кандидатов

Дата: 2026-11-27  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Исходный HEAD: `f43134f70f865126b66e17c7daa97ecafe43b787`  
Статус: консолидированный read-only пакет предметного отбора; не является INCLUDE manifest, rights clearance или owner approval.

## 1. Назначение и результат

Package I закрывает этап выявления перспективных разделов для первой редакции на основании уже существующей архитектуры Part I / Part II, 19-главной карты, representative-Claim shortlist и выполненных предметных проверок.

Цель — не начинать новый аудит корпуса, а определить, какие exact-version кандидаты дают наилучшее сочетание:
- ценности для читателя и вклада в широту Энциклопедии;
- прямой поддержки Claim конкретным Evidence Use и Source;
- ясной области применимости и ограничений;
- обозримой зависимости Claim → Evidence Use → Source;
- приемлемой текущести источника;
- отсутствия неразрешённого high-consequence риска;
- понятного и ограниченного следующего шага.

**Итог:** определены три очереди продвижения, сохранены точные кандидатные цепочки для всех 19 глав, выделены блокеры, которые не следует пытаться обходить локаторными исправлениями. Это рабочая приоритизация, а не утверждение истинности или готовности к публикации.

## 2. Что использовано — без повторения закрытых аудитов

### 2.1 Контролирующая архитектура

- `FIRST-EDITION-SCOPE-AND-SURVIVAL-INTEGRATION-2026-11-18.md`
- `FIRST-EDITION-OPENING-SURVIVAL-AND-DOMAIN-MAP-2026-11-18.md`
- `FIRST-EDITION-19-CHAPTER-EDITORIAL-TOC-AND-READER-STRUCTURE-2026-11-23.md`
- `FIRST-EDITION-19-CHAPTER-CANDIDATE-SLICE-MAPPING-AND-COVERAGE-2026-11-23.md`
- `FIRST-EDITION-19-CHAPTER-REPRESENTATIVE-CLAIM-CANDIDATE-SHORTLIST-2026-11-23.md`
- `FIRST-EDITION-BOUNDED-FOUNDATIONAL-CANDIDATE-CLOSURE-AND-QUEUE-2026-11-23.md`

### 2.2 Уже выполненные record-level screens

Шесть предметных отчётов охватывают суммарно 150 record files:
- Cell Basics + Statistics Basics — 20;
- Chemistry + Earth System + Learning — 27;
- Climate Basics + Measurement Uncertainty — 20;
- Emergency Alerts + Hand Hygiene + Food Security — 33;
- Maps & Navigation + Materials Basics — 18;
- Shelter + Soil + Emergency Water — 32.

Это не означает, что все 150 записей прошли научное рецензирование или допущены к публикации. Все проверенные Claims остаются HOLD.

### 2.3 Контроль изменений после предметных screens

PR #22 на исходном HEAD Package I: `f43134f70f865126b66e17c7daa97ecafe43b787`.

Сравнение inspection HEAD шести предметных отчётов с этим HEAD показало, что после соответствующих проверок canonical Content изменения затрагивали Soil Basics и Emergency Water, а не остальные рассмотренные кандидатные срезы. Для Soil/Water приоритет имеют более поздние Package F/G/H, а не устаревшие версии их прежних audit conclusions.

Поэтому:
- не повторяются проверки Alerts, Hand Hygiene, Food Security, Weather, Maps, Materials, Motion, Mixtures, Cell, Statistics, Earth System, Climate, Measurement Uncertainty, Databases и Learning;
- для Soil и Water учитываются versioned operations Package G и восстановление исторического Soil Source@1 в Package H;
- Shelter остаётся на своём ранее зафиксированном уровне: её 13-record audit не объявляется повторно выполненным на HEAD H2.

### 2.4 Текущая техническая точка

На HEAD Package H2 `f43134f70f865126b66e17c7daa97ecafe43b787` подтверждены четыре обязательных workflow: Reference Tests, Release Conformance Gate, Offline Edition и MVP Browser Tests — все PASS на одном HEAD. Это подтверждает техническое состояние проверенных gates, но не factual approval, rights clearance, editorial approval или допуск кандидатов.

## 3. Кандидаты по 19 главам — точные цепочки и решение о следующем шаге

Обозначения:
- **A — продвигать в следующую ограниченную remediation-очередь:** предметная основа достаточно перспективна; оставшиеся препятствия конкретны и обозримы.
- **B — резерв / продвигать после A:** есть полезный Claim, но остаётся более существенная source, wording, rights или dependency работа.
- **C — не ускорять:** существует конкретный содержательный, правовой или high-consequence blocker.
- Все позиции остаются **HOLD**. Буква очереди не является INCLUDE.

### Part I — «Выживание и сохранение жизни»

| Глава | Representative Claim → Evidence Use → Source | Очередь | Основание и следующий шаг |
|---:|---|:---:|---|
| 1. Чрезвычайные ситуации | `CLM-ALERTS-ENABLE-RESPOND@2` → `EU-ALERTS-ENABLE-RESPOND@2` → `SRC-RED-CROSS-ALERTS-2026@2` | A | Полезный explanatory материал о подготовке и понимании местных каналов оповещения. Сохранить географическую границу США; завершить точный page locator, currentness и source-specific rights review. Не расширять до универсальной эвакуационной инструкции. |
| 2. Вода | `CLM_WATER_RESOURCES_BASICS_A@1` → `EU-WATER_RESOURCES_BASICS-A@1` → `SRC-WATER_RESOURCES_BASICS@1` | C | Ранее зафиксирован substantive debt; generic Evidence Use не является единственным blocker. Не продвигать до предметного закрытия содержания и прямого USGS support. Отдельно не смешивать этот Claim с аварийной обработкой воды. |
| 3. Пища и продовольственная устойчивость | `CLM-FOOD_SECURITY_BASICS-A@1` → `EU-FOOD_SECURITY_BASICS-A@1` → `SRC-FOOD_SECURITY_BASICS@1` | A | FAO Handbook §1.4 прямо поддерживает базовое определение и различает availability, stability, access и biological utilization. Следующий шаг — versioned pinpoint EU, проверка условий конкретного FAO material и атрибуции; переиспользовать ранее завершённые substantive/Human View findings. Не превращать определение в индивидуальную диетическую рекомендацию. |
| 4. Укрытие и жильё | `CLM-SHELTER_BASICS-A@1` → `EU-SHELTER_BASICS-A@1` → `SRC-SHELTER_BASICS@1` | B | Claim A может быть полезным вводным объяснением, но текущий Ready.gov source — широкая точка входа. Нужен точный FEMA/Ready.gov locator и reader boundary. Claims B/C не fast-track: универсальные чек-листы выбора укрытия не поддержаны и могут конфликтовать с hazard-specific instructions. |
| 5. Здоровье и гигиена | `CLM-HANDWASH-20SEC@1` → `EU-HANDWASH-20SEC@1` → `SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1` | B | CDC emergency guidance прямо поддерживает 20 секунд; существует отдельный WHO corroboration track. Требуется точный locator в versioned EU, проверка CDC/WHO rights/disclaimer и qualified health/editorial review. Не расширять Claim до полной санитарной инструкции. |
| 6. Тепло, огонь и энергия | `CLM-ENERGY_BASICS-A@1` → `EU-ENERGY_BASICS-A@1` → `SRC-ENERGY_BASICS@1` | B | Это базовый Claim о кинетической энергии, а не инструкция по отоплению или генерации. Нужен точный OpenStax Physics locator и rights review именно этого издания. Не связывать его с безопасностью огня/электричества без отдельных доказательств. |
| 7. Инструменты и материалы | `CLM-MATERIALS_BASICS-A@1` → `EU-MATERIALS_BASICS-A@1` → `SRC-MATERIALS_BASICS@1` | B | NIST MSED overview поддерживает большую часть базовой связи measurement science, models, data и structure–property–processing. Нужен точный locator; проверить, что весь Claim не шире страницы. Source URI/identity и отдельные property claims требуют аккуратного source mapping. |
| 8. Сельское хозяйство и почва | `CLM-SOIL_BASICS-A@1` → `EU-SOIL_BASICS-A@1` → `SRC-SOIL_BASICS@1` | B | Исторический Source@1 восстановлен, Source@2 и EU-B@2 сохранены по Package G/H. Это закрывает version-storage defect и поддерживает отдельную линию Claim B, но не делает Claim A готовым: определение почвы, живые организмы и атрибуция Soil Taxonomy/SSSA требуют отдельной точной опоры. Не переносить EU-B@2 на Claim A/C. |
| 9. Природные опасности | `CLM-WEATHER_BASICS-A@1` → `EU-WEATHER_BASICS-A@1` → `SRC-WEATHER_BASICS@1` | A | NOAA и WMO прямо поддерживают определение погоды как состояния атмосферы в определённое время/месте. Но текущий source graph требует согласованной пятизаписной миграции Source/Claim/EU/Context/Scope, если выбирается новый NOAA page. Сохранить различие weather/climate; не подменять этим актуальный прогноз. |
| 10. Связь и навигация | `CLM-MAPS_AND_NAVIGATION_BASICS-A@1` → `EU-MAPS_AND_NAVIGATION_BASICS-A@1` → `SRC-MAPS_AND_NAVIGATION_BASICS@1` | A | USGS напрямую поддерживает назначение топографических карт, features, terrain и contours; Claim B о масштабе также имеет прямую поддержку. Подготовить точные versioned locators для A/B. Claim C шире имеющегося evidence и остаётся HOLD до прямой опоры на currency/field conditions или редакционного сужения. |

### Part II — фундаментальные и цивилизационные знания

| Глава | Representative Claim → Evidence Use → Source | Очередь | Основание и следующий шаг |
|---:|---|:---:|---|
| 11. Математика и измерения | `CLM-SI-SEVEN-BASE@1` → `EU-SI-SEVEN-BASE@2` → `SRC-NIST-SI-UNITS@1` | B / private-only | Самая зрелая точная семизаписная preview-цепочка; NIST locators различают seven defining constants и seven base units. Но существующая authorization разрешает только private non-release preview; трёхчитательская проверка ещё не выполнена. Не считать SI Claim публично готовым и не расширять private authorization. |
| 12. Физические науки | `CLM-MOTION_BASICS-A@1` → `EU-MOTION_BASICS-A@1` → `SRC-MOTION_BASICS@1` | A | OpenStax Physics §2.1 “Defining Motion” прямо поддерживает роль системы отсчёта. Нужен versioned pinpoint и rights review Physics title. Известная терминологическая проблема Claim B — отдельный blocker и не должна переноситься на Claim A или скрываться при навигации. |
| 13. Химические науки | `CLM-MIXTURES_AND_SOLUTIONS-A@1` → `EU-MIXTURES_AND_SOLUTIONS-A@2` → `SRC-MIXTURES_AND_SOLUTIONS@1` | C | Locator EU v2 указывает OpenStax Chemistry 2e §11.1 и прямо поддерживает однородность раствора. Однако CC BY-NC-SA / ограничения на LLM-ingestion и generative-AI use требуют письменного разрешения либо rights-compatible альтернативы. Не обходить blocker одним paraphrase. |
| 14. Науки о жизни | `CLM-CELL_BASICS-A@1` → `EU-CELL_BASICS-A@1` → `SRC-CELL_BASICS@1` | C | OpenStax Biology 2e даёт близкую базовую поддержку, но текущий EU generic, wording “structural and functional” требует точной поддержки, а лицензия/AI-ingestion restriction не закрыты. Искать rights-compatible source либо получать письменное разрешение; не менять Claim самовольно. |
| 15. Земля, климат и космос | `CLM-EARTH_SYSTEM_BASICS-A@1` → `EU-EARTH_SYSTEM_BASICS-A@1` → `SRC-EARTH_SYSTEM_BASICS@1` | C / резерв — Climate A | Earth System A имеет substantive classification issue: четыре против пяти spheres; locator patch не решит проблему. Более перспективная альтернатива для этой главы — `CLM-CLIMATE_BASICS-A@1`: NASA support найден, но EU/Source требуют versioned pinpoint proposal и проверки точного охвата. Не представлять Claim как полный разбор Earth system. |
| 16. Инженерия и вычисления | `CLM-DATABASES_BASICS-A@3` → `EU-DATABASES_BASICS-A@3` → `SRC-DATABASES_BASICS@3` | A | Один из наиболее зрелых bounded technical candidates: PostgreSQL 18.7 §2.2 прямо поддерживает Claim; Context/Scope ограничивают конкретную модель и версию. PostgreSQL 19 выпущен 2026-11-19, поэтому 18.7 нужно явно показывать как version-pinned example, не как последнюю версию. Завершить rights notice treatment и Human View; не обобщать на все базы данных. |
| 17. Науки о человеке | `CLM-LEARNING_BASICS-A@1` → `EU-LEARNING_BASICS-A@1` → `SRC-LEARNING_BASICS@1` | A / ограниченный | NIMH Learning and Memory Program прямо перечисляет encoding, consolidation, retrieval и working memory. Это поддерживает описание предмета исследовательской программы, а не универсальную исчерпывающую таксономию обучения. Нужен точный EU locator и сохранение representative/non-exhaustive boundary. Claims B/C остаются HOLD до прямых научных источников. |
| 18. Общество и институты | `CLM-ECONOMICS_BASICS-A@1` → `EU-ECONOMICS_BASICS-A@1` → `SRC-ECONOMICS_BASICS@1` | C | World Bank poverty page слишком косвенна для полного определения производства, распределения и использования товаров/услуг. Нужен другой прямой источник и повторный source-fit review. Не ускорять ради формального заполнения главы. |
| 19. История и культура | `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1` → `EU-ANCIENT_CIVILIZATIONS_BASICS-A@1` → `SRC-ANCIENT_CIVILIZATIONS_BASICS@1` | C / долгосрочный | Содержательно важный кандидат, но дополнительные corroboration EUs/Sources образуют более широкую зависимость, чем одна цепочка. Нужны полный multi-EU review, региональные/временные границы и проверка прав на конкретные источники. Не превращать разные общества в универсальную модель цивилизации. |

## 4. Дополнительные кандидаты, которые усиливают широту Part II

Эти кандидаты не заменяют 19-главную карту и не создают новую главу. Они уже присутствуют в существующих foundational screens и могут служить резервом:

| Кандидат | Exact Claim | Потенциал | Основной blocker |
|---|---|---|---|
| Climate Basics | `CLM-CLIMATE_BASICS-A@1` | Низкорисковое объяснение долгосрочных климатических характеристик; NASA support уже исследован | Versioned EU/Source pinpoint; различить long-term averages и changes; не расширять на все Earth-system mechanisms |
| Measurement Uncertainty | `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | Сильный фундаментальный принцип метрологии; NIST TN 1297 §2.1 напрямую поддерживает включение uncertainty в результат измерения | EU locator; различить legacy TN 1297 и maintained NIST guidance; сохранить BIPM/VIM dependency track и проверить полный slice |
| Statistics Basics | `CLM-STATISTICS_BASICS-A@1` | Потенциально полезное методологическое основание для всей Энциклопедии | Generic EU, возраст NIST/SEMATECH Handbook 151, item-level rights; OpenStax Statistics 2e license conflict и AI-ingestion restriction |
| Soil Basics Claim B | `CLM-SOIL_BASICS-B@1` | Практически значимый explanatory Claim о функциях почвы | EU-B@2 и Source@2 обновлены в Package G; нужна независимая опора и точное ограничение на вариативность разных почв |
| Emergency Water Claims | `CLM-WATER-BOILING-EFFECTIVE@1`, `CLM-WATER-BOILING-TIME@1`, `CLM-WATER-CHEMICAL-LIMIT@1`, `CLM-WATER-INDEPENDENT-CORROBORATION@1` | Высокая непосредственная полезность, CDC/EPA support и locator updates Package G | High-consequence safety review; CDC 6,500 ft и EPA 5,000 ft не смешивать; chemical/radioactive warning должен быть рядом с boiling guidance |
| Soil Basics Claims A/C | `CLM-SOIL_BASICS-A@1`, `CLM-SOIL_BASICS-C@1` | Важная фундаментальная связь с сельским хозяйством и экосистемами | Claim A — определение/organisms/SSSA attribution; Claim C — вариация по месту и глубине. Исторический Source@1 восстановлен, но это не закрывает evidence fit |

## 5. Сводная очередь следующего крупного этапа

### Очередь A — первые кандидаты для предметного продвижения

1. **Databases A** — лучший bounded technical candidate по прямоте locator и точности Context/Scope; сохранить PostgreSQL 18.7 boundary.
2. **Weather A** — прямое NOAA/WMO определение; требуется согласованная versioned source-graph migration.
3. **Food Security A** — прямой FAO §1.4; требуется pinpoint EU и rights review.
4. **Emergency Alerts** — содержательная Red Cross evidence track; закрыть page locator, актуальность и US boundary.
5. **Maps A/B** — прямой USGS support для двух отдельных Claims; подготовить versioned EU pinpoints.
6. **Motion A** — прямой OpenStax §2.1; отдельный Claim B не должен загрязнять Claim A.
7. **Learning A** — ограниченный NIMH program-scope Claim; точный locator и неуниверсальная формулировка.
8. **Climate A** — перспективный низкорисковый резерв для Earth/climate chapter после versioned EU/Source correction.

Эта очередь — следующая предметная remediation-последовательность, а не предложение автоматически включить восемь Claims в выпуск.

### Очередь B — продвижение после A или после отдельного решения

- Materials A;
- Soil B (с учётом Package G exact version);
- Hand Hygiene A;
- Shelter A;
- Energy A;
- Measurement Uncertainty A;
- SI Units A — только в пределах private preview authorization;
- Soil A/C и Emergency Water — только после своих отдельных evidence/safety boundaries.

### Очередь C — не ускорять и не маскировать локаторными исправлениями

- Water Resources A — substantive debt;
- Shelter B/C — hazard-dependent claims и потенциально опасное обобщение;
- Earth System A — unresolved four-vs-five spheres classification;
- Mixtures and Solutions — unresolved OpenStax rights/AI-ingestion restriction;
- Cell Basics — unresolved OpenStax rights/AI-ingestion restriction и точность wording;
- Statistics — rights/currentness conflict;
- Economics — insufficient direct source fit;
- Ancient Civilizations — multi-source dependency and historical editorial review.

## 6. Обязательные ограничения для следующего этапа

1. Не переводить ни одну запись из HOLD в INCLUDE на основании этой приоритизации.
2. Не создавать production allowlist из 19 representative Claims: shortlist — это стартовые кандидаты, а не полный dependency closure.
3. Для каждого продвигаемого Claim проверить точные версии всех зависимостей и target_ref Context/Scope; Evidence Use и Source должны поддерживать именно выбранный Claim.
4. Не переписывать canonical records без отдельного точного bounded owner authorization. Общая команда «продолжать работу» не расширяет Package G/H permissions.
5. Не менять Claim wording ради удобства источника; если формулировка шире доказательства, зафиксировать редакционное решение и оставить HOLD.
6. Не копировать сторонний текст, таблицы, изображения, карты, datasets или учебные материалы без конкретного правового основания. Public availability не равна redistribution permission.
7. High-consequence практические материалы — вода, санитария, медицина, огонь, электричество, строительство, химия и shelter actions — не fast-track без qualified review.
8. Не запускать новые M13 batches, не повторять закрытые Human View и не переаудировать весь корпус.
9. Сохранять Part I как открывающую самостоятельную часть и представлять Part II по всем девяти существующим цивилизационным доменам; не сужать Энциклопедию до survival-only manual или одной STEM-ветки.
10. PR #22 остаётся Draft; `main` не меняется; никакого merge, deployment или public release без отдельного решения владельца.

## 7. Точный выход Package I

- Сохранена 19-главная структура и representative Claim chain для каждой главы.
- Сведены в одну очередь 150 уже проверенных record files и дополнительные foundational screens.
- Выделены 8 первоочередных низко-/умеренно-рисковых кандидатов для следующего bounded remediation этапа.
- Отделены private-only SI, high-consequence water/health/shelter, rights-blocked OpenStax, substantive Earth System/Water Resources и слабый Economics source fit.
- Package G/H updates учтены; исторический Soil Source@1 не считается потерянным.
- Никакие canonical Content records, record versions, dispositions, Relations, candidate allowlist, production manifest, rights decisions или owner decisions этим пакетом не изменяются.

**Package I завершён как read-only candidate-prioritization deliverable.** Следующий этап по плану — ограниченная предметная редактура и доказательное закрытие кандидатов из Очереди A, с versioned proposals и точными authorization requests там, где требуется canonical write. После этого — отдельное закрытие прав и редакционной ответственности по существующему R-01–R-10 register; не смешивать эти этапы и не выдавать research priority за публикационное решение.
