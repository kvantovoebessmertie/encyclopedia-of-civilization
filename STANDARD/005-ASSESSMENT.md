005-ASSESSMENT.md

Статус: канонический стандарт v0.2
Проект: Энциклопедия цивилизации
Назначение: определить универсальную модель Assessment (оценивания) для Claims, Sources, Evidence Uses, Methods, Assessments, физических объектов, отношений, множеств и иных определённых Targets.

────────

0. Назначение стандарта

Assessment — это специализированный Record, представляющий результат оценивания определённого Target относительно определённого оценочного конструкта.

Стандарт не определяет, что является истиной, не создаёт универсальную оценку истинности и не даёт особого эпистемического статуса экспертам, государствам, институтам, проекту или автоматическим системам.

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

Assessment — специализированный Record, представляющий один определённый акт оценивания или, если это заранее определено Profile, одну непрерывную идентичность оценивания с сохраняемыми историческими состояниями (States).

Assessment не является Target и не является его внутреннее свойство.

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

1. один определённую структуру цели;
2. один основной аспект оценивания / оценочный конструкт;
3. один defined результат оценивания.

Дополнительные элементы являются условно обязательными и включаются только тогда, когда без них materially нарушается смысл Assessment.

1.3. Defined

«Defined» означает: имеющий достаточно определённую semantics для однозначной интерпретации в пределах применимого Standard/Profile.

определённое понятие не обязан существовать как отдельный Record.

1.4. Resolvable

«Resolvable» означает: объект, State, relation или semantics могут быть однозначно установлены из сохранённой структуры, history, provenance или references без изобретения отсутствующего смысла.

```text
resolvable ≠ currently online
```

1.5. Существенно значимый / required

Элемент является materially relevant, если его отсутствие, изменение или неверное представление способно существенно изменить:

• identity;
• interpretation;
• comparability;
• reproducibility;
• applicability;
• или оценку Result.

1.6. Draft и completed Assessment

Draft/in-progress Assessment Record MAY временно быть неполным согласно общим жизненным циклом Record.

Completed Assessment MUST иметь определённый результат.

Отсутствие Result в draft не делает сам Record невозможным; отсутствие Result в записи, заявленной как completed Assessment, является Core conformance failure.

────────

2. Assessment Target

2.1. Target structure

Каждый Assessment MUST иметь exactly one определённую структуру цели.

Это не означает exactly one Target Record.

Target structure MAY представлять:

• одиночную цель;
• адресуемую подцель;
• реляционную цель;
• цель уровня множества.

2.2. Relational Target

Если оцениваемое свойство существует между несколькими participants, Target MAY быть relational:

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

Set-level Assessment MUST NOT использоваться для скрытого объединения независимых member-level акт оцениванияs.

Legitimate Profile-defined collective predicate MAY иметь implications для members, но:

```text
Assessment(set)
≠ automatically collection of Assessment(member)
```

2.4. неоднородные цели

Target structure MUST NOT превращаться в произвольный контейнер семантически несвязанных объектов.

Если несколько participants входят в Target, их роли и общий evaluative смысл должны быть defined.

2.5. Sub-target

Если Result утверждается о самостоятельно addressable component как об отдельном evaluative object, этот component SHOULD быть представлен как sub-target.

Если component лишь ограничивает область рассмотрения свойства более широкого Target, MAY использоваться область оценивания.

2.6. состояние цели

Если Target mutable и его State materially влияет на Assessment, relevant состояние цели MUST оставаться resolvable.

```text
Assessment(Target@v1)
≠ automatically
Assessment(Target@v2)
```

New состояние цели MUST NOT молча менять historical Assessment.

2.7. динамическая цель

Target MAY определяться процесс запроса/фильтрации/выбора.

Completed Assessment MUST сохранять semantically closed historical Target через resolved membership либо достаточный неизменяемый контекст реконструкции.

Timestamp alone не гарантирует воспроизводимость historical Target.

────────

3. Evaluation Aspect, Basis & Result

3.1. Evaluation Aspect

Evaluation Aspect определяет, какое свойство или оценочный конструкт оценивается.

Каждый Assessment MUST иметь один основной аспект оценивания / оценочный конструкт.

