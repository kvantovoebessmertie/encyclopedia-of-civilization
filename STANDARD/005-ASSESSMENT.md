005-ASSESSMENT.md

Статус: канонический стандарт v0.2
Проект: Энциклопедия цивилизации
Назначение: определить универсальную модель оценивание (оценивания) для Claims, Sources, Evidence Uses, методs, оцениваниеs, физических объектов, отношений, множеств и иных определённых Targets.

────────

0. Назначение стандарта

оценивание — это специализированный Record, представляющий результат оценивания определённого Target относительно определённого оценочного конструкта.

Стандарт не определяет, что является истиной, не создаёт универсальную оценку истинности и не даёт особого эпистемического статуса экспертам, государствам, институтам, проекту или автоматическим системам.

Он определяет, как оценивание должен быть представлен так, чтобы его смысл, границы применимости, происхождение и история могли быть честно восстановлены.

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

1. оценивание Core

1.1. оценивание

оценивание — специализированный Record, представляющий один определённый акт оценивания или, если это заранее определено профиль, одну непрерывную идентичность оценивания с сохраняемыми историческими состояниями (состояниеs).

оценивание не является Target и не является его внутреннее свойство.

```text
Assessment ≠ Target
```

оценивание также не является автоматически:

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

Completed оценивание ДОЛЖЕН иметь:

1. один определённую структуру цели;
2. один основной аспект оценивания / оценочный конструкт;
3. один определённый результат оценивания.

Дополнительные элементы являются условно обязательными и включаются только тогда, когда без них materially нарушается смысл оценивание.

1.3. Defined

«Defined» означает: имеющий достаточно определённую семантика для однозначной интерпретации в пределах применимого Standard/профиль.

определённое понятие не обязан существовать как отдельный Record.

1.4. Resolvable

«Resolvable» означает: объект, состояние, relation или семантика могут быть однозначно установлены из сохранённой структуры, history, происхождение или references без изобретения отсутствующего смысла.

```text
resolvable ≠ currently online
```

1.5. Существенно значимый / required

Элемент является существенно значимый, если его отсутствие, изменение или неверное представление способно существенно изменить:

• идентичность;
• interpretation;
• comparability;
• reproducibility;
• применимость;
• или оценку результат.

1.6. Draft и completed оценивание

Draft/in-progress оценивание Record МОЖЕТ временно быть неполным согласно общим жизненным циклом Record.

Completed оценивание ДОЛЖЕН иметь определённый результат.

Отсутствие результат в draft не делает сам Record невозможным; отсутствие результат в записи, заявленной как completed оценивание, является соответствие ядру failure.

────────

2. оценивание Target

2.1. Target structure

Каждый оценивание ДОЛЖЕН иметь exactly one определённую структуру цели.

Это не означает exactly one Target Record.

Target structure МОЖЕТ представлять:

• одиночную цель;
• адресуемую подцель;
• реляционную цель;
• цель уровня множества.

2.2. Relational Target

Если оцениваемое свойство существует между несколькими participants, Target МОЖЕТ быть relational:

```text
Target:
(EU-A, EU-B)

Aspect:
independence
```

Roles/order ДОЛЖЕН быть resolvable, если relation асимметрична или порядок materially влияет на смысл.

2.3. Set-level Target

оценивание МОЖЕТ оценивать множество как единый Target:

```text
Target:
[EU-1, EU-2, EU-3]

Aspect:
methodological diversity
```

Set-level оценивание НЕ ДОЛЖЕН использоваться для скрытого объединения независимых member-level акт оцениванияs.

Legitimate профиль-определённый collective predicate МОЖЕТ иметь implications для members, но:

```text
Assessment(set)
≠ automatically collection of Assessment(member)
```

2.4. неоднородные цели

Target structure НЕ ДОЛЖЕН превращаться в произвольный контейнер семантически несвязанных объектов.

Если несколько participants входят в Target, их роли и общий evaluative смысл должны быть определённый.

2.5. Sub-target

Если результат утверждается о самостоятельно addressable component как об отдельном evaluative object, этот component СЛЕДУЕТ быть представлен как sub-target.

Если component лишь ограничивает область рассмотрения свойства более широкого Target, МОЖЕТ использоваться область оценивания.

2.6. состояние цели

