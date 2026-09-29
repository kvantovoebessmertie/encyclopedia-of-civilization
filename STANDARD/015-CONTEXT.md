# 015 — CONTEXT
## Стандарт контекста, применимости и Context Fidelity

**Проект:** Энциклопедия цивилизации  
**Статус:** зафиксированная версия  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляется Context — совокупность условий, обстоятельств и contextual settings, представленных как материально relevant или potentially материально relevant относительно определённого target, внутри которых knowledge representation получает определённый смысл, применимость, наблюдаемость, измеримость или интерпретацию.

Цель стандарта — позволить сохранять:

- к какому target относится Context;
- какие contextual dimensions материально relevant или potentially материально relevant;
- какие значения этих dimensions известны;
- каков epistemic status contextual values;
- когда Context действителен;
- какие части Context наблюдались, измерялись, сообщались, предполагались, выводились, моделировались или реконструировались;
- где Context отличается от State;
- где Context отличается от Scope;
- где Context отличается от semantic/reference frame;
- где Context отличается от Participant;
- где Context отличается от Evidence;
- где Context отличается от Provenance;
- где Context отличается от Assumption;
- где Context отличается от Preconditions;
- где Context отличается от Profile;
- какие contextual conditions материально влиять applicability;
- как Context наследуется;
- как Context переопределяется;
- как Context composed;
- допустим ли переносить knowledge между Contexts;
- насколько transferability partial, conditional или uncertain;
- как сохраняется historical Context;
- как предотвращается Context drift;
- как Context сохраняется при translation, summary, compression и offline использовать.

Стандарт не предназначен для автоматического определения:

- истинности knowledge representation;
- полноты реального Context;
- причинности contextual factors;
- того, что Context является Participant;
- того, что Context является State;
- того, что Context является Scope;
- того, что Context и applicable frame — одно и то же;
- того, что Context известен полностью;
- того, что отсутствие Context означает universal applicability;
- того, что отсутствие Context делает knowledge автоматически недействительным;
- того, что knowledge допустимый в Context X автоматически допустимый в Context Y;
- того, что similar или compatible Contexts обеспечивают applicability Claim;
- того, что similar Contexts обеспечивают одинаковую transferability;
- того, что Context dimensions независимы;
- того, что Context values из разных Sources относятся к одной реальной ситуации;
- того, что modern Context применим к historical knowledge.

Сохранить Context означает сохранить максимально честное представление об условиях, представленных как материально relevant или potentially материально relevant, относительно которых knowledge representation имеет определённый смысл, наблюдалось, измерялось, применяется или оценивается, не превращая неизвестный Context в universal Context, Context в State, Scope, Cause или Evidence, assumption в observation, laboratory conditions в universal field conditions, а похожие или совместимые Contexts — в доказанную применимость или переносимость знания.

---

# 1. Основное понятие

## 1.1. Context

**Context (Контекст)** — semantic construct, представляющий conditions, circumstances или contextual settings, рассматриваемые как материально relevant или potentially материально relevant относительно определённого target, внутри которых knowledge representation интерпретируется, наблюдается, измеряется, применяется, сравнивается или оценивается.

Context отвечает на основной вопрос:

> **При каких условиях, существенных или потенциально существенных для рассматриваемого знания, данное representation имеет указанный смысл, было получено, наблюдалось, измерялось, произошло или применяется?**

Context МОЖЕТ включать:

- physical conditions;
- environmental conditions;
- temporal conditions;
- spatial conditions;
- technical conditions;
- biological conditions;
- social conditions;
- cultural conditions;
- linguistic conditions;
- legal conditions;
- institutional conditions;
- experimental conditions;
- procedural conditions;
- model conditions;
- system/version conditions;
- other domain-specific conditions.

---

# 2. Context representation ≠ complete reality

Recorded Context является representation.

Следовательно:

    recorded Context
    ≠ complete real-world Context

Context МОЖЕТ быть:

- partial;
- approximate;
- uncertain;
- reported;
- assumed;
- inferred;
- modeled;
- reconstructed;
- disputed.

Representation НЕ ДОЛЖЕН означать contextual completeness если не completeness itself justified.

---

# 3. Context semantics ≠ mandatory Context Entity

Context не обязан существовать как отдельная fundamental Core Entity.

Context МОЖЕТ быть представленный through:

- fields;
- Relations;
- States;
- Records;
- temporal structures;
- spatial structures;
- Measurements;
- Models;
- Profiles;
- qualified metadata;
- other generic infrastructure.

Context МОЖЕТ быть materialized as Record когда материально useful for:

- reuse;
- provenance;
- versioning;
- dispute;
- complex composition;
- historical reconstruction.

Но:

    Context semantics
    ≠ mandatory fundamental Context Entity

---

# 4. Context is target-relative

Context всегда является Context **для чего-либо**.

Context МОЖЕТ contextualize:

- Claim;
- Observation;
- Measurement;
- State;
- Event;
- Process;
- Action;
- Result;
- Relation;
- Identity judgment;
- Model;
- Procedure;
- Decision;
- Source interpretation;
- other representation.

Следовательно:

    Context
    requires a contextualized target
    when target distinction materially matters

---

# 5. Context target granularity

Context target МОЖЕТ быть:

- whole representation;
- one Claim;
- one subclaim;
- one Relation;
- one phase of Process;
- one Measurement;
- one Result component;
- one defined semantic component.

Therefore:

    Context of whole Record
    ≠ Context of every semantic component automatically

Context attachment ДОЛЖЕН сохранять target granularity когда material.

---

# 6. Context ≠ contextualized object

Contextualized object ДОЛЖЕН оставаться distinguishishable из Context.

Example:

    Process:
    fermentation

    Context:
    temperature = 25°C

Temperature condition:

    ≠ fermentation Process

Likewise:

    Event
    ≠ Event Context

    Claim
    ≠ Claim Context

---

# 7. Context ≠ State

State describes a condition/configuration **of a subject**.

Context describes conditions represented as materially relevant or potentially materially relevant **relative to a contextualized target**.

Therefore:

    State
    ≠ Context

Example:

    Tank A:
    temperature = 80°C

МОЖЕТ представлять:

    State of Tank A

Этот same factual condition МОЖЕТ also participate as:

    Context of Reaction R
    occurring inside Tank A

Thus:

    same factual condition
    МОЖЕТ участвовать в State semantics
    and Context semantics

without:

    State = Context

Semantic role ДОЛЖЕН оставаться явным где material.

---

# 8. Context need not be external

Context need not be physically external to the contextualized system.

Один condition МОЖЕТ function as:

- Context at one semantic boundary;
- State variable at another;
- Process variable at another;
- Result at another.

Example:

Temperature МОЖЕТ быть:

    initial Context of Process P

and later:

    State variable changed by P

Therefore:

    Context
    ≠ external environment only

---

# 9. Context ≠ Participant automatically

An Entity or condition present around Event/Process:

    ≠ Participant automatically

Example:

Ambient oxygen МОЖЕТ быть:

- Context;
- reactant Participant;
- both under different semantic roles.

где Один more specific Participant role материально matters, that role ДОЛЖЕН оставаться явным.

---

# 10. Context ≠ Scope

**Context** answers primarily:

> При каких условиях representation interpreted/observed/applies?

**Scope** answers primarily:

> К какому domain subset, population, object set, spatial/temporal subset или class representation applies?

Therefore:

    Context
    ≠ Scope

---

# 11. Context/Scope role relativity

A condition is not inherently Context or Scope.

Its semantic role depends on how it constrains the representation.

Example:

    age > 65

МОЖЕТ быть:

    Scope:
    persons age >65

while:

    hospital setting

МОЖЕТ быть:

    Context:
    conditions of Observation/application

Но Этот same condition МОЖЕТ legitimately участвовать в both Context и Scope Если both roles are материально relevant.

Therefore:

    same condition
    МОЖЕТ иметь multiple semantic roles

without:

    roles collapsing

---

# 12. Context ≠ semantic/reference frame

Один frame МОЖЕТ определять:

- semantic system;
- coordinate system;
- identity system;
- ontology;
- legal framework;
- reference system.

Context МОЖЕТ describe factual/material conditions within that frame.

Example:

    Identity frame:
    corporate law

    Context:
    registration State at T1

Therefore:

    Context
    ≠ frame universally

---

# 13. Context does not determine frame automatically

Factual Context НЕ ДОЛЖЕН автоматически определять semantic/reference frame.

Example:

    France, 1804

does not automatically mean:

    French legal frame

Один modern historical Model МОЖЕТ describe facts из France в 1804 using Один different analytical frame.

Thus:

    Context
    ≠ frame selection automatically

---

# 14. Context ≠ Profile

Profile defines domain/project-specific representation requirements.

Context represents conditions relevant to particular knowledge.

Thus:

    medical Profile
    ≠ patient Context

    engineering Profile
    ≠ operating Context

Profile МОЖЕТ требовать certain contextual dimensions.

---

# 15. Context ≠ Assumption

Assumption is accepted or stipulated for reasoning/modeling.

Context describes conditions represented as relevant to knowledge.

Example:

    Context:
    temperature measured as 20°C

    Assumption:
    temperature remained constant

