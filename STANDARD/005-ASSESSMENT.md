005-ASSESSMENT.md

Статус: канонический стандарт v0.1
Проект: Энциклопедия цивилизации
Назначение: определить универсальную модель Assessment (оценивания) для Claims, Sources, Evidence Uses, Methods, Assessments, физических объектов, отношений, множеств и иных определённых Targets.

────────

0. Назначение стандарта

Assessment — это специализированный Record, представляющий результат оценивания определённого Target относительно определённого evaluative construct.

Стандарт не определяет, что является истиной, не создаёт universal truth score и не даёт особого эпистемического статуса экспертам, государствам, институтам, проекту или автоматическим системам.

Он определяет, как Assessment должен быть представлен так, чтобы его смысл, границы применимости, происхождение и история могли быть честно восстановлены.

Каноническое ядро:

```text
ASSESSMENT

is a specialized Record

requires:
  exactly 1 defined Target structure
  exactly 1 primary Evaluation Aspect / evaluative construct

when completed:
  exactly 1 defined Assessment Result

may include:
  0..N explicit Assessment Inputs

must additionally preserve or resolve:
  any Context
  Scope
  Basis
  States
  versions
  provenance
  lineage

that are materially necessary
for correct identification,
interpretation,
comparability,
reproducibility,
or applicability of the Result.
```

────────

1. Assessment Core

1.1. Assessment

Assessment — специализированный Record, представляющий один определённый evaluative act или, если это заранее определено Profile, одну continuous evaluative identity с сохраняемыми историческими States.

Assessment не является Target и не является его intrinsic property.

```text
Assessment ≠ Target
```

Assessment также не является автоматически:

```text
Claim
Evidence Use
Measurement
Truth
Decision
Consensus
Authority
Project Endorsement
```

1.2. Минимальная структура

Completed Assessment MUST иметь:

1. один defined Target structure;
2. один primary Evaluation Aspect / evaluative construct;
3. один defined Assessment Result.

Дополнительные элементы являются conditionally required и включаются только тогда, когда без них materially нарушается смысл Assessment.

1.3. Defined

Defined означает: имеющий достаточно определённую semantics для однозначной интерпретации в пределах применимого Standard/Profile.

Defined concept не обязан существовать как отдельный Record.

1.4. Resolvable

Resolvable означает: объект, State, relation или semantics могут быть однозначно установлены из сохранённой структуры, history, provenance или references без изобретения отсутствующего смысла.

```text
resolvable ≠ currently online
```

1.5. Materially relevant / required

Элемент является materially relevant, если его отсутствие, изменение или неверное представление способно существенно изменить:

• identity;
• interpretation;
• comparability;
• reproducibility;
• applicability;
• или оценку Result.

1.6. Draft и completed Assessment

Draft/in-progress Assessment Record MAY временно быть неполным согласно generic Record lifecycle.

Completed Assessment MUST иметь defined Result.

Отсутствие Result в draft не делает сам Record невозможным; отсутствие Result в записи, заявленной как completed Assessment, является Core conformance failure.

────────

2. Assessment Target

2.1. Target structure

Каждый Assessment MUST иметь exactly one defined Target structure.

Это не означает exactly one Target Record.

Target structure MAY представлять:

• single Target;
• addressable sub-target;
• relational Target;
• set-level Target.

2.2. Relational Target

Если evaluated property существует между несколькими participants, Target MAY быть relational:

```text
Target:
(EU-A, EU-B)

Aspect:
independence
```

Roles/order MUST быть resolvable, если relation асимметрична или порядок materially влияет на смысл.

2.3. Set-level Target

Assessment MAY оценивать множество как единый Target:

```text
Target:
[EU-1, EU-2, EU-3]

Aspect:
methodological diversity
```

Set-level Assessment MUST NOT использоваться для скрытого объединения независимых member-level evaluative acts.

Legitimate Profile-defined collective predicate MAY иметь implications для members, но:

```text
Assessment(set)
≠ automatically collection of Assessment(member)
```

2.4. Heterogeneous Targets

Target structure MUST NOT превращаться в arbitrary container семантически несвязанных объектов.

Если несколько participants входят в Target, их роли и общий evaluative смысл должны быть defined.

2.5. Sub-target

