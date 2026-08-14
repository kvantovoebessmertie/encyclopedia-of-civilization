# 010 — RESULT
## Стандарт представления результатов

**Проект:** Энциклопедия цивилизации  
**Статус:** рабочий стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются Results — phenomena или content, занимающие downstream/result role относительно определённого reference frame.

Таким reference frame MAY быть:

- Action;
- Process;
- Decision implementation;
- Intervention;
- Procedure execution;
- experiment;
- treatment;
- operation;
- policy;
- другой materially defined объект, действие, процесс или структурированный набор reference elements.

Цель стандарта — позволить сохранять:

- что рассматривается как Result;
- относительно чего это является Result;
- когда Result существовал, наблюдался, измерялся, вычислялся или реконструировался;
- где и в каком Scope;
- какой Comparison Reference используется;
- был ли Result expected, intended, desired или unexpected;
- был ли он observed, measured, computed, inferred, modeled или reconstructed;
- какие causal relations ему атрибутируются;
- насколько реализован Decision Outcome;
- насколько достигнут Objective;
- насколько Action, Decision implementation, Intervention или Process был effective;
- какие uncertainty, provenance и limitations существуют.

Стандарт не предназначен для автоматического определения:

- причины Result;
- качества Action;
- качества Decision;
- success;
- desirability;
- safety;
- benefit;
- harm;
- Outcome Realization;
- Objective Achievement;
- Effectiveness;
- responsibility.

Сохранить Result означает сохранить максимально честное представление о downstream/result role относительно определённого reference frame, не превращая временную последовательность в причинность, observation — в causal effect, а Result — в success или effectiveness автоматически.

---

# 1. Основное понятие

## 1.1. Result

**Result (Результат)** — relational semantic construct, представляющий определённый phenomenon или content, занимающий downstream/result role относительно определённого reference frame.

Такой content MAY быть представлен через:

- Event;
- State;
- change;
- Measurement-derived condition;
- quantity;
- distribution;
- pattern;
- other suitable semantics.

Result MAY быть materialized как специализированный Record, если independent identity, provenance, reuse, structured semantics или другие materially relevant требования делают это полезным.

Следовательно:

    Result role
    ≠ mandatory Result Entity

Result отвечает на вопрос:

> **Какой phenomenon или content занимает downstream/result role относительно определённого reference frame?**

Ключевой принцип:

    Result is relational

---

# 2. Result role identity ≠ Result Record identity

Необходимо различать:

    Result-role identity
    ≠ materialized Result Record identity automatically

Один underlying phenomenon MAY занимать несколько Result roles относительно разных reference frames без обязательного создания отдельной копии underlying content или occurrence Record для каждой роли.

И наоборот, один materialized Result Record MAY агрегировать structured Result semantics, если это не уничтожает materially relevant distinctions.

Core не требует одного fixed storage pattern.

---

# 3. Result ≠ Event

Event отвечает:

> Что произошло?

Result отвечает:

> Какой phenomenon занимает downstream/result role относительно определённого reference frame?

Например:

    Event:
    temperature decreased

и:

    Result:
    temperature decrease
    relative to cooling Action A

могут относиться к одному underlying phenomenon.

Следовательно:

    Event
    ≠ Result intrinsically

Event MAY существовать без Result role.

Result MAY использовать Event, State, Measurement-derived content или другую suitable semantics.

---

# 4. Result ≠ Claim

Claim отвечает:

> Что утверждается?

Result отвечает:

> Какой downstream/result phenomenon представлен относительно reference frame?

Следовательно:

    Claim about Result
    ≠ Result

Например:

    Source states:
    mortality was 4%

является Claim.

А:

    mortality = 4%
    within 30 days
    relative to Intervention I
    in Population P

MAY занимать Result role.

Наличие Result representation MUST NOT автоматически означать epistemic certainty соответствующего Claim.

---

# 5. Минимальная структура Result

Для завершённой Result semantics необходимо как минимум:

1. defined Result Content;
2. defined reference frame;
3. sufficient Result attribution.

Минимальная формула:

    defined Result Content
    +
    defined reference frame
    +
    sufficient Result attribution

**Result attribution** — semantics, связывающая Result Content с определённым reference frame как downstream/result role.

Result attribution является semantic requirement и не требует отдельного field, Record или Entity.

---

# 6. Result Content

**Result Content** — content, занимающий Result role относительно определённого reference frame.

Result Content MAY быть:

- Event;
- State;
- State change;
- measured condition;
- quantity;
- distribution;
- pattern;
- defined absence/presence of phenomenon;
- structured content;
- computed or inferred quantity;
- другой подходящий semantic construct.

Result Content не требует отдельной ResultContent Core Entity.

---

# 7. Reference frame

**Reference frame** — семантическая рамка, относительно которой Result рассматривается как downstream/result phenomenon.

Reference frame MAY быть:

- одним определённым upstream object/process;
- structured set of reference elements.

Например:

    Result relative to Action A

или:

    Result relative to:
    Action A
    +
    Procedure P
    +
    Context C

Structured reference frame MUST сохранять materially relevant roles своих элементов.

Следовательно:

    Action
    Procedure
    Context

MUST NOT автоматически flatten into one unordered set, если distinction между их ролями materially важна.

Structured reference frame не требует отдельной Core Entity.

Reference frame MUST быть sufficiently defined для materially relevant interpretation.

---

# 8. Downstream semantics

`Downstream` в `010` означает relational/result position относительно reference frame.

Он НЕ означает автоматически:

    later in time

или:

    causally downstream

Следовательно:

    later than X
    ≠ Result of X automatically

И:

    Result relative to X
    ≠ causally downstream from X automatically

Например:

    Action A occurred Monday
    rain occurred Friday

само по себе не делает rain Result of Action A.

Temporal ordering MAY участвовать в Result semantics, но недостаточно само по себе.

---

# 9. Result relation ≠ causal relation

Фундаментальное правило:

    Result relative to X
    ≠ caused by X automatically

Result relation MAY означать:

- post-intervention observation;
- operational association;
- measured output;
- study outcome;
- downstream State;
- defined comparison result;
- другую Profile-defined semantics.

Causal attribution требует отдельного основания.

---

# 10. Natural-language causal strengthening

Natural-language expressions MAY создавать ложное causal implication.

Например:

    "result of X"
    "outcome of X"
    "due to X"

MUST NOT автоматически использоваться как equivalent to:

    X caused R

если causal semantics отдельно не установлена.

Representation SHOULD сохранять distinction между:

    downstream from
    observed after
    relative to

и:

    caused by

когда она materially relevant.

---

# 11. Result ≠ Consequence

Consequence предполагает consequential attribution относительно upstream occurrence.

Result MAY быть Consequence.

Но:

    Result
    ≠ Consequence automatically

Например:

    Result:
    temperature decreased after Action A

не означает автоматически:

    decrease was a Consequence caused by A

---

# 12. Result ≠ Effect

`Effect` является domain-sensitive boundary concept.

