# Первая редакция — Package H: Soil history/CI closure и три приоритетных кандидата

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Исследованный branch HEAD: `3fe670795e397f4a6d4f85f8915e0ac80d5919a5`  
Статус: технический разбор точной причины CI failure + bounded owner-authorization request + предметная проверка трёх кандидатов. Никакие новые canonical Content records не изменялись.

## 1. Итог

Package G был применён в пределах шести одобренных versioned operations. После записи обнаружен не locator defect, а дефект сохранения истории версий Soil Source:

- `SRC-SOIL_BASICS@1` заменён текущим файлом `SRC-SOIL_BASICS@2`;
- Claim A/B/C и Evidence Use A/C продолжают ссылаться на `SRC-SOIL_BASICS@1`;
- старый Source snapshot физически отсутствует в текущем content tree;
- валидатор поэтому не может разрешить девять ссылок на Source@1.

Это не следует исправлять переписыванием Claims или массовым изменением ссылок: точная историческая версия Source@1 доступна в Git history и должна быть восстановлена как versioned historical snapshot, по образцу уже используемого в репозитории паттерна файлов `*-v1.json`.

Для этого требуется отдельное узкое owner approval на три файла: добавить исторический Source snapshot, синхронизировать два coverage counters и усилить существующий slice regression test. Этот пакет не считает предыдущее разрешение на шесть операций разрешением на эти три дополнительные операции.

Параллельно выполнен targeted source/rights screen для PostgreSQL, NOAA Weather и Emergency Hand Hygiene. PostgreSQL имеет наиболее точное Evidence Use, но требует актуальности версии и rights notice; Weather имеет точный внешний support, но текущая canonical EU не содержит locator и source graph нуждается в согласованном version migration; Hand Hygiene имеет точный CDC support, но нуждается в locator и международной rights/editorial проверке. Все три остаются HOLD.

## 2. Точный CI diagnosis на HEAD 3fe6707

### 2.1 Wave-safety finding — закрыт в реестре авторизаций

На предыдущем report-bearing HEAD `4508b356651898337a3bd6a3f0dac4ec57585585` preflight завершался:

`wave-safety: existing vertical slice modified without explicit editorial correction authorization: soil-basics, water`.

Проверка кода `REFERENCE/preflight_content.py` показала, что wave-safety guard сравнивает изменённые срезы с массивом `authorized_slices` из `RELEASE/EDITORIAL-CORRECTION.json`.

В ответ на точный Package G approval в authorization register добавлена запись:
`PACKAGE-G-WATER-SOIL-EU-LOCATOR-REMEDIATION-2026-11-23`.
В `authorized_slices` внесены только необходимые для этого preflight slug: `soil-basics` и `water`. В записи перечислены ровно шесть canonical files Package G, шесть разрешённых version bumps и запреты на Claim/disposition/rights/release changes.

После этой записи wave-safety finding исчез. Это не расширяет разрешение на будущие изменения внутри этих срезов: реестр содержит точный список разрешённых файлов и операций, а отдельная авторизация по-прежнему нужна для любой дополнительной canonical write.

### 2.2 Новый и единственный содержательный preflight blocker

На HEAD `3fe670795e397f4a6d4f85f8915e0ac80d5919a5` оба завершившихся `build-and-test` прогона остановились на content package/recovery preflight. Сообщения:

- `VAL-L3-REFERENCE-VERSION`
- `SRC-SOIL_BASICS@1`
- `STORAGE-VERSION-NOT-FOUND`

Найдено девять unresolved references:
- `CLM-SOIL_BASICS-A@1` — provenance.created_from → Source@1;
- `CLM-SOIL_BASICS-B@1` — provenance.created_from → Source@1;
- `CLM-SOIL_BASICS-C@1` — provenance.created_from → Source@1;
- `EU-SOIL_BASICS-A@1` — provenance.created_from и content.source_ref → Source@1;
- `EU-SOIL_BASICS-C@1` — provenance.created_from и content.source_ref → Source@1;
- остальные сообщения валидатора относятся к дополнительным зависимостям тех же records; `EU-SOIL_BASICS-B@2` уже корректно ссылается на Source@2.

Фактический текущий набор Soil records содержит 9 JSON files. Source@1 в них больше не присутствует; Source@2 присутствует. Исторический файл Source@1 был повторно извлечён из Git на commit `e2995d82d4e945b3afd8450959303d25e9c70231`:
- historical blob SHA: `e09d755f7590476c0ebe4ac4dec40d562e1c2e5b`;
- current Source@2 blob SHA: `d56da42a8aeb693f282dfbf30df139ede21bcac1`.

Это точное исходное содержимое Source@1, без редакторских изменений:

```json
{"record_version":"1","type_version":"1.0","publication_status":"published","completion_status":"complete","schema":"record/0.1","record_id":"SRC-SOIL_BASICS","record_type":"source","provenance":{"method":"external_official_source"},"content":{"source_identity":"USDA NRCS — Soils","representation":"official/public reference","external_ref":{"uri":"https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/soils"},"availability":"public","preservation":"external canonical source; local corpus stores identity and locator"}}
```

### 2.3 Предлагаемая точная коррекция — REQUEST ONLY

Предлагается отдельное разрешение ровно на следующие три файла:

1. Добавить `CONTENT/vertical-slices/soil-basics/records/SRC-SOIL_BASICS-v1.json` с точным historical Source@1 snapshot, приведённым выше. Не менять текущий `SRC-SOIL_BASICS.json` (Source@2) и не переписывать ни одну ссылку на Source@1.
2. Обновить `RELEASE/CONTENT-COVERAGE.json`:
   - `total_records: 4763 → 4764`;
   - `types.source.count: 603 → 604`;
   - все остальные counts, 479 slices, type registry и coverage narrative оставить неизменными.
3. Обновить существующий `REFERENCE/tests/test_content_soil_basics_vertical_slice.py`:
   - ожидать 10 файлов;
   - проверять наличие одного source record ID с версиями 1 и 2;
   - проверять, что historical v1 URI сохранён точно;
   - проверять, что текущий Source v2 URI остаётся NRCS “What is Soil?”;
   - сохранять проверку трёх Claims и трёх Evidence Use records, их identity и links.

Запрещено в рамках этой коррекции:
- менять Claims A/B/C или их wording/version;
- менять EU A/C, EU-B@2, Context или Scope;
- менять текущий Source@2;
- менять HOLD, publication_status или completion_status;
- менять любые другие slice/record/coverage values;
- добавлять INCLUDE/allowlist, выпускать preview/public artifact, менять main или merge PR.

Цель — восстановить разрешимость ранее существовавших exact-version references, не менять смысл и не расширять Package G.

**Owner approval: NOT YET RECEIVED. Никакая из трёх операций выше не выполнена.**

## 3. Три кандидата: предметная проверка на текущих exact versions

### 3.1 PostgreSQL / Databases

Текущие exact records:
- `CLM-DATABASES_BASICS-A@3`, blob `1c8b23390631fb46e616a1c5da3fede4f0866059`;
- `EU-DATABASES_BASICS-A@3`, blob `aba2fc9ed582c231776a5a12b9132a5919d8dc49`;
- `SRC-DATABASES_BASICS@3`, blob `c54bd1610b150beefc5f2689b1a98e1774b922b7`;
- `CTX-DATABASES_BASICS@3`, blob `4754fe1c935e1f12b98dd5a9a1c19a65ee134080`;
- `SCP-DATABASES_BASICS@3`, blob `80dbfd2ec86e9783d21be9c113ecd3d781981cc5`.

**Evidence fit: STRONG.** PostgreSQL 18.7 Tutorial §2.2 “Concepts” directly defines PostgreSQL as a relational database management system, explains that it manages data stored in relations, and identifies a relation as essentially a mathematical term for a table. It also describes tables, rows, columns and data types. This directly supports the bounded Claim wording. Exact URL: https://www.postgresql.org/docs/18/tutorial-concepts.html

**Currentness boundary:** PostgreSQL 19 was announced as released on 2026-11-19; PostgreSQL 18 remains a supported major version and 18.7 is the current 18-series documentation snapshot inspected here. The canonical Context/Scope already limits the slice to PostgreSQL 18.7. The Claim itself speaks about PostgreSQL generally. Before public inclusion, either:
- explicitly retain the educational proposition as a PostgreSQL 18.7-versioned example, making the displayed context unmistakable; or
- perform a new exact-source review against PostgreSQL 19 and authorize a coordinated version migration.

Do not imply that the 18.7 tutorial is documentation for PostgreSQL 19.

**Rights:** PostgreSQL's official License expressly permits use, copying, modification and distribution of its software and documentation for any purpose, including commercial use, subject to retaining the copyright notice and the licence's three following paragraphs in all copies. Official terms: https://www.postgresql.org/about/licence/. If the edition only paraphrases facts and links to the documentation, the precise reproduction trigger should be reviewed; if any documentation text is reproduced, include the complete required notice/disclaimer. No copied text, diagrams or images are proposed in this screen.

**Decision:** best current candidate for a tightly bounded technical article, but remains HOLD pending the 18.7-vs-19 editorial choice, applicable rights notice decision, release Human View and owner/editor approval. The existing EU pinpoint is already exact; do not repeat its locator remediation.

