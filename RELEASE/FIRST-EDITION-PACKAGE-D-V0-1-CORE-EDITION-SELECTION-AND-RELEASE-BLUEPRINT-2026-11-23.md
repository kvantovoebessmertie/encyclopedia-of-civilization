# Первая редакция — Package D: blueprint первой содержательной сборки v0.1

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: план ограниченного первого выпуска и точная последовательность сборки; не INCLUDE manifest и не release approval.

## 1. Принцип первой версии

Первая версия должна быть настоящей, небольшой и полезной Энциклопедией, а не пустой оболочкой на 385 срезов и не непроверенным дампом корпуса. Её задача — доказать полный путь от проверенного знания до понятной статьи, источника, ограничений, поиска и автономной работы.

Для этого не нужно:
- ждать завершения всех 1,494 M13 Claims;
- включать все 94 Part I или 385 Part II slices;
- заполнять все 19 глав ради формального покрытия;
- переносить исторические оценки;
- публиковать HOLD ради количества.

Нужно:
- выбрать небольшое число точных Claim versions из обеих частей;
- закрыть все прямые зависимости и source rights;
- дать понятный reader view;
- сохранить прозрачные ограничения и пустые главы;
- собрать и проверить воспроизводимый offline artifact.

## 2. Предлагаемый минимальный seed set

### Первая волна кандидатов — пять тематических входов

| Часть / глава | Candidate | Почему выбран | Главный блокер |
|---|---|---|---|
| Part I / 1 | CLM-ALERTS-ENABLE-RESPOND@2 | Практически полезное понимание местных каналов оповещения; содержательный Red Cross EU v2 | Rights/brand boundary Red Cross; точная версия источника и intended-use decision |
| Part I / 5 | CLM-HANDWASH-20SEC@1 | Конкретная, ограниченная гигиеническая рекомендация; CDC evidence и WHO corroboration | CDC attribution/disclaimer, third-party exclusion, international rights review; medical/editorial check |
| Part I / 9 | CLM-WEATHER_BASICS-A@1 | Низкорисковое фундаментальное определение погоды; NOAA direct locator найден | Versioned locator remediation, attribution/asset check |
| Part II / 11 | CLM-SI-SEVEN-BASE@1 | Точная NIST support chain и хорошая демонстрация evidence/reader | Текущая private preview authorization не разрешает публичную публикацию; нужны три reader reviews и отдельное public rights/release decision |
| Part II / 16 | CLM-DATABASES_BASICS-A@3 | PostgreSQL 18.7 §2.2 прямой locator, exact Context/Scope v3, license published | Verify canonical locator and include PostgreSQL license notice/disclaimers if documentation is redistributed; editor/Human View |

Это shortlist, а не решение INCLUDE. Все пять кандидатов остаются HOLD.

### Порядок подготовки

1. **Reader prototype:** завершён как offline navigation shell, но пока без статей.
2. **Evidence closure:** Package A содержит source/locator/rights findings для пяти из этих кандидатов.
3. **Rights decision:** владелец определяет distribution model и принимает R-01/R-02/R-05/R-06/R-07/R-08/R-09/R-10.
4. **Versioned remediation:** применяются только разрешённые обновления Evidence Use/Source; никаких несанкционированных Claim rewrites.
5. **Exact selection:** фиксируются выбранные ID/version/type/type_version/schema и прямые зависимости.
6. **Independent review:** профильная проверка и Human View на готовом reader view.
7. **Build:** selection-aware offline builder на clean checkout и точном source commit.
8. **Inspection:** проверка содержимого, ссылок, поиска, клавиатуры, мобильной ширины, offline, hash и отсутствия HOLD/private material.
9. **Approval:** release approver подписывает immutable artifact hash.
10. **Release:** только после всех gates и отдельного явного решения.

## 3. Рекомендуемый порядок включения

### Priority 1 — наиболее реалистичные после технической и правовой сверки

- PostgreSQL Claim A — ограниченное вводное объяснение одной конкретной СУБД; документация имеет явную PostgreSQL License.
- NOAA Weather Claim A — короткое фактическое определение; предпочтителен независимый paraphrase и ссылка на прямой NOAA explainer.
- CDC Handwashing Claim — конкретная emergency hygiene рекомендация; использовать только при соблюдении CDC use conditions и после проверки актуальности/территории.

### Priority 2 — после отдельного закрытия прав/полномочий