Therefore:

    Context fact
    ≠ Assumption

---

# 16. Epistemic status of Context

Context values МОЖЕТ быть:

- observed;
- measured;
- reported;
- assumed;
- inferred;
- modeled;
- reconstructed;
- unknown.

эти statuses ДОЛЖЕН оставаться различимым когда material.

Especially:

    assumed Context
    ≠ observed Context

    modeled Context
    ≠ historical Context

    reconstructed Context
    ≠ directly observed Context

---

# 17. Context epistemic status preservation

When Context is:

- inherited;
- reused;
- translated;
- summarized;
- transferred;
- normalized;
- compressed;

its материально relevant epistemic status НЕ ДОЛЖЕН незаметно disappear.

Thus:

    assumed temperature = 20°C

НЕ ДОЛЖЕН становиться:

    temperature = 20°C

without preservation of assumption semantics.

---

# 18. Context ≠ Preconditions

Один Precondition МОЖЕТ быть required for Action, Process или Procedure.

Context МОЖЕТ contain Один condition satisfying that Precondition.

But:

    contextual condition present
    ≠ Precondition semantics automatically

and:

    Precondition
    ≠ full Context

---

# 19. Context ≠ Cause

Fundamental rule:

    contextual factor present
    ≠ causal factor automatically

Example:

    failures occurred under high humidity

does not by itself establish:

    humidity caused failures

Causal Relation requires separate justification.

---

# 20. Context relevance ≠ causality

Even a contextual factor known to affect applicability:

    ≠ Cause of phenomenon automatically

Один factor МОЖЕТ matter for:

- interpretation;
- comparison;
- measurement;
- applicability;
- classification;

without causal role.

---

# 21. Context ≠ Evidence

Contextual information МОЖЕТ itself быть supported by Evidence.

Example:

    Context:
    temperature = 30°C

    Evidence:
    Measurement M

Therefore:

    Context
    ≠ Evidence

---

# 22. Context ≠ Provenance

Provenance answers:

> Откуда representation происходит?

Context answers:

> При каких conditions representation applies/was observed?

Therefore:

    Context
    ≠ Provenance

---

# 23. Context ≠ storage metadata

Not every metadata field is semantic Context.

Examples:

    database row ID
    file size
    upload date
    internal checksum

are not automatically Context of represented knowledge.

Thus:

    storage metadata
    ≠ domain Context automatically

---

# 24. Anti-garbage principle

Один fact НЕ ДОЛЖЕН быть classified merely as Context because Это is somehow related to Этот contextualized object.

где Один more specific semantic role is материально relevant, that role ДОЛЖЕН быть сохранённый.

Examples:

    Cause
    must remain Cause

    Evidence
    must remain Evidence

    Participant
    must remain Participant

    Scope
    must remain Scope

    Assumption
    must remain Assumption

    State
    must remain State

    Objective
    must remain Objective

    Result
    must remain Result

Один semantic element МОЖЕТ additionally contribute contextual information, Но Context НЕ ДОЛЖЕН становиться Один universal garbage container for every related fact.

---

# 25. Context granularity

Context МОЖЕТ быть представлен broadly:

    tropical climate

or precisely:

    31.2°C
    RH 82%
    pressure 1004 hPa

Granularity depends on material relevance and available knowledge.

---

# 26. More Context ≠ better Context automatically

Maximum metadata is not automatically maximum semantic quality.

Context representation СЛЕДУЕТ сохранять материально relevant distinctions без requiring exhaustive description из reality.

---

# 27. Context completeness

Context МОЖЕТ быть incomplete.

System ДОЛЖЕН permit:

    known dimensions
    +
    unknown dimensions

Missing values НЕ ДОЛЖЕН быть придуманный merely to satisfy Один полный schema.

---

# 28. Unknown Context

Fundamental rule:

    unknown Context
    ≠ universal Context

    unknown Context
    ≠ default Context

    unknown Context
    ≠ context independence

---

# 29. Missing Context ≠ universal applicability

If contextual metadata is missing:

    ≠ knowledge universally applicable

Absence из recorded Context НЕ ДОЛЖЕН expand Claim applicability автоматически.

---

# 30. Missing Context ≠ automatic invalidity

Opposite safeguard:

    missing Context
    ≠ knowledge automatically invalid
    ≠ knowledge automatically useless

Insufficient Context МОЖЕТ влиять:

- interpretability;
- confidence;
- transferability;
- applicability;
- risk;
- safety assessment;

depending on domain and Profile.

---

# 31. Explicit Context independence

Some knowledge МОЖЕТ быть supported as invariant или context-independent within определённый semantics.

But:

    no Context recorded
    ≠ context-independent

Context independence requires positive epistemic support when materially relevant.

---

# 32. Context dimensions

Context МОЖЕТ contain multiple dimensions.

Examples:

- temperature;
- humidity;
- pressure;
- location;
- jurisdiction;
- language;
- system version;
- date;
- equipment configuration;
- biological State;
- institutional regime.

Core НЕ ДОЛЖЕН impose one universal dimension list.

---

# 33. Context dimension semantics

Same dimension label МОЖЕТ иметь different meanings across domains.

Example:

    pressure

could mean:

- atmospheric pressure;
- blood pressure;
- hydraulic pressure.

Dimension meaning ДОЛЖЕН оставаться разрешимым где material.

---

# 34. Context dimensions МОЖЕТ быть dependent

Context decomposition into dimensions НЕ ДОЛЖЕН означать that those dimensions are independent.

Dimensions МОЖЕТ иметь:

- dependencies;
- compatibility constraints;
- joint semantics;
- conditional relationships;
- configuration dependencies.

Example:

    software version V
    plugin version P

may only be meaningful as a valid pair.

Thus:

    decomposed Context
    ≠ independent dimensions automatically

---

# 35. Context value

Context value МОЖЕТ быть:

- quantitative;
- categorical;
- interval;
- range;
- approximate;
- uncertain;
- unknown.

Units ДОЛЖЕН оставаться разрешимым где material.

---

# 36. Context uncertainty

Example:

    approximately 20°C

НЕ ДОЛЖЕН становиться:

    exactly 20°C

Context uncertainty is knowledge uncertainty.

---

# 37. Temporal Context

Temporal Context МОЖЕТ включать:

- date;
- era;
- season;
- interval;
- phase;
- legal period;
- system-version period.

---

# 38. Context time ≠ other times

Need distinguish:

    time of represented phenomenon
    ≠ Observation time
    ≠ Measurement time
    ≠ Source publication time
    ≠ Record creation time
    ≠ database modification time

эти НЕ ДОЛЖЕН схлопываться когда материально relevant.

---

# 39. Spatial Context

Spatial Context МОЖЕТ включать:

- coordinates;
- location;
- region;
- altitude;
- environment;
- spatial reference system.

---

# 40. Spatial Context ≠ Scope

Example:

    Observation made in London

does not automatically imply:

    Claim Scope = London population

Location of Observation:

    ≠ applicability population automatically

---

# 41. Environmental Context

Environmental Context МОЖЕТ включать:

- temperature;
- humidity;
- pressure;
- salinity;
- light;
- radiation;
- soil;
- water properties.

Presence of condition:

    ≠ causal role automatically

---

# 42. Technical Context

Technical Context МОЖЕТ включать:

- hardware;
- software version;
- configuration;
- operating mode;
- calibration;
- tool;
- power conditions.

Knowledge established for Version V:

    ≠ automatically valid for V+1

---

# 43. Biological Context

Biological Context МОЖЕТ включать:

- species;
- population;
- life stage;
- physiological State;
- health State;
- biological environment.

Cross-population generalization requires support.

---

# 44. Social and cultural Context

Social/cultural Context МОЖЕТ влиять:

- practice;
- meaning;
- interpretation;
- institution;
- terminology;
- classification;
- norms.

Modern или external cultural semantics НЕ ДОЛЖЕН незаметно заменять contextual historical/local semantics.

---

# 45. Linguistic Context

Interpretation МОЖЕТ зависеть от:

- language;
- dialect;
- era;
- terminology;
- technical vocabulary;
- local usage.

Same string:

    ≠ same meaning across Contexts automatically

---

# 46. Legal Context

Legal knowledge МОЖЕТ зависеть от:

- jurisdiction;
- time;
- authority;
- legal regime;
- instrument version.

Rule valid in jurisdiction A:

    ≠ valid in jurisdiction B automatically

---

# 47. Institutional Context

Institutional knowledge МОЖЕТ зависеть от:

- organization;
- governance structure;
- procedure version;
- role structure;
- authority.

Current institutional Context НЕ ДОЛЖЕН незаметно заменять historical Context.

---

# 48. Experimental Context

Experiment Context МОЖЕТ включать:

- protocol;
- equipment;
- sample;
- controls;
- environment;
- operator;
- calibration;
- timing.

---

# 49. Observation Context

Observation Context МОЖЕТ включать:

- observer;
- viewpoint;
- instrument;
- environment;
- sampling method;
- timing.

Observation НЕ ДОЛЖЕН автоматически быть treated as context-independent phenomenon description.

---

# 50. Measurement Context

Measurement Context МОЖЕТ включать:

- instrument;
- calibration;
- method;
- unit;
- sample;
- time;
- environmental conditions;
- range.

Same numeric value under different Measurement Context:

    ≠ same Measurement semantics automatically

---

# 51. Model Context

Model output МОЖЕТ зависеть от:

- model version;
- parameters;
- assumptions;
- inputs;
- boundary conditions.

Model Context:

    ≠ real-world Context automatically

---

# 52. Procedure Context

Procedure МОЖЕТ быть applicable, effective или safe только в particular Context.

Examples:

- available tools;
- material type;
- environment;
- operator competence;
- resources;
- equipment.

---

# 53. Action Context

Action semantics МОЖЕТ зависеть от:

- Actor;
- target;
- authority;
- tool;
- environment;
- timing;
- constraints.

Same physical movement:

    ≠ same Action semantics universally

---

# 54. Event Context

Event Context МОЖЕТ включать:

- location;
- time;
- environmental State;
- institutional situation;
- surrounding conditions.

Event Context:

    ≠ Event identity automatically

---

# 55. Process Context

Process dynamics МОЖЕТ depend материально on Context.

Example:

    fermentation at 10°C
    ≠ fermentation at 35°C automatically

Process knowledge НЕ ДОЛЖЕН незаметно переносить across материально different Contexts.

---

# 56. State Context

State representation МОЖЕТ itself требовать Context/reference conditions.

Example:

    pressure = 100 kPa

may require knowing:

- system;
- location;
- reference semantics;
- measurement conditions.

State remains distinct from Context.

---

# 57. Result Context

Result semantics МОЖЕТ зависеть от:

- baseline;
- population;
- Procedure;
- Measurement;
- environment;
- time;
- Objective.

Result observed in Context X:

    ≠ expected Result in Context Y automatically

---

# 58. Relation Context

Relation МОЖЕТ hold только under Context.

Example:

    A reacts-with B
    above temperature T

Relation НЕ ДОЛЖЕН незаметно generalize beyond supported Context.

---

# 59. Identity Context

Identity judgment МОЖЕТ зависеть от factual Context.

Но Context ДОЛЖЕН оставаться различимым из:

- identity frame;
- identity criterion;
- Identity Scope;

as defined in `014-IDENTITY`.

---

# 60. Claim Context

Claim applicability МОЖЕТ зависеть от Context.

Example:

    "Water boils at 100°C"

requires pressure-related contextual qualification for precise technical use.

Simplified expression МОЖЕТ оставаться useful, Но материально relevant Context ДОЛЖЕН оставаться recoverable.

---

# 61. Generic Claim ≠ universal Claim

Generic wording:

    A does B

НЕ ДОЛЖЕН автоматически означать:

    A does B in every Context

Generic language МОЖЕТ conceal Context dependence.

---

# 62. Context-dependent correctness

Один Claim МОЖЕТ быть supported в Context X и unsupported, false или inapplicable в Context Y.

This does not automatically mean Sources contradict.

Context alignment СЛЕДУЕТ precede contradiction judgment.

---

# 63. Context mismatch and contradiction

Context mismatch МОЖЕТ explain an apparent contradiction.

But:

    Context mismatch
    ≠ contradiction resolved automatically

Especially где one Context is неизвестный, system ДОЛЖЕН сохранять uncertainty about whether Claims truly conflict.

---

# 64. Context alignment

Before comparing representations, материально relevant contextual dimensions СЛЕДУЕТ быть aligned.

Potential dimensions include:

- time;
- place;
- population;
- system version;
- method;
- jurisdiction;
- environment;
- terminology;
- equipment;
- protocol.

---

# 65. Context mismatch

A Context mismatch occurs when knowledge is compared or applied across materially different conditions without sufficient justification.

---

# 66. Context drift

**Context drift** — alteration, loss or substitution of materially relevant Context during storage, reasoning, translation, summary, inference or reuse such that knowledge appears to belong to a different Context than originally supported.

Examples:

    historical rule
    → current rule

    laboratory Result
    → universal field Result

    adult guidance
    → pediatric guidance

    software V1 behavior
    → software V3 behavior

---

# 67. Silent Context drift

Context drift is especially dangerous when contextual qualifiers disappear without leaving evidence that they existed.

Example:

    safe under controlled dry conditions

becoming:

    safe

This is a material semantic failure.

---

# 68. Context substitution

Context X НЕ ДОЛЖЕН незаметно быть replaced by Context Y.

Examples:

    modern law
    → historical law

    current taxonomy
    → historical taxonomy

    laboratory environment
    → field environment

---

# 69. Context inheritance

Context МОЖЕТ быть inherited из an enclosing structure such as:

- experiment;
- section;
- dataset;
- Procedure;
- Source segment;
- other container.

But inheritance is not automatic merely because nesting exists.

Inherited Context ДОЛЖЕН оставаться semantically compatible с target.

---

# 70. Compatibility-before-inheritance

Inherited Context НЕ ДОЛЖЕН быть applied где Это conflicts с more specific contextual information.

Unknown compatibility:

    ≠ compatibility

More specific Context МОЖЕТ:

- override;
- qualify;
- block;
- leave inherited dimension unresolved.

---

# 71. Dimension-level inheritance

Context inheritance МОЖЕТ occur dimension by dimension.

Example:

    parent:
    year = 1770
    region = Europe

    child:
    region = Japan

Один system МОЖЕТ сохранять:

    year = 1770

while overriding:

    region = Japan

only if remaining inherited dimensions are independently compatible.

Therefore:

    one overridden dimension
    ≠ all other dimensions automatically safe to inherit

---

# 72. Context inheritance states

где material, inherited contextual values МОЖЕТ need status such as:

- inherited;
- overridden;
- blocked;
- unresolved;
- explicitly restated.

Core does not require these as separate Entities.

---

# 73. Context portability

когда knowledge is extracted из an enclosing structure, inherited материально relevant Context ДОЛЖЕН travel с Это или оставаться resolvably referenced.

Otherwise extraction МОЖЕТ create Context loss.

---

# 74. Context composition

Context МОЖЕТ быть composed из multiple dimensions или Sources.

Но composition ДОЛЖЕН сохранять semantic compatibility.

---

# 75. Context composition ≠ co-occurrence

Context values supported separately do not automatically belong to one represented real-world Context occurrence.

Example:

    Source A:
    temperature = 20°C

    Source B:
    humidity = 80%

If Sources refer to different experiments, composing:

    20°C + 80% RH

creates a false Context.

Therefore:

    individually supported Context values
    ≠ supported co-occurring Context automatically

---

# 76. Cross-provenance Context composition

Context values из separate Sources/provenance НЕ ДОЛЖЕН быть merged into one Context представленный as obtaining если не their co-occurrence или shared target compatibility is independently justified.

Thus:

    provenance-preserving composition
    ≠ evidence of co-occurrence

---

# 77. Context conflict

Context Claims МОЖЕТ conflict.

Example:

    Source A:
    temperature 20°C

    Source B:
    temperature 25°C

System ДОЛЖЕН сохранять competing Context representations и provenance.

---

# 78. Context provenance

Context values СЛЕДУЕТ сохранять provenance когда материально relevant.

Reconstructed Context:

    ≠ observed Context

Measured Context:

    ≠ assumed Context

---

# 79. Observed Context

Context МОЖЕТ быть directly observed.

But:

    observed factor
    ≠ causal factor automatically

---

# 80. Measured Context

Context МОЖЕТ быть measured.

Measurement uncertainty/precision ДОЛЖЕН оставаться сохранённым.

---

# 81. Reported Context

Source МОЖЕТ report Context без direct Measurement available.

Reported:

    ≠ independently verified automatically

---

# 82. Inferred Context

Context МОЖЕТ быть inferred.

Inference basis и uncertainty ДОЛЖЕН оставаться разрешимым где material.

---

# 83. Reconstructed historical Context

Historical Context МОЖЕТ быть reconstructed из:

- Sources;
- artifacts;
- environmental proxies;
- maps;
- Models;
- institutional records.

Reconstructed:

    ≠ directly observed

---

# 84. Later Context reconstruction ≠ original Source assertion

Later reconstruction из historical Context НЕ ДОЛЖЕН быть представлен как though original Source stated или knew that Context.

Example:

    original Source:
    temperature unknown

    later reconstruction:
    temperature ≈ 8°C

Both ДОЛЖЕН оставаться различимым.

---

# 85. Modeled Context

Model МОЖЕТ estimate contextual conditions.

Modeled Context:

    ≠ historical/observed Context automatically

---

# 86. Default Context

Systems МОЖЕТ определять defaults.

But:

    default Context
    ≠ Context represented as obtaining automatically

Defaults are convenience/policy semantics unless established otherwise.

---

# 87. Assumed Context

Assumed Context ДОЛЖЕН оставаться различимым из известный, reported, observed или measured Context.

---

# 88. Context uncertainty

Uncertainty МОЖЕТ concern:

- presence of factor;
- value;
- duration;
- temporal interval;
- spatial extent;
- relevance;
- provenance;
- compatibility;
- transferability.

Core does not require universal confidence metric.

---

# 89. Context relevance

Not every surrounding condition is materially relevant.

Один factor МОЖЕТ быть:

- materially relevant;
- probably relevant;
- possibly relevant;
- known irrelevant;
- relevance unknown.

Один condition whose material relevance remains uncertain МОЖЕТ still быть представлен как Context когда preserving that possibility matters.

But:

    factor present
    ≠ materially relevant automatically

and:

    represented as Context
    ≠ material relevance proven

---

# 90. Material relevance

Context distinction is material when omission/change may significantly alter:

- meaning;
- applicability;
- comparison;
- safety;
- interpretation;
- expected Result;
- identity resolution;
- causal reasoning;
- Decision.

где material relevance itself is uncertain, that uncertainty СЛЕДУЕТ оставаться representable.

---

# 91. Context minimality

Representation СЛЕДУЕТ сохранять enough Context to prevent material semantic error.

It need not describe all circumstances.

---

# 92. Context refinement

Later knowledge МОЖЕТ reveal previously omitted contextual factors.

System ДОЛЖЕН permit Context refinement без rewriting original Source semantics.

---

# 93. Context correction

Later Evidence МОЖЕТ correct представленный Context.

Correction СЛЕДУЕТ сохранять материально relevant:

- prior representation;
- new representation;
- reason;
- provenance;
- uncertainty.

---

# 94. Context versioning

Need distinguish:

    represented real-world Context changed
    ≠ Context representation changed
    ≠ new Evidence about past Context
    ≠ Context model changed

---

# 95. Context temporal validity

Context conditions МОЖЕТ иметь validity intervals.

Example:

    software version V
    active during T1–T2

Temporal validity СЛЕДУЕТ оставаться разрешимым где material.

---

# 96. Context snapshot ≠ interval

Context observed at T:

    ≠ stable Context throughout interval automatically

Example:

    one temperature Measurement
    ≠ all-day constant temperature

---

# 97. Context continuity

Observation gap:

    ≠ Context remained unchanged
    ≠ Context changed

without justified Inference.

---

# 98. Context transition

Context change МОЖЕТ быть представлен through:

- State change;
- Event;
- Process;
- Measurement sequence;
- other structures.

But:

    Context transition
    ≠ Event automatically

---

# 99. Context comparison

Context comparison СЛЕДУЕТ сохранять когда material:

- dimensions;
- definitions;
- units;
- temporal frame;
- spatial frame;
- uncertainty;
- epistemic status.

---

# 100. Context similarity

Similar Contexts:

    ≠ identical Contexts

Similarity alone does not establish knowledge transfer.

---

# 101. Context equivalence

Contexts МОЖЕТ быть considered equivalent for Один определённый purpose.

But:

    equivalent-for-purpose-P
    ≠ unrestricted Context identity

---

# 102. Context compatibility

Context compatibility МОЖЕТ быть:

- full;
- partial;
- conditional;
- dimension-specific;
- uncertain;
- unknown;
- incompatible.

Compatibility:

    ≠ Context identity

and:

    Context compatibility
    ≠ Claim applicability

Two Contexts МОЖЕТ быть compatible for Один particular comparison, mapping или operation без establishing that Один Claim допустимый в one applies в Этот other.

---

# 103. Transferability

Knowledge переносить из Context X to Context Y МОЖЕТ быть:

- fully supported;
- partially supported;
- conditionally supported;
- dimension-specific;
- uncertain;
- unknown;
- unsupported.

Transferability НЕ СЛЕДУЕТ быть forced into Один universal binary yes/no model.

---

# 104. Partial Context match

If Context X and Context Y match on some dimensions but differ or are unknown on others:

    ≠ identical Contexts
    ≠ incompatible Contexts automatically

Transferability МОЖЕТ оставаться partial или unresolved.

---

# 105. Context transfer

Transfer across materially different Contexts requires justification.

Transfer МОЖЕТ rely on:

- Evidence;
- Inference;
- Model;
- established invariance;
- validated domain rule;
- Profile.

---

# 106. No automatic transfer

Fundamental rule:

    valid in Context X
    ≠ valid in Context Y automatically

---

# 107. Missing Context and transfer

When materially relevant Context is unknown:

    transferability МОЖЕТ быть неизвестный

Но knowledge НЕ ДОЛЖЕН быть автоматически declared either:

- universally transferable;
- universally invalid.

---

# 108. Context generalization

Multiple observations across Contexts:

    ≠ universal context-independent rule automatically

Generalization requires epistemic support.

---

# 109. Context invariance

Knowledge МОЖЕТ быть shown invariant across Один определённый range из Contexts.

But:

    invariant across tested Contexts
    ≠ invariant across all possible Contexts

---

# 110. Context-specific exceptions

System ДОЛЖЕН permit:

    general Claim

plus:

    Context-specific exception

without automatically forcing global contradiction.

---

# 111. Exception ≠ total falsification automatically

Один contextual exception МОЖЕТ narrow Scope/applicability rather than falsify every form из Один broader Claim.

---

# 112. Context transfer laundering safeguard

Chains involving:

- Context similarity;
- partial compatibility;
- purpose-qualified equivalence;
- inferred transferability;
- mapping;

НЕ ДОЛЖЕН быть compressed into unrestricted applicability.

Example:

    Context A similar B
    B equivalent-for-P C

does not establish:

    Claim valid in A
    → Claim valid in C universally

Thus:

    contextual relation chain
    ≠ unrestricted transferability

---

# 113. Boundary conditions

Boundary conditions МОЖЕТ быть материально important for Models, Processes и Procedures.

Boundary conditions:

    ≠ full Context

Но материально relevant boundary conditions ДОЛЖЕН оставаться сохраняемым.

---

# 114. Operating envelope

Technical knowledge МОЖЕТ apply только inside Один определённый operating envelope.

Example:

    temperature 0–40°C
    pressure ≤ P

Outside envelope:

    behavior unknown
    ≠ known failure
    ≠ known safety

unless independently established.

---

# 115. Safety Context

Procedure, Action или system МОЖЕТ быть safe только under определённый Context.

Thus:

    safe in Context X
    ≠ safe universally

---

# 116. Safety-critical Context completeness

All материально safety-critical Context dimensions required for Один safety judgment ДОЛЖЕН survive:

- reuse;
- translation;
- summary;
- compression;
- export;
- offline rendering.

Example:

    outdoors
    concentration < X
    PPE Y
    duration < 10 min

НЕ ДОЛЖЕН быть reduced to только:

    outdoors

if omitted dimensions materially determine safety.

Partial preservation из safety Context МОЖЕТ constitute material Context loss.

---

# 117. Risk Context

Risk МОЖЕТ зависеть от:

- concentration;
- duration;
- route;
- population;
- environment;
- equipment;
- protective measures.

Removing эти conditions МОЖЕТ материально distort risk representation.

---

# 118. Decision Context

Decision СЛЕДУЕТ сохранять материально relevant Context available или used at Decision time.

Later Context knowledge:

    ≠ historical Decision Context automatically

---

# 119. Context and Decision Basis

Context later reconstructed ДОЛЖЕН оставаться различимым из Context actually available to Decision at T1.

---

# 120. Historical Context preservation

Historical knowledge НЕ ДОЛЖЕН незаметно inherit:

- current law;
- current taxonomy;
- current borders;
- current technology;
- present terminology;
- current institutions;
- modern social categories;
- present environmental conditions.

---

# 121. Presentism safeguard

Projection of current Context/categories into historical representation without justification is a contextual semantic failure.

---

# 122. Future-context extrapolation

Knowledge valid today:

    ≠ guaranteed valid in future system/version/institutional Context

---

# 123. Cross-cultural transfer

Cultural/social knowledge НЕ ДОЛЖЕН автоматически generalize across cultural Contexts.

---

# 124. Cross-jurisdiction transfer

Legal/institutional knowledge НЕ ДОЛЖЕН автоматически переносить across jurisdictions.

---

# 125. Cross-version transfer

Technical/software knowledge established under Version A:

    ≠ Version B automatically

---

# 126. Cross-population transfer

Biological/medical/social knowledge from Population A:

    ≠ Population B automatically

Context и Scope ДОЛЖЕН both оставаться considered.

---

# 127. Laboratory-to-field transfer

Laboratory finding:

    ≠ field behavior automatically

Context differences ДОЛЖЕН оставаться явным.

---

# 128. Sample-to-environment transfer

Sample conditions:

    ≠ source-environment conditions automatically

---

# 129. Context and Identity

Identity judgment valid in one Context/frame:

    ≠ unrestricted identity judgment

`015` ДОЛЖЕН сохранять compatibility с `014-IDENTITY`.

---

# 130. Context and Relation

Relation established in Context X:

    ≠ universal Relation

Compatibility с `013-RELATION` ДОЛЖЕН оставаться сохранённым.

---

# 131. Context and Process

Process behavior in Context X:

    ≠ same Process dynamics in Y automatically

Compatibility с `012-PROCESS` ДОЛЖЕН оставаться сохранённым.

---

# 132. Context and State

State и Context МОЖЕТ share factual conditions Но ДОЛЖЕН оставаться semantically distinguishable.

Compatibility с `011-STATE` ДОЛЖЕН оставаться сохранённым.

---

# 133. Context and Result

Result interpretation ДОЛЖЕН сохранять материально relevant Context.

