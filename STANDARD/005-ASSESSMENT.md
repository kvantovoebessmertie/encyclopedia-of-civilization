005-ASSESSMENT.md

Статус: канонический стандарт v0.2
Проект: Энциклопедия цивилизации
Назначение: определить универсальную модель Assessment (оценивания) для Claims, Sources, Evidence Uses, методs, Assessments, физических объектов, отношений, множеств и иных определённых Targets.

────────

0. Назначение стандарта

Assessment — это специализированная запись (Record), представляющий результат оценивания определённого Target относительно определённого оценочный конструкт.

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

Assessment — специализированная запись (Record), представляющий один определённый акт оценивания или, если это заранее определено Profile, одну непрерывная идентичность оценивания с сохраняемыми историческими States.

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

Completed Assessment ДОЛЖНО иметь:

1. один определёнными структура цели;
2. один primary аспект оценивания / оценочный конструкт;
3. один определёнными результат оценивания.

Дополнительные элементы являются условно обязательными и включаются только тогда, когда без них существенно нарушается смысл Assessment.

1.3. Defined

«Defined» означает: имеющий достаточно определённую semantics для однозначной интерпретации в пределах применимого Standard/Profile.

определённое понятие не обязан существовать как отдельный Record.

1.4. Resolvable

«Resolvable» означает: объект, State, отношение или semantics могут быть однозначно установлены из сохранённой структуры, history, provenance или references без изобретения отсутствующего смысла.

```text
resolvable ≠ currently online
```

1.5. Materially relevant / required

Элемент является существенно relevant, если его отсутствие, изменение или неверное представление способно существенно изменить:

• идентичность;
• интерпретацию;
• сопоставимость;
• воспроизводимость;
• применимость;
• или оценку Result.

1.6. Draft и завершённое оценивание

Draft/in-progress Assessment Record МОЖЕТ временно быть неполным согласно общим жизненным циклом Record.

Completed Assessment ДОЛЖНО иметь определёнными Result.

Отсутствие Result в draft не делает сам Record невозможным; отсутствие Result в записи, заявленной как завершённое оценивание, является Core conformance failure.

────────

2. цель оценивания

2.1. структура цели

Каждый Assessment ДОЛЖНО иметь exactly one определёнными структура цели.

Это не означает exactly one Target Record.

структура цели МОЖЕТ представлять:

• одиночная цель;
• адресуемая подцель;
• реляционная цель;
• цель уровня множества.

2.2. Relational Target

Если оцениваемое свойство существует между несколькими участники, Target МОЖЕТ быть отношениеal:

```text
Target:
(EU-A, EU-B)

Aspect:
independence
```

Roles/order ДОЛЖНО быть разрешимыми, если отношение асимметрична или порядок существенно влияет на смысл.

2.3. Set-level Target

Assessment МОЖЕТ оценивать множество как единый Target:

```text
Target:
[EU-1, EU-2, EU-3]

Aspect:
methodological diversity
```

Set-level Assessment ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО использоваться для скрытого объединения независимых member-level акт оцениванияs.

Legitimate Profile-определёнными collective predicate МОЖЕТ иметь implications для members, но:

```text
Assessment(set)
≠ automatically collection of Assessment(member)
```

2.4. Heterogeneous Targets

структура цели ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО превращаться в произвольный контейнер семантически несвязанных объектов.

Если несколько участники входят в Target, их роли и общий evaluative смысл должны быть определёнными.

2.5. Sub-target

Если Result утверждается о самостоятельно адресуемый компонент как об отдельном объект оценивания, этот компонент СЛЕДУЕТ быть представлен как sub-target.

Если компонент лишь ограничивает область рассмотрения свойства более широкого Target, МОЖЕТ использоваться Область оценивания.

2.6. Target State

Если Target изменяемая и его State существенно влияет на Assessment, соответствующее состояние цели ДОЛЖНО оставаться разрешимыми.

```text
Assessment(Target@v1)
≠ automatically
Assessment(Target@v2)
```

New Target State ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО молча менять historical Assessment.

2.7. Динамическая цель

Target МОЖЕТ определяться процесс запроса/фильтрации/выбора.

Completed Assessment ДОЛЖНО сохранять семантически замкнутую историческую цель через resolved membership либо достаточный imизменяемая reconstruction context.