Если Result утверждается о самостоятельно addressable component как об отдельном evaluative object, этот component SHOULD быть представлен как sub-target.

Если component лишь ограничивает область рассмотрения свойства более широкого Target, MAY использоваться Evaluation Scope.

2.6. Target State

Если Target mutable и его State materially влияет на Assessment, relevant Target State MUST оставаться resolvable.

```text
Assessment(Target@v1)
≠ automatically
Assessment(Target@v2)
```

New Target State MUST NOT молча менять historical Assessment.

2.7. Dynamic Target

Target MAY определяться query/filter/selection process.

Completed Assessment MUST сохранять semantically closed historical Target через resolved membership либо достаточный immutable reconstruction context.

Timestamp alone не гарантирует воспроизводимость historical Target.

────────

3. Evaluation Aspect, Basis & Result

3.1. Evaluation Aspect

Evaluation Aspect определяет, какое свойство или evaluative construct оценивается.

Каждый Assessment MUST иметь один primary Evaluation Aspect / evaluative construct.

Aspect semantics MUST быть resolvable.

Списки вроде reliability, risk, quality, robustness, applicability, reproducibility являются примерами, а не закрытым Core vocabulary.

3.2. Aspect identity и label

Label не определяет semantic identity.

```text
"надёжность"
"reliability"
"fiabilité"
```

MAY представлять одну и ту же concept identity.

3.3. Aspect composition

Aspect SHOULD выражать evaluated property.

Target, Context и Scope SHOULD использовать собственные механизмы, если эти semantics содержательно разделимы.

Profiles SHOULD определять canonical representation для повторяющихся domain patterns.

3.4. Evaluation Basis

Evaluation Basis — defined evaluative logic, method, criterion system, rule, model, scale или иная структура, по которой Target/Inputs интерпретируются в Result.

Basis MAY быть composite.

Core не требует exactly one Method.

Basis MAY включать Criterion, Metric, Threshold, Rule, Scale, Weight, Aggregation Method, Methodology, Benchmark, Model, Formula или expert procedure.

Эти элементы не являются universal required Core Entities.

3.5. Basis ≠ Inputs ≠ provenance

```text
Evaluation Basis
≠ Assessment Inputs
≠ execution provenance
≠ Record provenance
```

Semantic distinction не требует отдельных storage systems.

Одна provenance infrastructure MAY хранить несколько semantic layers.

3.5.1. Criterion ≠ Input

Criterion определяет, как или по какому условию производится оценивание.

Input определяет, какой материал фактически используется при оценивании.

```text
Criterion ≠ Input satisfying Criterion
```

Criterion и фактический материал, использованный для проверки Criterion, MUST оставаться семантически различимыми.

3.6. Assessment Result

Completed Assessment MUST иметь exactly one defined Assessment Result.

Result MAY быть qualitative, categorical, ordinal, numeric, probabilistic, interval/distribution, comparative, ranking, textual или structured.

Datatype не определяет ontology.

3.7. Structured Result

Structured Result допустим, если components образуют один Profile-defined coherent evaluative construct.

Structured Result MUST NOT становиться arbitrary container.

Если component требует самостоятельной addressability, provenance, competing evaluation или lifecycle, он SHOULD быть promoted в отдельный Assessment или иной explicit Record.

3.8. Result semantics

Result MUST быть интерпретируем относительно Aspect и materially required Basis/Scale.

Result = 3 не является достаточно defined, если неизвестно, что означает 3.

3.9. Result ordering ≠ desirability

Ordered scale не означает automatic good/bad polarity.

high reliability, high risk и high uncertainty имеют разные desirability semantics.

Core не предполагает universal monotonicity.

3.10. Measurement vs Assessment

Measurement и Assessment различаются semantics, а не datatype.

error rate = 4.2% может быть Measurement.

Если Profile определяет эту величину как evaluative Result, она MAY быть Result Assessment.

Quantification не даёт automatic epistemic superiority.

────────

4. Assessment Inputs, Evidence & Provenance

4.1. Assessment Input

Assessment Input — разрешимый информационный или фактический объект, содержание или State которого materially используется при получении Result.

Assessment MAY иметь 0..N explicit Inputs.

Explicit Inputs не являются universal Core requirement.

4.2. Допустимые Inputs