Если Target mutable и его состояние materially влияет на оценивание, relevant состояние цели ДОЛЖЕН оставаться resolvable.

```text
Assessment(Target@v1)
≠ automatically
Assessment(Target@v2)
```

New состояние цели НЕ ДОЛЖЕН молча менять исторический оценивание.

2.7. динамическая цель

Target МОЖЕТ определяться процесс запроса/фильтрации/выбора.

Completed оценивание ДОЛЖЕН сохранять semantically closed исторический Target через resolved membership либо достаточный неизменяемый контекст реконструкции.

Timestamp alone не гарантирует воспроизводимость исторический Target.

────────

3. Evaluation Aspect, Basis & результат

3.1. Evaluation Aspect

Evaluation Aspect определяет, какое свойство или оценочный конструкт оценивается.

Каждый оценивание ДОЛЖЕН иметь один основной аспект оценивания / оценочный конструкт.

семантика аспекта ДОЛЖЕН быть resolvable.

Списки вроде reliability, risk, качество, robustness, применимость, reproducibility являются примерами, а не закрытым Core vocabulary.

3.2. идентичность аспекта и label

Label не определяет семантическая идентичность.

```text
"надёжность"
"reliability"
"fiabilité"
```

МОЖЕТ представлять одну и ту же concept идентичность.

3.3. состав аспекта

Aspect СЛЕДУЕТ выражать оцениваемое свойство.

Target, Context и Scope СЛЕДУЕТ использовать собственные механизмы, если эти семантика содержательно разделимы.

профильs СЛЕДУЕТ определять каноническое представление для повторяющихся предметных шаблонов.

3.4. основание оценивания

основание оценивания — определённую логику оценивания, method, систему критериев, rule, model, scale или иная структура, по которой Target/входs интерпретируются в результат.

Basis МОЖЕТ быть composite.

Core не требует exactly one метод.

Basis МОЖЕТ включать Criterion, Metric, Threshold, Rule, шкала, Weight, агрегирование метод, методology, Benchmark, Model, Formula или экспертную процедуру.

Эти элементы не являются универсальными обязательными сущностями ядра.

3.5. Basis ≠ входs ≠ происхождение

```text
Evaluation Basis
≠ Assessment Inputs
≠ execution provenance
≠ Record provenance
```

семантическое различие не требует отдельных систем хранения.

Одна происхождение infrastructure МОЖЕТ хранить несколько семантические уровни.

3.5.1. Criterion ≠ вход

Criterion определяет, как или по какому условию производится оценивание.

вход определяет, какой материал фактически используется при оценивании.

```text
Criterion ≠ Input satisfying Criterion
```

Criterion и фактический материал, использованный для проверки Criterion, ДОЛЖЕН оставаться семантически различимыми.

3.6. результат оценивания

Completed оценивание ДОЛЖЕН иметь exactly one определённый результат оценивания.

результат МОЖЕТ быть qualitative, categorical, ordinal, numeric, probabilistic, interval/distribution, comparative, ranking, textual или structured.

Datatype не определяет ontology.

3.7. структурированный результат

структурированный результат допустим, если components образуют один профиль-определённый coherent оценочный конструкт.

структурированный результат НЕ ДОЛЖЕН становиться произвольный контейнер.

Если component требует самостоятельной addressability, происхождение, конкурирующее оценивание или lifecycle, он СЛЕДУЕТ быть promoted в отдельный оценивание или иной explicit Record.

3.8. семантика результата

результат ДОЛЖЕН быть интерпретируем относительно Aspect и существенно необходимый Basis/шкала.

результат = 3 не является достаточно определённый, если неизвестно, что означает 3.

3.9. Порядок результата ≠ желательность

Ordered scale не означает automatic good/bad polarity.

high reliability, high risk и high неопределённость имеют разные желательность семантика.

Core не предполагает универсальную монотонность.

3.10. Measurement vs оценивание

Measurement и оценивание различаются семантика, а не datatype.

error rate = 4.2% может быть Measurement.

Если профиль определяет эту величину как evaluative результат, она МОЖЕТ быть результат оценивание.

Количественное представление не даёт automatic эпистемического превосходства.

────────

4. вход оцениванияs, Evidence & Provenance

4.1. вход оценивания

вход оценивания — разрешимый информационный или фактический объект, содержание или состояние которого materially используется при получении результат.

