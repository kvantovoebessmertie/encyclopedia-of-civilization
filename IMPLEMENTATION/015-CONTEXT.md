# 015 — Контекст

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: закрытая архитектурная спецификация  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Настоящий документ определяет реализационный контракт для Record типа `context`.

Он переводит нормативные требования `STANDARD/015-CONTEXT.md` в проверяемые границы между:

- Record Envelope;
- Content Profile;
- JSON Schema;
- Semantic Validator;
- Resolver;
- Migration;
- Publication;
- Recovery;
- anti-inference tests.

Документ не создаёт новую фундаментальную сущность только потому, что существует тип Record `context`.

Главная цель:

> сохранить контекст как target-relative, исторически разрешимый и эпистемически честный объект представления, не превращая его в универсальный контейнер всех связанных фактов.

---

## 2. Нормативная иерархия

Порядок зависимости:

```
FOUNDATION
    ↓
STANDARD/015-CONTEXT
    ↓
IMPLEMENTATION/000
    ↓
IMPLEMENTATION/001 Envelope
    ↓
IMPLEMENTATION/004 Content Profiles
    ↓
IMPLEMENTATION/005 Record Schema
    ↓
IMPLEMENTATION/006 Validator
    ↓
015 Context Implementation Contract
    ↓
Resolver / Migration / Publication / Recovery
```

Настоящий документ НЕ переопределяет `STANDARD/015-CONTEXT.md`.

Если реализационное решение противоречит Standard, исправляется реализационный слой или оформляется отдельное архитектурное решение.

---

## 3. Область ответственности

015 отвечает за реализацию:

- структуры Context Content;
- target linkage;
- contextual dimensions и values;
- epistemic status;
- temporal applicability;
- Scope/Context distinction;
- Context/State/Frame/Participant distinction;
- Context inheritance;
- override и precedence;
- composition;
- transferability;
- Context Fidelity;
- historical resolution;
- anti-inference safeguards.

015 НЕ отвечает за:

- истинность Claim;
- общую семантику Scope;
- общую семантику Provenance;
- общую identity resolution;
- причинность;
- доказательное значение Source;
- конкретную СУБД;
- конкретный UI;
- публикационный формат.

---

## 4. Каноническая структура Record

Record типа `context` использует общий Envelope.

Минимальный Content Contract:

```text
content
├── context_content      required
└── target_ref           required
```

Допустимые дополнительные элементы текущей Schema:

```text
scope_ref
epistemic_status
precondition_refs
```

При этом:

- `record_id` и `record_version` относятся к самой Context Record;
- `target_ref` указывает, что именно контекстуализируется;
- Envelope `context` является общей ссылкой на Context Record и НЕ равен автоматически Content этой Record;
- `scope_ref` ограничивает область применимости и НЕ превращает Scope в Context;
- `precondition_refs` не превращают каждое условие в Precondition автоматически.

---

## 5. Минимальная обязательность

### 5.1 Structural required

Schema обязана требовать:

- `content`;
- `context_content`;
- `target_ref`.

### 5.2 Semantic required

Target и Context Content являются обязательными, потому что Context без target-relative semantics теряет основную функцию типа.

### 5.3 Contextually required

Следующие сведения НЕ должны становиться универсальными required-полями:

- время;
- Scope;
- epistemic status конкретного измерения;
- preconditions;
- dimensions;
- inheritance;
- transferability;
- fidelity;
- composition.

Их необходимость зависит от применимости и материальной значимости.

---

## 6. Почему `context_content` не имеет универсальной жёсткой формы

`context_content` в текущей Schema намеренно остаётся структурно открытым.

Причина:

- Context может содержать разные доменные dimensions;
- один универсальный список dimensions создавал бы ложную онтологию;
- одинаковые названия dimensions могут иметь разные значения;
- часть Context может быть неизвестна;
- domain Profile может требовать дополнительную структуру.

Это НЕ означает `any = semantic freedom`.

Структурные и семантические ограничения распределяются между Schema, Type Profile и Validator.

---

## 7. Target-relative semantics

Context всегда интерпретируется относительно target.