семантика аспекта MUST быть resolvable.

Списки вроде reliability, risk, quality, robustness, applicability, reproducibility являются примерами, а не закрытым Core vocabulary.

3.2. идентичность аспекта и label

Label не определяет семантическая идентичность.

```text
"надёжность"
"reliability"
"fiabilité"
```

MAY представлять одну и ту же concept identity.

3.3. состав аспекта

Aspect SHOULD выражать оцениваемое свойство.

Target, Context и Scope SHOULD использовать собственные механизмы, если эти semantics содержательно разделимы.

Profiles SHOULD определять каноническое представление для повторяющихся предметных шаблонов.

3.4. основание оценивания

основание оценивания — определённую логику оценивания, method, систему критериев, rule, model, scale или иная структура, по которой Target/Inputs интерпретируются в Result.

Basis MAY быть composite.

Core не требует exactly one Method.

Basis MAY включать Criterion, Metric, Threshold, Rule, Scale, Weight, агрегирование Method, Methodology, Benchmark, Model, Formula или экспертную процедуру.

Эти элементы не являются универсальными обязательными сущностями ядра.

3.5. Basis ≠ Inputs ≠ provenance

```text
Evaluation Basis
≠ Assessment Inputs
≠ execution provenance
≠ Record provenance
```

семантическое различие не требует отдельных систем хранения.

Одна provenance infrastructure MAY хранить несколько семантические уровни.

3.5.1. Criterion ≠ Input

Criterion определяет, как или по какому условию производится оценивание.

Input определяет, какой материал фактически используется при оценивании.

```text
Criterion ≠ Input satisfying Criterion
```

Criterion и фактический материал, использованный для проверки Criterion, MUST оставаться семантически различимыми.

3.6. результат оценивания

Completed Assessment MUST иметь exactly one defined результат оценивания.

Result MAY быть qualitative, categorical, ordinal, numeric, probabilistic, interval/distribution, comparative, ranking, textual или structured.

Datatype не определяет ontology.

3.7. структурированный результат

структурированный результат допустим, если components образуют один Profile-defined coherent оценочный конструкт.

структурированный результат MUST NOT становиться произвольный контейнер.

Если component требует самостоятельной addressability, provenance, конкурирующее оценивание или lifecycle, он SHOULD быть promoted в отдельный Assessment или иной explicit Record.

3.8. семантика результата

Result MUST быть интерпретируем относительно Aspect и materially required Basis/Scale.

Result = 3 не является достаточно defined, если неизвестно, что означает 3.

3.9. Порядок результата ≠ желательность

Ordered scale не означает automatic good/bad polarity.

high reliability, high risk и high uncertainty имеют разные желательность semantics.

Core не предполагает универсальную монотонность.

3.10. Measurement vs Assessment

Measurement и Assessment различаются semantics, а не datatype.

error rate = 4.2% может быть Measurement.

Если Profile определяет эту величину как evaluative Result, она MAY быть Result Assessment.

Количественное представление не даёт automatic эпистемического превосходства.

────────

4. вход оцениванияs, Evidence & Provenance

4.1. вход оценивания

вход оценивания — разрешимый информационный или фактический объект, содержание или State которого materially используется при получении Result.

Assessment MAY иметь 0..N явные входы.

Explicit Inputs не являются universal Core requirement.

4.2. Допустимые Inputs

вход оценивания MAY быть Evidence Use, Source, Claim, Measurement, Dataset, Method output, другим Assessment, derived value или иным defined object.

4.3. Evidence Use vs вход оценивания

Если material используется как атомарное evidence относительно Claim, SHOULD использоваться Evidence Use.

Если material является технический или оценочный вход процесса Assessment, он MAY быть direct вход оценивания.

```text
Evidence Use
≠ Assessment Input
```

Evidence Use MAY быть вход оценивания.

4.3.1. Citation/reference ≠ Input membership

Наличие Source, Claim или иного Record в citation, rationale, discussion или reference MUST NOT автоматически означать вход оценивания membership.

Фактическая роль объекта — Input, Target, Basis reference, citation, provenance reference или иная роль — должна оставаться resolvable, когда различие materially важно.

```text
citation/reference ≠ automatically Assessment Input
```