Assessment Input MAY быть Evidence Use, Source, Claim, Measurement, Dataset, Method output, другим Assessment, derived value или иным defined object.

4.3. Evidence Use vs Assessment Input

Если material используется как атомарное evidence относительно Claim, SHOULD использоваться Evidence Use.

Если material является technical/evaluative input процесса Assessment, он MAY быть direct Assessment Input.

```text
Evidence Use
≠ Assessment Input
```

Evidence Use MAY быть Assessment Input.

4.3.1. Citation/reference ≠ Input membership

Наличие Source, Claim или иного Record в citation, rationale, discussion или reference MUST NOT автоматически означать Assessment Input membership.

Фактическая роль объекта — Input, Target, Basis reference, citation, provenance reference или иная роль — должна оставаться resolvable, когда различие materially важно.

```text
citation/reference ≠ automatically Assessment Input
```

4.4. Target как implicit input

Если Assessment непосредственно использует свойства Target, которые уже resolvable через Target reference, отдельная duplicate Input reference не обязательна.

4.5. Historical Inputs

Completed Assessment MUST сохранять historical input basis actually used, если он materially significant.

New Input MUST NOT молча добавляться к старому completed Assessment.

Dynamic Input selection MUST сохранять membership или достаточный immutable reconstruction context, если membership materially влияет на Result.

4.6. Input State

Materially relevant Input State MUST оставаться resolvable.

```text
Input@v3
≠ Input@current automatically
```

4.7. Missingness

Нужно различать missing, unknown, not measured, not applicable, zero, not detected, excluded.

Эти состояния MUST NOT silently collapse, если различие materially важно.

4.8. Selection provenance

Selection criterion может быть частью Basis.

Selection execution — process/provenance.

Selected objects — Inputs.

Эти роли MUST оставаться различимыми.

4.9. Result derivation lineage

Следует различать:

```text
Record provenance
Evaluation execution provenance
Input selection provenance
Result derivation lineage
```

Но Core не требует отдельного storage mechanism для каждого слоя.

4.10. Transformations

Materially significant filtering, normalization, imputation, weighting или transformation между Inputs и Result MUST оставаться resolvable.

4.11. Dependency

Different Assessment IDs или different reviewer identities не устанавливают independence.

```text
unknown dependence
≠ independence
```

Dependence MAY быть partial, pairwise, methodology-relative, source-relative или unknown.

Core не требует universal binary independent=true/false.

4.12. Self-support

Assessment MUST NOT использовать собственный Result как independent evidential justification того же Result.

Defined recursive/fixed-point computation MAY существовать, если recursion является частью explicit Evaluation Basis и не представляется как independent corroboration.

Indirect dependency cycles MUST оставаться detectable, когда materially relevant.

────────

5. Identity, Lifecycle & Reassessment

5.1. Assessment Identity

Assessment имеет persistent Record Identity, inherited from generic Record infrastructure.

Identity MUST NOT вычисляться из Target + Aspect + Result или других semantic tuples.

Same Result ≠ same Assessment.

5.2. Discrete Assessment

Discrete Assessment обычно представляет один historical evaluative act.

5.3. Correction

Correction исправляет representation того же evaluative act.

Correction MAY сохранять Identity.

Примеры: transcription error, mistaken reference, metadata enrichment, clarification без нового evaluative reasoning.

5.4. Reassessment

Reassessment — новый evaluative act.

Он обычно SHOULD иметь новую Assessment Identity.

Same assessor MAY создать новый Assessment.

5.5. Review ≠ Reassessment

Review имеет Target = prior Assessment и оценивает сам Assessment.

Reassessment имеет Target = original/related Target и оценивает Target заново.

Один process MAY породить оба Records.

5.6. Continuous Assessment

Profile MAY определить continuously maintained Assessment identity.

В этом случае repeated recomputations MAY быть historical States одной Assessment identity.

Continuous lineage MUST быть определена до или независимо от конкретного изменения Result и MUST NOT объявляться задним числом только для избежания новой Identity.

Historical continuous States MUST сохранять materially relevant Target State, Input membership/states, Basis/Method version, Context и Result.

5.7. Identity lineage ≠ reassessment lineage

Связанные Reassessments MAY образовывать historical lineage, но это не означает одну Assessment Identity.