```text
Context C
    ↓
target_ref
```

Следовательно:

```text
Context of Record A
≠
Context of every component of A
```

Если Context относится только к subclaim, relation, phase, measurement или другому компоненту, ссылка должна быть адресована на этот target либо через разрешимый структурный механизм.

Validator НЕ должен распространять Context на соседние Record только по близости ссылок.

---

## 8. Context Record и inline Context

Допускаются две архитектурные формы:

1. Context представлен отдельной Record типа `context`.
2. Контекст представлен ссылкой/значением внутри другого типа, если это допускает его Profile.

Они не являются автоматически одним и тем же объектом.

Материализация Context в отдельную Record оправдана, если необходимы:

- повторное использование;
- собственная история;
- provenance;
- dispute;
- composition;
- отдельное цитирование;
- transferability analysis.

---

## 9. Context ≠ State

Validator и Profile НЕ должны выводить:

```text
State → Context
Context → State
```

автоматически.

Одна фактическая величина может играть разные роли.

Например:

```text
temperature = 25°C

State of Tank A
Context of Process P
```

Семантическая роль определяется target и соответствующим отношением, а не самим значением.

---

## 10. Context ≠ Scope

```text
Context → при каких условиях
Scope   → к какому множеству/границе применяется
```

Одна и та же характеристика может участвовать в обеих семантиках, но роли не должны сливаться.

Validator НЕ должен считать:

- Context равным Scope;
- наличие `scope_ref` доказательством полноты Context;
- отсутствие Scope доказательством universal applicability.

---

## 11. Context ≠ Frame

Factual Context не выбирает semantic/reference frame автоматически.

Например:

```text
France, 1804
```

не означает автоматически:

```text
French legal frame
```

Frame должен быть представлен своим разрешимым механизмом.

---

## 12. Context ≠ Participant

Присутствие Entity в окружении Event/Process не создаёт Participant автоматически.

Если роль Participant материально значима, она должна быть представлена отдельно.

Context может содержать условие, в котором Participant действует, но это разные семантические роли.

---

## 13. Context ≠ Assumption / Precondition

Assumption — принятая или stipulated предпосылка рассуждения.

Precondition — условие, необходимое для определённого действия/процесса.

Context — условия, относительно которых target получает определённый смысл, наблюдается, измеряется или применяется.

Одно значение может участвовать в нескольких ролях, но роли должны оставаться разрешимыми.

---

## 14. Context ≠ Cause

Наличие contextual factor НЕ создаёт причинность.

```text
failure under high humidity
≠
humidity caused failure
```

Causal interpretation принадлежит Relation/causal machinery и не выводится из Context.

---

## 15. Context ≠ Evidence

Context может быть подтверждён Evidence, но:

```text
Context
≠
Evidence
```

Source и Evidence Use не должны появляться автоматически только потому, что Context содержит factual values.

---

## 16. Context ≠ Provenance

Context отвечает за условия относительно target.

Provenance отвечает за происхождение representation.

Они могут ссылаться друг на друга, но не являются взаимозаменяемыми.

---

## 17. Epistemic status

Текущая Schema поддерживает общий статус Context:

- `known`;
- `unknown`;
- `partial`;
- `disputed`.

Этот статус относится к Context Record в целом.

Он НЕ означает автоматически, что каждый dimension или value имеет тот же статус.

Если внутри Context материально важно различать:

- observed;
- measured;
- reported;
- assumed;
- inferred;
- modeled;
- reconstructed;

это различие должно сохраняться на соответствующем уровне Profile/Content/Provenance.

Нельзя поднимать локальный статус на весь Context без основания.

---

## 18. Unknown discipline

Context implementation обязана сохранять различие:

```text
unknown
≠ absent
≠ not_applicable
≠ not_observed
≠ not_recorded
```

Отсутствие Context НЕ означает:

- universal applicability;
- context independence;
- falsehood;
- invalidity.

В то же время отсутствие Context не должно автоматически блокировать использование знания, если конкретный Standard/Profile не делает Context обязательным.

---

## 19. Temporal semantics