В некоторых domains Effect подразумевает causal attribution.

В других он MAY означать:

- measured difference;
- estimated contrast;
- observed response;
- other domain-specific semantics.

Поэтому `010` НЕ вводит universal:

    Effect = Result + causality

Domain semantics MUST remain distinguishable.

`010` не определяет полную Effect ontology.

---

# 13. Result ≠ Decision Outcome

Decision Outcome отвечает:

> Что было решено?

Result отвечает:

> Что произошло или было установлено downstream?

Следовательно:

    Decision Outcome
    ≠ Result

Например:

    Decision Outcome:
    evacuate 100 people

    Result:
    60 people evacuated

Result не переписывает Outcome.

---

# 14. Result ≠ Outcome Realization

**Outcome Realization** отвечает:

> В какой степени defined Outcome фактически реализовался?

Result MAY использоваться как input для Outcome Realization.

Но:

    Result
    ≠ Outcome Realization

Например:

    Decision Outcome:
    evacuate 100 people

    Result:
    60 evacuated

    Outcome Realization:
    partial

---

# 15. Result ≠ Objective Achievement

Objective отвечает:

> Какого состояния предполагалось достичь?

Objective Achievement отвечает:

> Был ли defined Objective достигнут?

Result отвечает:

> Что наблюдалось downstream?

Следовательно:

    Result
    ≠ Objective Achievement

---

# 16. Result ≠ Effectiveness

Effectiveness — causal/evaluative или attribution-sensitive semantics, в которой оценивается вклад Action, Decision implementation, Intervention или Process в достижение defined Result или Objective в соответствии с применимой domain/model semantics.

Следовательно:

    Result observed
    ≠ intervention effective

    Objective achieved
    ≠ intervention caused or materially contributed to achievement automatically

Effectiveness требует большего, чем сам Result.

---

# 17. Result ≠ Success

`010` не вводит universal:

    Result.success

или:

    Action.success

Потому что success MAY означать:

- Result occurred;
- intended Result occurred;
- Outcome realized;
- Objective achieved;
- harmful Result avoided;
- threshold reached;
- Procedure completed;
- other Profile-defined meaning.

Эти semantics MUST оставаться различимыми.

---

# 18. Result ≠ Assessment

Result является descriptive/relational semantics.

Assessment отвечает:

> Как Result оценивается?

Например:

    Result:
    mortality = 4%

    Assessment:
    mortality is unacceptably high

Следовательно:

    Result
    ≠ good/bad automatically

---

# 19. Positive / negative / harmful / beneficial

Terms:

- positive Result;
- negative Result;
- harmful Result;
- beneficial Result;

обычно включают evaluative semantics.

Core SHOULD по возможности сохранять descriptive Result отдельно.

Evaluation MAY быть Assessment.

---

# 20. Expected Result

**Expected Result** — Result semantics, существование или значение которой ожидалось до или независимо от actual observation.

Но:

    expected
    ≠ observed

    predicted
    ≠ actual

Expectation MAY происходить из:

- Model;
- Plan;
- Prediction;
- Procedure;
- Decision;
- prior evidence;
- Assessment.

---

# 21. Intended Result

**Intended Result** — downstream Result, который был intended относительно Action, Decision, Plan или Intervention.

Но:

    intended
    ≠ achieved

И:

    achieved
    ≠ intended automatically

---

# 22. Desired Result

Desired semantics необходимо отличать от expected и intended.

Следовательно:

    desired
    ≠ expected
    ≠ intended automatically

Desired Result MAY быть unlikely.

Expected Result MAY быть undesirable.

---

# 23. Unintended Result

Result MAY быть unintended.

Например:

    Action:
    irrigate field

    Result:
    neighboring soil became waterlogged

Unintendedness не означает автоматически:

- harm;
- failure;
- negligence;
- unforeseeability.

---

# 24. Expected ≠ intended ≠ desired ≠ observed

Когда materially relevant, необходимо сохранять distinction:

    expected
    ≠ intended
    ≠ desired
    ≠ observed

Один Result MAY одновременно занимать несколько таких roles.

---

# 25. Observed Result

Observed Result Content поддерживается Observation/Measurement или иной directly recorded evidence semantics.

Но:

    observed
    ≠ causally explained

    observed
    ≠ complete

    observed
    ≠ perfectly precise

Observation provenance MUST сохраняться when material.

---

# 26. Inferred Result

Result MAY быть inferred.

В таком случае:

    inferred
    ≠ directly observed

Inference provenance MUST сохраняться.

---

# 27. Reconstructed Result

Historical Result MAY быть reconstructed из:

- Sources;
- Claims;
- Events;
- Measurements;
- Actions;
- other evidence.

Reconstruction MUST NOT masquerade as direct Observation.

---

# 28. Computed Result

Result MAY быть computed.

Например:

    mortality rate
    =
    deaths / population

Computed Result SHOULD сохранять when material:

- method/formula;
- input provenance;
- units;
- population;
- time window;
- version.

Computed не означает directly observed.

---

# 29. Modeled Result

Model output MAY occupy Result role if modeled status сохраняется явно.

    modeled Result
    ≠ observed Result

Model provenance, assumptions и version SHOULD быть resolvable when material.

---

# 30. Estimated Result

Estimate MAY иметь uncertainty.

Estimate MUST NOT silently become:

    exact observed Result

---

# 31. Provenance dimensions MAY overlap

Observed, measured, computed, inferred, modeled и reconstructed не образуют обязательно mutually exclusive enum.

Например:

    computed mortality rate

может быть:

- computed;
- based on observed deaths;
- partially reconstructed denominator.

Representation MUST сохранять materially relevant combinations.

---

# 32. Result time

Необходимо различать, когда materially relevant:

- phenomenon occurrence time;
- Result time window;
- observation time;
- measurement time;
- detection time;
- computation time;
- evaluation time;
- report time;
- record time.

Они MUST NOT автоматически отождествляться.

---

# 33. Immediate vs delayed Result

Terms:

- immediate;
- short-term;
- delayed;
- long-term;

MUST иметь defined temporal semantics или Profile context.

Нет universal threshold:

    delayed > 24h

для всех domains.

---

# 34. Result time window

Некоторые Results имеют смысл только внутри defined window.

Например:

    mortality within 30 days

    crop yield over one season

    system uptime over 24 hours

Time window MUST оставаться resolvable when materially relevant.

---

# 35. Measurement time ≠ Result interval

Measurement at T2 MAY summarize Result over:

    T1 → T2

Следовательно:

    measurement time
    ≠ Result phenomenon time automatically

---

# 36. Spatial semantics

Необходимо различать:

- reference Action location;
- observation location;
- measurement location;
- Result phenomenon location;
- affected area;
- other spatial roles.

Core не вводит universal:

    Result.location

без role semantics.

---

# 37. Result Scope

**Result Scope** — scope, приписываемый represented Result phenomenon.

Он MAY включать:

- population;
- territory;
- systems;
- objects;
- devices;
- subgroup;
- other extent dimensions.

Result Scope MAY быть:

- known;
- partial;
- inferred;
- disputed;
- unknown.

Unknown Scope MUST NOT становиться universal.

---

# 38. Observation / Data Scope

**Observation/Data Scope** — scope, для которого фактически доступны Observation, Measurement или data.

Необходимо различать:

    Result Scope
    ≠ Observation/Data Scope automatically

Например:

    100 patients treated
    data available for 80

не позволяет автоматически утверждать known Result Scope для всех 100.

---

# 39. Result Scope ≠ Action Scope

    Action Scope
    ≠ Result Scope

Action MAY охватывать больше или меньше units, чем represented Result phenomenon.

---

# 40. Result Scope ≠ total Effect Scope

Measured или represented Result MAY покрывать только часть downstream effects.

Следовательно:

    Result Scope
    ≠ total affected Scope automatically

---

# 41. Population

Result MAY быть population-specific.

Например:

    adults
    ≠ all people

Population boundaries MUST оставаться resolvable when material.

---

# 42. Sample ≠ Population

Фундаментальное правило:

    sample Result
    ≠ population Result

Generalization требует:

- Inference;
- Model;
- statistical reasoning;
- other valid semantics.

---

# 43. Individual vs Aggregate Result

Result MAY быть:

- individual;
- aggregate;
- subgroup-specific;
- distributional.

Aggregate Result MUST NOT автоматически означать одинаковый individual Result.

Например:

    average improvement
    ≠ every participant improved

---

# 44. Mean ≠ Distribution

Summary statistic не сохраняет автоматически:

- variance;
- spread;
- distribution shape;
- outliers;
- subgroup differences.

Profile MAY требовать более detailed representation.

---

# 45. Multiple Results

One reference frame MAY иметь множество Results.

Например Action A:

- temperature decreased;
- pressure increased;
- energy consumption increased.

Core не требует одного aggregate Result.

---

# 46. One Result relative to multiple upstream references

Один Result MAY быть связан с:

- multiple Actions;
- multiple Processes;
- combined Intervention;
- Decision implementation;
- contextual factors.

Следовательно:

    one Result
    ≠ one upstream cause

---

# 47. Result cardinality

`010` не требует:

    exactly one Result per Action

или:

    exactly one upstream reference per Result

Relations MAY быть many-to-many.

---

# 48. Result identity

Result identity не определяется одним Result Content.

    same Result Content
    ≠ same Result identity automatically

Identity MAY зависеть от:

- underlying phenomenon;
- reference frame;
- time window;
- Scope;
- Comparison Reference;
- provenance;
- granularity;
- Result-role semantics;
- other materially relevant distinctions.

---

# 49. Different reports ≠ different Results

Разные reports, Sources или representations одного Result MUST NOT автоматически создавать distinct Result identities.

И наоборот:

    same value
    ≠ same Result automatically

например, если value относится к разным:

- periods;
- populations;
- frames;
- Scopes.

---

# 50. Same phenomenon, multiple Result roles

Один underlying phenomenon MAY занимать multiple Result roles.

Например Event E:

    tank level increased

MAY быть Result relative to:

- pump Action A;
- Process P;
- Intervention I.

Следовательно:

    distinct Result roles
    ≠ distinct underlying phenomena automatically

Distinct Result-role instances MAY share one materialized underlying content/occurrence representation.

Core MUST NOT требовать duplication underlying content solely because reference-frame semantics differs.

---

# 51. Result granularity

Result MAY быть представлен:

    system stabilized

или:

    pressure = X
    temperature = Y
    flow = Z

Purpose MAY влиять на granularity representation.

Но purpose MUST NOT invent:

- underlying phenomenon;
- Scope;
- Result identity;
- reference frame.

---

# 52. Composite Result

Result MAY иметь structured Content.

Но Composite Result MUST NOT скрывать materially independent Results, если это нарушает:

- provenance;
- time window;
- Scope;
- causal status;
- population;
- comparison semantics;
- safety-critical meaning.

---

# 53. Comparison Reference

**Comparison Reference** — semantic reference, относительно которого определяется comparative Result meaning.

Comparison Reference MAY быть:

- baseline State;
- prior value;
- control group;
- historical average;
- target;
- expected value;
- model output;
- counterfactual comparator;
- other defined comparator.

Comparison Reference не является обязательной Core Entity.

---

# 54. Comparison role distinctions

Один и тот же value/object MAY занимать разные semantic roles.

Например:

    80%

MAY быть:

- Comparison Reference;
- Objective criterion;
- threshold;
- regulatory limit;
- expected value.

Эти roles MUST оставаться distinguishable when materially relevant.

Same value:

    ≠ same semantic role automatically

---

# 55. Baseline

**Baseline** является одним возможным видом/role Comparison Reference.

Baseline условен и НЕ требуется для каждого Result.

Он необходим только когда Result semantics materially зависит от change/comparison.

Например:

    final pressure = 5 bar

MAY быть Result без explicit baseline.

Но:

    pressure decreased by 2 bar

требует Comparison Reference.

---

# 56. Prior State ≠ baseline automatically

Earlier State MAY быть baseline.

Но:

    prior State
    ≠ baseline automatically

Baseline selection должна быть semantically represented или inferable.

---

# 57. Control ≠ baseline automatically

Control group MAY служить Comparison Reference.

Но:

    control
    ≠ baseline necessarily

Они являются distinct comparison roles.

---

# 58. Comparison Reference provenance

Comparison Reference itself MAY быть:

- measured;
- modeled;
- inferred;
- reconstructed;
- disputed.

Its provenance MUST сохраняться when materially relevant.

---

# 59. Baseline selection

Baseline/comparator selection MAY materially влиять на Result interpretation.

Следовательно:

    chosen baseline
    ≠ neutral baseline automatically

Если selection materially важна, она должна быть resolvable.

---

# 60. Change Result

Если Result выражает change:

    X increased by Δ

должны быть resolvable when material:

- variable;
- direction;
- Comparison Reference;
- units;
- time relation.

---

# 61. Absolute Result

Result MAY быть absolute State/value:

    final pressure = 5 bar

relative to defined reference frame.

Explicit change не обязателен.

---

# 62. Relative Result

Result MAY быть expressed relative to:

- baseline;
- control;
- prior period;
- target;
- expected value;
- other comparator.

Comparator MUST быть resolvable when material.

---

# 63. Counterfactual comparator

Counterfactual comparator представляет:

> что предположительно произошло бы без X или при иной condition.

Counterfactual comparator:

    ≠ historical observed Result

Он принадлежит Inference/Model/comparison semantics.

---

# 64. Measurement ≠ Result

Measurement отвечает:

> Что было измерено?

Result отвечает:

> Какое measured/derived phenomenon занимает Result role относительно reference frame?

Следовательно:

    Measurement
    ≠ Result intrinsically

Measurement MAY provide Result Content.

---

# 65. Observation ≠ Result