Timestamp alone не гарантирует воспроизводимость historical Target.

────────

3. аспект оценивания, Basis & Result

3.1. аспект оценивания

аспект оценивания определяет, какое свойство или оценочный конструкт оценивается.

Каждый Assessment ДОЛЖНО иметь один primary аспект оценивания / оценочный конструкт.

семантика аспекта ДОЛЖНО быть разрешимыми.

Списки вроде reliability, risk, quality, robustness, applicability, reproducibility являются примерами, а не закрытым Core vocabulary.

3.2. Aspect identity и метка

Label не определяет семантическая идентичность.

```text
"надёжность"
"reliability"
"fiabilité"
```

MAY представлять одну и ту же concept identity.

3.3. Состав аспекта

Aspect СЛЕДУЕТ выражать оцениваемое свойство.

Target, Context и Scope СЛЕДУЕТ использовать собственные механизмы, если эти semantics содержательно разделимы.

Profiles СЛЕДУЕТ определять каноническое представление для повторяющихся предметных шаблонов.

3.4. основание оценивания

основание оценивания — определёнными evaluative logic, method, система критериев, rule, model, scale или иная структура, по которой Target/Inputs интерпретируются в Result.

Basis МОЖЕТ быть составным.

ядро не требует exactly one метод.

Basis МОЖЕТ включать критерий, метрика, порог, правило, шкала, вес, Агрегирование метод, методology, эталон, модель, формула или экспертная процедура.

Эти элементы не являются универсальными обязательными сущностями ядра.

3.5. Basis ≠ Inputs ≠ provenance

```text
Evaluation Basis
≠ Assessment Inputs
≠ execution provenance
≠ Record provenance
```

Семантическое различие не требует отдельных систем хранения.

Одна инфраструктура происхождения МОЖЕТ хранить несколько семантические уровни.

3.5.1. критерий ≠ Input

критерий определяет, как или по какому условию производится оценивание.

Input определяет, какой материал фактически используется при оценивании.

```text
Criterion ≠ Input satisfying Criterion
```

критерий и фактический материал, использованный для проверки критерий, ДОЛЖНО оставаться семантически различимыми.

3.6. результат оценивания

Completed Assessment ДОЛЖНО иметь exactly one определёнными результат оценивания.

Result МОЖЕТ быть качественным, категориальным, порядковым, числовым, вероятностным, интервальным/распределительным, сравнительным, ранжированием, текстовым или структурированным.

тип данных не определяет онтологию.

3.7. структурированный результат

структурированный результат допустим, если компонентs образуют один Profile-определёнными coherent оценочный конструкт.

структурированный результат ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО становиться произвольный контейнер.

Если компонент требует самостоятельной addressability, provenance, конкурирующее оценивание или жизненный цикл, он СЛЕДУЕТ быть вынесен в отдельный Assessment или иной explicit Record.

3.8. семантика результата

Result ДОЛЖНО быть интерпретируем относительно Aspect и существенно required Basis/шкала.

Result = 3 не является достаточно определёнными, если неизвестно, что означает 3.

3.9. Result ordering ≠ desirability

Ordered scale не означает автоматическую полярность «хорошо/плохо».

high reliability, high risk и high uncertainty имеют разные desirability semantics.

Core не предполагает универсальную монотонность.

3.10. Измерение и оценивание

Измерение и оценивание различаются семантикой, а не типом данных.

error rate = 4.2% может быть Measurement.

Если Profile определяет эту величину как evaluative Result, она МОЖЕТ быть Result Assessment.

Количественная форма не даёт автоматического эпистемического превосходства.

────────

4. вход оцениванияs, Evidence & Provenance

4.1. вход оценивания

вход оценивания — разрешимый информационный или фактический объект, содержание или State которого существенно используется при получении Result.

Assessment МОЖЕТ иметь 0..N явные входы.

Explicit Inputs не являются универсальное требование ядра.

4.2. Допустимые Inputs

вход оценивания МОЖЕТ быть Evidence Use, Source, Claim, Measurement, Dataset, метод output, другим Assessment, производное значение или иным определёнными object.

4.3. Evidence Use vs вход оценивания