оценивание МОЖЕТ иметь 0..N явные входы.

Explicit входs не являются universal Core requirement.

4.2. Допустимые входs

вход оценивания МОЖЕТ быть Evidence Use, Source, Claim, Measurement, Dataset, метод output, другим оценивание, derived value или иным определённый object.

4.3. Evidence Use vs вход оценивания

Если material используется как атомарное evidence относительно Claim, СЛЕДУЕТ использоваться Evidence Use.

Если material является технический или оценочный вход процесса оценивание, он МОЖЕТ быть direct вход оценивания.

```text
Evidence Use
≠ Assessment Input
```

Evidence Use МОЖЕТ быть вход оценивания.

4.3.1. Citation/reference ≠ вход membership

Наличие Source, Claim или иного Record в citation, rationale, discussion или reference НЕ ДОЛЖЕН автоматически означать вход оценивания membership.

Фактическая роль объекта — вход, Target, Basis reference, citation, происхождение reference или иная роль — должна оставаться resolvable, когда различие materially важно.

```text
citation/reference ≠ automatically Assessment Input
```

4.4. Target как implicit input

Если оценивание непосредственно использует свойства Target, которые уже resolvable через Target reference, отдельная duplicate вход reference не обязательна.

4.5. Historical входs

Completed оценивание ДОЛЖЕН сохранять историческую фактически использованную основу входных данных, если он materially significant.

New вход НЕ ДОЛЖЕН молча добавляться к старому completed оценивание.

динамический выбор входов ДОЛЖЕН сохранять membership или достаточный неизменяемый контекст реконструкции, если membership materially влияет на результат.

4.6. состояние входа

Существенно значимый состояние входа ДОЛЖЕН оставаться resolvable.

Для вход оценивания, который является Source, состояние входа ДОЛЖЕН быть семантически отличим от версии записи Source. Если исторически значимое состояние самого Source materially влияет на результат, именно это Source состояние ДОЛЖЕН оставаться resolvable.

Для вход оценивания, который является Evidence Use, исторически значимый Source Context, включая Source состояние и иные уровни Source, ДОЛЖЕН оставаться resolvable настолько, насколько они materially необходимы для интерпретации фактически использованного свидетельства. оценивание НЕ ДОЛЖЕН заменять такую историческую определённость текущей версией Source запись или текущим состоянием Source.

```text
Input@v3
≠ Input@current automatically

Source record version
≠ Source State automatically
```

4.7. неполнота данных

Нужно различать missing, неизвестный, not measured, not applicable, zero, not detected, excluded.

Эти состояния НЕ ДОЛЖЕН молча collapse, если различие materially важно.

4.8. Selection происхождение

критерий выбора может быть частью Basis.

выполнение выбора — process/происхождение.

выбранные объекты — входs.

Эти роли ДОЛЖЕН оставаться различимыми.

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

Materially significant фильтрацию, нормализацию, импутацию, взвешивание или transformation между входs и результат ДОЛЖЕН оставаться resolvable.

4.11. Зависимость

Different оценивание IDs или different reviewer identities не устанавливают independence.

```text
unknown dependence
≠ independence
```

Dependence МОЖЕТ быть partial, pairwise, methodology-relative, source-relative или неизвестный.

Core не требует universal binary independent=true/false.

4.12. Self-support

оценивание НЕ ДОЛЖЕН использовать собственный результат как independent доказательное обоснование того же результат.

Defined recursive/вычисление неподвижной точки МОЖЕТ существовать, если recursion является частью explicit основание оценивания и не представляется как независимое подтверждение.

Indirect dependency cycles ДОЛЖЕН оставаться detectable, когда существенно значимый.

────────

5. Identity, Lifecycle & Переоценивание

5.1. идентичность оценивания

оценивание имеет устойчивую идентичность Record, inherited from generic Record infrastructure.

Identity НЕ ДОЛЖЕН вычисляться из Target + Aspect + результат или других семантических кортежей.

Same результат ≠ same оценивание.

5.2. дискретное оценивание

дискретное оценивание обычно представляет один исторический акт оценивания.

5.3. Исправление

Исправление исправляет representation того же акт оценивания.

Если действие действительно является Исправление, идентичность оценивания ДОЛЖЕН сохраняться.

