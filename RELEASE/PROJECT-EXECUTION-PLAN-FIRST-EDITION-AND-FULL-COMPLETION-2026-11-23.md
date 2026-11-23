# Единый план работ: первый выпуск и полное завершение Энциклопедии

Дата фиксации: 2026-11-23  
Статус: **ОСНОВНОЙ ОПЕРАЦИОННЫЙ ПЛАН ПРОЕКТА**  
Рабочая ветка документа: `mvp-public-contribution-design-2026-10-11`  
Назначение: единая точка ежедневной сверки при каждом продолжении работы над проектом.

> Главный принцип: сначала выпускаем полноценную, ограниченную по составу, работающую первую редакцию; затем последовательно доводим весь корпус и систему до полного состояния. Полный M13 не является предварительным условием первого выпуска.

---

## 0. Обязательные правила работы

1. **Не начинать стратегию заново.** Перед каждой рабочей сессией открыть этот документ и сверить актуальные HEAD, PR, CI и доску закрытия первого выпуска.
2. **Не заставлять владельца повторно выбирать уже утверждённое.** Существующие решения и границы брать из перечисленных ниже controlling documents.
3. **Не расширять первый выпуск произвольно.** Использовать уже зафиксированную карту Part I / Part II, текущие candidate registers и exact-version master register. Новые темы не добавлять без явной необходимости и решения владельца.
4. **Не перепроверять сделанное без причины.** Повторно использовать ранее выполненные аудиты, Human View, source research и rights screens в пределах их точной области и версии.
5. **Не подменять доказательства количеством.** CI PASS, наличие Source, общий отчёт или упоминание в реестре сами по себе не означают INCLUDE.
6. **Не менять canonical Claims / Evidence Use / Sources / Relations и не назначать INCLUDE, HOLD или EXCLUDE за пределами точной авторизации.** Исторические версии сохранять.
7. **Не сливать Draft PR и не менять main без отдельного решения владельца.** Не публиковать и не развёртывать ничего автоматически после CI.
8. Работать большими согласованными пакетами, но каждый пакет должен иметь точную область, воспроизводимую проверку и зафиксированный результат.

## 1. Зафиксированный замысел первой редакции

Первая редакция — это **настоящая первая книга/версия Энциклопедии цивилизации**, а не техническая демонстрация и не только справочник по выживанию.

### Part I — «Выживание и сохранение жизни»

Это самостоятельная открывающая часть Энциклопедии. Сохраняем зафиксированный порядок десяти глав:

1. Ориентация, предупреждения, чрезвычайные ситуации и координация.
2. Вода: доступ, качество, хранение, обработка и санитарные системы.
3. Пища, питание и продовольственная безопасность.
4. Укрытие, жильё и безопасные основы строительства.
5. Здоровье, гигиена, санитария и границы первой помощи.
6. Тепло, огонь, электричество, энергия и освещение.
7. Инструменты, материалы, ремонт и изготовление.
8. Сельское хозяйство, почва, семена, растения и животные.
9. Природные и экологические опасности.
10. Связь, навигация, транспорт и логистика сообщества.

Состав конкретных срезов брать из:
- `RELEASE/FIRST-EDITION-OPENING-SURVIVAL-AND-DOMAIN-MAP-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-SECTION-IMPLEMENTATION-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-FULL-SLICE-INVENTORY-2026-11-18.md`
- `RELEASE/FIRST-EDITION-SURVIVAL-CANDIDATE-MANIFEST-2026-11-18.md`

Эти документы задают архитектуру и candidate scope. Они **не означают**, что каждый перечисленный Claim автоматически допущен к публикации.

### Part II — фундаментальные и цивилизационные знания

После открывающей части первая редакция должна дать реальную широту Энциклопедии. Сохраняем существующую карту направлений:
- математика и измерения;
- физические науки;
- химические науки;
- науки о жизни;
- Земля, климат и космос;
- инженерия и вычислительные технологии;
- науки о человеке;
- общество и институты;
- история и культура.

Состав Part II определяется уже созданными exact-version candidate registers, addenda, dependency closure и зафиксированной картой первого выпуска. Не пытаться включить все 385 Part II slices и тем более весь корпус. Не выдумывать новый набор тем вместо существующего реестра.

Главная цель первой редакции: **связная, полезная, честно ограниченная и достаточно широкая Энциклопедия**, в которой открывающая часть посвящена сохранению жизни, а последующие части сохраняют фундаментальные знания и опыт цивилизации.

