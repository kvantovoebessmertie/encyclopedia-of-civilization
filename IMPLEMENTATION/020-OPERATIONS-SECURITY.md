# 020 — Эксплуатация и безопасность

## Энциклопедия цивилизации

Версия: 0.2  
Класс: Implementation Specification  
Статус: **CLOSED WITH EXPLICIT ENFORCEMENT DEBT**  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Документ определяет эксплуатационный и security-контур долговременной системы: хранение, резервирование, целостность, доступ, зависимости, изменения, секреты, журналирование, инциденты, обновления, откат, восстановление и защиту цепочки поставки.

020 не определяет семантику Record и не заменяет Schema, Validator, Portable Package, Storage, Recovery или Conformance. Он определяет условия, при которых эти компоненты безопасно эксплуатируются.

**Security/Operations PASS не означает truth, validity содержания или epistemic trust.**

---

## 2. Нормативные зависимости

020 зависит от:

- 000 Implementation Model;
- 001 Record Envelope;
- 005 Machine-readable Record Schema;
- 006 Validator Architecture;
- 007 Test Fixtures;
- 008 Versioning & Migration;
- 009 Portable Package;
- 010 Storage Adapter;
- 011 Query/Edit Interface;
- 012 Publication Builder;
- 013 Recovery & Reproducibility;
- 014 Reference Implementation;
- 015 Context;
- 016 Scope;
- 017 Provenance;
- 018 Authorship & Contribution;
- 019 Trust & Reputation.

020 не должен переопределять Foundation или STANDARD.

---

## 3. Границы ответственности

### 3.1 Operations/Security отвечает за

- эксплуатационную целостность;
- резервирование;
- доступ и полномочия;
- защиту инфраструктуры;
- управление зависимостями;
- секреты;
- журналирование технических операций;
- incident handling;
- update/rollback;
- recovery drills;
- supply-chain controls.

### 3.2 Operations/Security не отвечает за

- истинность Claim;
- достоверность Source;
- качество Evidence;
- авторство;
- epistemic Trust;
- применимость Scope/Context;
- смысловую эквивалентность Migration.

Эти свойства проверяются соответствующими нормативными и implementation-слоями.

---

## 4. Модель эксплуатационных слоёв

### L1 — Configuration & Structural Safety

Проверяются:

- версии компонентов;
- конфигурация;
- права файлов;
- структура package;
- обязательные manifest fields;
- отсутствие секретов в canonical artifacts.

### L2 — Access, Dependency & Supply Chain

Проверяются:

- identity/authentication;
- authorization;
- least privilege;
- separation of duties;
- dependency pinning;
- provenance инструментов;
- integrity dependency artifacts.

### L3 — Integrity, Backup, Package & Storage

Проверяются:

- hashes/digests;
- backup creation;
- backup restoration;
- package integrity;
- storage integrity;
- независимость копий;
- обнаружение повреждения.

### L4 — Change, Incident, Update & Rollback

Проверяются:

- change record;
- compatibility check;
- pre-update backup;
- tests;
- incident record;
- rollback;
- сохранение истории;
- distinction update vs migration.

### L5 — Recovery, Disaster & Operational Fidelity

Проверяются:

- clean-environment recovery;
- offline recovery;
- reproducibility;
- disaster recovery drill;
- восстановление исторических версий;
- проверка integrity после recovery;
- отсутствие скрытого изменения семантики при operational procedures.

---

## 5. Backup

Backup должен:

1. иметь идентификатор;
2. иметь время создания;
3. ссылаться на охватываемый набор данных/версий;
4. иметь integrity metadata;
5. быть восстановимым;
6. храниться независимо от исходного failure domain, когда это возможно.

**Backup ≠ Portable Package.**

Backup предназначен прежде всего для восстановления эксплуатационного состояния; Portable Package — для переносимого воспроизводимого представления системы.

Нельзя считать существование backup доказательством его восстановимости без recovery test.

---

## 6. Integrity

Integrity check может проверять:

- bytes;
- file set;
- manifest;
- hash/digest;
- schema artifact;
- validator artifact;
- package structure;
- dependency artifact.

Integrity подтверждает соответствие проверяемого представления ожидаемому digest/reference. Она **не подтверждает truth содержания**.

Нарушение integrity должно порождать техническое finding/incident, но не автоматически изменять epistemic status Record.

---

## 7. Access Control

Минимальные технические роли:

- reader;
- editor;
- validator operator;
- publisher;
- administrator;
- recovery operator.

Для критических операций должна применяться least privilege.

Authorization должна проверяться отдельно от epistemic assessment.

**Право изменить Record ≠ право считать Record истинной.**

---

## 8. Separation of Duties

Критические действия по возможности разделяются:

- изменение нормативных документов;
- изменение Schema;
- изменение Validator;
- публикация;
- административная конфигурация;
- recovery;
- удаление/retention;
- выпуск.