Примеры: transcription error, mistaken reference, metadata enrichment, clarification без нового evaluative reasoning.

Если исправление меняет акт оценивания настолько, что возникает новый акт оценивания, это ДОЛЖЕН рассматриваться как Переоценивание или иной новый оценивание, а не как Исправление.

5.4. Переоценивание

Переоценивание — новый акт оценивания.

Переоценивание ДОЛЖЕН иметь новую идентичность оценивания.

Исключение не допускается за счёт переименования Переоценивание в состояние update. Если заранее определённый профиль поддерживает Непрерывное оценивание с одной persistent Identity, последующее вычисление/обновление, являющееся частью этой continuous идентичность, не является Переоценивание в смысле настоящего раздела.

Same assessor МОЖЕТ создать новый оценивание.

5.5. Проверка ≠ Переоценивание

Проверка имеет Target = prior оценивание и оценивает сам оценивание.

Переоценивание имеет Target = original/related Target и оценивает Target заново.

Один process МОЖЕТ породить оба Records.

5.6. Непрерывное оценивание

профиль МОЖЕТ определить continuously maintained оценивание идентичность.

В этом случае повторные вычисления МОЖЕТ быть исторические состояния одной оценивание идентичность.

Continuous линия происхождения ДОЛЖЕН быть определена до или независимо от конкретного изменения результат и НЕ ДОЛЖЕН объявляться задним числом только для избежания новой Identity.

Historical continuous состояниеs ДОЛЖЕН сохранять существенно значимый состояние цели, вход membership/states, Basis/метод version, Context и результат.

5.7. Identity линия происхождения ≠ reassessment линия происхождения

Связанные Переоцениваниеs МОЖЕТ образовывать исторический линия происхождения, но это не означает одну идентичность оценивания.

```text
related reassessment lineage
≠ same Assessment identity
```

5.8. Замещение

оценивание МОЖЕТ быть superseded другим.

```text
superseded
≠ deleted
≠ false
```

Замещение СЛЕДУЕТ иметь resolvable область/контекст, если она не универсальна.

Core НЕ ДОЛЖЕН предполагать one global current оценивание.

5.8.1. Branching supersession

Замещение МОЖЕТ быть branching и профиль/Context-relative.

```text
Assessment A
├── Assessment B preferred under Profile P1
└── Assessment C preferred under Profile P2
```

Core НЕ ДОЛЖЕН предполагать одну глобальную линейную цепочку old → new → uniquely valid.

5.8.2. Отзыв

оценивание МОЖЕТ быть withdrawn.

```text
withdrawn ≠ deleted ≠ false
```

Отзыв означает изменение lifecycle/operational status, а не автоматическое утверждение о falsity результат.

Materially important reason for withdrawal СЛЕДУЕТ оставаться traceable, если это разрешено применимыми legal/privacy/security constraints.

Historical оценивание СЛЕДУЕТ сохраняться where permitted. Если внешний обязательный constraint требует physical deletion, такое удаление НЕ ДОЛЖЕН маскироваться как обычная correction или reassessment.

5.9. Latest / preferred / applicable / active

```text
latest
≠ preferred
≠ applicable
≠ active
≠ true
```

current не является Core concept без определённый профиль семантика.

5.10. Migration

Carrier migration, serialization или import transport не являются Переоценивание.

Carrier ≠ идентичность оценивания.

────────

6. Context, Applicability & область оценивания

6.1. контекст оценивания

контекст оценивания — внешние условия, назначение и ограничения применения, относительно которых результат должен интерпретироваться.

Context является условно обязательными.

Если без него результат materially меняет смысл или может быть неправильно применён, Context ДОЛЖЕН быть resolvable.

6.2. Context ≠ Target

Target отвечает: что оценивается?

Context: при каких внешних условиях / для какого применения?

Если второй participant является частью самого evaluated relation, СЛЕДУЕТ использоваться реляционную цель.

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

Applicability не является universal intrinsic bool оценивание.

результат оценивания интерпретируется внутри собственного исходного семантическая оболочка без требования отдельного universal Applicability оценивание.

Отдельный вопрос Applicability возникает прежде всего при reuse/transfer существующего результат за пределы исходного семантическая оболочка — например, на другой Target, состояние, Context или use-case.

