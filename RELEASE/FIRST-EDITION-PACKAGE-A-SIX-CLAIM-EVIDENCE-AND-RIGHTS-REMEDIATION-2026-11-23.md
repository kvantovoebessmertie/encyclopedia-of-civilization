# Первая редакция — Package A: шесть Claim-кандидатов, точные локаторы и rights remediation

Дата проверки внешних источников: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: доказательная и правовая remediation-записка; не canonical edit, не INCLUDE и не разрешение на публикацию.

## 1. Назначение

Пакет закрывает наиболее перспективную часть shortlist: SI base units, PostgreSQL relational model, emergency hand hygiene, disaster alerts, food security и weather. Для каждого кандидата проверены актуальная страница источника, конкретный поддерживающий раздел/пассаж, границы утверждения и опубликованные условия использования источника.

Проверка не меняет JSON-записи. Предлагаемые формулировки Evidence Use — текст для будущего versioned change после проверки полномочий и schema. Все шесть кандидатов остаются HOLD.

## 2. Сводная таблица

| Глава | Claim@version | Evidence Use@version | Source@version | Вывод |
|---|---|---|---|---|
| 11 — SI | CLM-SI-SEVEN-BASE@1 | EU-SI-SEVEN-BASE@2 | SRC-NIST-SI-UNITS@1 | Доказательный locator точный; private preview не равен public release |
| 16 — Базы данных | CLM-DATABASES_BASICS-A@3 | EU-DATABASES_BASICS-A@3 | SRC-DATABASES_BASICS@3 | Точная опора в PostgreSQL 18.7 §2.2; сильный bounded candidate |
| 5 — Гигиена | CLM-HANDWASH-20SEC@1 | EU-HANDWASH-20SEC@1 и WHO corroboration | SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1 | CDC прямо подтверждает минимум 20 секунд; актуальность и локальная применимость должны быть явно ограничены |
| 1 — Оповещения | CLM-ALERTS-ENABLE-RESPOND@2 | EU-ALERTS-ENABLE-RESPOND@2 | SRC-RED-CROSS-ALERTS-2026@2 | Red Cross прямо поддерживает локальные каналы оповещения и различение watch/warning; claim не следует расширять |
| 3 — Продовольственная безопасность | CLM-FOOD_SECURITY_BASICS-A@1 | EU-FOOD_SECURITY_BASICS-A@1 | SRC-FOOD_SECURITY_BASICS@1 | FAO §1.4 поддерживает определение; rights terms FAO ограничивают reuse в коммерческих продуктах без разрешения |
| 9 — Погода | CLM-WEATHER_BASICS-A@1 | EU-WEATHER_BASICS-A@1 | SRC-WEATHER_BASICS@1 | NOAA weather/climate explainer напрямую поддерживает определение; использовать текстовый paraphrase и прямую ссылку |

## 3. Candidate A — SI: семь базовых единиц

**Текущая точная цепочка**
- Claim: `CLM-SI-SEVEN-BASE@1`
- Evidence Use: `EU-SI-SEVEN-BASE@2`
- Source: `SRC-NIST-SI-UNITS@1`
- Context: `CTX-SI@1`
- Scope: `SCP-SI@1`

**Подтверждение.** NIST SI Units page содержит разделы “Defining Constants” и “Base and Derived Units”. Первый называет семь defining constants. Второй прямо указывает, что SI состоит из семи базовых единиц, определения которых выражены через фиксированные значения констант. NIST также отдельно описывает 22 производные единицы со специальными именами и символами; это не общее число всех возможных производных единиц. <https://www.nist.gov/pml/owm/metric-si/si-units>

**Результат.** Существующий EU v2 содержит оба точных раздела и предостережение не смешивать семь базовых единиц с семью определяющими константами. Доказательная формулировка достаточна для Claim A без расширения.