- Red Cross alerts — не копировать текст/бренд/медиа; решить, достаточно ли независимого paraphrase + link в принятой проектной политике.
- SI base units — не расширять существующую private preview authorization; получить отдельный public approval, rights evidence и завершить независимые reader reviews.

### Не включать в v0.1 до решения

- OpenStax Biology 2e, Chemistry 2e, World History Volume 1 — NC-SA + запрет LLM/generative AI ingestion without prior written permission; совместимость проекта не подтверждена.
- FAO content — коммерческое использование/адаптация/перевод требует permission; distribution model пока не утверждён.
- Motion Claim B — терминологическая неоднозначность.
- Water resources — ранее выявленный substantive debt.
- Любые высокорисковые процедуры по очистке воды, огню, электричеству, строительству, медицине и химии без квалифицированной проверки.

## 4. Минимальный критерий v0.1

Первая версия может быть ограниченной и иметь пустые главы. Минимальная содержательная сборка считается пригодной к release review только если:

- присутствуют не менее двух предметных областей Part I и двух Part II;
- каждая опубликованная статья содержит Claim, прямой Evidence Use → Source, правильные Context/Scope и locator;
- ни одна статья не зависит от HOLD/EXCLUDE/private preview record;
- все прямые dependencies exact-version pinned;
- все источники имеют recorded rights status для intended distribution;
- есть понятные дата/версия/атрибуция/ограничения;
- поиск и переходы работают offline;
- reader не показывает технические JSON вместо человеческого текста по умолчанию;
- production selection manifest schema 1.1 проходит fail-closed validation;
- независимый reviewer и accountable editor подтверждают содержание;
- release approver принимает точный artifact hash.

Число статей само по себе не является критерием готовности. Лучше 4–8 действительно проверенных материалов, чем 50 материалов с неполными правами или доказательствами.

## 5. Структура готового offline release

Предлагаемая структура артефакта:

- `index.html` — стартовая страница, статус выпуска и поиск;
- `chapters/` — главы и доступные статьи;
- `assets/` — только разрешённые локальные assets;
- `sources/` — ссылки и точные библиографические сведения, если они нужны локально;
- `edition-manifest.json` — edition ID, exact source commit, selection manifest digest, builder version, record hashes;
- `selection-manifest.json` — только одобренные exact-version records и dependencies;
- `ATTRIBUTION-AND-LICENSES.md` — item-level attribution and license notices;
- `CORRECTIONS.md` — реальный адрес/процесс corrections только после R-08;
- `SHA256SUMS` — контрольные суммы файлов и всего артефакта.

Нельзя включать в release:
- HOLD/EXCLUDE;
- внутренние audit reports и owner decision drafts;
- private preview artifacts;
- непроверенные third-party assets;
- source materials, которые разрешено только просматривать, но не распространять;
- пользовательские submissions до принятия contributor terms.

## 6. Build & inspection sequence

1. Freeze exact manifest на immutable commit.
2. Run content preflight.
3. Run reference tests and release conformance gate.
4. Run selected offline build in empty, non-symlinked output directory.
5. Compare selected IDs/hashes against the approved manifest.
6. Inspect every rendered article and its evidence/context/scope/source links.
7. Inspect navigation, search, keyboard operation, screen-reader labels, mobile layout and no horizontal overflow.
8. Verify no external network request is needed for offline use.
9. Verify no HOLD, private preview or undeclared dependency appears in artifact.
10. Verify attribution/license notices and correction contact.
11. Compute SHA-256 checksums and independent artifact inspection report.
12. Obtain release approver's recorded decision tied to the artifact hash.

CI PASS alone is not a release approval. A successful build proves packaging/declared closure, not factual truth, source fit, rights, expert review or editorial quality.

## 7. Что уже есть и чего ещё нет

**Есть:**
- 19-chapter reader structure;
- 19-chapter slice mapping;
- representative Claim shortlist;
- six-Claim source/rights package;
- science remediation package;
- internal offline navigation shell and tests;
- fail-closed exact-version selection builder.

**Нет:**
- owner decisions R-01–R-10;
- production INCLUDE manifest;
- public rights clearance for the proposed seed set;
- final versioned remediation commits;
- complete reviewer sign-offs;
- production reader consuming the approved selection;
- final reproducible release bundle and artifact inspection;
- release approver decision.

## 8. Explicit status

The v0.1 seed set is not approved for publication. The static shell is an internal navigation prototype. PR #22 remains Draft and unmerged. No deployment or public release is authorized by this blueprint.