Она МОЖЕТ быть профиль-определённый mapping, отдельным оценивание или определённый inference.

6.6. перенос между контекстами

результат НЕ ДОЛЖЕН автоматически переноситься между materially different Claims, populations, domains, Contexts, состояние целиs или versions.

Cross-контекст reuse МОЖЕТ происходить только при resolvable semantic equivalence, transfer rule, mapping или отдельном reasoning step.

сопоставимость/transfer МОЖЕТ быть Aspect-relative.

6.7. наследование контекста

Context МОЖЕТ наследоваться из профиль.

Существенно значимый inherited Context ДОЛЖЕН разрешаться к исторический профиль/Context состояние, реально применявшемуся к оценивание.

6.8. динамический контекст

Dynamic labels вроде current law, current standard, current risk level НЕ ДОЛЖЕН молча изменять исторический оценивание семантика.

6.9. Временные роли

Следует различать оценивание creation time, состояние цели time и период применимости.

6.10. Geographic roles

Следует различать assessor location, Target location и география применимости.

6.11. семантическая оболочка

оценивание семантическая оболочка — аналитическое понятие, а не Core Entity и не mandatory field.

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

результат НЕ ДОЛЖЕН молча переноситься за пределы своего семантическая оболочка без определённый mapping, inference, оценивание или профиль rule.

────────

7. качество оценивания, неопределённость & уверенность

7.1. оценивание-of-оценивание

оценивание МОЖЕТ быть Target другого оценивание.

Новая Entity Metaоценивание не требуется.

7.2. Meta-level privilege отсутствует

```text
meta-level
≠ epistemic privilege
```

оценивание-of-оценивание МОЖЕТ быть ошибочным и МОЖЕТ сам быть reviewed.

7.3. Quality ≠ Correctness

```text
Assessment quality
≠ Result correctness
```

Good methodology не гарантирует true/correct результат.

Correct результат не доказывает good methodology.

7.4. мета-аспекты

аспекты, связанные с качеством могут включать methodological adequacy, robustness, reproducibility, transparency, traceability, bias risk, calibration, применимость, confidence.

Этот список является illustrative, не Core vocabulary.

7.5. неопределённость layers

Следует различать Target неопределённость, вход неопределённость, результат неопределённость, уверенность in результат, Model confidence, Applicability неопределённость.

неопределённость/уверенность ДОЛЖЕН иметь resolvable referent.

7.6. вероятность ≠ уверенность

```text
P(Claim true)
≠ confidence in estimate
≠ model confidence
```

Equal numeric range не означает equal семантика.

7.7. уверенность ≠ inverse неопределённость

Core НЕ ДОЛЖЕН предполагать confidence = 1 - неопределённость.

High неопределённость Target МОЖЕТ coexist with high confidence в том, что неопределённость действительно high.

7.8. Representation confidence/неопределённость

профиль МОЖЕТ представлять confidence/неопределённость как structured component результат, отдельный Evaluation Aspect или meta-оценивание.

Core не требует redundant representation.

7.9. Propagation

Quality, confidence, неопределённость и иные оценивание properties НЕ ДОЛЖЕН автоматически compose/propagate через входs, методs, Targets или meta-levels без определённый evaluative rule.

7.10. рекурсивная проверка

Recursive оценивание МОЖЕТ существовать, но recursive closure не является Core requirement.

Meta-review depth определяется профиль/risk requirements.

Core не требует elimination of all неопределённость.

High-risk stopping principle: выполнить предусмотренные профиль requirements для review, independence, неопределённость handling, validation/reproducibility, а не бесконечно продолжать review.

────────

8. агрегирование, сравнение & синтез

8.1. сравнение ≠ агрегирование

сравнение отвечает: насколько оцениваниеs отличаются и сопоставимы?

агрегирование: можно ли получить новый результат из нескольких входs?

8.2. синтез

синтез — более широкая process/function category, а не обязательная Core Entity.

```text
evaluative synthesis → Assessment
inferential synthesis → Inference / Argument
action-selecting synthesis → Decision
```

Один process МОЖЕТ produce multiple Records.

8.3. Aggregate оценивание

Aggregate оценивание — обычный оценивание, использующий prior оцениваниеs и/или другие objects как входs.

Universal Entity Aggregateоценивание не требуется.