Observation MAY detect/record phenomenon.

Но:

    Observation
    ≠ Result intrinsically

Result требует reference-frame semantics.

---

# 66. Unknown Result

Если Result неизвестен:

    Result unknown
    ≠ no Result

Unknown downstream phenomenon MUST NOT заменяться:

- zero;
- no change;
- success;
- failure.

Если Result Content неизвестен, это MAY быть partial Result representation, но не completed Result under minimum Core.

---

# 67. No observed Result

    no observed Result
    ≠ no Result occurred

Причиной отсутствия Observation MAY быть:

- no monitoring;
- insufficient detection;
- insufficient time window;
- missing data;
- other limitations.

---

# 68. Zero Result

Значение:

    0

MAY быть valid Result Content.

Но:

    zero
    ≠ unknown
    ≠ missing
    ≠ not measured

---

# 69. Missing data

Missing data MUST NOT автоматически интерпретироваться как:

- zero;
- no change;
- no Effect;
- no Event;
- success;
- failure.

---

# 70. Null result terminology

Term:

    null result

является domain-specific.

Он MUST NOT получать universal Core semantics.

В statistical/scientific Profile он MAY иметь defined meaning, но:

    null result
    ≠ no data
    ≠ no Event
    ≠ no Effect with certainty

---

# 71. Partial Result

Result MAY быть partial относительно:

- Scope;
- time window;
- population;
- Outcome;
- Objective;
- Measurement coverage.

Partiality MUST сохраняться.

---

# 72. Preliminary Result

Preliminary Result MAY существовать до later/final estimate.

Но:

    preliminary
    ≠ final

Historical preliminary semantics MUST NOT silently disappear if materially relevant.

---

# 73. Final Result

`Final` является Profile/context-specific semantics.

It MAY mean:

- end of defined observation window;
- formally accepted Result;
- protocol-defined final estimate;
- no further update expected.

Core не вводит universal finality.

---

# 74. Result revision

Необходимо различать:

- Correction;
- new Observation;
- revised estimate;
- extended data;
- new Result period;
- new reference frame.

Changed value alone MUST NOT определять identity.

A later estimate MUST NOT автоматически:

- replace;
- merge with;
- become new Result;

solely because numeric value changed.

Likewise:

    same value
    ≠ same Result automatically

Identity зависит от:

- frame;
- phenomenon;
- period;
- Scope;
- provenance;
- comparison semantics;
- other materially relevant distinctions.

---

# 75. Historical Result State

Historical Result MUST NOT silently drift with later data.

Например:

    Result@T1
    based on 100 cases

    ≠

    Result@T2
    based on 1000 cases

Если Result@T1 использовался downstream, его historical State MUST оставаться resolvable.

---

# 76. Result and Decision Basis

Later Result MUST NOT retroactively enter earlier Decision Basis.

    Decision at T1
    Result observed at T2

не означает:

    Result@T2
    was Basis of Decision@T1

unless contemporaneous equivalent evidence existed independently.

---

# 77. Result and Action history

Later Result MUST NOT rewrite Action history.

    bad Result
    ≠ different Action Content

    good Result
    ≠ broader Action Scope

---

# 78. Result and Event history

Later assignment of Result role MUST NOT rewrite underlying Event identity automatically.

Event MAY later acquire Result role while remaining same underlying occurrence.

---

# 79. Causal boundary

`010` устанавливает **границы causal interpretation**, а не полную causal inference ontology.

Concepts such as:

- confounding;
- mediation;
- moderation;
- effect modification;
- counterfactual causal estimation;

являются illustrative/domain concepts, если они отдельно не стандартизированы.

---

# 80. Causal attribution

Result relation and causal relation MUST remain distinct.

    Result relative to X
    ≠ X caused Result

Causal attribution requires separate support.

---

# 81. Causal provenance

Causal attribution SHOULD сохранять when material:

- Evidence;
- Inference;
- causal Model;
- uncertainty;
- scope;
- assumptions;
- alternative explanations;
- time frame;
- Context.

---

# 82. Direct Result / Direct Effect

Terms:

    direct Result
    direct Effect

MUST NOT использоваться без defined causal/operational semantics.

Temporal proximity alone:

    ≠ direct causality

---

# 83. Indirect Result

Term:

    indirect Result

requires defined intermediate relation/mechanism when material.

It is not intrinsic Result subtype.

---

# 84. Multiple contributing causes

A Result MAY иметь multiple contributing causes.

No single Action, Decision or Intervention receives complete causal attribution automatically.

---

# 85. Confounding

Observed association MAY быть affected by other factors.

Known materially relevant confounding SHOULD NOT silently disappear from causal interpretation.

But `010` не определяет full confounding ontology.

---

# 86. Mediation

Result MAY arise through intermediate Events, Actions or Processes.

Например:

    Action A
    → Event E
    → Process P
    → Result R

Direct/indirect attribution MUST remain explicit when material.

---

# 87. Context dependence

Result MAY depend on:

- population;
- environment;
- dose/intensity;
- timing;
- baseline;
- system version;
- concurrent Actions;
- Procedure version;
- other Context.

Result from Context X MUST NOT silently generalize to Context Y.

---

# 88. Transfer of Result

Historical Result in Context X does not imply same Result in Context Y.

Transfer requires:

- Inference;
- Assessment;
- Model;
- other transfer semantics.

---

# 89. Replication

Same Action Content repeated MAY produce different Results.

Therefore:

    same Action
    ≠ same Result automatically

Likewise:

    same Result
    ≠ same mechanism automatically

---

# 90. Reproducibility

Reproducibility is cross-case evaluative/empirical semantics.

It is not intrinsic property of one Result.

---

# 91. Outcome Realization

**Outcome Realization** — relational comparison semantics describing whether and to what extent a defined Outcome became realized.

Outcome Realization MAY use:

- Result semantics;
- Event semantics;
- Action semantics;
- other relevant Evidence.

It does NOT require a mandatory materialized Result Record as its only input.

It requires:

- defined Outcome;
- sufficient downstream evidence semantics;
- comparison relation.

Illustrative labels MAY include:

- complete;
- partial;
- none;
- unknown;
- disputed.

These labels are illustrative only and MUST NOT be treated as a universal closed, ordered or quantitative scale unless a Profile explicitly defines such semantics.

---

# 92. Outcome Realization ≠ Result

Например:

    Decision Outcome:
    evacuate 100 people

    Result:
    60 evacuated

    Outcome Realization:
    partial

Следовательно:

    Result
    ≠ Outcome Realization

---

# 93. Outcome Realization ≠ Objective Achievement

Outcome MAY быть полностью реализован, а Objective не достигнут.

Например:

    Outcome:
    close road

    Result:
    road closed

    Objective:
    reduce accidents

Если accidents не снизились:

    Outcome realized
    ≠ Objective achieved

---

# 94. Objective Achievement

**Objective Achievement** — relational comparison/evaluative semantics, определяющая, был ли defined Objective достигнут относительно Result(s), Evidence, Comparison Reference и defined criteria.

