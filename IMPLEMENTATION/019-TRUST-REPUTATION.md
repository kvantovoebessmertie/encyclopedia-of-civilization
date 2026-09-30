# 019 — Trust & Reputation

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: CLOSED WITH EXPLICIT ENFORCEMENT DEBT  
Дата: 29 сентября 2026 года

## 1. Назначение

Определяет реализацию Доверия и Репутации как scoped, target-relative и purpose-dependent assessments.

Главный принцип:

> Trust/Reputation может быть основанием опоры, но не заменой прямого Evidence и не гарантией Truth.

## 2. Structural contract

Schema уже требует:

- `target_ref`;
- `assessment_type`;
- `basis_refs`.

Дополнительно поддерживает:

- `value`;
- `scope_ref`;
- `context_ref`;
- `uncertainty`;
- `time`;
- `subject_ref`;
- `goal_ref`.

Для Trust/Assessment текущая Schema ранее уже закрепила `subject_ref` и `goal_ref` как часть исправления ADR-0005.

Это structural conformance, но не semantic trust computation.

## 3. Semantic dimensions

Assessment Trust/Reputation должен быть разрешим по возможности относительно:

- target;
- subject/object;
- aspect;
- scope;
- context;
- goal/purpose;
- time;
- evidence/basis;
- uncertainty;
- risk/cost of error.

Нельзя автоматически переносить Trust между:

- аспектами;
- доменами;
- задачами;
- версиями;
- субъектами;
- контекстами;
- целями.

## 4. Trust ≠ Truth

Ни один из следующих сигналов не доказывает Truth автоматически:

- reputation;
- popularity;
- certification;
- consensus;
- institutional status;
- previous accuracy;
- AI benchmark;
- number of confirming identities.

Прямое Evidence имеет собственную эпистемическую роль.

## 5. Independence

Количество Sources/Agents/confirmations не равно количеству независимых оснований.

System должна различать:

- identity count;
- agent count;
- information-root count;
- common dataset;
- common method;
- common witness;
- dependency graph.

Sybil и reputation laundering должны оставаться обнаруживаемыми.

## 6. Historical reputation

Reputation — time-indexed representation.

Нельзя автоматически переносить:

```text
high reputation at T1
→
high reputation at T2
```

Изменения команды, метода, domain, object или evidence могут изменить applicability.

Исторические assessments не переписываются задним числом.

## 7. Aspect and goal

Trust в одном аспекте не является Trust во всех аспектах.

Пример:

```text
reliable translator
≠
reliable diagnostician
```

Цель также materially relevant:

```text
trust for low-risk lookup
≠
trust for high-consequence decision
```

## 8. Uncertainty and no-history

Нужно различать:

- unknown;
- insufficient evidence;
- not applicable;
- disputed;
- no history.

Отсутствие репутационной истории не является отрицательной репутацией.

## 9. Cycles and self-support

Trust graph не должен создавать собственное основание через цикл:

```text
A trusts B
B trusts C
C trusts A
```

Cycle detection не должен автоматически превращать cycle в evidence.

## 10. Aggregation

Нельзя вводить единый универсальный Trust score без архитектурного основания.

Aggregation должна сохранять:

- component assessments;
- weights/criteria where applicable;
- uncertainty;
- dependency;
- scope;
- goal;
- time.

Average может скрывать critical failure modes.

## 11. AI and organizations

Trust к AI, organization, source, method и human — разные targets.

Benchmark performance в одной task не доказывает reliability в другой.

Organization reputation не переносится автоматически на every artifact.

## 12. Validator levels

### L1 Schema
Required refs и allowed assessment types.

### L2 Profile
Trust/Reputation profile.

### L3 Reference
Target/basis/subject/goal/time resolution.

### L4 Semantic
Scope/aspect/goal/time/dependency/cycle rules.

### L5 Assessment
Independence, aggregation, historical reassessment and transferability.

## 13. Negative tests