Если техническая среда не позволяет разделить обязанности, ограничение должно быть явно записано как operational debt/risk.

---

## 9. Change Management

Каждое значимое изменение должно иметь:

- change identifier;
- причину;
- описание;
- затронутые компоненты;
- actor/agent;
- исходную версию;
- целевую версию;
- test result;
- rollback/recovery plan;
- связь с ADR, если изменение архитектурное.

Изменение реализации не должно молча менять нормативный смысл.

---

## 10. Dependency Management

Для критических зависимостей по возможности фиксируются:

- name;
- version;
- source;
- digest/checksum;
- acquisition time;
- license/compatibility metadata;
- применимость к release.

Floating/latest dependency не должна использоваться как единственная основа воспроизводимой архивной сборки.

**Integrity dependency ≠ trust результата dependency.**

---

## 11. Secrets

Secrets должны быть отделены от canonical data.

Запрещается помещать секреты в:

- Record;
- Portable Package;
- public fixtures;
- public logs;
- source control;
- release artifacts без специально защищённого механизма.

Публикация, backup и export должны иметь secret-scanning boundary.

При обнаружении секрета в canonical/public artifact это security incident.

---

## 12. Logging

Technical logs должны фиксировать, когда это применимо:

- timestamp;
- component;
- operation;
- actor/agent;
- target;
- result;
- finding/error code;
- component version;
- correlation/reference id.

Лог не должен незаметно становиться каноническим источником epistemic semantics.

Если факт имеет семантическое значение для Record, он должен быть представлен соответствующим Record/Provenance механизмом, а не только логом.

---

## 13. Incident Handling

Incident record должен по возможности содержать:

- incident_id;
- detected_at;
- affected component;
- affected versions;
- observed symptoms;
- technical cause, если установлена;
- containment;
- recovery actions;
- validation result;
- affected artifacts;
- unresolved uncertainty.

Следует различать:

- security incident;
- integrity incident;
- availability incident;
- data-loss incident;
- configuration incident;
- semantic/epistemic finding.

**Technical incident ≠ false content.**

Причина, если она не установлена, должна оставаться unknown, а не заменяться догадкой.

---

## 14. Update

Update pipeline:

~~~
preflight
  ↓
compatibility check
  ↓
backup/package
  ↓
tests
  ↓
apply
  ↓
integrity
  ↓
validator
  ↓
recovery verification
  ↓
release record
~~~

Update не должен скрывать Migration.

Если изменение требует преобразования Record/Schema semantics, оно должно проходить через 008 Versioning & Migration.

---

## 15. Rollback

Rollback должен:

- иметь идентификатор;
- фиксировать target state;
- сохранять audit trail;
- не уничтожать исторические версии;
- иметь recovery fallback.

Rollback инфраструктуры не означает удаление исторических Record.

Если физический rollback невозможен без потери истории, применяется восстановление из проверенного Portable Package/backup.

---

## 16. Security Boundaries

Особо защищаются:

- import;
- export;
- package extraction;
- archive paths;
- path traversal;
- symlinks;
- external resources;
- credentials;
- APIs;
- admin operations;
- recovery environment;
- generated publication artifacts.

Недоверенные Record, package contents и external text являются **данными**, а не инструкциями для исполнения.

Import не должен автоматически выполнять содержимое данных.

---

## 17. Supply-chain Security

Для executable/tooling artifacts должны по возможности сохраняться:

- source;
- version;
- digest;
- acquisition metadata;
- build/reference metadata;
- applicable security findings.

Система должна различать:

1. целостность инструмента;
2. происхождение инструмента;
3. безопасность инструмента;
4. доверие к результату инструмента.

Ни одно из них автоматически не устанавливает truth Record.

---

## 18. Disaster Recovery

Минимальный recovery drill:

~~~
portable package / backup
        ↓
clean environment
        ↓
verify artifact integrity
        ↓
acquire schema/tools
        ↓
import
        ↓
validate
        ↓
restore storage
        ↓
rebuild publication
        ↓
compare expected outputs
        ↓
record recovery report
~~~

Recovery считается доказанным только результатом фактического или воспроизводимого теста, а не наличием инструкции.

---

## 19. Operational Fidelity

Операционная процедура не должна:

- менять Record без versioned operation;
- удалять history ради удобства;
- заменять unknown на empty/null;
- заменять historical Context текущим;
- менять Provenance;
- менять Authorship;
- превращать security finding в epistemic finding;
- превращать integrity PASS в truth PASS.

Любое преобразование данных должно иметь установленный owner-layer и fidelity policy.

---

## 20. Security/Operations Test Suite

### Базовые O01–O15