**Rights.** Общая политика NIST говорит, что информация на сайтах NIST, если отдельно не помечена как copyrighted, считается публичной и может распространяться с надлежащей атрибуцией. Для отдельных продуктов и материалов могут действовать специальные условия; логотипы/изображения не следует автоматически включать. <https://www.nist.gov/copyrights-disclaimers>

**Ограничение.** SI preview authorization покрывает только семь exact-version записей, внутреннее private review, offline, non-redistributable. Три независимых читательских review ещё не выполнены. Никакой public release из этой проверки не следует.

**Disposition:** HOLD — evidence locator substantially closed; preview review, item-level rights check, project rights and owner release decisions remain open.

## 4. Candidate B — PostgreSQL relational model

**Текущая точная цепочка**
- Claim: `CLM-DATABASES_BASICS-A@3`
- Evidence Use: `EU-DATABASES_BASICS-A@3`
- Source: `SRC-DATABASES_BASICS@3`
- Context: `CTX-DATABASES_BASICS@3`
- Scope: `SCP-DATABASES_BASICS@3`

**Claim.** PostgreSQL — реляционная СУБД, управляющая данными, хранящимися в relations, которые в данном контексте представлены таблицами.

**Точный locator.** PostgreSQL 18.7 Documentation, Part I, Chapter 2, §2.2 “Concepts”. Раздел определяет PostgreSQL как RDBMS, объясняет relation как математический термин для table, а далее — таблицу как набор строк с одинаковым набором именованных колонок и типами данных. <https://www.postgresql.org/docs/18/tutorial-concepts.html>

**Предложение для Evidence Use description (не canonical edit):**

> PostgreSQL 18.7 Documentation, Part I, Chapter 2, §2.2 “Concepts” identifies PostgreSQL as a relational database management system and explains that a relation is essentially a table. The same section describes a table as a named collection of rows with named columns and column data types. This supports the bounded Claim about PostgreSQL's relational model; it does not generalize the statement to every database system or storage model. Source attribution: PostgreSQL Global Development Group, PostgreSQL 18.7 Documentation, §2.2.

**Rights.** PostgreSQL official license page explicitly grants permission to use, copy, modify and distribute the software and its documentation for any purpose, without fee, provided the required copyright notice, license paragraph and disclaimers appear in copies. <https://www.postgresql.org/about/licence/>

**Ограничение.** В будущей публикации достаточно сохранить attribution/license text в соответствии с точным intended use; не копировать лишние страницы документации. Проверить, что Source record фиксирует version 18.7 и что URI остается точным. Existing Context/Scope v3 correctly limits this Claim to introductory relational concepts and PostgreSQL 18.7.

**Disposition:** HOLD — evidence fit is strong; confirm source-version pin, exact license notice placement, editor/Human View and project-level approvals.

## 5. Candidate C — мытьё рук во время чрезвычайной ситуации

**Текущая точная цепочка**
- Claim: `CLM-HANDWASH-20SEC@1`
- CDC Evidence Use: `EU-HANDWASH-20SEC@1`
- Source: `SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1`
- Отдельная WHO corroboration: `EU-HANDWASH-20SEC-WHO@1` → `SRC-WHO-HYGIENE-EMERGENCY-2013@1`

**Точный locator.** CDC, “Guidelines for Personal Hygiene During an Emergency”, опубликовано 5 августа 2024 года, раздел “Wash your hands”. CDC рекомендует мыть руки с мылом и водой не менее 20 секунд, особенно в ключевые моменты, когда вероятность распространения микробов выше. <https://www.cdc.gov/water-emergency/safety/guidelines-for-personal-hygiene-during-an-emergency.html>

**Поддержка.** Claim ограничен рекомендацией CDC в emergency context. EU description можно конкретизировать разделом “Wash your hands” и датой страницы. Не расширять Claim до эффективности всех антисептиков, пригодности любой воды, медицинской профилактики или универсальных санитарных правил.

