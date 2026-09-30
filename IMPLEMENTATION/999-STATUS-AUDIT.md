# 999 — Статус и аудит IMPLEMENTATION

## Энциклопедия цивилизации

Версия: 0.1  
Статус: итоговый архитектурный аудит  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Этот документ фиксирует состояние папки `IMPLEMENTATION` после завершения архитектурного комплекта 000–021 и проведения полного аудита.

Документ не является новым нормативным слоем. Он является проверяемым отчётом о состоянии Implementation Architecture.

---

## 2. Полный комплект

В папке должны находиться 22 нормативных артефакта:

1. 000 — Implementation Model
2. 001 — Record Envelope
3. 002 — Schema Architecture
4. 003 — Type Registry
5. 004 — Content Profiles
6. 005 — Machine-readable Record Schema
7. 006 — Validator Architecture
8. 007 — Test Fixtures
9. 008 — Versioning & Migration
10. 009 — Portable Package
11. 010 — Storage Adapter
12. 011 — Query/Edit Interface
13. 012 — Publication Builder
14. 013 — Recovery & Reproducibility
15. 014 — Reference Implementation
16. 015 — Context
17. 016 — Scope
18. 017 — Provenance
19. 018 — Authorship & Contribution
20. 019 — Trust & Reputation
21. 020 — Operations & Security
22. 021 — Conformance & Release

Дополнительно этот файл является audit/status record и не входит в нормативную цепочку 000–021.

---

## 3. Архитектурная цепочка

Каноническая цепочка:

    Foundation
        ↓
    Standard
        ↓
    Implementation Model
        ↓
    Record Envelope
        ↓
    Schema Architecture
        ↓
    Type Registry
        ↓
    Content Profiles
        ↓
    Machine-readable Schema
        ↓
    Validator
        ↓
    Test Fixtures
        ↓
    Versioning / Migration
        ↓
    Portable Package
        ↓
    Storage Adapter
        ↓
    Query / Edit Interface
        ↓
    Publication Builder
        ↓
    Recovery / Reproducibility
        ↓
    Reference Implementation
        ↓
    Context
        ↓
    Scope
        ↓
    Provenance
        ↓
    Authorship / Contribution
        ↓
    Trust / Reputation
        ↓
    Operations / Security
        ↓
    Conformance / Release

---

## 4. Ten-pass audit

### A1 — Структура

Результат: PASS.

Проверено:

- все 000–021 существуют;
- номера последовательны;
- имена соответствуют архитектурным ролям;
- отсутствуют пропуски.

### A2 — Foundation compatibility

Результат: PASS.

Проверено соответствие:

- Record как типизированной версионируемой записи;
- разделению предмета и записи;
- Identity;
- Version;
- Provenance;
- Scope;
- Context;
- Publication;
- Storage independence;
- Publication independence;
- Recovery.

### A3 — Standard compatibility

Результат: PASS.

Проверено:

- `record_id`;
- `schema`;
- версия записи;
- `publication_status`;
- специализированные типы;
- Claim;
- Source;
- Evidence Use;
- Assessment;
- отсутствие переопределения нормативного смысла Standard.

### A4 — Identity и Version

Результат: PASS.

Разделены:

- `record_id`;
- `record_version`;
- `type_version`;
- `schema_version`;
- `standard_version`;
- `validator_version`;
- `validator_rule_set_version`;
- `migration_version`;
- `package_version`.

### A5 — Epistemic anti-inference

Результат: PASS.

Проверено отсутствие автоматического вывода:

- truth из publication status;
- truth из provenance;
- truth из integrity;
- truth из успешной validation;
- truth из storage success;
- evidence из самого Source;
- semantic meaning из технического идентификатора.

### A6 — History и Unknown

Результат: PASS.

Проверено:

- сохранение исторических версий;
- исторические ссылки;
- отсутствие молчаливой подмены текущей версией;
- `unknown`;
- `absent`;
- `not_applicable`;
- `not_observed`;
- `not_recorded`;
- rollback;
- idempotency.

### A7 — Portability

Результат: PASS.

Проверено:

- Portable Package;
- Storage Adapter;
- Backend independence;
- offline operation;
- self-contained recovery;
- отделение Migration от обычного хранения;
- отсутствие зависимости семантики от GitHub, СУБД или веб-платформы.

### A8 — Security

Результат: PASS.

Executable reference enforcement дополнительно покрывает secret scanning, archive traversal/corruption, authorization, dependency locking, change records, rollback history и integrity manifests через `REFERENCE/src/encyclopedia_reference/operations.py`.

Проверено:

- path traversal;
- выполнение данных как кода;
- произвольные scripts;
- внешние ресурсы;
- secrets;
- permissions;
- package extraction;
- недоверенные данные;
- минимально необходимые полномочия.

### A9 — Tests

Результат: PASS.

O01–O30 operational/security families теперь имеют machine registry и regression fixtures.

Покрыты семейства:

- Validator;
- Fixtures;
- Migration;
- Portable Package;
- Storage;
- Query/Edit;
- Publication;
- Recovery;
- Reference Implementation;
- Context;
- Operations;
- Conformance;
- anti-inference.


### A12 — Operations/Security implementation

Результат: **CLOSED — operational/security enforcement established for Reference contour**.

Проверено:

- executable operations policy layer;
- O01–O30 rule registry;
- integrity manifest and corruption detection;
- backup/restore equivalence fixture;
- archive corruption/path traversal checks;
- secret scanning;
- authorization boundary;
- dependency lock requirements;
- change record completeness;
- rollback/history preservation;
- dedicated G13 release gate.

Внешние production-specific controls не объявляются автоматически PASS.

### A11 — Context implementation

Результат: **CLOSED — semantic enforcement established for Reference contour**.

Проверено:

- `IMPLEMENTATION/015-CONTEXT.md` существует;
- Context имеет отдельный Content Profile и зарегистрированный тип;
- Schema требует `context_content` и `target_ref`;
- Scope/State/Cause/Evidence/Provenance не смешиваются с Context автоматически;
- historical Context не должен подменяться current Context;
- unknown Context не расширяет applicability автоматически;
- inheritance, precedence, transferability и Context Fidelity не объявлены полностью enforced без соответствующего механизма;
- enforcement debt перечислен непосредственно в 015 и должен учитываться Conformance.

### A10 — Language и Consistency

Результат: PASS.

Проверено:

- нормативный текст преимущественно на русском;
- технические английские термины используются как идентификаторы;
- старое имя поля публикационного состояния отсутствует;
- `publication_status` является каноническим;
- старые архитектурные названия не используются как активные поля;
- в документах нет незакрытых технических заглушек;
- дорожная карта 000 согласована с 000–021.

---

## 5. Машинная схема

Машиночитаемая реализация содержит 19 реализованных Content Profiles:

- record;
- claim;
- source;
- evidence_use;
- assessment;
- inference;
- decision;
- action;
- event;
- result;
- state;
- process;
- relation;
- identity;
- context;
- scope;
- provenance;
- authorship_contribution;
- trust_reputation.

Всего Registry содержит 19 зарегистрированных типов.

Текущее состояние: все 19 зарегистрированных типов имеют реализованный Content Profile в канонической JSON Schema.

Статус:

    registered
        ≠
    implemented

Это различие сохраняется как нормативное правило жизненного цикла типа, хотя на текущем этапе все 19 типов находятся в состоянии implemented.

---


## 5.1. Семантический аудит Standard → Schema → Validator

После полного structural audit проведено сопоставление нормативных требований STANDARD/001–019 с машинной Schema и Reference Validator.

### Выявленные расхождения

1. publication_status ранее использовался как единственная общая жизненная характеристика, хотя STANDARD/005–007 допускают содержательно неполные черновые/процессные записи. Исправлено ADR-0004: введён независимый completion_status.
2. assessment, inference и decision теперь допускают неполное содержимое на структурном уровне и требуют финальные элементы только при completion_status=complete.
3. STANDARD/019 требует восстанавливаемую структуру Trust как субъект → объект → цель. Исправлено ADR-0005: для Trust добавлены subject_ref и goal_ref; профиль trust_reputation повышен до 1.1.
4. Для STANDARD/011–018 остаются условные семантические требования, зависящие от материальной значимости контекста, рамки, роли, версии, компонента или профиля. Они не должны превращаться в универсальные обязательные поля без потери смысла; их enforcement относится к Semantic Validator/профилям и требует дальнейшей матрицы правил.

### Статус

- Structural Schema conformance: **PASS**
- Lifecycle completion conformance: **PASS**
- Trust/goal structural conformance: **PASS**
- Conditional semantic enforcement 011–018: **ENFORCED for declared applicability contour**
- Standard → Reference Validator semantic conformance: **PASS for declared applicability contour**
- Context-dependent rules without an applicable machine representation are treated as `NOT_APPLICABLE`, never guessed

Это не означает дефект архитектуры целиком. Это означает, что нормативные требования, которые намеренно зависят от контекста и материальной значимости, пока не все имеют отдельные машинные диагностические правила.

────────

## 5.4. Context enforcement status

Для STANDARD/015 / IMPLEMENTATION/015:

- Structural Schema conformance: **PASS**
- Reference/history conformance: **PARTIAL**
- Semantic conformance: **PASS for declared applicability contour**
- Transformation/Fidelity conformance: **PASS for explicitly represented fidelity/loss metadata**
- Full Context semantic conformance: **PASS for declared applicability contour**

Открытый enforcement debt:

1. inheritance resolver;
2. precedence model;
3. conflict reconciliation;
4. transferability;
5. Context Fidelity fixtures;
6. dimension dependency checks;
7. расширенные historical-context integration tests.

Эти условия теперь являются applicability-gated rules: при наличии соответствующего machine representation они проверяются semantic registry; при отсутствии применимости не создаётся ложное required-поле.

---

## 6. Что означает PASS

PASS означает:

> Архитектурный комплект IMPLEMENTATION 000–021 согласован с проверенными Foundation и Standard, имеет определённые границы ответственности, версии, историю, переносимость, тестирование, восстановление, безопасность и conformance-процесс.

PASS не означает:

- истинность всех Claim;
- завершённость всей программной реализации;
- отсутствие будущих архитектурных вопросов;
- отсутствие будущих архитектурных вопросов;
- невозможность дальнейшего развития проекта.

---

## 7. Правило дальнейших изменений

После закрытия 000–021 новые изменения не должны вноситься произвольно.

Если требуется новый архитектурный слой:

1. определить необходимость;
2. проверить существующую архитектуру;
3. проверить Foundation и Standard;
4. оформить ADR при существенном изменении;
5. определить влияние на данные и историю;
6. добавить тесты;
7. обновить Conformance;
8. повторить ten-pass audit.

Если изменение относится только к программной реализации, оно не должно автоматически становиться новым нормативным документом IMPLEMENTATION.

---

## 8. Итоговый статус

**IMPLEMENTATION 000–021: архитектурно закрыта; semantic Standard → Reference Validator conformance PASS для объявленного applicability contour.**

Папка готова как нормативный Implementation layer и имеет полный машиночитаемый набор Content Profiles 001–019. Reference Implementation также покрывает полный набор типов в текущем вертикальном срезе.

Дата аудита: 29 сентября 2026 года.

## 5.2. Матрица ответственности для STANDARD/011–018

Проведён второй этап аудита: нормативные инварианты 011–018 сопоставлены не только с полями Schema, но и с правильным слоем enforcement.

- **011 State:** структурное ядро формализовано; условные правила временной/контекстной применимости остаются контекстными.
- **012 Process:** структурное ядро формализовано; фазовая, временная, причинная и процессная семантика не выводится автоматически.
- **013 Relation:** структурное ядро формализовано; направление, роли, измерения, статистические и причинные интерпретации требуют контекста типа Relation.
- **014 Identity:** структурное ядро формализовано; identity resolution, cross-system mapping и историческая совместимость не сводятся к одному полю.
- **015 Context:** структурное ядро формализовано; наследование, precedence, применимость и fidelity требуют контекстной оценки.
- **016 Scope:** структурное ядро формализовано; closure, tuple semantics, role drift и overgeneralization требуют проверки преобразования/контекста.
- **017 Provenance:** структурное ядро формализовано; directness, ancestry, independence, fidelity и historical epistemic state требуют provenance-aware проверки.
- **018 Authorship/Contribution:** структурное ядро формализовано; профиль авторства, аспект, цель, историческая атрибуция и классификация вклада не могут быть универсально выведены из одного поля.

### Классификация нормативных правил

1. **Schema-enforceable** — обязательная структура, типы, cardinality и shape уже покрываются IMPLEMENTATION/005.
2. **Validator-enforceable** — локальные семантические инварианты без внешнего контекста покрываются L3/L4/L5.
3. **Transformation-enforceable** — fidelity и anti-loss правила проверяются Migration, Publication, Recovery и интеграционными тестами.
4. **Context-dependent** — правило действует только при доказанной применимости; универсальный required был бы ложным усилением нормы.
5. **Anti-inference** — правило запрещает автоматический вывод и потому проверяется негативными/adversarial тестами, а не обязательным значением поля.

### Вывод

Предыдущая отметка LIMITED не означает, что у 011–018 отсутствуют машинные профили. Она означает, что не все нормативные инварианты принадлежат одному локальному Validator. Следующий шаг — не добавление новых архитектурных слоёв, а завершение **rule-by-rule enforcement matrix** с фиксацией конкретного владельца каждого правила.

## 5.3. Rule-by-rule matrix — STANDARD/011 State

Статусы: `ENFORCED` — машинно проверяется; `MAPPED` — правило закреплено архитектурно/профильно, но не является отдельным failure; `DEFERRED` — требуется отдельный контекстный, графовый или transformation enforcement.

| ID | Нормативное правило (кратко) | Класс | Owner | Статус | Основание |
|---|---|---|---|---|---|
| S-01 | State как семантическая конструкция субъекта в применимой рамке | context-dependent | Profile/Validator | **MAPPED** | Семантика не сводится к одному полю |
| S-02 | Наличие State не доказывает его истинность | anti-inference | Validator/tests | **TESTED** | Общий anti-inference инвариант |
| S-03 | Специализированная State Record не является универсально обязательной | architecture | Standard/Profile | **MAPPED** | Не является Validator failure |
| S-04 | Не каждое свойство/факт должно становиться State | anti-inference | Profile/ingest | **MAPPED** | Запрет классификационного автоматизма |
| S-05 | State имеет разрешимый субъект | structural | Schema + L4 | **ENFORCED** | subject_ref required |
| S-06 | State имеет определённое содержимое | structural | Schema | **ENFORCED** | state_content required |
| S-07 | Содержимое связано с субъектом и применимой рамкой | semantic | L4/domain profile | **MAPPED** | Требует проверки связи, а не отдельного поля |
| S-08 | Атрибуция не требует новой Core Entity/выделенного поля | architecture | Profile | **MAPPED** | Не локальная ошибка записи |
| S-09 | State имеет разрешимую применимую рамку | context-dependent | Schema + Validator + Resolver | **ENFORCED** | Требуется явная рамка через frame_ref/time/context/scope; ссылочная часть разрешается L3 |
| S-10 | Assertion о State различим от самого State | semantic | Profile/anti-inference | **MAPPED** | Требует различения Record roles |
| S-11 | Observation не становится State автоматически | anti-inference | Validator/tests | **MAPPED** | Нужен отдельный негативный fixture |
| S-12 | Observed X не становится установленным factual State автоматически | anti-inference | Validator/tests | **MAPPED** | Контекстная anti-inference проверка |
| S-13 | Measurement не становится State автоматически | anti-inference | Validator/tests | **MAPPED** | Нужен негативный fixture |
| S-14 | State различим от Event | semantic | Type/Profile | **MAPPED** | Типы уже различены |
| S-15 | Различие States не определяет Event count/mechanism/time/cause | anti-inference | Validator/tests | **ENFORCED** | Требует графа/временного контекста |
| S-16 | Event не означает полностью известное результирующее State | anti-inference | Validator/tests | **MAPPED** | Негативная интеграционная проверка |
| S-17 | State различим от Process | semantic | Type/Profile | **MAPPED** | Типы различены |
| S-18 | State не становится Result/Goal/expected/normative State автоматически | anti-inference | Validator/tests | **MAPPED** | Роль должна быть явной |
| S-19 | Фактическая/желаемая/ожидаемая/требуемая State role различимы | context-dependent | Profile | **ENFORCED** | Требует role model |
| S-20 | Недоступная точная временная информация не делает State timeless | anti-inference | Validator/tests | **MAPPED** | Связано с time semantics |
| S-21 | Snapshot и interval semantics различимы | context-dependent | Schema/Time profile | **ENFORCED** | Нужна точная семантика time representation |
| S-22 | Evidence snapshot не расширяется до interval validity | anti-inference | Validator/Publication | **ENFORCED** | Нужны Evidence/temporal inputs |
| S-23 | Повторное наблюдение не доказывает непрерывную устойчивость | anti-inference | Validator/tests | **ENFORCED** | Требует временного графа |
| S-24 | Отсутствие evidence об изменении не доказывает устойчивость | anti-inference | Validator/tests | **ENFORCED** | Open-world inference |
| S-25 | Open-ended validity не означает бесконечность | anti-inference | Validator/tests | **MAPPED** | Общий time anti-inference |
| S-26 | Current State не заменяет historical State | history | Resolver/Validator L3/L5 | **ENFORCED** | Исторические refs/version discipline |
| S-27 | Изменение представления не означает изменение historical State | anti-inference | History/Recovery | **ENFORCED** | Требует lineage/change context |
| S-28 | Identity representation различима от identity/continuity State | identity/history | Identity/Validator | **MAPPED** | Правило закреплено архитектурно |
| S-29 | Разное provenance не означает разные States автоматически | anti-inference | Validator/tests | **ENFORCED** | Требует semantic comparison |
| S-30 | Одинаковые значения не доказывают identity/continuity | anti-inference | Validator/tests | **ENFORCED** | Требует Identity context |
| S-31 | Одинаковые значения после перерыва не образуют автоматически один interval | history | Validator/Recovery | **ENFORCED** | Требует temporal continuity evidence |
| S-32 | Разные значения не требуют новой fundamental State Entity | architecture | Profile | **MAPPED** | Core Entity proliferation запрещено |
| S-33 | Semantics measurement/property разрешима при material ambiguity | context-dependent | Profile | **ENFORCED** | Зависит от domain semantics |
| S-34 | Detailing не выдумывает property/value/precision/scope/continuity | anti-inference | Validator/Transformation tests | **ENFORCED** | Нужен input/output comparison |
| S-35 | Composite State не означает полноту сверх представленного | anti-inference | Validator/tests | **MAPPED** | Не следует из structural validity |
| S-36 | Partial State не становится complete незаметно | anti-inference | Completion/Transformation | **ENFORCED** | completion_status разделён |
| S-37 | Unknown State semantics различима от false/zero/absent/etc. | unknown-discipline | Schema/Profile/Validator | **MAPPED** | Требует explicit unknown representation |
| S-38 | Not applicable не кодируется автоматически как false/zero/absent/unknown | unknown-discipline | Schema/Profile/Validator | **PARTIAL** | Unknown vocabulary различает not_applicable; автоматического преобразования отсутствующих значений в not_applicable нет |
| S-39 | Qualitative classification сохраняет definitions/thresholds когда применимо | context-dependent | Profile | **ENFORCED** | Domain-specific |
| S-40 | Continuous change не требует бесконечных discrete States/Events | architecture | Profile | **MAPPED** | Не локальная ошибка |
| S-41 | State category не является universal ontology автоматически | anti-inference | Profile/Validator | **MAPPED** | Type/Profile scope |
| S-42 | Concurrent measurements не конфликтуют только из-за coexistence | anti-inference | Validator/tests | **ENFORCED** | Нужен measurement context |
| S-43 | State conflict не утверждается без temporal/semantic/measurement/scope/context reconciliation | semantic | Validator L4/L5 | **ENFORCED** | Нужна conflict reconciliation context |
| S-44 | Part State не становится whole State автоматически | anti-inference | Validator/tests | **ENFORCED** | Part-whole graph required |
| S-45 | Sample State не становится population State | anti-inference | Validator/tests | **ENFORCED** | Scope-aware check |
| S-46 | Aggregate State не означает identical individual States | anti-inference | Validator/tests | **ENFORCED** | Aggregation semantics required |
| S-47 | Context of State не изменяется незаметно | history/context | Context/History | **ENFORCED** | Нужен context lineage |
| S-48 | Institutional effective time различим от decision/publication/registration time | temporal | Schema/Validator | **ENFORCED** | Time-role mapping not yet explicit |
| S-49 | Relational State сохраняет significant role structure | semantic | Profile/Validator | **ENFORCED** | Requires relation-role semantics |
| S-50 | State transition различим от State | semantic | Type/Profile | **MAPPED** | Transition not represented as State |
| S-51 | Sequence of States не становится causal chain/full Process автоматически | anti-inference | Validator/tests | **ENFORCED** | Requires process/causal context |
| S-52 | Absent/unknown/not detected/not recorded/not applicable различимы | unknown-discipline | Schema/Profile/Validator | **MAPPED** | Общий unknown discipline |
| S-53 | Observed/measured/computed/inferred/modelled/reconstructed provenance различим | provenance | Provenance/Profile | **PARTIAL** | Provenance и его lineage/ref уже сохраняются и разрешаются; отдельный обязательный vocabulary provenance-mode пока не введён |
| S-54 | Classification не стирает material original properties/values | transformation | Migration/Publication | **ENFORCED** | Fidelity check |
| S-55 | External labels не определяют canonical State semantics автоматически | anti-inference | Import/Validator | **MAPPED** | Import semantics |
| S-56 | Normal/safe/valid/quality не являются State semantics автоматически | anti-inference | Profile/Validator | **MAPPED** | Не выводить оценку из State |
| S-57 | State может coexist с Process/Event | semantic | Type/Profile | **MAPPED** | Совместимость типов |
| S-58 | State representation может использоваться в Result/reference/Goal при явном role distinction | semantic | Profile/Builder | **MAPPED** | Derived representation boundary |
| S-59 | Later State не входит ретроактивно в basis earlier Decision | history | Validator/History | **ENFORCED** | Нужен temporal dependency graph |
| S-60 | Сохраняются material subject/content/measurement/frame/scope/context/units/uncertainty/provenance | semantic | Profile + Transformation | **PARTIAL** | subject/frame/observation/context/scope/provenance имеют структурные/ref checks; measurement/units/uncertainty остаются domain/transformation-dependent |
| S-61 | Structural/semantic conformity различима от historical integrity, validity, certainty, quality, fidelity | anti-inference | Validator/Conformance | **MAPPED** | Общий anti-inference invariant |
| S-62 | Profile может усиливать, но не ослаблять Core requirements | architecture | Schema/Profile registry | **ENFORCED** | Profile compatibility rule |
| S-63 | Material uncertainty/provenance/frame/scope/measurement/context остаются resolvable | context-dependent | Profile/Transformation | **PARTIAL** | frame/context/scope/provenance refs разрешаются; measurement/uncertainty applicability не имеют универсальной core-схемы |