## 2. Текущая рабочая база на дату фиксации

Состояние сверено 2026-11-23:

- PR #22 — MVP / первая редакция, открыт, Draft, не слит; ветка `mvp-public-contribution-design-2026-10-11`; HEAD `a56bce118dc38efca497ee793c0a181c62fae940`.
- На указанном HEAD подтверждены 4/4 успешных workflow: Reference Tests, Release Conformance Gate, Offline Edition, MVP Contribution Form Browser Tests.
- PR #21 — M13, открыт, Draft, не слит; ветка `m13-system-wide-depth-audit-2026-10-09`; HEAD `b6c11385906cd73c907ddd9cf2fe7a37af76558f`.
- На указанном HEAD подтверждены 3/3 успешных основных workflow: Reference Tests, Release Conformance Gate, Offline Edition.
- `main` не менялся в рамках этих проверок. Оба PR остаются Draft.

**Ограничение текущего состояния:** зелёный CI подтверждает техническое соответствие проверенным workflow, но не является разрешением на публикацию. Reader/offline/contribution implementation и синтетические browser checks не заменяют реальный record-level allowlist, права, редакционное одобрение и проверку готового релизного артефакта.

Числа, SHA и workflow выше — контрольный снимок на дату документа. Перед каждым пакетом обновлять их по GitHub, не считать неизменными.

## 3. Приоритет №1 — срочно выпустить первую редакцию

Работать по следующим пакетам. Пакеты можно выполнять параллельно, если они не блокируют друг друга; общий приоритет всегда у release-critical задач.

### P0. Ежедневная фиксация точного состояния

- Получить текущие HEAD PR #21 и #22, проверить их base/head и Draft/open/unmerged.
- Проверить workflow именно на текущих HEAD; не переносить PASS со старого коммита.
- Проверить, не появились ли новые коммиты, документы, авторизации или решения владельца.
- Обновить этот план только при реальном изменении scope, статуса или порядка работ.

Выход: подтверждённая рабочая точка, от которой можно безопасно продолжать.

### P1. Закрыть точный состав первой редакции и release allowlist

- Использовать существующую архитектуру Part I + Part II и все уже подготовленные candidate registers.
- Свести точные ID и версии всех предполагаемых к публикации Records: Claims, Evidence Use, Sources, Context, Scope и действительно необходимые Relations.
- Для каждой записи установить одно из решений: INCLUDE / HOLD / EXCLUDE с точной причиной. До прохождения всех gate запись остаётся HOLD.
- Проверить все зависимости включаемой записи. Не включать страницу, если её существенная зависимость, источник, граница применимости или Relation создаёт неразрешённый риск.
- Повторно использовать закрытые аудиты и prior reviews; выполнять только недостающую проверку актуальной версии.
- Сформировать единый exact-version allowlist и явный список исключений/пробелов.

**Ключевое правило:** проверяется весь материал, который войдёт в первый выпуск, и его необходимые зависимости. Не требуется завершать содержательный аудит всех остальных Claims корпуса.

### P2. Закрыть доказательность и безопасность именно выбранных записей

Для каждого кандидата, претендующего на INCLUDE:
- проверить точную версию Claim и её смысл;
- проверить соответствие Evidence Use конкретному Claim;
- проверить идентичность Source и точный locator / passage;
- оценить прямоту поддержки, ограничения, независимость и актуальность доказательств;
- проверить Context / Scope и применимость;
- проверить критические противоречия, неопределённость и риск неверного применения;
- проверить точные версии всех зависимостей и Relations, отображаемых читателю;
- сохранить границы между описательным знанием и операционной инструкцией.

Усиленная проверка обязательна для медицинских, водных, пищевых, санитарных, электрических, строительных, химических, пожарных, аварийных и других high-consequence материалов. Если квалифицированного review нет, соответствующая практическая инструкция остаётся HOLD или исключается из этой редакции. Это не должно блокировать безопасные, независимо проверенные материалы других разделов.

### P3. Закрыть права, редакционную ответственность и операционные решения

В существующем регистре R-01—R-10 открыты следующие owner-level вопросы:
- установить правообладателя/основание полномочий;
- выбрать лицензию и точный охват авторского контента/данных;
- отдельно определить лицензию ПО;
- определить условия будущих вкладов;
- зафиксировать правила использования сторонних источников;
- назначить ответственного редактора;
- назначить лицо, утверждающее релиз;
- определить канал исправлений, споров и срочного снятия;
- определить атрибуцию и авторство;
- определить, где и как хранятся доказательства прав и разрешений.