### 3.2 Weather basics

Current exact records:
- `CLM-WEATHER_BASICS-A@1`, blob `3279256471421ea51a50abd01454a1309d9cfc6d`;
- `EU-WEATHER_BASICS-A@1`, blob `2a4c116ed9067211a1d2320d044cf539436658fc`;
- `SRC-WEATHER_BASICS@1`, blob `4788dff0b49183302c566f58bc4ed64c3d76ba32`;
- `CTX-WEATHER_BASICS@1`, blob `88f84ec4814dfbc8e42364e5668b20a16acc2847`;
- `SCP-WEATHER_BASICS@1`, blob `d8fbdfff076ba17149df6e02aa3f28007dfcc3c6`.

Claim: “Погода описывает состояние атмосферы в конкретном месте и времени.”

**Evidence fit: STRONG for the proposition.** NOAA's current explainer states that weather and climate describe the state of the atmosphere at different timescales and defines weather as the state of the atmosphere at a particular location over the short term. Exact passage: heading “How is weather different from climate?” and following definition, lines 33–56 of the inspected page. URL: https://www.noaa.gov/explainers/what-s-difference-between-climate-and-weather. WMO independently defines weather as the state of the atmosphere at a particular time, using meteorological elements such as temperature, precipitation, pressure, wind and humidity: https://public.wmo.int/themes/weather.

**Canonical gap:** current Evidence Use has no `content.material.locator`; its description is generic. Current Source points to a broad NOAA “Weather & Atmosphere” resource collection rather than the directly inspected definition page. To use the exact current NOAA page, the graph needs coordinated exact-version changes because Claim provenance, EU source_ref, and Context/Scope target references are version-pinned. The proposed graph migration is:
- Source@1 → @2, exact NOAA explainer identity/URI;
- Claim@1 → @2, same statement, provenance aligned to Source@2;
- Evidence Use@1 → @2, pinpoint “How is weather different from climate?” and the definition paragraph;
- Context@1 → @2, target Claim@2;
- Scope@1 → @2, target Claim@2.
No wording change to the Claim is proposed. This is a five-record migration request only; not authorized or applied.

**Rights:** NOAA states that nearly all NOAA content is public domain, but users must verify page/item credits, credit NOAA/program and individual where listed, avoid implied endorsement, and disclose edits including generative-AI edits. The inspected NOAA explainer includes images with separate image credits; no image or other asset is proposed for reuse. Policy: https://www.noaa.gov/office-education/outreach-communication/faq. The page itself is suitable for independent factual paraphrase + attribution/link, subject to item-level review and project policy.

**Decision:** high-priority low-risk candidate after five-record exact-version migration, item-level rights review and release Human View. HOLD until then.

### 3.3 Emergency hand hygiene

Current exact records:
- `CLM-HANDWASH-20SEC@1`, blob `f5bf1ee347c9fd0befbbc49e2ced1f2ca58d8d75`;
- `EU-HANDWASH-20SEC@1`, blob `f0e9443f32c539105d6a9f8ff950a78563b16dea`;
- `EU-HANDWASH-20SEC-WHO@1`, blob `9735038b0a5c91c45d3a3cfc099d831d586cb147`;
- `SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1`, blob `1ed6c5b8a82cba02b27039391e0f1bdecf26c5d0`;
- Context@1 blob `0e06b06c3dde2107159c8d1c30e66f82d2d51829`;
- Scope@1 blob `c542acea7c1387a25c341c9227ca4d1e9451c3da`.

Claim: “Во время чрезвычайной ситуации CDC рекомендует мыть руки с мылом и водой не менее 20 секунд.”

**Evidence fit: STRONG.** CDC emergency personal hygiene guidance, dated 2024-08-05, has a “Wash your hands” section and says to wash with soap and water for at least 20 seconds, especially at key times. Exact page: https://www.cdc.gov/water-emergency/safety/guidelines-for-personal-hygiene-during-an-emergency.html, section “Wash your hands”. It also gives material adjacent boundaries: use boiled/disinfected water if local authorities or a doctor recommend extra caution; during a boil-water or do-not-drink advisory it may be safe to wash with tap water; sanitizer is an alternative when soap and water are unavailable but has limitations. Those details must not be silently omitted if the reader presentation broadens beyond the single 20-second Claim.

**Canonical gap:** EU currently describes the section but has no pinpoint locator. A narrowly scoped EU@1 → @2 update can add the exact “Wash your hands” locator and preserve Claim@1/Source@1. The separate WHO corroboration also has no pinpoint in its current record; it should remain a separate corroboration path and must not be represented as independently reverified in this task.