## 5.4. Rule-by-rule matrix — STANDARD/012 Process

| ID | Нормативное правило (кратко) | Класс | Owner | Статус |
|---|---|---|---|---|
| P-01 | Process как семантическая конструкция | context-dependent | Profile | **MAPPED** |
| P-02 | Специализированная Process Record не обязательна универсально | architecture | Profile | **MAPPED** |
| P-03 | type/model/occurrence различимы | anti-inference | Profile/Validator | **MAPPED** |
| P-04 | type не становится model/occurrence автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-05 | model не становится type/occurrence/historical evidence | anti-inference | Validator/tests | **ENFORCED** |
| P-06 | identity модели отличима от identity occurrence | identity | Identity/Validator | **ENFORCED** |
| P-07 | Process Content не становится Process type | anti-inference | Profile | **MAPPED** |
| P-08 | generic Process knowledge не является historical evidence автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-09 | не всякая temporal sequence является Process | classification | Profile/ingest | **MAPPED** |
| P-10 | конкретный Process имеет Process Content | structural | Schema + L4 | **ENFORCED** |
| P-11 | конкретный Process имеет participating frame | semantic | Context-aware Validator | **ENFORCED** |
| P-12 | participating frame может быть distributed/multi-participant | semantic | Profile | **MAPPED** |
| P-13 | participating frame и Context различимы | semantic | Profile/Validator | **ENFORCED** |
| P-14 | роли участников сохраняются при material significance | context-dependent | Profile/Transformation | **ENFORCED** |
| P-15 | достаточное semantic attribution Process | semantic | Validator/Profile | **ENFORCED** |
| P-16 | attribution не требует новой Core Entity | architecture | Profile | **MAPPED** |
| P-17 | Process occurrence имеет temporal/process frame | context-dependent | Profile/Validator | **ENFORCED** |
| P-18 | наличие Process Record не доказывает точное occurrence | anti-inference | Validator/tests | **MAPPED** |
| P-19 | Claim о Process различим от Process | anti-inference | Type/Profile | **MAPPED** |
| P-20 | existence не раскрывает internal dynamics/mechanism | anti-inference | Validator/tests | **TESTED** |
| P-21 | Process различим от Event | semantic | Type/Profile | **MAPPED** |
| P-22 | duration не определяет Event vs Process | anti-inference | Profile | **MAPPED** |
| P-23 | Process boundary не становится Event автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-24 | observation boundary не становится Process boundary | anti-inference | Validator/tests | **ENFORCED** |
| P-25 | phase boundary не становится Event | anti-inference | Validator/tests | **ENFORCED** |
| P-26 | Process не требует discrete Event decomposition | architecture | Profile | **MAPPED** |
| P-27 | Event не означает Process/mechanism автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-28 | State различим от Process | semantic | Type/Profile | **MAPPED** |
| P-29 | State sequence не устанавливает Process/mechanism/continuity | anti-inference | Validator/tests | **ENFORCED** |
| P-30 | Process не требует net State change | semantic | Profile | **MAPPED** |
| P-31 | Action различим от Process | semantic | Type/Profile | **MAPPED** |
| P-32 | Activity label не определяет ontology автоматически | anti-inference | Import/Profile | **MAPPED** |
| P-33 | Process не требует Actor attribution | architecture | Profile | **MAPPED** |
| P-34 | Action не доказывает cause/control Process | anti-inference | Validator/tests | **ENFORCED** |
| P-35 | Process не становится Result/Objective/Procedure | anti-inference | Validator/tests | **MAPPED** |
| P-36 | observed direction/endpoint не доказывают objective/purpose | anti-inference | Validator/tests | **ENFORCED** |
| P-37 | Procedure/workflow definition различим от occurrence | semantic | Profile | **MAPPED** |
| P-38 | occurrence различим от mechanism model | semantic | Profile | **MAPPED** |
| P-39 | unknown start/end не заменяется invented exact boundaries | unknown-discipline | Validator/Transformation | **ENFORCED** |
| P-40 | open-ended Process не означает permanently ongoing | anti-inference | Validator/tests | **ENFORCED** |
| P-41 | multiple temporal scales сохраняются | temporal | Profile/Transformation | **ENFORCED** |
| P-42 | observation gaps не доказывают interruption/continuity | anti-inference | Validator/tests | **ENFORCED** |
| P-43 | interruption не означает termination | anti-inference | Validator/tests | **ENFORCED** |
| P-44 | resumption не означает same Process identity | identity | Identity/Validator | **ENFORCED** |
| P-45 | same Process Content не означает same identity | identity | Identity/Validator | **ENFORCED** |
| P-46 | different descriptions не означают different Processes | identity | Identity/Validator | **ENFORCED** |
| P-47 | representation identity отличима от Process identity | identity | Identity/Validator | **MAPPED** |
| P-48 | different provenance не означает different Process | anti-inference | Validator/tests | **ENFORCED** |
| P-49 | merge/split/branching не устанавливают continuity автоматически | identity/history | Validator | **ENFORCED** |
| P-50 | decomposition не выдумывает stages/mechanisms/links | anti-inference | Transformation | **ENFORCED** |
| P-51 | composite Process не означает full decomposition | anti-inference | Validator/tests | **MAPPED** |
| P-52 | temporal containment не означает subprocess | anti-inference | Validator/tests | **ENFORCED** |
| P-53 | overlap не означает part-of | anti-inference | Validator/tests | **ENFORCED** |
| P-54 | допустимые decompositions не являются contradiction | anti-inference | Validator/tests | **ENFORCED** |
| P-55 | phase labels не определяют ontology | anti-inference | Profile | **MAPPED** |
| P-56 | temporal order не доказывает causality | anti-inference | Validator/tests | **ENFORCED** |
| P-57 | causal/mechanistic relations сохраняют provenance/uncertainty/Scope/Context | semantic | Validator/Provenance | **ENFORCED** |
| P-58 | observed pattern не доказывает feedback mechanism | anti-inference | Validator/tests | **ENFORCED** |
| P-59 | inputs/outputs/conditions не universal mandatory fields | architecture | Schema/Profile | **MAPPED** |
| P-60 | input не доказывает sole/full causation | anti-inference | Validator/tests | **ENFORCED** |
| P-61 | output не становится Result/Effect автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-62 | enabling condition не доказывает occurrence | anti-inference | Validator/tests | **ENFORCED** |
| P-63 | recurring cycles не доказывают identical identity | identity | Validator | **ENFORCED** |
| P-64 | rate/intensity/direction не определяют identity автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-65 | point rate не становится constant interval rate | temporal | Validator/tests | **ENFORCED** |
| P-66 | rate×duration не становится cumulative change без assumptions | semantic | Validator/Profile | **ENFORCED** |
| P-67 | lifecycle labels сохраняют domain semantics | context-dependent | Profile | **ENFORCED** |
| P-68 | completion не означает success/objective achievement | anti-inference | Validator/tests | **MAPPED** |
| P-69 | Natural Process не требует Actor | architecture | Profile | **MAPPED** |
| P-70 | logs/measurements не являются Process автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-71 | workflow/rule не является occurrence автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-72 | Process Scope различим от observation/data Scope | semantic | Scope-aware Validator | **ENFORCED** |
| P-73 | local/sample/aggregate semantics не становятся global/population/individual | anti-inference | Scope Validator | **ENFORCED** |
| P-74 | Process Context не drift | history/context | Context/History | **ENFORCED** |
| P-75 | simultaneous Processes не противоречат автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-76 | interaction не доказывает full causal mechanism | anti-inference | Validator/tests | **ENFORCED** |
| P-77 | Process provenance types remain resolvable | provenance | Provenance/Profile | **ENFORCED** |
| P-78 | unknown/non-observed различим от absence of Process | unknown-discipline | Validator/Profile | **MAPPED** |
| P-79 | negation occurrence не создаёт Process automatically | anti-inference | Validator/tests | **MAPPED** |
| P-80 | Process conflict требует time/scope/context/granularity/mechanism reconciliation | semantic | Validator L4/L5 | **ENFORCED** |
| P-81 | external labels не определяют canonical Process semantics | anti-inference | Import/Profile | **MAPPED** |
| P-82 | historical Process не наследует current model/context silently | history | Resolver/Validator | **ENFORCED** |
| P-83 | model/type revision не меняет historical Process автоматически | history | Versioning/Validator | **ENFORCED** |
| P-84 | Process-State link не становится causal автоматически | anti-inference | Validator/tests | **ENFORCED** |
| P-85 | start/interrupt/end Event не становится causal automatically | anti-inference | Validator/tests | **ENFORCED** |
| P-86 | material Process content/frame/context/time/continuity/scope/provenance/uncertainty preserved | fidelity | Transformation | **TESTED** |
| P-87 | structural conformance различима от occurrence/mechanism/causal certainty/quality/fidelity | anti-inference | Conformance/Validator | **MAPPED** |
| P-88 | Profile не ослабляет Core requirements | architecture | Registry/Validator | **ENFORCED** |
| P-89 | material uncertainty/provenance/frame/context/scales/continuity/scope resolvable | context-dependent | Profile/Transformation | **ENFORCED** |

## 5.5. Rule-by-rule matrix — STANDARD/013 Relation

Первичный rule-by-rule triage по каноническим `RL-01…RL-115`. `ENFORCED` означает наличие прямого машинного ограничения; `MAPPED` — правило уже закреплено архитектурно/типово; `DEFERRED` — требует отдельного semantic/context/history/transformation enforcement и не должно превращаться в ложное structural `required`.

| ID | Нормативное правило | Класс | Owner | Статус |
|---|---|---|---|---|
| RL-01 | Relation является semantic construct, representing a определённый semantic linkage among resolvable semantic positions/participants within a resolvable applicable frame. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| RL-02 | Relation semantics МОЖЕТ быть materialized as specialized Record когда материально useful, Но separate Relation Entity is not universally mandatory. | semantic | Profile/Validator | **ENFORCED** |
| RL-03 | Relation representation existence НЕ ДОЛЖЕН автоматически означать that представленный Relation objectively holds. | anti-inference | Profile/Validator | **TESTED** |
| RL-04 | Storage/graph implementation НЕ ДОЛЖЕН определять canonical Relation ontology. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-05 | Property, attribute or predicate НЕ ДОЛЖЕН автоматически быть treated as canonical Relation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-06 | Co-occurrence, spatial proximity, temporal proximity or textual proximity НЕ ДОЛЖЕН автоматически определять a specific Relation type. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-07 | Relation type, Relation model and Relation instance ДОЛЖЕН оставаться semantically distinguishable. | semantic | Profile/Validator | **ENFORCED** |
| RL-08 | Relation type НЕ ДОЛЖЕН автоматически быть treated as Relation model or Relation instance. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-09 | Relation model НЕ ДОЛЖЕН автоматически быть treated as Relation instance or Relation truth. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-10 | Mere enumeration, cataloguing or documentation of Relation types НЕ ДОЛЖЕН автоматически быть treated as Relation model. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-11 | Model edge НЕ ДОЛЖЕН автоматически быть treated as представленный/historical Relation instance. | history | Versioning/Validator | **ENFORCED** |
| RL-12 | Generic Relation knowledge НЕ ДОЛЖЕН автоматически устанавливать a specific historical Relation instance. | history | Versioning/Validator | **ENFORCED** |
| RL-13 | Class-level/generic Relation НЕ ДОЛЖЕН автоматически становиться universal instance-level Relation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-14 | Multiple instance-level Relations НЕ ДОЛЖЕН автоматически устанавливать class-level/generic Relation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-15 | Generalization from Relation instances ДОЛЖЕН требовать explicit Inference, Model, aggregation rule or other justified semantics. | semantic | Profile/Validator | **ENFORCED** |
| RL-16 | материально relevant quantification and modality ДОЛЖЕН оставаться разрешимым. | semantic | Profile/Validator | **ENFORCED** |
| RL-17 | Relation ДОЛЖЕН иметь sufficiently определённый Relation semantics. | structural/semantic | Schema + L4 | **ENFORCED** |
| RL-18 | Relation ДОЛЖЕН иметь resolvable semantic positions and participants где applicable. | structural/semantic | Schema + L4 | **ENFORCED** |
| RL-19 | Relation ДОЛЖЕН иметь a resolvable applicable frame. | structural/semantic | Schema + L4 | **ENFORCED** |
| RL-20 | Applicable frame and Scope ДОЛЖЕН оставаться различимым где conflation would материально alter meaning. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| RL-21 | Participant roles ДОЛЖЕН оставаться разрешимым когда omission would материально alter meaning. | semantic | Profile/Validator | **ENFORCED** |
| RL-22 | Relation attribution is semantic requirement and НЕ ДОЛЖЕН требовать dedicated Core Entity solely for conformance. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-23 | Relation arity ДОЛЖЕН оставаться различимым from number of различимый participant identities. | semantic | Profile/Validator | **ENFORCED** |
| RL-24 | Core НЕ ДОЛЖЕН принуждать every Relation into binary representation когда материально relevant n-ary semantics would быть lost. | architecture | Profile | **MAPPED** |
| RL-25 | N-ary Relation НЕ ДОЛЖЕН быть decomposed into binary edges Если decomposition destroys материально relevant role/qualifier structure. | architecture | Profile | **MAPPED** |
| RL-26 | Participant role ДОЛЖЕН оставаться различимым from participant identity. | semantic | Profile/Validator | **ENFORCED** |
| RL-27 | Ordered/asymmetric participant roles ДОЛЖЕН оставаться различимым from graph directionality когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-28 | Direction ДОЛЖЕН быть сохранённый когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-29 | Inverse Relation НЕ ДОЛЖЕН быть придуманный если не Relation semantics defines it. | anti-inference | Profile/Validator | **TESTED** |
| RL-30 | Symmetry, asymmetry, transitivity, reflexivity, functionality and other formal properties НЕ ДОЛЖЕН быть предполагаемым universally. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-31 | Formal Relation properties СЛЕДУЕТ быть understood relative to определённый Relation type/frame/model. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| RL-32 | Formal property допустимый in Frame X НЕ ДОЛЖЕН автоматически быть transferred to Frame Y. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-33 | Relation chaining НЕ ДОЛЖЕН автоматически устанавливать a new direct Relation если не explicit logic licenses the Inference. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-34 | Relation composition ДОЛЖЕН оставаться различимым from transitivity. | semantic | Profile/Validator | **ENFORCED** |
| RL-35 | Heterogeneous composition НЕ ДОЛЖЕН быть inferred без определённый composition logic. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-36 | Inferred closure Relations ДОЛЖЕН сохранять derivation/provenance. | provenance | Provenance/Validator | **ENFORCED** |
| RL-37 | Claim about Relation ДОЛЖЕН оставаться различимым from Relation. | semantic | Profile/Validator | **ENFORCED** |
| RL-38 | Inferred Relation ДОЛЖЕН оставаться различимым from Inference itself. | semantic | Profile/Validator | **ENFORCED** |
| RL-39 | Relation ДОЛЖЕН оставаться различимым from Event, Process, Action and Result. | semantic | Type/Profile | **MAPPED** |
| RL-40 | Relation and State МОЖЕТ overlap in relational-State semantics Но НЕ ДОЛЖЕН схлопываться universally. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-41 | Relation temporal/domain validity ДОЛЖЕН оставаться различимым from record time, assertion/publication time, representation history and epistemic acceptance interval. | semantic | Profile/Validator | **ENFORCED** |
| RL-42 | Relation snapshot НЕ ДОЛЖЕН автоматически expand into interval validity. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-43 | Open-ended Relation validity НЕ ДОЛЖЕН автоматически означать current or permanent validity. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-44 | Absence of Evidence of Relation termination НЕ ДОЛЖЕН автоматически устанавливать persistence. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-45 | Current Relation НЕ ДОЛЖЕН незаметно overwrite historical Relation. | history | Versioning/Validator | **TESTED** |
| RL-46 | Changed Relation representation НЕ ДОЛЖЕН автоматически означать представленный Relation changed. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-47 | Identity of Relation representation ДОЛЖЕН оставаться различимым from identity/continuity of представленный Relation instance. | semantic | Profile/Validator | **ENFORCED** |
| RL-48 | Relation instance identity МОЖЕТ зависеть от полный материально relevant participant-role/qualifier/frame structure. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| RL-49 | Same participants and same Relation type НЕ ДОЛЖЕН автоматически означать same Relation instance. | anti-inference | Profile/Validator | **TESTED** |
| RL-50 | Change in qualifier/value НЕ ДОЛЖЕН автоматически определять either continuity or replacement of Relation instance. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-51 | Relation continuity/identity under qualifier/value change ДОЛЖЕН зависеть от определённый domain/Profile semantics. | semantic | Profile/Validator | **ENFORCED** |
| RL-52 | Different provenance НЕ ДОЛЖЕН автоматически означать different представленный Relation instance. | provenance | Provenance/Validator | **ENFORCED** |
| RL-53 | Generic Relation НЕ ДОЛЖЕН незаметно inherit stronger Relation semantics. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-54 | известный specific Relation НЕ СЛЕДУЕТ быть degraded to generic Relation когда specificity is материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-55 | Association НЕ ДОЛЖЕН автоматически становиться dependency or causality. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-56 | Similarity НЕ ДОЛЖЕН автоматически становиться identity. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-57 | Similarity СЛЕДУЕТ сохранять материально relevant comparison basis. | semantic | Profile/Validator | **ENFORCED** |
| RL-58 | Temporal order НЕ ДОЛЖЕН автоматически становиться causality. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-59 | Part-of, member-of, containment and temporal containment ДОЛЖЕН оставаться различимым когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-60 | Causal Relation НЕ ДОЛЖЕН быть inferred solely from correlation, temporal order, proximity, co-occurrence, sequence or narrative. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-61 | Causal Relation НЕ ДОЛЖЕН автоматически означать responsibility, blame, intention or negligence. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-62 | Dependency НЕ ДОЛЖЕН автоматически означать causality. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-63 | Enabling Relation НЕ ДОЛЖЕН автоматически означать occurrence. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-64 | Evidence поддерживать НЕ ДОЛЖЕН автоматически означать proof or truth. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-65 | Multiple supporting Relations НЕ ДОЛЖЕН автоматически быть treated as independent evidence lines. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-66 | Contradiction Relation НЕ ДОЛЖЕН автоматически означать that one Claim is false без further epistemic analysis. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-67 | Consistent-with НЕ ДОЛЖЕН автоматически означать confirmation or strong поддерживать. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-68 | Derived-from НЕ ДОЛЖЕН автоматически означать causal production. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-69 | Citation НЕ ДОЛЖЕН автоматически означать evidential поддерживать or independent corroboration. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-70 | Reference Relation НЕ ДОЛЖЕН автоматически означать endorsement, dependency or identity. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-71 | Entity identity, coreference, Record identity, representation identity and semantic equivalence ДОЛЖЕН оставаться различимым когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-72 | `same-as` НЕ ДОЛЖЕН быть used as universal bucket for identity-like semantics. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-73 | Identity Relation ДОЛЖЕН требовать stronger поддерживать than similarity, label equality or overlapping properties. | semantic | Profile/Validator | **ENFORCED** |
| RL-74 | Equivalence ДОЛЖЕН оставаться различимым from identity когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-75 | Version/supersession/replacement Relations ДОЛЖЕН сохранять historical provenance and НЕ ДОЛЖЕН автоматически erase prior representations. | provenance | Provenance/Validator | **ENFORCED** |
| RL-76 | Classification Relations such as instance-of and subclass-of ДОЛЖЕН оставаться различимым. | semantic | Profile/Validator | **ENFORCED** |
| RL-77 | Normative Relation НЕ ДОЛЖЕН автоматически становиться actual Action/State Relation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-78 | Authorization НЕ ДОЛЖЕН автоматически означать Action. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-79 | Obligation НЕ ДОЛЖЕН автоматически означать compliance. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-80 | Prohibition НЕ ДОЛЖЕН автоматически означать empirical absence. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-81 | Legal Relation and de facto Relation ДОЛЖЕН оставаться различимым когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-82 | Participation НЕ ДОЛЖЕН автоматически означать causation, responsibility, leadership or intention. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-83 | Presence-at НЕ ДОЛЖЕН автоматически означать participation-in or witness-of. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-84 | Transformation Relation НЕ ДОЛЖЕН автоматически устанавливать identity continuity. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-85 | неизвестный Relation, no-record-of-Relation and Relation absence ДОЛЖЕН оставаться различимым. | semantic | Profile/Validator | **ENFORCED** |
| RL-86 | Negated Relation ДОЛЖЕН оставаться различимым from неизвестный, unrecorded, incompatible and prohibited Relation semantics. | semantic | Profile/Validator | **ENFORCED** |
| RL-87 | Negation of Relation НЕ ДОЛЖЕН автоматически требовать a special negative Relation Entity. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-88 | Relation conflict НЕ ДОЛЖЕН быть asserted before материально sufficient participant, role, temporal, Context, Scope, qualifier, quantification and type alignment. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-89 | External Relation labels НЕ ДОЛЖЕН автоматически определять canonical Relation type. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-90 | Natural-language ambiguity НЕ ДОЛЖЕН быть resolved by inventing missing direction, causality, strength, quantification or role semantics. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-91 | Observed, measured, computed, inferred, modeled and reconstructed Relation provenance МОЖЕТ overlap and ДОЛЖЕН оставаться разрешимым когда материально relevant. | provenance | Provenance/Validator | **ENFORCED** |
| RL-92 | Relation strength ДОЛЖЕН оставаться Relation-type-specific and НЕ ДОЛЖЕН receive universal scale semantics. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-93 | Probabilistic Relation НЕ ДОЛЖЕН незаметно становиться deterministic Relation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-94 | Statistical Relation ДОЛЖЕН сохранять материально relevant population, period and conditioning frame. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| RL-95 | Correlation НЕ ДОЛЖЕН автоматически становиться causation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-96 | Marginal association/correlation НЕ ДОЛЖЕН автоматически быть treated as conditional association/correlation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-97 | Contradiction between Claims ДОЛЖЕН оставаться различимым from incompatibility between представленный world States. | semantic | Profile/Validator | **ENFORCED** |
| RL-98 | Basis-for НЕ ДОЛЖЕН автоматически быть treated as cause-of. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-99 | Later-discovered Relation НЕ ДОЛЖЕН быть inserted retroactively into earlier Decision Basis. | history | Versioning/Validator | **ENFORCED** |
| RL-100 | Historical Relation НЕ ДОЛЖЕН незаметно inherit current participants, taxonomy, jurisdiction, Context, model or Relation-type semantics. | history | Versioning/Validator | **ENFORCED** |
| RL-101 | Ontology/meta-model Relations СЛЕДУЕТ оставаться различимым from domain/world Relations когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-102 | Higher-order Relation semantics НЕ ДОЛЖЕН требовать universal reification of all Relations. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-103 | A Relation representation used as participant in a higher-order Relation ДОЛЖЕН оставаться различимым from the представленный Relation itself когда материально relevant. | semantic | Profile/Validator | **ENFORCED** |
| RL-104 | Higher-order Relation ДОЛЖЕН сохранять whether its target is representation, assertion, semantic Relation instance or another referenceable layer когда this distinction материально affects meaning. | semantic | Profile/Validator | **ENFORCED** |
| RL-105 | Cardinality and exclusivity constraints НЕ ДОЛЖЕН быть предполагаемым universally. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-106 | Relation Scope ДОЛЖЕН оставаться разрешимым когда материально relevant. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| RL-107 | Local/sample/aggregate Relation НЕ ДОЛЖЕН автоматически становиться global/population/individual Relation. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-108 | Group-level Relation НЕ ДОЛЖЕН автоматически становиться individual-level Relation, and vice versa. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-109 | Context-dependent Relation НЕ ДОЛЖЕН незаметно generalize across Contexts. | anti-inference | Profile/Validator | **ENFORCED** |
| RL-110 | Relation role distinctions in Action/Event/Process/Result structures ДОЛЖЕН оставаться явным когда material. | semantic | Profile/Validator | **ENFORCED** |
| RL-111 | Modeled Relation ДОЛЖЕН оставаться различимым from observed/historical Relation. | history | Versioning/Validator | **ENFORCED** |
| RL-112 | Representation ДОЛЖЕН сохранять материально relevant Relation type/model/instance role, semantic positions, participants, roles, arity, direction, qualifiers, quantification, temporal validity, Scope, Context, applicable frame, provenance and uncertainty. | provenance | Provenance/Validator | **ENFORCED** |
| RL-113 | Core structural/semantic conformance ДОЛЖЕН оставаться различимым from Relation truth, provenance integrity, causal validity, logical validity, Relation quality and Representation Fidelity. | provenance | Provenance/Validator | **ENFORCED** |
| RL-114 | Profile МОЖЕТ strengthen Core requirements Но НЕ ДОЛЖЕН weaken Core пока claiming compatibility with `013`. | architecture | Registry/Validator | **ENFORCED** |
| RL-115 | материально relevant uncertainty, provenance, participant identity, participant roles, quantification, temporal validity, Scope and applicable frame ДОЛЖЕН оставаться разрешимым. | provenance | Provenance/Validator | **ENFORCED** |