4.4. Target как implicit input

Если Assessment непосредственно использует свойства Target, которые уже resolvable через Target reference, отдельная duplicate Input reference не обязательна.

4.5. Historical Inputs

Completed Assessment MUST сохранять историческую фактически использованную основу входных данных, если он materially significant.

New Input MUST NOT молча добавляться к старому completed Assessment.

динамический выбор входов MUST сохранять membership или достаточный неизменяемый контекст реконструкции, если membership materially влияет на Result.

4.6. состояние входа

Существенно значимый состояние входа MUST оставаться resolvable.

Для вход оценивания, который является Source, состояние входа MUST быть семантически отличим от версии записи Source. Если исторически значимое состояние самого Source materially влияет на Result, именно это Source State MUST оставаться resolvable.

Для вход оценивания, который является Evidence Use, исторически значимый Source Context, включая Source State и иные уровни Source, MUST оставаться resolvable настолько, насколько они materially необходимы для интерпретации фактически использованного свидетельства. Assessment MUST NOT заменять такую историческую определённость текущей версией Source record или текущим состоянием Source.

```text
Input@v3
≠ Input@current automatically

Source record version
≠ Source State automatically
```

4.7. неполнота данных

Нужно различать missing, unknown, not measured, not applicable, zero, not detected, excluded.

Эти состояния MUST NOT silently collapse, если различие materially важно.

4.8. Selection provenance

критерий выбора может быть частью Basis.

выполнение выбора — process/provenance.

выбранные объекты — Inputs.

Эти роли MUST оставаться различимыми.

4.9. линия вывода результата

Следует различать:

```text
Record provenance
Evaluation execution provenance
Input selection provenance
Result derivation lineage
```

Но Core не требует отдельного storage mechanism для каждого слоя.

4.10. Transformations

Materially significant фильтрацию, нормализацию, импутацию, взвешивание или transformation между Inputs и Result MUST оставаться resolvable.

4.11. Зависимость

Different Assessment IDs или different reviewer identities не устанавливают independence.

```text
unknown dependence
≠ independence
```

Dependence MAY быть partial, pairwise, methodology-relative, source-relative или unknown.

Core не требует universal binary independent=true/false.

4.12. Self-support

Assessment MUST NOT использовать собственный Result как independent evidential justification того же Result.

Defined recursive/вычисление неподвижной точки MAY существовать, если recursion является частью explicit основание оценивания и не представляется как независимое подтверждение.

Indirect dependency cycles MUST оставаться detectable, когда materially relevant.

────────

5. Identity, Lifecycle & Переоценивание

5.1. идентичность оценивания

Assessment имеет устойчивую идентичность Record, inherited from generic Record infrastructure.

Identity MUST NOT вычисляться из Target + Aspect + Result или других семантических кортежей.

Same Result ≠ same Assessment.

5.2. дискретное оценивание

дискретное оценивание обычно представляет один historical акт оценивания.

5.3. Исправление

Исправление исправляет representation того же акт оценивания.

Если действие действительно является Исправление, идентичность оценивания MUST сохраняться.

Примеры: transcription error, mistaken reference, metadata enrichment, clarification без нового evaluative reasoning.

Если исправление меняет акт оценивания настолько, что возникает новый акт оценивания, это MUST рассматриваться как Переоценивание или иной новый Assessment, а не как Исправление.

5.4. Переоценивание

Переоценивание — новый акт оценивания.

Переоценивание MUST иметь новую идентичность оценивания.

Исключение не допускается за счёт переименования Переоценивание в State update. Если заранее определённый Profile поддерживает Непрерывное оценивание с одной persistent Identity, последующее вычисление/обновление, являющееся частью этой continuous identity, не является Переоценивание в смысле настоящего раздела.

Same assessor MAY создать новый Assessment.

5.5. Проверка ≠ Переоценивание

Проверка имеет Target = prior Assessment и оценивает сам Assessment.

Переоценивание имеет Target = original/related Target и оценивает Target заново.

Один process MAY породить оба Records.

5.6. Непрерывное оценивание

Profile MAY определить continuously maintained Assessment identity.

В этом случае повторные вычисления MAY быть исторические состояния одной Assessment identity.

