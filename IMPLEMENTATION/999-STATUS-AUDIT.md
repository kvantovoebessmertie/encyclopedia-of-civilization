# 999 — Статус и аудит IMPLEMENTATION

## Энциклопедия цивилизации

Версия: 0.1  
Статус: итоговый архитектурный аудит  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Этот документ фиксирует состояние папки `IMPLEMENTATION` после завершения архитектурного комплекта 000–016 и проведения полного аудита.

Документ не является новым нормативным слоем. Он является проверяемым отчётом о состоянии Implementation Architecture.

---

## 2. Полный комплект

В папке должны находиться 17 нормативных артефактов:

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
16. 015 — Operations & Security
17. 016 — Conformance & Release

Дополнительно этот файл является audit/status record и не входит в нормативную цепочку 000–016.

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
    Operations / Security
        ↓
    Conformance / Release

---

## 4. Ten-pass audit

### A1 — Структура

Результат: PASS.

Проверено:

- все 000–016 существуют;
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
- Operations;
- Conformance;
- anti-inference.

### A10 — Language и Consistency

Результат: PASS.

Проверено:

- нормативный текст преимущественно на русском;
- технические английские термины используются как идентификаторы;
- старое имя поля публикационного состояния отсутствует;
- `publication_status` является каноническим;
- старые архитектурные названия не используются как активные поля;
- в документах нет незакрытых технических заглушек;
- дорожная карта 000 согласована с 000–016.

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
- Conditional semantic enforcement 011–018: **LIMITED / требует дальнейшей формализации**
- Полный Standard → Validator semantic conformance: **не заявляется как PASS**

Это не означает дефект архитектуры целиком. Это означает, что нормативные требования, которые намеренно зависят от контекста и материальной значимости, пока не все имеют отдельные машинные диагностические правила.

────────

## 6. Что означает PASS

PASS означает:

> Архитектурный комплект IMPLEMENTATION 000–016 согласован с проверенными Foundation и Standard, имеет определённые границы ответственности, версии, историю, переносимость, тестирование, восстановление, безопасность и conformance-процесс.

PASS не означает:

- истинность всех Claim;
- завершённость всей программной реализации;
- отсутствие будущих архитектурных вопросов;
- отсутствие будущих архитектурных вопросов;
- невозможность дальнейшего развития проекта.

---

## 7. Правило дальнейших изменений

После закрытия 000–016 новые изменения не должны вноситься произвольно.

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