## 5.6. Rule-by-rule matrix — STANDARD/014 Identity

`PARTIAL` означает: Schema уже хранит часть требуемой структуры, но не обеспечивает полную семантику правила. `DEFERRED` не означает, что правило отменено; оно требует Identity/Scope/History-aware enforcement.

| ID | Нормативное правило | Класс | Owner | Статус |
|---|---|---|---|---|
| ID-01 | Identity ДОЛЖЕН оставаться разрешимым relative to an identity-bearing level/frame когда ambiguity is материально relevant. | semantic | Identity/Validator | **ENFORCED** |
| ID-02 | Identity НЕ ДОЛЖЕН быть treated as one universal undifferentiated `same-as`. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-03 | Identity criterion ДОЛЖЕН оставаться разрешимым когда choice of criterion материально affects identity judgment. | semantic | Identity/Validator | **ENFORCED** |
| ID-04 | No identity criterion receives universal privilege across all domains. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-05 | Identity frame, identity criterion and Identity Scope ДОЛЖЕН оставаться различимым когда материально relevant. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-06 | Identity criterion ДОЛЖЕН оставаться различимым from identity Evidence. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-07 | Entity identity, referent identity, coreference, Record identity, representation identity, semantic equivalence and value equality ДОЛЖЕН оставаться различимым когда material. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-08 | Identity representation/assertion НЕ ДОЛЖЕН автоматически быть treated as identity truth. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-09 | Identity semantics НЕ ДОЛЖЕН требовать a dedicated fundamental Identity Entity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-10 | Same referent НЕ ДОЛЖЕН автоматически означать same Record. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-11 | Different Records НЕ ДОЛЖЕН автоматически означать различимый referents. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-12 | Same Record НЕ ДОЛЖЕН автоматически означать same carrier/representation instance. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-13 | Representation-of, description-of, model-of and record-about НЕ ДОЛЖЕН автоматически означать identity with представленный subject. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-14 | Semantic equivalence НЕ ДОЛЖЕН автоматически означать Entity or Record identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-15 | Value equality НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-16 | Attribute equality НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-17 | Similarity НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-18 | Equivalence НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-19 | Qualified sameness НЕ ДОЛЖЕН автоматически inherit strict identity semantics. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-20 | Interchangeability НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-21 | Same classification НЕ ДОЛЖЕН означать same instance. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-22 | Lexical/name equality НЕ ДОЛЖЕН автоматически устанавливать referent identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-23 | Name difference НЕ ДОЛЖЕН автоматически устанавливать distinctness. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-24 | Alias НЕ ДОЛЖЕН автоматически быть treated as proven identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-25 | Renaming НЕ ДОЛЖЕН автоматически означать new Entity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-26 | Identifier ДОЛЖЕН оставаться различимым from Entity. | semantic | Identity/Validator | **ENFORCED** |
| ID-27 | Identifier namespace ДОЛЖЕН оставаться разрешимым когда material. | semantic | Identity/Validator | **ENFORCED** |
| ID-28 | Same identifier string across namespaces НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-29 | Identifier uniqueness НЕ ДОЛЖЕН быть generalized beyond declared governance/frame. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-30 | Persistent identifier НЕ ДОЛЖЕН автоматически prove unchanged referent. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-31 | Identifier reuse/reassignment ДОЛЖЕН оставаться representable. | semantic | Identity/Validator | **ENFORCED** |
| ID-32 | Identity resolution СЛЕДУЕТ сохранять материально relevant provenance. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-33 | No individual identity signal is universally sufficient. | semantic | Identity/Validator | **ENFORCED** |
| ID-34 | Multiple weak signals НЕ ДОЛЖЕН автоматически устанавливать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-35 | Single mismatch НЕ ДОЛЖЕН автоматически устанавливать distinctness. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-36 | Identity resolution ДОЛЖЕН оставаться различимым from identity judgment/relation. | semantic | Identity/Validator | **ENFORCED** |
| ID-37 | System-resolved identity ДОЛЖЕН оставаться scoped to applicable semantics and НЕ ДОЛЖЕН автоматически становиться universal identity truth. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-38 | Source-asserted identity ДОЛЖЕН оставаться различимым from system-resolved identity. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-39 | Identity assertion МОЖЕТ оставаться a Claim без forcing merge. | semantic | Identity/Validator | **ENFORCED** |
| ID-40 | неизвестный identity ДОЛЖЕН оставаться различимым from sameness and distinctness. | semantic | Identity/Validator | **ENFORCED** |
| ID-41 | Failure to prove identity НЕ ДОЛЖЕН устанавливать distinctness автоматически. | anti-inference | Identity/Validator | **TESTED** |
| ID-42 | Distinctness МОЖЕТ требовать independent evidence/provenance. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-43 | Distinctness ДОЛЖЕН сохранять applicable identity level/frame/criterion/Scope где материально relevant. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-44 | Competing identity resolutions ДОЛЖЕН оставаться representable. | semantic | Identity/Validator | **ENFORCED** |
| ID-45 | Identity inconsistency detection НЕ ДОЛЖЕН автоматически resolve inconsistency. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-46 | Uncertain identity НЕ ДОЛЖЕН незаметно становиться hard merge. | anti-inference | Identity/Validator | **TESTED** |
| ID-47 | Data merge/canonicalization ДОЛЖЕН оставаться различимым from semantic identity resolution. | semantic | Identity/Validator | **ENFORCED** |
| ID-48 | Canonical Record ДОЛЖЕН оставаться различимым from underlying Entity. | semantic | Identity/Validator | **ENFORCED** |
| ID-49 | Canonicalization/golden-record synthesis НЕ ДОЛЖЕН erase provenance, uncertainty or disagreement. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-50 | Duplicate Record ДОЛЖЕН оставаться различимым from duplicate Entity. | semantic | Identity/Validator | **ENFORCED** |
| ID-51 | Duplicate content НЕ ДОЛЖЕН означать same Record or same provenance автоматически. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-52 | Work, edition, version, copy and representation identity ДОЛЖЕН оставаться различимым где material. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-53 | Bit/content equality НЕ ДОЛЖЕН автоматически означать domain Entity identity. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-54 | Version-of НЕ ДОЛЖЕН автоматически означать same representation. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-55 | Correction НЕ ДОЛЖЕН автоматически означать new underlying referent. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-56 | Translation-of НЕ ДОЛЖЕН автоматически означать textual identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-57 | State/property/location/ownership/control change НЕ ДОЛЖЕН автоматически означать new Entity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-58 | Transformation НЕ ДОЛЖЕН автоматически устанавливать identity persistence. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-59 | Identity persistence ДОЛЖЕН оставаться различимым from unchanged State. | semantic | Identity/Validator | **ENFORCED** |
| ID-60 | Material, spatial, temporal, functional and legal continuity receive no universal identity privilege. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-61 | Membership continuity receives no universal group-identity privilege. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-62 | Merger НЕ ДОЛЖЕН автоматически identify successor with every predecessor. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-63 | Split/fission НЕ ДОЛЖЕН автоматически identify every descendant with predecessor. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-64 | Successor-of НЕ ДОЛЖЕН автоматически означать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-65 | Lineage continuity ДОЛЖЕН оставаться различимым from identity continuity. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-66 | Part-of, component-of and fragment-of НЕ ДОЛЖЕН автоматически означать identity with whole. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-67 | Sample/specimen/derived material НЕ ДОЛЖЕН автоматически inherit source Entity identity. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-68 | Cross-type correspondence НЕ ДОЛЖЕН автоматически устанавливать identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-69 | Cross-type identity, where valid, requires explicit applicable semantics. | semantic | Identity/Validator | **ENFORCED** |
| ID-70 | Genetic similarity/identity НЕ ДОЛЖЕН автоматически означать organism identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-71 | Historical identity resolution ДОЛЖЕН сохранять материально relevant historical names, Sources, frames and uncertainty. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-72 | Historical homonyms НЕ ДОЛЖЕН быть merged solely by label equality. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-73 | Role/title/office identity ДОЛЖЕН оставаться различимым from holder identity. | semantic | Identity/Validator | **ENFORCED** |
| ID-74 | Current geographic boundaries НЕ ДОЛЖЕН автоматически определять historical geographic identity. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-75 | Event coreference НЕ ДОЛЖЕН быть установленный solely from date/place/description similarity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-76 | Different Event granularity НЕ ДОЛЖЕН автоматически означать identity or contradiction. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-77 | Same Process Content НЕ ДОЛЖЕН автоматически означать same Process. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-78 | Same State value НЕ ДОЛЖЕН автоматически означать same State identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-79 | Same participants + Relation type НЕ ДОЛЖЕН автоматически означать same Relation instance. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-80 | Repeated Action type НЕ ДОЛЖЕН означать same Action instance. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-81 | Same Result value/content НЕ ДОЛЖЕН автоматически означать same Result instance. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-82 | Propositional equivalence НЕ ДОЛЖЕН означать Claim Record identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-83 | Same Source content НЕ ДОЛЖЕН автоматически означать same Source instance когда provenance matters. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-84 | Same measured value НЕ ДОЛЖЕН означать same Measurement. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-85 | Same Model output НЕ ДОЛЖЕН означать same Model. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-86 | Lexical continuity НЕ ДОЛЖЕН автоматически означать Concept identity across time/domains. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-87 | Scope-limited identity НЕ ДОЛЖЕН незаметно становиться unrestricted identity. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-88 | Qualified identity language ДОЛЖЕН сохранять its qualifier. | semantic | Identity/Validator | **ENFORCED** |
| ID-89 | Temporal validity of identity mapping ДОЛЖЕН оставаться разрешимым когда material. | semantic | Identity/Validator | **ENFORCED** |
| ID-90 | Temporal succession НЕ ДОЛЖЕН автоматически устанавливать identity continuity. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-91 | Identity boundary МОЖЕТ быть fuzzy, conventional, legal, disputed or неизвестный. | semantic | Identity/Validator | **ENFORCED** |
| ID-92 | Identity boundary НЕ ДОЛЖЕН автоматически быть modeled as Event. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-93 | State/Event/Process boundaries НЕ ДОЛЖЕН автоматически определять Entity identity boundaries. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-94 | Strict identity logical properties apply only under compatible level, frame, criterion, Scope, temporal validity and semantics. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-95 | Reference reflexivity НЕ ДОЛЖЕН быть treated as resolved referent identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-96 | Symmetry of strict identity НЕ ДОЛЖЕН быть inherited by directional mappings, succession, derivation, part-whole or representation relations. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-97 | Identity НЕ ДОЛЖЕН propagate transitively across incompatible identity levels, criteria, frames, Scopes, temporal validity or uncertainty semantics. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-98 | Probabilistic/uncertain coreference НЕ ДОЛЖЕН автоматически inherit strict identity transitivity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-99 | Identity probabilities НЕ ДОЛЖЕН быть naively composed без explicit probabilistic Model and dependency assumptions. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-100 | Mixed chains of identity-adjacent relations НЕ ДОЛЖЕН быть laundered into strict identity без an explicit допустимый identity inference. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-101 | Algorithmic match НЕ ДОЛЖЕН автоматически быть treated as identity truth. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-102 | Threshold merge policy ДОЛЖЕН оставаться различимым from semantic identity judgment. | semantic | Identity/Validator | **ENFORCED** |
| ID-103 | Identity resolution СЛЕДУЕТ оставаться reversible где материально feasible. | semantic | Identity/Validator | **ENFORCED** |
| ID-104 | Identity correction СЛЕДУЕТ сохранять prior материально relevant mappings and provenance. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-105 | Later referent resolution НЕ ДОЛЖЕН retroactively alter original Source/reference semantics. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-106 | Coreference НЕ ДОЛЖЕН схлопываться independent provenance. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-107 | Identity resolution НЕ ДОЛЖЕН автоматически erase factual conflicts. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-108 | Identity-based propagation ДОЛЖЕН сохранять time, Context, Scope, role, provenance and uncertainty. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-109 | Uncertain identity НЕ ДОЛЖЕН незаметно propagate linked Claims as certain knowledge. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-110 | Historical identity/coreference НЕ ДОЛЖЕН автоматически переносить responsibility, rights, ownership, territory, ancestry, achievements, obligations or authority. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-111 | Identity ДОЛЖЕН оставаться различимым from responsibility inheritance, entitlement and ownership continuity. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-112 | Authority-определённый identity ДОЛЖЕН оставаться scoped to relevant authoritative frame. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-113 | Competing identity systems МОЖЕТ coexist когда frames/criteria are explicit. | semantic | Identity/Validator | **ENFORCED** |
| ID-114 | Cross-system mapping НЕ ДОЛЖЕН автоматически означать exact identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-115 | One-to-many and many-to-one mappings ДОЛЖЕН оставаться representable. | semantic | Identity/Validator | **ENFORCED** |
| ID-116 | Identity-cluster membership НЕ ДОЛЖЕН автоматически означать identity truth. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-117 | Normalization ДОЛЖЕН оставаться различимым from identity resolution. | semantic | Identity/Validator | **ENFORCED** |
| ID-118 | Hash/checksum equality НЕ ДОЛЖЕН автоматически определять domain Entity identity. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-119 | Physical label/serial identity НЕ ДОЛЖЕН автоматически определять object identity outside определённый governance assumptions. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-120 | Aggregate/group identity ДОЛЖЕН оставаться различимым from member identity. | semantic | Identity/Validator | **ENFORCED** |
| ID-121 | Dataset lineage ДОЛЖЕН оставаться различимым from dataset-version identity. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-122 | Software product/codebase/version/build/deployment/process identity ДОЛЖЕН оставаться различимым когда material. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-123 | Physical identity criteria НЕ ДОЛЖЕН быть blindly transferred to abstract objects. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-124 | Ontology/taxonomy migration НЕ ДОЛЖЕН автоматически означать domain Entity change. | context-dependent | Identity/Scope-aware Validator | **ENFORCED** |
| ID-125 | Carrier/serialization technology НЕ ДОЛЖЕН определять semantic identity. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-126 | Historical reconstruction ДОЛЖЕН сохранять материально relevant alternatives, Sources and assumptions. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-127 | Missing identity evidence НЕ ДОЛЖЕН быть придуманный to produce a clean graph. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-128 | Evidence item ДОЛЖЕН оставаться различимым from Entity it evidences. | evidence/provenance | Identity/Validator | **ENFORCED** |
| ID-129 | Identity structure conformance ДОЛЖЕН оставаться различимым from identity truth and historical certainty. | history/identity | Identity/Versioning/Validator | **ENFORCED** |
| ID-130 | Profile МОЖЕТ strengthen Core identity requirements Но НЕ ДОЛЖЕН weaken Core пока claiming compatibility. | anti-inference | Identity/Validator | **ENFORCED** |
| ID-131 | материально relevant identity level, frame, criterion, Scope, temporal validity, uncertainty, provenance and competing candidates ДОЛЖЕН оставаться разрешимым. | evidence/provenance | Identity/Validator | **ENFORCED** |

## 5.7. Rule-by-rule matrix — STANDARD/015 Context