Aggregate status не даёт automatic эпистемического превосходства.

8.4. агрегирование optional

Несколько оцениваниеs МОЖЕТ сосуществовать без единого aggregate результат.

Plurality является допустимым состоянием знания.

8.5. Majority / latest / authority

Core не использует правила majority wins, latest wins, authority wins, project wins как universal epistemic семантика.

Voting МОЖЕТ быть профиль-определённый aggregation method, но vote count не имеет universal truth meaning.

8.6. сопоставимость

сопоставимость является operation-relative.

```text
comparable for ranking
≠ comparable for arithmetic mean
≠ comparable for statistical pooling
```

Same Aspect или same label не гарантирует comparability.

8.7. Cross-Aspect synthesis

Different Aspects МОЖЕТ участвовать в новом оценивание при explicit evaluative model.

Они НЕ ДОЛЖЕН молча collapse в один score.

Если synthesis выбирает действие, это МОЖЕТ переходить в Decision.

8.8. Unsupported Scalarization

Scalarization сама по себе допустима.

Unsupported Scalarization — превращение multidimensional, ordinal или otherwise non-scalar результатs в scalar без определённый semantically valid mapping.

8.9. Зависимость overlap

агрегирование должна учитывать существенно значимый dependency overlap, не только exact вход идентичность.

Repeated use of same вход не запрещено само по себе.

Запрещено представлять repeated/dependent contribution как независимое подтверждение без определённый justification.

8.10. уверенность amplification

Совпадающие/high-confidence оцениваниеs НЕ ДОЛЖЕН автоматически повышать aggregate confidence только из-за количества.

8.11. конфликт

Перед substantive conflict СЛЕДУЕТ сравниваться семантическая оболочкаs.

Different Basis МОЖЕТ всё равно давать substantive разногласие, если evaluative question sufficiently aligned.

Disagreement МОЖЕТ быть component-level.

конфликт не требует forced resolution.

8.12. Agreement ≠ Truth

```text
90% agreement
≠ 90% probability true
```

Consensus/Agreement score НЕ ДОЛЖЕН молча превращаться в truth probability или confidence.

8.13. Inconclusive

inconclusive МОЖЕТ быть legitimate профиль-определённый результат.

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

Эти слои МОЖЕТ пересекаться.

9.2. Core соответствие

оценивание Core-conformant, если он представляет допустимый оценивание Record с resolvable Target, resolvable primary Aspect/construct, определённый результат если completed, и sufficient structural, referential, semantic и контекстual-исторический resolution всех materially necessary элементов.

9.2.1. Structural соответствие

Structural соответствие относится к required structure, cardinality, допустимым формам и lifecycle completeness оценивание Record.

9.2.2. Referential соответствие

Referential соответствие относится к корректной разрешимости существенно необходимый references, включая Target, входs, состояниеs, профиль, шкала, метод и иные referenced objects.

9.2.3. Semantic соответствие

Semantic соответствие относится к достаточной определённости и интерпретируемости Aspect, результат, шкала, roles и иных существенно значимый семантика.

9.2.4. Contextual-Historical соответствие

Contextual-Historical соответствие относится к сохранению materially necessary Context, Scope, исторические состояния, versions и применимость boundaries, необходимых для честной интерпретации исторический результат.

Эти виды соответствие МОЖЕТ пересекаться; одна проблема МОЖЕТ затрагивать несколько слоёв одновременно.

9.3. соответствие ≠ правильность

```text
Core Conformance
≠ Truth
≠ Epistemic Quality
≠ Project Endorsement
```

Core-conformant оценивание МОЖЕТ быть methodologically poor.

Epistemically plausible оценивание МОЖЕТ быть non-conformant как Record.

9.4. целостность / Provenance Failure

целостность Failure — несоответствие зарегистрированной идентичность, происхождение, входs, authorship, history или derivation тому, что фактически произошло или должно быть resolvable.

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

9.6. Epistemic / методological Failure

оценивание МОЖЕТ быть Core-conformant и при этом иметь selection bias, inappropriate метод, invalid inference, bad assumptions, unsupported generalization или poor statistics.

Это отдельный слой.

9.7. Governance / Operational Failure

Относится к publication, фильтрацию, preference, UI representation, export/import claims, deletion, одобрение, operational use.