Continuous lineage MUST быть определена до или независимо от конкретного изменения Result и MUST NOT объявляться задним числом только для избежания новой Identity.

Historical continuous States MUST сохранять materially relevant состояние цели, Input membership/states, Basis/Method version, Context и Result.

5.7. Identity lineage ≠ reassessment lineage

Связанные Переоцениваниеs MAY образовывать historical lineage, но это не означает одну идентичность оценивания.

```text
related reassessment lineage
≠ same Assessment identity
```

5.8. Замещение

Assessment MAY быть superseded другим.

```text
superseded
≠ deleted
≠ false
```

Замещение SHOULD иметь resolvable scope/context, если она не универсальна.

Core MUST NOT предполагать one global current Assessment.

5.8.1. Branching supersession

Замещение MAY быть branching и Profile/Context-relative.

```text
Assessment A
├── Assessment B preferred under Profile P1
└── Assessment C preferred under Profile P2
```

Core MUST NOT предполагать одну глобальную линейную цепочку old → new → uniquely valid.

5.8.2. Отзыв

Assessment MAY быть withdrawn.

```text
withdrawn ≠ deleted ≠ false
```

Отзыв означает изменение lifecycle/operational status, а не автоматическое утверждение о falsity Result.

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

Carrier migration, serialization или import transport не являются Переоценивание.

Carrier ≠ идентичность оценивания.

────────

6. Context, Applicability & область оценивания

6.1. контекст оценивания

контекст оценивания — внешние условия, назначение и ограничения применения, относительно которых Result должен интерпретироваться.

Context является условно обязательными.

Если без него Result materially меняет смысл или может быть неправильно применён, Context MUST быть resolvable.

6.2. Context ≠ Target

Target отвечает: что оценивается?

Context: при каких внешних условиях / для какого применения?

Если второй participant является частью самого evaluated relation, SHOULD использоваться реляционную цель.

6.3. область оценивания

область оценивания — внутренняя граница реально выполненного evaluative task.

Scope условно обязательными, если Target + Aspect не задают evaluative boundary достаточно точно.

6.4. Context ≠ Scope

```text
Context
→ внешние условия применения

Scope
→ внутренняя область того, что реально оценивалось
```

6.5. Applicability

Applicability не является universal intrinsic bool Assessment.

результат оценивания интерпретируется внутри собственного исходного семантическая оболочка без требования отдельного universal Applicability Assessment.

Отдельный вопрос Applicability возникает прежде всего при reuse/transfer существующего Result за пределы исходного семантическая оболочка — например, на другой Target, State, Context или use-case.

Она MAY быть Profile-defined mapping, отдельным Assessment или defined inference.

6.6. перенос между контекстами

Result MUST NOT автоматически переноситься между materially different Claims, populations, domains, Contexts, состояние целиs или versions.

Cross-context reuse MAY происходить только при resolvable semantic equivalence, transfer rule, mapping или отдельном reasoning step.

сопоставимость/transfer MAY быть Aspect-relative.

6.7. наследование контекста

Context MAY наследоваться из Profile.

Существенно значимый inherited Context MUST разрешаться к historical Profile/Context State, реально применявшемуся к Assessment.

6.8. динамический контекст

Dynamic labels вроде current law, current standard, current risk level MUST NOT silently изменять historical Assessment semantics.

6.9. Временные роли

Следует различать Assessment creation time, состояние цели time и период применимости.

6.10. Geographic roles

Следует различать assessor location, Target location и география применимости.

6.11. семантическая оболочка

Assessment семантическая оболочка — аналитическое понятие, а не Core Entity и не mandatory field.

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

вход оцениванияs не входят автоматически в семантическая оболочка, поскольку относятся прежде всего к derivation.

```text
Semantic Envelope
≠ Result Derivation Basis
```

6.12. семантическая оболочка Escape

Result MUST NOT молча переноситься за пределы своего семантическая оболочка без defined mapping, inference, Assessment или Profile rule.

────────

7. качество оценивания, неопределённость & уверенность

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

7.4. мета-аспекты

аспекты, связанные с качеством могут включать methodological adequacy, robustness, reproducibility, transparency, traceability, bias risk, calibration, applicability, confidence.