**IMPLEMENTATION 000–016: архитектурно закрыта; полный semantic Standard → Validator conformance пока имеет статус LIMITED.**

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
| S-09 | State имеет разрешимую применимую рамку | context-dependent | Profile/Context-aware Validator | **DEFERRED** | Нельзя требовать один универсальный frame field |
| S-10 | Assertion о State различим от самого State | semantic | Profile/anti-inference | **MAPPED** | Требует различения Record roles |
| S-11 | Observation не становится State автоматически | anti-inference | Validator/tests | **MAPPED** | Нужен отдельный негативный fixture |
| S-12 | Observed X не становится установленным factual State автоматически | anti-inference | Validator/tests | **MAPPED** | Контекстная anti-inference проверка |
| S-13 | Measurement не становится State автоматически | anti-inference | Validator/tests | **MAPPED** | Нужен негативный fixture |
| S-14 | State различим от Event | semantic | Type/Profile | **MAPPED** | Типы уже различены |
| S-15 | Различие States не определяет Event count/mechanism/time/cause | anti-inference | Validator/tests | **DEFERRED** | Требует графа/временного контекста |
| S-16 | Event не означает полностью известное результирующее State | anti-inference | Validator/tests | **MAPPED** | Негативная интеграционная проверка |
| S-17 | State различим от Process | semantic | Type/Profile | **MAPPED** | Типы различены |
| S-18 | State не становится Result/Goal/expected/normative State автоматически | anti-inference | Validator/tests | **MAPPED** | Роль должна быть явной |
| S-19 | Фактическая/желаемая/ожидаемая/требуемая State role различимы | context-dependent | Profile | **DEFERRED** | Требует role model |
| S-20 | Недоступная точная временная информация не делает State timeless | anti-inference | Validator/tests | **MAPPED** | Связано с time semantics |
| S-21 | Snapshot и interval semantics различимы | context-dependent | Schema/Time profile | **DEFERRED** | Нужна точная семантика time representation |
| S-22 | Evidence snapshot не расширяется до interval validity | anti-inference | Validator/Publication | **DEFERRED** | Нужны Evidence/temporal inputs |
| S-23 | Повторное наблюдение не доказывает непрерывную устойчивость | anti-inference | Validator/tests | **DEFERRED** | Требует временного графа |
| S-24 | Отсутствие evidence об изменении не доказывает устойчивость | anti-inference | Validator/tests | **DEFERRED** | Open-world inference |
| S-25 | Open-ended validity не означает бесконечность | anti-inference | Validator/tests | **MAPPED** | Общий time anti-inference |
| S-26 | Current State не заменяет historical State | history | Resolver/Validator L3/L5 | **ENFORCED** | Исторические refs/version discipline |
| S-27 | Изменение представления не означает изменение historical State | anti-inference | History/Recovery | **DEFERRED** | Требует lineage/change context |
| S-28 | Identity representation различима от identity/continuity State | identity/history | Identity/Validator | **MAPPED** | Правило закреплено архитектурно |
| S-29 | Разное provenance не означает разные States автоматически | anti-inference | Validator/tests | **DEFERRED** | Требует semantic comparison |
| S-30 | Одинаковые значения не доказывают identity/continuity | anti-inference | Validator/tests | **DEFERRED** | Требует Identity context |
| S-31 | Одинаковые значения после перерыва не образуют автоматически один interval | history | Validator/Recovery | **DEFERRED** | Требует temporal continuity evidence |
| S-32 | Разные значения не требуют новой fundamental State Entity | architecture | Profile | **MAPPED** | Core Entity proliferation запрещено |
| S-33 | Semantics measurement/property разрешима при material ambiguity | context-dependent | Profile | **DEFERRED** | Зависит от domain semantics |
| S-34 | Detailing не выдумывает property/value/precision/scope/continuity | anti-inference | Validator/Transformation tests | **DEFERRED** | Нужен input/output comparison |
| S-35 | Composite State не означает полноту сверх представленного | anti-inference | Validator/tests | **MAPPED** | Не следует из structural validity |
| S-36 | Partial State не становится complete незаметно | anti-inference | Completion/Transformation | **ENFORCED** | completion_status разделён |
| S-37 | Unknown State semantics различима от false/zero/absent/etc. | unknown-discipline | Schema/Profile/Validator | **MAPPED** | Требует explicit unknown representation |
| S-38 | Not applicable не кодируется автоматически как false/zero/absent/unknown | unknown-discipline | Validator/tests | **DEFERRED** | Нужна semantic null discipline |
| S-39 | Qualitative classification сохраняет definitions/thresholds когда применимо | context-dependent | Profile | **DEFERRED** | Domain-specific |
| S-40 | Continuous change не требует бесконечных discrete States/Events | architecture | Profile | **MAPPED** | Не локальная ошибка |
| S-41 | State category не является universal ontology автоматически | anti-inference | Profile/Validator | **MAPPED** | Type/Profile scope |
| S-42 | Concurrent measurements не конфликтуют только из-за coexistence | anti-inference | Validator/tests | **DEFERRED** | Нужен measurement context |
| S-43 | State conflict не утверждается без temporal/semantic/measurement/scope/context reconciliation | semantic | Validator L4/L5 | **DEFERRED** | Нужна conflict reconciliation context |
| S-44 | Part State не становится whole State автоматически | anti-inference | Validator/tests | **DEFERRED** | Part-whole graph required |
| S-45 | Sample State не становится population State | anti-inference | Validator/tests | **DEFERRED** | Scope-aware check |
| S-46 | Aggregate State не означает identical individual States | anti-inference | Validator/tests | **DEFERRED** | Aggregation semantics required |
| S-47 | Context of State не изменяется незаметно | history/context | Context/History | **DEFERRED** | Нужен context lineage |
| S-48 | Institutional effective time различим от decision/publication/registration time | temporal | Schema/Validator | **DEFERRED** | Time-role mapping not yet explicit |
| S-49 | Relational State сохраняет significant role structure | semantic | Profile/Validator | **DEFERRED** | Requires relation-role semantics |
| S-50 | State transition различим от State | semantic | Type/Profile | **MAPPED** | Transition not represented as State |
| S-51 | Sequence of States не становится causal chain/full Process автоматически | anti-inference | Validator/tests | **DEFERRED** | Requires process/causal context |
| S-52 | Absent/unknown/not detected/not recorded/not applicable различимы | unknown-discipline | Schema/Profile/Validator | **MAPPED** | Общий unknown discipline |
| S-53 | Observed/measured/computed/inferred/modelled/reconstructed provenance различим | provenance | Provenance/Profile | **DEFERRED** | Требует provenance vocabulary |
| S-54 | Classification не стирает material original properties/values | transformation | Migration/Publication | **DEFERRED** | Fidelity check |
| S-55 | External labels не определяют canonical State semantics автоматически | anti-inference | Import/Validator | **MAPPED** | Import semantics |
| S-56 | Normal/safe/valid/quality не являются State semantics автоматически | anti-inference | Profile/Validator | **MAPPED** | Не выводить оценку из State |
| S-57 | State может coexist с Process/Event | semantic | Type/Profile | **MAPPED** | Совместимость типов |
| S-58 | State representation может использоваться в Result/reference/Goal при явном role distinction | semantic | Profile/Builder | **MAPPED** | Derived representation boundary |
| S-59 | Later State не входит ретроактивно в basis earlier Decision | history | Validator/History | **DEFERRED** | Нужен temporal dependency graph |
| S-60 | Сохраняются material subject/content/measurement/frame/scope/context/units/uncertainty/provenance | semantic | Profile + Transformation | **DEFERRED** | Composite fidelity rule |
| S-61 | Structural/semantic conformity различима от historical integrity, validity, certainty, quality, fidelity | anti-inference | Validator/Conformance | **MAPPED** | Общий anti-inference invariant |
| S-62 | Profile может усиливать, но не ослаблять Core requirements | architecture | Schema/Profile registry | **ENFORCED** | Profile compatibility rule |
| S-63 | Material uncertainty/provenance/frame/scope/measurement/context остаются resolvable | context-dependent | Profile/Transformation | **DEFERRED** | Требует materiality/applicability context |