Canonical Record МОЖЕТ быть conformant при misleading UI.

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

Explicit определённый mapping/inference/профиль rule МОЖЕТ legitimately transform семантика.

9.10. подмена жизненного цикла

Новый акт оценивания НЕ ДОЛЖЕН маскироваться как simple correction.

К этому относятся Silent Переоценивание, Fake Исправление, Revision Laundering.

9.11. смещение состояния / версии

Historical оценивание НЕ ДОЛЖЕН молча reinterpret через materially different состояние цели, состояние входа, шкала version, профиль version, Context definition или метод version.

9.12. Representation fidelity

Canonical оценивание conformance и representation fidelity различаются.

Lossy representations МОЖЕТ быть допустимы.

Failure возникает, если representation заявляет полная точность представления, но materially necessary семантика потеряна; применимый профиль требует более высокой fidelity; либо presentation создаёт materially misleading interpretation.

9.13. Selection/фильтрацию

Показ одного оценивание из многих не является failure сам по себе.

Failure возникает, если representation ложно утверждает отсутствие alternatives/consensus или нарушает declared профиль/governance семантика.

9.14. Import

Unknown imported семантика ДОЛЖЕН remain неизвестный.

Lossy/partial import МОЖЕТ существовать, но НЕ ДОЛЖЕН заполнять отсутствующую семантика догадкой и заявлять full оценивание equivalence.

9.15. Downstream impact

Upstream correction/withdrawal НЕ ДОЛЖЕН молча mutate исторический последующие результаты.

Affected downstream dependency МОЖЕТ потребовать review/reassessment.

```text
affected
≠ automatically invalid
```

Known существенно значимый downstream dependencies СЛЕДУЕТ remain discoverable; профиль МОЖЕТ повышать это до ДОЛЖЕН.

────────

10. Core выводы стресс-тестирования

Эта глава фиксирует результаты системного stress testing и не вводит новых Core Entities.

10.1. Minimal expert оценивание — PASS

Простой qualitative оценивание без numeric score и без явные входы МОЖЕТ быть Core-conformant.

10.2. Machine conformance оценивание — PASS

Machine оценивание использует тот же Core и не получает epistemic privilege.

10.3. Mutable Target/вход — PASS

Historical состояниеs остаются resolvable и не следуют current состояние автоматически.

10.4. Relational/цель уровня множестваs — PASS

Допустимы при определённый Target семантика.

10.5. динамическая цель/вход selection — PASS

Historical membership должен быть closed/reconstructable, если materially important.

10.6. Probabilistic/qualitative/structured результатs — PASS

Core не зависит от одной mathematical ontology.

10.7. Непрерывное оценивание — PASS

Допустим при профиль-определённый lifecycle и сохранении исторические состояния.

10.8. Meta-оценивание — PASS

Отдельная Entity не требуется.

10.9. конфликтing оцениваниеs — PASS

Plurality без forced consensus является legitimate knowledge state.

10.10. агрегирование — PASS

Aggregate оценивание является ordinary оценивание; aggregation optional.

10.11. Offline preservation — PASS

оценивание Core не зависит от URL, HTTP, JSON, GitHub или иной текущей технологии.

10.12. Multilingual representation — PASS

Label language не определяет семантическая идентичность.

10.13. Physical/non-digital Targets — PASS

Target не обязан быть цифровым object.

10.14. Historical неизвестный семантика

Если сохранена запись Target: S / Value: 4, но Aspect/шкала неизвестны, система ДОЛЖЕН сохранять неизвестный семантика вместо догадки.

10.15. Full fidelity

Full fidelity означает семантическая восстановимость, а не byte-for-byte идентичность.

Разные carrier representations МОЖЕТ представлять один оценивание.

10.16. Project self-authority test — PASS

оценивание, созданный или preferred проектом, не становится Truth автоматически.

10.17. расширяемость профилей — PASS

Future профильs МОЖЕТ добавлять новые Aspects, методs, шкалаs, review requirements и confidence models без переписывания Core.

────────

11. Канонические инварианты ядра

Ниже только фундаментальные инварианты оценивание Core. Остальные правила документа являются семантические правила, правила профилей, принципы сохранения или диагностические предохранители.