Если material используется как атомарное evidence относительно Claim, СЛЕДУЕТ использоваться Evidence Use.

Если material является технический или оценочный вход процесса Assessment, он МОЖЕТ быть direct вход оценивания.

```text
Evidence Use
≠ Assessment Input
```

Evidence Use МОЖЕТ быть вход оценивания.

4.3.1. Citation/reference ≠ принадлежность к входам

Наличие Source, Claim или иного Record в citation, rationale, discussion или reference ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО автоматически означать вход оценивания membership.

Фактическая роль объекта — Input, Target, Basis reference, citation, provenance reference или иная роль — должна оставаться разрешимыми, когда различие существенно важно.

```text
citation/reference ≠ automatically Assessment Input
```

4.4. Target как implicit input

Если Assessment непосредственно использует свойства Target, которые уже разрешимыми через Target reference, отдельная дублирующая ссылка на вход не обязательна.

4.5. Исторические входы

Completed Assessment ДОЛЖНО сохранять историческую фактически использованную основу входных данных, если он существенно significant.

New Input ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО молча добавляться к старому завершённое оценивание.

Динамический выбор входов ДОЛЖНО сохранять membership или достаточный imизменяемая reconstruction context, если membership существенно влияет на Result.

4.6. состояние входа

Materially relevant состояние входа ДОЛЖНО оставаться разрешимыми.

Для вход оценивания, который является Source, состояние входа ДОЛЖНО быть семантически отличим от версии записи Source. Если исторически значимое состояние самого Source существенно влияет на Result, именно это Source State ДОЛЖНО оставаться разрешимыми.

Для вход оценивания, который является Evidence Use, исторически значимый Source Context, включая Source State и иные уровни Source, ДОЛЖНО оставаться разрешимыми настолько, насколько они существенно необходимы для интерпретации фактически использованного свидетельства. Assessment ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО заменять такую историческую определённость текущей версией Source record или текущим состоянием Source.

```text
Input@v3
≠ Input@current automatically

Source record version
≠ Source State automatically
```

4.7. неполнота данных

Нужно различать missing, unknown, not measured, not применимый, zero, not detected, excluded.

Эти состояния ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently collapse, если различие существенно важно.

4.8. происхождение выбора

критерий выбора может быть частью Basis.

выполнение выбора — process/provenance.

выбранные объекты — Inputs.

Эти роли ДОЛЖНО оставаться различимыми.

4.9. линия вывода результата

Следует различать:

```text
Record provenance
Evaluation execution provenance
Input selection provenance
Result derivation lineage
```

Но ядро не требует отдельного storage mechanism для каждого слоя.

4.10. Transformations

Materially significant фильтрация, нормализация, импутация, взвешивание или преобразование между Inputs и Result ДОЛЖНО оставаться разрешимыми.

4.11. Зависимость

Different Assessment IDs или different reviewer identities не устанавливают независимость.

```text
unknown dependence
≠ independence
```

Dependence МОЖЕТ быть partial, pairwise, methodology-relative, source-relative или unknown.

ядро не требует universal binary independent=true/false.

4.12. Self-support

Assessment ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО использовать собственный Result как independent evidential justification того же Result.

Defined recursive/вычисление неподвижной точки МОЖЕТ существовать, если recursion является частью explicit основание оценивания и не представляется как независимое подтверждение.

Косвенные циклы зависимости ДОЛЖНО оставаться detectable, когда существенно relevant.

────────

5. Identity, Lifecycle & Переоценивание

5.1. идентичность оценивания

Assessment имеет устойчивая идентичность Record, inherited from generic Record infrastructure.

Identity ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО вычисляться из Target + Aspect + Result или других семантических кортежах.

Одинаковый результат ≠ same Assessment.

5.2. Дискретное оценивание

Дискретное оценивание обычно представляет один historical акт оценивания.

5.3. Исправление

Исправление исправляет representation того же акт оценивания.

Если действие действительно является Исправление, идентичность оценивания ДОЛЖНО сохраняться.

Примеры: transcription error, mistaken reference, metadata enrichment, clarification без нового evaluative reasoning.

Если исправление меняет акт оценивания настолько, что возникает новый акт оценивания, это ДОЛЖНО рассматриваться как Переоценивание или иной новый Assessment, а не как Исправление.