Нельзя выдумывать ответы за владельца. Сначала подготовить один компактный пакет решений с вариантами и последствиями, затем запросить только те решения, которые действительно должен принять владелец.

Для первой редакции сохранять консервативную границу: собственные оригинальные формулировки и factual paraphrase при документированном основании; не копировать сторонние тексты, изображения, таблицы, карты и datasets без ясного разрешения. Публичная доступность источника не равна праву на перераспространение.

### P4. Довести рабочую программу до релизного пользовательского состояния

На основе существующего MVP и уже реализованных механизмов:
- read-only reader для exact allowlist;
- понятная структура Part I / Part II и навигация по темам;
- поиск по разрешённому выпуску;
- страницы/карточки Claim с доступными Evidence Use и Source;
- переходы по Relations только если точная Relation прошла допуск;
- ясные статусы: проверено для этой редакции / ограничено / не входит в выпуск;
- исключение HOLD, draft, private review и внутренних M13-материалов из публичной сборки;
- мобильная читаемость, клавиатурная навигация, доступность и корректное отображение русского текста;
- воспроизводимая offline edition без обязательного сетевого соединения;
- локальная форма/JSON export не должна напрямую менять canonical records или создавать ложное впечатление, что вклад принят;
- защита от XSS, утечек приватных данных, ошибочных внутренних ссылок и случайного включения неразрешённых записей.

Не строить новую платформу или backend, если текущая Reference Implementation и release/offline pipeline могут обеспечить минимально достаточный выпуск.

### P5. Финальная сборка и выпуск

На одном неизменяемом release candidate SHA:
1. собрать manifest с точными версиями, commit, builder/tool versions и hashes;
2. проверить, что сборка содержит только allowlist и необходимые разрешённые зависимости;
3. прогнать Reference Tests, Release Conformance Gate, security/browser tests и Offline Edition;
4. открыть и вручную проверить реальный артефакт на desktop и mobile;
5. проверить ссылки, навигацию, поиск, язык, предупреждения, ограничения и атрибуцию;
6. провести независимую редакционную/Human View проверку и короткий non-specialist usability test;
7. зафиксировать права, approver, ограничения, известные пробелы, канал исправлений и rollback;
8. получить явное решение владельца о публикации конкретного immutable bundle.

Публиковать только после прохождения всех обязательных пунктов. Первый выпуск может иметь пробелы; он не должен заявлять полноту всего корпуса или завершённость M13.

### Что НЕ должно задерживать первый выпуск

Если задача не затрагивает:
- точный allowlist первого выпуска;
- существенную зависимость включённой записи;
- безопасность/правдивость включённого материала;
- права, приватность или безопасность программы;
- воспроизводимость сборки и обязательные release gates,

то она остаётся в послерелизной очереди. Не запускать новые общекорпусные M13 batches только ради формального процента завершения. Не повторять уже закрытые проверки.

## 4. Приоритет №2 — после первого выпуска довести всю Энциклопедию до конца

После выпуска первая редакция становится стабильной точкой, а работа продолжается итеративно. Полный проект не считается законченным только потому, что выпущен первый том.

### F1. Завершить M13 на всём корпусе

- Полностью закрыть утверждённый denominator Claims и reconciled inventory.
- Проверить происхождение и актуальность исторических оценок; сохранять историю и не переносить старые D/E/B автоматически.
- Провести содержательное D/E/B assessment там, где оно предусмотрено методикой.
- Для каждого Claim проверить Evidence Use, Source identity, точные locators, прямоту поддержки, независимость, противоречия, currency, Context и Scope.
- Завершить high-consequence review, Human View, semantic duplicate/alias review и независимую adversarial review.
- Проверить cross-slice Relations: endpoint identity/version/type, смысловую обоснованность, контекст, доказательную основу и отсутствие искусственных связей.
- Сформировать итоговый defect register, residual risk register, independent review и exact-head CI.
- Закрыть M13 только по его полным критериям, а не по числу выполненных пакетов или зелёному CI.

### F2. Завершить полноту и глубину доменного корпуса