Основное время действительности Context задаётся общим Envelope `valid_time`, когда оно применимо.

Технические времена:

```text
created_at
updated_at
```

не должны интерпретироваться как время Context автоматически.

Observation/measurement/source times при необходимости должны приходить через соответствующие Provenance/Evidence/Source механизмы.

Historical Context должен оставаться разрешимым к исторической версии Record.

Текущий Context не должен молча подменять исторический Context.

---

## 20. Context composition

Context может быть составным:

```text
C = C1 + C2 + ... + Cn
```

Но композиция не означает автоматически:

- независимость dimensions;
- совместимость values;
- полноту;
- отсутствие конфликтов.

Если Context составлен из нескольких Record, каждая составляющая должна сохранять собственную identity и provenance.

---

## 21. Dependency между dimensions

Dimensions могут зависеть друг от друга.

Пример:

```text
software_version = V
plugin_version   = P
```

не обязательно имеет смысл как две независимые величины.

Validator не должен считать Context согласованным только потому, что каждое поле по отдельности прошло Schema.

Проверка совместимости принадлежит Context-aware Validator/Profile, когда необходимый контекст существует.

---

## 22. Inheritance

Context может наследоваться от более общего Context.

Но:

```text
inheritance
≠
copy
```

При наследовании должны быть разрешимы:

- parent Context;
- target;
- inherited dimensions;
- local additions;
- local overrides;
- effective result;
- historical versions.

Не допускается скрытое копирование Context в новую Record без указания происхождения.

---

## 23. Override и precedence

Если несколько Context применимы одновременно, система может иметь precedence rules.

Precedence должна быть:

- явной;
- версионируемой;
- воспроизводимой;
- ограниченной применимым Profile.

Validator не должен самовольно выбирать «более конкретный» Context без нормативного правила.

Если precedence неизвестна, результат должен быть `indeterminate` или сохранять конфликт.

---

## 24. Context conflict

Конфликт двух Context не должен определяться только различием значений.

Различия могут быть совместимыми при:

- разных time intervals;
- разных Scope;
- разных targets;
- разных versions;
- разных semantic dimensions.

Conflict устанавливается только после разрешения релевантного Context/Scope/Time.

Если разрешение невозможно, система сохраняет conflict/indeterminate, а не выбирает значение автоматически.

---

## 25. Context transfer

Перенос знания из Context A в Context B не следует из:

- similarity;
- textual overlap;
- common target;
- same domain;
- same Scope;
- same dimension names.

Transferability должна быть:

- явно обоснована;
- условной;
- частичной;
- либо неизвестной,

если Standard/Profile не устанавливает более сильное правило.

---

## 26. Context Fidelity

Fidelity — сохранение материально значимой Context semantics при:

- translation;
- summary;
- compression;
- migration;
- import/export;
- publication;
- recovery.

Успешное преобразование Record НЕ означает автоматически сохранённую Context Fidelity.

Если transformation удаляет неизвестный или материально значимый Context, результат не должен объявляться семантически эквивалентным без основания.

---

## 27. Anti-inference boundary

Validator не должен автоматически выводить из Context:

- причинность;
- универсальность;
- полноту;
- applicability;
- transferability;
- identity;
- truth;
- State;
- Participant;
- Scope;
- Frame;
- Evidence.

Context может быть входом для таких проверок, но не является достаточным основанием сам по себе.

---

## 28. Resolver boundary

Context Resolver может отвечать за:

- разрешение target;
- разрешение parent Context;
- построение effective Context;
- применение precedence;
- проверку temporal compatibility;
- обнаружение конфликтов;
- построение transferability/fidelity result.

Resolver НЕ должен:

- менять Record;
- создавать отсутствующие значения;
- заменять unknown на default;
- выбирать конфликтующую сторону без правила.

---

## 29. Validator ownership

Проверки делятся на уровни.

### L1 — Schema

Проверяет:

- envelope;
- `record_type=context`;
- `content` object;
- required `context_content`;
- required `target_ref`;
- формы `scope_ref`, `precondition_refs`;
- допустимые `epistemic_status`.

### L2 — Type/Profile

Проверяет:

- соответствие Context Content Profile;
- запрет неизвестных критических полей;
- профильные ограничения;
- допустимые расширения.

### L3 — Reference / History

Проверяет:

- существование target;
- разрешимость version при её указании;
- историческую совместимость;
- отсутствие молчаливой подмены текущей версией;
- разрешимость parent/related Context при наличии.

### L4 — Semantic Context

Проверяет при наличии условий применимости:

- role distinction;
- Context/Scope compatibility;
- dimension semantics;
- Context conflict;
- inheritance;
- precedence;
- target granularity;
- contextual applicability.

### L5 — Transformation / Integration

Проверяет:

- Context Fidelity;
- migration preservation;
- publication preservation;
- recovery preservation;
- transferability;
- anti-inference regressions.

---

## 30. Что уже проверяется текущей Schema

В текущем `IMPLEMENTATION/005-RECORD-SCHEMA.json` для `context` уже структурно закреплено:

- `context_content` — required;
- `target_ref` — required;
- `scope_ref` — структурная ссылка;
- `epistemic_status` — перечисленный набор значений;
- `precondition_refs` — массив структурных ссылок;
- `additionalProperties: false`.

Это является реальной structural conformance.

Не следует объявлять эти поля доказательством полного semantic conformance.

---

## 31. Что НЕ следует искусственно добавлять в Schema

Без отдельного архитектурного основания не следует делать универсально required:

- `time`;
- `scope_ref`;
- `frame_ref`;
- `state_ref`;
- `participant_ref`;
- `cause_ref`;
- `evidence_ref`;
- `provenance_ref`;
- `transferability`;
- `fidelity`;
- `inheritance`;
- `precedence`.

Их наличие зависит от конкретного Context и применимого Profile.

---

## 32. Матрица enforcement

| Семейство правил | Класс | Owner | Статус |
|---|---|---|---|
| базовая форма Context | structural | Schema | ENFORCED |
| target_ref | structural | Schema + L3 | ENFORCED |
| context_content | structural | Schema | ENFORCED |
| scope/precondition reference shape | structural | Schema | ENFORCED |
| epistemic_status vocabulary | structural | Schema | ENFORCED |
| target resolution | reference | L3 | ENFORCED / зависит от доступности graph |
| historical target resolution | history | L3 | ENFORCED / при version-sensitive refs |
| Context ≠ Scope | semantic | L4 | MAPPED |
| Context ≠ State | anti-inference | L4/tests | MAPPED |
| Context ≠ Cause | anti-inference | L4/tests | MAPPED |
| Context ≠ Evidence | anti-inference | L4/tests | MAPPED |
| unknown ≠ universal applicability | anti-inference | L4/tests | MAPPED |
| inheritance | context-dependent | L4 | DEFERRED |
| precedence | context-dependent | L4 | DEFERRED |
| conflict reconciliation | context-dependent | L4 | DEFERRED |
| transferability | context-dependent | L4/L5 | DEFERRED |
| Context Fidelity | transformation | L5 | DEFERRED |
| historical Context preservation | history/transformation | L3/L5 | PARTIAL |
| dimension dependency | context-dependent | L4 | DEFERRED |
| context independence | anti-inference | L4 | DEFERRED |

`DEFERRED` здесь означает enforcement debt, а НЕ нарушение архитектуры.

---

## 33. Negative / adversarial tests

Минимальный набор:

- Context без `target_ref` → fail.
- Context без `context_content` → fail.
- Неверный `epistemic_status` → fail.
- Неразрешимый target → fail или indeterminate по причине недоступности.
- Historical target не должен разрешаться на current version.
- Unknown Context не должен становиться universal.
- Context не должен становиться Cause автоматически.
- Context не должен становиться Evidence автоматически.
- Context не должен становиться State автоматически.
- Context не должен становиться Scope автоматически.
- Два Context с разными time intervals не должны считаться конфликтом только из-за разных values.
- Два Context для разных targets не должны считаться конфликтом.
- Inherited Context не должен молча становиться локальным фактом.
- Translation, потерявшая material Context, не должна заявлять полную fidelity.
- Migration не должна удалять unknown Context.
- Publication не должна заменять исторический Context текущим.

