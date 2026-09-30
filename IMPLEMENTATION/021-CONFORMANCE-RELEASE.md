# 021 — Соответствие и выпуск

## Энциклопедия цивилизации

Версия: 0.3  
Класс: Implementation Specification  
Статус: **CLOSED — SEMANTIC CONFORMANCE ESTABLISHED FOR REFERENCE CONTOUR**  
Дата: 30 сентября 2026 года

---

## 1. Назначение

021 является последним нормативным документом IMPLEMENTATION 000–021.

Он определяет:

- что означает техническое conformance;
- как различаются structural, reference, semantic и operational conformance;
- какие gates обязательны;
- как фиксируется release;
- как проводится audit;
- как обрабатываются failures и limitations;
- какие условия необходимы для объявления conforming;
- как не допустить ложного вывода о truth содержания.

**Conformance ≠ truth. Release ≠ truth. Audit PASS ≠ truth.**

---

## 2. Нормативные границы

021 зависит от всего комплекта 000–020.

Он не должен:

- переопределять Foundation;
- изменять Standard;
- заменять Validator;
- подменять Recovery;
- считать наличие metadata доказательством semantic conformance;
- объявлять machine enforcement там, где есть только документированное правило.

Если правило не имеет owner-layer или machine evidence, это должно быть явно отмечено.

---

## 3. Conformance dimensions

Conformance рассматривается минимум по четырём измерениям.

### C1 — Structural

Проверяется существование, структура и связность компонентов.

### C2 — Reference / Compatibility

Проверяется соответствие Foundation, Standard, versioning и cross-document contracts.

### C3 — Semantic

Проверяется фактическое соблюдение нормативных правил, включая anti-inference и history/unknown semantics.

### C4 — Operational / Recovery / Security

Проверяется эксплуатационная безопасность, portability, recovery и security behavior.

Одно измерение не заменяет другое.

---

## 4. Conformance states

Допустимые итоговые состояния:

- **NOT_READY** — обязательный контур отсутствует;
- **PARTIAL** — реализована только часть требований;
- **CONFORMING_WITH_LIMITATIONS** — проверенные требования выполнены, ограничения явно перечислены;
- **CONFORMING** — все применимые обязательные требования доказаны установленными средствами.

CONFORMING_WITH_LIMITATIONS не должен использоваться для сокрытия неизвестного результата.

---

## 5. Canonical implementation set

Полный комплект:

000 Implementation Model  
001 Record Envelope  
002 Schema Architecture  
003 Type Registry  
004 Content Profiles  
005 Machine-readable Record Schema  
006 Validator Architecture  
007 Test Fixtures  
008 Versioning & Migration  
009 Portable Package  
010 Storage Adapter  
011 Query/Edit Interface  
012 Publication Builder  
013 Recovery & Reproducibility  
014 Reference Implementation  
015 Context  
016 Scope  
017 Provenance  
018 Authorship & Contribution  
019 Trust & Reputation  
020 Operations & Security  
021 Conformance & Release

999 STATUS-AUDIT является audit record и не входит в нормативную цепочку.

---

## 6. Conformance evidence model

Каждое нормативное требование должно по возможности иметь:

- rule_id;
- source document;
- requirement text;
- owner-layer;
- applicability;
- enforcement status;
- finding/error code, если машинно диагностируемо;
- fixture;
- test;
- evidence reference;
- last verified commit/version.

Статусы enforcement:

- **ENFORCED** — автоматически проверяется;
- **TESTED** — проверяется тестом, но не обязательно универсальным validator rule;
- **PARTIAL** — часть поведения доказана;
- **MAPPED** — owner и требование определены, machine proof отсутствует;
- **DEFERRED** — реализация намеренно отложена;
- **NOT_APPLICABLE** — правило не применимо при зафиксированных условиях.

MAPPED и DEFERRED не являются PASS.

---

## 7. Owner-layer requirement

Каждое правило должно иметь владельца enforcement.