Compatibility с `010-RESULT` ДОЛЖЕН оставаться сохранённым.

---

# 134. Context and Event

Events occurring in same Context:

    ≠ same Event
    ≠ causally linked automatically

Compatibility с `009-EVENT` ДОЛЖЕН оставаться сохранённым.

---

# 135. Context and Action

Action interpretation, Effect и safety МОЖЕТ зависеть от Context.

Compatibility с `008-ACTION` ДОЛЖЕН оставаться сохранённым.

---

# 136. Context and Claim

Claim МОЖЕТ:

- explicitly include Context;
- inherit Context;
- reference Context;
- have component-specific Context.

Removing Context НЕ ДОЛЖЕН universalize Claim.

---

# 137. Source production Context

Source itself has a production/publication Context.

But:

    Source production Context
    ≠ represented Context automatically

---

# 138. Source Context ≠ represented Context

Один modern Source МОЖЕТ describe an ancient Event.

Therefore:

    Source produced in 2026
    ≠ Event Context = 2026

Это distinction ДОЛЖЕН оставаться явным где material.

---

# 139. Context and Evidence

Evidence МОЖЕТ поддерживать Context Claims.

Context itself ДОЛЖЕН оставаться различимым из Evidence.

---

# 140. Context and Assumption

Assumed contextual values НЕ ДОЛЖЕН незаметно становиться observed или historical factual Context.

---

# 141. Context and Model

Model may impose contextual/boundary assumptions.

Model Context ДОЛЖЕН оставаться различимым из real-world Context.

---

# 142. Context and Profile

Profile МОЖЕТ определять:

- required contextual dimensions;
- required precision;
- required safety conditions;
- allowed defaults;
- transfer rules.

But:

    Profile
    ≠ Context

---

# 143. Context Record identity

Two Context Records МОЖЕТ describe one contextual situation.

But:

    same represented contextual situation
    ≠ same Context Record

Identity remains governed by `014`.

---

# 144. Context Record ≠ represented contextual situation

A Context Record represents contextual conditions.

It is not the real-world Context itself.

Thus:

    Context Record
    ≠ represented contextual situation
    ≠ complete real-world Context

---

# 145. Higher-order Context reference

Higher-order statements ДОЛЖЕН сохранять whether they refer to:

- Context Record;
- contextual condition;
- Claim about Context;
- inferred Context;
- modeled Context;
- reconstructed Context.

---

# 146. Context negation and absence

Need distinguish:

    contextual factor absent
    ≠ factor unknown
    ≠ factor unrecorded
    ≠ factor irrelevant

Example:

    oxygen absent

is different from:

    oxygen unknown

---

# 147. Known absence

Defined absence из contextual factor МОЖЕТ itself быть material Context.

Example:

    anaerobic condition:
    oxygen absent

But:

    oxygen not recorded
    ≠ oxygen absent

---

# 148. Relevance unknown

Factor МОЖЕТ быть известным to exist пока its relevance remains неизвестный.

Thus:

    factor present
    ≠ material relevance established

Potential material relevance МОЖЕТ itself justify preservation когда losing Этот factor could материально distort later interpretation.

---

# 149. Context hierarchy

Contexts МОЖЕТ быть nested:

    global Context
      → experiment Context
        → run Context
          → Measurement Context

Nested representation МОЖЕТ inherit, override или block contextual values.

---

# 150. Context precedence

Если inherited/contextual values conflict, system НЕ ДОЛЖЕН arbitrarily choose one если не Один допустимый precedence rule exists.

More-specific location в hierarchy alone МОЖЕТ быть relevant, Но semantic compatibility still matters.

---

# 151. Context inheritance provenance

Inherited Context СЛЕДУЕТ оставаться traceable to Source/enclosing structure где материально relevant.

---

# 152. Context reuse

Reusable Context Records МОЖЕТ reduce duplication.

Но reuse НЕ ДОЛЖЕН означать that multiple real-world occurrences had perfectly identical conditions если не установленный.

---

# 153. Template Context ≠ Context represented as obtaining

Один Procedure или system template МОЖЕТ определять expected Context.

But:

    expected Context
    ≠ Context represented as obtaining

---

# 154. Nominal Context ≠ Context represented as obtaining

Need distinguish:

- nominal;
- default;
- assumed;
- measured;
- observed;
- reported;
- inferred;
- Context represented as obtaining where established.

---

# 155. Context normalization

External contextual descriptions МОЖЕТ быть normalized.

Но normalization НЕ ДОЛЖЕН придумывать precision.

Example:

    room temperature
    ≠ exactly 20°C automatically

---

# 156. Unit conversion

Unit conversion МОЖЕТ сохранять value semantics.

But:

    conversion
    ≠ increased precision

Example:

    approximately 20°C

converted to Fahrenheit ДОЛЖЕН оставаться approximate.

---

# 157. Context translation fidelity

Translation ДОЛЖЕН сохранять материально relevant:

- conditions;
- negation;
- modality;
- ranges;
- uncertainty;
- qualifiers;
- epistemic status.

---

# 158. Context summary fidelity

Summary НЕ ДОЛЖЕН convert:

    tested under Context X
    → universally valid

    assumed Context
    → observed Context

    reconstructed Context
    → historical certainty

    Context unknown
    → default Context

    contextual factor
    → causal factor

    similar/compatible Context
    → applicable or transferable Context automatically

    partial safety Context
    → complete safety Context

---

# 159. Context compression

Compression МОЖЕТ omit non-material Context.

Но НЕ ДОЛЖЕН erase материально relevant:

- applicability conditions;
- safety conditions;
- operating envelope;
- temporal validity;
- uncertainty;
- epistemic status;
- system version;
- jurisdiction;
- population;
- historical distinctions.

---

# 160. Context Fidelity

**Context Fidelity** — degree to which representation preserves materially relevant contextual semantics through:

- storage;
- transfer;
- translation;
- summarization;
- inference;
- reuse;
- offline presentation.

High Context Fidelity does not require exhaustive metadata.

It requires enough contextual information to prevent material semantic distortion.

Crucially:

    high Context Fidelity
    ≠ preserved Context is factually true

Один Source МОЖЕТ report an incorrect Context с high representational fidelity.

Therefore:

    fidelity
    ≠ truth

Context Fidelity evaluates preservation of contextual semantics, not factual correctness of those semantics.

---

# 161. Context loss

Context loss occurs when materially relevant contextual information disappears.

Это МОЖЕТ produce:

- false universalization;
- false contradiction;
- unsafe Procedure;
- invalid comparison;
- incorrect identity resolution;
- incorrect transfer;
- false causal reasoning.

---

# 162. Context contamination

Context contamination occurs when Context from one target is incorrectly attached to another.

Example:

    Experiment A Context
    → Result B

without justification.

---

# 163. Context conflation

Context conflation occurs when distinct Contexts are merged as one without sufficient support.

---

# 164. Context leakage

Context leakage occurs when assumptions/conditions from one reasoning chain silently influence another representation.

---

# 165. Context hallucination

Context hallucination occurs when missing contextual information is invented.

Fundamental preference:

    unknown Context
    > plausible unsupported Context

---

# 166. Context overgeneralization

Knowledge supported under restricted Context НЕ ДОЛЖЕН быть представлен как unrestricted без justified generalization.

---

# 167. Context under-specification

Under-specification occurs when materially relevant Context dimensions are omitted.

---

# 168. Context over-specification

Over-specification occurs when unsupported contextual details are asserted.

---

# 169. Historical Context reconstruction fidelity

Historical reconstruction ДОЛЖЕН сохранять distinctions among:

- known;
- reported;
- inferred;
- reconstructed;
- assumed;
- modeled;
- disputed.

---

# 170. Damaged archives

If Source says:

    "the mixture was heated"

but omits:

- temperature;
- pressure;
- duration;
- vessel;

эти НЕ ДОЛЖЕН быть придуманный.

---

# 171. Offline preservation

Context СЛЕДУЕТ оставаться interpretable без live online dependencies.

Where material preserve:

- values;
- units;
- definitions;
- time;
- place;
- version;
- jurisdiction;
- provenance;
- uncertainty;
- epistemic status.

---

# 172. Offline Context references

Context references НЕ СЛЕДУЕТ depend solely on mutable online IDs.

Human-readable meaning СЛЕДУЕТ оставаться reconstructable offline где feasible.

---

# 173. Carrier neutrality

Context semantics does not depend on:

- graph;
- JSON;
- RDF;
- SQL;
- Markdown;
- PDF;
- printed text.

Carrier does not determine Context semantics.

---

# 174. High-risk Profiles

High-risk Profiles МОЖЕТ требовать stricter Context preservation.

Examples:

- medicine;
- chemistry;
- engineering;
- food safety;
- hazardous materials;
- survival procedures;
- electrical systems.

Profile МОЖЕТ требовать:

- temperature;
- pressure;
- concentration;
- duration;
- population;
- equipment;
- version;
- PPE;
- safety thresholds;
- transfer limits;
- uncertainty.

---

# 175. Conformance ≠ truth