---

## 34. Acceptance tests

- C01 — минимальный валидный Context проходит Schema.
- C02 — отсутствие `target_ref` отклоняется.
- C03 — отсутствие `context_content` отклоняется.
- C04 — неизвестный `epistemic_status` отклоняется.
- C05 — валидный `scope_ref` сохраняется.
- C06 — valid `precondition_refs` сохраняются.
- C07 — неизвестный target не маскируется под valid target.
- C08 — version-specific target сохраняется.
- C09 — historical target не заменяется current target.
- C10 — unknown Context не становится universal Context.
- C11 — Context не создаёт автоматически Cause.
- C12 — Context не создаёт автоматически Evidence.
- C13 — Context не создаёт автоматически State.
- C14 — Context не создаёт автоматически Scope.
- C15 — Context для разных targets не конфликтует автоматически.
- C16 — временно непересекающиеся Context не конфликтуют автоматически.
- C17 — inherited Context сохраняет parent provenance.
- C18 — transformation не теряет material Context без фиксации потери.
- C19 — publication сохраняет Context и его version linkage.
- C20 — recovery сохраняет Context identity, target и historical state.

---

## 35. Stress tests

- C21 — тысячи Context Record.
- C22 — глубокая цепочка inheritance.
- C23 — циклическая ссылка Context → Context.
- C24 — большой набор dimensions.
- C25 — большой reference graph.
- C26 — conflicting Contexts.
- C27 — overlapping temporal intervals.
- C28 — частично неизвестный Context.
- C29 — массовая migration.
- C30 — массовый publication/export.
- C31 — translation с потерей Context.
- C32 — offline recovery.
- C33 — Unicode и локализованные dimension names.
- C34 — повреждённый Context Record.
- C35 — повторная проверка с теми же версиями.

Циклические зависимости не должны приводить к бесконечной рекурсии Resolver/Validator.

---

## 36. Error / finding model

Где Context-specific machine findings уже формализуются, должны использоваться стабильные коды.

Минимально рекомендуемые семейства:

```text
CTX_SCHEMA_*
CTX_REFERENCE_*
CTX_HISTORY_*
CTX_SEMANTIC_*
CTX_INFERENCE_*
CTX_FIDELITY_*
CTX_TRANSFER_*
```

Код ошибки не должен становиться новым семантическим полем Record.

Если требование пока не имеет machine-diagnostic rule, отсутствие кода НЕ является основанием притворяться, что оно enforced.

---

## 37. Determinism

При одинаковых:

- Record versions;
- Schema version;
- Type Profile version;
- Standard versions;
- Validator rule-set;
- Resolver configuration;
- external inputs;

результат Context validation должен быть эквивалентным.

Если внешний input недоступен, результат должен отражать `indeterminate`, `unverified` или иной явно определённый статус, а не `pass`.

---

## 38. Security

Context Content является недоверенными данными.

Resolver/Validator НЕ должен:

- выполнять Context как код;
- исполнять expression из `context_content`;
- автоматически загружать внешние ресурсы;
- доверять URI как инструкции;
- допускать path traversal;
- бесконечно обходить Context graph.

---

## 39. Migration

Migration Context обязана сохранять:

- `record_id`;
- `record_version`;
- `target_ref`;
- `context_content`;
- unknown semantics;
- epistemic status;
- Scope linkage;
- precondition linkage;

если эти элементы присутствуют в исходной версии.

Если fidelity не может быть доказана, migration result не должен объявляться эквивалентным без ограничения.

---

## 40. Publication

Publication Builder должен:

- сохранять Context при его материальной релевантности;
- сохранять ссылки на конкретные версии;
- не превращать Context в universal metadata;
- не удалять unknown без явной политики;
- не менять Context semantics при переводе;
- фиксировать потерю Context при lossy transformation.

---

## 41. Recovery

Recovery должен проверять как минимум:

```text
Context identity
target resolution
version resolution
unknown preservation
scope linkage
precondition linkage
historical Context
```

