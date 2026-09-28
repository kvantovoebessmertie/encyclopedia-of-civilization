005-ASSESSMENT.md

Статус: канонический стандарт v0.2
Проект: Энциклопедия цивилизации
Назначение: определить универсальную модель Assessment (оценивания) для Claims, Sources, Evidence Uses, Methods, Assessments, физических объектов, отношений, множеств и иных определённых Targets.

────────

0. Назначение стандарта

Assessment — специализированный Record, представляющий результат оценивания определённого Target относительно определённого оценочного конструкта.

Стандарт не определяет, что является истиной, не создаёт универсальной оценки истинности и не придаёт особого эпистемического статуса экспертам, государствам, институтам, проекту или автоматическим системам.

Он определяет, как Assessment должен быть представлен так, чтобы его смысл, границы применимости, происхождение и история могли быть честно восстановлены.

Каноническое ядро:

```text
ASSESSMENT

является специализированным Record

требует:
  ровно 1 определённую структуру Target
  ровно 1 основной Evaluation Aspect / оценочный конструкт

при завершении:
  ровно 1 определённый Assessment Result

может включать:
  0..N явно указанных Assessment Inputs

должен дополнительно сохранять или позволять разрешить:
  любой Context
  Scope
  Basis
  States
  версии
  происхождение
  цепочку происхождения результата

которые существенно необходимы
для корректной идентификации,
интерпретации,
сопоставимости,
воспроизводимости
или применимости Result.
```

────────

1. Assessment Core

1.1. Assessment

Assessment — специализированный Record, представляющий один определённый акт оценивания или, если это заранее определено Profile, одну непрерывную оценочную сущность с сохраняемыми историческими States.

Assessment не является Target и не является его внутренним свойством.

```text
Assessment ≠ Target
```

Assessment также автоматически не является:

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

Завершённый Assessment ДОЛЖЕН иметь:

1. одну определённую структуру Target;
2. один основной Evaluation Aspect / оценочный конструкт;
3. один определённый Assessment Result.

Дополнительные элементы являются условно обязательными и включаются только тогда, когда без них существенно нарушается смысл Assessment.

1.3. Defined

Defined означает: имеющий достаточно определённую семантику для однозначной интерпретации в пределах применимого Standard/Profile.

Определённое понятие не обязано существовать как отдельный Record.

1.4. Resolvable

Resolvable означает: объект, State, отношение или семантика могут быть однозначно установлены из сохранённой структуры, истории, происхождения или ссылок без изобретения отсутствующего смысла.

```text
разрешимость ≠ наличие текущего доступа онлайн
```

1.5. Существенная значимость / обязательность

Элемент является существенно значимым, если его отсутствие, изменение или неверное представление способно существенно изменить:

• идентичность;
• интерпретацию;
• сопоставимость;
• воспроизводимость;
• применимость;
• или оценку Result.

1.6. Draft и completed Assessment

Assessment Record в состоянии Draft/in-progress МОЖЕТ временно быть неполным согласно общему жизненному циклу Record.

Завершённый Assessment ДОЛЖЕН иметь определённый Result.

Отсутствие Result в черновике не делает сам Record невозможным; отсутствие Result в записи, заявленной как завершённый Assessment, является нарушением базового соответствия стандарту.

────────

2. Assessment Target

2.1. Структура Target

Каждый Assessment ДОЛЖЕН иметь ровно одну определённую структуру Target.

Это не означает наличие ровно одного Target Record.

Структура Target МОЖЕТ представлять:

• отдельный Target;
• адресуемый подцелевой объект;
• реляционный Target;
• Target на уровне множества.

2.2. Реляционный Target

Если оцениваемое свойство существует между несколькими участниками, Target МОЖЕТ быть реляционным:

```text
Target:
(EU-A, EU-B)

Aspect:
independence
```

Роли и порядок ДОЛЖНЫ быть разрешимы, если отношение асимметрично или порядок существенно влияет на смысл.

2.3. Target на уровне множества

Assessment МОЖЕТ оценивать множество как единый Target:

```text
Target:
[EU-1, EU-2, EU-3]

Aspect:
methodological diversity
```

Assessment на уровне множества НЕ ДОЛЖЕН использоваться для скрытого объединения независимых актов оценивания отдельных членов.

Определённый Profile коллективный предикат МОЖЕТ иметь следствия для членов множества, но:

```text
Assessment(set)
≠ автоматически совокупность Assessment(member)
```

2.4. Разнородные Targets

Структура Target НЕ ДОЛЖНА превращаться в произвольный контейнер семантически несвязанных объектов.

Если несколько участников входят в Target, их роли и общий оценочный смысл ДОЛЖНЫ быть определены.

2.5. Подцелевой объект

Если Result утверждается о самостоятельно адресуемом компоненте как об отдельном объекте оценивания, этот компонент СЛЕДУЕТ представлять как sub-target.

Если компонент лишь ограничивает область рассмотрения свойства более широкого Target, МОЖЕТ использоваться Evaluation Scope.

2.6. Состояние Target

Если Target изменяем и его State существенно влияет на Assessment, соответствующий Target State ДОЛЖЕН оставаться разрешимым.

```text
Assessment(Target@v1)
≠ автоматически
Assessment(Target@v2)
```

Новое состояние Target НЕ ДОЛЖНО молча менять исторический Assessment.

2.7. Динамический Target

Target МОЖЕТ определяться посредством запроса, фильтра или процесса отбора.

Завершённый Assessment ДОЛЖЕН сохранять семантически замкнутый исторический Target через разрешённый состав либо достаточный неизменяемый контекст его восстановления.

Одна временная отметка сама по себе не гарантирует воспроизводимость исторического Target.

────────

3. Evaluation Aspect, Basis & Result

3.1. Evaluation Aspect

Evaluation Aspect определяет, какое свойство или оценочный конструкт оценивается.

Каждый Assessment ДОЛЖЕН иметь один основной Evaluation Aspect / оценочный конструкт.

Семантика Aspect ДОЛЖНА быть разрешима.

Перечни вроде надёжности, риска, качества, устойчивости, применимости и воспроизводимости являются примерами, а не закрытым словарём Core.

3.2. Идентичность Aspect и его обозначение

Обозначение не определяет семантическую идентичность.

```text
"надёжность"
"reliability"
"fiabilité"
```

МОГУТ представлять одну и ту же семантическую идентичность понятия.

3.3. Составной Aspect

Aspect СЛЕДУЕТ выражать оцениваемое свойство.

Target, Context и Scope СЛЕДУЕТ представлять собственными механизмами, если соответствующие семантические различия содержательно разделимы.

Profiles СЛЕДУЕТ определять каноническое представление для повторяющихся предметных шаблонов.

3.4. Evaluation Basis

Evaluation Basis — определённая оценочная логика, метод, система критериев, правило, модель, шкала или иная структура, по которой Target/Inputs интерпретируются в Result.

Basis МОЖЕТ быть составным.

Core не требует ровно одного Method.

Basis МОЖЕТ включать Criterion, Metric, Threshold, Rule, Scale, Weight, Aggregation Method, Methodology, Benchmark, Model, Formula или экспертную процедуру.

Эти элементы не являются универсально обязательными сущностями Core.

3.5. Basis ≠ Inputs ≠ provenance

```text
Evaluation Basis
≠ происхождение Assessment Input
≠ происхождение выполнения
≠ происхождение Record
```

Семантическое различие не требует отдельных систем хранения.

Одна инфраструктура происхождения МОЖЕТ хранить несколько семантических слоёв.

3.5.1. Criterion ≠ Input

Criterion определяет, как или по какому условию производится оценивание.

Input определяет, какой материал фактически используется при оценивании.

```text
Criterion ≠ Input, удовлетворяющий Criterion
```

Criterion и фактический материал, использованный для проверки Criterion, ДОЛЖНЫ оставаться семантически различимыми.

3.6. Assessment Result

Завершённый Assessment ДОЛЖЕН иметь ровно один определённый Assessment Result.