Need distinguish:

    Context structural conformance
    ≠ Context truth
    ≠ Context completeness
    ≠ universal applicability
    ≠ transferability
    ≠ causality
    ≠ safety
    ≠ Context Fidelity proof of truth

Validator PASS does not establish these.

---

# 176. Machine validation

Validator МОЖЕТ check:

- required Profile Context fields;
- units;
- ranges;
- version presence;
- temporal consistency;
- inheritance conflicts;
- target presence;
- invalid Context combinations;
- known incompatibilities.

But:

    validator PASS
    ≠ factual Context truth
    ≠ valid transfer
    ≠ Claim applicability
    ≠ universal applicability

Validator has no Context-truth privilege.

---

# 177. Diagnostic families

## 177.1. Context/State collapse

Examples:

- State variable → Context only;
- Context variable → subject State automatically.

## 177.2. Context/Scope collapse

Examples:

- observation population → applicability Context only;
- hospital Context → hospital population Scope automatically.

## 177.3. Context/frame collapse

Examples:

- France 1804 → French legal frame automatically;
- Context location → ontology selection automatically.

## 177.4. Context/Participant collapse

Examples:

- ambient factor → Process Participant automatically.

## 177.5. Context/Cause collapse

Examples:

- factor present → caused phenomenon.

## 177.6. Context/Evidence collapse

Examples:

- Context value → Evidence itself.

## 177.7. Context/Assumption collapse

Examples:

- assumed condition → observed condition.

## 177.8. Context/Profile collapse

Examples:

- medical Profile → patient Context.

## 177.9. Unknown-context failure

Examples:

- missing Context → universal applicability;
- missing Context → automatic invalidity.

## 177.10. Temporal Context drift

Examples:

- historical Context → present Context.

## 177.11. Version drift

Examples:

- V1 Context → V3 Context.

## 177.12. Population drift

Examples:

- Population A → Population B.

## 177.13. Jurisdiction drift

Examples:

- Law Context A → jurisdiction B.

## 177.14. Inheritance failure

Examples:

- incompatible parent Context inherited;
- overridden dimension ignored;
- unknown compatibility treated as compatible.

## 177.15. Composition failure

Examples:

- Context values from different experiments merged;
- provenance mistaken for co-occurrence.

## 177.16. Transfer failure

Examples:

- similar Context → full transferability;
- compatible Context → Claim applicability;
- partial compatibility → universal applicability.

## 177.17. Safety Context loss

Examples:

- one safety qualifier retained while critical others removed.

## 177.18. Context laundering

Examples:

- similarity + equivalence chain → unrestricted applicability.

## 177.19. Context hallucination

Examples:

- missing historical temperature → plausible invented value.

## 177.20. Semantic garbage-bin failure

Examples:

- Cause stored only as Context;
- Evidence stored only as Context;
- State stored only as Context despite material role distinction.

Diagnostic label does not establish:

- intent;
- fraud;
- negligence;
- responsibility.

---

# 178. Межстандартная совместимость

`015-CONTEXT` ДОЛЖЕН сохранять boundaries установленный by:

- `008-ACTION`;
- `009-EVENT`;
- `010-RESULT`;
- `011-STATE`;
- `012-PROCESS`;
- `013-RELATION`;
- `014-IDENTITY`.

In compact form:

    Context
    → materially relevant or potentially
      materially relevant conditions
      relative to target

    State
    → condition/configuration
      of subject in applicable frame

    Scope
    → domain subset
      to which representation applies

    Frame
    → semantic/reference system
      within which representation interprets

    Assumption
    → proposition/condition adopted
      for reasoning/modeling

    Evidence
    → support for a knowledge representation

    Provenance
    → origin/history of representation

Therefore:

    Context
    ≠ State

    Context
    ≠ Scope

    Context
    ≠ Frame universally

    Context
    ≠ Assumption

    Context
    ≠ Evidence

    Context
    ≠ Provenance

    Context
    ≠ Cause

    Context
    ≠ Participant automatically

Этот same factual information МОЖЕТ участвовать в several semantic roles, Но those roles НЕ ДОЛЖЕН схлопываться где their distinctions материально matter.

---

# 179. Boundary concepts outside full 015 ontology

`015` uses but does not fully define:

- Scope;
- frame;
- State;
- Profile;
- Assumption;
- Preconditions;
- Evidence;
- Provenance;
- Observation;
- Measurement;
- Model;
- Procedure;
- Decision;
- Risk;
- Safety;
- Transferability.

Their complete semantics belong to existing or future standards.

---

# 180. Тест на разрастание сущностей

`015` DOES NOT require introducing the following as fundamental Core Entities:

- Context;
- ContextType;
- ContextDimension;
- ContextValue;
- ContextTarget;
- ContextFrame;
- ContextScope;
- ContextCondition;
- EnvironmentalContext;
- HistoricalContext;
- LegalContext;
- TechnicalContext;
- BiologicalContext;
- ExperimentalContext;
- MeasurementContext;
- ContextConflict;
- ContextVersion;
- ContextInheritance;
- ContextOverride;
- ContextConfidence;
- ContextCompatibility;
- ContextTransfer;
- ContextDrift;
- ContextFidelity;
- ContextEpistemicStatus.

эти МОЖЕТ быть представлен through:

- Records;
- Relations;
- States;
- Claims;
- Measurements;
- temporal/spatial structures;
- Profiles;
- Models;
- provenance;
- existing generic infrastructure.

Absence of separate Core Entity does not imply absence of semantics.

---

# 181. Core invariants

### CTX-01
Context represents conditions considered materially relevant or potentially materially relevant relative to a contextualized target.

### CTX-02
Recorded Context НЕ ДОЛЖЕН автоматически быть treated as полный real-world Context.

### CTX-03
Context semantics НЕ ДОЛЖЕН требовать Один dedicated fundamental Context Entity.

### CTX-04
Context target ДОЛЖЕН оставаться разрешимым где target ambiguity материально affects meaning.

### CTX-05
Context МОЖЕТ target an entire representation или Один определённый semantic component.

### CTX-06
Context ДОЛЖЕН оставаться различимым из contextualized object.

### CTX-07
Context ДОЛЖЕН оставаться различимым из State.

### CTX-08
Этот same factual condition МОЖЕТ участвовать в State и Context semantics без making them identical.

### CTX-09
Context need not be external to contextualized system.

### CTX-10
Context НЕ ДОЛЖЕН автоматически быть treated as Participant.

### CTX-11
Context ДОЛЖЕН оставаться различимым из Scope.

### CTX-12
Один condition МОЖЕТ play Context и Scope roles simultaneously, Но roles ДОЛЖЕН оставаться различимым когда material.

### CTX-13
Context ДОЛЖЕН оставаться различимым из semantic/reference frame.

### CTX-14
Context НЕ ДОЛЖЕН автоматически определять semantic/reference frame.

### CTX-15
Context ДОЛЖЕН оставаться различимым из Profile.

### CTX-16
Context ДОЛЖЕН оставаться различимым из Assumption.

### CTX-17
Context values ДОЛЖЕН сохранять материально relevant epistemic status.

### CTX-18
Observed, measured, reported, предполагаемым, inferred, modeled и reconstructed Context НЕ ДОЛЖЕН незаметно схлопываться когда reused или summarized.

### CTX-19
Context ДОЛЖЕН оставаться различимым из Preconditions.

### CTX-20
Contextual factor НЕ ДОЛЖЕН автоматически быть treated as causal factor.

### CTX-21
Contextual relevance НЕ ДОЛЖЕН автоматически означать causality.

### CTX-22
Context ДОЛЖЕН оставаться различимым из Evidence.

### CTX-23
Context ДОЛЖЕН оставаться различимым из Provenance.

### CTX-24
Storage metadata НЕ ДОЛЖЕН автоматически становиться domain Context.

### CTX-25
Один fact НЕ ДОЛЖЕН быть classified merely as Context когда Один more specific semantic role is материально relevant.

### CTX-26
Context МОЖЕТ быть incomplete; missing values НЕ ДОЛЖЕН быть придуманный.

### CTX-27
неизвестный/missing Context НЕ ДОЛЖЕН автоматически означать universal applicability.

### CTX-28
неизвестный/missing Context НЕ ДОЛЖЕН автоматически означать invalidity или uselessness.

### CTX-29
Context independence ДОЛЖЕН требовать positive поддерживать когда material.

### CTX-30
Context dimensions НЕ ДОЛЖЕН быть forced into Один universal fixed list.

### CTX-31
Context decomposition НЕ ДОЛЖЕН означать independence among dimensions.

### CTX-32
Context dimensions МОЖЕТ carry dependencies и joint constraints.

### CTX-33
Context values ДОЛЖЕН сохранять материально relevant units, definitions, uncertainty и precision.

### CTX-34
Phenomenon time ДОЛЖЕН оставаться различимым из Observation, Measurement, Source и Record times.

### CTX-35
Spatial Context ДОЛЖЕН оставаться различимым из Scope.

### CTX-36
Technical/version Context НЕ ДОЛЖЕН незаметно generalize across versions.

### CTX-37
Biological Context НЕ ДОЛЖЕН незаметно generalize across populations или life stages где material.

### CTX-38
Cultural/linguistic Context НЕ ДОЛЖЕН незаметно inherit foreign/current semantics.