Objective Achievement не является intrinsic property Result.

---

# 95. Objective ambiguity

Vague Objective:

    improve safety

не позволяет автоматически invent exact criteria.

Если criteria unknown:

    Objective Achievement
    MAY remain unresolved

---

# 96. Multiple Objectives

One Intervention MAY иметь multiple Objectives.

Например:

    Objective 1 achieved
    Objective 2 partially achieved
    Objective 3 not achieved

Core не требует universal overall success score.

---

# 97. Conflicting Objectives

Result MAY улучшать один Objective и ухудшать другой.

Например:

    throughput increased
    safety decreased

Tradeoff aggregation belongs to Assessment/Decision analysis, not automatic Result semantics.

---

# 98. Effectiveness

**Effectiveness** — causal/evaluative или attribution-sensitive semantics concerning the extent to which Action, Decision implementation, Intervention or Process contributed to achieving a defined Objective or producing a defined Result under the applicable domain/model semantics.

Effectiveness requires a resolvable target:

    effective for what?

It MUST NOT be inferred solely from observed Result.

---

# 99. Effectiveness ≠ Outcome Realization

Outcome MAY be realized while intervention remains ineffective relative to broader Objective or selected evaluation frame.

---

# 100. Effectiveness ≠ Objective Achievement

Objective MAY be achieved due to unrelated causes.

Therefore:

    Objective achieved
    ≠ Effectiveness automatically

---

# 101. Effectiveness with partial Outcome Realization

Partial Outcome Realization does not automatically imply low Effectiveness.

Например:

    Outcome target:
    vaccinate 1000

    realized:
    800

    broader objective:
    reduce outbreak

Objective impact MAY still be substantial.

---

# 102. Efficiency

Efficiency involves relation between:

- Result/output;
- resources;
- cost;
- time;
- other inputs.

Therefore:

    effectiveness
    ≠ efficiency

`010` не определяет complete Efficiency ontology.

---

# 103. Harm / Benefit

Harm and benefit are contextual/evaluative semantics.

Result MAY support Harm/Benefit Assessment.

But:

    Result
    ≠ harm/benefit intrinsically

---

# 104. Safety Result

Descriptive Result:

    0 injuries observed over 30 days

does not imply:

    system universally safe

Safety requires broader Assessment and Context.

---

# 105. Adverse Result

`Adverse Result` MAY be Profile/domain vocabulary.

Core SHOULD preserve descriptive Result semantics and separate adverse evaluation where practical.

---

# 106. Side Effect

Side Effect is domain-sensitive terminology.

It MAY be:

- intended/unintended;
- expected/unexpected;
- harmful/neutral/beneficial.

It is not mandatory Core subtype.

---

# 107. Result sequence

Results MAY appear at different times:

    immediate R1
    delayed R2
    long-term R3

Temporal sequence does not automatically define:

- causality;
- dependency;
- one Result identity.

---

# 108. Result chain

A Result MAY become a reference frame/input for later Result analysis.

But:

    Result chain
    ≠ causal chain automatically

---

# 109. Result relations

Results MAY have relations such as:

- precedes;
- follows;
- refines;
- supersedes estimate;
- derived from;
- measured by;
- compares to;
- associated with;
- other Profile-defined relations.

`010` SHOULD reuse generic project relation infrastructure.

Generic relation SHOULD NOT replace a known more specific relation when materially relevant.

---

# 110. Relation provenance

Relations between Results MAY be:

- directly recorded;
- computed;
- inferred;
- assessed;
- reconstructed;
- disputed.

Materially relevant provenance MUST remain resolvable.

---

# 111. Statistical Result

Statistical Result MAY include:

- estimate;
- interval;
- effect-size measure;
- test statistic;
- other domain quantities.

`010` does not define full statistical ontology.

Profiles MAY specialize.

---

# 112. Statistical significance ≠ importance

Statistical significance MUST NOT automatically imply:

- practical importance;
- causality;
- large magnitude;
- usefulness;
- clinical importance;
- Effectiveness.

---

# 113. No statistical significance ≠ no Effect

Likewise:

    not statistically significant
    ≠ proven absence of Effect

Uncertainty and study design matter.

---

# 114. Measurement error

Known materially relevant measurement limitations SHOULD preserve:

- instrument uncertainty;
- calibration;
- method;
- bias;
- missingness;
- other limitations.

---

# 115. Reporting bias

Absence of reported Result:

    ≠ Result absent

Selective reporting MAY distort available Result representation.

---

# 116. Selection / survivorship effects

Observed Result sample MAY exclude materially relevant units.

Therefore:

    observed sample Result
    ≠ universal Result

without generalization semantics.

---

# 117. Result conflict

Different Sources MAY report conflicting Results.

System MUST allow:

- competing Results;
- competing Claims;
- disputed measurements;
- different methods;
- different baselines;
- different populations/windows.

Conflict MUST NOT be resolved by arbitrary merge or averaging.

---

# 118. Apparent conflict

Different Result values MAY both be valid if they refer to different:

- time windows;
- populations;
- baselines;
- units;
- methods;
- Contexts;
- Scopes.

Semantic alignment is required before declaring contradiction.

---

# 119. Result comparison

Comparison requires materially sufficient alignment.

Before comparing R1/R2, relevant alignment MAY include:

- variable;
- units;
- scale;
- population;
- Comparison Reference;
- time window;
- method;
- Context;
- Scope.

---

# 120. Unit fidelity

Numerical Result MUST preserve units.

Например:

    mg/L
    ≠ g/L

Conversions MUST be explicit or resolvable.

---

# 121. Scale fidelity

Scale MAY be:

- absolute;
- relative;
- logarithmic;
- normalized;
- ordinal;
- other.

Representation MUST NOT silently change scale.

---

# 122. Percentage vs percentage points

From:

    20% → 30%

means:

    +10 percentage points

and:

    +50% relative increase

These MUST NOT be conflated.

---

# 123. Absolute vs Relative Result

Representation SHOULD preserve whether difference is:

- absolute;
- relative.

Relative changes MUST NOT silently substitute absolute changes or vice versa.

---

# 124. Normalization

Normalized Result MUST preserve normalization basis when material.

Otherwise value may become uninterpretable.

---

# 125. Result Context

Result Context MAY include:

- environment;
- population;
- system version;
- Procedure version;
- dose;
- season;
- operational conditions;
- concurrent Actions;
- other materially relevant conditions.

Context MUST NOT silently drift.

---

# 126. Historical Context preservation

Result@T1 MUST retain materially relevant Context@T1.

Current Context MUST NOT silently replace it.

---

# 127. System version

Result obtained under:

    System v1

MUST NOT automatically be represented as Result for:

    System v5

when version materially matters.

---

# 128. Procedure version

Likewise:

    Procedure P@v1
    ≠ Procedure P@current

if Procedure version materially affects Result interpretation.

---

# 129. Result Import