- Продолжать от утверждённой DOMAIN-ROADMAP и Gap Map.
- Закрывать незаполненные важные направления и углублять слабые существующие срезы.
- Для новых/переработанных срезов соблюдать полный Definition of Done: Source → Claim → Evidence Use → Context/Scope, provenance, regression, Human View, release evidence.
- Убирать дубли и исправлять семантические пробелы только через контролируемые versioned changes.
- Не вводить новые Record types без обоснования через Entity Discipline / ADR, schema, validator и tests.
- Сохранять широту Энциклопедии: естественные и физические науки, здоровье, инженерия, технологии, экономика, право, общество, история, культура и другие области.

### F3. Развить систему и пользовательские возможности

- Улучшать reader, поиск, фильтры, тематические карты и навигацию по подтверждённым связям.
- Развивать contribution intake только после privacy, access, abuse, retention, moderation и staffing controls.
- Вести прозрачную версионность выпусков, исправления, changelog, rollback и обратную совместимость.
- Развивать экспорт, офлайн-пакеты, переносимость, проверку целостности и долговременное архивирование.
- Подготовить дополнительные языки с редакционной проверкой и сохранением provenance/атрибуции.
- Проводить регулярные security, accessibility, recovery и независимые usability checks.

### F4. Критерий полного завершения проекта

Энциклопедия может считаться зрелой и завершённой только когда:
- утверждённый корпус имеет проверяемое покрытие и честный реестр пробелов;
- Claims и их доказательная основа прошли установленную содержательную оценку;
- высокорисковые материалы получили квалифицированную проверку или явно исключены;
- Relations семантически обоснованы и не вводят читателя в заблуждение;
- права, авторство, редакционная ответственность и correction operations документированы;
- reader, поиск, офлайн-режим, экспорт и восстановление стабильно работают;
- каждый выпуск воспроизводим и version-pinned;
- исправления и новые знания можно добавлять без потери истории;
- независимая проверка не выявляет критических дефектов в заявленном контуре.

## 5. Разделение потоков и правило приоритета

До первого выпуска:
- **Главный поток:** P1–P5, выпуск первой редакции.
- **Вспомогательный поток:** M13 — только release-critical пересечения и системные проверки, не блокирующие независимые release задачи.
- **Запрещённое распыление:** новые широкие аудиты, новые произвольные темы, повтор закрытых проверок, неавторизованные canonical edits и улучшения, не влияющие на выпуск.

После первого выпуска:
- M13 и полное развитие корпуса становятся основными потоками;
- исправления безопасности/целостности первой редакции имеют безусловный приоритет;
- расширение следующей редакции выполняется через controlled release batches.

Не использовать фиксированный процент времени как самоцель. Переключение на M13 определяется реальными зависимостями и рисками релиза, а не желанием равномерно распределить задачи.

## 6. Ежедневный протокол — обязательно перед началом работы

При каждом новом рабочем дне/продолжении проекта:

- [ ] Прочитать этот документ целиком или релевантные разделы перед выбором следующей задачи.
- [ ] Проверить текущие PR #21 и #22, HEAD, base, Draft/open/merged.
- [ ] Проверить CI только на текущем HEAD.
- [ ] Открыть Priority Closure Board и установить фактические незакрытые release blockers.
- [ ] Сверить Part I / Part II candidate registers, exact-version master register и owner decisions; не дублировать закрытые действия.
- [ ] Выбрать самый большой безопасный пакет, непосредственно сокращающий путь к первому выпуску.
- [ ] Выполнить работу, сохранить её в правильной ветке, проверить diff и exact-head CI.
- [ ] Обновить статус/следующее действие в этом плане или в связанном execution board, если состояние действительно изменилось.
- [ ] В итоговом сообщении назвать только выполненные изменения, проверенные результаты, оставшиеся реальные блокеры и следующий конкретный пакет.

**Не отправлять пользователю промежуточные статусы вместо работы. Не просить его повторно подтверждать уже принятые решения. Если блокирует только одно решение владельца, задать один конкретный вопрос с точным контекстом.**

## 7. Иерархия проектных документов

Этот план — главный операционный маршрут, но он не отменяет более точные технические и редакционные документы. При конфликте применять следующий порядок:

1. Явное последнее решение владельца и точная bounded authorization.
2. Текущий exact-version register / allowlist / owner decision record для конкретной записи.
3. Специальный first-edition scope и priority closure board.
4. Настоящий план — порядок и приоритет работ.
5. DOMAIN-ROADMAP и общие архитектурные документы — долгосрочная карта.