- O01 — backup создаётся и идентифицируется;
- O02 — backup реально восстанавливается;
- O03 — package integrity проверяется;
- O04 — повреждение artifact обнаруживается;
- O05 — неавторизованный edit блокируется;
- O06 — least privilege соблюдается;
- O07 — secrets не попадают в canonical/public artifacts;
- O08 — dependency versions фиксируются;
- O09 — change record создаётся;
- O10 — rollback сохраняет историю;
- O11 — update отличим от migration;
- O12 — technical incident не меняет epistemic status автоматически;
- O13 — untrusted input не исполняется;
- O14 — recovery проходит в clean environment;
- O15 — recovered output сравнивается с ожидаемым.

### Stress O16–O30

- O16 — отказ Backend;
- O17 — потеря индекса;
- O18 — повреждение package;
- O19 — повреждение backup;
- O20 — потеря storage node;
- O21 — компрометация dependency;
- O22 — malicious package content;
- O23 — path traversal;
- O24 — массовый import;
- O25 — массовый export;
- O26 — длительное offline хранение;
- O27 — большой archive recovery;
- O28 — повторный recovery drill;
- O29 — частичный failure update;
- O30 — recovery после неудачного rollback.

---

## 21. Anti-inference invariants

1. Backup existence ≠ recoverability.
2. Package integrity ≠ truth.
3. Hash validity ≠ epistemic validity.
4. Security PASS ≠ content truth.
5. Access role ≠ expertise.
6. Technical incident ≠ false Record.
7. Dependency integrity ≠ trustworthy conclusion.
8. Update success ≠ semantic equivalence.
9. Rollback ≠ history deletion.
10. Recovery success ≠ truth of recovered content.
11. Log entry ≠ canonical semantic fact.
12. Untrusted data ≠ executable instruction.
13. Unknown cause ≠ known cause.
14. Current state ≠ historical state.

---

## 22. Conformance classification

### Structural

**PASS** — эксплуатационные границы, роли, artifacts, gates и test suite определены.

### Reference / Cross-reference

**PARTIAL** — ссылки на конкретные реализации и deployment environments должны подтверждаться соответствующими implementation artifacts.

### Semantic

**LIMITED** — часть operational semantics требует машинных policy checks и интеграционных тестов.

### Recovery / Security

**LIMITED** — архитектура и негативные сценарии определены, но фактическое выполнение всех drills/security tests зависит от конкретной reference implementation и окружения.

---

## 23. Enforcement Matrix

| Область | Архитектурное правило | Текущий статус | Требуемый owner |
|---|---|---|---|
| Backup identity | backup должен быть идентифицируем | MAPPED | Operations |
| Backup recovery | backup должен быть восстановим | DEFERRED | Recovery/Operations |
| Package integrity | digest/integrity check | PARTIAL | Package/Operations |
| Access control | unauthorized edit запрещён | DEFERRED | Interface/Operations |
| Least privilege | роли ограничены | DEFERRED | Operations |
| Secrets | secret exclusion | DEFERRED | CI/Package/Operations |
| Dependency pinning | версии фиксируются | DEFERRED | Build/Operations |
| Incident record | incident fields | MAPPED | Operations |
| Update/migration boundary | migration не скрывается | MAPPED | Migration/Conformance |
| Rollback history | history сохраняется | DEFERRED | Versioning/Storage |
| Untrusted input | data не исполняется | DEFERRED | Import/Tooling |
| Recovery drill | clean recovery | DEFERRED | Recovery |
| Supply chain | artifact provenance/integrity | DEFERRED | Build/Operations |

**DEFERRED не означает разрешено игнорировать.** Это означает, что owner-layer определён, но автоматическое enforcement ещё не доказано.

---

## 24. Enforcement Debt

Остаются следующие debt items:

- machine-readable operational policy;
- executable access-control tests;
- secret scanning;
- dependency lock/digest verification;
- backup restore fixtures;
- package corruption fixtures;
- malicious archive/path fixtures;
- rollback/history fixtures;
- update-vs-migration integration tests;
- clean-environment recovery fixture;
- disaster recovery drill automation;
- supply-chain verification;
- operational finding/error-code registry;
- incident-to-record non-inference tests.

Эти долги не закрываются добавлением обязательных полей в Record, если правило относится к эксплуатации.

---

## 25. Closure Criteria

020 считается архитектурно закрытым, когда:

- границы ответственности определены;
- security/operations invariants определены;
- backup/package/storage различены;
- update/migration/rollback различены;
- recovery pipeline определён;
- anti-inference правила определены;
- stress suite определён;
- owner-layer для enforcement debt указан;
- ограничения явно зафиксированы.

**Все критерии выполнены на уровне архитектурной спецификации.**

Это не означает, что все enforcement tests уже реализованы.

---

## 26. Итоговый статус

**020 — CLOSED WITH EXPLICIT ENFORCEMENT DEBT**

Архитектура эксплуатационного и security-контура завершена. Машинное enforcement остаётся отдельной задачей reference implementation, Validator, CI, Storage, Recovery и Conformance layers.