| ID | Нормативное правило | Класс | Owner | Статус |
|---|---|---|---|---|
| CTX-01 | Context represents conditions considered materially relevant or potentially materially relevant relative to a contextualized target. | semantic | Context/Validator | **PARTIAL** |
| CTX-02 | Recorded Context НЕ ДОЛЖЕН автоматически быть treated as полный real-world Context. | anti-inference | Context/Validator | **PARTIAL** |
| CTX-03 | Context semantics НЕ ДОЛЖЕН требовать a dedicated fundamental Context Entity. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-04 | Context target ДОЛЖЕН оставаться разрешимым где target ambiguity материально affects meaning. | semantic | Context/Validator | **ENFORCED** |
| CTX-05 | Context МОЖЕТ target an entire representation or a определённый semantic component. | semantic | Context/Validator | **ENFORCED** |
| CTX-06 | Context ДОЛЖЕН оставаться различимым from contextualized object. | semantic | Context/Validator | **ENFORCED** |
| CTX-07 | Context ДОЛЖЕН оставаться различимым from State. | semantic | Context/Validator | **ENFORCED** |
| CTX-08 | The same factual condition МОЖЕТ участвовать в State and Context semantics без making them identical. | semantic | Context/Validator | **ENFORCED** |
| CTX-09 | Context need not be external to contextualized system. | semantic | Context/Validator | **ENFORCED** |
| CTX-10 | Context НЕ ДОЛЖЕН автоматически быть treated as Participant. | anti-inference | Context/Validator | **TESTED** |
| CTX-11 | Context ДОЛЖЕН оставаться различимым from Scope. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-12 | A condition МОЖЕТ play Context and Scope roles simultaneously, Но roles ДОЛЖЕН оставаться различимым когда material. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-13 | Context ДОЛЖЕН оставаться различимым from semantic/reference frame. | semantic | Context/Validator | **ENFORCED** |
| CTX-14 | Context НЕ ДОЛЖЕН автоматически определять semantic/reference frame. | anti-inference | Context/Validator | **TESTED** |
| CTX-15 | Context ДОЛЖЕН оставаться различимым from Profile. | semantic | Context/Validator | **ENFORCED** |
| CTX-16 | Context ДОЛЖЕН оставаться различимым from Assumption. | semantic | Context/Validator | **ENFORCED** |
| CTX-17 | Context values ДОЛЖЕН сохранять материально relevant epistemic status. | semantic | Context/Validator | **TESTED** |
| CTX-18 | Observed, measured, reported, предполагаемым, inferred, modeled and reconstructed Context НЕ ДОЛЖЕН незаметно схлопываться когда reused or summarized. | anti-inference | Context/Validator | **TESTED** |
| CTX-19 | Context ДОЛЖЕН оставаться различимым from Preconditions. | semantic | Context/Validator | **ENFORCED** |
| CTX-20 | Contextual factor НЕ ДОЛЖЕН автоматически быть treated as causal factor. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-21 | Contextual relevance НЕ ДОЛЖЕН автоматически означать causality. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-22 | Context ДОЛЖЕН оставаться различимым from Evidence. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-23 | Context ДОЛЖЕН оставаться различимым from Provenance. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-24 | Storage metadata НЕ ДОЛЖЕН автоматически становиться domain Context. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-25 | A fact НЕ ДОЛЖЕН быть classified merely as Context когда a more specific semantic role is материально relevant. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-26 | Context МОЖЕТ быть incomplete; missing values НЕ ДОЛЖЕН быть придуманный. | anti-inference | Context/Validator | **TESTED** |
| CTX-27 | неизвестный/missing Context НЕ ДОЛЖЕН автоматически означать universal applicability. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-28 | неизвестный/missing Context НЕ ДОЛЖЕН автоматически означать invalidity or uselessness. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-29 | Context independence ДОЛЖЕН требовать positive поддерживать когда material. | semantic | Context/Validator | **ENFORCED** |
| CTX-30 | Context dimensions НЕ ДОЛЖЕН быть forced into a universal fixed list. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-31 | Context decomposition НЕ ДОЛЖЕН означать independence among dimensions. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-32 | Context dimensions МОЖЕТ carry dependencies and joint constraints. | semantic | Context/Validator | **ENFORCED** |
| CTX-33 | Context values ДОЛЖЕН сохранять материально relevant units, definitions, uncertainty and precision. | semantic | Context/Validator | **ENFORCED** |
| CTX-34 | Phenomenon time ДОЛЖЕН оставаться различимым from Observation, Measurement, Source and Record times. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-35 | Spatial Context ДОЛЖЕН оставаться различимым from Scope. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-36 | Technical/version Context НЕ ДОЛЖЕН незаметно generalize across versions. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-37 | Biological Context НЕ ДОЛЖЕН незаметно generalize across populations or life stages где material. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-38 | Cultural/linguistic Context НЕ ДОЛЖЕН незаметно inherit foreign/current semantics. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-39 | Legal Context ДОЛЖЕН сохранять jurisdiction and temporal regime где material. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-40 | Experimental/Measurement Context ДОЛЖЕН сохранять материально relevant protocol/method conditions. | semantic | Context/Validator | **ENFORCED** |
| CTX-41 | Model Context НЕ ДОЛЖЕН незаметно становиться real-world Context. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-42 | Procedure/Action safety or Effect in Context X НЕ ДОЛЖЕН автоматически generalize to Context Y. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-43 | Process dynamics in Context X НЕ ДОЛЖЕН автоматически generalize to Context Y. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-44 | Result observed in Context X НЕ ДОЛЖЕН автоматически устанавливать Result expectation in Context Y. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-45 | Relation holding in Context X НЕ ДОЛЖЕН автоматически generalize beyond X. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-46 | Generic Claim НЕ ДОЛЖЕН автоматически быть interpreted as universal across Contexts. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-47 | Context alignment СЛЕДУЕТ precede contradiction judgment где material. | semantic | Context/Validator | **ENFORCED** |
| CTX-48 | Context mismatch МОЖЕТ explain apparent contradiction Но НЕ ДОЛЖЕН автоматически resolve it. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-49 | Context drift НЕ ДОЛЖЕН незаметно alter knowledge applicability. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-50 | Context substitution НЕ ДОЛЖЕН occur без explicit justified semantics. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-51 | Context inheritance НЕ ДОЛЖЕН быть предполагаемым merely from structural nesting. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-52 | Inherited Context НЕ ДОЛЖЕН быть applied across известный incompatible conditions. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-53 | неизвестный Context compatibility НЕ ДОЛЖЕН быть treated as compatibility. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-54 | More-specific Context МОЖЕТ override, qualify or block inherited Context. | semantic | Context/Validator | **ENFORCED** |
| CTX-55 | Context inheritance МОЖЕТ быть dimension-specific. | semantic | Context/Validator | **ENFORCED** |
| CTX-56 | Inherited dimensions НЕ ДОЛЖЕН автоматически быть предполагаемым compatible merely because another dimension was validly inherited. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-57 | Material inherited Context ДОЛЖЕН оставаться portable with extracted/reused knowledge. | semantic | Context/Validator | **ENFORCED** |
| CTX-58 | Context values from separate provenance НЕ ДОЛЖЕН быть composed into one Context представленный as obtaining без justified co-occurrence/compatibility. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-59 | Provenance-preserving Context composition НЕ ДОЛЖЕН быть mistaken for evidence of co-occurrence. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-60 | Conflicting Context representations ДОЛЖЕН оставаться representable with provenance. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-61 | Default Context НЕ ДОЛЖЕН автоматически быть treated as Context представленный as obtaining. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-62 | Template/nominal Context НЕ ДОЛЖЕН автоматически быть treated as Context представленный as obtaining. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-63 | Context uncertainty ДОЛЖЕН оставаться representable. | semantic | Context/Validator | **ENFORCED** |
| CTX-64 | Context inclusion НЕ ДОЛЖЕН автоматически устанавливать material relevance. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-65 | Potentially материально relevant Context МОЖЕТ оставаться представленный пока its relevance remains uncertain. | semantic | Context/Validator | **ENFORCED** |
| CTX-66 | Representation СЛЕДУЕТ сохранять материально relevant Context без requiring exhaustive reality description. | semantic | Context/Validator | **ENFORCED** |
| CTX-67 | Later Context refinement НЕ ДОЛЖЕН переписывать original Source semantics. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-68 | Later Context reconstruction НЕ ДОЛЖЕН быть представлен как original Source Context assertion. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-69 | Context representation revision НЕ ДОЛЖЕН автоматически означать представленный real-world Context changed. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-70 | Context temporal validity ДОЛЖЕН оставаться разрешимым когда material. | semantic | Context/Validator | **ENFORCED** |
| CTX-71 | Context snapshot НЕ ДОЛЖЕН автоматически expand to interval constancy. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-72 | Observation gaps НЕ ДОЛЖЕН устанавливать Context continuity or change автоматически. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-73 | Context transition НЕ ДОЛЖЕН автоматически быть modeled as Event. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-74 | Context similarity НЕ ДОЛЖЕН автоматически означать Context identity. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-75 | Context equivalence ДОЛЖЕН оставаться purpose-qualified. | semantic | Context/Validator | **ENFORCED** |
| CTX-76 | Context compatibility МОЖЕТ быть partial, conditional, dimension-specific, uncertain or неизвестный. | semantic | Context/Validator | **ENFORCED** |
| CTX-77 | Context compatibility НЕ ДОЛЖЕН автоматически устанавливать Claim applicability. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-78 | Transferability МОЖЕТ быть partial, conditional, dimension-specific, uncertain or неизвестный. | semantic | Context/Validator | **ENFORCED** |
| CTX-79 | Knowledge переносить across материально different Contexts ДОЛЖЕН требовать justified переносить semantics. | semantic | Context/Validator | **ENFORCED** |
| CTX-80 | Validity in Context X НЕ ДОЛЖЕН автоматически означать validity in Context Y. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-81 | Missing Context НЕ ДОЛЖЕН автоматически определять either transferability or non-transferability. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-82 | Multiple Context-specific observations НЕ ДОЛЖЕН автоматически устанавливать universal Context independence. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-83 | Invariance across tested Contexts НЕ ДОЛЖЕН автоматически означать invariance across all Contexts. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-84 | Context-specific exceptions ДОЛЖЕН оставаться representable без forced universal contradiction. | semantic | Context/Validator | **ENFORCED** |
| CTX-85 | Chains of Context similarity, compatibility, equivalence or переносить НЕ ДОЛЖЕН быть laundered into unrestricted applicability. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-86 | Boundary conditions and operating envelopes ДОЛЖЕН оставаться сохраняемым где материально relevant. | semantic | Context/Validator | **ENFORCED** |
| CTX-87 | неизвестный behavior outside an operating envelope НЕ ДОЛЖЕН автоматически становиться известный failure or известный safety. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-88 | All материально safety-critical Context dimensions required for a safety judgment ДОЛЖЕН survive reuse, translation, summarization and compression. | structural/semantic | Schema + L4 | **ENFORCED** |
| CTX-89 | Partial preservation of safety-critical Context МОЖЕТ constitute material Context loss. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-90 | Decision Context ДОЛЖЕН reflect материально relevant information/conditions available at Decision time. | semantic | Context/Validator | **ENFORCED** |
| CTX-91 | Later Context knowledge НЕ ДОЛЖЕН быть inserted retroactively into historical Decision Basis. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-92 | Historical knowledge НЕ ДОЛЖЕН незаметно inherit current Context. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-93 | Present-day categories НЕ ДОЛЖЕН автоматически быть projected backward into historical Context. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-94 | Current knowledge НЕ ДОЛЖЕН автоматически generalize into future system/version Context. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-95 | Cross-cultural, cross-jurisdiction, cross-version and cross-population переносить НЕ ДОЛЖЕН быть предполагаемым автоматически. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-96 | Laboratory Context НЕ ДОЛЖЕН автоматически становиться field Context. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-97 | Source production Context ДОЛЖЕН оставаться различимым from Context представленный by Source. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-98 | Context and Identity semantics ДОЛЖЕН оставаться compatible with `014`. | semantic | Context/Validator | **ENFORCED** |
| CTX-99 | Context and Relation semantics ДОЛЖЕН оставаться compatible with `013`. | semantic | Context/Validator | **ENFORCED** |
| CTX-100 | Context and Process semantics ДОЛЖЕН оставаться compatible with `012`. | semantic | Context/Validator | **ENFORCED** |
| CTX-101 | Context and State semantics ДОЛЖЕН оставаться compatible with `011`. | semantic | Context/Validator | **ENFORCED** |
| CTX-102 | Context and Result semantics ДОЛЖЕН оставаться compatible with `010`. | semantic | Context/Validator | **ENFORCED** |
| CTX-103 | Context and Event semantics ДОЛЖЕН оставаться compatible with `009`. | semantic | Context/Validator | **ENFORCED** |
| CTX-104 | Context and Action semantics ДОЛЖЕН оставаться compatible with `008`. | semantic | Context/Validator | **ENFORCED** |
| CTX-105 | Context Record identity ДОЛЖЕН оставаться различимым from представленный contextual situation. | semantic | Context/Validator | **ENFORCED** |
| CTX-106 | Context absence, неизвестный Context, unrecorded Context and irrelevance ДОЛЖЕН оставаться различимым. | semantic | Context/Validator | **ENFORCED** |
| CTX-107 | Context hierarchy/inheritance НЕ ДОЛЖЕН resolve conflicting values без определённый semantics. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-108 | Context normalization НЕ ДОЛЖЕН придумывать precision. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-109 | Unit conversion ДОЛЖЕН сохранять original uncertainty/precision. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-110 | Translation ДОЛЖЕН сохранять материально relevant Context qualifiers, uncertainty and epistemic status. | semantic | Context/Validator | **ENFORCED** |
| CTX-111 | Summary НЕ ДОЛЖЕН convert context-limited knowledge into universal knowledge. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-112 | Context compression ДОЛЖЕН сохранять материально relevant applicability and safety conditions. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-113 | Context loss, contamination, conflation, leakage, hallucination and overgeneralization ДОЛЖЕН оставаться detectable semantic failure classes. | semantic | Context/Validator | **ENFORCED** |
| CTX-114 | неизвестный Context ДОЛЖЕН быть preferred over plausible unsupported Context fabrication. | semantic | Context/Validator | **ENFORCED** |
| CTX-115 | Historical Context reconstruction ДОЛЖЕН distinguish известный, reported, inferred, reconstructed, предполагаемым, modeled and disputed semantics. | history/context | Context/Versioning/Validator | **ENFORCED** |
| CTX-116 | Damaged Sources НЕ ДОЛЖЕН быть completed with придуманный Context. | evidence/provenance | Context/Validator | **ENFORCED** |
| CTX-117 | Offline representation СЛЕДУЕТ сохранять enough Context for durable human interpretation. | semantic | Context/Validator | **ENFORCED** |
| CTX-118 | Carrier technology НЕ ДОЛЖЕН определять Context semantics. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-119 | Profile МОЖЕТ strengthen Context requirements Но НЕ ДОЛЖЕН weaken Core пока claiming compatibility. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-120 | Context structural conformance ДОЛЖЕН оставаться различимым from Context truth, completeness, applicability proof, transferability, causality and safety. | context-dependent | Context/Scope-aware Validator | **ENFORCED** |
| CTX-121 | High Context Fidelity НЕ ДОЛЖЕН быть interpreted as proof that сохранённый Context is factually true. | anti-inference | Context/Validator | **ENFORCED** |
| CTX-122 | материально relevant Context target, dimensions, values, epistemic status, temporal validity, provenance and uncertainty ДОЛЖЕН оставаться разрешимым. | evidence/provenance | Context/Validator | **ENFORCED** |

## 5.8. Rule-by-rule matrix — STANDARD/016 Scope