5.4. Переоценивание

Переоценивание — новый акт оценивания.

Переоценивание ДОЛЖНО иметь новую идентичность оценивания.

Исключение не допускается за счёт переименования Переоценивание в State update. Если заранее определённый Profile поддерживает Непрерывное оценивание с одной устойчивой идентичностью, последующее вычисление/обновление, являющееся частью этой continuous identity, не является Переоценивание в смысле настоящего раздела.

Same assessor МОЖЕТ создать новый Assessment.

5.5. Проверка ≠ Переоценивание

Проверка имеет Target = prior Assessment и оценивает сам Assessment.

Переоценивание имеет Target = original/related Target и оценивает Target заново.

Один process МОЖЕТ породить оба Records.

5.6. Непрерывное оценивание

Profile МОЖЕТ определить continuously maintained Assessment identity.

В этом случае повторные вычисления МОЖЕТ быть исторические состояния одной Assessment identity.

Continuous lineage ДОЛЖНО быть определена до или независимо от конкретного изменения Result и ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО объявляться задним числом только для избежания новой Identity.

Historical continuous States ДОЛЖНО сохранять существенно соответствующее состояние цели, принадлежность к входам/states, Basis/метод version, Context и Result.

5.7. Identity lineage ≠ reassessment lineage

Связанные Переоцениваниеs МОЖЕТ образовывать historical lineage, но это не означает одну идентичность оценивания.

```text
related reassessment lineage
≠ same Assessment identity
```

5.8. Замещение

Assessment МОЖЕТ быть superseded другим.

```text
superseded
≠ deleted
≠ false
```

Замещение СЛЕДУЕТ иметь разрешимыми scope/context, если она не универсальна.

Core ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО предполагать one global current Assessment.

5.8.1. Branching supersession

Замещение МОЖЕТ быть branching и Profile/Context-relative.

```text
Assessment A
├── Assessment B preferred under Profile P1
└── Assessment C preferred under Profile P2
```

Core ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО предполагать одну глобальную линейную цепочку old → new → uniquely valid.

5.8.2. Отзыв

Assessment МОЖЕТ быть withdrawn.

```text
withdrawn ≠ deleted ≠ false
```

Отзыв означает изменение жизненный цикл/operational status, а не автоматическое утверждение о falsity Result.

Materially important reason for withdrawal СЛЕДУЕТ оставаться traceable, если это разрешено применимыми legal/privacy/security constraints.

Historical Assessment СЛЕДУЕТ сохраняться where permitted. Если внешний обязательный constraint требует physical deletion, такое удаление ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО маскироваться как обычная correction или reassessment.

5.9. Latest / предпочтительный / применимый / активный

```text
latest
≠ preferred
≠ applicable
≠ active
≠ true
```

current не является Core concept без определёнными Profile semantics.

5.10. Миграция

миграция носителя, сериализация или перенос при импорте не являются Переоценивание.

Carrier ≠ идентичность оценивания.

────────

6. Context, Применимость & Область оценивания

6.1. Контекст оценивания

Контекст оценивания — внешние условия, назначение и ограничения применения, относительно которых Result должен интерпретироваться.

Context является условно обязательными.

Если без него Result существенно меняет смысл или может быть неправильно применён, Context ДОЛЖНО быть разрешимыми.

6.2. Context ≠ Target

Target отвечает: что оценивается?

Context: при каких внешних условиях / для какого применения?

Если второй participant является частью самого evaluated отношение, СЛЕДУЕТ использоваться реляционная цель.

6.3. Область оценивания

Область оценивания — внутренняя граница реально выполненного evaluative task.

Scope условно обязательными, если Target + Aspect не задают evaluative boundary достаточно точно.

6.4. Context ≠ Scope

```text
Context
→ внешние условия применения

Scope
→ внутренняя область того, что реально оценивалось
```

6.5. Применимость

Применимость не является universal intrinsic bool Assessment.

результат оценивания интерпретируется внутри собственного исходного семантическую оболочку без требования отдельного universal Применимость Assessment.

Отдельный вопрос Применимость возникает прежде всего при повторном использовании/переносе существующего Result за пределы исходного семантическую оболочку — например, на другой Target, State, Context или use-case.