Result МОЖЕТ быть качественным, категориальным, порядковым, числовым, вероятностным, интервальным/распределительным, сравнительным, ранжированным, текстовым или структурированным.

Тип данных не определяет онтологию.

3.7. Структурированный Result

Структурированный Result допустим, если его компоненты образуют один определённый Profile согласованный оценочный конструкт.

Структурированный Result НЕ ДОЛЖЕН становиться произвольным контейнером.

Если компонент требует самостоятельной адресуемости, происхождения, конкурирующего оценивания или жизненного цикла, его СЛЕДУЕТ выделить в отдельный Assessment или иной явно представленный Record.

3.8. Семантика Result

Result ДОЛЖЕН быть интерпретируемым относительно Aspect и существенно необходимых Basis/Scale.

Result = 3 недостаточно определён, если неизвестно, что означает 3.

3.9. Порядок Result ≠ желательность

Упорядоченная шкала не означает автоматически положительную или отрицательную направленность.

Высокая надёжность, высокий риск и высокая неопределённость имеют разную семантику желательности.

Core не предполагает универсальной монотонности.

3.10. Measurement и Assessment

Measurement и Assessment различаются семантикой, а не типом данных.

error rate = 4.2% может быть Measurement.

Если Profile определяет эту величину как оценочный Result, она МОЖЕТ быть Result Assessment.

Количественное выражение не даёт автоматического эпистемического превосходства.

────────

4. Assessment Inputs, Evidence & Provenance

4.1. Assessment Input

Assessment Input — разрешимый информационный или фактический объект, содержание или State которого существенно используется при получении Result.

Assessment МОЖЕТ иметь 0..N явно указанных Inputs.

Явно указанные Inputs не являются универсальным требованием Core.

4.2. Допустимые Inputs

Assessment Input МОЖЕТ быть Evidence Use, Source, Claim, Measurement, Dataset, результатом Method, другим Assessment, производным значением или иным определённым объектом.

4.3. Evidence Use и Assessment Input

Если материал используется как атомарное свидетельство относительно Claim, СЛЕДУЕТ использовать Evidence Use.

Если материал является техническим или оценочным входом процесса Assessment, он МОЖЕТ быть прямым Assessment Input.

```text
Evidence Use
≠ Assessment Input
```

Evidence Use МОЖЕТ быть Assessment Input.

4.3.1. Citation/reference ≠ Input membership

Наличие Source, Claim или иного Record в цитате, обосновании, обсуждении или ссылке НЕ ДОЛЖНО автоматически означать принадлежность к Assessment Input.

Фактическая роль объекта — Input, Target, ссылка на Basis, цитата, ссылка на происхождение или иная роль — ДОЛЖНА оставаться разрешимой, когда различие существенно важно.

```text
citation/reference
≠ автоматически Assessment Input
```

4.4. Target как неявный Input

Если Assessment непосредственно использует свойства Target, которые уже разрешимы через ссылку на Target, отдельная дублирующая ссылка Input не обязательна.

4.5. Исторические Inputs

Завершённый Assessment ДОЛЖЕН сохранять фактически использованную историческую основу входных данных, если она существенно значима.

Новый Input НЕ ДОЛЖЕН молча добавляться к старому завершённому Assessment.

Динамический отбор Input ДОЛЖЕН сохранять состав или достаточный неизменяемый контекст его восстановления, если состав существенно влияет на Result.

4.6. Состояние Input

Существенно значимое состояние Input ДОЛЖНО оставаться разрешимым.

Для Assessment Input, который является Source, состояние Input ДОЛЖНО быть семантически отличимо от версии записи Source. Если исторически значимое состояние самого Source существенно влияет на Result, именно это состояние Source ДОЛЖНО оставаться разрешимым.

Для Assessment Input, который является Evidence Use, исторически значимый Source Context, включая Source State и иные уровни Source, ДОЛЖЕН оставаться разрешимым настолько, насколько они существенно необходимы для интерпретации фактически использованного свидетельства. Assessment НЕ ДОЛЖЕН заменять такую историческую определённость текущей версией записи Source или текущим состоянием Source.