1. оценивание является специализированным Record.
2. Каждый оценивание ДОЛЖЕН иметь exactly one определённую структуру цели.
3. Каждый оценивание ДОЛЖЕН иметь exactly one основной аспект оценивания / оценочный конструкт.
4. Каждый completed оценивание ДОЛЖЕН иметь exactly one определённый результат оценивания.
5. оценивание Target structure ДОЛЖЕН иметь определённый evaluative семантика и НЕ ДОЛЖЕН быть произвольный контейнер.
6. результат оценивания ДОЛЖЕН быть интерпретируем относительно Aspect и существенно необходимый семантика.
7. результат НЕ ДОЛЖЕН молча escape существенно значимый Target/состояние/Aspect/Scope/Context/Basis семантика.
8. оценивание НЕ ДОЛЖЕН молча change исторический Target/вход/профиль/шкала/Context/метод семантика.
9. оценивание НЕ ДОЛЖЕН использовать собственный результат как independent доказательное обоснование того же результат; определённый computational recursion не считается независимое подтверждение.
10. результат оценивания НЕ ДОЛЖЕН автоматически становиться Truth, Decision, Consensus или Project Endorsement.
11. профиль НЕ ДОЛЖЕН отменять инварианты ядра, одновременно заявляя совместимость с ядром.
12. Unknown семантика НЕ ДОЛЖЕН заменяться invented семантика.
13. Historical evaluative meaning НЕ ДОЛЖЕН молча be rewritten by later состояние, correction, migration or reassessment.
14. идентичность оценивания НЕ ДОЛЖЕН выводиться только из semantic tuple вроде Target + Aspect + результат.
15. New акт оценивания НЕ ДОЛЖЕН маскироваться как technical correction.
16. Dependent/repeated входs/оцениваниеs НЕ ДОЛЖЕН маскироваться как независимое подтверждение.
17. Same label, number, результат или reviewer идентичность НЕ ДОЛЖЕН автоматически означать same семантика, same оценивание или independence.
18. Core соответствие НЕ ДОЛЖЕН интерпретироваться как правильность, качество или одобрение.
19. оценивание architecture ДОЛЖЕН оставаться предметно-нейтральной и технологически нейтральной.
20. оценивание Core ДОЛЖЕН позволять неопределённость, множественность, разногласие и неполное знание без принудительного выдумывания единого ответа.

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

13. профиль rules

профильs МОЖЕТ требовать явные входы, вводить domain vocabularies, определять шкалаs, требовать Target/вход snapshots, задавать confidence/неопределённость representation, устанавливать review depth, требовать independent Проверка, определять aggregation methods, continuous lifecycle и усиливать preservation requirements.

профильs НЕ ДОЛЖЕН ослаблять инварианты ядра при заявленной совместимость с ядром.

соответствие claim ДОЛЖЕН быть областьd к конкретному профиль/version.

────────

14. принципы сохранения

1. Material исторический семантика СЛЕДУЕТ оставаться recoverable.
2. Resolvability не требует текущего online access.
3. Full fidelity означает семантическая восстановимость.
4. Carrier migration не создаёт Переоценивание.
5. Historical оценивание МОЖЕТ пережить утрату non-material metadata.
6. Потеря существенно необходимый семантика МОЖЕТ сделать результат unresolved.
7. Later recovery of lost семантика МОЖЕТ быть correction/enrichment без нового акт оценивания.
8. Offline/printed representation СЛЕДУЕТ быть возможна без изменения Core meaning.
9. Technology-specific storage details НЕ ДОЛЖЕН определять оценивание идентичность.
10. Preservation профиль МОЖЕТ усиливать эти требования для долгосрочного архива.

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

> **Чем сложнее конкретный оценивание, тем больше Context, входs, Basis, происхождение и history может быть materially необходимо. Но сложность конкретной оценки не должна становиться обязательной сложностью каждого оценивание.**

Принцип эпистемической честности:

> **Если система не может честно определить Target, оценочный конструкт, результат или materially necessary семантика, она должна сохранить неопределённость или неполноту, а не изобретать недостающий смысл.**

────────

Статус

После интеграционного аудита с актуальными 001–004, локальных аудитов глав 1–10, сквозной атаки глав 1–9, аудита главы 10 и контрольного destructive audit архитектура оценивание зафиксирована как канонический стандарт v0.2 005-ASSESSMENT.md.