**Rights.** CDC указывает, что большая часть материалов CDC/ATSDR не защищена авторским правом и находится в public domain, но возможны исключения для подрядчиков, грантополучателей и третьих сторон. Для публичного использования требуются атрибуция CDC, disclaimer об отсутствии endorsement, сохранение substantive content и указание, что материал доступен бесплатно на сайте CDC. CDC также рекомендует прямые ссылки на ресурс и проверку обновлений. <https://www.cdc.gov/other/agencymaterials.html>

**Важная международная оговорка.** Политика CDC прямо отмечает, что защита федеральных материалов США за пределами США может отличаться в других юрисдикциях. Для глобального распространения требуется отдельная rights review по территории и выбранной форме использования.

**Disposition:** HOLD — direct support confirmed; rights record must document the exact CDC page, attribution/disclaimer, third-party asset exclusion, free-source link and international distribution review.

## 6. Candidate D — подготовка к местным оповещениям

**Текущая точная цепочка**
- Claim: `CLM-ALERTS-ENABLE-RESPOND@2`
- Evidence Use: `EU-ALERTS-ENABLE-RESPOND@2`
- Source: `SRC-RED-CROSS-ALERTS-2026@2`

**Точный locator.** American Red Cross, “Be Informed”, раздел “Be Informed”. Страница советует выяснить, как местные органы власти будут уведомлять людей во время бедствия и через какие каналы получать информацию (local radio, TV, NOAA Weather Radio); различать weather alerts “watches” и “warnings” и знать действия, связанные с каждым типом. <https://www.redcross.org/get-help/how-to-prepare-for-emergencies/be-informed.html>

**Поддержка и границы.** Существующий Claim v2 уже ограничивает рекомендацию контекстом подготовки в США. EU v2 корректно говорит о местных каналах и watch/warning. Он прямо не утверждает, что пользователь должен включить мобильные уведомления; такую рекомендацию нельзя добавлять без другого источника.

**Rights.** В ходе этой проверки не найдено достаточного официального разрешения Red Cross на воспроизведение/адаптацию текста в будущей коммерческой или международной редакции. Использовать только самостоятельный фактический paraphrase и ссылку — всё равно не заменяет документированного решения по правам на предполагаемый способ публикации. Не копировать текст, карточки, изображения, графику, логотипы или брендовые элементы Red Cross без отдельного разрешения.

**Disposition:** HOLD — factual support strong; item-level reuse terms and Red Cross brand/asset exclusions must be documented; project rights policy must decide whether external links + independent paraphrase are acceptable.

## 7. Candidate E — продовольственная безопасность

**Текущая точная цепочка**
- Claim: `CLM-FOOD_SECURITY_BASICS-A@1`
- Evidence Use: `EU-FOOD_SECURITY_BASICS-A@1`
- Source: `SRC-FOOD_SECURITY_BASICS@1`
- Context: `CTX-FOOD_SECURITY_BASICS@1`
- Scope: `SCP-FOOD_SECURITY_BASICS@1`

**Точный locator.** FAO, “Handbook for Defining and Setting up a Food Security Information and Early Warning System”, §1.4 “Definition of Food Security”. В нём приводится определение, принятое World Food Summit в 1996 году: физический и экономический доступ всех людей во все времена к достаточной, безопасной и питательной пище, отвечающей их потребностям и предпочтениям. <https://www.fao.org/4/x8622e/x8622e04.htm>

**Поддержка.** Claim о физическом и экономическом доступе, достаточной, безопасной и питательной пище поддержан напрямую. Context добавляет важные измерения доступности, доступа и стабильности во времени; Scope запрещает выдавать материал за текущую оценку продовольственной ситуации, политическую рекомендацию или индивидуальную диетическую рекомендацию.

**Предложение для EU description (не canonical edit):**

> FAO, Handbook for Defining and Setting up a Food Security Information and Early Warning System, §1.4 “Definition of Food Security”, reproduces the 1996 World Food Summit definition, including physical and economic access to sufficient, safe and nutritious food. This supports the bounded definition in the linked Claim. The source also identifies availability, stability and access as classic aspects; do not treat this section as a current assessment of any country or household. Source attribution: FAO, §1.4.