- missing target → fail;
- missing basis → fail;
- invalid assessment_type → fail;
- no history ≠ negative reputation;
- reputation ≠ truth;
- popularity ≠ reliability;
- certification ≠ universal trust;
- consensus ≠ truth;
- same root ≠ independent confirmations;
- historical reputation does not become current automatically;
- domain transfer without basis → indeterminate/fail;
- aspect transfer without basis → indeterminate/fail;
- cycle does not create support;
- high trust does not erase direct contradictory evidence;
- AI benchmark does not establish universal reliability.

## 14. Stress tests

T01–T24:

- large trust graph;
- cycles;
- Sybil clusters;
- common-root networks;
- historical reassessment;
- domain transfer;
- aspect transfer;
- changing goals;
- high-risk vs low-risk decisions;
- organization restructuring;
- AI version changes;
- common datasets;
- reputation laundering;
- conflicting assessments;
- missing history;
- disputed signals;
- weighted aggregation;
- outlier failure;
- average masking;
- privacy constraints;
- offline recovery;
- migration;
- publication;
- deterministic replay.

## 15. Enforcement matrix

| Rule | Owner | Status |
|---|---|---|
| required structural fields | Schema | ENFORCED |
| target/basis resolution | L3 | PARTIAL |
| subject/goal resolution | L3 | PARTIAL |
| scope/context/time linkage | L3/L4 | MAPPED |
| no-history discipline | L4 | DEFERRED |
| independence/common-root | L4/L5 | DEFERRED |
| cycle detection | L4 | DEFERRED |
| transferability | L5 | DEFERRED |
| historical reassessment | L5 | DEFERRED |
| aggregation safeguards | L5 | DEFERRED |
| privacy-aware retention | L5/016 | DEFERRED |

## 16. Conformance

Structural: **PASS**  
Reference/history: **PARTIAL**  
Semantic: **LIMITED**  
Assessment/transfer: **LIMITED**

Полный semantic Trust/Reputation conformance не заявляется.

## 17. Enforcement debt

1. typed Trust/Reputation assessment model;
2. aspect/goal/time-aware validator;
3. independence/common-root analysis;
4. cycle detection;
5. historical reassessment;
6. transferability checks;
7. aggregation safeguards;
8. privacy-aware retention;
9. Trust-specific fixtures;
10. contradiction-with-direct-evidence tests.

## 18. Invariants

1. Trust is not Truth.
2. Reputation is not Truth.
3. No history is not negative reputation.
4. Popularity is not independence.
5. Identity count is not agent count.
6. Agent count is not independent evidence count.
7. Consensus is not Truth.
8. Historical reputation is not current reputation automatically.
9. Domain-specific Trust is not universal Trust.
10. Trust cycles do not create evidence.
11. Resolver does not invent support.
12. Assessment pass does not prove target truth.

## 19. Статус

**019 — CLOSED WITH EXPLICIT ENFORCEMENT DEBT.**


## 17. Rule traceability

STANDARD/019 is tracked in the audit registry with the unique namespace TR-001…TR-196, mapped one-to-one to sections §1…§196 of STANDARD/019-TRUST-AND-REPUTATION.md.

A rule is not considered semantically closed merely because its structural fields exist. Closure requires an owner-layer mechanism and direct fixture/test evidence.

## 18. Current semantic evidence package

Package 6 directly tests:

- preservation of subject, goal, scope, context, time and uncertainty;
- distinction between assessments with different goals;
- unknown reputation versus negative reputation;
- preservation of historical Trust/Reputation versions;
- non-transfer between distinct targets;
- publication not creating truth.

Nine TR-* rules are therefore TESTED in the current audit registry. The remaining 187 Trust/Reputation rules remain explicitly DEFERRED pending dedicated enforcement evidence.

## 19. Conformance boundary

Structural conformance: **PASS**  
Reference resolution: **PARTIAL**  
Semantic evidence: **LIMITED / 9 rules TESTED**  
Full semantic conformance: **NOT CLAIMED**