```text
Input@v3
≠ Input@current автоматически

версия записи Source
≠ состояние Source автоматически
```

4.7. Отсутствующие значения

Необходимо различать missing, unknown, not measured, not applicable, zero, not detected, excluded.

Эти состояния НЕ ДОЛЖНЫ молча сливаться, если различие существенно важно.

4.8. Происхождение отбора

Критерий отбора МОЖЕТ быть частью Basis.

Выполнение отбора относится к процессу и его происхождению.

Выбранные объекты являются Inputs.

Эти роли ДОЛЖНЫ оставаться различимыми.

4.9. Цепочка происхождения Result

СЛЕДУЕТ различать:

```text
Record provenance
Evaluation execution provenance
Input selection provenance
Result derivation lineage
```

Но Core не требует отдельного механизма хранения для каждого слоя.

4.10. Преобразования

Существенно значимые фильтрация, нормализация, импутация, взвешивание или иное преобразование между Inputs и Result ДОЛЖНЫ оставаться разрешимыми.

4.11. Зависимость

Различные Assessment ID или разные идентичности рецензентов сами по себе не устанавливают независимость.

```text
неизвестная зависимость
≠ независимость
```

Зависимость МОЖЕТ быть частичной, попарной, относительной к методологии, относительной к источнику или неизвестной.

Core не требует универсального двоичного значения independent=true/false.

4.12. Самообоснование

Assessment НЕ ДОЛЖЕН использовать собственный Result как независимое свидетельское обоснование того же Result.

Определённое рекурсивное вычисление или вычисление с фиксированной точкой МОЖЕТ существовать, если рекурсия является частью явно заданной Evaluation Basis и не представляется как независимое подтверждение.

Косвенные циклы зависимости ДОЛЖНЫ оставаться обнаруживаемыми, когда это существенно важно.

────────

5. Identity, Lifecycle & Reassessment

5.1. Assessment Identity

Assessment имеет постоянную идентичность Record, унаследованную от общей инфраструктуры Record.

Идентичность НЕ ДОЛЖНА вычисляться из Target + Aspect + Result или других семантических кортежей.

Одинаковый Result ≠ один и тот же Assessment.

5.2. Дискретный Assessment

Дискретный Assessment обычно представляет один исторический акт оценивания.

5.3. Correction

Correction исправляет представление того же акта оценивания.

Если действие действительно является Correction, идентичность Assessment ДОЛЖНА сохраняться.

Примеры: ошибка транскрипции, ошибочная ссылка, обогащение метаданных, уточнение без нового оценочного рассуждения.

Если исправление меняет акт оценивания настолько, что возникает новый акт оценивания, оно ДОЛЖНО рассматриваться как Reassessment или иной новый Assessment, а не как Correction.

5.4. Reassessment

Reassessment — новый акт оценивания.

Reassessment ДОЛЖЕН иметь новую идентичность Assessment.

Исключение не допускается за счёт переименования Reassessment в обновление State. Если заранее определённый Profile поддерживает Continuous Assessment с одной постоянной идентичностью, последующее вычисление или обновление, являющееся частью этой непрерывной идентичности, не является Reassessment в смысле настоящего раздела.

Один и тот же оценщик МОЖЕТ создать новый Assessment.

5.5. Review ≠ Reassessment

Review имеет Target = prior Assessment и оценивает сам Assessment.

Reassessment имеет Target = original/related Target и оценивает Target заново.

Один процесс МОЖЕТ породить обе записи.

5.6. Continuous Assessment

Profile МОЖЕТ определить постоянно поддерживаемую идентичность Assessment.

В этом случае повторные вычисления МОГУТ быть историческими состояниями одной идентичности Assessment.

Непрерывная цепочка происхождения ДОЛЖНА быть определена до или независимо от конкретного изменения Result и НЕ ДОЛЖНА объявляться задним числом только для избежания новой идентичности.

Исторические состояния непрерывного Assessment ДОЛЖНЫ сохранять существенно значимые Target State, состав/состояния Input, версию Basis/Method, Context и Result.

