# Первая редакция — Package L: owner decision sheet для R-01–R-10

Дата: 2026-11-27  
PR #22: OPEN / DRAFT / NOT MERGED  
Исходный HEAD: `43907755e7366e8e0c5ab526e5b5e65cb39000f0`  
Статус: READ-ONLY DECISION PACKET. Не содержит решений владельца, не выбирает лицензию, не назначает лиц, не отправляет permissions requests.

## 1. Зачем нужен этот пакет

Package K завершил source-level rights screen для 19 представительских кандидатов. Он выявил, что права источников нельзя свести к одному универсальному разрешению. Но даже permissive source license не отвечает на вопрос, кто владеет оригинальными материалами Энциклопедии и под какими условиями их можно распространять.

В авторитетном регистре `FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER-2026-11-19.md` все R-01–R-10 остаются OPEN. Package L переводит эти десять пунктов в короткий набор конкретных решений, вариантов и последствий для первого выпуска.

**Решения должен принять уполномоченный владелец проекта.** Наличие этого документа, GitHub commits, авторство записей, использование AI-инструментов или роль ChatGPT не позволяют вывести правообладателя, лицензию, редактора или release approver.

## 2. Фактическое состояние репозитория

На исходном HEAD `43907755e7366e8e0c5ab526e5b5e65cb39000f0` проверено:

1. В корне репозитория не обнаружены файлы `LICENSE`, `COPYING` или отдельный content/data license notice. Это не доказывает отсутствие прав у конкретного автора, но означает, что публичная лицензия проекта в репозитории явно не зафиксирована.
2. `CONTRIBUTIONS/INTAKE-CONTRACT-V1.md` — технический контракт структуры intake payload. Он прямо не является hosted intake service, identity system или правовым grant от contributor.
3. `CONTRIBUTIONS/PROFESSIONAL-CONTRIBUTION-WORKFLOW-SPEC-2026-10-11.md` имеет статус Design draft. В нём предусмотрено подтверждение ознакомления с submission terms, но это не утверждённые и не опубликованные contributor terms.
4. `IMPLEMENTATION/018-AUTHORSHIP-CONTRIBUTION.md` структурно поддерживает `rights_ref`, но различает credit, contribution, responsibility и ownership; права и ответственность не выводятся автоматически из авторства.
5. `STANDARD/017-PROVENANCE.md` различает provenance, authorship и ownership. Provenance цепочки не являются доказательством правообладания.
6. `RELEASE/EDITORIAL-CORRECTION.json` — реестр ограниченных разрешений на конкретные редакционные изменения. Он не выбирает project license и не назначает rights holder/editor/approver.
7. Contribution intake остаётся локальным/ручным. Hosted intake нельзя открывать до решений по лицензированию, privacy, retention, abuse controls и review ownership.

## 3. Десять решений владельца

### R-01 — Кто является правообладателем оригинального корпуса?

**Нужно решить:** кто владеет правами на оригинальные тексты, структуру, редакционные формулировки, графику и другие созданные проектом материалы.

Возможные модели:
- конкретное физическое лицо;
- юридическое лицо/организация;
- документированная коллективная модель с распределением прав по авторам/вкладам;
- комбинированная модель, где права на разные компоненты принадлежат разным лицам.

**Что зафиксировать:** юридически корректное имя правообладателя, объект прав, основание владения/полномочий, перечень исключений и способ обработки материалов, созданных сторонними contributors.

**Нельзя выводить:** правообладателя из имени GitHub account, автора commit, администратора репозитория, названия проекта или факта, что один человек координирует работу.

### R-02 — Какая лицензия распространяется на оригинальный текст и структурированные данные?

**Нужно выбрать точную лицензию и версию**, а не просто заявить «open source» или «свободная энциклопедия».

| Вариант | Что означает для распространения | Основное последствие |
|---|---|---|
| CC BY 4.0 | Разрешает копирование и адаптацию, включая коммерческое использование, при атрибуции и указании изменений | Наиболее широкая совместимость с открытым распространением, но attribution/third-party exclusions обязательны |
| CC BY-SA 4.0 | Разрешает копирование и адаптацию при атрибуции; производные материалы должны сохранять ShareAlike | Производные работы обязаны использовать совместимую ShareAlike-лицензию |
| CC BY-NC-SA 4.0 | Некоммерческое использование, атрибуция и ShareAlike | Коммерческое использование исключено; совместимость с коммерческими/смешанными каналами ограничена |
| All rights reserved / permission-based | Повторное использование возможно только в пределах отдельно выданных разрешений и применимых исключений | Максимальный контроль, но меньшее свободное распространение и более тяжёлая обработка permissions |

**Рабочая рекомендация для обсуждения, не решение:** если главная цель — долговременное свободное распространение оригинальных материалов Энциклопедии, CC BY 4.0 — наиболее простая и широкая модель из перечисленных. Она не должна распространяться на сторонние Source texts, images, maps, datasets, logos или contributor materials, права на которые проект не получил.