```text
related reassessment lineage
≠ same Assessment identity
```

5.8. Supersession

Assessment MAY быть superseded другим.

```text
superseded
≠ deleted
≠ false
```

Supersession SHOULD иметь resolvable scope/context, если она не универсальна.

Core MUST NOT предполагать one global current Assessment.

5.8.1. Branching supersession

Supersession MAY быть branching и Profile/Context-relative.

```text
Assessment A
├── Assessment B preferred under Profile P1
└── Assessment C preferred under Profile P2
```

Core MUST NOT предполагать одну глобальную линейную цепочку old → new → uniquely valid.

5.8.2. Withdrawal

Assessment MAY быть withdrawn.

```text
withdrawn ≠ deleted ≠ false
```

Withdrawal означает изменение lifecycle/operational status, а не автоматическое утверждение о falsity Result.

Materially important reason for withdrawal SHOULD оставаться traceable, если это разрешено применимыми legal/privacy/security constraints.

Historical Assessment SHOULD сохраняться where permitted. Если внешний обязательный constraint требует physical deletion, такое удаление MUST NOT маскироваться как обычная correction или reassessment.

5.9. Latest / preferred / applicable / active

```text
latest
≠ preferred
≠ applicable
≠ active
≠ true
```

current не является Core concept без defined Profile semantics.

5.10. Migration

Carrier migration, serialization или import transport не являются Reassessment.

Carrier ≠ Assessment Identity.

────────

6. Context, Applicability & Evaluation Scope

6.1. Assessment Context

Assessment Context — внешние условия, назначение и ограничения применения, относительно которых Result должен интерпретироваться.

Context является conditionally required.

Если без него Result materially меняет смысл или может быть неправильно применён, Context MUST быть resolvable.

6.2. Context ≠ Target

Target отвечает: что оценивается?

Context: при каких внешних условиях / для какого применения?

Если второй participant является частью самого evaluated relation, SHOULD использоваться relational Target.

6.3. Evaluation Scope

Evaluation Scope — внутренняя граница реально выполненного evaluative task.

Scope conditionally required, если Target + Aspect не задают evaluative boundary достаточно точно.

6.4. Context ≠ Scope

```text
Context
→ внешние условия применения

Scope
→ внутренняя область того, что реально оценивалось
```

6.5. Applicability

Applicability не является universal intrinsic bool Assessment.

Assessment Result интерпретируется внутри собственного исходного Semantic Envelope без требования отдельного universal Applicability Assessment.

Отдельный вопрос Applicability возникает прежде всего при reuse/transfer существующего Result за пределы исходного Semantic Envelope — например, на другой Target, State, Context или use-case.

Она MAY быть Profile-defined mapping, отдельным Assessment или defined inference.

6.6. Cross-context transfer

Result MUST NOT автоматически переноситься между materially different Claims, populations, domains, Contexts, Target States или versions.

Cross-context reuse MAY происходить только при resolvable semantic equivalence, transfer rule, mapping или отдельном reasoning step.

Comparability/transfer MAY быть Aspect-relative.

6.7. Context inheritance

Context MAY наследоваться из Profile.

Materially relevant inherited Context MUST разрешаться к historical Profile/Context State, реально применявшемуся к Assessment.

6.8. Dynamic Context

Dynamic labels вроде current law, current standard, current risk level MUST NOT silently изменять historical Assessment semantics.

6.9. Временные роли

Следует различать Assessment creation time, Target State time и applicability period.

6.10. Geographic roles

Следует различать assessor location, Target location и applicability geography.

6.11. Semantic Envelope

Assessment Semantic Envelope — аналитическое понятие, а не Core Entity и не mandatory field.

Концептуально:

```text
Semantic Envelope
=
Target
+
materially relevant Target State
+
primary Evaluation Aspect / construct
+
Evaluation Scope where material
+
Assessment Context where material
+
those Basis semantics that materially constrain
interpretation, comparability, or applicability
```

Assessment Inputs не входят автоматически в Semantic Envelope, поскольку относятся прежде всего к derivation.

```text
Semantic Envelope
≠ Result Derivation Basis
```

6.12. Semantic Envelope Escape

Result MUST NOT молча переноситься за пределы своего Semantic Envelope без defined mapping, inference, Assessment или Profile rule.