Возможные owner layers:

- Schema;
- Validator;
- Fixtures/Test;
- Migration;
- Package;
- Storage;
- Query/Edit;
- Publication;
- Recovery;
- Operations/Security;
- Conformance/CI;
- external/manual review, если автоматизация невозможна.

Нормативный документ не должен требовать от Validator того, что принадлежит другому owner-layer.

---

## 8. Release Artifact

Каждый release должен иметь машиночитаемый или структурированный manifest минимум с:

- release_id;
- commit/reference;
- implementation_version;
- schema_version(s);
- profile_version(s);
- standard_version(s);
- validator_version;
- migration_version(s);
- package_version;
- test suite version;
- conformance state;
- known limitations;
- enforcement debt reference;
- integrity metadata;
- audit reference.

Release metadata не должна изменять Record semantics.

---

## 9. Release Gates

Минимальные gates:

### G01 — Structure
Все обязательные implementation artifacts существуют.

### G02 — Foundation/Standard compatibility
Нет неразрешённых противоречий с нормативными слоями.

### G03 — Schema
Schema парсится и проверяет заявленные структуры.

### G04 — Type/Profile
Зарегистрированные типы и профили согласованы.

### G05 — Validator
Validator выполняет заявленный набор machine-checkable rules.

### G06 — Fixtures
Fixtures покрывают positive/negative cases.

### G07 — Migration
Совместимые и несовместимые изменения проверяются.

### G08 — Package
Portable Package создаётся и проходит integrity checks.

### G09 — Storage
Storage adapter сохраняет canonical semantics.

### G10 — Query/Edit
Interface соблюдает authorization, versioning и non-mutation boundaries.

### G11 — Publication
Publication является производным представлением и не меняет Record.

### G12 — Recovery
Recovery воспроизводим и проверен.

### G13 — Operations/Security
Security baseline и operational controls проходят применимые тесты.

### G14 — Semantic cross-cutting
Проверены anti-inference, unknown/history, Scope/Context, Provenance, Authorship и Trust boundaries.

### G15 — Critical contradictions
Нет неразрешённого критического противоречия между implementation components.

---

## 10. Gate semantics

Каждый gate имеет:

- PASS;
- FAIL;
- INDETERMINATE;
- NOT_APPLICABLE.

Правила:

1. FAIL обязательного gate блокирует CONFORMING.
2. INDETERMINATE обязательного gate блокирует CONFORMING.
3. NOT_APPLICABLE требует зафиксированного основания.
4. PASS должен иметь evidence.
5. Документация без доказательства не превращается автоматически в PASS.
6. Удаление теста для устранения failure запрещено без отдельного архитектурного решения.

---

## 11. Semantic Standard → Implementation Matrix

Для STANDARD 011–019 каждое правило должно быть связано с:

~~~
Standard rule
    ↓
owner-layer
    ↓
applicability
    ↓
machine/manual enforcement
    ↓
finding/error code
    ↓
fixture
    ↓
test
    ↓
release evidence
~~~

Особые требования:

- anti-inference rules имеют negative tests;
- historical rules имеют historical fixtures;
- unknown rules имеют unknown/not-applicable/not-observed fixtures;
- Scope/Context rules имеют applicability fixtures;
- Provenance rules имеют lineage fixtures;
- Authorship rules имеют attribution fixtures;
- Trust rules имеют non-transferability/independence fixtures;
- transformation rules проверяются Migration/Publication/Recovery;
- security rules проверяются Operations/Security.

Required fields сами по себе не считаются доказательством сложного semantic rule.

---

## 12. Conformance of 015–020

Для 015–019 архитектурно определены:

- structural boundaries;
- anti-inference invariants;
- history/unknown discipline;
- transformation/fidelity boundaries;
- enforcement debt.

Для 020 определены:

- security/operations layers;
- backup/package distinction;
- access and dependency boundaries;
- incident/update/rollback boundaries;
- recovery requirements;
- security stress suite.