### CTX-39
Legal Context ДОЛЖЕН сохранять jurisdiction и temporal regime где material.

### CTX-40
Experimental/Measurement Context ДОЛЖЕН сохранять материально relevant protocol/method conditions.

### CTX-41
Model Context НЕ ДОЛЖЕН незаметно становиться real-world Context.

### CTX-42
Procedure/Action safety или Effect в Context X НЕ ДОЛЖЕН автоматически generalize to Context Y.

### CTX-43
Process dynamics в Context X НЕ ДОЛЖЕН автоматически generalize to Context Y.

### CTX-44
Result observed в Context X НЕ ДОЛЖЕН автоматически устанавливать Result expectation в Context Y.

### CTX-45
Relation holding в Context X НЕ ДОЛЖЕН автоматически generalize beyond X.

### CTX-46
Generic Claim НЕ ДОЛЖЕН автоматически быть interpreted as universal across Contexts.

### CTX-47
Context alignment СЛЕДУЕТ precede contradiction judgment где material.

### CTX-48
Context mismatch МОЖЕТ explain apparent contradiction Но НЕ ДОЛЖЕН автоматически resolve Это.

### CTX-49
Context drift НЕ ДОЛЖЕН незаметно alter knowledge applicability.

### CTX-50
Context substitution НЕ ДОЛЖЕН occur без explicit justified semantics.

### CTX-51
Context inheritance НЕ ДОЛЖЕН быть предполагаемым merely из structural nesting.

### CTX-52
Inherited Context НЕ ДОЛЖЕН быть applied across известный incompatible conditions.

### CTX-53
неизвестный Context compatibility НЕ ДОЛЖЕН быть treated as compatibility.

### CTX-54
More-specific Context МОЖЕТ override, qualify или block inherited Context.

### CTX-55
Context inheritance МОЖЕТ быть dimension-specific.

### CTX-56
Inherited dimensions НЕ ДОЛЖЕН автоматически быть предполагаемым compatible merely because another dimension was validly inherited.

### CTX-57
Material inherited Context ДОЛЖЕН оставаться portable с extracted/reused knowledge.

### CTX-58
Context values из separate provenance НЕ ДОЛЖЕН быть composed into one Context представленный as obtaining без justified co-occurrence/compatibility.

### CTX-59
Provenance-preserving Context composition НЕ ДОЛЖЕН быть mistaken for evidence из co-occurrence.

### CTX-60
Conflicting Context representations ДОЛЖЕН оставаться representable с provenance.

### CTX-61
Default Context НЕ ДОЛЖЕН автоматически быть treated as Context представленный as obtaining.

### CTX-62
Template/nominal Context НЕ ДОЛЖЕН автоматически быть treated as Context представленный as obtaining.

### CTX-63
Context uncertainty ДОЛЖЕН оставаться representable.

### CTX-64
Context inclusion НЕ ДОЛЖЕН автоматически устанавливать material relevance.

### CTX-65
Potentially материально relevant Context МОЖЕТ оставаться представленный пока its relevance remains uncertain.

### CTX-66
Representation СЛЕДУЕТ сохранять материально relevant Context без requiring exhaustive reality description.

### CTX-67
Later Context refinement НЕ ДОЛЖЕН переписывать original Source semantics.

### CTX-68
Later Context reconstruction НЕ ДОЛЖЕН быть представлен как original Source Context assertion.

### CTX-69
Context representation revision НЕ ДОЛЖЕН автоматически означать представленный real-world Context changed.

### CTX-70
Context temporal validity ДОЛЖЕН оставаться разрешимым когда material.

### CTX-71
Context snapshot НЕ ДОЛЖЕН автоматически expand to interval constancy.

### CTX-72
Observation gaps НЕ ДОЛЖЕН устанавливать Context continuity или change автоматически.

### CTX-73
Context transition НЕ ДОЛЖЕН автоматически быть modeled as Event.

### CTX-74
Context similarity НЕ ДОЛЖЕН автоматически означать Context identity.

### CTX-75
Context equivalence ДОЛЖЕН оставаться purpose-qualified.

### CTX-76
Context compatibility МОЖЕТ быть partial, conditional, dimension-specific, uncertain или неизвестный.

### CTX-77
Context compatibility НЕ ДОЛЖЕН автоматически устанавливать Claim applicability.

### CTX-78
Transferability МОЖЕТ быть partial, conditional, dimension-specific, uncertain или неизвестный.

### CTX-79
Knowledge переносить across материально different Contexts ДОЛЖЕН требовать justified переносить semantics.

### CTX-80
Validity в Context X НЕ ДОЛЖЕН автоматически означать validity в Context Y.

### CTX-81
Missing Context НЕ ДОЛЖЕН автоматически определять either transferability или non-transferability.

### CTX-82
Multiple Context-specific observations НЕ ДОЛЖЕН автоматически устанавливать universal Context independence.

### CTX-83
Invariance across tested Contexts НЕ ДОЛЖЕН автоматически означать invariance across all Contexts.

### CTX-84
Context-specific exceptions ДОЛЖЕН оставаться representable без forced universal contradiction.

### CTX-85
Chains из Context similarity, compatibility, equivalence или переносить НЕ ДОЛЖЕН быть laundered into unrestricted applicability.

### CTX-86
Boundary conditions и operating envelopes ДОЛЖЕН оставаться сохраняемым где материально relevant.

### CTX-87
неизвестный behavior outside an operating envelope НЕ ДОЛЖЕН автоматически становиться известный failure или известный safety.

### CTX-88
All материально safety-critical Context dimensions required for Один safety judgment ДОЛЖЕН survive reuse, translation, summarization и compression.

### CTX-89
Partial preservation из safety-critical Context МОЖЕТ constitute material Context loss.

### CTX-90
Decision Context ДОЛЖЕН reflect материально relevant information/conditions available at Decision time.

### CTX-91
Later Context knowledge НЕ ДОЛЖЕН быть inserted retroactively into historical Decision Basis.

### CTX-92
Historical knowledge НЕ ДОЛЖЕН незаметно inherit current Context.

### CTX-93
Present-day categories НЕ ДОЛЖЕН автоматически быть projected backward into historical Context.

### CTX-94
Current knowledge НЕ ДОЛЖЕН автоматически generalize into future system/version Context.

### CTX-95
Cross-cultural, cross-jurisdiction, cross-version и cross-population переносить НЕ ДОЛЖЕН быть предполагаемым автоматически.

### CTX-96
Laboratory Context НЕ ДОЛЖЕН автоматически становиться field Context.

### CTX-97
Source production Context ДОЛЖЕН оставаться различимым из Context представленный by Source.

### CTX-98
Context и Identity semantics ДОЛЖЕН оставаться compatible с `014`.

### CTX-99
Context и Relation semantics ДОЛЖЕН оставаться compatible с `013`.

### CTX-100
Context и Process semantics ДОЛЖЕН оставаться compatible с `012`.

### CTX-101
Context и State semantics ДОЛЖЕН оставаться compatible с `011`.

### CTX-102
Context и Result semantics ДОЛЖЕН оставаться compatible с `010`.

### CTX-103
Context и Event semantics ДОЛЖЕН оставаться compatible с `009`.

### CTX-104
Context и Action semantics ДОЛЖЕН оставаться compatible с `008`.

### CTX-105
Context Record identity ДОЛЖЕН оставаться различимым из представленный contextual situation.

### CTX-106
Context absence, неизвестный Context, unrecorded Context и irrelevance ДОЛЖЕН оставаться различимым.

### CTX-107
Context hierarchy/inheritance НЕ ДОЛЖЕН resolve conflicting values без определённый semantics.

### CTX-108
Context normalization НЕ ДОЛЖЕН придумывать precision.

### CTX-109
Unit conversion ДОЛЖЕН сохранять original uncertainty/precision.

### CTX-110
Translation ДОЛЖЕН сохранять материально relevant Context qualifiers, uncertainty и epistemic status.

### CTX-111
Summary НЕ ДОЛЖЕН convert context-limited knowledge into universal knowledge.

### CTX-112
Context compression ДОЛЖЕН сохранять материально relevant applicability и safety conditions.

### CTX-113
Context loss, contamination, conflation, leakage, hallucination и overgeneralization ДОЛЖЕН оставаться detectable semantic failure classes.

### CTX-114
неизвестный Context ДОЛЖЕН быть preferred over plausible unsupported Context fabrication.

### CTX-115
Historical Context reconstruction ДОЛЖЕН distinguish известный, reported, inferred, reconstructed, предполагаемым, modeled и disputed semantics.

### CTX-116
Damaged Sources НЕ ДОЛЖЕН быть completed с придуманный Context.

### CTX-117
Offline representation СЛЕДУЕТ сохранять enough Context for durable human interpretation.

### CTX-118
Carrier technology НЕ ДОЛЖЕН определять Context semantics.

### CTX-119
Profile МОЖЕТ strengthen Context requirements Но НЕ ДОЛЖЕН weaken Core пока claiming compatibility.

### CTX-120
Context structural conformance ДОЛЖЕН оставаться различимым из Context truth, completeness, applicability proof, transferability, causality и safety.