Она МОЖЕТ быть Profile-определёнными отображение, отдельным Assessment или определёнными inference.

6.6. Перенос между контекстами

Result ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО автоматически переноситься между существенно different Claims, populations, domains, Contexts, Target States или versions.

Cross-context reuse МОЖЕТ происходить только при разрешимыми semantic equivalence, transfer rule, отображение или отдельном этап рассуждения.

Сопоставимость/transfer МОЖЕТ быть Aspect-relative.

6.7. Наследование контекста

Context МОЖЕТ наследоваться из Profile.

Materially relevant inherited Context ДОЛЖНО разрешаться к historical Profile/Context State, реально применявшемуся к Assessment.

6.8. Динамический контекст

Dynamic меткаs вроде current law, current standard, current risk level ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently изменять historical Assessment semantics.

6.9. Временные роли

Следует различать Assessment creation time, время состояния цели и период применимости.

6.10. Geographic roles

Следует различать местоположение оценщика, местоположение цели и география применимости.

6.11. семантическую оболочку

Assessment семантическую оболочку — аналитическое понятие, а не Core Entity и не mandatory field.

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

вход оцениванияs не входят автоматически в семантическую оболочку, поскольку относятся прежде всего к derivation.

```text
Semantic Envelope
≠ Result Derivation Basis
```

6.12. семантическую оболочку Escape

Result ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО молча переноситься за пределы своего семантическую оболочку без определёнными отображение, inference, Assessment или Profile rule.

────────

7. Качество оценивания, Неопределённость & Уверенность

7.1. Assessment-of-Assessment

Assessment МОЖЕТ быть Target другого Assessment.

Новая Entity MetaAssessment не требуется.

7.2. Meta-level privilege отсутствует

```text
meta-level
≠ epistemic privilege
```

Assessment-of-Assessment МОЖЕТ быть ошибочным и МОЖЕТ сам быть reviewed.

7.3. Качество ≠ правильность

```text
Assessment quality
≠ Result correctness
```

Good methodology не гарантирует true/correct Result.

Correct Result не доказывает good methodology.

7.4. Мета-аспекты

Аспекты, связанные с качеством могут включать methodological adequacy, robustness, воспроизводимости, transparency, traceability, bias risk, calibration, applicability, confidence.

Этот список является illustrative, не Core vocabulary.

7.5. Неопределённость layers

Следует различать Target uncertainty, Input uncertainty, Result uncertainty, Уверенность in Result, модель confidence, Применимость uncertainty.

Неопределённость/Уверенность ДОЛЖНО иметь разрешимыми referent.

7.6. Probability ≠ Уверенность

```text
P(Claim true)
≠ confidence in estimate
≠ model confidence
```

Equal числовым range не означает equal semantics.

7.7. Уверенность ≠ inverse uncertainty

Core ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО предполагать confidence = 1 - uncertainty.

High uncertainty Target МОЖЕТ coexist with high confidence в том, что uncertainty действительно high.

7.8. Representation confidence/uncertainty

Profile МОЖЕТ представлять confidence/uncertainty как структурированным компонент Result, отдельный аспект оценивания или meta-Assessment.

ядро не требует redundant representation.

7.9. Распространение

Quality, confidence, uncertainty и иные Assessment properties ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО автоматически compose/propagate через Inputs, методs, Targets или meta-levels без определёнными evaluative rule.

7.10. Рекурсивная проверка

Recursive Assessment МОЖЕТ существовать, но recursive closure не является Core requirement.

Meta-review depth определяется Profile/risk requirements.

ядро не требует elimination of all uncertainty.

High-risk stopping principle: выполнить предусмотренные Profile requirements для review, независимость, uncertainty handling, validation/воспроизводимости, а не бесконечно продолжать review.

────────

8. Агрегирование, Сравнение & Синтез

8.1. Сравнение ≠ Агрегирование

Сравнение отвечает: насколько Assessments отличаются и сопоставимы?

Агрегирование: можно ли получить новый Result из нескольких Inputs?

8.2. Синтез

Синтез — более широкая process/function category, а не обязательная Core Entity.

```text
evaluative synthesis → Assessment
inferential synthesis → Inference / Argument
action-selecting synthesis → Decision
```

Один process МОЖЕТ produce multiple Records.