────────

7. Assessment Quality, Uncertainty & Confidence

7.1. Assessment-of-Assessment

Assessment MAY быть Target другого Assessment.

Новая Entity MetaAssessment не требуется.

7.2. Meta-level privilege отсутствует

```text
meta-level
≠ epistemic privilege
```

Assessment-of-Assessment MAY быть ошибочным и MAY сам быть reviewed.

7.3. Quality ≠ Correctness

```text
Assessment quality
≠ Result correctness
```

Good methodology не гарантирует true/correct Result.

Correct Result не доказывает good methodology.

7.4. Meta-Aspects

Quality-related Aspects могут включать methodological adequacy, robustness, reproducibility, transparency, traceability, bias risk, calibration, applicability, confidence.

Этот список является illustrative, не Core vocabulary.

7.5. Uncertainty layers

Следует различать Target uncertainty, Input uncertainty, Result uncertainty, Confidence in Result, Model confidence, Applicability uncertainty.

Uncertainty/Confidence MUST иметь resolvable referent.

7.6. Probability ≠ Confidence

```text
P(Claim true)
≠ confidence in estimate
≠ model confidence
```

Equal numeric range не означает equal semantics.

7.7. Confidence ≠ inverse uncertainty

Core MUST NOT предполагать confidence = 1 - uncertainty.

High uncertainty Target MAY coexist with high confidence в том, что uncertainty действительно high.

7.8. Representation confidence/uncertainty

Profile MAY представлять confidence/uncertainty как structured component Result, отдельный Evaluation Aspect или meta-Assessment.

Core не требует redundant representation.

7.9. Propagation

Quality, confidence, uncertainty и иные Assessment properties MUST NOT автоматически compose/propagate через Inputs, Methods, Targets или meta-levels без defined evaluative rule.

7.10. Recursive review

Recursive Assessment MAY существовать, но recursive closure не является Core requirement.

Meta-review depth определяется Profile/risk requirements.

Core не требует elimination of all uncertainty.

High-risk stopping principle: выполнить предусмотренные Profile requirements для review, independence, uncertainty handling, validation/reproducibility, а не бесконечно продолжать review.

────────

8. Aggregation, Comparison & Synthesis

8.1. Comparison ≠ Aggregation

Comparison отвечает: насколько Assessments отличаются и сопоставимы?

Aggregation: можно ли получить новый Result из нескольких Inputs?

8.2. Synthesis

Synthesis — более широкая process/function category, а не обязательная Core Entity.

```text
evaluative synthesis → Assessment
inferential synthesis → Inference / Argument
action-selecting synthesis → Decision
```

Один process MAY produce multiple Records.

8.3. Aggregate Assessment

Aggregate Assessment — обычный Assessment, использующий prior Assessments и/или другие objects как Inputs.

Universal Entity AggregateAssessment не требуется.

Aggregate status не даёт automatic epistemic superiority.

8.4. Aggregation optional

Несколько Assessments MAY сосуществовать без единого aggregate Result.

Plurality является допустимым состоянием знания.

8.5. Majority / latest / authority

Core не использует правила majority wins, latest wins, authority wins, project wins как universal epistemic semantics.

Voting MAY быть Profile-defined aggregation method, но vote count не имеет universal truth meaning.

8.6. Comparability

Comparability является operation-relative.

```text
comparable for ranking
≠ comparable for arithmetic mean
≠ comparable for statistical pooling
```

Same Aspect или same label не гарантирует comparability.

8.7. Cross-Aspect synthesis

Different Aspects MAY участвовать в новом Assessment при explicit evaluative model.

Они MUST NOT silently collapse в один score.

Если synthesis выбирает действие, это MAY переходить в Decision.

8.8. Unsupported Scalarization

Scalarization сама по себе допустима.

Unsupported Scalarization — превращение multidimensional, ordinal или otherwise non-scalar Results в scalar без defined semantically valid mapping.

8.9. Dependency overlap

Aggregation должна учитывать materially relevant dependency overlap, не только exact Input identity.

Repeated use of same Input не запрещено само по себе.

Запрещено представлять repeated/dependent contribution как independent support без defined justification.

8.10. Confidence amplification

Совпадающие/high-confidence Assessments MUST NOT автоматически повышать aggregate confidence только из-за количества.