**Что зафиксировать:** точное имя/версию, canonical URI, охватываемые объекты, исключения, attribution requirements, treatment of adaptations, effective date и правообладателя, который вправе её предоставить.

### R-03 — Отдельная лицензия для программного кода

**Нужно решить:** распространяется ли software code под отдельной лицензией, независимо от content/data.

Варианты для рассмотрения:
- MIT — короткая permissive license с сохранением copyright/license notice;
- Apache-2.0 — permissive license с более подробными условиями и patent grant;
- другая совместимая open-source license;
- all rights reserved / controlled distribution.

**Рабочая рекомендация:** код и содержимое Энциклопедии лицензировать раздельно. Лицензия текстов не должна случайно распространяться на код, а лицензия кода — на Claim/Evidence/Source records.

**Что зафиксировать:** точную лицензию, версию, покрываемые каталоги/файлы, исключения, copyright holder и notice.

### R-04 — Какие условия принимают будущие contributors?

**Нужно утвердить contributor terms**, которые соответствуют выбранной R-02 license и не требуют от автора передавать права, которыми он не владеет.

Минимальные условия:
- подтверждение, что contributor имеет право отправлять материал;
- grant/permission на включение, редактирование, хранение, versioning и распространение в пределах выбранной project license;
- выбор публичной атрибуции, коллективного/псевдонимного/анонимного credit там, где допустимо;
- запрет на материалы третьих лиц без правового основания;
- обязанность сообщить о лицензии, permissions и известных ограничениях;
- порядок исправления, отзыва, спора и удаления;
- гарантии не должны превращаться в необоснованное обещание научной истинности.

**Важно:** существующий intake contract не является contributor license agreement и не даёт проекту прав на присланные материалы. Hosted intake остаётся закрытым.

### R-05 — Какова политика повторного использования внешних источников?

**Нужно выбрать правила по типам материала**, не единое «можно использовать, если указать источник».

Рекомендуемая консервативная структура:

1. **Factual paraphrase + citation + link:** базовый режим, если source terms, AI/LLM restrictions и intended distribution не запрещают соответствующее использование.
2. **Короткие цитаты:** только при проверке применимого закона, лицензии, объёма, цели и source terms; обязательны quotation marks и точная attribution.
3. **Images, maps, diagrams, figures, photographs, video:** не включать без item-level license/permission evidence.
4. **Tables and datasets:** отдельно проверять copyright, database rights, license, provenance, privacy and terms.
5. **OpenStax CC BY-NC-SA with LLM restriction:** не использовать в AI-assisted workflow без предварительного письменного разрешения или approved rights-compatible replacement.
6. **Government material:** проверять, что конкретный item действительно создан государственным органом/сотрудником и не содержит third-party material; добавлять attribution и non-endorsement.
7. **Source link:** сохранять точную страницу/издание/locator; не выдавать доступность URL за право копировать материал.

**Что зафиксировать:** правила для каждого класса материала, кто делает item-level review, когда нужно разрешение, кто принимает исключения и где хранится доказательство.

### R-06 — Кто несёт редакционную ответственность?

**Нужно назначить accountable editor или редакционную роль/орган.**

Зафиксировать:
- имя/роль/организацию;
- полномочия по содержанию, редакционным решениям и HOLD/INCLUDE/EXCLUDE;
- границы делегирования;
- порядок конфликта интересов и эскалации;
- замену/резервного ответственного на период отсутствия.

Editor не назначается автоматически по факту написания документа или выполнения CI.

### R-07 — Кто утверждает выпуск?

**Нужно отдельно назначить release approver.**

Зафиксировать:
- имя/роль/организацию;
- какие проверки и документы он должен просмотреть;
- какие решения подтверждает;
- форму и место записи approval;
- необходимость отдельного подтверждения каждого edition/release.

CI PASS — технический факт, а не editorial/rights approval. Editor и release approver могут быть одним или разными лицами, но это должно быть осознанно зафиксировано.

### R-08 — Как читатель сообщает об ошибке, споре или нарушении прав?

**Нужно определить реальный публичный канал и процесс.**

Минимум:
- monitored contact address/form или другой реально работающий канал;
- ответственный оператор и резерв;
- первичная классификация: safety-critical, factual, rights/privacy, attribution, technical;
- target response times и urgent restriction/takedown path;
- временная отметка и запись жалобы;
- расследование, решение, appeal/escalation;
- correction/version history и rollback;
- privacy/retention policy для контактов и вложений.

Нельзя публиковать выдуманный email или контакт, который никто не обслуживает.

### R-09 — Как фиксируются авторство, вклад и атрибуция?

