# 016 — Scope

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: CLOSED WITH EXPLICIT ENFORCEMENT DEBT  
Дата: 29 сентября 2026 года

## 1. Назначение

Определяет реализацию Record типа `scope`: target-relative область применимости, universe/domain, membership rules, диапазоны, конфигурации и ограничения переноса.

Цель — сохранить семантическую границу знания без автоматического расширения Scope.

## 2. Schema boundary

Текущая каноническая Schema уже закрепляет:

- `target_ref` — required;
- `scope_content` — required;
- `universe_ref` — optional;
- `level` — optional;
- `membership_rule` — optional;
- `additionalProperties: false`.

Это реальная structural conformance.

`scope_content` остаётся открытым значением намеренно: multidimensional, relational, tuple-based и domain-specific Scope не должны насильно сводиться к одному универсальному формату.

## 3. Semantic invariants

Implementation обязана сохранять:

- Scope ≠ Universe;
- Scope ≠ Quantifier;
- Scope ≠ Context;
- Scope ≠ Precondition;
- Scope ≠ State;
- Scope ≠ Class;
- Scope ≠ Sample;
- Scope ≠ Evidence;
- Scope ≠ Provenance;
- Scope ≠ applicability proof.

Особенно:

```text
x ∈ Scope
≠
Claim(x) автоматически
```

и

```text
Scope containment
≠
Claim transfer
```

## 4. Universe and membership

Resolver должен различать:

- global и local universe;
- explicit и inferred universe;
- known и unknown membership;
- non-membership и отсутствие доказательства membership;
- open и closed world;
- complete и partial extension.

Нельзя выводить closed-world semantics из отсутствия записей.

## 5. Quantifier boundary

Quantifier не является частью Scope автоматически.

Система должна сохранять различия:

- all/every;
- some;
- most;
- none;
- at least/at most/exactly;
- only;
- generic/non-universal.

Transformation не должна молча менять quantifier.

## 6. Multidimensional Scope

Scope может зависеть от нескольких dimensions.

Validator НЕ должен автоматически строить Cartesian product:

```text
valid values
≠
valid tuples
```

Нужно сохранять correlated/dependent configurations, holes, discontinuities, open/closed boundaries и conditional applicability.

## 7. Sample / population discipline

Нельзя автоматически выводить:

- sample → population;
- enrolled → analyzed;
- observed → target population;
- member evidence → aggregate claim;
- aggregate result → member claim.

При материальной значимости должны сохраняться denominator, reference population и selection mechanism.

## 8. Scope provenance and epistemic status

Declared Scope не является доказательством applicability.

Scope может быть:

- stated;
- observed;
- tested;
- validated;
- reported;
- inferred;
- modeled;
- intended;
- permitted;
- disputed;
- unknown.

Эти различия не должны стираться при canonicalization.

## 9. Composition and transfer

Union/intersection/projection/mapping/inheritance/transfer должны быть явными операциями.

Нельзя считать:

- similarity = equivalence;
- compatibility = applicability;
- overlap = conflict;
- containment = transferability.

Lossy projection не даёт права реконструировать потерянную зависимость.

## 10. Scope Fidelity

Migration, translation, summary, extraction и publication должны сохранять материально значимые:

- target;
- universe;
- membership semantics;
- boundaries;
- quantifier;
- dependencies;
- uncertainty.

Lossy transformation не должна объявляться fully faithful без основания.

## 11. Validator levels

### L1 Schema
Форма Scope Record.

### L2 Profile
Профиль Scope Content.

### L3 Reference
Target/universe/version resolution.

### L4 Semantic
Membership, quantifier, tuple integrity, containment, conflict, transfer и applicability rules.

### L5 Transformation
Scope Fidelity при migration/publication/recovery.

## 12. Anti-inference tests

Минимально:

- Scope без target → fail.
- Scope без content → fail.
- unknown universe не превращается в invented universe.
- отсутствие membership не становится non-membership.
- sample не становится population.
- valid component values не становятся valid tuples.
- valid endpoints не становятся valid interval.
- Scope не становится Context.
- Evidence Scope не становится Claim Scope.
- narrow Scope не расширяется автоматически.
- historical Scope не заменяется современным.
- similarity не становится equivalence.
- lossy mapping не заявляется reversible.
- отсутствие Evidence вне X не становится доказательством non-applicability вне X.

## 13. Stress tests

S01–S20:

- многомерные Scope;
- correlated tuples;
- nested universes;
- discontinuous ranges;
- uncertain membership;
- historical geography;
- changing jurisdictions;
- version ranges;
- Scope inheritance;
- cyclic Scope references;
- composition explosion;
- lossy projection;
- translation;
- deduplication;
- offline recovery;
- large membership sets;
- conflicting Scope assertions;
- open-world/closed-world edge cases;
- quantifier transformations;
- repeated deterministic validation.

Циклы и большие графы не должны приводить к бесконечному Resolver.

## 14. Enforcement matrix

| Правило | Owner | Статус |
|---|---|---|
| required target/content | Schema | ENFORCED |
| reference shape | Schema | ENFORCED |
| target resolution | L3 | ENFORCED / graph-dependent |
| Scope/Context distinction | L4 | MAPPED |
| quantifier preservation | L4 | MAPPED |
| tuple integrity | L4 | MAPPED |
| sample/population safeguards | L4 | DEFERRED |
| inheritance | L4 | DEFERRED |
| transfer | L4 | DEFERRED |
| Scope Fidelity | L5 | DEFERRED |
| full membership algebra | L4 | DEFERRED |

DEFERRED означает enforcement debt, а не архитектурную ошибку.

## 15. Conformance

Structural: **PASS**  
Reference/history: **PARTIAL**  
Semantic: **LIMITED**  
Transformation/Fidelity: **LIMITED**

Полный semantic conformance не заявляется.

## 16. Enforcement debt

1. formal Scope algebra;
2. quantifier-aware validator;
3. multidimensional tuple validator;
4. inheritance/transfer resolver;
5. membership provenance checks;
6. Scope Fidelity fixtures;
7. historical Scope integration tests.

## 17. Архитектурные инварианты

1. Scope target-relative.
2. Scope не является доказательством applicability.
3. Unknown Scope не является universal Scope.
4. Missing Scope не является Empty Scope.
5. Multidimensional Scope не является Cartesian product.
6. Sample не является population.
7. Evidence Scope не является Claim Scope.
8. Scope similarity не является equivalence.
9. Scope compatibility не является applicability.
10. Validator pass не является truth.

## 18. Статус

**016 — CLOSED WITH EXPLICIT ENFORCEMENT DEBT.**

Архитектура Scope определена; реальное structural enforcement закрыто, а оставшаяся semantic/transformation работа явно зафиксирована.