Контролирующие документы первой редакции:
- `RELEASE/FIRST-EDITION-SCOPE-AND-SURVIVAL-INTEGRATION-2026-11-18.md`
- `RELEASE/FIRST-EDITION-OPENING-SURVIVAL-AND-DOMAIN-MAP-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-SECTION-IMPLEMENTATION-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PRIORITY-CLOSURE-BOARD-2026-11-19.md`
- `RELEASE/FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PART-II-EXACT-VERSION-MASTER-REGISTER-2026-11-19.md`
- `RELEASE/FIRST-EDITION-BATCH1-16-CONSOLIDATED-IMPLEMENTATION-QUEUE-2026-11-19.md`
- `RELEASE/FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER-2026-11-19.md`
- `RELEASE/FIRST-EDITION-EDITORIAL-RIGHTS-AND-OPERATIONS-POLICY-2026-11-18.md`
- `RELEASE/MVP-EXACT-HEAD-CONTINUATION-REVIEW-2026-11-13.md`
- `RELEASE/PUBLIC-PILOT-AND-RELEASE-GATES-2026-10-11.md`
- `CONTENT/DOMAIN-ROADMAP.md`

M13 remains governed by its own protocol and bounded authorizations on PR #21. Этот план не ослабляет M13; он фиксирует, что его полный объём не должен без необходимости задерживать первую редакцию.

---

## 8. Ближайшее следующее действие

**Сначала выполнить единый release-blocker reconciliation для Part I + Part II на актуальном PR #22 HEAD:** сопоставить Priority Closure Board, точные candidate registers, права R-01–R-10, зависимости и текущий reader/offline implementation; вывести один недублирующий execution queue с конкретными закрываемыми блокерами. Затем выполнять его крупными пакетами до появления реального exact-version allowlist и релизного артефакта.

Документ пересматривается ежедневно, но его стратегические решения не меняются без фактической причины и явного решения владельца.


---

## Live execution addendum — 2026-11-23

This addendum supersedes the historical HEAD/CI snapshot in §2 where it differs.

### Verified current state at addendum preparation

- PR #22 is OPEN / DRAFT / NOT MERGED, branch `mvp-public-contribution-design-2026-10-11`, base `main`.
- The branch HEAD at the latest read-only candidate package was `a081d58390832fa46d9d753ebab042ad9b9de604`.
- PR #22 base SHA observed: `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.
- `main` observed: `d58289f319993ede5294a46f4741a506fd2fd710`.
- On the new documentation HEAD, GitHub returned one `build-and-test` check in progress. No full exact-head CI PASS is claimed for this addendum HEAD.
- PR #21 remains OPEN / DRAFT / NOT MERGED. M13 remains independent of the first-edition release gate.

### Completed bounded candidate package

See `RELEASE/FIRST-EDITION-BOUNDED-FOUNDATIONAL-CANDIDATE-CLOSURE-AND-QUEUE-2026-11-23.md`.

The exact seven-record SI private-review closure was re-fetched. The current canonical IDs, versions, record types, Claim→Evidence Use→Source edges, NIST section pinpoints, “22 special-named derived units” qualification and Claim-A-only Context/Scope targets were verified. The existing private preview implementation and browser inspection suite were re-read and reused; no replacement builder was created.

Two additional low-consequence Part II candidates were boundedly re-fetched:
- Climate basics Claim A: five-record Claim/EU/Source/Context/Scope subgraph; canonical EU is still generic despite prior NASA locator research.
- Measurement uncertainty Claim A: five-record Claim/EU/Source/Context/Scope subgraph; canonical EU is still generic and the legacy NIST TN 1297/current-guidance distinction must remain explicit. The complete slice has an additional BIPM evidence track and was not certified by this subgraph-only check.

All three remain HOLD. No canonical JSON or disposition was changed. The candidate order is SI private review, climate Claim A, measurement uncertainty Claim A, statistics, then motion/cell. High-consequence procedures remain outside the fast-track.

### Release constraints remain

- No public INCLUDE is established by this work.
- No production exact-version allowlist exists.
- R-01–R-10 remain open.
- The SI artifact is a private, non-redistributable preview only; independent three-reader review is not run.
- The first edition still requires exact selected dependency closure, rights/attribution clearance, accountable editor and release approver, correction route, production reader/offline bundle, artifact inspection and explicit owner release approval.
- No merge, deployment, public release or `main` change was performed.