Этот список является illustrative, не Core vocabulary.

7.5. неопределённость layers

Следует различать Target uncertainty, Input uncertainty, Result uncertainty, уверенность in Result, Model confidence, Applicability uncertainty.

неопределённость/уверенность MUST иметь resolvable referent.

7.6. Probability ≠ уверенность

```text
P(Claim true)
≠ confidence in estimate
≠ model confidence
```

Equal numeric range не означает equal semantics.

7.7. уверенность ≠ inverse uncertainty

Core MUST NOT предполагать confidence = 1 - uncertainty.

High uncertainty Target MAY coexist with high confidence в том, что uncertainty действительно high.

7.8. Representation confidence/uncertainty

Profile MAY представлять confidence/uncertainty как structured component Result, отдельный Evaluation Aspect или meta-Assessment.

Core не требует redundant representation.

7.9. Propagation

Quality, confidence, uncertainty и иные Assessment properties MUST NOT автоматически compose/propagate через Inputs, Methods, Targets или meta-levels без defined evaluative rule.

7.10. рекурсивная проверка

Recursive Assessment MAY существовать, но recursive closure не является Core requirement.

Meta-review depth определяется Profile/risk requirements.

Core не требует elimination of all uncertainty.

High-risk stopping principle: выполнить предусмотренные Profile requirements для review, independence, uncertainty handling, validation/reproducibility, а не бесконечно продолжать review.

────────

8. агрегирование, сравнение & синтез

8.1. сравнение ≠ агрегирование

сравнение отвечает: насколько Assessments отличаются и сопоставимы?

агрегирование: можно ли получить новый Result из нескольких Inputs?

8.2. синтез

синтез — более широкая process/function category, а не обязательная Core Entity.

```text
evaluative synthesis → Assessment
inferential synthesis → Inference / Argument
action-selecting synthesis → Decision
```

Один process MAY produce multiple Records.

8.3. Aggregate Assessment

Aggregate Assessment — обычный Assessment, использующий prior Assessments и/или другие objects как Inputs.

Universal Entity AggregateAssessment не требуется.

Aggregate status не даёт automatic эпистемического превосходства.

8.4. агрегирование optional

Несколько Assessments MAY сосуществовать без единого aggregate Result.

Plurality является допустимым состоянием знания.

8.5. Majority / latest / authority

Core не использует правила majority wins, latest wins, authority wins, project wins как universal epistemic semantics.

Voting MAY быть Profile-defined aggregation method, но vote count не имеет universal truth meaning.

8.6. сопоставимость

сопоставимость является operation-relative.

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

8.9. Зависимость overlap

агрегирование должна учитывать materially relevant dependency overlap, не только exact Input identity.

Repeated use of same Input не запрещено само по себе.

Запрещено представлять repeated/dependent contribution как independent support без defined justification.

8.10. уверенность amplification

Совпадающие/high-confidence Assessments MUST NOT автоматически повышать aggregate confidence только из-за количества.

8.11. конфликт

Перед substantive conflict SHOULD сравниваться семантическая оболочкаs.

Different Basis MAY всё равно давать substantive disagreement, если evaluative question sufficiently aligned.

Disagreement MAY быть component-level.

конфликт не требует forced resolution.

8.12. Agreement ≠ Truth

```text
90% agreement
≠ 90% probability true
```

Consensus/Agreement score MUST NOT silently превращаться в truth probability или confidence.

8.13. Inconclusive

inconclusive MAY быть legitimate Profile-определённый результат.

```text
no aggregate Assessment
≠ aggregate Result = inconclusive
```

────────

9. соответствие, целостность & Failure Modes

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

9.2. Core соответствие

Assessment Core-conformant, если он представляет допустимый Assessment Record с resolvable Target, resolvable primary Aspect/construct, определённый результат если completed, и sufficient structural, referential, semantic и contextual-historical resolution всех materially necessary элементов.

9.2.1. Structural соответствие

Structural соответствие относится к required structure, cardinality, допустимым формам и lifecycle completeness Assessment Record.

9.2.2. Referential соответствие

Referential соответствие относится к корректной разрешимости materially required references, включая Target, Inputs, States, Profile, Scale, Method и иные referenced objects.