External systems MAY use terms:

- result;
- outcome;
- effect;
- response;
- endpoint;
- finding;
- output;
- consequence.

External label alone MUST NOT determine canonical Result semantics.

Semantic function determines mapping.

---

# 130. Output ≠ Result automatically

System output MAY be:

- intermediate data;
- prediction;
- command;
- log;
- Measurement;
- Result.

Therefore:

    output label
    ≠ Result automatically

---

# 131. Endpoint

Endpoint MAY define a domain-specific outcome measure.

Endpoint is not required as separate Core Entity by `010`.

---

# 132. Finding

Finding MAY be:

- Claim;
- Observation;
- Result;
- Assessment;
- Inference.

External term does not determine ontology.

---

# 133. Historical Result ≠ current expectation

Historical:

    intervention had Result R in Context X

does NOT imply:

    same Result will occur now

Transfer requires separate reasoning.

---

# 134. Historical Result ≠ Recommendation

Historical Result MUST NOT automatically become:

- Recommendation;
- Instruction;
- Decision rule;
- current treatment/procedure advice.

---

# 135. Representation Fidelity

Representation MUST NOT materially alter:

- Result Content;
- reference frame;
- Comparison Reference;
- Scope;
- Observation/Data Scope;
- population;
- time window;
- units;
- provenance status;
- uncertainty;
- causal status;
- Context.

---

# 136. Translation Fidelity

Translation MUST preserve distinctions such as:

    associated with
    ≠ caused by

    Result of
    ≠ caused by automatically

    improvement
    ≠ recovery

    partial
    ≠ complete

    estimate
    ≠ exact

    observed
    ≠ inferred

    no detected difference
    ≠ no difference

---

# 137. Logical Fidelity

Representation SHOULD preserve:

- negation;
- quantifiers;
- intervals;
- thresholds;
- conditions;
- subgroup boundaries;
- time windows.

Например:

    no increase detected
    ≠ decrease occurred

---

# 138. Summary Fidelity

Summary MUST NOT convert:

    sample Result
    → population Result

    estimated Result
    → exact Result

    associated Result
    → causal Effect

    short-term Result
    → permanent Result

    Result in Context X
    → universal Result

    missing data
    → zero

---

# 139. Damaged archives

Historical Result MAY be partially preserved.

Example:

    "... harvest increased ..."

Missing:

- amount;
- baseline;
- year;
- region;
- population;
- causal explanation;

MUST NOT be invented.

---

# 140. Result reconstruction

Historical Result MAY be reconstructed.

Reconstruction MUST preserve:

- provenance;
- assumptions;
- uncertainty;
- competing interpretations;
- source limitations.

---

# 141. Result provenance

Result provenance MAY include:

- Source;
- Observation;
- Measurement;
- computation;
- Inference;
- Model;
- Assessment;
- reconstruction.

No single provenance type is universal.

---

# 142. Offline preservation

Result SHOULD be representable without dependence on modern platform.

Where materially relevant, preserve:

- Result Content;
- reference frame;
- Comparison Reference;
- units;
- Scope;
- Observation/Data Scope;
- population;
- time window;
- Context;
- provenance;
- uncertainty;
- causal status.

---

# 143. Carrier neutrality

Result semantics does not depend on:

- database;
- Markdown;
- JSON;
- spreadsheet;
- scientific paper;
- printed table;
- archive;
- other durable carrier.

Carrier does not define Result ontology.

---

# 144. High-risk Profiles

High-risk Profiles MAY require stricter Result representation.

Examples:

- medicine;
- epidemiology;
- engineering;
- environmental monitoring;
- safety;
- survival procedures.

Profile MAY require:

- exact variable definition;
- units;
- population;
- Comparison Reference;
- time window;
- uncertainty;
- adverse Results;
- method;
- causal status;
- replication;
- data completeness.

These are not universal Core requirements.

---

# 145. Result quality

`010` does not introduce universal intrinsic Result Quality.

Quality aspects MAY include:

- precision;
- validity;
- reliability;
- completeness;
- bias;
- relevance;
- applicability.

These belong to Assessment/Profile semantics.

---

# 146. Conformance and Integrity

Need distinguish:

    Core structural/semantic conformance
    ≠ historical/provenance integrity
    ≠ measurement validity
    ≠ causal certainty
    ≠ Result quality
    ≠ Representation Fidelity

Core PASS does not mean:

- Result true with certainty;
- Result caused by reference frame;
- Objective achieved;
- intervention effective;
- Result beneficial.

---

# 147. Profiles

Profile MAY strengthen Core.

Profile MUST NOT weaken Core while claiming compatibility with `010`.

---

# 148. Diagnostic families

Diagnostic terminology describes semantic failure patterns.

## 148.1. Reference-frame failures

Examples:

- Event treated as Result without frame;
- Result linked to wrong frame;
- neutral Result relation turned causal;
- reference frame omitted;
- structured frame roles flattened;
- distinct Result role treated as intrinsic phenomenon.

## 148.2. Comparison / Scope failures

Examples:

- wrong baseline;
- control treated as baseline automatically;
- Comparison Reference confused with Objective criterion;
- sample → population;
- Result Scope → Observation/Data Scope;
- short-term → permanent;
- Context X → universal.

## 148.3. Measurement / provenance failures

Examples:

- estimate → exact;
- modeled → observed;
- inferred → measured;
- missing → zero;
- preliminary → final;
- revised estimate → silent replacement.

## 148.4. Causality failures

Examples:

- after → caused by;
- downstream → causally downstream;
- Result → Effect automatically;
- association → causation;
- one Action → sole cause;
- Objective achieved → Effectiveness.

## 148.5. Evaluation failures

Examples:

- Result → success;
- Result → benefit;
- Outcome Realization → Objective Achievement;
- Objective Achievement → Effectiveness;
- statistical significance → importance.

Diagnostic label itself does not establish:

- intent;
- fraud;
- negligence;
- responsibility;
- blame.

---

# 149. Machine validation

Validator MAY check:

- required Result Content;
- reference frame presence;
- reference integrity;
- units;
- Scope;
- Comparison Reference when required;
- time windows;
- Profile requirements;
- structural consistency.

But:

    validator PASS
    ≠ Result true
    ≠ causal
    ≠ beneficial
    ≠ Objective achieved
    ≠ effective

Validator has no truth privilege.

---

# 150. Cross-standard compatibility

`010-RESULT` MUST preserve neighboring semantic boundaries.

In compact form:

    Claim
    → что утверждается

    Evidence Use
    → что используется как evidence

    Assessment
    → как что-либо оценивается

    Inference
    → что выводится

    Decision
    → что решено

    Action
    → что сделано

    Event
    → что произошло

    Result
    → какую downstream/result role
      phenomenon занимает
      относительно defined reference frame