**Rights blocker.** Условия FAO разрешают копирование/использование обычного web content и публикаций для private study, research, teaching и non-commercial products/services при надлежащей атрибуции и отсутствии подразумеваемого endorsement. Для commercial use, resale, translation/adaptation rights требуется запрос разрешения. FAO также предупреждает, что отдельные компоненты могут принадлежать третьим лицам. <https://www.fao.org/contact-us/terms/en/>; <https://www.fao.org/publications/about-fao-publishing/permissions/en>

**Disposition:** HOLD — evidence locator closed; intended project distribution must be explicitly classified. If commercial/resale/adaptation is intended, request written FAO permission or select a rights-compatible independent source.

## 8. Candidate F — определение погоды

**Текущая точная цепочка**
- Claim: `CLM-WEATHER_BASICS-A@1`
- Evidence Use: `EU-WEATHER_BASICS-A@1`
- Source: `SRC-WEATHER_BASICS@1`
- Context: `CTX-WEATHER_BASICS@1`
- Scope: `SCP-WEATHER_BASICS@1`

**Новый прямой NOAA locator.** NOAA, “What’s the difference between climate and weather?” раздел “How is weather different from climate?” определяет weather как состояние атмосферы в конкретном месте в краткосрочном масштабе; погода может быстро меняться во времени и на коротких расстояниях. <https://www.noaa.gov/explainers/what-s-difference-between-climate-and-weather>

**Предложение.** Для Claim “Погода описывает состояние атмосферы в конкретном месте и времени” этот NOAA explainer является более точной опорой, чем общий образовательный collection page. Предлагается versioned Source/Evidence Use remediation с locator на указанный раздел. Claim не следует расширять до прогноза, климата, причин изменения погоды или локальных оперативных предупреждений.

**Rights.** NOAA указывает, что большая часть информации National Ocean Service является публичной информацией и может копироваться/распространяться, если не отмечено иное; необходимо указывать NOAA, не создавать впечатление endorsement и не выдавать изменённый материал за официальный. Конкретная страница и отдельные embedded assets всё равно требуют проверки отметок/credits. <https://oceanservice.noaa.gov/disclaimer.html>; <https://oceanservice.noaa.gov/about/faq.html>

**Disposition:** HOLD — direct factual support found; update source locator/version under authorized change control, preserve NOAA attribution and exclude third-party assets.

## 9. Приоритет после Package A

### Можно быстро завершать по доказательствам
1. PostgreSQL 18.7 §2.2 — exact source fit and permissive documentation license; check exact license notice and reader view.
2. SI base units — exact NIST sections; complete private review only.
3. CDC hand hygiene — direct locator and source-use requirements; complete international rights assessment.
4. NOAA weather — direct locator; confirm item-level credits and create authorized versioned update.

### Зависит от прав / отдельного решения
5. FAO food security — request permission if intended distribution is commercial/resale/adaptation, otherwise explicitly document non-commercial scope.
6. Red Cross alerts — no reproduction/brand assets; project must decide acceptable source treatment and rights evidence.

## 10. Release gate

Для каждого из шести Claim остаются обязательными:
- exact current canonical versions and schema/type pins;
- complete dependency closure, including all required corroboration tracks;
- correct Context/Scope target references;
- item-level rights evidence for intended jurisdictions and distribution model;
- editorial and qualified review appropriate to consequence;
- independent Human View and accessible reader rendering;
- explicit INCLUDE and APPROVED attestation from authorized approver;
- approved project-level R-01–R-10 decisions;
- inclusion in frozen exact-version manifest and clean reproducible build.

Ни один кандидат не переводится в INCLUDE этим документом. Никакие canonical records, record versions, candidate statuses, rights decisions, allowlist, production build, PR merge или main branch не изменены.