9.2.3. Semantic соответствие

Semantic соответствие относится к достаточной определённости и интерпретируемости Aspect, Result, Scale, roles и иных materially relevant semantics.

9.2.4. Contextual-Historical соответствие

Contextual-Historical соответствие относится к сохранению materially necessary Context, Scope, исторические состояния, versions и applicability boundaries, необходимых для честной интерпретации historical Result.

Эти виды соответствие MAY пересекаться; одна проблема MAY затрагивать несколько слоёв одновременно.

9.3. соответствие ≠ правильность

```text
Core Conformance
≠ Truth
≠ Epistemic Quality
≠ Project Endorsement
```

Core-conformant Assessment MAY быть methodologically poor.

Epistemically plausible Assessment MAY быть non-conformant как Record.

9.4. целостность / Provenance Failure

целостность Failure — несоответствие зарегистрированной identity, provenance, Inputs, authorship, history или derivation тому, что фактически произошло или должно быть resolvable.

целостность Failure не требует доказательства malicious intent.

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

Относится к publication, фильтрацию, preference, UI representation, export/import claims, deletion, endorsement, operational use.

Canonical Record MAY быть conformant при misleading UI.

9.8. таксономия анти-паттернов

таксономия анти-паттернов — диагностическая классификация, не Core ontology.

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

9.10. подмена жизненного цикла

Новый акт оценивания MUST NOT маскироваться как simple correction.

К этому относятся Silent Переоценивание, Fake Исправление, Revision Laundering.

9.11. смещение состояния / версии

Historical Assessment MUST NOT silently reinterpret через materially different состояние цели, состояние входа, Scale version, Profile version, Context definition или Method version.

9.12. Representation fidelity

Canonical Assessment conformance и representation fidelity различаются.

Lossy representations MAY быть допустимы.

Failure возникает, если representation заявляет полная точность представления, но materially necessary semantics потеряна; применимый Profile требует более высокой fidelity; либо presentation создаёт materially misleading interpretation.

9.13. Selection/фильтрацию

Показ одного Assessment из многих не является failure сам по себе.

Failure возникает, если representation ложно утверждает отсутствие alternatives/consensus или нарушает declared Profile/governance semantics.

9.14. Import

Unknown imported semantics MUST remain unknown.

Lossy/partial import MAY существовать, но MUST NOT заполнять отсутствующую semantics догадкой и заявлять full Assessment equivalence.

9.15. Downstream impact

Upstream correction/withdrawal MUST NOT silently mutate historical последующие результаты.

Affected downstream dependency MAY потребовать review/reassessment.

```text
affected
≠ automatically invalid
```

Known materially relevant downstream dependencies SHOULD remain discoverable; Profile MAY повышать это до MUST.

────────

10. Core выводы стресс-тестирования

Эта глава фиксирует результаты системного stress testing и не вводит новых Core Entities.

10.1. Minimal expert Assessment — PASS

Простой qualitative Assessment без numeric score и без явные входы MAY быть Core-conformant.

10.2. Machine conformance Assessment — PASS

Machine Assessment использует тот же Core и не получает epistemic privilege.

10.3. Mutable Target/Input — PASS

Historical States остаются resolvable и не следуют current State автоматически.

10.4. Relational/цель уровня множестваs — PASS

Допустимы при defined Target semantics.

10.5. динамическая цель/Input selection — PASS

Historical membership должен быть closed/reconstructable, если materially important.

10.6. Probabilistic/qualitative/structured Results — PASS

Core не зависит от одной mathematical ontology.

10.7. Непрерывное оценивание — PASS

Допустим при Profile-defined lifecycle и сохранении исторические состояния.

10.8. Meta-Assessment — PASS

Отдельная Entity не требуется.

10.9. конфликтing Assessments — PASS

Plurality без forced consensus является legitimate knowledge state.

10.10. агрегирование — PASS

Aggregate Assessment является ordinary Assessment; aggregation optional.

10.11. Offline preservation — PASS

Assessment Core не зависит от URL, HTTP, JSON, GitHub или иной текущей технологии.

10.12. Multilingual representation — PASS

Label language не определяет семантическая идентичность.

10.13. Physical/non-digital Targets — PASS