### CTX-121
High Context Fidelity НЕ ДОЛЖЕН быть interpreted as proof that сохранённый Context is factually true.

### CTX-122
материально relevant Context target, dimensions, values, epistemic status, temporal validity, provenance и uncertainty ДОЛЖЕН оставаться разрешимым.

---

# 182. Stress-test framework

`015-CONTEXT` ДОЛЖЕН оставаться robust against at least:

1. Context vs object;
2. Context vs State;
3. same condition as State and Context;
4. endogenous Context;
5. Context vs Participant;
6. Context vs Scope;
7. role-relative Context/Scope;
8. Context vs frame;
9. Context determining frame;
10. Context vs Profile;
11. Context vs Assumption;
12. assumed vs observed Context;
13. Context vs Preconditions;
14. Context vs Cause;
15. relevance vs causality;
16. Context vs Evidence;
17. Context vs Provenance;
18. storage metadata vs Context;
19. Context as semantic garbage bin;
20. Context target granularity;
21. missing Context;
22. unknown vs universal Context;
23. missing Context vs invalidity;
24. context-independent Claim;
25. Context dimensions;
26. dimension dependencies;
27. value uncertainty;
28. temporal Context;
29. phenomenon time vs Record time;
30. spatial Context vs Scope;
31. environmental Context;
32. technical/version Context;
33. biological Context;
34. social/cultural Context;
35. linguistic Context;
36. legal Context;
37. institutional Context;
38. experimental Context;
39. Observation Context;
40. Measurement Context;
41. Model Context;
42. Procedure Context;
43. Action Context;
44. Event Context;
45. Process Context;
46. State Context;
47. Result Context;
48. Relation Context;
49. Identity Context;
50. Claim Context;
51. generic vs universal Claim;
52. Context alignment;
53. Context mismatch;
54. contradiction under unknown Context;
55. Context drift;
56. silent Context loss;
57. Context substitution;
58. Context inheritance;
59. inheritance incompatibility;
60. dimension-level inheritance;
61. inherited Context portability;
62. override;
63. blocked inheritance;
64. Context composition;
65. cross-provenance composition;
66. co-occurrence assumption;
67. Context conflict;
68. Context provenance;
69. observed Context;
70. measured Context;
71. reported Context;
72. assumed Context;
73. inferred Context;
74. reconstructed Context;
75. later reconstruction vs original Source;
76. modeled Context;
77. default Context;
78. nominal Context;
79. Context uncertainty;
80. relevance unknown;
81. Context refinement;
82. Context correction;
83. Context versioning;
84. temporal validity;
85. snapshot vs interval;
86. Context continuity;
87. Context transition;
88. Context comparison;
89. similarity;
90. equivalence;
91. partial compatibility;
92. conditional compatibility;
93. compatibility vs Claim applicability;
94. transferability;
95. missing Context and transferability;
96. generalization;
97. invariance;
98. contextual exception;
99. Context transfer laundering;
100. boundary conditions;
101. operating envelope;
102. safety Context;
103. partial safety Context loss;
104. Risk Context;
105. Decision Context;
106. historical Context;
107. presentism;
108. future extrapolation;
109. cross-cultural transfer;
110. cross-jurisdiction transfer;
111. cross-version transfer;
112. cross-population transfer;
113. laboratory vs field;
114. sample vs environment;
115. Source production Context vs represented Context;
116. Context/Identity interaction;
117. Context/Relation interaction;
118. Context/Process interaction;
119. Context/State interaction;
120. Context/Result interaction;
121. Context/Event interaction;
122. Context/Action interaction;
123. Context/Claim interaction;
124. Context Record vs represented Context;
125. Context negation;
126. absence vs unknown;
127. unrecorded vs absent;
128. irrelevance vs unknown relevance;
129. potentially relevant Context;
130. Context hierarchy;
131. precedence conflict;
132. reusable Context;
133. template vs represented Context;
134. normalization;
135. qualitative-to-numeric corruption;
136. unit-conversion precision;
137. translation corruption;
138. summary corruption;
139. Context Fidelity vs truth;
140. Context loss;
141. contamination;
142. conflation;
143. leakage;
144. hallucination;
145. overgeneralization;
146. under-specification;
147. over-specification;
148. damaged archives;
149. offline preservation;
150. high-risk Profiles;
151. machine validation;
152. cross-standard collisions;
153. Entity Explosion.

Stress tests do not themselves create Core requirements.

Если Один stress test reveals Один necessary fundamental rule, that rule ДОЛЖЕН быть incorporated into Этот normative architecture.

---

# 183. Принцип сохранения

При конфликте между удобством обобщения и честностью representation предпочтение отдаётся честности.

    unknown Context
    > invented default Context

    missing Context
    > false universal applicability

    missing Context
    > false automatic invalidity

    partial Context
    > fabricated complete Context

    uncertain relevance
    > invented certainty of relevance or irrelevance

    Context condition
    > semantic-role collapse

    State + Context distinction
    > one universal condition bucket

    Context X
    > silent substitution by Context Y

    incompatible inheritance
    > convenient inheritance

    separate Sources
    > invented co-occurring Context

    partial transferability
    > invented universal transfer

    compatible Contexts
    > invented Claim applicability

    laboratory Result
    > false field universality

    historical Context
    > modern Context substitution

    assumed Context
    > falsely observed Context

    reconstructed Context
    > falsely historical certainty

    similar Context
    > invented Context identity

    unknown transferability
    > invented applicability

    contextual association
    > invented causality

    complete safety Context
    > dangerous partial summary

    high fidelity
    > false claim of truth

    incomplete archive
    > plausible contextual fabrication

Цель стандарта — сохранить Context настолько полно, насколько позволяют данные, **не превращая отсутствие Context в universal applicability или automatic invalidity, contextual condition в Cause, State или Scope без сохранения роли, parent Context в бесконтрольное inheritance, independent contextual values в вымышленную совместную ситуацию, modern Context в historical Context, laboratory Result в field truth, assumption в observation, Context similarity или compatibility в automatic applicability/transferability, а Context Fidelity — в доказательство истины**.

---

# 184. Итоговая формула

В компактной форме:

    Context
    → при каких материально relevant
      или potentially материально relevant
      условиях representation
      интерпретируется, наблюдалась,
      измерялась или применяется

    State
    → condition/configuration
      определённого subject

    Scope
    → к какой части domain
      representation applies

    Frame
    → в какой semantic/reference system
      representation interpreted

    Assumption
    → что принимается
      для reasoning/modeling

    Evidence
    → что поддерживает representation

    Provenance
    → откуда representation происходит

И:

    Context
    ≠ State

    Context
    ≠ Scope

    Context
    ≠ Frame universally

    Context
    ≠ Assumption

    Context
    ≠ Evidence

    Context
    ≠ Provenance

    Context
    ≠ Cause

    Context
    ≠ Participant automatically

Но:

    same factual condition
    МОЖЕТ участвовать в several roles
    if those roles remain explicit

Также:

    missing Context
    ≠ universal Context
    ≠ automatic invalidity

    represented as Context
    ≠ relevance proven

    assumed Context
    ≠ observed Context

    reconstructed Context
    ≠ original Source assertion

    parent Context
    ≠ child Context automatically

    individually supported Context values
    ≠ co-occurring Context automatically

    Context similarity
    ≠ Context compatibility

    Context compatibility
    ≠ Claim applicability

    Context compatibility
    ≠ unrestricted transferability

    valid in X
    ≠ valid in Y automatically

    Context Fidelity
    ≠ Context truth

---

# 185. Центральный принцип

> **Сохранить Context — значит сохранить существенные и потенциально существенные условия, относительно которых knowledge representation имеет определённый смысл, применимость или наблюдаемость, вместе с target, semantic role, epistemic status, temporal validity, provenance, uncertainty, relevance status и переносить limits этих условий, не позволяя системе потерять, подменить, выдумать, ошибочно унаследовать или универсализировать Context при сравнении, reasoning, переводе, суммаризации и переносе знания.**

---

# 186. Статус версии

**015-CONTEXT v0.1**

Версия прошла:

- первичную архитектурную сборку;
- полную adversarial attack;
- clean rebuild;
- контрольный аудит;
- cross-standard audit с `008–014`;
- Тест на разрастание сущностей;
- финальную интеграцию аудиторских исправлений.

В финальную версию дополнительно встроены:

- `actual Context` → epistemically safer representation language;
- uncertain/potential material relevance;
- `Context compatibility ≠ Claim applicability`;
- `Context Fidelity ≠ Context truth`.

Итог:

    Критические архитектурные дефекты:       0
    Существенные архитектурные дефекты:          0
    Средние архитектурные дефекты:         0
    Невнесённые исправления аудита:         0
    Новые обязательные Core-сущности:          0
    Тест на разрастание сущностей:                PASS
    Межстандартная совместимость:         PASS
    Требуется архитектурная перестройка:      NO

**015-CONTEXT v0.1 зафиксирован.**

Финальный hardening-аудит: PASS.
Выбранные adversarial barrier checks: PASS.
Критических архитектурных противоречий: 0.
Новых обязательных Core Entities: 0.
Невнесённых обязательных изменений: 0.
Статус: CLOSED.

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