5.7. Цепочка идентичности ≠ цепочка переоцениваний

Связанные Reassessments МОГУТ образовывать историческую цепочку, но это не означает одну идентичность Assessment.

```text
цепочка связанных переоцениваний
≠ одна идентичность Assessment
```

5.8. Замещение

Assessment МОЖЕТ быть замещён другим Assessment.

```text
замещён
≠ удалён
≠ ложен
```

Замещение СЛЕДУЕТ связывать с разрешимой областью и контекстом, если оно не является универсальным.

Core НЕ ДОЛЖЕН предполагать наличие одного глобально текущего Assessment.

5.8.1. Ветвящееся замещение

Замещение МОЖЕТ быть ветвящимся и относительным к Profile/Context.

```text
Assessment A
├── Assessment B предпочтителен при Profile P1
└── Assessment C предпочтителен при Profile P2
```

Core НЕ ДОЛЖЕН предполагать одну глобальную линейную цепочку «старый → новый → единственно действительный».

5.8.2. Отзыв

Assessment МОЖЕТ быть отозван.

```text
отозван
≠ удалён
≠ ложен
```

Отзыв означает изменение состояния жизненного цикла или операционного статуса, а не автоматически утверждение о ложности Result.

Существенно важная причина отзыва СЛЕДУЕТ сохраняться прослеживаемой, если это допускается применимыми ограничениями законодательства, конфиденциальности или безопасности.

Исторический Assessment СЛЕДУЕТ сохранять, если это разрешено. Если внешнее обязательное ограничение требует физического удаления, такое удаление НЕ ДОЛЖНО маскироваться под обычное исправление или переоценивание.

5.9. Последний / предпочтительный / применимый / активный

```text
последний
≠ предпочтительный
≠ применимый
≠ активный
≠ истинный
```

current не является Core-понятием без определённой семантики Profile.

5.10. Миграция

Миграция носителя, сериализация или транспорт импорта не являются Reassessment.

Carrier ≠ Assessment Identity.

────────

6. Контекст, применимость и область оценивания

6.1. Assessment Context

Assessment Context — внешние условия, назначение и ограничения применения, относительно которых должен интерпретироваться Result.

Context является условно обязательным.

Если без него Result существенно меняет смысл или может быть неправильно применён, Context ДОЛЖЕН быть разрешимым.

6.2. Context ≠ Target

Target отвечает: что оценивается?

Context отвечает: при каких внешних условиях и для какого применения?

Если второй участник является частью самого оцениваемого отношения, СЛЕДУЕТ использовать реляционный Target.

6.3. Evaluation Scope

Evaluation Scope — внутренняя граница фактически выполненной задачи оценивания.

Scope является условно обязательным, если Target + Aspect недостаточно точно задают границу оценивания.

6.4. Context ≠ Scope

```text
Context
→ внешние условия применения

Scope
→ внутренняя область того, что фактически оценивалось
```

6.5. Применимость

Applicability не является универсальным внутренним логическим значением Assessment.

Result интерпретируется внутри собственного исходного Semantic Envelope без требования отдельного универсального Assessment применимости.

Отдельный вопрос применимости возникает прежде всего при повторном использовании или переносе существующего Result за пределы исходного Semantic Envelope — например, на другой Target, State, Context или вариант применения.

Она МОЖЕТ быть определённым Profile правилом отображения, отдельным Assessment или явно определённым выводом.

6.6. Перенос между контекстами

Result НЕ ДОЛЖЕН автоматически переноситься между существенно различающимися Claims, совокупностями, предметными областями, Contexts, состояниями Target или версиями.

Повторное использование между контекстами МОЖЕТ происходить только при разрешимой семантической эквивалентности, наличии правила переноса, отображения или отдельного шага рассуждения.

Сопоставимость и переносимость МОГУТ зависеть от Aspect.

6.7. Наследование Context

Context МОЖЕТ наследоваться из Profile.

Существенно значимый унаследованный Context ДОЛЖЕН разрешаться к историческому состоянию Profile/Context, фактически применявшемуся к Assessment.

6.8. Динамический Context