**Rights:** CDC says most CDC material is public domain, but contractor/grantee/third-party content and state/local material may be protected; attribution and a prominent non-endorsement disclaimer are required. CDC specifically warns that copyright protection may differ internationally. Policy: https://www.cdc.gov/Other/imagereuse.html. No CDC image, logo, copied prose or media is proposed. International distribution still requires an item-level rights decision and project policy.

**Editorial/safety boundary:** this is a health-adjacent public-health recommendation. Keep it as a source-attributed description of CDC guidance, not a universal guarantee or substitute for local emergency/health authority directions. The existing scope excludes specialized healthcare-facility hand hygiene; preserve that exclusion. A qualified health/editorial reviewer should inspect the final reader view.

**Decision:** candidate for the opening survival section after EU pinpoint remediation, source/rights review, international applicability note and qualified Human View. HOLD until those gates close.

## 4. Prioritization after this screen

| Rank | Candidate | Evidence readiness | Remaining minimum work | Current decision |
|---:|---|---|---|---|
| 1 | PostgreSQL 18.7 Claim A | Exact pinpoint already present | Resolve 18.7 vs 19 display boundary; rights notice treatment; Human View/editor | HOLD |
| 2 | NOAA Weather Claim A | Exact external support found; canonical EU generic | Coordinated 5-record source/Claim/EU/Context/Scope migration; rights/reader check | HOLD |
| 3 | CDC Handwashing Claim | Direct emergency-specific support found | EU locator v2; CDC international rights/disclaimer review; qualified health/editorial review | HOLD |

These are prioritization results, not INCLUDE decisions. No public selection manifest should be created from this table.

## 5. Exact next authorization requests

### Request H1 — restore Soil Source@1 historical snapshot

Approve only:
- add `SRC-SOIL_BASICS-v1.json` with the exact historical Source@1 JSON in §2.2;
- update `CONTENT-COVERAGE.json` from 4,763 to 4,764 total records and Source count from 603 to 604, leaving every other value unchanged;
- update the existing Soil regression test to expect 10 records and assert both exact Source versions/URIs.

All nine previously pinned references to Source@1 remain unchanged. Source@2 remains current. No Claim/EU/Context/Scope changes.

### Request H2 — Weather exact source graph migration

Approve only the five version bumps and reference alignments listed in §3.2. The Claim statement is unchanged. No additional Source, no relation, no disposition and no rights/allowlist changes.

### Request H3 — Hand Hygiene pinpoint

Approve only `EU-HANDWASH-20SEC@1 → @2` adding the exact CDC “Wash your hands” locator and preserving the current Claim@1 and CDC Source@1 links. No Claim rewrite, no Source or WHO record change.

No approval for H1, H2 or H3 is implied by the general instruction to continue work or by Package G's completed authorization. Until explicit approval, no canonical writes will be made for these requests.

## 6. Verification and boundaries

- Package G six writes: applied and post-write re-fetched; all affected Claims remain HOLD.
- Package G owner authorization: recorded in `RELEASE/EDITORIAL-CORRECTION.json` under exact bounded entry.
- Exact-head preflight on `3fe6707...`: wave-safety passes; content package/recovery fails because Source@1 historical snapshot is missing.
- `build-and-test`: FAIL on the exact HEAD due to nine unresolved `SRC-SOIL_BASICS@1` references.
- Reference Tests, Release Gate and Browser Form workflows were still in progress at the last status check; no exact-head PASS is claimed.
- No local test suite was run.
- No Claim, Evidence Use, Source, Context, Scope, Relation, assessment, inference, decision, INCLUDE/HOLD/EXCLUDE, selection manifest or production allowlist was changed in this Package H task.
- No merge, rebase, PR retargeting, main-branch update, deployment or public release.
- PR #22 remains OPEN / DRAFT / NOT MERGED.

## 7. Source references inspected

- NOAA, “What’s the difference between climate and weather?” — https://www.noaa.gov/explainers/what-s-difference-between-climate-and-weather
- WMO, “Weather” — https://public.wmo.int/themes/weather
- NOAA, “Using NOAA content” — https://www.noaa.gov/office-education/outreach-communication/faq
- PostgreSQL 18.7 Tutorial §2.2 — https://www.postgresql.org/docs/18/tutorial-concepts.html
- PostgreSQL License — https://www.postgresql.org/about/licence/
- CDC, “Guidelines for Personal Hygiene During an Emergency” — https://www.cdc.gov/water-emergency/safety/guidelines-for-personal-hygiene-during-an-emergency.html
- CDC, “Use of Agency Materials” — https://www.cdc.gov/Other/imagereuse.html