8.11. Conflict

Перед substantive conflict SHOULD сравниваться Semantic Envelopes.

Different Basis MAY всё равно давать substantive disagreement, если evaluative question sufficiently aligned.

Disagreement MAY быть component-level.

Conflict не требует forced resolution.

8.12. Agreement ≠ Truth

```text
90% agreement
≠ 90% probability true
```

Consensus/Agreement score MUST NOT silently превращаться в truth probability или confidence.

8.13. Inconclusive

inconclusive MAY быть legitimate Profile-defined Result.

```text
no aggregate Assessment
≠ aggregate Result = inconclusive
```

────────

9. Conformance, Integrity & Failure Modes

9.1. Diagnostic layers

```text
1. Invariant / Ontology
2. Conformance
   ├── Structural
   ├── Referential
   ├── Semantic
   └── Contextual-Historical
3. Integrity / Provenance
4. Epistemic / Methodological
5. Governance / Operational
```

Эти слои MAY пересекаться.

9.2. Core Conformance

Assessment Core-conformant, если он представляет допустимый Assessment Record с resolvable Target, resolvable primary Aspect/construct, defined Result если completed, и sufficient structural, referential, semantic и contextual-historical resolution всех materially necessary элементов.

9.2.1. Structural Conformance

Structural Conformance относится к required structure, cardinality, допустимым формам и lifecycle completeness Assessment Record.

9.2.2. Referential Conformance

Referential Conformance относится к корректной разрешимости materially required references, включая Target, Inputs, States, Profile, Scale, Method и иные referenced objects.

9.2.3. Semantic Conformance

Semantic Conformance относится к достаточной определённости и интерпретируемости Aspect, Result, Scale, roles и иных materially relevant semantics.

9.2.4. Contextual-Historical Conformance

Contextual-Historical Conformance относится к сохранению materially necessary Context, Scope, historical States, versions и applicability boundaries, необходимых для честной интерпретации historical Result.

Эти виды Conformance MAY пересекаться; одна проблема MAY затрагивать несколько слоёв одновременно.

9.3. Conformance ≠ correctness

```text
Core Conformance
≠ Truth
≠ Epistemic Quality
≠ Project Endorsement
```

Core-conformant Assessment MAY быть methodologically poor.

Epistemically plausible Assessment MAY быть non-conformant как Record.

9.4. Integrity / Provenance Failure

Integrity Failure — несоответствие зарегистрированной identity, provenance, Inputs, authorship, history или derivation тому, что фактически произошло или должно быть resolvable.

Integrity Failure не требует доказательства malicious intent.

```text
error ≠ fraud
```

9.5. Broken vs fabricated

```text
unavailable reference
≠ fabricated reference

missing provenance
≠ false provenance
```

9.6. Epistemic / Methodological Failure

Assessment MAY быть Core-conformant и при этом иметь selection bias, inappropriate Method, invalid inference, bad assumptions, unsupported generalization или poor statistics.

Это отдельный слой.

9.7. Governance / Operational Failure

Относится к publication, filtering, preference, UI representation, export/import claims, deletion, endorsement, operational use.

Canonical Record MAY быть conformant при misleading UI.

9.8. Anti-pattern taxonomy

Anti-pattern taxonomy — диагностическая классификация, не Core ontology.

Основные families:

```text
Semantic Laundering
Semantic Envelope Failures
Lifecycle Laundering
State / Version Drift
Dependency Failures
Input / Selection Failures
Integrity Failures
Aggregation Failures
Representation Fidelity Failures
```

9.9. Laundering

Laundering описывает эффект скрытой семантической подмены.

Термин не утверждает намерение, мошенничество или недобросовестность автора.

Explicit defined mapping/inference/Profile rule MAY legitimately transform semantics.

9.10. Lifecycle Laundering

Новый evaluative act MUST NOT маскироваться как simple correction.

К этому относятся Silent Reassessment, Fake Correction, Revision Laundering.

9.11. State / Version Drift

Historical Assessment MUST NOT silently reinterpret через materially different Target State, Input State, Scale version, Profile version, Context definition или Method version.

9.12. Representation fidelity

Canonical Assessment conformance и representation fidelity различаются.

Lossy representations MAY быть допустимы.