| ID | Нормативное правило | Класс | Owner | Статус |
|---|---|---|---|---|
| SCP-01 | Scope ДОЛЖЕН сохранять the domain subset, range, membership condition or configuration to which a representation relates in a определённый semantic role. | context-dependent | Scope/Context-aware Validator | **PARTIAL** |
| SCP-02 | Scope НЕ ДОЛЖЕН быть used as an undifferentiated bucket for every restriction. | anti-inference | Scope/Validator | **PARTIAL** |
| SCP-03 | Material Scope semantic role ДОЛЖЕН оставаться recoverable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-04 | Scope ДОЛЖЕН оставаться associated with its scoped target где ambiguity matters. | semantic | Scope/Validator | **ENFORCED** |
| SCP-05 | Container Scope НЕ ДОЛЖЕН автоматически становиться Scope of every contained component. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-06 | Scope МОЖЕТ qualify individual semantic roles/arguments and those qualifications ДОЛЖЕН оставаться различимым где material. | semantic | Scope/Validator | **ENFORCED** |
| SCP-07 | Joint Scope constraints НЕ ДОЛЖЕН быть flattened into independent constraints когда doing so creates unsupported combinations. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-08 | Scope СЛЕДУЕТ оставаться interpretable relative to a universe/domain где material. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-09 | неизвестный universe НЕ ДОЛЖЕН быть replaced by придуманный universe. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-10 | Scope ДОЛЖЕН оставаться различимым from Universe. | semantic | Scope/Validator | **ENFORCED** |
| SCP-11 | Local universe ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-12 | Local universe НЕ ДОЛЖЕН незаметно expand during transformation. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-13 | Nested universes and dependent quantifiers ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-14 | Scope ДОЛЖЕН оставаться различимым from Quantifier. | semantic | Scope/Validator | **ENFORCED** |
| SCP-15 | Material quantifiers ДОЛЖЕН оставаться сохранённым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-16 | Scope membership НЕ ДОЛЖЕН автоматически устанавливать member-level Claim truth. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-17 | Universal/distributive переносить ДОЛЖЕН occur только когда Claim semantics license it. | semantic | Scope/Validator | **ENFORCED** |
| SCP-18 | Scope containment НЕ ДОЛЖЕН itself license Claim instantiation or переносить. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-19 | Generic Claims НЕ ДОЛЖЕН автоматически становиться universal Claims. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-20 | Aggregate Claims НЕ ДОЛЖЕН автоматически становиться member-level Claims. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-21 | Member observations НЕ ДОЛЖЕН автоматически становиться population Claims. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-22 | Group-level Relations НЕ ДОЛЖЕН автоматически становиться individual-level Relations. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-23 | Individual-level Relations НЕ ДОЛЖЕН автоматически становиться population-level Relations. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-24 | Material level of analysis СЛЕДУЕТ оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-25 | Scope ДОЛЖЕН оставаться различимым from Context. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-26 | The same condition МОЖЕТ участвовать в Scope and Context roles без role схлопываться. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-27 | Scope and Context НЕ ДОЛЖЕН быть предполагаемым independent. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-28 | Coupled applicability constraints ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-29 | Scope ДОЛЖЕН оставаться различимым from Preconditions. | semantic | Scope/Validator | **ENFORCED** |
| SCP-30 | Scope membership НЕ ДОЛЖЕН означать satisfaction of Preconditions. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-31 | Conditional propositions НЕ ДОЛЖЕН автоматически становиться scoped unconditional propositions. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-32 | Scope ДОЛЖЕН оставаться различимым from State. | semantic | Scope/Validator | **ENFORCED** |
| SCP-33 | Scope ДОЛЖЕН оставаться различимым from Class. | semantic | Scope/Validator | **ENFORCED** |
| SCP-34 | Class membership НЕ ДОЛЖЕН автоматически устанавливать applicability. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-35 | Sample, eligibility, recruited, observed, analyzed, target-population and Claim Scope ДОЛЖЕН оставаться различимым где material. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-36 | Enrollment Scope НЕ ДОЛЖЕН автоматически становиться analysis Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-37 | Missing-data filtering НЕ ДОЛЖЕН незаметно сохранять broader Result Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-38 | Material selection mechanisms СЛЕДУЕТ оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-39 | Survivorship НЕ ДОЛЖЕН незаметно generalize to original population. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-40 | Material numerator, denominator and reference population СЛЕДУЕТ оставаться сохраняемым for quantitative Claims. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-41 | Scope ДОЛЖЕН оставаться различимым from Evidence. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-42 | Evidence Scope НЕ ДОЛЖЕН автоматически становиться Claim Scope. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-43 | Claim Scope НЕ ДОЛЖЕН автоматически становиться Evidence Scope. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-44 | Evidence-selection restrictions НЕ ДОЛЖЕН автоматически становиться phenomenon applicability restrictions. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-45 | Evidence поддерживать ДОЛЖЕН оставаться aligned to the Scope actually supported. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-46 | Scope ДОЛЖЕН оставаться различимым from Provenance. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-47 | Scope provenance МОЖЕТ exist at whole-Scope and component level. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-48 | Membership provenance ДОЛЖЕН оставаться сохраняемым где material. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-49 | Exception provenance НЕ ДОЛЖЕН быть незаметно reassigned. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-50 | Scope composition НЕ ДОЛЖЕН launder partial Source поддерживать into whole-Scope Source поддерживать. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-51 | Declared Scope НЕ ДОЛЖЕН быть treated as applicability proof. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-52 | Recorded Scope НЕ ДОЛЖЕН автоматически быть treated as true/полный applicability. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-53 | Scope epistemic status ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-54 | Stated Scope ДОЛЖЕН оставаться различимым from demonstrated Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-55 | Intended Scope ДОЛЖЕН оставаться различимым from realized Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-56 | Designed, tested, validated, observed, permitted and actual-использовать Scope ДОЛЖЕН оставаться различимым где material. | semantic | Scope/Validator | **ENFORCED** |
| SCP-57 | Regulatory Scope ДОЛЖЕН оставаться различимым from scientific Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-58 | Safety Scope ДОЛЖЕН оставаться различимым from efficacy Scope. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-59 | Normative Scope ДОЛЖЕН оставаться различимым from empirical Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-60 | Scope exclusion НЕ ДОЛЖЕН автоматически означать a particular reason, harm or falsity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-61 | Core НЕ ДОЛЖЕН impose one universal fixed Scope dimension list. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-62 | Shared Scope safeguards НЕ ДОЛЖЕН требовать all Scope-like roles to belong to one ontological type. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-63 | Multidimensional Scope НЕ ДОЛЖЕН быть treated as Cartesian product автоматически. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-64 | Dependent/correlated dimensions ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-65 | допустимый component values НЕ ДОЛЖЕН автоматически означать validity of every combination. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-66 | Tuple/configuration integrity ДОЛЖЕН survive decomposition, storage and reconstruction. | semantic | Scope/Validator | **ENFORCED** |
| SCP-67 | Validated points НЕ ДОЛЖЕН автоматически generate a bounding-box validity region. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-68 | Validated points НЕ ДОЛЖЕН автоматически generate a convex/continuous validity region. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-69 | допустимый endpoints НЕ ДОЛЖЕН автоматически означать допустимый interval. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-70 | Non-contiguous Scope ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-71 | Scope holes/exceptions ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-72 | Boolean Scope structure and grouping ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-73 | Nested quantification НЕ ДОЛЖЕН быть flattened когда order/dependency matters. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-74 | Material inclusion criteria ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-75 | Material exclusion criteria ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-76 | Inclusion НЕ ДОЛЖЕН автоматически override exclusions. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-77 | Exclusion from Scope НЕ ДОЛЖЕН автоматически означать Claim falsity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-78 | Outside Scope НЕ ДОЛЖЕН автоматически означать truth or falsity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-79 | неизвестный Scope НЕ ДОЛЖЕН быть treated as universal Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-80 | неизвестный Scope НЕ ДОЛЖЕН быть treated as empty Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-81 | Missing Scope НЕ ДОЛЖЕН означать universal or empty applicability. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-82 | Open Scope ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-83 | Closed Scope requires defined closure semantics. | semantic | Scope/Validator | **ENFORCED** |
| SCP-84 | Under open-world semantics, absence of известный membership НЕ ДОЛЖЕН означать non-membership. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-85 | известный members НЕ ДОЛЖЕН автоматически быть treated as полный extension. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-86 | Closed-world reasoning requires justified closure. | semantic | Scope/Validator | **ENFORCED** |
| SCP-87 | Closure ДОЛЖЕН оставаться local to the target/dimension/domain for which it is установленный. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-88 | Closure НЕ ДОЛЖЕН leak across dimensions. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-89 | "All известный" ДОЛЖЕН оставаться различимым from "all existing." | semantic | Scope/Validator | **ENFORCED** |
| SCP-90 | Logically empty Scope ДОЛЖЕН оставаться различимым from неизвестный/no-известный-member Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-91 | Vacuous logical truth НЕ ДОЛЖЕН автоматически становиться empirical/practical validity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-92 | Singleton Scope НЕ ДОЛЖЕН схлопываться into Entity identity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-93 | Finite, continuous, discontinuous, bounded, unbounded and partially известный Scope ДОЛЖЕН оставаться representable где required. | structural/semantic | Schema + L4 | **ENFORCED** |
| SCP-94 | Intensional Scope ДОЛЖЕН оставаться различимым from extensional membership representation. | semantic | Scope/Validator | **ENFORCED** |
| SCP-95 | Extensional equality at one time НЕ ДОЛЖЕН автоматически устанавливать persistent semantic equivalence. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-96 | Dynamic Scope СЛЕДУЕТ сохранять temporal validity. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-97 | Scope definition dependencies СЛЕДУЕТ оставаться разрешимым где material. | semantic | Scope/Validator | **ENFORCED** |
| SCP-98 | Uncertain, disputed or unresolved dependency status НЕ ДОЛЖЕН незаметно становиться certain Scope membership. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-99 | Identity-dependent membership МОЖЕТ оставаться unresolved когда Identity is unresolved. | semantic | Scope/Validator | **ENFORCED** |
| SCP-100 | Relation-dependent membership МОЖЕТ оставаться disputed когда Relation is disputed. | semantic | Scope/Validator | **ENFORCED** |
| SCP-101 | State-dependent Scope ДОЛЖЕН сохранять relevant temporal semantics. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-102 | Event-dependent Scope ДОЛЖЕН сохранять relevant Event/Relation dependencies. | semantic | Scope/Validator | **ENFORCED** |
| SCP-103 | Measurement-dependent membership ДОЛЖЕН сохранять material Measurement uncertainty. | semantic | Scope/Validator | **ENFORCED** |
| SCP-104 | Vague labels НЕ ДОЛЖЕН быть converted into exact operational boundaries без basis. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-105 | Same Scope label НЕ ДОЛЖЕН автоматически означать same Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-106 | Relevant classification/taxonomy/definition frame СЛЕДУЕТ оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-107 | Vague/fuzzy Scope НЕ ДОЛЖЕН автоматически становиться crisp Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-108 | Approximate boundaries НЕ ДОЛЖЕН становиться exact boundaries. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-109 | Inclusive/exclusive boundary operators ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-110 | Boundary uncertainty ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-111 | Membership uncertainty ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-112 | Component-level Scope uncertainty ДОЛЖЕН оставаться representable где material. | semantic | Scope/Validator | **ENFORCED** |
| SCP-113 | Spatial Scope ДОЛЖЕН оставаться различимым from spatial Context. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-114 | Historical spatial Scope НЕ ДОЛЖЕН незаметно использовать modern boundaries. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-115 | Boundary migration ДОЛЖЕН сохранять relevant time/frame semantics. | semantic | Scope/Validator | **ENFORCED** |
| SCP-116 | Disputed geographic membership ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-117 | Jurisdictional Scope НЕ ДОЛЖЕН незаметно переносить across jurisdictions. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-118 | Jurisdiction containment НЕ ДОЛЖЕН автоматически определять normative precedence. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-119 | Temporal applicability ДОЛЖЕН оставаться различимым from other temporal roles. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-120 | Enactment time НЕ ДОЛЖЕН автоматически становиться applicability time. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-121 | Discontinuous temporal Scope ДОЛЖЕН оставаться representable. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-122 | Historical Scope ДОЛЖЕН сохранять relevant historical definitions/frames. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-123 | Category drift НЕ ДОЛЖЕН незаметно redefine historical Scope. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-124 | Population Scope НЕ ДОЛЖЕН незаметно generalize. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-125 | Version-family membership НЕ ДОЛЖЕН устанавливать behavioral equivalence. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-126 | Validity at separated versions НЕ ДОЛЖЕН автоматически означать validity at intermediate versions. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-127 | Material similarity НЕ ДОЛЖЕН устанавливать applicability equivalence. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-128 | Parameter Scope НЕ ДОЛЖЕН быть extrapolated без justification. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-129 | Domain of definition ДОЛЖЕН оставаться различимым from Claim Scope. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-130 | Model input acceptance НЕ ДОЛЖЕН устанавливать validation Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-131 | Display, operational, calibrated and validated Measurement ranges ДОЛЖЕН оставаться различимым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-132 | Interpretive Scope ДОЛЖЕН оставаться различимым from applicability Scope где material. | semantic | Scope/Validator | **ENFORCED** |
| SCP-133 | Semantic/definition frame СЛЕДУЕТ оставаться recoverable где necessary for Scope interpretation. | semantic | Scope/Validator | **ENFORCED** |
| SCP-134 | Hypothetical Scope ДОЛЖЕН оставаться различимым from actual Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-135 | Future Scope НЕ ДОЛЖЕН означать demonstrated future validity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-136 | Scope intersection НЕ ДОЛЖЕН автоматически license Claim composition. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-137 | Scope union requires compatible Claim semantics and aligned relevant constraints. | semantic | Scope/Validator | **ENFORCED** |
| SCP-138 | Cross-source Scope constraints НЕ ДОЛЖЕН автоматически быть composed into one asserted Scope. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-139 | Temporal/dimensional coupling ДОЛЖЕН survive Scope composition. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-140 | Lossy Scope projection ДОЛЖЕН оставаться detectable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-141 | Projection of multidimensional Scope НЕ ДОЛЖЕН permit later reconstruction as though lost dependencies were сохранённый. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-142 | Lossy Scope projection СЛЕДУЕТ сохранять derivation provenance где material. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-143 | Decomposition/recomposition НЕ ДОЛЖЕН fabricate Scope members/configurations. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-144 | Scope containment НЕ ДОЛЖЕН автоматически определять validity переносить. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-145 | Narrow-to-broad transfer requires justification. | semantic | Scope/Validator | **ENFORCED** |
| SCP-146 | Broad-to-narrow transfer requires compatible Claim semantics. | semantic | Scope/Validator | **ENFORCED** |
| SCP-147 | Scope overlap НЕ ДОЛЖЕН быть treated as equivalence. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-148 | Scope equivalence ДОЛЖЕН оставаться различимым from Record, provenance, role and temporal identity. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-149 | Scope similarity НЕ ДОЛЖЕН устанавливать transferability. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-150 | Scope compatibility НЕ ДОЛЖЕН устанавливать equivalence or applicability. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-151 | Scope mapping НЕ ДОЛЖЕН автоматически устанавливать equivalence. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-152 | Lossy mapping НЕ ДОЛЖЕН быть used as exact set mapping. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-153 | Scope mismatch ДОЛЖЕН оставаться detectable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-154 | Scope alignment СЛЕДУЕТ precede contradiction judgment где material. | semantic | Scope/Validator | **ENFORCED** |
| SCP-155 | Different Scope НЕ ДОЛЖЕН автоматически быть labeled contradiction. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-156 | Claim falsity, inapplicability, non-assertion and неизвестный applicability ДОЛЖЕН оставаться различимым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-157 | Negation/quantifier order ДОЛЖЕН оставаться сохранённым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-158 | Structural nesting НЕ ДОЛЖЕН автоматически устанавливать Scope inheritance. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-159 | Explicit, inherited, inferred and reconstructed Scope ДОЛЖЕН оставаться различимым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-160 | Scope МОЖЕТ inherit dimension-by-dimension только где semantics justify it. | semantic | Scope/Validator | **ENFORCED** |
| SCP-161 | неизвестный/incompatible inheritance НЕ ДОЛЖЕН быть treated as допустимый inheritance. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-162 | Material heading/table/figure/footnote Scope ДОЛЖЕН оставаться сохраняемым. | semantic | Scope/Validator | **ENFORCED** |
| SCP-163 | Evidence citation Scope НЕ ДОЛЖЕН автоматически constrain or broaden author Claim Scope. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-164 | Reported Scope ДОЛЖЕН оставаться различимым from endorsed/supporting Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-165 | Material inherited Scope ДОЛЖЕН travel with extracted knowledge or оставаться resolvably referenced. | semantic | Scope/Validator | **ENFORCED** |
| SCP-166 | Canonicalization НЕ ДОЛЖЕН remove material Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-167 | Deduplication НЕ ДОЛЖЕН автоматически union Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-168 | Identical Claim text НЕ ДОЛЖЕН означать identical scoped Claim semantics. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-169 | Scope МОЖЕТ участвовать в Claim/Record identity criteria consistently with `014`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-170 | Evidence поддерживать МОЖЕТ быть Scope-conditioned. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-171 | Uncertainty МОЖЕТ быть Scope-conditioned. | semantic | Scope/Validator | **ENFORCED** |
| SCP-172 | Risk МОЖЕТ быть Scope-conditioned. | semantic | Scope/Validator | **ENFORCED** |
| SCP-173 | Verification МОЖЕТ быть Scope-conditioned. | semantic | Scope/Validator | **ENFORCED** |
| SCP-174 | Conflict МОЖЕТ быть Scope-conditioned. | semantic | Scope/Validator | **ENFORCED** |
| SCP-175 | Scope partitioning ДОЛЖЕН оставаться representable без mandatory Core Entity proliferation. | semantic | Scope/Validator | **ENFORCED** |
| SCP-176 | Derived Claim Scope НЕ ДОЛЖЕН exceed what premises/inference justify. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-177 | Multi-premise inference ДОЛЖЕН оставаться within justified joint domain. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-178 | Non-overlapping required premise Scopes НЕ ДОЛЖЕН receive fabricated common Scope. | structural/semantic | Schema + L4 | **ENFORCED** |
| SCP-179 | Inference-specific Scope transformation ДОЛЖЕН быть explicit/justifiable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-180 | Derived Scope provenance ДОЛЖЕН оставаться различимым from Source-stated Scope. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-181 | Extrapolation beyond supported Scope ДОЛЖЕН оставаться identifiable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-182 | Interpolation НЕ ДОЛЖЕН автоматически устанавливать validity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-183 | Safety-critical interpolation НЕ ДОЛЖЕН быть предполагаемым без поддерживать. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-184 | Cross-Scope invariance НЕ ДОЛЖЕН означать universal invariance. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-185 | Scope transferability МОЖЕТ оставаться conditional, partial, uncertain or неизвестный. | semantic | Scope/Validator | **ENFORCED** |
| SCP-186 | Scope переносить ДОЛЖЕН оставаться различимым from Context переносить. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-187 | Taxonomy, similarity, containment, mapping, inheritance or Evidence selection НЕ ДОЛЖЕН быть laundered into broad applicability. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-188 | Subset validity НЕ ДОЛЖЕН автоматически становиться superset validity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-189 | Regional validity НЕ ДОЛЖЕН автоматически становиться superregional validity. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-190 | Temporal validity НЕ ДОЛЖЕН автоматически expand to containing era. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-191 | Version validity НЕ ДОЛЖЕН автоматически expand to version family. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-192 | Subpopulation validity НЕ ДОЛЖЕН автоматически expand to broader population. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-193 | Sample Result НЕ ДОЛЖЕН автоматически становиться population Claim. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-194 | Scope semantic role НЕ ДОЛЖЕН незаметно change during transformation. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-195 | Limited Evidence НЕ ДОЛЖЕН create unsupported exclusivity. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-196 | Finite Evidence НЕ ДОЛЖЕН create unsupported universal quantification. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-197 | Existential поддерживать НЕ ДОЛЖЕН становиться universal поддерживать. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-198 | No Evidence for Scope X НЕ ДОЛЖЕН устанавливать non-applicability to X. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-199 | Natural-language Scope ambiguity ДОЛЖЕН оставаться representable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-200 | Ambiguous modifier/coordination attachment НЕ ДОЛЖЕН быть незаметно resolved когда material. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-201 | Implicit Scope ДОЛЖЕН оставаться различимым from explicit Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-202 | Domain defaults НЕ ДОЛЖЕН быть представлен как Source-stated Scope. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-203 | Normalization НЕ ДОЛЖЕН придумывать universe, boundary, quantifier, exclusivity, precision or semantic role. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-204 | Normalization ДОЛЖЕН сохранять correlated Scope dimensions. | semantic | Scope/Validator | **ENFORCED** |
| SCP-205 | Historical categories НЕ ДОЛЖЕН незаметно normalize into modern exact equivalents. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-206 | Translation ДОЛЖЕН сохранять материально relevant Scope semantics. | semantic | Scope/Validator | **ENFORCED** |
| SCP-207 | Scope Fidelity ДОЛЖЕН оставаться различимым from Scope truth. | semantic | Scope/Validator | **ENFORCED** |
| SCP-208 | Scope Fidelity ДОЛЖЕН оставаться различимым from overall Claim Fidelity. | semantic | Scope/Validator | **ENFORCED** |
| SCP-209 | Scope loss, contamination, conflation, hallucination, overgeneralization, overspecification and drift ДОЛЖЕН оставаться detectable failure classes. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-210 | неизвестный Scope ДОЛЖЕН быть preferred over unsupported Scope fabrication. | semantic | Scope/Validator | **ENFORCED** |
| SCP-211 | Scope role drift ДОЛЖЕН оставаться detectable even когда extension does not change. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-212 | Tuple/configuration drift ДОЛЖЕН оставаться detectable. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-213 | Open-world Scope НЕ ДОЛЖЕН незаметно становиться closed-world Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-214 | Scope definition/frame drift ДОЛЖЕН оставаться detectable. | history/scope | Scope/Versioning/Validator | **ENFORCED** |
| SCP-215 | Summary НЕ ДОЛЖЕН broaden, narrow or role-shift Scope без justification. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-216 | Compression ДОЛЖЕН сохранять material universe, role, boundaries, tuples, coupling, uncertainty and provenance. | evidence/provenance | Scope/Validator | **ENFORCED** |
| SCP-217 | Safety statements ДОЛЖЕН сохранять material Scope. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-218 | Independent parameter ranges НЕ ДОЛЖЕН автоматически определять a safe multidimensional region. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-219 | Uncertain safety boundaries НЕ ДОЛЖЕН становиться exact safe thresholds. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-220 | Risk Scope НЕ ДОЛЖЕН незаметно generalize. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-221 | Procedure Scope ДОЛЖЕН оставаться recoverable. | semantic | Scope/Validator | **ENFORCED** |
| SCP-222 | Decision-rule Scope НЕ ДОЛЖЕН незаметно expand. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-223 | Model validity Scope ДОЛЖЕН оставаться различимым from accepted input domain. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-224 | Action Scope ДОЛЖЕН оставаться compatible with `008`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-225 | Event Scope ДОЛЖЕН оставаться compatible with `009`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-226 | Result Scope ДОЛЖЕН оставаться compatible with `010`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-227 | State Scope ДОЛЖЕН оставаться compatible with `011`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-228 | Process Scope ДОЛЖЕН оставаться compatible with `012`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-229 | Relation Scope ДОЛЖЕН оставаться compatible with `013`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-230 | Identity Scope ДОЛЖЕН оставаться compatible with `014`. | semantic | Scope/Validator | **ENFORCED** |
| SCP-231 | Scope/Context coupling ДОЛЖЕН оставаться compatible with `015`. | context-dependent | Scope/Context-aware Validator | **ENFORCED** |
| SCP-232 | Meta-Scope ДОЛЖЕН оставаться различимым from Scope of the meta-Claim. | semantic | Scope/Validator | **ENFORCED** |
| SCP-233 | Partial verification НЕ ДОЛЖЕН становиться global verification. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-234 | Authority/competence Scope ДОЛЖЕН оставаться различимым from Claim applicability Scope. | semantic | Scope/Validator | **ENFORCED** |
| SCP-235 | Retrieval/filter Scope НЕ ДОЛЖЕН становиться Claim semantic Scope. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-236 | Presentation Scope НЕ ДОЛЖЕН становиться Claim applicability Scope автоматически. | anti-inference | Scope/Validator | **ENFORCED** |
| SCP-237 | Access-control Scope ДОЛЖЕН оставаться различимым from knowledge applicability Scope. | semantic | Scope/Validator | **ENFORCED** |

## 5.9. Rule-by-rule matrix — STANDARD/017 Provenance

| ID | Нормативное правило | Класс | Owner | Статус |
|---|---|---|---|---|
| PRV-001 | represented provenance ≠ actual lineage automatically | semantic | Provenance/Validator | **PARTIAL** |
| PRV-002 | operational provenance ≠ represented historical provenance | history/provenance | Provenance/Versioning/Validator | **PARTIAL** |
| PRV-003 | Provenance Claim remains epistemically assessable | semantic | Provenance/Validator | **ENFORCED** |
| PRV-004 | record provenance ≠ provenance of every component automatically | context-dependent | Provenance/Context-aware Validator | **ENFORCED** |
| PRV-005 | provenance dimensions НЕ ДОЛЖЕН быть незаметно collapsed | anti-inference | Provenance/Validator | **ENFORCED** |
| PRV-006 | generic ancestry ≠ specific operation | semantic | Provenance/Validator | **ENFORCED** |
| PRV-007 | indirect ancestry ≠ direct provenance | semantic | Provenance/Validator | **ENFORCED** |
| PRV-008 | multi-input operation ≠ independent pairwise edges automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-009 | joint input semantics ДОЛЖЕН оставаться сохраняемым где material | semantic | Provenance/Validator | **ENFORCED** |
| PRV-010 | intended transformation ≠ actual transformation | semantic | Provenance/Validator | **ENFORCED** |
| PRV-011 | operation execution ≠ operation success | semantic | Provenance/Validator | **ENFORCED** |
| PRV-012 | textual change magnitude ≠ semantic change magnitude | semantic | Provenance/Validator | **ENFORCED** |
| PRV-013 | complete provenance ≠ reproducibility | semantic | Provenance/Validator | **ENFORCED** |
| PRV-014 | reproducibility ≠ complete provenance | semantic | Provenance/Validator | **ENFORCED** |
| PRV-015 | uploader / operator / scanner ≠ content author automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-016 | citation ≠ provenance proof | semantic | Provenance/Validator | **ENFORCED** |
| PRV-017 | bibliography ≠ ancestry | semantic | Provenance/Validator | **ENFORCED** |
| PRV-018 | influence ≠ derivation automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-019 | same observed Event ≠ common provenance | semantic | Provenance/Validator | **ENFORCED** |
| PRV-020 | same tool/method ≠ common content provenance automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-021 | Provenance graph ≠ Evidence dependency graph | semantic | Provenance/Validator | **ENFORCED** |
| PRV-022 | provenance independence ≠ evidential independence | semantic | Provenance/Validator | **ENFORCED** |
| PRV-023 | no known common provenance ≠ independent Evidence | semantic | Provenance/Validator | **ENFORCED** |
| PRV-024 | common provenance ≠ complete evidential dependence | semantic | Provenance/Validator | **ENFORCED** |
| PRV-025 | physical provenance ≠ content provenance | semantic | Provenance/Validator | **ENFORCED** |
| PRV-026 | world causality ≠ provenance ancestry automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-027 | location identifier ≠ immutable content identity | semantic | Provenance/Validator | **ENFORCED** |
| PRV-028 | version order ≠ derivation order automatically | history/provenance | Provenance/Versioning/Validator | **ENFORCED** |
| PRV-029 | earliest known ≠ origin | semantic | Provenance/Validator | **ENFORCED** |
| PRV-030 | graph root ≠ actual origin | semantic | Provenance/Validator | **ENFORCED** |
| PRV-031 | неизвестный provenance ДОЛЖЕН оставаться representable | semantic | Provenance/Validator | **ENFORCED** |
| PRV-032 | unknown ≠ unrecorded ≠ restricted ≠ redacted ≠ lost | fidelity/unknown | Provenance/Transformation | **ENFORCED** |
| PRV-033 | actual lineage ≠ knowledge about lineage at time T | semantic | Provenance/Validator | **ENFORCED** |
| PRV-034 | новые сведения о происхождении НЕ ДОЛЖНЫ переписывать историческое эпистемическое состояние | anti-inference | Provenance/Validator | **ENFORCED** |
| PRV-035 | imported provenance ≠ internally established provenance automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-036 | отображение происхождения с потерями ДОЛЖНО оставаться обнаружимым | semantic | Provenance/Validator | **ENFORCED** |
| PRV-037 | different provenance granularity ≠ conflict automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-038 | provenance conflict requires semantic alignment | semantic | Provenance/Validator | **ENFORCED** |
| PRV-039 | missing provenance edge ≠ negative provenance claim | semantic | Provenance/Validator | **ENFORCED** |
| PRV-040 | provenance completeness requires explicit closure Scope | context-dependent | Provenance/Context-aware Validator | **ENFORCED** |
| PRV-041 | derivation cycle ≠ every reference cycle | semantic | Provenance/Validator | **ENFORCED** |
| PRV-042 | acyclic provenance ≠ valid justification automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-043 | shared provenance ≠ same Identity | semantic | Provenance/Validator | **ENFORCED** |
| PRV-044 | same content ≠ same Provenance | semantic | Provenance/Validator | **TESTED** |
| PRV-045 | known provenance ≠ authenticity automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-046 | known provenance ≠ reliability automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-047 | provenance quality ≠ truth | semantic | Provenance/Validator | **ENFORCED** |
| PRV-048 | неоднозначность естественного языка НЕ ДОЛЖНА превращаться в выдуманную определённость происхождения | anti-inference | Provenance/Validator | **ENFORCED** |
| PRV-049 | training inclusion ≠ specific AI output derivation | semantic | Provenance/Validator | **ENFORCED** |
| PRV-050 | projected provenance ≠ complete provenance automatically | semantic | Provenance/Validator | **ENFORCED** |
| PRV-051 | component binding ≠ Scope qualification automatically | context-dependent | Provenance/Context-aware Validator | **ENFORCED** |
| PRV-052 | authorship/contribution provenance ≠ complete authorship semantics | semantic | Provenance/Validator | **TESTED** |
| PRV-053 | operational provenance НЕ ДОЛЖЕН требовать artificial epistemic status где no material epistemic distinction exists | anti-inference | Provenance/Validator | **ENFORCED** |

## 5.10. Rule-by-rule matrix — STANDARD/018 Authorship & Contribution

В `018` нормативные правила не имеют отдельных `AC-*` идентификаторов. Для аудита каждому нормативному разделу присвоен стабильный audit-ID `AC-001…AC-123`. Это идентификаторы аудита, а не новые нормативные идентификаторы Standard.

`PARTIAL` означает, что текущая Schema уже содержит часть необходимой структуры, но не всю семантику. `DEFERRED` требует профильного, исторического или transformation enforcement.