Therefore:

    Claim about Result
    ≠ Result

    Event
    ≠ Result intrinsically

    State
    ≠ Result intrinsically

    Measurement
    ≠ Result intrinsically

    Observation
    ≠ Result intrinsically

    Decision Outcome
    ≠ Result

    Result
    ≠ Outcome Realization

    Result
    ≠ Objective Achievement

    Result
    ≠ Effectiveness

`010` MUST NOT consume neighboring ontologies.

---

# 151. Boundary concepts outside full 010 ontology

`010` uses neighboring concepts to establish Result boundaries.

These include:

- Event;
- State;
- Measurement;
- Observation;
- Effect;
- Consequence;
- Objective;
- Outcome Realization;
- Objective Achievement;
- Effectiveness;
- Efficiency;
- Comparison Reference.

`010` does not assert that their complete ontology belongs inside Result standard.

---

# 152. Entity Explosion Test

`010` НЕ требует введения следующих фундаментальных Core Entities только ради Result:

- ResultContent;
- ResultReferenceFrame;
- ComparisonReference;
- ResultBaseline;
- ResultScope;
- ObservationScope;
- DataScope;
- ResultPopulation;
- ExpectedResult;
- IntendedResult;
- DesiredResult;
- UnintendedResult;
- ObservedResult;
- InferredResult;
- ModeledResult;
- ComputedResult;
- PreliminaryResult;
- FinalResult;
- CompositeResult;
- ResultSeries;
- ResultChain;
- ResultCause;
- ResultEffect;
- ResultConsequence;
- OutcomeRealization;
- ObjectiveAchievement;
- Effectiveness;
- Efficiency;
- SideEffect;
- AdverseResult;
- Endpoint;
- ResultConfidence;
- ResultQuality.

These MAY be represented through:

- semantic roles;
- relations;
- Profiles;
- Assessments;
- Inferences;
- existing Records;
- generic infrastructure;
- future standards.

Absence of separate Core Entity does not mean absence of semantics.

---

# 153. Core invariants

Следующие положения образуют минимальное нормативное ядро `010-RESULT`.

### R-01
Result является relational semantic construct, представляющим phenomenon/content в downstream/result role относительно defined reference frame.

### R-02
Result role MAY быть materialized как specialized Record when independent identity, provenance, reuse or structured semantics are materially required; separate Result Entity is not universally mandatory.

### R-03
Result-role identity и materialized Result Record identity MUST NOT автоматически считаться одним и тем же понятием.

### R-04
Result MUST иметь defined Result Content.

### R-05
Result MUST иметь one defined reference frame or defined structured reference frame.

### R-06
Structured reference frame MUST сохранять materially relevant roles своих элементов.

### R-07
Result MUST сохранять sufficient Result attribution linking Result Content to its reference frame.

### R-08
Result attribution является semantic requirement и MUST NOT требовать separate Core Entity solely for conformance.

### R-09
Event, State, Measurement or Observation MUST NOT automatically become Result without Result-role semantics.

### R-10
Claim about Result MUST remain distinct from Result.

### R-11
Temporal succession alone MUST NOT establish Result relation.

### R-12
Downstream semantics MUST NOT automatically be interpreted as causal downstream semantics.

### R-13
Result relation MUST NOT automatically imply causal attribution.

### R-14
Natural-language framing MUST NOT silently strengthen neutral Result relation into causal claim.

### R-15
Effect MUST NOT receive one universal Core meaning through `010`; domain semantics MUST remain distinguishable.

### R-16
Decision Outcome MUST remain distinct from Result.

### R-17
Result MUST remain distinct from Outcome Realization.

### R-18
Result MUST remain distinct from Objective Achievement.

### R-19
Result MUST remain distinct from Effectiveness.

### R-20
Result MUST NOT automatically be interpreted as success, benefit, harm or quality judgment.

### R-21
Expected, intended, desired and observed semantics MUST remain distinguishable when materially relevant.

### R-22
Observed, computed, inferred, modeled and reconstructed provenance dimensions MAY overlap and MUST remain resolvable when materially relevant.

### R-23
Unknown Result MUST NOT be represented as zero, missing, no change, success or failure.

### R-24
Missing data MUST NOT automatically be represented as zero or no Effect.

### R-25
Domain terms such as `null result` MUST NOT receive universal Core semantics.

### R-26
Result Scope, Observation/Data Scope, Action Scope and total Effect Scope MUST remain distinct when materially relevant.

### R-27
Result Scope MUST represent scope attributed to represented Result phenomenon and MUST NOT imply complete objective knowledge of underlying phenomenon extent.

### R-28
Sample Result MUST NOT automatically become population Result.

### R-29
Aggregate Result MUST NOT imply identical individual Results.

### R-30
One reference frame MAY have multiple Results, and one Result MAY relate to multiple upstream reference elements.

### R-31
Same Result Content MUST NOT automatically imply same Result identity.

### R-32
Different reports/representations MUST NOT automatically imply different Result identities.

### R-33
Distinct Result roles MUST NOT automatically imply distinct underlying phenomena.

### R-34
Distinct Result-role instances MUST NOT require duplication of underlying content/occurrence representation solely because reference-frame semantics differs.

### R-35
Baseline is conditional and MUST NOT be required when Result meaning does not depend on comparison.

### R-36
Comparison Reference MUST remain resolvable when comparative Result semantics materially depends on it.

### R-37
Prior State or control MUST NOT automatically be treated as baseline.

### R-38
Comparison Reference, Objective criterion и threshold MUST remain distinguishable when materially relevant.

### R-39
Counterfactual comparator MUST NOT be represented as historical observed Result.

### R-40
Result time, phenomenon time, measurement time, observation time, reporting time and evaluation time MUST remain distinguishable when materially relevant.

### R-41
Historical Result Context MUST NOT silently drift to current Context.

### R-42
Historical Result MUST NOT silently update or disappear when later data changes the estimate.

### R-43
Changed estimate alone MUST NOT determine whether representation is Correction, revised Result or new Result identity.

### R-44
Later Result MUST NOT be inserted retroactively into earlier Decision Basis.

### R-45
`010` defines causal boundaries and MUST NOT be interpreted as complete causal inference ontology.

### R-46
Causal attribution MUST preserve materially relevant provenance, uncertainty, scope and assumptions.

### R-47
Temporal succession or association MUST NOT automatically become causal attribution.

### R-48
Outcome Realization является relational comparison semantics and MUST remain distinct from Result.

### R-49
Outcome Realization MUST NOT require a materialized Result Record when sufficient Event/Action/Evidence semantics exists.

### R-50
Illustrative Outcome Realization labels MUST NOT be treated as universal closed or ordered scale unless defined by a Profile.

### R-51
Objective Achievement MUST remain distinct from Outcome Realization.

### R-52
Objective Achievement MUST remain distinct from Effectiveness.

### R-53
Effectiveness MUST preserve applicable domain/model semantics and requires a defined target/reference beyond Result observation alone.

### R-54
Effectiveness MUST NOT automatically be inferred from observed Result or Objective Achievement.

### R-55
Statistical significance MUST NOT automatically imply practical importance, causality or Effectiveness.