8.3. Агрегированное оценивание

Агрегированное оценивание — обычный Assessment, использующий prior Assessments и/или другие objects как Inputs.

Universal Entity AggregateAssessment не требуется.

Aggregate status не даёт automatic epistemic superiority.

8.4. Агрегирование optional

Несколько Assessments МОЖЕТ сосуществовать без единого aggregate Result.

множественность является допустимым состоянием знания.

8.5. Majority / последний / authority

Core не использует правила majority wins, последний wins, authority wins, project wins как universal epistemic semantics.

Voting МОЖЕТ быть Profile-определёнными aggregation method, но vote count не имеет universal truth meaning.

8.6. Сопоставимость

Сопоставимость является operation-relative.

```text
comparable for ranking
≠ comparable for arithmetic mean
≠ comparable for statistical pooling
```

Same Aspect или same метка не гарантирует comparability.

8.7. Межаспектный синтез

Different Aspects МОЖЕТ участвовать в новом Assessment при explicit evaluative model.

Они ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently collapse в один score.

Если synthesis выбирает действие, это МОЖЕТ переходить в Decision.

8.8. Необоснованная скаляризация

Скаляризация сама по себе допустима.

Необоснованная скаляризация — превращение multidimensional, порядковым или otherwise non-scalar Results в scalar без определёнными semantically valid отображение.

8.9. Зависимость overlap

Агрегирование должна учитывать существенно relevant dependency overlap, не только exact Input identity.

Repeated use of same Input не запрещено само по себе.

Запрещено представлять repeated/dependent contribution как independent support без определёнными justification.

8.10. Уверенность amplification

Совпадающие/high-confidence Assessments ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО автоматически повышать aggregate confidence только из-за количества.

8.11. Конфликт

Перед substantive conflict СЛЕДУЕТ сравниваться семантическую оболочкуs.

Different Basis МОЖЕТ всё равно давать substantive disagreement, если evaluative question sufficiently aligned.

Disagreement МОЖЕТ быть компонент-level.

Конфликт не требует forced resolution.

8.12. Согласие ≠ истина

```text
90% agreement
≠ 90% probability true
```

Consensus/Agreement score ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently превращаться в truth probability или confidence.

8.13. Inconclusive

неопределённый результат МОЖЕТ быть legitimate Profile-определёнными Result.

```text
no aggregate Assessment
≠ aggregate Result = inconclusive
```

────────

9. Соответствие, Целостность & Failure Modes

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

9.2. Core Соответствие

Assessment Core-conformant, если он представляет допустимый Assessment Record с разрешимыми Target, разрешимыми primary Aspect/construct, определёнными Result если completed, и sufficient structural, referential, semantic и conтекстовым-historical resolution всех существенно necessary элементов.

9.2.1. Structural Соответствие

Structural Соответствие относится к required structure, cardinality, допустимым формам и жизненный цикл completeness Assessment Record.

9.2.2. Referential Соответствие

Referential Соответствие относится к корректной разрешимости существенно required references, включая Target, Inputs, States, Profile, шкала, метод и иные referenced objects.

9.2.3. Semantic Соответствие

Semantic Соответствие относится к достаточной определённости и интерпретируемости Aspect, Result, шкала, roles и иных существенно relevant semantics.

9.2.4. Conтекстовым-Historical Соответствие

Conтекстовым-Historical Соответствие относится к сохранению существенно necessary Context, Scope, исторические состояния, versions и applicability boundaries, необходимых для честной интерпретации historical Result.

Эти виды Соответствие МОЖЕТ пересекаться; одна проблема МОЖЕТ затрагивать несколько слоёв одновременно.

9.3. Соответствие ≠ correctness

```text
Core Conformance
≠ Truth
≠ Epistemic Quality
≠ Project Endorsement
```

Core-conformant Assessment МОЖЕТ быть methodologically poor.

Epistemically plausible Assessment МОЖЕТ быть non-conformant как Record.

9.4. Целостность / Provenance Failure

Целостность Failure — несоответствие зарегистрированной identity, provenance, Inputs, authorship, history или derivation тому, что фактически произошло или должно быть разрешимыми.

Целостность Failure не требует доказательства malicious intent.

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