Восстановление не должно заменять Context текущей версией или реконструированным значением без маркировки.

---

## 42. Reference implementation boundary

Эталонная реализация обязана поддерживать Context как первый-class зарегистрированный Type Profile в общей схеме.

Но она НЕ обязана реализовывать сразу все:

- domain-specific dimensions;
- inheritance semantics;
- precedence engines;
- transferability models;
- fidelity analysis.

Эти функции вводятся вертикальными срезами при наличии соответствующих правил и fixtures.

---

## 43. Conformance policy

Для Context необходимо различать:

### Structural conformance

Schema и Profile правильно представляют обязательную структуру.

Текущий статус: **PASS**.

### Reference conformance

Ссылки и версии разрешаются по правилам Resolver.

Текущий статус: **PARTIAL**, потому что часть graph/history checks зависит от реализации Resolver и доступности полного graph.

### Semantic conformance

Все применимые Context rules проверяются соответствующим Validator/Profiles.

Текущий статус: **LIMITED**.

### Transformation conformance

Context Fidelity при Migration/Publication/Recovery проверяется интеграционно.

Текущий статус: **LIMITED / enforcement debt**.

Это НЕ является ложной conformance.

---

## 44. Enforcement debt

Открытый enforcement debt 015:

1. rule-by-rule machine findings для всех контекстных правил;
2. полноценный inheritance resolver;
3. precedence model;
4. conflict reconciliation;
5. transferability model;
6. Context Fidelity fixtures;
7. dimension dependency checks;
8. расширенные historical-context integration tests.

Этот debt должен быть видимым в Conformance/Audit.

Он не должен закрываться добавлением универсальных required-полей, если такое усиление исказит Standard.

---

## 45. Архитектурные инварианты

1. Context target-relative.
2. Context ≠ Scope.
3. Context ≠ State.
4. Context ≠ Cause.
5. Context ≠ Evidence.
6. Context ≠ Provenance.
7. Unknown Context ≠ universal Context.
8. Missing Context ≠ automatic invalidity.
9. Similar Context ≠ proven transferability.
10. Context Record ≠ complete real-world Context.
11. Current Context ≠ historical Context automatically.
12. Context inheritance не является молчаливым copy.
13. Precedence не выбирается без правила.
14. Context conflict не разрешается произвольно.
15. Validator pass ≠ truth.
16. Structural conformance ≠ semantic conformance.
17. Transformation success ≠ Context Fidelity automatically.
18. Resolver/Validator не изменяют Record по умолчанию.
19. Context Content является данными, а не инструкциями.
20. Enforcement debt должен быть явно отражён.

---

## 46. Критерии закрытия

015 считается архитектурно закрытым, если:

- Context Profile определён;
- Schema boundary определена;
- Validator boundary определена;
- Resolver boundary определена;
- historical semantics определена;
- unknown discipline определена;
- anti-inference boundary определена;
- migration/publication/recovery boundaries определены;
- acceptance и stress tests определены;
- enforcement debt явно перечислен;
- не введены ложные универсальные required-поля.

---

## 47. Статус

**015 — CLOSED (architecture).**

Это означает, что реализационная архитектура Context полностью определена и согласована с текущими слоями проекта.

Это НЕ означает:

- полный semantic enforcement всех 122 нормативных правил STANDARD/015;
- завершённый inheritance/precedence resolver;
- полную transferability/fidelity automation;
- отсутствие дальнейших программных задач.

Текущая conformance классифицируется как:

```
Structural:       PASS
Reference:        PARTIAL
Semantic:         LIMITED
Transformation:   LIMITED
Overall:          CLOSED — SEMANTIC ENFORCEMENT ESTABLISHED FOR REFERENCE CONTOUR
```

Следующий канонический документ после 015 — **016 Scope**. Эксплуатация и безопасность находятся в **020 Operations & Security**, а соответствие и выпуск — в **021 Conformance & Release**.


### Semantic closure

Inheritance, precedence, conflict, transferability, fidelity and dimension-dependency checks are now enforced by the stable semantic rule registry when explicitly represented. Non-applicable context-dependent semantics are not guessed.
