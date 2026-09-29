# 017 — Provenance

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: CLOSED WITH EXPLICIT ENFORCEMENT DEBT  
Дата: 29 сентября 2026 года

## 1. Назначение

Определяет реализацию Provenance как представления происхождения Record, transformation lineage, inputs/outputs, agents, methods, operation status и fidelity.

Provenance является утверждением о происхождении, а не гарантией фактической истории.

## 2. Existing structural support

Schema уже предоставляет:

### Envelope Provenance

- `agent_refs`;
- `created_from`;
- `transformed_from`;
- `external_sources`;
- `method`;
- `recorded_at`;
- `note`.

### Provenance Record

- `target_ref`;
- `relation`;
- `inputs`;
- `outputs`;
- `agent_ref`;
- `method_ref`;
- `operation_status`;
- `fidelity`.

Это structural conformance, но не доказательство lineage.

## 3. Основные границы

Implementation должна различать:

- operational provenance ≠ represented provenance;
- provenance ≠ truth;
- ancestry ≠ specific operation;
- direct ≠ indirect provenance;
- citation ≠ provenance;
- bibliography ≠ lineage;
- influence ≠ derivation;
- Evidence ≠ Provenance;
- Authorship ≠ Provenance;
- world causality ≠ representation lineage.

## 4. Target and granularity

Provenance должен быть привязан к конкретному target.

Не допускается молчаливое расширение provenance Record на все компоненты.

Гранулярность может быть:

- Record;
- Content component;
- transformation;
- input/output;
- physical artifact;
- execution;
- Evidence dependency.

## 5. Graph semantics

Provenance является графом с:

- nodes;
- typed edges;
- direction;
- optional temporal information;
- operation status;
- agent/method;
- fidelity.

Транзитивность не должна предполагаться для каждой relation.

```text
A → B → C

eq
одна и та же provenance relation A → C
```

## 6. Multi-input / multi-output

Joint input semantics должна сохраняться.

Нельзя автоматически превращать:

```text
f(A,B) → C
```

в независимые доказательства:

```text
A → C
B → C
```

если операция не поддерживает такую декомпозицию.

Аналогично один input с несколькими outputs не означает, что каждый output полностью derived только из любого отдельного fragment.

## 7. Transformation

Implementation должна различать:

- intended transformation;
- attempted transformation;
- completed transformation;
- failed transformation;
- partial transformation;
- actual output;
- fidelity.

Textual similarity не является semantic fidelity.

## 8. Reproducibility boundary

Provenance может быть необходимым условием reproducibility, но:

```text
complete provenance
≠
reproducibility automatically
```

Нужны также версии input, method, environment и parameters, если они materially relevant.

## 9. Independence

Общие inputs, tools, methods или information roots могут создавать зависимость.

Количество provenance edges не равно количеству независимых evidence roots.

## 10. Historical semantics

Нужно различать:

- earliest recorded;
- earliest known;
- asserted origin;
- reconstructed origin;
- unknown origin.

Knowledge about provenance changes over time. Новое знание не должно переписывать историческое epistemic state задним числом.

## 11. Mutable references

Live reference и materialized copy — разные объекты lineage.

Изменение live source не должно молча изменять исторический Provenance claim.

Deletion/redaction/withdrawal не уничтожают историческую связь; они изменяют доступность или состояние target.

## 12. Mapping and import

Imported provenance должен сохранять:

- source provenance;
- mapping method;
- mapping loss;
- confidence/uncertainty;
- source version.

Lossy mapping не должна объявляться identity-preserving.

## 13. Validator levels

### L1 Schema
Форма Provenance.

### L2 Profile
Допустимые relations/fields.

### L3 Reference
Resolution inputs/outputs/agents/methods/versions.

### L4 Semantic
Direction, granularity, operation semantics, dependency and independence.

### L5 Reproducibility/Fidelity
Transformation fidelity, import/export and recovery preservation.

## 14. Negative tests

- Provenance без target → fail.
- Provenance без relation → fail.
- Missing edge не становится negative provenance.
- Earliest recorded не становится origin.
- Citation не становится derivation.
- A→B→C не превращается автоматически в direct A→C.
- Multi-input не распадается на independent inputs.
- common root не считается независимым подтверждением.
- intended transformation не становится actual.
- textual similarity не становится fidelity.
- historical provenance не заменяется current provenance.
- imported provenance сохраняет mapping loss.

## 15. Stress tests

P01–P20:

- deep lineage;
- branching;
- merging;
- cyclic graph;
- large multi-input transformation;
- multiple outputs;
- partial provenance;
- competing provenance hypotheses;
- common-root detection;
- live reference changes;
- deletion/redaction;
- rollback;
- imported provenance;
- lossy mapping;
- offline package recovery;
- deterministic replay;
- nondeterministic transformation;
- provenance-of-provenance;
- conflicting operation status;
- historical reassessment.

## 16. Enforcement matrix

| Rule family | Owner | Status |
|---|---|---|
| target/relation required | Schema | ENFORCED |
| reference shape | Schema | ENFORCED |
| input/output structure | Schema | ENFORCED |
| target/input resolution | L3 | PARTIAL |
| graph direction semantics | L4 | MAPPED |
| multi-input jointness | L4 | DEFERRED |
| independence | L4 | DEFERRED |
| transformation fidelity | L5 | DEFERRED |
| historical epistemic state | L3/L5 | PARTIAL |
| provenance mapping loss | L5 | DEFERRED |
| reproducibility | L5 | DEFERRED |

## 17. Conformance

Structural: **PASS**  
Reference/history: **PARTIAL**  
Semantic: **LIMITED**  
Reproducibility/Fidelity: **LIMITED**

## 18. Enforcement debt

1. typed provenance relation registry;
2. graph semantic validator;
3. joint-input semantics;
4. independence/common-root analysis;
5. provenance Fidelity fixtures;
6. historical provenance integration tests;
7. reproducibility coupling;
8. imported-provenance loss accounting.

## 19. Инварианты

1. Provenance is not truth.
2. Citation is not lineage.
3. Earliest recorded is not origin.
4. Missing edge is not negative evidence.
5. Common root is not independent evidence.
6. Intended transformation is not actual transformation.
7. Fidelity is not textual similarity.
8. Historical provenance must remain historically resolvable.
9. Resolver does not invent ancestors.
10. Provenance data is data, not executable instructions.

## 20. Статус

**017 — CLOSED WITH EXPLICIT ENFORCEMENT DEBT.**