Assessment МОЖЕТ быть Core-conformant и при этом иметь selection bias, inappropriate метод, invalid inference, bad assumptions, unsupported generalization или poor statistics.

Это отдельный слой.

9.7. Ошибка управления/эксплуатации

Относится к publication, фильтрация, preference, UI representation, export/import claims, deletion, endorsement, operational use.

Canonical Record МОЖЕТ быть conformant при misleading UI.

9.8. Таксономия анти-паттернов

Таксономия анти-паттернов — диагностическая классификация, не Core онтологию.

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

Explicit определёнными отображение/inference/Profile rule МОЖЕТ legitimately transform semantics.

9.10. Подмена жизненного цикла

Новый акт оценивания ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО маскироваться как simple correction.

К этому относятся Silent Переоценивание, Fake Исправление, Revision Laundering.

9.11. Смещение состояния/версии

Historical Assessment ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently reinterpret через существенно different Target State, состояние входа, шкала version, Profile version, Context definition или метод version.

9.12. Representation fidelity

Canonical Assessment conformance и representation fidelity различаются.

Lossy representations МОЖЕТ быть допустимы.

Failure возникает, если representation заявляет полная точность представления, но существенно necessary semantics потеряна; применимый Profile требует более высокой fidelity; либо presentation создаёт существенно misleading interpretation.

9.13. Selection/фильтрация

Показ одного Assessment из многих не является failure сам по себе.

Failure возникает, если representation ложно утверждает отсутствие alternatives/consensus или нарушает declared Profile/governance semantics.

9.14. Import

Unknown imported semantics ДОЛЖНО remain unknown.

Lossy/partial import МОЖЕТ существовать, но ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО заполнять отсутствующую semantics догадкой и заявлять full Assessment equivalence.

9.15. Downstream impact

Upstream correction/withdrawal ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently mutate historical последующие зависимые Results.

Affected последующие зависимые dependency МОЖЕТ потребовать review/reassessment.

```text
affected
≠ automatically invalid
```

Known существенно relevant последующие зависимые dependencies СЛЕДУЕТ remain discoverable; Profile МОЖЕТ повышать это до MUST.

────────

10. Core Выводы стресс-тестирования

Эта глава фиксирует результаты системного stress testing и не вводит новых Core Entities.

10.1. Minimal expert Assessment — PASS

Простой качественным Assessment без числовым score и без явные входы МОЖЕТ быть Core-conformant.

10.2. Machine conformance Assessment — PASS

Machine Assessment использует тот же Core и не получает epistemic privilege.

10.3. Mutable Target/Input — PASS

Historical States остаются разрешимыми и не следуют current State автоматически.

10.4. Relational/цель уровня множестваs — PASS

Допустимы при определёнными Target semantics.

10.5. Динамическая цель/Input selection — PASS

Historical membership должен быть closed/reconstructable, если существенно important.

10.6. Probabilistic/качественным/структурированным Results — PASS

Core не зависит от одной mathematical онтологию.

10.7. Непрерывное оценивание — PASS

Допустим при Profile-определёнными жизненный цикл и сохранении исторические состояния.

10.8. Meta-Assessment — PASS

Отдельная Entity не требуется.

10.9. Конфликтing Assessments — PASS

множественность без forced consensus является legitimate knowledge state.

10.10. Агрегирование — PASS

Агрегированное оценивание является ordinary Assessment; aggregation optional.

10.11. Offline preservation — PASS

Assessment Core не зависит от URL, HTTP, JSON, GitHub или иной текущей технологии.

10.12. Multilingual representation — PASS

Label language не определяет семантическая идентичность.

10.13. Physical/non-digital Targets — PASS

Target не обязан быть цифровым object.

10.14. Historical unknown semantics

Если сохранена запись Target: S / Value: 4, но Aspect/шкала неизвестны, система ДОЛЖНО сохранять unknown semantics вместо догадки.

10.15. Full fidelity

Full fidelity означает семантическая восстановимость, а не byte-for-byte identity.

Разные carrier representations МОЖЕТ представлять один Assessment.

10.16. Project self-authority test — PASS

Assessment, созданный или предпочтительный проектом, не становится Truth автоматически.

10.17. Расширяемость профилей — PASS