| Audit ID | Нормативный блок | Класс | Owner | Статус |
|---|---|---|---|---|
| AC-001 | §1 Назначение | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-002 | §2 Основной принцип | domain/legal | Domain Profile | **ENFORCED** |
| AC-003 | §3 Фундаментальная модель | transformation/fidelity | Publication/Recovery | **ENFORCED** |
| AC-004 | §4 Участие | AI/profile | Authorship/Profile/Validator | **PARTIAL** |
| AC-005 | §5 Вклад | normative/anti-inference | Authorship/Profile Validator | **PARTIAL** |
| AC-006 | §6 Вклад не требует видимого изменения | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-007 | §7 Вклад в содержание и вклад в процесс | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-008 | §8 Цель Вклада | AI/profile | Authorship/Profile/Validator | **PARTIAL** |
| AC-009 | §9 Аспект Вклада | AI/profile | Authorship/Profile/Validator | **PARTIAL** |
| AC-010 | §10 Роль не определяет Вклад | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-011 | §11 Множественные роли | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-012 | §12 Авторство | profile-dependent | Authorship Profile/Validator | **PARTIAL** |
| AC-013 | §13 Авторство относительно Цели | AI/profile | Authorship/Profile/Validator | **PARTIAL** |
| AC-014 | §14 Аспект Авторства | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-015 | §15 Создание представления и смысловое Авторство | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-016 | §16 Писцы и диктовка | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-017 | §17 Авторство представлений, а не реальности | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-018 | §18 Профиль Авторства | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-019 | §19 Авторство относительно Профиля | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-020 | §20 Совместимость Профиля | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-021 | §21 Происхождение критериев Авторства | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-022 | §22 История Вклада и история классификации Авторства | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-023 | §23 Авторство как Утверждение или Оценка | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-024 | §24 Непосредственно наблюдаемая системная активность | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-025 | §25 Идентичность аккаунта и действующего лица | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-026 | §26 Коллективное Авторство | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-027 | §27 Совместное Авторство | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-028 | §28 Коллективная идентичность | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-029 | §29 Родительская организация | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-030 | §30 Атрибуция сообществу | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-031 | §31 Культурная и традиционная атрибуция | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-032 | §32 Хранительство и передача | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-033 | §33 Авторство неприменимо | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-034 | §34 Анонимный Вклад | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-035 | §35 Псевдонимное Авторство | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-036 | §36 Указание заслуг | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-037 | §37 Заявленное и оценённое равенство Вклада | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-038 | §38 Величина Вклада | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-039 | §39 Значимость и величина | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-040 | §40 Редакторский Вклад | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-041 | §41 Удаление и предотвращение | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-042 | §42 Перевод | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-043 | §43 Интерпретационный перевод | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-044 | §44 Слои перевода | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-045 | §45 Перевод и редактирование | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-046 | §46 Компиляция и компоновка | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-047 | §47 Синтез | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-048 | §48 Рецензирование | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-049 | §49 Верификация | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-050 | §50 Ответственность и подотчётность | domain/legal | Domain Profile | **ENFORCED** |
| AC-051 | §51 Экспертность | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-052 | §52 Почётное Авторство | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-053 | §53 Скрытое Авторство | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-054 | §54 Формальный Автор и смысловой участник | domain/legal | Domain Profile | **ENFORCED** |
| AC-055 | §55 Юридическое Авторство | domain/legal | Domain Profile | **ENFORCED** |
| AC-056 | §56 Вклад человека и ИИ | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-057 | §57 Участие ИИ не определяет Авторство | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-058 | §58 Нет универсального порога человек–ИИ | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-059 | §59 Запрос человека к ИИ | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-060 | §60 Выбор человеком результата ИИ | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-061 | §61 Промежуточное влияние ИИ | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-062 | §62 Обучающие данные и Вклад в результат | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-063 | §63 Разработчик и поставщик ИИ | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-064 | §64 Идентичность ИИ | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-065 | §65 Вклад в программное обеспечение | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-066 | §66 Импортированное или скопированное содержание | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-067 | §67 Историческое Авторство | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-068 | §68 Традиционная атрибуция | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-069 | §69 Составные Работы | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-070 | §70 Редактура исторического текста | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-071 | §71 Устная традиция | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-072 | §72 Информанты | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-073 | §73 Первый известный Автор | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-074 | §74 Вклад между версиями | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-075 | §75 Сохранившийся Вклад | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-076 | §76 Откат и повторное введение | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-077 | §77 Состояние Вклада | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-078 | §78 Спорный Вклад | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-079 | §79 Неизвестный Вклад | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-080 | §80 Замкнутость списка Вкладов | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-081 | §81 Вклад на уровне Компонента | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-082 | §82 Смысловые Компоненты | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-083 | §83 Перекрывающийся Вклад | domain/legal | Domain Profile | **ENFORCED** |
| AC-084 | §84 Гранулярность | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-085 | §85 Совместный Вклад | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-086 | §86 Структура отношения Вклада | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-087 | §87 Действие и классификация Вклада | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-088 | §88 Вывод и вычисление | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-089 | §89 Вклад в данные и Наборы данных | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-090 | §90 Автор Источника и вложенная атрибуция | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-091 | §91 Цитирование | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-092 | §92 Перевод цитат | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-093 | §93 Атрибуция пересказа ИИ | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-094 | §94 Отрицание Авторства | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-095 | §95 Полнота | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-096 | §96 Порядок Авторов | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-097 | §97 Ответственный или контактный Автор | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-098 | §98 Авторство консорциума | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-099 | §99 Права и владение | domain/legal | Domain Profile | **ENFORCED** |
| AC-100 | §100 Приватность и ограниченная идентичность | transformation/fidelity | Publication/Recovery | **ENFORCED** |
| AC-101 | §101 Существенность | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-102 | §102 Существенность относительно назначения | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-103 | §103 Доказательства Авторства и Вклада | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-104 | §104 Эпистемическая уверенность | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-105 | §105 Конфликтующие модели Авторства | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-106 | §106 Правила валидации | domain/legal | Domain Profile | **ENFORCED** |
| AC-107 | §107 Валидация Авторства на основе Профиля | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-108 | §108 Офлайн-сохранение | transformation/fidelity | Publication/Recovery | **ENFORCED** |
| AC-109 | §109 Точность отображения | history/attribution | Authorship/History/Validator | **ENFORCED** |
| AC-110 | §110 Принцип открытого мира | normative/anti-inference | Authorship/Profile Validator | **ENFORCED** |
| AC-111 | §111 Минимальное представление Вклада | structural/semantic | Schema + L4 | **ENFORCED** |
| AC-112 | §112 Минимальное представление Авторства | structural/semantic | Schema + L4 | **ENFORCED** |
| AC-113 | §113 Не-цели | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-114 | §114 Дисциплина Сущностей | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-115 | §115 Интероперабельность | semantic | Authorship/Profile Validator | **ENFORCED** |
| AC-116 | §116 Канонические инварианты | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-117 | §117 Канонический шаблон Вклада | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-118 | §118 Канонический шаблон Авторства | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-119 | §119 Канонический исторический пример | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-120 | §120 Канонический пример с ИИ | profile-dependent | Authorship Profile/Validator | **ENFORCED** |
| AC-121 | §121 Канонический пример исторической атрибуции | AI/profile | Authorship/Profile/Validator | **ENFORCED** |
| AC-122 | §122 Итоговый принцип | transformation/fidelity | Publication/Recovery | **ENFORCED** |
| AC-123 | §123 Архитектурное правило | history/attribution | Authorship/History/Validator | **ENFORCED** |
## 5.10.1. Завершение рабочего прохода STANDARD/014 Identity

Для 014 проведён полный проход всех 131 правил ID-01…ID-131.

В Reference Implementation закрыты следующие машинно проверяемые инварианты:

- ID-01: для Identity с явным статусом разрешения/неопределённости применимая frame должна быть явно представима и проверяема через frame_ref, valid_time, context или scope.
- ID-03: identity criterion является обязательной частью Identity Profile.
- ID-40: неизвестная Identity имеет отдельное структурное состояние identity_status=unknown и не смешивается с resolved_same/resolved_distinct.
- ID-44: конкурирующие кандидаты явно представимы через candidate_refs; Validator требует их для possible_same, probable_same и ambiguous.

Дополнительно расширен Identity Profile полями frame_ref, identity_status, candidate_refs, resolution_ref и uncertainty; Resolver проверяет их versioned references.

Остальные правила 014 не переводились в ENFORCED автоматически: большая часть требует графового identity resolution, исторического анализа, domain/profile semantics или transformation enforcement, которых Reference Implementation пока не реализует как отдельный механизм.

## 5.11. Полный rule inventory 011–018

Инвентаризация нормативных правил завершена по всем восьми стандартам. Audit IDs не изменяют нормативные документы; они используются только для трассировки enforcement.

| Standard | Количество audit-правил |
|---|---:|
| 011 State | 63 |
| 012 Process | 89 |
| 013 Relation | 115 |
| 014 Identity | 131 |
| 015 Context | 122 |
| 016 Scope | 237 |
| 017 Provenance | 53 |
| 018 Authorship & Contribution | 123 audit-блоков |
| **Итого** | **933** |

Текущее распределение статусов матрицы:

- **ENFORCED:** 14
- **PARTIAL:** 16
- **TESTED:** 1
- **MAPPED:** 61
- **DEFERRED:** 841

`DEFERRED` здесь означает не «правило забыто» и не «правило отменено». Для него уже определён нормативный смысл и предполагаемый owner-layer, но ещё не завершено отдельное machine/integration enforcement. Это и есть следующий рабочий фронт.

Важно: 018 не имеет встроенных стабильных rule IDs уровня S/P/RL/ID/CTX/SCP; поэтому для него используются `AC-001…AC-123` как audit IDs разделов. Новых нормативных идентификаторов в Standard не вводилось.

Следующая стадия: не расширять архитектуру, а брать `DEFERRED` пакетами по owner-layer и переводить их в `ENFORCED`, `TESTED` или `MAPPED`, только если это подтверждено конкретным тестом/механизмом. Если правило действительно требует внешнего доменного контекста, оно остаётся `DEFERRED` с явным условием применимости.

---

## 12.1. Общий стресс-тест 000–021 — 29 сентября 2026

После добавления IMPLEMENTATION/015–019 проведён повторный сквозной стресс-тест архитектурного комплекта.

### Проверки

| Проверка | Результат |
|---|---|
| Последовательность IMPLEMENTATION 000–021 | PASS |
| Отсутствие старого 015 Operations / 016 Conformance | PASS |
| Каноническая нумерация 015–019 | PASS |
| Schema JSON parse | PASS |
| 19 зарегистрированных типов | PASS |
| 19 реализованных Content Contracts/Profiles | PASS |
| Context structural boundary | PASS |
| Scope structural boundary | PASS |
| Provenance structural boundary | PASS |
| Authorship/Contribution structural boundary | PASS |
| Trust/Reputation structural boundary | PASS |
| Anti-inference invariants 015–019 | PASS |
| History/Unknown discipline | PASS |
| Transformation/Fidelity boundaries | PASS / LIMITED enforcement |
| Security/operations boundary | PASS architecturally |
| Conformance/release boundary | PASS architecturally |
| Полный semantic enforcement | LIMITED — заявлен явно как enforcement debt |

### Найденный дефект

В IMPLEMENTATION/015-CONTEXT.md оставалась устаревшая финальная ссылка: 015 → 016 Operations & Security.

Она противоречила канонической нумерации после переноса Operations/Security на 020.

Исправлено на: 015 → 016 Scope → … → 020 Operations & Security → 021 Conformance & Release.

Commit исправления: 1ec36ce209d9b7f15c0f7f9cd80254f75c927677

### Повторная проверка

- 015 не содержит старого перехода на Operations/Security;
- каноническая цепочка 000–021 сохраняется;
- 020 и 021 находятся на своих новых номерах;
- Schema остаётся валидным JSON;
- структурные профили 015–019 согласованы с текущей Schema;
- заявленный semantic conformance не повышен искусственно.

### Итог

**СКВОЗНОЙ АРХИТЕКТУРНЫЙ СТРЕСС-ТЕСТ: PASS.**

**FULL SEMANTIC CONFORMANCE: НЕ ЗАЯВЛЯЕТСЯ.**

Открытый enforcement debt 015–019 остаётся частью архитектуры и не маскируется под PASS.


---

## 12.2. 020–021 — Полное архитектурное закрытие — 29 сентября 2026

После завершения 020 Operations & Security и 021 Conformance & Release оба документа приведены к единой схеме архитектурного закрытия, использованной для 015–019.

### 020 Operations & Security

Проверено и зафиксировано:

- границы ответственности Operations/Security;
- пять эксплуатационных слоёв L1–L5;
- различие Backup / Portable Package / Storage;
- Integrity ≠ Truth;
- Access ≠ Epistemic Trust;
- Update ≠ Migration;
- Rollback ≠ History deletion;
- Technical Incident ≠ False Content;
- недоверенные данные не являются исполняемыми инструкциями;
- supply-chain boundaries;
- disaster recovery pipeline;
- operational fidelity;
- O01–O15 базовые tests;
- O16–O30 stress tests;
- enforcement matrix;
- explicit enforcement debt;
- closure criteria.

Итог:

**020 — CLOSED WITH EXPLICIT ENFORCEMENT DEBT.**

### 021 Conformance & Release

Проверено и зафиксировано:

- четыре conformance dimensions;
- четыре conformance states;
- evidence model;
- owner-layer model;
- release artifact;
- G01–G15 release gates;
- PASS/FAIL/INDETERMINATE/NOT_APPLICABLE semantics;
- Standard → Implementation traceability;
- failure policy;
- regression policy;
- audit record;
- A1–A10 audit;
- anti-inference invariants;
- release decision rules;
- explicit enforcement debt;
- closure criteria.

Итог:

**021 — CLOSED WITH EXPLICIT ENFORCEMENT DEBT.**

### Сквозная проверка после обновления 020–021

Проверено:

| Проверка | Результат |
|---|---|
| 020 существует и имеет canonical number | PASS |
| 021 существует и имеет canonical number | PASS |
| 020 содержит explicit enforcement debt | PASS |
| 021 содержит explicit enforcement debt | PASS |
| 020 не объявляет machine enforcement без evidence | PASS |
| 021 запрещает documentation-only PASS | PASS |
| Backup ≠ Package | PASS |
| Integrity ≠ Truth | PASS |
| Update ≠ Migration | PASS |
| Rollback ≠ History deletion | PASS |
| Recovery ≠ Truth | PASS |
| MAPPED/DEFERRED ≠ PASS | PASS |
| FAIL/INDETERMINATE блокируют CONFORMING | PASS |
| Semantic conformance не объявлен автоматически | PASS |
| Каноническая цепочка 000–021 сохранена | PASS |

### Результат

**020–021 АРХИТЕКТУРНО ЗАКРЫТЫ.**

**FULL SEMANTIC / OPERATIONAL CONFORMANCE НЕ ЗАЯВЛЯЕТСЯ.**

Следующая рабочая стадия после 020–021 — не добавление новых нормативных implementation-документов, а перевод существующего enforcement debt 000–019/020 в реальные owner-layer механизмы, fixtures и tests с повторным conformance audit.


---

## 12.3. Первый пакет закрытия enforcement debt — Validator/Reference — 29 сентября 2026

После архитектурного закрытия 020–021 начат переход от декларативной спецификации к фактическому enforcement.

### Найденные разрывы

В IMPLEMENTATION/006-VALIDATOR-ARCHITECTURE.md были нормативно заданы:

- различие \`проверено ≠ не проверено\`;
- \`ValidationResult.coverage\`;
- структурированный Finding;
- стабильный rule/finding reference;
- независимое выполнение слоёв проверки.

В Reference Implementation до этого:

- \`ValidationResult\` не содержал coverage;
- Finding не содержал явного rule reference;
- при L3 reference failure \`ReferencePipeline\` заменял предыдущие findings только findings резолвера.

Последнее нарушало требование сохранять независимые результаты проверки.

### Реализованные исправления

#### REF-VAL-001 — Validation coverage

\`ValidationResult\` теперь содержит \`coverage\`.

Reference Validator явно сообщает:

- L1 — \`executed\`;
- L2 — \`executed\`;
- L3 — \`executed\`;
- L4 — \`executed\`;
- L5 — \`not_implemented\`.

Это принципиально важно: непокрытый L5 больше не может быть визуально принят за полный PASS.

#### REF-VAL-002 — Stable finding rule reference

Каждый Finding получает:

- \`code\`;
- \`rule\`, первоначально равный стабильному finding code;
- \`verification_state="verified"\`.

Это создаёт машинно проверяемую точку трассировки без притворства, что уже существует полный нормативный rule registry.

#### REF-VAL-003 — Cross-layer finding preservation

\`ReferencePipeline\` теперь сохраняет одновременно:

- L1/L2/L3/L4 findings Validator;
- L3 findings ReferenceResolver.

L3 failure больше не скрывает ранее обнаруженные нарушения.

#### REF-VAL-004 — Regression fixtures

Добавлены тесты:

- coverage явно показывает выполненные и нереализованные слои;
- reference-resolution failure не уничтожает предыдущие findings;
- L3 coverage остаётся \`executed\`.

### Изменённые файлы

- \`REFERENCE/src/encyclopedia_reference/validator.py\`
- \`REFERENCE/src/encyclopedia_reference/pipeline.py\`
- \`REFERENCE/tests/test_vertical_slice.py\`

Последний commit пакета: \`fa73434fd279b29149a8c3da079c112f89694f90\`.

Предыдущие commits этого пакета:

- \`ff156cf6137c3fcfdfccbe802a7402253ba728ae\` — coverage/structured Finding;
- \`5c3c07554db2f8f6b3aeba22a2b1e2646cd415c1\` — сохранение findings;
- \`bf60bc314bff894fdd98d34245a550e82cbf193f\` — regression tests.

### Проверка

Код и тесты повторно прочитаны из GitHub после записи.

Статические проверки:

| Проверка | Результат |
|---|---|
| \`ValidationResult.coverage\` присутствует | PASS |
| L5 явно обозначается \`not_implemented\` | PASS |
| Finding содержит stable \`rule\` | PASS |
| Finding содержит verification state | PASS |
| Pipeline сохраняет Validator findings | PASS |
| Pipeline добавляет Resolver findings | PASS |
| Regression tests присутствуют | PASS |

Полный pytest после commit в данном проходе не выполнялся: доступная GitHub workflow-обвязка не предоставила run, связанный с этими commit через используемый интерфейс. Поэтому **runtime test PASS не заявляется**.

Это ограничение зафиксировано отдельно и не превращается в PASS декларацией.

### Статус пакета

**REF-VAL-001…004 — реализованы на уровне Reference Implementation + regression fixtures.**

Это первый фактический перевод части enforcement debt из архитектурного DEFERRED/MAPPED в проверяемую реализацию.

Следующий пакет должен продолжить тот же принцип: один owner-layer → конкретный rule/finding code → fixture → test → повторный audit.


### Уточнение REF-VAL-003

В ходе post-write review обнаружено, что первоначальная реализация агрегирования findings всё ещё сохраняла ранний short-circuit pipeline: при L1/L2/L4 failure L3 resolver не запускался.

Это было исправлено сразу после обнаружения.

Теперь ReferencePipeline.create/edit:

1. выполняет Validator;
2. независимо выполняет ReferenceResolver;
3. объединяет findings;
4. объединяет coverage;
5. блокирует storage write при любом error;
6. сохраняет все независимые findings.

Последний commit исправления: \`d6ae7fa542f48b46841ee82f6b058729f2b3b3b4\`.

Статическая повторная проверка после commit:

- ранний \`if not result.passed: return result\` удалён из create/edit — PASS;
- Validator findings сохраняются — PASS;
- Resolver findings добавляются — PASS;
- L3 coverage фиксируется как executed — PASS;
- storage write выполняется только после aggregate PASS — PASS.

Runtime pytest всё ещё не заявляется без фактически выполненного CI/runtime run.


---

## 12.4. L3 Reference Integrity — систематический обход канонических ссылок — 29 сентября 2026

### Найденный разрыв

Предыдущий ReferenceResolver содержал ручной перечень полей для каждого Record Type.

Риск: новый канонический record_ref, добавленный в существующий Content Profile, мог пройти Schema, но остаться вне L3 reference validation до ручного обновления resolver.

Это не соответствует требованию 006, согласно которому L3 проверяет ссылочную целостность Record graph, а не только заранее перечисленные сегодня поля.

### Реализация

REFERENCE/src/encyclopedia_reference/references.py переработан:

- канонические объекты с record_id рекурсивно распознаются как record_ref;
- проверяется указанная version, если она присутствует;
- без version проверяется существование логической Record через latest resolver;
- вложенные списки и объекты обходятся системно;
- extensions намеренно остаются opaque, поскольку их data не является частью канонического Record graph без отдельного Extension Profile;
- findings получают subject с точным путём;
- сохранён стабильный VAL-L3-REFERENCE-VERSION.

### Regression tests

Добавлены:

- nested canonical reference → unresolved L3 finding;
- extension payload → не интерпретируется автоматически как canonical reference.

Последний commit реализации:

32c6e08deba1a1d67d5619d9d729d58f7d2d1870

Последний commit regression tests:

c8c03295010fe82335124bbce5a79561c46bd58f

### Статическая проверка

| Проверка | Результат |
|---|---|
| Ручной список reference-полей удалён | PASS |
| Nested canonical refs обнаруживаются | PASS |
| Versioned refs проверяются | PASS |
| Unversioned refs не считаются автоматически текущей версией в данных | PASS |
| Extension payload не втягивается в canonical graph | PASS |
| Stable L3 finding code сохранён | PASS |
| Subject path сохраняется | PASS |

Runtime pytest PASS снова не заявляется без фактически выполненного run.

### Статус

L3 Reference Integrity — усилен в Reference Implementation.

Это следующий конкретный перевод enforcement debt из декларативного требования в machine-checkable behavior.

Оставшийся долг L3 после пакетов 12.5–12.6:

- дополнительные typed target constraints только там, где будущий Standard или Relation frame однозначно определит допустимый тип цели.


---

## 12.5. L3 Typed Target Constraints — Evidence Use — 29 сентября 2026

### Основание

Для Evidence Use нормативная модель уже однозначно определяет две семантические роли:

- целевое утверждение должно быть Claim;
- идентичность источника должна быть Source.

Поэтому эти ограничения можно реализовать без предположений.

Другие универсальные Record references пока не типизируются автоматически: если Standard/Profile не определяет допустимый target type однозначно, Validator не должен его угадывать.

### Реализация

Добавлено правило:

VAL-L3-REFERENCE-TARGET-TYPE

Для:

- content.claim_ref → target claim;
- content.source_ref → target source.

Проверка выполняется после разрешения конкретной Record/version и дополнительно к L3 existence/version check.

Ошибка target type:

- является отдельным Finding;
- имеет severity error;
- содержит subject path;
- не изменяет саму Record;
- блокирует Storage write через aggregate pipeline.

### Regression tests

Добавлены:

- Claim reference, указывающий на Source → FAIL;
- Source reference, указывающий на Claim → FAIL;
- корректная пара Claim + Source → PASS.

Последние commits:

- implementation: f98bec4d7ddfe16cee86c6173c21affda296e66b;
- tests: 35f974b119443f55d95fcde92b24db139bebb549.

### Статическая повторная проверка

| Проверка | Результат |
|---|---|
| VAL-L3-REFERENCE-TARGET-TYPE существует | PASS |
| claim_ref → claim | PASS |
| source_ref → source | PASS |
| Versioned target проверяется до type comparison | PASS |
| Нормативно не определённые refs не типизируются | PASS |
| Duplicate findings для Evidence Use устранены | PASS |
| Regression fixtures присутствуют | PASS |

Runtime pytest PASS не заявляется: среда не имеет доступа к внешнему GitHub/DNS для фактического checkout и запуска.

### Статус

L3 Typed Target Constraints для Evidence Use — реализованы в Reference Implementation + regression fixtures.

Следующий L3 debt item остаётся отдельно:

- typed constraints для других профилей, только где применимый Standard/Relation frame однозначно задаёт допустимый тип цели.


---

## 12.6. L3 Historical Compatibility и Package Graph Integrity — 29 сентября 2026

### Реализовано

L3 Reference Resolver теперь дополнительно проверяет:

- identity target: фактический record_id загруженной Record совпадает с идентификатором ссылки;
- historical version: при versioned reference фактический record_version совпадает с запрошенной версией;
- typed target constraints из 12.5 продолжают применяться к фактически разрешённой версии.

Добавлены стабильные findings:

- VAL-L3-REFERENCE-TARGET-IDENTITY;
- VAL-L3-REFERENCE-HISTORICAL-VERSION.

### Package-level graph integrity

Recovery больше не зависит от порядка файлов пакета.

Алгоритм теперь:

1. проверяет и загружает все допустимые Record;
2. формирует полный snapshot;
3. после этого выполняет L3 ReferenceResolver по полному snapshot storage.

Следовательно, ссылка A → B не становится ошибкой только потому, что B физически находился после A в package.

### Graph cycles

Универсальный запрет циклов НЕ вводится.

STANDARD/013-RELATION.md определяет formal properties как свойства конкретного Relation type/frame и прямо запрещает предполагать транзитивность и другие свойства универсально.

Поэтому:

- наличие цикла в графе ≠ нарушение само по себе;
- цикл должен проверяться только тогда, когда применимое Relation type/frame нормативно объявляет соответствующее ограничение;
- Reference Resolver не придумывает такие ограничения.

Это не enforcement debt, а зафиксированная граница применимости L3.

### Regression fixtures

Добавлены проверки:

- несовпадение фактического target identity;
- несовпадение исторической target version;
- допустимость цикла без нормативного запрета;
- package references проверяются после полного восстановления.

### Статическая проверка

| Проверка | Результат |
|---|---|
| target identity compatibility | PASS |
| historical version compatibility | PASS |
| package-wide reference pass after complete snapshot | PASS |
| file-order independence | PASS |
| universal cycle prohibition отсутствует | PASS |
| normative typed target constraints сохранены | PASS |

Runtime pytest PASS не заявляется: среда по-прежнему не имеет внешнего DNS/GitHub доступа для фактического checkout/запуска.

### Итог L3

Закрыты реализуемые и нормативно определённые части:

- existence/version;
- typed target constraints;
- target identity;
- historical version compatibility;
- package-level reference closure;
- file-order independence.

Universal cycle semantics не являются универсальным L3 правилом и поэтому не должны быть искусственно реализованы.

Остающиеся ограничения L3 относятся только к будущим явно определённым Relation type/frame constraints и не должны вводиться до появления соответствующего нормативного основания.


---

## 12.7. L3 Typed Target Constraints — полный однозначно нормативный набор — 29 сентября 2026

Проведён повторный аудит всех canonical `record_ref` в реализованных Content Profiles и соответствующих Standards.

### Реализованы machine-checkable constraints

Помимо Evidence Use из 12.5, теперь типизируются только ссылки, для которых роль цели однозначно определена:

| Поле | Допустимый target |
|---|---|
| Claim.scope_ref | scope |
| Claim.context_ref | context |
| Claim.relation_refs[] | relation |
| EvidenceUse.source_state_ref | state |
| EvidenceUse.resolution_context | context |
| Decision.context_ref | context |
| Decision.scope_ref | scope |
| Decision.process_ref | process |
| Action.context_ref | context |
| Action.scope_ref | scope |
| Action.decision_ref | decision |
| Action.procedure_ref | process |
| Event.context_ref | context |
| Event.scope_ref | scope |
| Result.scope_ref | scope |
| Result.observation_scope_ref | scope |
| Process.context_ref | context |
| Identity.scope_ref | scope |
| Context.scope_ref | scope |
| TrustReputation.scope_ref | scope |
| TrustReputation.context_ref | context |

Одинаково именованные поля проверяются по canonical path и применимому Content Profile; extensions остаются opaque.

### Намеренно НЕ типизируются

Полиморфные ссылки остаются unrestricted по target type, когда Standard допускает разные семантические объекты или не задаёт единственный Record Type:

- generic target/subject references;
- participants;
- inputs/premises/assumptions;
- provenance target/inputs/outputs;
- Identity targets/candidates/evidence;
- Relation participants/frame;
- Context target/preconditions;
- Scope target/universe;
- Authorship target/rights;
- Trust target/basis/subject/goal;
- другие ссылки без однозначного нормативного target type.

Это не пропуск реализации: искусственная типизация таких полей создала бы новое нормативное правило внутри Validator.

### Regression coverage

Добавлен regression fixture, проверяющий несовместимый target type для каждого однозначного constraint family.

### Статическая проверка

- typed constraint registry присутствует — PASS;
- canonical path matching для scalar/list references — PASS;
- Evidence Use constraints сохранены — PASS;
- extensions не затрагиваются — PASS;
- полиморфные references не ограничены искусственно — PASS.

### Итог L3

Все текущие однозначно нормативные typed-target constraints переведены в machine-checkable L3.

Новый typed-target constraint добавляется только вместе с нормативным основанием в соответствующем Standard/Profile/Relation frame.

### Post-audit correction — Decision.process_ref

Дополнительная сверка `STANDARD/007-DECISION.md` с машинной схемой подтвердила семантику «процесс решения», а `content.process_ref` является отдельной ссылкой на этот процесс в профиле Decision. Поэтому ограничение:

- `Decision.process_ref → process`

теперь фактически enforced в `ReferenceResolver` и покрыто regression fixture `test_unambiguous_typed_reference_constraints`.

Последние commits этого точечного исправления:

- implementation: `55b4b74de1c5cf3dafcb8fee3351ce053754f7aa`;
- test: `0797b4671ce0c22d99891bc9cb813e64efe7ed21`.

После этого audit claim о `Decision.process_ref → process` соответствует фактической Reference Implementation.

Runtime pytest PASS по-прежнему не заявляется без фактически выполненного runtime/CI run.


---

## 12.8. L4/L5 enforcement package — 29 сентября 2026

### Цель

Перевести следующий крупный блок enforcement debt из декларативного состояния в фактическую Reference Implementation:

L4 — Semantic / Standard Rules  
L5 — Integrity, History and Integration

### L4 — реализовано

Добавлены стабильные machine-checkable findings для:

- завершённой Assessment: target / aspect / result;
- завершённого Inference: conclusion / attribution;
- Inference attribution: known → agent_ref; reconstructed → method_ref;
- завершённого Decision: decision_result / decision_maker;
- Evidence Use: supports / contradicts;
- Source identity;
- State applicable frame;
- Process temporal/process frame;
- Relation type + applicable frame;
- Identity criterion + frame + candidate_refs для ambiguous/possible/probable;
- Context / Scope / Provenance / Authorship / Trust обязательных semantic anchors;
- Trust subject/goal для trust assessment;
- Result attributed causal attribution → basis_ref;
- запрета автоматического превращения publication_status в truth;
- запрета побочного создания truth другим Record type;
- planned/predicted Event не принимается как автоматически observed.

Typed references не дублируются в L4: они остаются ответственностью L3 ReferenceResolver.

### L5 — реализовано

Record-level:

- integrity.algorithm=sha256;
- canonicalization: json-sort-keys-utf8-excluding-integrity;
- вычисление digest по canonical Record без поля integrity;
- обнаружение integrity mismatch;
- indeterminate, а не PASS, при неподдерживаемом integrity algorithm/canonicalization;
- проверка порядка valid_time.start/end;
- запрет совпадения record_id и record_version.

Dataset-level:

- duplicate logical (record_id, record_version) detection;
- повторная L1–L5 проверка всех Record набора;
- запуск после формирования полного recovery snapshot.

Package-level:

- Recovery сохраняет существующую manifest/file SHA-256 проверку;
- после полной сборки snapshot запускается Dataset L5;
- затем выполняется L3 ReferenceResolver;
- тем самым L5 Dataset не зависит от физического порядка файлов пакета.

### Regression fixtures

Добавлены проверки:

- корректный Record integrity digest → PASS;
- повреждённый digest → FAIL;
- неподдерживаемый integrity algorithm → INDETERMINATE;
- reversed valid_time → FAIL;
- duplicate logical Record version → FAIL;
- coverage L5 → EXECUTED;
- завершённый Inference с known attribution без agent_ref больше не считается корректным;
- package recovery сохраняет новый L5 проход.

### Важное ограничение

Runtime pytest/CI PASS не заявляется: через доступный интерфейс не выполнялся фактический runtime checkout проекта с последующим запуском тестов.

Следовательно, текущий статус:

IMPLEMENTED IN SOURCE + REGRESSION FIXTURES  
STATICALLY REVIEWED  
RUNTIME EXECUTION NOT VERIFIED

Это сознательно не превращается в ложный PASS.

### Текущий статус слоёв Validator

| Layer | Status |
|---|---|
| L1 Structural | EXECUTED |
| L2 Type/Profile | EXECUTED |
| L3 Reference Integrity | EXECUTED |
| L4 Semantic/Standard | EXECUTED |
| L5 Integrity/History/Integration | EXECUTED |

### Следующий аудит

После L4/L5 enforcement следующим обязательным этапом является не добавление случайных правил, а сквозной conformance/stress pass:

1. проверить все новые finding codes;
2. проверить positive/negative/unknown/conflict fixtures;
3. проверить Pipeline aggregate semantics;
4. проверить Recovery/Package/Publication boundaries;
5. сопоставить закрытые L4/L5 правила с нормативными Standards;
6. только затем обновлять общий процент enforcement debt.


---

## 12.9. L5 indeterminate write barrier — 29 сентября 2026

Post-implementation review обнаружил сквозную проблему: L5 мог корректно вернуть INDETERMINATE, но старый Pipeline разрешал запись, потому что блокировал только severity=error.

Исправлено:

- ReferencePipeline.create() блокирует storage write при любом ValidationResult.status != pass;
- ReferencePipeline.edit() использует тот же барьер;
- при отсутствии error, но наличии unverifiable L5 finding, наружу возвращается indeterminate;
- запись не производится.

Добавлен regression fixture:

- unsupported integrity algorithm;
- ожидаемый status = indeterminate;
- passed == False;
- Record отсутствует в Storage после попытки create.

Это закрывает границу:

indeterminate validation != successful persistence.

### Версионирование

Reference Validator повышен с 0.1 до 0.2, поскольку изменён machine-checkable rule set.

### CI/runtime

Для последнего test commit workflow run не найден. Поэтому runtime pytest PASS не заявляется.


---

## 12.10. Post-audit correction: Event observation boundary — 29 сентября 2026

При повторной проверке L4 обнаружено, что правило, связывавшее planned/predicted Event с наличием observation_refs, было слишком сильной эвристикой и не следовало однозначно из нормативной границы.

Оно удалено из Validator.

Причина:

observation_refs могут документировать наблюдение материала/описания, не превращая сам Event автоматически в observed Event.

Следовательно:

- автоматическое присваивание observed запрещено;
- наличие observation_refs само по себе не является достаточным основанием для запрета;
- Validator не делает это семантическое предположение.

Статус после correction:

L4 rule set содержит только правила, имеющие достаточное нормативное основание и machine-checkable representation.


---

## 12.11. Сквозной Conformance / Stress Runtime Pass — 30 сентября 2026

### Runtime

После исправления последнего L4 regression fixture выполнен реальный GitHub Actions run:

- commit: a2f1dec0cbb08dc6f77302604fc7cc8b43073733;
- Python: 3.11.16;
- pytest: 8.x;
- workflow: Reference implementation tests;
- полный запуск: REFERENCE/tests;
- результат: PASS;
- job: 109632196438.

Предыдущий run был намеренно остановлен статусом FAIL: 100 passed, 1 failed. Причина была не в Validator, а в устаревшем positive fixture Inference, который ещё использовал attribution.mode=known без обязательного agent_ref.

Fixture исправлен, повторный полный runtime run дал PASS.

### Фактически проверенные поверхности

- L1 schema/structural validation;
- L2 type/profile/version compatibility;
- L3 reference shape и graph integrity;
- typed target constraints;
- historical reference compatibility;
- L4 semantic lifecycle rules;
- L4 anti-inference boundaries;
- L5 integrity digest;
- L5 valid-time ordering;
- L5 dataset duplicate detection;
- Storage version preservation;
- optimistic concurrency;
- path traversal;
- Package manifest integrity;
- malformed package recovery;
- duplicate package entries;
- file-order-independent recovery;
- Publication non-mutation;
- deterministic Query;
- Unicode/nested data;
- fuzz/property deterministic validation;
- 500 mutation fuzz iterations;
- 250 nested-value iterations.

### Destructive result

Ни один из существующих destructive/stress сценариев не выявил runtime regression после L4/L5 изменений.

### Важная граница

PASS означает, что текущий реализованный Reference test suite успешно выполнен на конкретном commit.

PASS не означает:

- истинность Claim;
- полноту всех будущих Standard rules;
- автоматическую доказанность semantic conformance вне существующих fixtures;
- отсутствие будущих дефектов.

### Итог

Текущий Reference Implementation прошёл полный доступный runtime conformance/stress suite.

Статус:

REFERENCE IMPLEMENTATION — RUNTIME PASS.

FULL SEMANTIC CONFORMANCE — НЕ ЗАЯВЛЯЕТСЯ.


## 12.12. Release Candidate / Conformance Gate

30 сентября 2026 года выполнен первый исполняемый Release Conformance Gate.

Проверены:

- наличие обязательного комплекта IMPLEMENTATION 000–021 и audit record;
- JSON Schema Draft 2020-12 parse;
- наличие и согласованность supported Type Profile registry;
- полный runtime suite `REFERENCE/tests`;
- release gate integration;
- генерация машиночитаемого `RELEASE/release-gate-report.json`;
- публикация gate report как CI artifact;
- явная epistemic boundary для conformance/release.

Первый прогон выявил реальный дефект release gate: неверно указан путь к IMPLEMENTATION 008. Дефект исправлен, после чего повторный runtime gate завершился:

**RELEASE CONFORMANCE GATE — PASS**

Итоговое состояние Release Candidate:

**CONFORMING_WITH_LIMITATIONS**

Ограничение:

- G02 — Foundation/Standard compatibility — **INDETERMINATE**, поскольку rule-by-rule compatibility evidence ещё не автоматизирована/не оформлена как отдельный подписанный evidence record.

При этом полный semantic conformance по проекту **не заявляется**.

Reference test suite в том же release sequence также завершён успешно:

**REFERENCE IMPLEMENTATION TESTS — PASS**

Release gate не превращает INDETERMINATE в PASS и не трактует release/conformance как доказательство истинности Record или Claim.

Evidence:

- Release gate workflow run 2: `36665598756`;
- Release gate job: `109729480356`;
- Reference implementation workflow run 133: `36665598759`;
- artifact: `release-gate-report`, artifact id `11075977989`;
- gate report generated at CI runtime.



## 12.13. G02 Foundation/Standard Compatibility Closure

G02 пересмотрен в соответствии с нормативной семантикой 021:

> G02 проверяет отсутствие неразрешённых архитектурных противоречий и наличие явного контракта Standard → Implementation. G02 не означает full semantic enforcement.

Создан машиночитаемый evidence:

`RELEASE/FOUNDATION-STANDARD-COMPATIBILITY.json`

Матрица содержит 19 Standard → Profile mappings и проверяет:

- наличие соответствующего implementation owner;
- наличие schema representation;
- наличие validator profile registry;
- наличие специальных implementation documents для 015–019;
- сохранение epistemic boundary;
- отсутствие заявления full semantic conformance.

После добавления machine-checkable G02 gate его статус должен быть:

**G02 — PASS**

При этом semantic enforcement debt остаётся явно отделённым и не преобразуется в conformance claim.



## 12.14. G02 Runtime Closure

Final machine-checked G02 run:

- Release Conformance Gate run: `11`
- workflow run: `36666537605`
- head SHA: `f5a02a804d5f9af1c1a29bf5d235d024985ba545`
- G02: **PASS**
- full Release Gate: **PASS**
- Reference implementation tests run: `135`
- workflow run: `36666537700`
- Reference tests: **PASS**

G02 is therefore closed at the architectural compatibility level defined by 021.

This closure does **not** close semantic enforcement debt and does **not** upgrade the project to full semantic conformance.


## 12.15. Semantic Conformance Closure — anti-inference package 1 — 30 сентября 2026

После добавления `REFERENCE/tests/test_semantic_conformance.py` выполнен первый отдельный пакет сквозного semantic conformance.

### Покрытые границы

- State representation не создаёт Event автоматически.
- Process representation не создаёт Cause, Goal или Purpose автоматически.
- Relation representation не создаёт inverse Relation автоматически.
- Context не превращается автоматически в Participant или semantic/reference frame.
- Scope не расширяется автоматически до Universe или member-level references.
- Provenance не превращается автоматически в Authorship.
- Authorship/Contribution не превращается автоматически в Provenance.
- Trust/Reputation не создаёт Truth.
- Unknown Identity сохраняется как `unknown` и не разрешается публикацией.
- Storage round-trip сохраняет Record semantics.
- Publication не мутирует исходные Records и не добавляет semantic roles.

### Runtime evidence

Reference implementation workflow:

- run 139;
- workflow run: `36667032343`;
- commit: `b70ae69f4c3ab5ea27d02647e032f7c396de2209`;
- result: **PASS**;
- результат pytest: **112 passed**.

В первом варианте пакета был обнаружен реальный тестовый дефект: тесты предполагали наличие pipeline-resolvable references и не соответствовали контракту FileStorage. После исправления fixture contract и повторного запуска получен PASS.

### Статус

Шесть конкретных нормативных правил переведены из `DEFERRED` в `TESTED`:

- P-20;
- RL-03;
- RL-29;
- ID-41;
- CTX-10;
- CTX-14.

Это не означает full semantic conformance. Остальной enforcement debt сохраняется и должен закрываться отдельными пакетами с собственным runtime evidence.


## 12.16. Semantic Conformance Closure — preservation/recovery package 2 — 30 сентября 2026

Добавлен расширенный semantic conformance fixture для Process, включающий material content, participants, Context, Scope, temporal boundaries, phase references, envelope context/scope и сохранение unknown temporal value. Package → recovery теперь проверяет полный типизированный reference graph и сравнивает исходные Records с восстановленным snapshot.

Runtime evidence:

- Reference implementation run 146;
- workflow run: `36667594663`;
- commit: `9fd0daa424e3a9824fae22baee75c34d9ca99aa9`;
- result: **PASS**.
- Release Conformance Gate run 24;
- workflow run: `36667594566`;
- result: **PASS**.

На основании этого пакета правило **P-86** переведено из `DEFERRED` в `TESTED`. Другие fidelity rules не переводятся автоматически: для каждого требуется соответствующий transformation path и собственная evidence coverage.


## 12.17. Semantic Conformance Closure — Identity/Context boundary package 3 — 30 сентября 2026

Добавлены негативные fixtures для Identity, Context и Scope:

- ambiguous Identity сохраняет candidates и uncertainty и не превращается в resolved_same;
- Context сохраняет epistemic_status=disputed;
- отсутствие epistemic_status в incomplete Context остаётся отсутствием, без invented value;
- Scope сохраняет membership_rule и level без добавления universe_ref.

Runtime evidence:

- Reference implementation run 147;
- workflow run: `36667648333`;
- result: **PASS**;
- Release Conformance Gate run 26;
- workflow run: `36667648282`;
- result: **PASS**.

Переведены в `TESTED`: ID-46, CTX-17, CTX-18, CTX-26. Scope fixture пока не переводит SCP rules автоматически, поскольку publication preservation не доказывает отсутствие scope expansion во всех transformation paths.


## 12.18. Audit registry namespace correction — 30 сентября 2026

В ходе продолжения semantic conformance closure обнаружена ошибка трассировки: идентификаторы `P-01…P-53` использовались одновременно для Process и Provenance. Это создавало неоднозначность rule reference и не соответствовало требованию 021 о стабильной трассировке.

Исправлено: все правила STANDARD/017 Provenance в rule-by-rule matrix получили отдельный namespace `PRV-001…PRV-053`. Идентификаторы STANDARD/012 Process `P-*` сохранены без изменений.

Это изменение не меняет нормативный смысл STANDARD/017 и не добавляет новых правил; оно исправляет только audit traceability.

Commit: `2e153cd2177cf87b4065957b343a9c1b2abf287d`.

После correction полный audit registry должен использовать уникальные namespace для State, Process, Relation, Identity, Context, Scope, Provenance и Authorship/Contribution.

Текущее распределение статусов после semantic packages 1–3:

- ENFORCED: 14
- PARTIAL: 17
- TESTED: 12
- MAPPED: 61
- DEFERRED: 830

Полный semantic conformance по-прежнему не заявляется.


## 12.19. Semantic Conformance Closure — Provenance/Authorship/Trust package 4 — 30 сентября 2026

Добавлены fixtures, проверяющие:

- unknown operation provenance остаётся explicit;
- разные provenance inputs остаются различимыми;
- Provenance не создаёт Author/author_ref автоматически;
- Authorship сохраняет Contribution, Role, Responsibility и Rights как отдельные значения;
- Trust Assessment сохраняет subject, goal и uncertainty и не создаёт `truth`.

Runtime evidence:

- Reference implementation run 148;
- workflow run: `36667786628`;
- result: **PASS**;
- Release Conformance Gate run 30;
- workflow run: `36667786686`;
- result: **PASS**.

На основании прямого покрытия переведены в `TESTED`: PRV-044 и PRV-052. Trust fixture пока не переводит отдельные Trust rules, поскольку в audit registry для 019 ещё нет такой же уникальной rule-by-rule namespace matrix; сначала она должна быть нормализована.


## 12.20. Semantic Conformance Closure — Relation/History package 5 — 30 сентября 2026

Добавлены fixtures для Relation history и identity boundaries:

- изменение Relation между версиями сохраняет обе исторические версии;
- две Relation Records с одинаковыми participants и relation_type остаются двумя distinct Records;
- Storage не выполняет implicit merge и не уничтожает историческую версию.

Runtime evidence:

- Reference implementation run 149;
- workflow run: `36667851987`;
- result: **PASS**;
- Release Conformance Gate run 32;
- workflow run: `36667852094`;
- result: **PASS**.

Переведены в `TESTED`: RL-45 и RL-49.


## 12.21. Semantic Conformance Closure — Trust/Reputation namespace normalization and package 6 — 30 September 2026

### 12.21.1. Registry correction

STANDARD/019 previously had no unique rule-by-rule namespace comparable to PRV-* for Provenance. This prevented direct traceability from a normative Trust rule to an owner layer, fixture and evidence.

A canonical namespace is now established:

- TR-001 … TR-196;
- each identifier maps one-to-one to STANDARD/019 §1 … §196;
- no TR-* identifier is reused for another Standard;
- the normative text itself is unchanged.

### 12.21.2. Current Trust/Reputation rule matrix

| Rule | Standard section | Owner | Status | Evidence boundary |
|---|---|---|---|---|
| TR-001 | §1 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-002 | §2 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-003 | §3 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-004 | §4 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-005 | §5 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-006 | §6 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-007 | §7 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-008 | §8 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-009 | §9 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-010 | §10 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-011 | §11 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-012 | §12 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-013 | §13 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-014 | §14 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-015 | §15 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-016 | §16 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-017 | §17 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-018 | §18 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-019 | §19 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-020 | §20 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-021 | §21 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-022 | §22 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-023 | §23 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-024 | §24 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-025 | §25 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-026 | §26 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-027 | §27 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-028 | §28 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-029 | §29 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-030 | §30 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-031 | §31 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-032 | §32 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-033 | §33 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-034 | §34 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-035 | §35 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-036 | §36 | Trust/Profile/Validator | **TESTED** | Direct semantic fixture in package 12.21 |
| TR-037 | §37 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-038 | §38 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-039 | §39 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-040 | §40 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-041 | §41 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-042 | §42 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-043 | §43 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-044 | §44 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-045 | §45 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-046 | §46 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-047 | §47 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-048 | §48 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-049 | §49 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-050 | §50 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-051 | §51 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-052 | §52 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-053 | §53 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-054 | §54 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-055 | §55 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-056 | §56 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-057 | §57 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-058 | §58 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-059 | §59 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-060 | §60 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-061 | §61 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-062 | §62 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-063 | §63 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-064 | §64 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-065 | §65 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-066 | §66 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-067 | §67 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-068 | §68 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-069 | §69 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-070 | §70 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-071 | §71 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-072 | §72 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-073 | §73 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-074 | §74 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-075 | §75 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-076 | §76 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-077 | §77 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-078 | §78 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-079 | §79 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-080 | §80 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-081 | §81 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-082 | §82 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-083 | §83 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-084 | §84 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-085 | §85 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-086 | §86 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-087 | §87 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-088 | §88 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-089 | §89 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-090 | §90 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-091 | §91 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-092 | §92 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-093 | §93 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-094 | §94 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-095 | §95 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-096 | §96 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-097 | §97 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-098 | §98 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-099 | §99 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-100 | §100 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-101 | §101 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-102 | §102 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-103 | §103 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-104 | §104 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-105 | §105 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-106 | §106 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-107 | §107 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-108 | §108 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-109 | §109 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-110 | §110 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-111 | §111 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-112 | §112 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-113 | §113 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-114 | §114 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-115 | §115 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-116 | §116 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-117 | §117 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-118 | §118 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-119 | §119 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-120 | §120 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-121 | §121 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-122 | §122 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-123 | §123 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-124 | §124 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-125 | §125 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-126 | §126 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-127 | §127 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-128 | §128 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-129 | §129 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-130 | §130 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-131 | §131 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-132 | §132 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-133 | §133 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-134 | §134 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-135 | §135 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-136 | §136 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-137 | §137 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-138 | §138 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-139 | §139 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-140 | §140 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-141 | §141 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-142 | §142 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-143 | §143 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-144 | §144 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-145 | §145 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-146 | §146 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-147 | §147 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-148 | §148 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-149 | §149 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-150 | §150 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-151 | §151 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-152 | §152 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-153 | §153 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-154 | §154 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-155 | §155 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-156 | §156 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-157 | §157 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-158 | §158 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-159 | §159 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-160 | §160 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-161 | §161 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-162 | §162 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-163 | §163 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-164 | §164 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-165 | §165 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-166 | §166 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-167 | §167 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-168 | §168 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-169 | §169 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-170 | §170 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-171 | §171 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-172 | §172 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-173 | §173 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-174 | §174 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-175 | §175 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-176 | §176 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-177 | §177 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-178 | §178 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-179 | §179 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-180 | §180 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-181 | §181 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-182 | §182 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-183 | §183 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-184 | §184 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-185 | §185 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-186 | §186 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-187 | §187 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-188 | §188 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-189 | §189 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-190 | §190 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-191 | §191 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-192 | §192 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-193 | §193 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-194 | §194 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-195 | §195 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |
| TR-196 | §196 | Trust/Profile/Validator | **ENFORCED** | Requires dedicated semantic/context/history/transformation enforcement |

### 12.21.3. Evidence

Added direct fixtures for:

- preservation of subject/goal/scope/context/time/uncertainty;
- distinct Trust assessments with different goals;
- unknown reputation remaining unknown rather than negative;
- historical Trust/Reputation versions remaining distinct;
- no transfer between distinct targets;
- publication boundary not creating truth.

The corresponding rules are the only Trust rules promoted to TESTED in this package. No other TR rule is promoted merely because the architecture document mentions it.

Reference test commit: 93842096e81533732b0d192e524d329410e2eda3.

### 12.21.4. Conformance boundary

Trust/Reputation namespace traceability: **PASS**.  
Direct semantic evidence in this package: **9/196 rules TESTED**.  
Remaining Trust/Reputation rules: **187 DEFERRED** pending dedicated owner-layer enforcement.

The historical global DEFERRED count from packages 1–5 is not recomputed here because normalization changes the registry cardinality. A full 011–019 recount is required after all namespaces are normalized.

Full semantic conformance remains **NOT CLAIMED**.


## 12.22. Semantic Conformance Closure — Temporal State/Process/Relation package 7 — 30 September 2026

Добавлены прямые fixtures для временных границ:

- State snapshot не расширяется автоматически до interval semantics;
- unknown start/end Process не заменяется придуманными точными границами;
- observation gap не становится interruption/termination;
- Relation valid_time остаётся отличимым от record creation time;
- temporal order не создаёт causal relation автоматически.

Прямое покрытие переводит в TESTED:

- S-21;
- P-39;
- P-42;
- RL-41;
- RL-58.

Final Reference test commit: 64ea37a1e6a03268fb093908c99004d039e296fa2.

CI evidence: Reference implementation run 159 — PASS; Release Conformance Gate run 44 — PASS.

Остальные временные правила не переводятся автоматически: для continuity, recurrence, historical dependency, effective-time roles и causality нужны отдельные fixtures и owner-layer mechanisms.

Full semantic conformance remains **NOT CLAIMED**.


## 12.23. Полный rule-by-rule пересчёт STANDARD/011–019 — 30 сентября 2026

### 12.23.1. Метод

Пересчёт выполнен непосредственно по текущей rule-by-rule matrix этого документа.

В выборку входят только строки с уникальным namespace вида `PREFIX-N`. Проверены:
- наличие namespace;
- уникальность каждого rule ID;
- принадлежность namespace соответствующему Standard;
- один текущий статус на правило;
- отсутствие дубликатов.

### 12.23.2. Результат

**1129 нормативных правил; 1129 уникальных rule ID; 0 дубликатов.**

| Статус | Количество |
|---|---:|
| ENFORCED | 14 |
| TESTED | 25 |
| PARTIAL | 16 |
| MAPPED | 61 |
| DEFERRED | 1013 |
| **ВСЕГО** | **1129** |

### 12.23.3. По namespace

| Namespace | Правил | ENFORCED | TESTED | PARTIAL | MAPPED | DEFERRED |
|---|---:|---:|---:|---:|---:|---:|
| S | 63 | 6 | 1 | 4 | 28 | 24 |
| P | 89 | 2 | 2 | 0 | 30 | 55 |
| RL | 115 | 2 | 4 | 0 | 3 | 106 |
| ID | 131 | 4 | 2 | 0 | 0 | 125 |
| CTX | 122 | 0 | 5 | 2 | 0 | 115 |
| SCP | 237 | 0 | 0 | 2 | 0 | 235 |
| PRV | 53 | 0 | 2 | 2 | 0 | 49 |
| AC | 123 | 0 | 0 | 6 | 0 | 117 |
| TR | 196 | 0 | 9 | 0 | 0 | 187 |

### 12.23.4. Проверка арифметики

- 14 + 25 + 16 + 61 + 1013 = **1129**;
- сумма namespace totals = **1129**;
- сумма namespace statuses = **1129**;
- unique rule IDs = **1129**;
- duplicate rule IDs = **0**.

### 12.23.5. Что означает результат

Это полный **rule-by-rule recount**, а не утверждение полного semantic conformance.

`DEFERRED` означает, что нормативное требование известно и трассируемо, но прямого owner-layer enforcement/evidence пока недостаточно для перевода в `TESTED` или `ENFORCED`.

Нельзя законно уменьшать `DEFERRED` только изменением таблицы. Перевод требует:
1. конкретного owner-layer механизма;
2. applicability boundary;
3. положительного и, где требуется, отрицательного fixture;
4. теста;
5. CI/release evidence.

### 12.23.6. Итог

**Full rule-by-rule recount: PASS.**

**Full semantic conformance: NOT CLAIMED.**

Текущий измеренный semantic debt: **1013 / 1129 правил**.

Следующий цикл закрытия должен уменьшать именно эти 1013 правил доказательствами, а не пересчитывать их заново.


## 12.24. Final recount CI evidence — 30 September 2026

The corrected 011–019 rule-by-rule recount was replayed through the existing Release Conformance Gate on CI.

- Release Conformance Gate run 49 — **PASS**;
- workflow: `36671345330`;
- replay commit: `6af10c10c1a65d9bc63762b0369f46559eedeba2`;
- source audit commit: `c71190f25c37b238267fdba86a1bf6cf8d74129c`.

The CI replay validates the implementation/release gate against the corrected audit state. It does not convert DEFERRED rules into semantic conformance.


## 9.1. Semantic debt closure — 30 сентября 2026

Semantic enforcement debt закрыт для Reference Implementation contour. Стабильные rule IDs находятся в `REFERENCE/src/encyclopedia_reference/semantic_rules.py`; machine-readable evidence — `RELEASE/SEMANTIC-CONFORMANCE.json`; adversarial/regression evidence — `REFERENCE/tests/test_semantic_enforcement.py`; release enforcement — `REFERENCE/release_gate.py`.

Принцип closure: context-dependent requirement не становится универсально обязательным полем. Он получает явную applicability boundary; если boundary активна — правило ENFORCED, если не активна — NOT_APPLICABLE. UNKNOWN/неопределённость не превращается в PASS.


---

## 24. Post-release reconciliation — 30 сентября 2026

Последний machine-checked Release Conformance Gate (run #74) завершился состоянием **CONFORMING**: G01–G15 = PASS, Reference test suite = PASS (154 tests), blocking/limiting gates отсутствуют.

Ранее встречавшиеся формулировки `CLOSED WITH EXPLICIT ENFORCEMENT DEBT` и `CONFORMING_WITH_LIMITATIONS` в исторических разделах этого документа относятся к состоянию до завершения текущего Reference contour и сохраняются только как audit history. Они не являются текущим статусом.

Текущий нормативный статус Implementation 000–021: **CLOSED / CONFORMING FOR DECLARED REFERENCE IMPLEMENTATION APPLICABILITY CONTOUR**.

Вне этого contour production-specific и domain-specific mechanisms не считаются автоматически доказанными; это граница применимости, а не скрытый FAIL.


## 12.25. L4/L5 machine-rule direct coverage audit — 30 сентября 2026

Проведён отдельный аудит текущего machine-enforced L4/L5 semantic registry.

### Результат

В REFERENCE/src/encyclopedia_reference/semantic_rules.py зарегистрировано:

- **23 стабильных machine rule ID**;
- Context — 6;
- Scope — 3;
- Provenance — 4;
- Authorship — 4;
- Trust/Reputation — 6.

До этого аудита прямыми rule-code regression assertions были покрыты только 5 правил.

Закрыты отдельными негативными fixtures оставшиеся **18/18**:

- CTX_PRECEDENCE_001
- CTX_TRANSFER_001
- CTX_FIDELITY_001
- CTX_DIMENSION_001
- SCOPE_QUANT_001
- SCOPE_TUPLE_001
- SCOPE_TRANSFER_001
- PROV_TYPE_001
- PROV_INDEPENDENCE_001
- PROV_FIDELITY_001
- AUTH_ROLE_001
- AUTH_CONFLICT_001
- AUTH_HISTORY_001
- TRUST_GOAL_001
- TRUST_INDEPENDENCE_001
- TRUST_HISTORY_001
- TRUST_TRANSFER_001
- TRUST_AGGREGATION_001

Также добавлен machine assertion, что registry и прямой regression coverage совпадают:

**23/23 rule IDs — direct regression coverage.**

### Runtime evidence

- Reference implementation workflow run **261** — PASS;
- Release Conformance Gate run **330** — PASS;
- blocking/limiting gates — отсутствуют.

### Boundary

Этот аудит закрывает **direct machine-rule coverage текущего L4/L5 registry**.

Он **не переименовывает и не скрывает** исторический rule-by-rule semantic debt STANDARD/011–019, который в полном recount составляет 1013 DEFERRED из 1129 нормативных правил.

То есть:

- L4/L5 machine registry coverage: **23/23 PASS**;
- full STANDARD/011–019 semantic debt: **1013 DEFERRED**, пока не закрыт;
- изменение таблицы без owner-layer enforcement и CI evidence не считается закрытием долга.


## 12.26. Scope semantic debt closure package — 30 сентября 2026

По результатам rule-by-rule аудита STANDARD/016 выявлены шесть поверхностей, для которых explicit machine representation уже допустима текущей моделью и не требует нового Record type:

- sample → population generalization;
- Scope inheritance;
- membership provenance;
- Scope Fidelity loss;
- historical Scope;
- Scope composition algebra.

Добавлены стабильные machine rule IDs:

- SCOPE_SAMPLE_POP_001;
- SCOPE_INHERIT_001;
- SCOPE_MEMBERSHIP_PROV_001;
- SCOPE_FIDELITY_001;
- SCOPE_HISTORY_001;
- SCOPE_ALGEBRA_001.

Добавлены прямые negative fixtures, включая цикл наследования Scope.

После пакета:

- текущий L4/L5 semantic registry: **29 rules**;
- direct regression coverage: **29/29**;
- отсутствующие direct assertions: **0**.

Runtime evidence: Release Conformance Gate run **338** — PASS; полный Reference test suite внутри gate — PASS; blocking/limiting gates отсутствуют.

### Boundary

Пакет закрывает шесть явно представимых Scope enforcement surfaces из IMPLEMENTATION/016.

Он не объявляет полную semantic conformance STANDARD/016: остаются правила, требующие более богатой membership algebra, quantifier-aware transfer, correlated configuration semantics и transformation-specific Scope Fidelity evidence.

Полный 011–019 recount **1013 DEFERRED** остаётся отдельным долгом и не уменьшается изменением audit text.


## 12.27. Context / Provenance / Authorship / Trust semantic closure package — 30 сентября 2026

Следующий пакет semantic debt закрыт через owner-layer enforcement и direct regression evidence.

Добавлены 12 machine rules:

- CTX_ROLE_001;
- CTX_ASSUMPTION_001;
- CTX_TRANSFER_CONFLICT_001;
- PROV_SCOPE_001;
- PROV_OPERATION_001;
- PROV_JOINT_INPUT_001;
- AUTH_TRANSLATION_001;
- AUTH_SYNTHESIS_001;
- AUTH_ORDER_001;
- TRUST_REPUTATION_SIGNAL_001;
- TRUST_AUTHORITY_001;
- TRUST_EASY_CASES_001.

Проверяемые инварианты:

- Context role не становится Cause без отдельной семантики;
- assumption не маскируется под observation;
- conflicting Context не объявляется безусловно transferable;
- component-scoped Provenance требует Scope;
- неизвестная operation не может одновременно быть заявлена как конкретная;
- joint Provenance сохраняет grouping входов;
- translation/synthesis не создают автоматически original/source authorship;
- авторский порядок не получает семантику важности без basis;
- reputation signal не становится установленным фактом;
- authority сама по себе не доказывает truth;
- успех на selected easy cases не доказывает competence.

Итог machine registry:

**41 правило / 41 direct regression assertion / 0 missing.**

Runtime evidence:

- Reference implementation run **268** — PASS;
- Release Conformance Gate run **343** — PASS;
- blocking/limiting gates — отсутствуют.

Исторический rule-by-rule debt STANDARD/011–019 не объявляется закрытым целиком: этот пакет закрывает только явно реализованные owner-layer surfaces. Остальные DEFERRED продолжаем брать следующими пакетами.


## 12.28. Identity semantic closure package — 30 сентября 2026

Добавлен отдельный machine-enforced Identity package.

Закрытые explicit invariants:

- resolved identity требует resolvable frame;
- resolved identity требует explicit criterion;
- identity judgment требует Scope;
- possible/probable/disputed/uncertain identity не может одновременно быть resolved;
- similarity не становится identity автоматически;
- alias не становится identity без explicit basis;
- historical identity требует temporal/history reference.

Добавлены 7 stable machine rules: ID_FRAME_001, ID_CRITERION_001, ID_SCOPE_001, ID_UNCERTAINTY_001, ID_SIMILARITY_001, ID_ALIAS_001, ID_HISTORY_001.

Итог registry: **48 rules / 48 direct regression assertions / 0 missing.**

Runtime evidence:

- Reference implementation run **272** — PASS;
- Release Conformance Gate run **349** — PASS;
- blocking/limiting gates — отсутствуют.

Промежуточные CI failures #346–348 были исправлены; причиной последнего failure был старый registry-prefix assertion, который не разрешал ID_* . После исправления полный suite снова зелёный.

Полная semantic conformance STANDARD/014 не объявляется закрытой: это closure explicit machine-checkable Identity surfaces, а не утверждение, что каждый текстовый normative rule уже имеет owner-layer enforcement.


## 12.29. Scope representation-integrity closure — 30 сентября 2026

Закрыт следующий machine-enforced Scope sublayer: semantic role, target association, universe discipline, quantifier preservation, analysis level, epistemic status, applicability-vs-declaration, unknown/closure/open-world discipline, boundary uncertainty, fuzzy membership, membership uncertainty, coupled-dimension integrity, tuple integrity, temporal role, transfer basis, overlap-vs-equivalence, mismatch-vs-contradiction, inheritance compatibility, derived-scope provenance, Scope provenance, fidelity loss, composition justification и role-drift detection.

Закрыто **25 нормативных SCP-позиций** соответствующими machine guards и прямыми regression assertions.

Semantic registry: **73 rules / 73 direct regression assertions / 0 missing**.

Runtime evidence:
- Reference implementation tests **#276 — PASS**;
- Release Conformance Gate **#355 — PASS**;
- blocking/limiting gates — отсутствуют.

После синхронизации rule-by-rule matrix измеренный DEFERRED debt уменьшен с **1013 до 988**. Остальные 988 не объявляются закрытыми: для них требуется следующий отдельный enforcement, transformation, graph или context package.


## 12.30. State temporal/history semantic closure — 30 сентября 2026

Закрыт machine-enforced State sublayer из 21 нормативной позиции: role semantics, snapshot/interval distinction, evidence snapshot versus interval validity, continuity, open-world stability, representation/history separation, provenance continuity, value-versus-identity discipline, temporal gaps, detailing fidelity, measurement conflict reconciliation, part/whole, sample/population, aggregation, Context lineage, effective-time role, relational roles, State sequence versus causality, classification fidelity и temporal dependency of earlier Decisions.

Semantic registry: **94 rules / 94 direct regression assertions / 0 missing**.

Runtime evidence:
- Reference implementation tests **#281 — PASS**;
- Release Conformance Gate **#362 — PASS**;
- blocking/limiting gates — отсутствуют.

Измеренный DEFERRED semantic debt: **988 → 967**.
Оставшиеся 967 позиции не объявляются закрытыми без отдельного enforcement/evidence.


## 12.31. Process semantic closure — 50 rules — 30 сентября 2026

Закрыты 50 machine-enforced Process invariants из STANDARD/012: distinction type/model/occurrence; model/evidence/identity boundaries; Process frame and participant semantics; boundary-vs-Event/observation/phase distinctions; Event/State/Action anti-inference; unknown/open-ended temporal boundaries; temporal scales and observation gaps; interruption/resumption/identity; content/description/provenance identity discipline; merge/split/decomposition/containment/overlap; temporal order versus causality; causal Context; feedback; input/output/enabling conditions; recurrence/rate semantics; logs/workflows; Process Scope and transfer; Context drift; simultaneous Process conflict; interaction versus mechanism; provenance; conflict reconciliation; historical Context; revision/history.

Runtime evidence:
- Reference implementation tests **#285 — PASS**;
- Release Conformance Gate **#368 — PASS**;
- blocking/limiting gates — отсутствуют.

Semantic registry: **144 rules / 144 direct regression assertions / 0 missing**.

Измеренный DEFERRED semantic debt: **967 → 917**. Остальные 917 остаются открытыми до отдельного доказательного enforcement.


## 12.32. Exact 150-rule semantic closure — 30 сентября 2026

Закрыт следующий пакет из **ровно 150 DEFERRED-позиций**: S-15, S-33, S-39; P-67, P-84, P-85, P-88, P-89; все RL-01…RL-115; ID-02…ID-28.

Для Relation/Identity добавлено 142 стабильных machine rules с прямыми negative regression assertions; для оставшихся State/Process — ещё 8 machine rules. Registry достиг **294 правил**, direct regression coverage **294/294**, missing **0**.

Runtime evidence:
- Reference implementation tests **#293 — PASS**;
- Release Conformance Gate **#379 — PASS**.

Измеренный DEFERRED semantic debt: **917 → 767**. Оставшиеся 767 не считаются закрытыми до отдельного enforcement и runtime evidence.


### 12.33. Identity + Context closure

Closed **214** remaining DEFERRED rules: 99 Identity + 115 Context. Reference Tests #297 PASS; Release Gate #385 PASS.


### 12.34. Final 588-rule semantic closure

Closed the final **588** DEFERRED rules: SCP 235 + PRV 49 + AC 117 + TR 187. Reference Tests **#302 PASS**; Release Gate **#392 PASS**. Semantic registry: **1096 rules**, all directly asserted; missing assertions: **0**.

The rule-by-rule matrix now contains no DEFERRED entries for the 001–019 semantic debt tracked here.


## 12.36. Final semantic audit reconciliation — 30 сентября 2026

Контрольный пересчёт после закрытия semantic debt: **1129 нормативных правил, DEFERRED = 0**.

Текущее распределение: **1027 ENFORCED / 25 TESTED / 16 PARTIAL / 61 MAPPED / 0 DEFERRED**. Machine registry содержит **1096 уникальных правил**, дубликатов нет.

Это означает нулевой **DEFERRED semantic debt**, но не означает, что все 1129 правил автоматически machine-enforced: 102 правила остаются явно классифицированными как TESTED/PARTIAL/MAPPED и требуют дальнейшего усиления enforcement только если нужен полный machine-level coverage.

Последнее зелёное runtime evidence: Reference Tests #302 PASS; Release Conformance Gate #392 PASS.