Failure возникает, если representation заявляет full fidelity, но materially necessary semantics потеряна; применимый Profile требует более высокой fidelity; либо presentation создаёт materially misleading interpretation.

9.13. Selection/filtering

Показ одного Assessment из многих не является failure сам по себе.

Failure возникает, если representation ложно утверждает отсутствие alternatives/consensus или нарушает declared Profile/governance semantics.

9.14. Import

Unknown imported semantics MUST remain unknown.

Lossy/partial import MAY существовать, но MUST NOT заполнять отсутствующую semantics догадкой и заявлять full Assessment equivalence.

9.15. Downstream impact

Upstream correction/withdrawal MUST NOT silently mutate historical downstream Results.

Affected downstream dependency MAY потребовать review/reassessment.

```text
affected
≠ automatically invalid
```

Known materially relevant downstream dependencies SHOULD remain discoverable; Profile MAY повышать это до MUST.

────────

10. Core Stress-Test Conclusions

Эта глава фиксирует результаты системного stress testing и не вводит новых Core Entities.

10.1. Minimal expert Assessment — PASS

Простой qualitative Assessment без numeric score и без explicit Inputs MAY быть Core-conformant.

10.2. Machine conformance Assessment — PASS

Machine Assessment использует тот же Core и не получает epistemic privilege.

10.3. Mutable Target/Input — PASS

Historical States остаются resolvable и не следуют current State автоматически.

10.4. Relational/set-level Targets — PASS

Допустимы при defined Target semantics.

10.5. Dynamic Target/Input selection — PASS

Historical membership должен быть closed/reconstructable, если materially important.

10.6. Probabilistic/qualitative/structured Results — PASS

Core не зависит от одной mathematical ontology.

10.7. Continuous Assessment — PASS

Допустим при Profile-defined lifecycle и сохранении historical States.

10.8. Meta-Assessment — PASS

Отдельная Entity не требуется.

10.9. Conflicting Assessments — PASS

Plurality без forced consensus является legitimate knowledge state.

10.10. Aggregation — PASS

Aggregate Assessment является ordinary Assessment; aggregation optional.

10.11. Offline preservation — PASS

Assessment Core не зависит от URL, HTTP, JSON, GitHub или иной текущей технологии.

10.12. Multilingual representation — PASS

Label language не определяет semantic identity.

10.13. Physical/non-digital Targets — PASS

Target не обязан быть цифровым object.

10.14. Historical unknown semantics

Если сохранена запись Target: S / Value: 4, но Aspect/Scale неизвестны, система MUST сохранять unknown semantics вместо догадки.

10.15. Full fidelity

Full fidelity означает semantic recoverability, а не byte-for-byte identity.

Разные carrier representations MAY представлять один Assessment.

10.16. Project self-authority test — PASS

Assessment, созданный или preferred проектом, не становится Truth автоматически.

10.17. Profile extensibility — PASS

Future Profiles MAY добавлять новые Aspects, Methods, Scales, review requirements и confidence models без переписывания Core.

────────

11. Канонические Core invariants

Ниже только фундаментальные инварианты Assessment Core. Остальные правила документа являются semantic rules, Profile guidance, preservation principles или diagnostic safeguards.

1. Assessment является специализированным Record.
2. Каждый Assessment MUST иметь exactly one defined Target structure.
3. Каждый Assessment MUST иметь exactly one primary Evaluation Aspect / evaluative construct.
4. Каждый completed Assessment MUST иметь exactly one defined Assessment Result.
5. Assessment Target structure MUST иметь defined evaluative semantics и MUST NOT быть arbitrary container.
6. Assessment Result MUST быть интерпретируем относительно Aspect и materially required semantics.
7. Result MUST NOT silently escape materially relevant Target/State/Aspect/Scope/Context/Basis semantics.
8. Assessment MUST NOT silently change historical Target/Input/Profile/Scale/Context/Method semantics.
9. Assessment MUST NOT использовать собственный Result как independent evidential justification того же Result; defined computational recursion не считается independent support.
10. Assessment Result MUST NOT автоматически становиться Truth, Decision, Consensus или Project Endorsement.
11. Profile MUST NOT отменять Core invariants, одновременно заявляя Core compatibility.
12. Unknown semantics MUST NOT заменяться invented semantics.
13. Historical evaluative meaning MUST NOT silently be rewritten by later State, correction, migration or reassessment.
14. Assessment Identity MUST NOT выводиться только из semantic tuple вроде Target + Aspect + Result.
15. New evaluative act MUST NOT маскироваться как technical correction.
16. Dependent/repeated Inputs/Assessments MUST NOT маскироваться как independent support.
17. Same label, number, Result или reviewer identity MUST NOT автоматически означать same semantics, same Assessment или independence.
18. Core Conformance MUST NOT интерпретироваться как correctness, quality или endorsement.
19. Assessment architecture MUST оставаться domain-neutral и technology-neutral.
20. Assessment Core MUST позволять uncertainty, plurality, disagreement и incomplete knowledge без принудительного выдумывания единого ответа.