Future Profiles МОЖЕТ добавлять новые Aspects, методs, шкалаs, review requirements и confidence models без переписывания Core.

────────

11. Канонические Core invariants

Ниже только фундаментальные инварианты Assessment Core. Остальные правила документа являются semantic rules, Profile guidance, preservation principles или diagnostic safeguards.

1. Assessment является специализированным Record.
2. Каждый Assessment ДОЛЖНО иметь exactly one определёнными структура цели.
3. Каждый Assessment ДОЛЖНО иметь exactly one primary аспект оценивания / оценочный конструкт.
4. Каждый завершённое оценивание ДОЛЖНО иметь exactly one определёнными результат оценивания.
5. цель оценивания structure ДОЛЖНО иметь определёнными evaluative semantics и ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО быть произвольный контейнер.
6. результат оценивания ДОЛЖНО быть интерпретируем относительно Aspect и существенно required semantics.
7. Result ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently escape существенно relevant Target/State/Aspect/Scope/Context/Basis semantics.
8. Assessment ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently change historical Target/Input/Profile/шкала/Context/метод semantics.
9. Assessment ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО использовать собственный Result как independent evidential justification того же Result; определёнными computational recursion не считается independent support.
10. результат оценивания ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО автоматически становиться Truth, Decision, Consensus или Project Endorsement.
11. Profile ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО отменять Core invariants, одновременно заявляя Core compatibility.
12. Unknown semantics ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО заменяться invented semantics.
13. Historical evaluative meaning ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО silently be rewritten by later State, correction, migration or reassessment.
14. идентичность оценивания ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО выводиться только из semantic tuple вроде Target + Aspect + Result.
15. New акт оценивания ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО маскироваться как technical correction.
16. Dependent/repeated Inputs/Assessments ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО маскироваться как independent support.
17. Same метка, number, Result или reviewer identity ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО автоматически означать same semantics, same Assessment или независимость.
18. Core Соответствие ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО интерпретироваться как correctness, quality или endorsement.
19. Assessment architecture ДОЛЖНО оставаться предметно-нейтральной и технологически нейтральной.
20. Assessment Core ДОЛЖНО позволять uncertainty, plurality, disagreement и incomplete knowledge без принудительного выдумывания единого ответа.

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

Profiles МОЖЕТ требовать явные входы, вводить domain vocabularies, определять шкалаs, требовать Target/Input snapshots, задавать confidence/uncertainty representation, устанавливать review depth, требовать independent Проверка, определять aggregation methods, continuous жизненный цикл и усиливать preservation requirements.

Profiles ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО ослаблять Core invariants при заявленной Core compatibility.

Соответствие claim ДОЛЖНО быть scoped к конкретному Profile/version.

────────

14. Принципы сохранения

1. Material historical semantics СЛЕДУЕТ оставаться recoverable.
2. Resolvability не требует текущего online access.
3. Full fidelity означает семантическая восстановимость.
4. миграция носителя не создаёт Переоценивание.
5. Historical Assessment МОЖЕТ пережить утрату non-material metadata.
6. Потеря существенно required semantics МОЖЕТ сделать Result unresolved.
7. Later recovery of lost semantics МОЖЕТ быть correction/enrichment без нового акт оценивания.
8. Offline/printed representation СЛЕДУЕТ быть возможна без изменения Core meaning.
9. Technology-specific storage details ДОЛЖНО БЫТЬ ЗАПРЕЩЕНО определять Assessment identity.
10. Preservation Profile МОЖЕТ усиливать эти требования для долгосрочного архива.

────────

15. Final Core модель

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

> **Чем сложнее конкретный Assessment, тем больше Context, Inputs, Basis, provenance и history может быть существенно необходимо. Но сложность конкретной оценки не должна становиться обязательной сложностью каждого Assessment.**

Принцип эпистемической честности:

> **Если система не может честно определить Target, оценочный конструкт, Result или существенно necessary semantics, она должна сохранить неопределённость или неполноту, а не изобретать недостающий смысл.**

────────

Статус

После интеграционного аудита с актуальными 001–004, локальных аудитов глав 1–10, сквозной атаки глав 1–9, аудита главы 10 и контрольного destructive audit архитектура Assessment зафиксирована как канонический стандарт v0.2 005-ASSESSMENT.md.