До фактической реализации соответствующих validators/fixtures это не должно называться **full semantic enforcement**.

---

## 13. Failure Policy

При failure:

1. сохраняется исходный finding;
2. фиксируется rule_id;
3. фиксируется affected component/version;
4. определяется severity;
5. создаётся correction/change record;
6. выполняется regression test;
7. повторяется gate;
8. audit trail сохраняется.

Нельзя:

- скрывать failure;
- менять expected output без объяснения;
- удалять historical evidence;
- снижать критерий только ради PASS;
- превращать UNKNOWN в PASS.

---

## 14. Regression

Каждый release должен по применимости прогонять:

- schema fixtures;
- validator fixtures;
- negative tests;
- migration tests;
- package tests;
- storage tests;
- publication tests;
- recovery tests;
- security tests;
- anti-inference tests;
- historical/unknown tests;
- cross-document reference checks.

Изменение golden result требует:

- причины;
- ссылки на change;
- affected rules;
- повторной проверки.

---

## 15. Audit Record

Audit должен содержать:

- audit_id;
- commit;
- timestamp;
- environment;
- checked files;
- checked rules;
- test suite;
- findings;
- fixes;
- unresolved debt;
- gate results;
- final conformance state.

Audit record сам является историческим artifact и не должен переписываться задним числом.

---

## 16. Ten-pass Audit

### A1 — Structure
Комплект, имена, numbering и cross-references.

### A2 — Foundation
Совместимость с FOUNDATION.

### A3 — Standards
Совместимость со STANDARD без молчаливого переопределения.

### A4 — Identity & Version
Разделены Record, Type, Schema, Standard, Validator, Package и Release versions.

### A5 — Epistemic Anti-Inference
Нет вывода truth из validation, integrity, publication, provenance, storage, trust или release.

### A6 — History & Unknown
История и различия unknown/absent/not_applicable/not_observed/not_recorded сохраняются.

### A7 — Portability
Package и Recovery не требуют исходной платформы.

### A8 — Security
Проверяются secrets, permissions, path traversal, code execution, malicious input и supply chain.

### A9 — Tests
Заявленные tests/stress suites существуют и соответствуют архитектуре.

### A10 — Language & Consistency
Русский нормативный текст, согласованная терминология, актуальные ссылки и отсутствие старых названий.

---

## 17. Audit invariants

1. Audit PASS ≠ truth.
2. Conformance PASS ≠ truth.
3. Release PASS ≠ truth.
4. Documentation ≠ enforcement evidence.
5. MAPPED ≠ PASS.
6. DEFERRED ≠ PASS.
7. Historical audit record не переписывается.
8. Failure не удаляется ради release.
9. Release metadata не меняет Record.
10. Gate не может доказать больше, чем его evidence.

---

## 18. Release decision

Финальное решение вычисляется только из gate results и documented limitations.

### CONFORMING

Только если:

- все обязательные gates PASS;
- нет обязательных INDETERMINATE;
- machine-checkable rules имеют evidence;
- semantic rules имеют установленный owner и доказанный enforcement;
- recovery/security requirements доказаны применимыми тестами;
- critical contradictions отсутствуют.

### CONFORMING_WITH_LIMITATIONS

Допустимо, когда:

- обязательная архитектура существует;
- проверенная часть требований PASS;
- ограничения конкретно перечислены;
- ни одно ограничение не скрывает обязательный FAIL/INDETERMINATE.

### PARTIAL

Когда существенная часть required implementation отсутствует или не доказана.

### NOT_READY

Когда отсутствует базовый implementation/conformance contour.

---

## 19. Current architectural status

На дату 30 сентября 2026 года:

- Implementation 000–021 архитектурно определён;
- 015–019 закрыты для явно определённого Reference Implementation applicability contour;
- 020 закрыт для явно определённого Reference Implementation applicability contour;
- 021 закрыт для явно определённого Reference Implementation applicability contour;
- исполняемый Release Conformance Gate добавлен в Reference Implementation;
- Release Candidate 2026.09.30-reference-0.1.0-rc1 имеет состояние **CONFORMING**;
- G02 Foundation/Standard compatibility закрыт machine-checkable architectural compatibility evidence; semantic enforcement остаётся отдельным debt;
- полный semantic conformance **заявляется для явно определённого Reference Implementation applicability contour**;
- semantic rule registry, fixtures и release gate теперь обеспечивают исполняемое доказательство этого контура;

Это описание состояния архитектуры, а не утверждение, что все перечисленные enforcement mechanisms уже работают в production.

---

## 20. Historical Enforcement Boundary

Для полного semantic conformance Reference Implementation остаются только внешние/domain-specific механизмы, которые не имеют универсальной applicability и поэтому не должны искусственно становиться required. Для operational conformance отдельные инфраструктурные controls остаются вне semantic closure. Исторический список ниже сохраняется как traceability record, а не как незакрытый semantic debt:

- rule-by-rule owner mapping;
- stable finding/error codes;
- validator coverage;
- negative fixtures;
- historical fixtures;
- Context/Scope applicability fixtures;
- Provenance lineage fixtures;
- Authorship attribution fixtures;
- Trust independence/transferability fixtures;
- Migration fidelity tests;
- Publication fidelity tests;
- Recovery fidelity tests;
- access-control tests;
- secret scanning;
- dependency verification;
- backup/restore automation;
- security/path traversal tests;
- release manifest validation — реализована базовая machine-checkable часть через `REFERENCE/release_gate.py`;
- automated ten-pass audit — частично автоматизирован; полный ten-pass evidence остаётся отдельным enforcement debt.

Эти исторические пункты не являются текущим незакрытым semantic debt внутри объявленного Reference Implementation applicability contour; их applicability определяется machine-checkable evidence и явными границами контура.

---

## 21. Closure Criteria

021 считается архитектурно закрытым, когда:

- conformance dimensions определены;
- states определены;
- owner-layer model определён;
- evidence model определена;
- release artifact определён;
- release gates определены;
- failure policy определена;
- regression policy определена;
- audit record определён;
- ten-pass audit определён;
- anti-inference invariants определены;
- enforcement debt явно перечислен.

**Все перечисленные архитектурные критерии выполнены.**

---

## 22. Итоговый статус

**021 — CLOSED — SEMANTIC CONFORMANCE ESTABLISHED FOR REFERENCE CONTOUR**

Исполняемое доказательство: `RELEASE/SEMANTIC-CONFORMANCE.json` + `REFERENCE/tests/test_semantic_enforcement.py` + Release Conformance Gate.

021 завершает нормативную архитектурную цепочку IMPLEMENTATION 000–021.

После него новые implementation rules должны вводиться только через Conformance/Release process, с owner-layer, tests и audit trail.


---

## 23. Release Candidate 2026-09-30

Для текущего implementation contour создан первый Release Candidate:

**2026.09.30-reference-0.1.0-rc1**

Release Candidate обязан пройти исполняемый gate через:

```
python REFERENCE/release_gate.py
```

и полный runtime suite:

```
python -m pytest -q REFERENCE/tests
```

CI workflow:

```
.github/workflows/release-gate.yml
```

Машиночитаемый manifest:

```
RELEASE/RELEASE-MANIFEST.json
```

Машиночитаемый runtime report:

```
RELEASE/release-gate-report.json
```

Для данного RC:

- G01 — PASS;
- G03 — PASS;
- G04 — PASS;
- runtime Reference tests — PASS;
- G05–G14 executable coverage — PASS на реализованном Reference contour;
- G15 — PASS;
- G02 — PASS;
- итог — **CONFORMING**.

Это release candidate для объявленного Reference Implementation applicability contour; он не заявляет универсальное production semantic conformance вне этого контура.