## 5.4. Rule-by-rule matrix — STANDARD/012 Process

| ID | Нормативное правило (кратко) | Класс | Owner | Статус |
|---|---|---|---|---|
| P-01 | Process как семантическая конструкция | context-dependent | Profile | MAPPED |
| P-02 | Специализированная Process Record не обязательна универсально | architecture | Profile | MAPPED |
| P-03 | type/model/occurrence различимы | anti-inference | Profile/Validator | MAPPED |
| P-04 | type не становится model/occurrence автоматически | anti-inference | Validator/tests | DEFERRED |
| P-05 | model не становится type/occurrence/historical evidence | anti-inference | Validator/tests | DEFERRED |
| P-06 | identity модели отличима от identity occurrence | identity | Identity/Validator | DEFERRED |
| P-07 | Process Content не становится Process type | anti-inference | Profile | MAPPED |
| P-08 | generic Process knowledge не является historical evidence автоматически | anti-inference | Validator/tests | DEFERRED |
| P-09 | не всякая temporal sequence является Process | classification | Profile/ingest | MAPPED |
| P-10 | конкретный Process имеет Process Content | structural | Schema + L4 | ENFORCED |
| P-11 | конкретный Process имеет participating frame | semantic | Context-aware Validator | DEFERRED |
| P-12 | participating frame может быть distributed/multi-participant | semantic | Profile | MAPPED |
| P-13 | participating frame и Context различимы | semantic | Profile/Validator | DEFERRED |
| P-14 | роли участников сохраняются при material significance | context-dependent | Profile/Transformation | DEFERRED |
| P-15 | достаточное semantic attribution Process | semantic | Validator/Profile | DEFERRED |
| P-16 | attribution не требует новой Core Entity | architecture | Profile | MAPPED |
| P-17 | Process occurrence имеет temporal/process frame | context-dependent | Profile/Validator | DEFERRED |
| P-18 | наличие Process Record не доказывает точное occurrence | anti-inference | Validator/tests | MAPPED |
| P-19 | Claim о Process различим от Process | anti-inference | Type/Profile | MAPPED |
| P-20 | existence не раскрывает internal dynamics/mechanism | anti-inference | Validator/tests | DEFERRED |
| P-21 | Process различим от Event | semantic | Type/Profile | MAPPED |
| P-22 | duration не определяет Event vs Process | anti-inference | Profile | MAPPED |
| P-23 | Process boundary не становится Event автоматически | anti-inference | Validator/tests | DEFERRED |
| P-24 | observation boundary не становится Process boundary | anti-inference | Validator/tests | DEFERRED |
| P-25 | phase boundary не становится Event | anti-inference | Validator/tests | DEFERRED |
| P-26 | Process не требует discrete Event decomposition | architecture | Profile | MAPPED |
| P-27 | Event не означает Process/mechanism автоматически | anti-inference | Validator/tests | DEFERRED |
| P-28 | State различим от Process | semantic | Type/Profile | MAPPED |
| P-29 | State sequence не устанавливает Process/mechanism/continuity | anti-inference | Validator/tests | DEFERRED |
| P-30 | Process не требует net State change | semantic | Profile | MAPPED |
| P-31 | Action различим от Process | semantic | Type/Profile | MAPPED |
| P-32 | Activity label не определяет ontology автоматически | anti-inference | Import/Profile | MAPPED |
| P-33 | Process не требует Actor attribution | architecture | Profile | MAPPED |
| P-34 | Action не доказывает cause/control Process | anti-inference | Validator/tests | DEFERRED |
| P-35 | Process не становится Result/Objective/Procedure | anti-inference | Validator/tests | MAPPED |
| P-36 | observed direction/endpoint не доказывают objective/purpose | anti-inference | Validator/tests | DEFERRED |
| P-37 | Procedure/workflow definition различим от occurrence | semantic | Profile | MAPPED |
| P-38 | occurrence различим от mechanism model | semantic | Profile | MAPPED |
| P-39 | unknown start/end не заменяется invented exact boundaries | unknown-discipline | Validator/Transformation | DEFERRED |
| P-40 | open-ended Process не означает permanently ongoing | anti-inference | Validator/tests | DEFERRED |
| P-41 | multiple temporal scales сохраняются | temporal | Profile/Transformation | DEFERRED |
| P-42 | observation gaps не доказывают interruption/continuity | anti-inference | Validator/tests | DEFERRED |
| P-43 | interruption не означает termination | anti-inference | Validator/tests | DEFERRED |
| P-44 | resumption не означает same Process identity | identity | Identity/Validator | DEFERRED |
| P-45 | same Process Content не означает same identity | identity | Identity/Validator | DEFERRED |
| P-46 | different descriptions не означают different Processes | identity | Identity/Validator | DEFERRED |
| P-47 | representation identity отличима от Process identity | identity | Identity/Validator | MAPPED |
| P-48 | different provenance не означает different Process | anti-inference | Validator/tests | DEFERRED |
| P-49 | merge/split/branching не устанавливают continuity автоматически | identity/history | Validator | DEFERRED |
| P-50 | decomposition не выдумывает stages/mechanisms/links | anti-inference | Transformation | DEFERRED |
| P-51 | composite Process не означает full decomposition | anti-inference | Validator/tests | MAPPED |
| P-52 | temporal containment не означает subprocess | anti-inference | Validator/tests | DEFERRED |
| P-53 | overlap не означает part-of | anti-inference | Validator/tests | DEFERRED |
| P-54 | допустимые decompositions не являются contradiction | anti-inference | Validator/tests | DEFERRED |
| P-55 | phase labels не определяют ontology | anti-inference | Profile | MAPPED |
| P-56 | temporal order не доказывает causality | anti-inference | Validator/tests | DEFERRED |
| P-57 | causal/mechanistic relations сохраняют provenance/uncertainty/Scope/Context | semantic | Validator/Provenance | DEFERRED |
| P-58 | observed pattern не доказывает feedback mechanism | anti-inference | Validator/tests | DEFERRED |
| P-59 | inputs/outputs/conditions не universal mandatory fields | architecture | Schema/Profile | MAPPED |
| P-60 | input не доказывает sole/full causation | anti-inference | Validator/tests | DEFERRED |
| P-61 | output не становится Result/Effect автоматически | anti-inference | Validator/tests | DEFERRED |
| P-62 | enabling condition не доказывает occurrence | anti-inference | Validator/tests | DEFERRED |
| P-63 | recurring cycles не доказывают identical identity | identity | Validator | DEFERRED |
| P-64 | rate/intensity/direction не определяют identity автоматически | anti-inference | Validator/tests | DEFERRED |
| P-65 | point rate не становится constant interval rate | temporal | Validator/tests | DEFERRED |
| P-66 | rate×duration не становится cumulative change без assumptions | semantic | Validator/Profile | DEFERRED |
| P-67 | lifecycle labels сохраняют domain semantics | context-dependent | Profile | DEFERRED |
| P-68 | completion не означает success/objective achievement | anti-inference | Validator/tests | MAPPED |
| P-69 | Natural Process не требует Actor | architecture | Profile | MAPPED |
| P-70 | logs/measurements не являются Process автоматически | anti-inference | Validator/tests | DEFERRED |
| P-71 | workflow/rule не является occurrence автоматически | anti-inference | Validator/tests | DEFERRED |
| P-72 | Process Scope различим от observation/data Scope | semantic | Scope-aware Validator | DEFERRED |
| P-73 | local/sample/aggregate semantics не становятся global/population/individual | anti-inference | Scope Validator | DEFERRED |
| P-74 | Process Context не drift | history/context | Context/History | DEFERRED |
| P-75 | simultaneous Processes не противоречат автоматически | anti-inference | Validator/tests | DEFERRED |
| P-76 | interaction не доказывает full causal mechanism | anti-inference | Validator/tests | DEFERRED |
| P-77 | Process provenance types remain resolvable | provenance | Provenance/Profile | DEFERRED |
| P-78 | unknown/non-observed различим от absence of Process | unknown-discipline | Validator/Profile | MAPPED |
| P-79 | negation occurrence не создаёт Process automatically | anti-inference | Validator/tests | MAPPED |
| P-80 | Process conflict требует time/scope/context/granularity/mechanism reconciliation | semantic | Validator L4/L5 | DEFERRED |
| P-81 | external labels не определяют canonical Process semantics | anti-inference | Import/Profile | MAPPED |
| P-82 | historical Process не наследует current model/context silently | history | Resolver/Validator | DEFERRED |
| P-83 | model/type revision не меняет historical Process автоматически | history | Versioning/Validator | DEFERRED |
| P-84 | Process-State link не становится causal автоматически | anti-inference | Validator/tests | DEFERRED |
| P-85 | start/interrupt/end Event не становится causal automatically | anti-inference | Validator/tests | DEFERRED |
| P-86 | material Process content/frame/context/time/continuity/scope/provenance/uncertainty preserved | fidelity | Transformation | DEFERRED |
| P-87 | structural conformance различима от occurrence/mechanism/causal certainty/quality/fidelity | anti-inference | Conformance/Validator | MAPPED |
| P-88 | Profile не ослабляет Core requirements | architecture | Registry/Validator | DEFERRED |
| P-89 | material uncertainty/provenance/frame/context/scales/continuity/scope resolvable | context-dependent | Profile/Transformation | DEFERRED |