Динамические обозначения вроде «действующее законодательство», «действующий стандарт», «текущий уровень риска» НЕ ДОЛЖНЫ молча менять семантику исторического Assessment.

6.9. Временные роли

СЛЕДУЕТ различать время создания Assessment, время состояния Target и период применимости.

6.10. Географические роли

СЛЕДУЕТ различать местоположение оценщика, местоположение Target и географию применимости.

6.11. Semantic Envelope

Semantic Envelope — аналитическое понятие, а не Core-сущность и не обязательное поле.

Концептуально:

```text
Semantic Envelope
=
Target
+
существенно значимое состояние Target
+
основной Evaluation Aspect / construct
+
Evaluation Scope, если существенно
+
Assessment Context, если существенно
+
те семантические элементы Basis, которые существенно ограничивают
интерпретацию, сопоставимость или применимость
```

Assessment Inputs автоматически не входят в Semantic Envelope, поскольку относятся прежде всего к выводу Result.

```text
Semantic Envelope
≠ Basis вывода Result
```

6.12. Выход за Semantic Envelope

Result НЕ ДОЛЖЕН молча переноситься за пределы собственного Semantic Envelope без определённого отображения, вывода, Assessment или правила Profile.

────────

7. Качество Assessment, неопределённость и уверенность

7.1. Assessment для Assessment

Assessment МОЖЕТ быть Target другого Assessment.

Новая сущность MetaAssessment не требуется.

7.2. Отсутствие привилегии мета-уровня

```text
meta-level
≠ эпистемическая привилегия
```

Assessment для Assessment МОЖЕТ быть ошибочным и сам МОЖЕТ быть пересмотрен.

7.3. Качество ≠ корректность

```text
качество Assessment
≠ корректность Result
```

Хорошая методология не гарантирует истинный или корректный Result.

Корректный Result не доказывает хорошую методологию.

7.4. Метааспекты

Аспекты, связанные с качеством, МОГУТ включать методологическую адекватность, устойчивость, воспроизводимость, прозрачность, прослеживаемость, риск смещения, калибровку, применимость и уверенность.

Этот список является иллюстративным, а не словарём Core.

7.5. Слои неопределённости

СЛЕДУЕТ различать неопределённость Target, неопределённость Input, неопределённость Result, уверенность в Result, уверенность модели и неопределённость применимости.

Неопределённость и уверенность ДОЛЖНЫ иметь разрешимый референт.

7.6. Вероятность ≠ уверенность

```text
P(Claim true)
≠ уверенность в оценке
≠ уверенность модели
```

Одинаковый числовой диапазон не означает одинаковой семантики.

7.7. Уверенность ≠ обратная неопределённость

Core НЕ ДОЛЖЕН предполагать, что уверенность = 1 - неопределённость.

Высокая неопределённость Target МОЖЕТ сосуществовать с высокой уверенностью в том, что неопределённость действительно высока.

7.8. Представление уверенности и неопределённости

Profile МОЖЕТ представлять уверенность/неопределённость как структурированный компонент Result, отдельный Evaluation Aspect или мета-Assessment.

Core не требует избыточного представления.

7.9. Распространение

Качество, уверенность, неопределённость и иные свойства Assessment НЕ ДОЛЖНЫ автоматически складываться или распространяться через Inputs, Methods, Targets или мета-уровни без определённого оценочного правила.

7.10. Рекурсивный обзор

Рекурсивное оценивание МОЖЕТ существовать, но рекурсивное замыкание не является требованием Core.

Глубина мета-обзора определяется требованиями Profile и уровнем риска.

Core не требует устранения всей неопределённости.

Принцип остановки для высокого риска: выполнять предусмотренные Profile требования к обзору, независимости, обработке неопределённости, валидации и воспроизводимости, а не продолжать обзор бесконечно.

────────

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

После интеграционного аудита с актуальными 001–004, локальных аудитов глав 1–10, сквозной атаки глав 1–9, аудита главы 10 и контрольного destructive audit архитектура Assessment зафиксирована как канонический стандарт v0.2 005-ASSESSMENT.md.