────────

12. Фундаментальные semantic boundaries

```text
Assessment ≠ Target
Assessment ≠ Claim
Assessment ≠ Evidence Use
Assessment ≠ Measurement
Assessment ≠ Truth
Assessment ≠ Decision
Assessment ≠ Consensus
Assessment ≠ Authority
Assessment ≠ Project Endorsement
```

```text
Target
≠ Context
≠ Evaluation Scope
```

```text
Evaluation Aspect
≠ Evaluation Basis
≠ Assessment Result
```

```text
Assessment Inputs
≠ Evaluation Basis
≠ provenance
```

```text
Record provenance
≠ execution provenance
≠ selection provenance
≠ derivation lineage
```

```text
Probability
≠ Confidence
≠ Uncertainty
```

```text
Quality
≠ Correctness
≠ Applicability
```

```text
Conformance
≠ Integrity
≠ Epistemic Quality
≠ Governance Status
```

────────

13. Profile rules

Profiles MAY требовать explicit Inputs, вводить domain vocabularies, определять Scales, требовать Target/Input snapshots, задавать confidence/uncertainty representation, устанавливать review depth, требовать independent Review, определять aggregation methods, continuous lifecycle и усиливать preservation requirements.

Profiles MUST NOT ослаблять Core invariants при заявленной Core compatibility.

Conformance claim MUST быть scoped к конкретному Profile/version.

────────

14. Preservation principles

1. Material historical semantics SHOULD оставаться recoverable.
2. Resolvability не требует текущего online access.
3. Full fidelity означает semantic recoverability.
4. Carrier migration не создаёт Reassessment.
5. Historical Assessment MAY пережить утрату non-material metadata.
6. Потеря materially required semantics MAY сделать Result unresolved.
7. Later recovery of lost semantics MAY быть correction/enrichment без нового evaluative act.
8. Offline/printed representation SHOULD быть возможна без изменения Core meaning.
9. Technology-specific storage details MUST NOT определять Assessment identity.
10. Preservation Profile MAY усиливать эти требования для долгосрочного архива.

────────

15. Final Core Model

```text
ASSESSMENT
│
├── inherited Record Identity / applicable Record semantics
│
├── Target structure                  required
├── primary Evaluation Aspect         required
├── Assessment Result                 required when completed
│
├── Assessment Inputs                 0..N explicit
│
├── Evaluation Basis                  conditional
├── Assessment Context                conditional
├── Evaluation Scope                  conditional
│
├── Target / Input States             conditional
├── Method / Scale / Profile versions conditional
│
├── selection / execution provenance  conditional
└── result derivation lineage         conditional
```

Принцип минимализма:

> **Чем сложнее конкретный Assessment, тем больше Context, Inputs, Basis, provenance и history может быть materially необходимо. Но сложность конкретной оценки не должна становиться обязательной сложностью каждого Assessment.**

Принцип эпистемической честности:

> **Если система не может честно определить Target, evaluative construct, Result или materially necessary semantics, она должна сохранить неопределённость или неполноту, а не изобретать недостающий смысл.**

────────

Статус

После локальных аудитов глав 1–10, сквозной атаки глав 1–9, аудита главы 10 и финального системного аудита глав 1–10 После локальных аудитов глав 1–10, сквозной атаки глав 1–9, аудита главы 10, финального системного аудита глав 1–10 и контрольного аудита собранного документа архитектура Assessment зафиксирована как канонический стандарт v0.1 005-ASSESSMENT.md.