**Нужно утвердить правила для:**
- original authors;
- subject-matter contributors;
- editors and curators;
- translators;
- reviewers and domain experts;
- data/software creators;
- collective, anonymous and pseudonymous contributions;
- AI/tool assistance and human responsibility;
- source-rights-holder credit, который отличается от авторства Энциклопедии.

**Рабочая рекомендация:** фиксировать человеческие роли и существенную AI/tool assistance прозрачно, не объявляя модель юридическим автором и не снимая ответственности с назначенного редактора/правообладателя. Не выводить ownership из credit или provenance.

**Что зафиксировать:** формат attribution в Reader, порядок перечисления contributors, способ указания изменений/перевода, policy для anonymous/pseudonymous authorship и AI-assisted work.

### R-10 — Где и как хранится rights evidence?

**Нужно утвердить версионированный rights evidence register.**

Минимальные поля для каждой единицы:
- exact Source/asset ID и version;
- title, author/organization, canonical URL/DOI и exact locator;
- rights holder/licensor;
- license name/version/URI или permission reference;
- covered material: text, code, image, map, figure, table, dataset, audio/video;
- territory, term, permitted uses and restrictions;
- commercial/non-commercial boundary;
- adaptation/translation/ShareAlike/attribution requirements;
- AI/LLM ingestion restrictions;
- third-party components and exclusions;
- permission file/email/contract reference;
- reviewer/approver and decision timestamp;
- expiry/review date and change-monitoring trigger;
- status: VERIFIED / CONDITIONAL / PERMISSION REQUIRED / EXCLUDED / UNKNOWN.

Публичный Source record с `availability=public` не заменяет rights evidence record.

## 4. Взаимозависимости решений

- **R-01 + R-02 + R-03:** устанавливают, кто может лицензировать оригинальные материалы и программный код.
- **R-02 + R-04:** определяют, какие права проект получает от будущих contributors.
- **R-05 + R-10:** превращают source-level screen из Package K в воспроизводимую процедуру для каждого exact-version item.
- **R-06 + R-07:** отделяют редакционную ответственность от утверждения выпуска и от технического CI.
- **R-08:** обеспечивает работающий канал исправлений и срочных ограничений после выпуска.
- **R-09:** обеспечивает корректное credit/authorship и не смешивает attribution, ownership, provenance и responsibility.
- **R-02/R-05 особенно важны для Red Cross, FAO, World Bank и OpenStax NC-SA/AI-restricted sources.** Их нельзя «очистить» только указанием ссылки.

## 5. Предлагаемая последовательность принятия решений

1. Определить distribution model: бесплатный non-commercial, открытый коммерчески совместимый, коммерческий/платный, смешанный или иной.
2. Назначить rights holder и определить, какие материалы он вправе лицензировать.
3. Выбрать project content/data license и отдельную code license.
4. Утвердить source reuse policy и contributor terms.
5. Назначить accountable editor и release approver.
6. Утвердить correction/dispute/withdrawal contact и процесс.
7. Утвердить attribution/authorship/AI assistance policy.
8. Утвердить rights evidence storage/validation and review cadence.
9. Применить решения к exact-version candidate set и только затем решать INCLUDE/HOLD/EXCLUDE.

Эта последовательность не требует принимать все решения одним документом или одним днём, но ни одно из них не должно быть подменено технической реализацией.

## 6. Текущие стоп-факторы для первой редакции

До решения R-01–R-10:
- нет выбранной project content/data license;
- нет зафиксированного rights holder;
- нет отдельной code license в корне репозитория;
- contributor terms остаются draft/technical contract, не legal grant;
- source reuse policy не утверждена;
- accountable editor/release approver не назначены;
- публичный correction/rights contact не определён;
- attribution/authorship policy не утверждена;
- versioned rights evidence storage policy не закрыта.

Поэтому Package K не может быть трактован как разрешение на публикацию любого из 19 кандидатов. Источники с permissive terms остаются зависимыми от project-level governance; источники с ограничительными terms требуют отдельных решений/разрешений/замены.

## 7. Что этот пакет закрывает и чего не закрывает

**Закрывает:**
- перевод R-01–R-10 в конкретные вопросы владельцу;
- список минимальных evidence для каждого решения;
- взаимозависимости решений;
- безопасную рекомендуемую последовательность.

**Не закрывает:**
- ни одного owner decision R-01–R-10;
- project license, code license или contributor grant;
- appointment editor/release approver/contact;
- rights clearance конкретного source/asset;
- INCLUDE/HOLD/EXCLUDE и production allowlist;
- публикацию, merge, deployment или public intake.

**Package L завершён как read-only owner decision packet.** Следующий этап по плану — итоговый состав и архитектура первой редакции. Он может быть подготовлен как условная exact-version composition, но окончательный INCLUDE manifest должен оставаться fail-closed до того, как владелец примет необходимые R-01–R-10 решения и закроет source-specific rights blockers.