### R-56
Absence of statistical significance MUST NOT automatically imply absence of Effect.

### R-57
Units, scales, relative/absolute measures, percentage points, normalization bases and time windows MUST remain resolvable when materially relevant.

### R-58
Result comparison MUST NOT occur without materially sufficient semantic alignment.

### R-59
External labels such as outcome, effect, endpoint, finding or output MUST NOT automatically determine Result semantics.

### R-60
Historical Result MUST NOT automatically become current expectation, Recommendation or transferable rule.

### R-61
Representation MUST NOT upgrade estimated, inferred, modeled or reconstructed Result into exact/directly observed Result.

### R-62
Core structural/semantic conformance MUST remain distinct from historical/provenance integrity, measurement validity, causal certainty, Result quality and Representation Fidelity.

### R-63
Profile MAY strengthen Core requirements but MUST NOT weaken Core while claiming compatibility with `010`.

### R-64
Materially relevant uncertainty, provenance, reference frame, Comparison Reference and Context MUST remain resolvable.

---

# 154. Stress-test framework

Архитектура `010-RESULT` должна выдерживать как минимум следующие классы атак:

1. Event with no Result role;
2. Claim about Result vs Result;
3. Result role vs Result Record identity;
4. same Event as Result under multiple frames;
5. distinct Result roles sharing one underlying phenomenon;
6. structured reference frames;
7. flattened reference-frame roles;
8. downstream without chronology;
9. downstream without causality;
10. natural-language causal laundering;
11. disputed causal attribution;
12. Effect terminology across domains;
13. one Action with many Results;
14. one Result with many upstream references;
15. unknown Result;
16. no observed Result;
17. missing data;
18. zero Result;
19. domain-specific null Result;
20. preliminary Result;
21. revised Result;
22. same value across different Results;
23. historical Result state;
24. expected vs actual;
25. intended vs expected;
26. desired vs expected;
27. unintended Result;
28. immediate vs delayed;
29. Result time window;
30. measurement time vs Result interval;
31. Action Scope vs Result Scope;
32. Result Scope vs Observation/Data Scope;
33. Result Scope uncertainty;
34. Result Scope vs total Effect Scope;
35. sample vs population;
36. aggregate vs individual;
37. subgroup heterogeneity;
38. same Result Content under different frames;
39. different reports of same Result;
40. composite Results;
41. baseline absent when not needed;
42. baseline ambiguity;
43. wrong baseline;
44. control comparator;
45. target as comparator vs Objective;
46. threshold vs Comparison Reference;
47. counterfactual comparator;
48. Measurement vs Result;
49. Observation vs Result;
50. inferred Result;
51. reconstructed Result;
52. modeled Result;
53. computed Result;
54. overlapping provenance statuses;
55. causal confounding;
56. causal mediation;
57. context dependence;
58. transfer across Contexts;
59. replication with different Results;
60. Decision Outcome vs Result;
61. Outcome Realization without Result Record;
62. Outcome Realization label misuse;
63. Objective Achievement;
64. multiple Objectives;
65. conflicting Objectives;
66. Objective Achievement without Effectiveness;
67. Effectiveness with partial Outcome Realization;
68. domain-sensitive Effectiveness;
69. Efficiency vs Effectiveness;
70. harm/benefit evaluation;
71. adverse Result;
72. side effects;
73. Result sequence;
74. Result chain;
75. conflicting Results;
76. apparent conflict due to population/window differences;
77. units mismatch;
78. scale mismatch;
79. percentage vs percentage points;
80. absolute vs relative measure;
81. normalization basis;
82. system version drift;
83. Procedure version drift;
84. output/result ambiguity;
85. endpoint terminology;
86. finding terminology;
87. historical Result vs current expectation;
88. historical Result vs Recommendation;
89. translation corruption;
90. summary corruption;
91. damaged archives;
92. reconstruction;
93. offline preservation;
94. high-risk Profiles;
95. cross-standard collisions.

Stress-test cases не создают Core requirements самостоятельно.

Если новый test выявляет необходимое фундаментальное правило, оно должно быть внесено в соответствующий normative section.

Прохождение stress-test не является доказательством полноты или окончательности модели.

---

# 155. Принцип сохранения

При конфликте между полнотой и честностью representation предпочтение отдаётся честности.

    downstream phenomenon
    > invented causal effect

    unknown Result
    > false zero

    missing data
    > invented no-effect

    sample Result
    > false population claim

    estimated Result
    > false precision

    partial Result
    > falsely complete Result

    historical Context
    > current-context substitution

    uncertain causality
    > post hoc causality

    valid Comparison Reference
    > convenient invented baseline

    domain-specific semantics
    > false universal definition

Цель стандарта — сохранить Result настолько полно, насколько позволяют данные, **не превращая downstream relation в causal effect, Result в success, Outcome Realization в Objective Achievement, Objective Achievement в Effectiveness или локальный Result в универсальную истину**.

---

# 156. Итоговая формула

В наиболее компактной форме:

    Decision
    → что было решено

    Action
    → что было сделано

    Event
    → что произошло

    Result
    → какую downstream/result role
      phenomenon занимает относительно
      defined reference frame

    Outcome Realization
    → насколько реализовался defined Outcome

    Objective Achievement
    → насколько достигнут defined Objective

    Effectiveness
    → насколько upstream Action /
      Decision implementation /
      Intervention / Process
      способствовал defined Result
      или Objective в рамках
      applicable domain/model semantics

    Assessment
    → как всё это оценивается

    Inference
    → что из этого выводится

Центральный принцип `010-RESULT`:

> **Сохранить Result — значит сохранить максимально честное представление о phenomenon/content в downstream/result role относительно определённого reference frame вместе с materially relevant Scope, Comparison Reference, Context, provenance и uncertainty.**

Факт Result сам по себе не означает causality, success, benefit, Outcome Realization, Objective Achievement или Effectiveness.

---

## Статус версии

**010-RESULT v0.1**

Архитектура прошла:

- первичную полную сборку;
- сквозную атаку стандарта;
- контрольный аудит собранного файла;
- проверку Result role / Result Record;
- проверку Result / Claim;
- проверку Result / Event;
- проверку reference-frame semantics;
- проверку structured reference frames;
- проверку downstream / causal boundary;
- проверку Result / Effect / Consequence;
- проверку Decision Outcome / Result;
- проверку Outcome Realization;
- проверку Objective Achievement;
- проверку Effectiveness;
- проверку Comparison Reference / baseline;
- проверку Measurement / Observation boundary;
- проверку Result Scope / Observation Scope;
- проверку sample / population;
- проверку provenance dimensions;
- проверку statistical representation;
- проверку historical-state preservation;
- проверку compatibility с `007-DECISION`, `008-ACTION`, `009-EVENT`;
- Entity Explosion Test.

**Критических архитектурных противоречий: 0.**  
**Новых обязательных Core Entities: 0.**  
**Невнесённых замечаний контрольного аудита: 0.**

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