---

## Live execution addendum — 2026-11-23, after 19-chapter architecture and candidate shortlist

This addendum supersedes earlier live HEAD/queue references in this document where they differ.

### Current branch and exact inventory snapshot

- PR #22 remains OPEN / DRAFT / NOT MERGED.
- Branch: `mvp-public-contribution-design-2026-10-11`.
- Current PR HEAD at this addendum: `85a5cdd4fc572d4723fb485240622025ff3b7b40`.
- PR base remains `main`, recorded base SHA `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.
- Part I controlling register: 94/94 slices structurally inventoried and 980/980 record files screened. Screening is not INCLUDE approval.
- Part II exact-version master table: 1,146 unique record/version rows across 124 thematic slices (125 slice labels including the service-only `cross-slice-linkage`); all 1,146 rows are HOLD. The table composition is 352 Claims, 408 Evidence Uses, 171 Sources, 107 Contexts and 108 Scopes.
- Relations remain separately tracked: 63/63 inventoried and semantically reviewed; semantic HOLD cases remain.
- No production INCLUDE manifest exists. R-01–R-10 remain open owner decisions.

### Completed editorial/release-preparation package

Three durable artifacts were added:

1. `RELEASE/FIRST-EDITION-19-CHAPTER-EDITORIAL-TOC-AND-READER-STRUCTURE-2026-11-23.md`
   - Defines the two-part, 19-chapter reader structure with numbered subsections, safety/editorial boundaries and cross-chapter pathways.
2. `RELEASE/FIRST-EDITION-19-CHAPTER-CANDIDATE-SLICE-MAPPING-AND-COVERAGE-2026-11-23.md`
   - Maps the ten Survival chapters to existing Part I candidate slices and assigns all 124 Part II topical slice IDs to primary reader chapters, preserving cross-part entry points and deduplication.
3. `RELEASE/FIRST-EDITION-19-CHAPTER-REPRESENTATIVE-CLAIM-CANDIDATE-SHORTLIST-2026-11-23.md`
   - Identifies one representative Claim candidate for each chapter, re-fetches exact Claim/Evidence Use/Source versions, and records specific evidence, rights, consequence and reader blockers.
   - Work priority lanes are Package A/B/C only; all candidates remain HOLD.

The priority board has been updated with the corresponding execution checkpoints. No canonical Claim/Evidence Use/Source/Context/Scope/Relation record, candidate disposition, denominator, licence, rights decision, allowlist or production state was changed by these documents.

### Technical verification boundary

- The four required PR workflows all completed successfully on exact HEAD `e656620fe7910d099fae6de9f8f933f89922b4c8`: Reference implementation tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests. The Release Conformance Gate run `45169717227` was polled to completion and succeeded.
- Subsequent commits `0c28d861...`, `986bb0a8...`, `0df29964...` and `85a5cdd4...` are documentation-only.
- GitHub returned no PR-triggered workflow runs for the mapping/shortlist documentation commits. Therefore the prior 4/4 PASS is not attributed to the current HEAD `85a5cdd4...`; exact-head revalidation is still required before any technical conformance claim about this revision.

### Next execution order — release path only

1. Execute Package A source-locator and rights checks, reusing completed substantive/Human View audits and not repeating M13 or closed P1/P2 reviews.
2. Prepare exact versioned EU/source remediation proposals where the current evidence description is generic or not reproducible.
3. Apply only those record changes that fall within an existing explicit bounded authorization; request a separate authorization where needed.
4. Keep high-consequence procedures and rights-incompatible material outside the first-edition fast track.
5. Resolve owner decisions R-01–R-10 and item-level rights evidence; no assistant or technical CI result may substitute for the owner.
6. Freeze a true exact-version INCLUDE manifest only after every selected record and dependency passes all applicable gates.
7. Complete production reader, selected offline bundle, artifact/hash inspection, independent reader/editorial review and explicit release approval.

The first edition remains the priority; full M13 and corpus completion continue independently and are not blanket prerequisites. No merge, deployment, publication or main-branch change is authorized by this addendum.


### Package A source research addendum — 2026-11-23

Added `RELEASE/FIRST-EDITION-PACKAGE-A-EXACT-SOURCE-LOCATOR-AND-RIGHTS-SCREEN-2026-11-23.md`.

The first bounded source-research package now has official locators for ten candidates: Red Cross emergency alerts; CDC hand hygiene; FAO food-security definition §1.4; NOAA weather definition; NIST materials science; USDA NRCS soil; USGS topographic maps; OpenStax Physics §2.1; NIST SI units; and PostgreSQL 18.7 §2.2.

The most actionable results:
- Databases Claim A has a direct PostgreSQL §2.2 “Concepts” page, but the claim remains version-specific to PostgreSQL 18.7; PostgreSQL 19 was released 19 November 2026.
- CDC handwashing Claim A has direct emergency-specific support in the “Wash your hands” section; the WHO corroboration track remains distinct.
- Food-security Claim A is directly supported by FAO handbook §1.4.
- Weather Claim A is directly supported by NOAA's definition of weather by time and geographic location.
- Materials and soil require Source/EU versioned corrections and explicit third-party attribution/rights review; USGS navigation should prefer current educational pages over archived map PDFs.
- SI content work is already bounded and must not be repeated; only the authorized private preview and review steps remain.

No canonical record was changed and no rights clearance was inferred. Current branch HEAD after the research and board update is `820af53dcc1ea905197189d214b0dada38817ab2`. The latest changes are documentation-only; no PR-triggered workflow run was returned for the research commit, so no exact-head CI PASS is claimed. Prior four-workflow PASS remains tied only to `e656620...`.

Next: reconcile each proposed EU/Source correction against its exact bounded authorization; implement only authorized locator-only changes, and request separate approval for any Source identity/URI, Claim wording or dependency-graph change.


## Addendum — five first-edition execution packages completed — 2026-11-23

Five coordinated packages have been completed on this PR branch:

1. **Package A — six Claim evidence and rights remediation.** Verified exact source passages and rights conditions for SI, PostgreSQL, CDC emergency handwashing, Red Cross alerts, FAO food security and NOAA weather.
2. **Package B — scientific Claim repair.** Recorded motion terminology defects, direct locators for chemistry/cell/history candidates, title-specific OpenStax NC-SA and LLM-ingestion restrictions, and remaining NIST locator work.
3. **Package C — internal offline reader shell.** Added 19-chapter navigation, search, responsive design, local-only assets, CSP and explicit empty states. No corpus records are loaded and no content is represented as approved.
4. **Package D — bounded v0.1 seed-set blueprint.** Prioritized five representative Claim entry points across both parts and defined exact selection, rights, review, artifact and approval gates.
5. **Package E — exact chapter-map validator.** Added a fail-closed 19-chapter assignment validator and empty unapproved chapter-map template. Every selected Claim must be assigned exactly once; non-Claim dependencies cannot become chapter articles.

Supporting artifacts and implementation files are indexed in the updated priority closure board and the individual Package A–E reports.

### Exact current status

- PR #22 latest HEAD: `bc34065818ed174e9cd56e2f5ff71235d59ea888`.
- PR #22 remains OPEN / DRAFT / NOT MERGED.
- GitHub returned no PR workflow runs for this exact HEAD. The newly added reader-shell and chapter-map tests are committed but not yet verified by CI on this revision.
- There is still no production INCLUDE manifest. All shortlisted records remain HOLD.
- The internal shell is a functional navigation prototype, not a content-complete first edition.
- R-01–R-10 remain OPEN. No project licence, rights holder, editor, release approver or public correction channel has been assumed.

### Updated next sequence

1. Obtain exact-head CI results for Reference Tests, Release Conformance Gate and Offline Edition; reconcile failures rather than treating absent runs as success.
2. Integrate the chapter map into a production reader that accepts only the schema-1.1 approved selection output.
3. Finish the highest-value exact-version source remediation for PostgreSQL, NOAA and CDC; keep Red Cross and FAO conditional on rights decisions; keep SI private preview within its existing authorization.
4. Close project-level owner decisions and item-level source rights for the selected seed set.
5. Freeze a minimal cross-part INCLUDE manifest, build the offline artifact, perform independent inspection and obtain approval tied to the artifact hash.

The parallel M13 audit remains on its own Draft branch and is not a prerequisite to the bounded first edition. No merge, deployment, main-branch content change or public release was performed.


### Exact-field locator reinspection and owner decision packet — 2026-11-23

A full-field re-fetch corrected the initial interpretation of two Evidence Use records:
- Databases Claim A/B/C @3 already contain exact PostgreSQL 18.7 section locators in their structured `material.locator` fields; Source @3 pins §§2.2–2.6, and Context/Scope @3 are correctly target-aligned.
- Mixtures and Solutions Claim A EU @2 already contains the exact OpenStax Chemistry 2e §11.1 locator. The generic prose description is not evidence that the structured locator is missing.
- Chemical Reactions Claim A EU @4 and Source @2 already carry the authorized OpenStax Chemistry 2e §4.3 locator.
- Red Cross emergency-alert Claim/EU/Source @2 and their separately authorized cross-slice dependency alignments are already implemented.

No additional canonical changes are indicated for these locator paths. The representative shortlist and priority board record the correction.

A separate blocker was found in Ancient Civilizations:
- The owner-approved Package A has six new CC BY 4.0 Source/Evidence Use tracks with exact locators, all present in the 23-record slice and Part II master.
- Claim B@1 still references the original OpenStax World History Volume 1 Source@1 in provenance. OpenStax identifies that title as CC BY-NC-SA 4.0 and prohibits LLM/generative-AI ingestion without prior written permission.
- The selection builder validates provenance references as exact dependencies, so the original Source remains required if Claim B@1 is selected.
- A narrow owner authorization request was prepared: `RELEASE/OWNER-AUTHORIZATION-REQUEST-ANCIENT-CIVILIZATIONS-CLAIM-B-CC-BY-PROVENANCE-MIGRATION-2026-11-23.md`. It proposes Claim B@1→@2 with unchanged wording and three approved CC BY 4.0 source origins, plus three corresponding EU@1→@2 claim_ref updates. All old versions remain historical; no changes are authorized yet.

This request is separate from the still-open project-level R-01–R-10 decisions and does not imply INCLUDE. If approved, it will make only Claim B's new version and three new Evidence Use versions eligible for a subsequent independent review; it will not clear Claims A/C or the whole slice.

### Latest exact-head CI poll

- PR #22 HEAD at the latest observation: `fba2a8b9f4d47a89c552fced7812f18f712427f7`.
- Reference implementation tests run `45173229571`: queued/pending.
- Offline Edition run `45173229859`: in progress at content preflight.
- No current-head Release Gate or Browser Tests PASS is claimed. Prior 4/4 success applies only to `e656620...`.


### Source-rights compatibility screen — 2026-11-23

Added `RELEASE/FIRST-EDITION-SOURCE-RIGHTS-COMPATIBILITY-SCREEN-2026-11-23.md`.

The screen verifies source-specific terms rather than inferring reuse rights from public availability:
- OpenStax Chemistry 2e, Biology 2e and World History Volume 1: CC BY-NC-SA 4.0 and explicit LLM/generative-AI ingestion restrictions without prior written permission.
- OpenStax Physics: its title-specific page has conflicting/complex reuse language (CC BY 4.0 in Customization, plus LLM ingestion restriction and TEA/non-commercial language in the reuse notice); treat as unresolved pending written clarification.
- PostgreSQL documentation: PostgreSQL License permits copying/modifying/distribution of documentation for any purpose subject to notice retention; strongest current compatibility path.
- Red Cross: Terms of Use limit access/copying to personal non-commercial use and restrict reproduction/distribution.
- FAO: publications remain copyrighted; specified non-commercial use with attribution is allowed under its general policy, while reuse/adaptation requires permission.
- World Bank: general terms limit use to personal/educational/non-commercial purposes; commercial redistribution generally requires written permission.
- CDC/NOAA/NIST/USGS/USDA federal sources are promising for factual paraphrase but exact pages may include third-party material; exclude third-party assets and verify page-level rights.
- USDA soil definition includes SSSA/Soil Taxonomy attribution and requires careful source attribution.

The screen is not legal clearance and does not choose the project's license. R-01–R-10 remain open. The current practical candidate order now prioritizes PostgreSQL and carefully screened federal factual sources; OpenStax NC-SA titles and restrictive Red Cross/FAO/World Bank sources require permission, alternative sources or a separately approved distribution model.

No canonical records, record versions, rights decisions, candidate dispositions, allowlists or publication states changed.

At the rights-screen HEAD `43094b0b5283b6785551b44eb85c4ae8dc6f5f90`, all four required PR workflows were triggered (Reference Tests, Release Conformance Gate, Offline Edition, Browser Tests). Their current statuses at last poll were pending/in progress; no PASS was yet claimed. The priority-board update advances the branch beyond that tested HEAD, so the next exact-head run status must be reconciled before technical conformance is claimed.