Target не обязан быть цифровым object.

10.14. Historical unknown semantics

Если сохранена запись Target: S / Value: 4, но Aspect/Scale неизвестны, система MUST сохранять unknown semantics вместо догадки.

10.15. Full fidelity

Full fidelity означает семантическая восстановимость, а не byte-for-byte identity.

Разные carrier representations MAY представлять один Assessment.

10.16. Project self-authority test — PASS

Assessment, созданный или preferred проектом, не становится Truth автоматически.

10.17. расширяемость профилей — PASS

Future Profiles MAY добавлять новые Aspects, Methods, Scales, review requirements и confidence models без переписывания Core.

────────

11. Канонические Core invariants

Ниже только фундаментальные инварианты Assessment Core. Остальные правила документа являются semantic rules, Profile guidance, preservation principles или diagnostic safeguards.

1. Assessment является специализированным Record.
2. Каждый Assessment MUST иметь exactly one определённую структуру цели.
3. Каждый Assessment MUST иметь exactly one основной аспект оценивания / оценочный конструкт.
4. Каждый completed Assessment MUST иметь exactly one defined результат оценивания.
5. Assessment Target structure MUST иметь defined evaluative semantics и MUST NOT быть произвольный контейнер.
6. результат оценивания MUST быть интерпретируем относительно Aspect и materially required semantics.
7. Result MUST NOT silently escape materially relevant Target/State/Aspect/Scope/Context/Basis semantics.
8. Assessment MUST NOT silently change historical Target/Input/Profile/Scale/Context/Method semantics.
9. Assessment MUST NOT использовать собственный Result как independent evidential justification того же Result; defined computational recursion не считается independent support.
10. результат оценивания MUST NOT автоматически становиться Truth, Decision, Consensus или Project Endorsement.
11. Profile MUST NOT отменять Core invariants, одновременно заявляя Core compatibility.
12. Unknown semantics MUST NOT заменяться invented semantics.
13. Historical evaluative meaning MUST NOT silently be rewritten by later State, correction, migration or reassessment.
14. идентичность оценивания MUST NOT выводиться только из semantic tuple вроде Target + Aspect + Result.
15. New акт оценивания MUST NOT маскироваться как technical correction.
16. Dependent/repeated Inputs/Assessments MUST NOT маскироваться как independent support.
17. Same label, number, Result или reviewer identity MUST NOT автоматически означать same semantics, same Assessment или independence.
18. Core соответствие MUST NOT интерпретироваться как правильность, quality или endorsement.
19. Assessment architecture MUST оставаться предметно-нейтральной и технологически нейтральной.
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

Profiles MAY требовать явные входы, вводить domain vocabularies, определять Scales, требовать Target/Input snapshots, задавать confidence/uncertainty representation, устанавливать review depth, требовать independent Проверка, определять aggregation methods, continuous lifecycle и усиливать preservation requirements.

Profiles MUST NOT ослаблять Core invariants при заявленной Core compatibility.

соответствие claim MUST быть scoped к конкретному Profile/version.

────────

14. принципы сохранения

1. Material historical semantics SHOULD оставаться recoverable.
2. Resolvability не требует текущего online access.
3. Full fidelity означает семантическая восстановимость.
4. Carrier migration не создаёт Переоценивание.
5. Historical Assessment MAY пережить утрату non-material metadata.
6. Потеря materially required semantics MAY сделать Result unresolved.
7. Later recovery of lost semantics MAY быть correction/enrichment без нового акт оценивания.
8. Offline/printed representation SHOULD быть возможна без изменения Core meaning.
9. Technology-specific storage details MUST NOT определять Assessment identity.
10. Preservation Profile MAY усиливать эти требования для долгосрочного архива.

────────

15. Final модель ядра

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

> **Если система не может честно определить Target, оценочный конструкт, Result или materially necessary semantics, она должна сохранить неопределённость или неполноту, а не изобретать недостающий смысл.**

────────

Статус

После интеграционного аудита с актуальными 001–004, локальных аудитов глав 1–10, сквозной атаки глав 1–9, аудита главы 10 и контрольного destructive audit архитектура Assessment зафиксирована как канонический стандарт v0.2 005-ASSESSMENT.md.
