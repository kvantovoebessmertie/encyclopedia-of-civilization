# 016 — SCOPE
## Стандарт области применимости, охвата и границ знания

**Проект:** Энциклопедия цивилизации  
**Статус:** ACCEPTED / BASELINE  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляется Scope — область, множество, диапазон, конфигурация или иная граница, относительно которой knowledge representation заявляется, применяется, проверяется, интерпретируется, поддерживается или ограничивается.

Scope необходим для ответа на вопрос:

> **К чему именно относится данное representation — и за пределы какой области его нельзя автоматически переносить?**

Стандарт должен позволять сохранять:

- scoped target;
- semantic role Scope;
- universe/domain;
- inclusion criteria;
- exclusion criteria;
- population;
- sample;
- spatial range;
- temporal range;
- jurisdiction;
- system/version range;
- material range;
- parameter range;
- multidimensional Scope;
- correlated dimensions;
- valid tuples/configurations;
- discontinuous Scope;
- open/closed boundaries;
- vague/approximate boundaries;
- uncertain boundaries;
- intensional Scope;
- extensional Scope;
- dynamic Scope;
- hypothetical Scope;
- stated Scope;
- observed Scope;
- tested Scope;
- validated Scope;
- inferred Scope;
- modeled Scope;
- claimed Scope;
- analysis Scope;
- Evidence Scope;
- Scope provenance;
- membership provenance;
- Scope inheritance;
- Scope refinement;
- Scope narrowing;
- Scope expansion;
- Scope mapping;
- Scope transfer;
- Scope conflict;
- Scope-conditioned epistemic status;
- Scope Fidelity.

Стандарт должен предотвращать:

- universalization ограниченного Claim;
- sample-to-population laundering;
- member-to-population laundering;
- population-to-member laundering;
- ecological fallacy;
- atomistic fallacy;
- потерю denominator/reference population;
- потерю selection mechanism;
- смешение Scope и Quantifier;
- смешение Scope и Context;
- смешение Scope и Preconditions;
- смешение Scope и State;
- смешение Scope и Class;
- смешение Scope и Evidence;
- смешение Scope и Provenance;
- смешение разных semantic roles Scope;
- Cartesian-product hallucination;
- bounding-box hallucination;
- false interpolation;
- false extrapolation;
- false closure;
- Scope drift;
- Scope laundering;
- Scope hallucination;
- ложное Scope inheritance;
- Scope loss при extraction;
- Scope loss при canonicalization;
- автоматический Scope union при deduplication;
- потерю Scope при offline-представлении.

---

# 1. Основное понятие

## 1.1. Scope

**Scope (область применимости / охвата)** — semantic construct, определяющий domain subset, range, membership condition, configuration space или иную границу, относительно которой конкретное representation выполняет определённую semantic function.

В общем виде:

    Scope
    → к каким членам,
      случаям,
      диапазонам
      или конфигурациям
      относится representation
      в определённой semantic role

Scope MUST NOT пониматься как универсальный контейнер любых ограничений.

---

# 2. Scope имеет semantic role

Одно и то же множество может выполнять разные функции.

Например:

    adults

может быть:

- Claim applicability Scope;
- target population;
- study eligibility Scope;
- recruited population;
- analyzed population;
- Evidence Scope;
- recommendation Scope;
- regulatory Scope;
- verification Scope.

Следовательно:

    same extension
    ≠ same Scope semantics

где различие materially relevant.

Общие safeguards данного стандарта для Scope-like roles не означают, что все такие роли обязаны принадлежать одному онтологическому типу.

    shared Scope safeguards
    ≠ one mandatory ontological type

---

# 3. Scope anti-garbage principle

Ограничение не становится Scope только потому, что оно что-либо сужает.

Следовательно:

    Context
    ≠ Scope automatically

    Precondition
    ≠ Scope automatically

    State
    ≠ Scope automatically

    authorization rule
    ≠ Claim Scope automatically

    query filter
    ≠ Claim Scope automatically

    presentation grouping
    ≠ Claim Scope automatically

    access control
    ≠ epistemic Scope automatically

Semantic role MUST remain recoverable where material.

---

# 4. Scope requires a scoped target

Scope относится к чему-либо.

Scoped target MAY be:

- Claim;
- Relation;
- State representation;
- Event representation;
- Result;
- Process knowledge;
- Action;
- Procedure;
- Model;
- Measurement interpretation;
- Evidence;
- verification act;
- decision rule;
- semantic component;
- other representation.

Thus:

    Scope
    without scoped target
    MAY be ambiguous

---

# 5. Target granularity

Scope MAY apply to:

- whole Record;
- Claim;
- subclaim;
- Relation;
- argument of Relation;
- Result component;
- Procedure step;
- Model output;
- Evidence item;
- verification statement;
- other semantic component.

Therefore:

    Scope of container
    ≠ Scope of every contained component automatically

---

# 6. Scope MAY qualify semantic roles or argument positions

Scope constraints MAY concern different semantic positions.

Example:

    Relation:
    treats(drug, disease)

Possible constraints:

    drug:
    antibiotics

    disease:
    bacterial infections

These MUST NOT be flattened into one undifferentiated Scope where the distinction matters.

---

# 7. Joint and relational Scope

Some Scope constraints apply jointly to several dimensions or semantic roles.

Example:

    valid pairs:
    (adult, dose A)
    (child, dose B)

This MUST NOT become:

    population:
    adult OR child

    dose:
    A OR B

because that would fabricate:

    (adult, B)
    (child, A)

Therefore:

    valid component values
    ≠ valid combinations automatically

---

# 8. Scope and universe

Scope is interpreted relative to a universe/domain where required.

Example:

    Universe:
    humans

    Scope:
    humans age ≥65

But unresolved universe MAY remain represented as unresolved.

Therefore:

    unknown universe
    ≠ permission to invent universe

---

# 9. Scope ≠ Universe

Universe defines the broader domain of possible members.

Scope defines relevant members, ranges or configurations inside that domain.

    Universe
    ≠ Scope

---

# 10. Local universe

Quantification MAY operate over a local universe.

Example:

    "all samples"

may mean:

    all samples in Experiment E

not:

    all samples everywhere

Local universe MUST remain preservable.

---

# 11. Universe drift

Transformation MUST NOT silently change:

    all samples in Experiment E

into:

    all samples

or otherwise broaden the reference universe.

---

# 12. Nested universes

Representations MAY contain nested local universes.

Example:

    for every country
        all registered hospitals in that country

Flattening nested universes MUST NOT destroy quantifier dependencies.

---

# 13. Scope ≠ Quantifier

Scope defines the domain over which a proposition operates.

Quantifier defines how the proposition ranges over that Scope.

Therefore:

    Scope
    ≠ Quantifier

Example:

    Scope:
    birds

    Quantifier:
    most

    Claim:
    most birds can fly

---

# 14. Quantifier preservation

Material quantifiers MUST remain distinguishable, including:

- all;
- every;
- any;
- some;
- most;
- none;
- at least;
- at most;
- exactly;
- only;
- generic/non-universal formulations.

Transformation MUST NOT silently change them.

---

# 15. Scope membership ≠ member-level Claim truth

From:

    x ∈ Scope

and:

    Claim over Scope

one MUST NOT automatically infer:

    Claim(x)

unless Claim semantics and quantification license member-level instantiation.

Example:

    most birds can fly

    penguin ∈ birds

does NOT establish:

    penguin can fly

---

# 16. Universal instantiation is conditional

Broad-to-member or broad-to-narrow transfer MAY be licensed for suitable universal/distributive Claims.

Example:

    all mammals are vertebrates

MAY license:

    all dogs are vertebrates

But this rule MUST NOT be generalized to:

- statistical Claims;
- aggregate Claims;
- existential Claims;
- generic Claims;
- probabilistic Claims;
- modal Claims;
- distributional Claims.

Fundamental safeguard:

    Scope containment
    does not itself license
    Claim instantiation or transfer.

    Compatible Claim semantics
    are also required.

---

# 17. Generic Claim ≠ universal Claim

Example:

    tigers are striped

MUST NOT automatically be normalized as:

    every tiger without exception is striped

Generic semantics MUST remain distinguishable from universal quantification.

---

# 18. Aggregate Claim ≠ member Claim

Example:

    average lifespan of Population A = 80 years

does NOT establish:

    lifespan of each member = 80 years

Therefore:

    aggregate statement
    ≠ individual statement

---

# 19. Member evidence ≠ aggregate Claim

Observations about individual members MUST NOT automatically become population-level or aggregate Claims.

---

# 20. Ecological fallacy safeguard

A Relation observed between group-level variables MUST NOT automatically become a Relation between individual-level variables.

---

# 21. Atomistic fallacy safeguard

Individual-level Relations MUST NOT automatically be generalized into group/population-level Relations.

---

# 22. Level of analysis

Where material, representation SHOULD preserve relevant level of analysis, such as:

- individual;
- subgroup;
- population;
- aggregate;
- system;
- other domain-specific level.

Level of analysis MUST NOT be inferred solely from Scope membership.

---

# 23. Scope ≠ Context

Context answers primarily:

> При каких materially relevant условиях representation рассматривается?

Scope answers primarily:

> К каким членам, случаям или конфигурациям относится representation?

Thus:

    Scope
    ≠ Context

---

# 24. Same condition MAY participate in Scope and Context

A factual condition MAY participate in multiple semantic roles.

Example:

    age >65

MAY define:

    population Scope

and MAY participate in:

    interpretive Context

Role distinction MUST remain explicit where material.

---

# 25. Scope + Context coupling

Scope and Context MUST NOT be assumed independent.

Example:

    population A valid when T<20
    population B valid when T<10

This MUST NOT become:

    Scope = A OR B
    Context = T<20

because that fabricates applicability for:

    B at 10≤T<20

System MUST support coupled applicability constraints.

---

# 26. Scope ≠ Preconditions

A Precondition may restrict whether an Action/Procedure can be performed.

It MUST NOT automatically be transformed into Scope.

Likewise:

    Scope membership
    ≠ Preconditions satisfied

---

# 27. Conditional proposition ≠ scoped unconditional proposition

Representation:

    if A then B

MUST NOT universally be rewritten as:

    Scope = A
    Claim = B

unless semantic equivalence is justified.

---

# 28. Scope ≠ State

State describes condition/configuration of subject.

Scope identifies members/cases/configurations to which representation relates.

    State
    ≠ Scope

---

# 29. Scope ≠ Class

Class membership MAY participate in Scope definition.

But:

    Class
    ≠ Scope automatically

and:

    membership in Class
    ≠ applicability proof

---

# 30. Scope ≠ Sample

Need distinguish at minimum where material:

    eligibility Scope
    recruited Scope
    observed Scope
    analyzed Scope
    sample Scope
    target population Scope
    Claim Scope

These MUST NOT silently collapse.

---

# 31. Enrollment ≠ analysis Scope

Participants initially enrolled:

    ≠ participants actually analyzed

Attrition MUST NOT silently preserve the larger analysis Scope.

---

# 32. Missing-data Scope

Result computed only from cases with available/valid data MUST NOT automatically be represented as Result over the entire dataset.

---

# 33. Selection mechanism

Where materially relevant, Scope interpretation SHOULD preserve selection mechanism.

Examples:

- volunteers;
- survivors;
- responders;
- available records;
- convenience sample;
- screened population.

Selection mechanism MUST NOT silently disappear when it affects generalization.

---

# 34. Survivorship safeguard

Knowledge derived only from surviving/remaining cases MUST NOT automatically be generalized to the original population.

---

# 35. Denominator/reference population

Quantitative Claims SHOULD preserve materially relevant:

- numerator;
- denominator;
- reference population;
- sampling basis.

Example:

    3 of 10 tested samples reacted

MUST NOT automatically become:

    30% of all such material reacts

---

# 36. Scope ≠ Evidence

Evidence MAY itself have Scope.

But:

    Evidence Scope
    ≠ Claim Scope automatically

and:

    Claim Scope
    ≠ Evidence Scope automatically

---

# 37. Evidence-selection Scope

Restrictions on Evidence collection, such as:

    English-language studies only

MUST NOT automatically become applicability restrictions of the phenomenon/Claim.

---

# 38. Evidence-to-Scope alignment

Evidence support MUST remain aligned to the Scope it actually supports.

A citation supporting Scope A MUST NOT silently be presented as support for broader Scope A∪B.

---

# 39. Scope ≠ Provenance

Scope answers:

> к чему относится representation?

Provenance answers:

> откуда representation происходит?

Thus:

    Scope
    ≠ Provenance

---

# 40. Scope provenance

Scope MAY preserve provenance for:

- entire Scope;
- individual constraint;
- boundary;
- inclusion;
- exclusion;
- membership;
- mapping;
- exception.

Different Scope components MAY have different provenance.

---

# 41. Membership provenance

Scope definition Source and membership Source MAY differ.

Example:

    Source A defines category X
    Source B establishes Entity E ∈ X

System SHOULD preserve this distinction where material.

---

# 42. Exception provenance

Exception originating from Source B MUST NOT silently be attributed to Source A merely because it was combined with a Scope from Source A.

---

# 43. Scope provenance laundering

Composition MUST NOT make every contributing Source appear to support the entire composed Scope unless it actually does.

---

# 44. Declared Scope ≠ applicability proof

A declared Scope indicates represented applicability.

It does not itself establish truth throughout that Scope.

---

# 45. Recorded Scope ≠ real applicability

Recorded Scope is a representation.

It MAY be:

- correct;
- incorrect;
- incomplete;
- approximate;
- inferred;
- modeled;
- disputed;
- outdated;
- hypothetical;
- unknown.

---

# 46. Scope epistemic status

Scope or its components MAY be:

- explicitly stated;
- observed;
- tested;
- validated;
- reported;
- inferred;
- modeled;
- assumed;
- reconstructed;
- intended;
- designed;
- permitted;
- unknown.

These statuses MUST remain distinguishable where material.

---

# 47. Stated Scope ≠ demonstrated Scope

Source may state:

    applicable to all steel structures

while Evidence demonstrates only:

    tested on steel type X

These MUST remain distinguishable.

---

# 48. Intended ≠ realized Scope

Example:

    intended recruitment:
    500 adults

    actual recruitment:
    320 adults

Intended Scope MUST NOT replace realized Scope.

---

# 49. Designed ≠ tested ≠ validated ≠ observed ≠ permitted

For technical or normative knowledge:

    designed Scope
    tested Scope
    validated Scope
    observed Scope
    permitted Scope
    actual-use Scope

MAY differ.

They MUST NOT silently collapse.

---

# 50. Regulatory Scope ≠ scientific Scope

Legal approval for Scope X and scientific Evidence for Scope Y MAY coexist.

Neither MUST automatically replace the other.

---

# 51. Safety Scope ≠ efficacy Scope

A treatment/process MAY be:

    effective in Scope A∪B

but:

    established safe only in Scope A

Record-level Scope MUST NOT erase this distinction.

---

# 52. Normative Scope ≠ empirical Scope

A recommendation/prohibition applying to X does not itself establish empirical efficacy, harm or truth for X.

---

# 53. Excluded Scope ≠ harmful Scope

"Not for children" MAY represent:

- regulatory restriction;
- manufacturer policy;
- Evidence absence;
- safety concern;
- normative prohibition.

Exclusion alone MUST NOT be converted into a specific reason.

---

# 54. Scope dimensions

Scope MAY involve:

- Entity type;
- population;
- age;
- species;
- geography;
- jurisdiction;
- time;
- system version;
- material;
- parameter;
- operating condition;
- semantic definition;
- other domain-specific dimensions.

Core MUST NOT impose one universal fixed dimension list.

---

# 55. Multidimensional Scope

Scope MAY depend on several dimensions simultaneously.

But:

    multidimensional Scope
    ≠ Cartesian product automatically

---

# 56. Correlated dimensions

Scope dimensions MAY be correlated or dependent.

Valid values on each axis MUST NOT imply validity of every combination.

---

# 57. Tuple/configuration integrity

Scope MAY be represented as valid configurations/tuples.

Example:

    {(A,1), (B,2)}

This MUST NOT be decomposed and reconstructed as:

    {A,B} × {1,2}

unless such Cartesian composition is independently justified.

---

# 58. Cross-product hallucination

Transformation MUST NOT fabricate combinations by independently combining values originating from correlated dimensions.

---

# 59. Bounding-box hallucination

Validated points or configurations MUST NOT automatically become a rectangular/continuous validity region spanning their minimum and maximum coordinates.

---

# 60. Convex-hull hallucination

Validated points MUST NOT automatically imply validity of intermediate multidimensional regions.

---

# 61. Valid endpoints ≠ valid interval

Validity at endpoints:

    X1
    X2

does NOT establish validity for all values between X1 and X2.

---

# 62. Non-contiguous Scope

Scope MAY be discontinuous.

Example:

    versions 1.2, 1.4, 1.7

MUST NOT become:

    versions 1.2–1.7

---

# 63. Scope holes

Bounding interval MAY contain excluded regions.

Example:

    0–100°C
    except 37–42°C

Bounding interval MUST NOT be treated as complete Scope.

---

# 64. Boolean Scope structure

Scope constraints MAY use:

- AND;
- OR;
- NOT;
- nested combinations.

Logical grouping MUST remain explicit where ambiguity would change membership.

---

# 65. Operator precedence

Expression:

    A OR B AND C

MUST NOT be interpreted without defined grouping/precedence.

Prefer explicit grouping:

    A OR (B AND C)

or:

    (A OR B) AND C

---

# 66. Nested quantification

Scope representations MAY contain dependent quantification.

Example:

    for every region
        exists at least one hospital in that region

Flattening MUST NOT destroy quantifier order or dependency.

---

# 67. Inclusion criteria

Scope MAY contain explicit inclusion criteria.

They SHOULD remain recoverable where material.

---

# 68. Exclusion criteria

Material exclusions MUST remain recoverable.

---

# 69. Inclusion ≠ absence of exclusion

Meeting inclusion criteria does not guarantee membership when exclusion criteria also apply.

---

# 70. Exclusion ≠ negation

Exclusion from Scope means representation does not claim applicability there.

It does NOT automatically mean:

    Claim false there

---

# 71. Outside Scope

Fundamental rule:

    outside Scope
    ≠ Claim false automatically
    ≠ Claim true automatically

Often correct status is:

    applicability unknown/not asserted

---

# 72. Unknown Scope

    unknown Scope
    ≠ universal Scope
    ≠ empty Scope

---

# 73. Missing Scope

Missing Scope metadata MUST NOT imply:

    universal applicability

or:

    no applicability

---

# 74. Open Scope

Scope MAY be partially known.

Example:

    known applicable at least to A, B, C

without known maximum boundary.

---

# 75. Closed Scope

A Scope MAY explicitly claim completeness.

But closure MUST have defined semantics and reference frame.

---

# 76. Open-world membership

Under open-world semantics:

    no known membership
    ≠ non-membership

and:

    known members
    ≠ complete extension

---

# 77. Closed-world membership

Closed-world reasoning MAY be used only where completeness/closure is justified.

---

# 78. Closure is local

Closure MAY be:

- target-specific;
- dimension-specific;
- dataset-specific;
- time-specific;
- relation-specific.

Closure in one dimension MUST NOT automatically propagate to another.

---

# 79. Partial closure

Example:

A dataset MAY be complete for enrolled participants but incomplete for diagnoses.

Therefore:

    closed participants
    ≠ closed diagnoses

---

# 80. "All known" ≠ "all existing"

Example:

    all known planets at T

MUST remain distinguishable from:

    all planets existing at T

---

# 81. Empty Scope

Need distinguish:

    logically empty Scope
    no known members
    unknown membership
    currently no members

These are different states.

---

# 82. Vacuous truth safeguard

Logical truth arising only because Scope is empty MUST NOT automatically be interpreted as:

- empirical support;
- demonstrated applicability;
- practical validity;
- safety evidence.

---

# 83. Singleton Scope

Scope MAY contain one member without becoming Entity identity.

---

# 84. Finite / continuous / unbounded Scope

Scope MAY be:

- finite;
- enumerated;
- continuous;
- discontinuous;
- bounded;
- unbounded;
- partially known.

Core MUST NOT force all Scope into one representation form.

---

# 85. Intensional Scope

Scope MAY be defined by a rule:

    all humans age >65

This is an intensional definition.

---

# 86. Extensional Scope

Scope MAY be represented by members:

    {A,B,C}

This is an extensional representation.

---

# 87. Intensional ≠ extensional Scope

A rule defining membership and a current list of members MUST NOT automatically be treated as semantically identical.

---

# 88. Snapshot equality

Two Scopes having identical members at time T:

    ≠ semantic equivalence across time automatically

---

# 89. Dynamic Scope

Scope membership MAY change over time.

Examples:

- organization members;
- currently operational machines;
- legal jurisdictions;
- supported software versions.

Temporal validity SHOULD remain preservable.

---

# 90. Scope definition dependencies

Scope membership MAY depend on:

- State;
- Identity;
- Relation;
- Event;
- Process;
- Measurement;
- classification;
- taxonomy;
- external mapping;
- other Claims.

Dependencies SHOULD remain resolvable where material.

---

# 91. Dependency status propagation

If Scope membership depends on uncertain, disputed or unresolved information, resulting membership MUST NOT silently become certain.

Thus:

    uncertain dependency
    → MAY imply uncertain membership

    disputed dependency
    → MAY imply disputed membership

    unresolved dependency
    → MAY imply unresolved membership

The exact propagation semantics MAY depend on the dependency structure.

---

# 92. Identity-dependent Scope

Scope such as:

    works created by Person X

depends on Identity judgments.

Unresolved Identity MAY imply unresolved membership.

---

# 93. Relation-dependent Scope

Scope:

    countries bordering X

depends on Relation `borders`.

Disputed Relation MAY produce disputed membership.

---

# 94. State-dependent Scope

Scope:

    currently operational machines

depends on State and time.

State change MAY change Scope membership.

---

# 95. Event-dependent Scope

Scope:

    buildings damaged by Event E

may depend on Event identity and impact/causal Relations.

---

# 96. Measurement-dependent Scope

Scope membership MAY depend on Measurement.

Example:

    BP >140

Measurement uncertainty MAY create membership uncertainty.

---

# 97. Operational definition

Scope labels MAY require operational definitions.

Example:

    "obese"
    "elderly"
    "high temperature"

MUST NOT automatically be converted into exact thresholds without justified definition.

---

# 98. Same label ≠ same Scope

Example:

    adult

MAY mean ≥18 in one framework and ≥21 in another.

Therefore:

    same Scope label
    ≠ same Scope

---

# 99. Classification frame

Scope membership MAY depend on:

- ontology;
- taxonomy;
- legal definition;
- historical classification;
- scientific classification;
- institutional rule.

Relevant frame/version SHOULD remain preservable.

---

# 100. Vague/fuzzy Scope

Scope MAY be vague or graded.

Examples:

    elderly
    near coast
    high temperature
    experienced operator

Vague Scope MUST NOT automatically become a crisp exact set.

---

# 101. Approximate boundaries

Approximate boundary:

    ≈ 10

MUST NOT become exact:

    =10

or an unjustifiably precise converted value.

---

# 102. Open/closed numerical boundaries

Need preserve:

    >
    ≥
    <
    ≤

where material.

---

# 103. Boundary uncertainty

Boundary itself MAY be uncertain.

This uncertainty MUST remain representable.

---

# 104. Membership uncertainty

Membership of a particular Entity/configuration MAY be uncertain even when Scope definition is clear.

---

# 105. Component-level uncertainty

Different Scope components MAY have different uncertainty.

Example:

    population boundary = certain
    temporal boundary = uncertain

A single global confidence value MUST NOT erase this structure where material.

---

# 106. Spatial Scope

Spatial Scope MAY use:

- place;
- region;
- polygon;
- distance;
- altitude;
- biome;
- watershed;
- other spatial structures.

Spatial Scope MUST NOT automatically collapse into spatial Context.

---

# 107. Historical spatial Scope

Historical boundaries MUST NOT silently be replaced with modern boundaries.

---

# 108. Boundary migration

Geographic/administrative boundaries MAY change.

Scope MUST preserve relevant temporal/frame semantics.

---

# 109. Disputed geography

Disputed territorial membership MUST remain representable as disputed rather than silently resolved.

---

# 110. Jurisdictional Scope

Rule in jurisdiction A:

    ≠ rule in jurisdiction B

unless transfer is independently justified.

---

# 111. Jurisdiction containment ≠ normative precedence

Overlapping/nested jurisdictions MAY have simultaneous rules.

Geographic containment alone MUST NOT determine legal/normative precedence.

---

# 112. Temporal Scope

Temporal applicability MUST remain distinguishable from:

- publication time;
- Record creation time;
- Observation time;
- Event time;
- enactment time;
- transaction time;
- other temporal roles.

---

# 113. Temporal-role integrity

Example:

A law enacted at T2 MAY apply to Events at T1.

Therefore:

    enactment time
    ≠ applicability time

---

# 114. Temporal discontinuity

Temporal Scope MAY consist of multiple intervals.

It MUST NOT be forced into one continuous interval.

---

# 115. Historical Scope

Historical Scope MUST preserve historically relevant:

- definitions;
- classifications;
- jurisdictions;
- boundaries;
- terminology.

---

# 116. Category drift

Same term MAY denote different extensions over time.

Therefore:

    same historical/current label
    ≠ same Scope automatically

---

# 117. Population Scope

Population Scope MAY include materially relevant:

- species;
- age;
- biological/physiological grouping;
- exposure group;
- profession;
- status;
- other domain-specific characteristics.

Population Scope MUST NOT silently generalize.

---

# 118. Version Scope

Technical knowledge MAY apply to particular versions.

Version-family membership:

    ≠ behavioral equivalence

---

# 119. Version endpoints

Validity in version A and version C:

    ≠ validity in intermediate version B

unless supported.

---

# 120. Material Scope

Engineering/material knowledge MAY depend on:

- material;
- alloy;
- grade;
- composition;
- treatment;
- geometry;
- manufacturing process.

Material similarity:

    ≠ applicability equivalence

---

# 121. Parameter Scope

Knowledge MAY apply to parameter ranges or configuration regions.

Parameter range MUST NOT automatically be extrapolated beyond supported domain.

---

# 122. Domain of definition ≠ Claim Scope

Mathematical/computational domain of definition MUST remain distinguishable from Scope of a particular Claim.

Example:

    f(x)=1/x
    domain: x≠0

Claim:

    f decreases for x>0

Claim Scope:

    x>0

---

# 123. Model input domain ≠ validated Scope

A Model accepting an input:

    ≠ Model validated for that input

---

# 124. Measurement range distinctions

Need distinguish where material:

- display range;
- operational range;
- calibrated range;
- validated range;
- observed range.

These MUST NOT automatically collapse.

---

# 125. Interpretive Scope

Scope MAY affect interpretation rather than only applicability.

Example:

    "normal"

may have different meaning for newborns and adults.

Interpretive Scope MUST remain distinguishable from applicability Scope where material.

---

# 126. Semantic Scope

A Claim MAY hold only under a particular definition/frame.

Definition/frame SHOULD remain recoverable where materially necessary.

---

# 127. Hypothetical Scope

Model/counterfactual reasoning MAY define hypothetical populations/configurations.

Hypothetical Scope:

    ≠ actual Scope

---

# 128. Future Scope

Future-directed Scope MAY be represented without implying demonstrated future validity.

---

# 129. Scope intersection

Two Scopes MAY intersect.

But Claim composition over intersection requires semantic justification.

---

# 130. Scope union

Claims valid in Scope A and Scope B MAY support union only where:

- Claim semantics align;
- definitions align;
- relevant Context aligns;
- provenance/support remains correctly represented.

---

# 131. Cross-source Scope composition

Constraints from different Sources MUST NOT automatically form one asserted Scope.

Example:

    Source A → adults
    Source B → Europe

does not automatically establish:

    adults in Europe

for the same Claim.

---

# 132. Temporal composition safeguard

Scope:

    France at 1800

and:

    Germany at 1900

MUST NOT become simply:

    France + Germany

when temporal coupling is material.

---

# 133. Scope projection

A multidimensional Scope MAY be projected onto fewer dimensions.

But projection MAY be lossy.

Loss MUST remain detectable where material.

Projection of multidimensional Scope MAY destroy dependency information.

A lossy projection MUST NOT later be recombined as though those dependencies had been preserved.

Where material:

    lossy Scope projection
    SHOULD preserve derivation provenance

so that the richer source structure remains recoverable.

---

# 134. Decomposition/recomposition safeguard

Decomposing correlated Scope into independent dimension sets and later recombining them MUST NOT fabricate combinations.

---

# 135. Scope containment

A⊆B does not by itself determine validity transfer.

Scope containment alone MUST NOT license Claim instantiation or transfer.

Transfer additionally requires compatible Claim semantics and a justified inference.

---

# 136. Narrow-to-broad transfer

Validity in narrow Scope A:

    ≠ validity throughout broader Scope B

without justification.

---

# 137. Broad-to-narrow transfer

Validity in broad Scope MAY transfer to narrower Scope only when Claim semantics permit.

Universal/distributive Claim:

    MAY permit

Aggregate/statistical/generic/probabilistic Claim:

    MUST NOT be assumed to permit

---

# 138. Scope overlap

Overlap:

    ≠ equivalence

---

# 139. Scope equivalence

Equivalent membership:

    ≠ Record identity
    ≠ provenance identity
    ≠ semantic-role identity
    ≠ temporal equivalence automatically

---

# 140. Scope similarity

Similarity:

    ≠ equivalence
    ≠ transferability

---

# 141. Scope compatibility

Compatibility:

    ≠ equivalence
    ≠ applicability proof
    ≠ transferability proof

---

# 142. Scope mapping

Mapping MAY connect Scopes across:

- taxonomies;
- jurisdictions;
- historical classifications;
- geographic systems;
- version systems;
- semantic definitions.

Mapping MUST NOT automatically establish equivalence.

---

# 143. Lossy mapping

Lossy mapping MUST NOT support exact set reasoning as though no distinctions were lost.

---

# 144. Scope mismatch

Materially incompatible Scopes MUST remain detectable during:

- comparison;
- inference;
- Evidence aggregation;
- contradiction analysis;
- deduplication.

---

# 145. Scope alignment before contradiction

Claims SHOULD be Scope-aligned before contradiction judgment where material.

Different Scope:

    ≠ contradiction automatically

---

# 146. Scope difference ≠ Scope conflict automatically

Different Sources may state different Scopes due to:

- different Context;
- different endpoint;
- different time;
- different definition;
- different Evidence;
- genuine disagreement.

Difference alone MUST NOT be labeled contradiction without further analysis.

---

# 147. Negation and Scope

Need distinguish:

    Claim false for X
    Claim not asserted for X
    Claim inapplicable to X
    applicability unknown for X

These are not equivalent.

---

# 148. Negation/quantifier order

Transformation MUST preserve order.

Example:

    not all birds fly

≠

    all birds do not fly

---

# 149. Scope inheritance

Scope MAY be inherited from:

- heading;
- section;
- article;
- dataset;
- Procedure;
- Model;
- Source segment;
- other enclosing structure.

But:

    structural nesting
    ≠ valid inheritance automatically

---

# 150. Inheritance status

Need distinguish:

- explicit Scope;
- inherited Scope;
- inferred Scope;
- reconstructed Scope.

---

# 151. Dimension-level inheritance

Child MAY inherit some parent dimensions while overriding/narrowing others.

Example:

    parent:
    Europe + adults

    child:
    France

may yield:

    France + adults

only where semantics justify inheritance.

---

# 152. Incompatible inheritance

Unknown or incompatible parent-child semantics MUST NOT be treated as valid inheritance.

---

# 153. Heading Scope

Headings MAY encode material Scope.

Extraction SHOULD preserve it.

---

# 154. Table Scope

Row/column headers MAY encode Scope.

Cell extraction MUST preserve materially relevant row/column constraints.

---

# 155. Figure Scope

Axes, legend and caption MAY encode Scope.

Extracted Result MUST preserve materially relevant Scope.

---

# 156. Footnote Scope

Material Scope qualifiers in footnotes MUST NOT be discarded solely because of their structural location.

---

# 157. Citation Scope

Scope of cited Evidence MUST NOT automatically become Scope of author's Claim.

Likewise author's Claim Scope MUST NOT automatically become Evidence Scope.

---

# 158. Quoted Scope

A Source reporting another person's Claim MUST preserve distinction between:

    reported Scope
    endorsed Scope
    Evidence-supported Scope

---

# 159. Extraction portability

When a representation is removed from its original structure, materially relevant inherited Scope MUST travel with it or remain resolvably referenced.

---

# 160. Canonicalization safeguard

Canonicalization MUST NOT remove material Scope merely to create a simpler canonical Claim.

---

# 161. Deduplication safeguard

Identical Claim text with different Scope MUST NOT automatically be merged into a universalized Claim.

---

# 162. Scope union during deduplication

Deduplication MUST NOT automatically transform:

    Claim C in Scope A
    Claim C in Scope B

into:

    Claim C in A∪B

without semantic justification.

---

# 163. Scope-sensitive Identity

Scope MAY materially participate in Claim/Record identity criteria.

Whether two differently scoped Claims count as:

- same Claim with different qualifiers;
- distinct Claims;

depends on defined identity semantics.

`016` MUST remain compatible with `014-IDENTITY`.

---

# 164. Scope-sensitive Evidence

Evidence support MAY vary across Scope.

Example:

    adults → strong support
    elderly → weak support

One global support value MUST NOT erase this difference where material.

---

# 165. Scope-sensitive uncertainty

Uncertainty MAY vary across Scope regions.

Example:

    age 18–60 → high confidence
    age 61–70 → uncertain

---

# 166. Scope-sensitive risk

Risk MAY vary across Scope.

Global risk label MUST NOT hide materially different risk across subscopes.

---

# 167. Scope-sensitive verification

Verification MAY cover only part of a Record/Claim/Scope.

Partial verification MUST NOT automatically mark the entire broader representation as verified.

---

# 168. Scope-sensitive conflict

Sources MAY conflict only within part of Scope.

System SHOULD preserve locality of conflict where material.

---

# 169. Scope partitioning

A Scope MAY be partitioned into subregions with different:

- Evidence;
- confidence;
- Result;
- risk;
- verification;
- applicability;
- Context requirements.

Core MUST support this semantics without requiring every partition to become a fundamental Entity.

---

# 170. Inference Scope

Derived Claim MUST NOT silently exceed Scope justified by:

- premises;
- inference rule;
- Context;
- definitions;
- relevant domain constraints.

---

# 171. Multi-premise inference

When several premises must hold simultaneously, derived applicability MUST NOT exceed their justified joint domain.

Often this is an intersection, but Core MUST NOT impose intersection as a universal rule for every inference type.

---

# 172. Empty-intersection safeguard

If required premise Scopes do not overlap:

    joint inference MAY be inapplicable

System MUST NOT fabricate common Scope.

---

# 173. Inference-specific Scope transformation

Inference rules MAY transform Scope nontrivially.

Such transformation MUST be explicit/justifiable rather than assumed.

---

# 174. Derived Scope provenance

Scope created by inference MUST remain distinguishable from Source-stated Scope.

---

# 175. Scope extrapolation

Extrapolation beyond directly supported Scope MUST remain identifiable as extrapolation/modeling/inference.

---

# 176. Interpolation safeguard

Being between supported points:

    ≠ demonstrated validity automatically

---

# 177. Safety interpolation safeguard

In safety-critical domains:

    safe at point A
    safe at point B

MUST NOT automatically imply:

    safe at all intermediate configurations

---

# 178. Cross-Scope invariance

Observed invariance across tested Scopes:

    ≠ universal invariance

---

# 179. Scope transferability

Transfer from Scope A to Scope B MAY be:

- supported;
- partially supported;
- conditional;
- uncertain;
- unknown;
- unsupported.

---

# 180. Scope transfer ≠ Context transfer

They MAY interact but MUST remain distinguishishable.

---

# 181. Scope laundering

Chains involving:

- taxonomy;
- similarity;
- containment;
- mapping;
- inheritance;
- overlap;
- compatibility;
- Evidence selection;

MUST NOT be compressed into unsupported applicability.

---

# 182. Taxonomic laundering

    valid for dogs
    dogs ⊂ mammals

does NOT establish:

    valid for all mammals

---

# 183. Geographic laundering

    valid in France

does NOT establish:

    valid throughout Europe

---

# 184. Temporal laundering

    valid in 2020

does NOT establish:

    valid throughout an era containing 2020

---

# 185. Version laundering

    valid in v2.1

does NOT establish:

    valid in all v2.x

---

# 186. Population laundering

    observed in adult men

does NOT establish:

    all adults
    all men
    all humans

---

# 187. Sample laundering

    Result in sample

does NOT automatically become:

    population Claim

---

# 188. Cross-role laundering

A Scope in one semantic role MUST NOT silently become another.

Examples:

    Evidence Scope
    → Claim Scope

    tested Scope
    → approved Scope

    approved Scope
    → safe Scope

    study inclusion Scope
    → phenomenon Scope

    access Scope
    → applicability Scope

---

# 189. "Only" safeguard

Limited Evidence for X:

    ≠ applicability only to X

Example:

    studied in adults

does NOT establish:

    works only in adults

---

# 190. "All" safeguard

Finite or incomplete Evidence:

    ≠ universal quantification

without justification.

---

# 191. "Some" safeguard

Existential support:

    ≠ universal support

---

# 192. No-Evidence safeguard

No Evidence for Scope X:

    ≠ evidence of non-applicability to X

---

# 193. Natural-language Scope

Natural-language Scope MAY be:

- explicit;
- implicit;
- distributed;
- structurally inherited;
- ambiguous;
- vague;
- definition-dependent.

Machine extraction MUST preserve uncertainty/ambiguity rather than fabricate precision.

---

# 194. Modifier ambiguity

Ambiguous modifier attachment MUST NOT be silently resolved when it materially changes Scope.

---

# 195. Coordination ambiguity

Expressions such as:

    A and B with C

MAY have multiple Scope parses.

Ambiguity SHOULD remain explicit until resolved.

---

# 196. Implicit subject Scope

Procedure commands such as:

    wear gloves

MAY imply:

    operators performing Procedure

but this MUST be treated as structural/semantic inference rather than explicit universal Scope.

---

# 197. Default assumptions

Domain defaults MAY aid interpretation.

But:

    domain default
    ≠ Source-stated Scope

---

# 198. Normalization

Scope normalization MUST NOT:

- invent universe;
- invent boundary;
- invent quantifier;
- invent exclusivity;
- invent precision;
- remove exceptions;
- remove uncertainty;
- change semantic role;
- destroy dimensional coupling.

---

# 199. Historical normalization

Historical categories MUST NOT silently be mapped to modern categories as exact equivalents.

---

# 200. Translation fidelity

Translation MUST preserve materially relevant:

- Scope role;
- universe;
- inclusion;
- exclusion;
- quantifier;
- boundary;
- definition;
- uncertainty;
- temporal semantics;
- jurisdiction;
- dimensional coupling.

---

# 201. Scope Fidelity

**Scope Fidelity** — degree to which transformation preserves materially relevant Scope semantics.

It MAY concern:

- target;
- role;
- universe;
- members;
- constraints;
- boundaries;
- tuples/configurations;
- uncertainty;
- provenance;
- temporal validity;
- epistemic status.

---

# 202. Scope Fidelity ≠ truth

Faithfully preserving an incorrect Source Scope MAY have high Scope Fidelity.

Therefore:

    Scope Fidelity
    ≠ Scope truth

---

# 203. Scope Fidelity ≠ overall semantic fidelity

A representation may preserve Scope while corrupting:

- Quantifier;
- modality;
- Claim content;
- causality;
- confidence;
- Evidence relation.

Thus:

    high Scope Fidelity
    ≠ high Claim Fidelity automatically

---

# 204. Scope loss

Scope loss occurs when material applicability/coverage boundaries disappear.

Typical failure:

    limited Claim
    → apparently universal Claim

---

# 205. Scope contamination

Scope from one representation is incorrectly attached to another.

---

# 206. Scope conflation

Distinct Scope roles/definitions are merged without justification.

---

# 207. Scope hallucination

Missing Scope information is invented.

Preference:

    unknown Scope
    > plausible unsupported Scope

---

# 208. Scope overgeneralization

Representation is broadened beyond supported Scope.

---

# 209. Scope overspecification

Unsupported boundaries/exclusions are added.

---

# 210. Scope underspecification

Material Scope boundaries are omitted.

---

# 211. Scope drift

**Scope drift** — alteration, loss, expansion, contraction, role substitution or reconfiguration of Scope during:

- storage;
- extraction;
- inference;
- translation;
- summarization;
- canonicalization;
- deduplication;
- export;
- reuse.

---

# 212. Scope role drift

Example:

    tested in adults

becomes:

    approved for adults

Even if extension remains adults, semantic role changed.

This is Scope corruption.

---

# 213. Scope tuple drift

Correlated configuration:

    (A,1)
    (B,2)

becomes independent:

    {A,B} × {1,2}

This is Scope corruption.

---

# 214. Scope closure drift

Open-world Scope MUST NOT silently become closed-world enumeration.

---

# 215. Scope definition drift

Same label MUST NOT silently change operational definition/frame.

---

# 216. Scope summary fidelity

Summary MUST NOT convert:

    adults studied
    → humans

    some adults
    → adults

    study sample
    → population

    known members
    → all members

    version 2.1
    → version 2.x

    France
    → Europe

    safe under configuration X
    → safe

    evidence exists in X
    → applies only to X

---

# 217. Scope compression

Compression MAY simplify representation but MUST preserve materially relevant:

- role;
- universe;
- quantifier relationship;
- exclusions;
- boundaries;
- tuples;
- Context coupling;
- uncertainty;
- temporal validity;
- provenance.

---

# 218. Safety Scope

Safety statements MUST preserve material Scope.

Example:

    safe for adults under condition X

MUST NOT become:

    safe

---

# 219. Safety-critical configuration

In safety-critical knowledge, valid independent ranges MUST NOT be assumed to define a safe multidimensional region.

---

# 220. Safety boundary uncertainty

Uncertain safety boundary MUST NOT be converted into exact safe threshold.

---

# 221. Risk Scope

Risk estimate in Population A:

    ≠ Risk in Population B automatically

---

# 222. Procedure Scope

Procedure MAY apply only to specific:

- Actors;
- materials;
- equipment;
- populations;
- environments;
- versions;
- jurisdictions;
- configurations.

Material Procedure Scope MUST remain recoverable.

---

# 223. Decision Scope

Decision rule MUST NOT silently expand beyond defined cases.

---

# 224. Model Scope

Model domain of validity MUST remain distinguishable from all syntactically accepted inputs.

---

# 225. Action Scope

Action knowledge MAY have Scope concerning:

- Actor;
- target;
- tool;
- authority;
- population;
- system;
- environment.

Compatibility with `008-ACTION` MUST remain preserved.

---

# 226. Event Scope

Event representation MAY have Scope concerning:

- participants;
- affected area;
- subevents;
- temporal extent.

Compatibility with `009-EVENT` MUST remain preserved.

---

# 227. Result Scope

Result MAY concern:

- one run;
- analyzed sample;
- population;
- system;
- time interval;
- parameter region.

Compatibility with `010-RESULT` MUST remain preserved.

---

# 228. State Scope

State representation MAY concern defined subjects/time/configurations.

Compatibility with `011-STATE` MUST remain preserved.

---

# 229. Process Scope

Process knowledge MAY depend on materials, organisms, systems or configurations.

Compatibility with `012-PROCESS` MUST remain preserved.

---

# 230. Relation Scope

Relation MAY hold only for defined participant/configuration sets.

Compatibility with `013-RELATION` MUST remain preserved.

---

# 231. Identity Scope

Identity judgments MAY themselves be scoped.

Compatibility with `014-IDENTITY` MUST remain preserved.

---

# 232. Context compatibility

Scope and Context MUST remain distinguishable while allowing coupled applicability constraints.

Compatibility with `015-CONTEXT` MUST remain preserved.

---

# 233. Meta-Scope

A Claim MAY concern Scope of another representation.

Example:

    "The applicability boundary of Procedure P is uncertain."

Need distinguish:

    target of meta-Claim = Scope(P)

from:

    Scope of meta-Claim itself

---

# 234. Scope about Scope

Higher-order references MUST NOT collapse object-level Scope and meta-level Scope.

---

# 235. Verification Scope

Verification MAY concern only:

- one Claim;
- one dimension;
- one boundary;
- one Source;
- one Scope region.

Partial verification MUST NOT become global verification.

---

# 236. Authority/competence Scope

Expert competence MAY itself have Scope.

Example:

    structural engineering

This MUST remain distinguishable from applicability Scope of the Claim being reviewed.

---

# 237. Retrieval Scope

Search/filter/retrieval Scope MUST NOT automatically become semantic Scope of retrieved Claims.

---

# 238. Presentation Scope

Article/chapter/navigation grouping MUST NOT automatically become Claim applicability Scope.

---

# 239. Access-control Scope

Who may access a representation:

    ≠ to whom the knowledge applies

---

# 240. Machine validation

Validator MAY detect:

- missing required Scope;
- malformed ranges;
- contradictory boundaries;
- impossible intersections;
- invalid operators;
- Scope-role mismatch;
- inclusion/exclusion conflicts;
- tuple decomposition errors;
- unsupported closure declarations;
- broken references.

But:

    validator PASS
    ≠ Scope truth
    ≠ Claim truth
    ≠ Evidence sufficiency
    ≠ safety

---

# 241. Impossible Scope

A logically contradictory Scope SHOULD remain detectable.

Example:

    age <5
    AND
    age >80

Need distinguish:

    logically empty
    ≠ unknown
    ≠ no known members

---

# 242. Circular Scope definition

Circular references:

    Scope A depends on B
    Scope B depends on A

MUST NOT automatically be considered resolved without an independent semantic anchor or valid fixed-point semantics.

---

# 243. Recursive Scope

Recursive Scope definitions MAY be valid, but recursion semantics MUST be defined sufficiently to prevent uncontrolled or ambiguous resolution.

---

# 244. Offline preservation

Scope SHOULD remain interpretable offline.

Where material preserve:

- scoped target;
- semantic role;
- universe;
- inclusion/exclusion;
- quantifier relationship;
- ranges;
- units;
- tuple/configuration structure;
- time;
- population;
- jurisdiction;
- version;
- uncertainty;
- provenance.

---

# 245. Human-readable offline safeguard

Safety-critical or materially important Scope MUST NOT depend solely on opaque identifiers or fragile detached references.

A human-readable offline representation SHOULD remain possible.

Material Scope qualifiers SHOULD be co-located with the knowledge they constrain when separation creates a significant risk of offline loss or dangerous misinterpretation.

---

# 246. Detached legend safeguard

Material Scope MUST NOT depend solely on a legend, hyperlink or external reference likely to disappear during print/copy/export when this would make the knowledge unsafe or misleading.

---

# 247. Carrier neutrality

Scope semantics MUST NOT depend on:

- RDF;
- JSON;
- SQL;
- graph database;
- Markdown;
- PDF;
- print;
- specific software.

---

# 248. Diagnostic families

## 248.1. Scope/Quantifier collapse

    most X
    → all X

## 248.2. Scope/Context collapse

    Context restriction
    → population Scope

## 248.3. Scope/Precondition collapse

    operational prerequisite
    → applicability Scope

## 248.4. Scope/State collapse

    individual State
    → population Scope

## 248.5. Scope/Class collapse

    class membership
    → applicability proof

## 248.6. Scope/Sample collapse

    sample
    → target population

## 248.7. Scope/Evidence collapse

    Evidence Scope
    → Claim Scope

## 248.8. Scope/Provenance collapse

    Source origin
    → applicability Scope

## 248.9. Scope-role collapse

    tested
    → approved
    → safe

## 248.10. Aggregate/member collapse

    population average
    → individual value

## 248.11. Ecological fallacy

    group Relation
    → individual Relation

## 248.12. Atomistic fallacy

    individual Relation
    → population Relation

## 248.13. Denominator loss

    3/10 sample
    → 30% population

## 248.14. Selection loss

    selected/surviving sample
    → original population

## 248.15. Unknown-Scope failure

    missing Scope
    → universal/empty Scope

## 248.16. Open-world failure

    no known member
    → non-member

## 248.17. Closure leakage

    closed dimension A
    → closed dimension B

## 248.18. Intensional/extensional collapse

    current member list
    → permanent Scope definition

## 248.19. Cartesian-product hallucination

    valid values
    → every combination valid

## 248.20. Bounding-box hallucination

    validated points
    → entire range valid

## 248.21. Interpolation hallucination

    endpoints valid
    → interval valid

## 248.22. Tuple decomposition loss

    correlated configurations
    → independent dimensions

## 248.23. Scope/Context decoupling

    conditional validity surface
    → independent Scope + Context

## 248.24. Scope inheritance failure

    parent Scope
    → child automatically

## 248.25. Cross-source composition failure

    independent constraints
    → combined Scope

## 248.26. Scope broadening

    adults
    → humans

## 248.27. Scope narrowing

    mammals
    → only dogs

without exclusivity support.

## 248.28. Taxonomic laundering

    subset validity
    → superset validity

## 248.29. Geographic laundering

    region
    → superregion

## 248.30. Temporal laundering

    interval
    → era

## 248.31. Version laundering

    version
    → version family

## 248.32. Population laundering

    subgroup
    → population

## 248.33. Cross-role laundering

    Evidence restriction
    → applicability restriction

## 248.34. Quantifier corruption

    some
    → all

## 248.35. Exclusivity hallucination

    studied in X
    → only valid in X

## 248.36. Boundary corruption

    >10
    → ≥10

## 248.37. Definition hallucination

    elderly
    → ≥65

without basis.

## 248.38. Historical Scope drift

    historical category
    → modern category

## 248.39. Scope provenance laundering

    partial Source support
    → whole Scope attributed to Source

## 248.40. Scope dependency failure

    uncertain basis
    → certain membership

## 248.41. Scope canonicalization loss

    scoped Claim
    → universal canonical Claim

## 248.42. Deduplication union

    C@A + C@B
    → C@(A∪B)

without justification.

## 248.43. Scope-sensitive Evidence laundering

    Evidence@A
    → Evidence@(A∪B)

## 248.44. Scope-sensitive confidence laundering

    high confidence@A
    → high confidence globally

## 248.45. Scope-sensitive verification laundering

    verified@A
    → verified globally

## 248.46. Scope-sensitive risk loss

    risk differs by Scope
    → one global risk

## 248.47. Negation/quantifier inversion

    not all
    → all not

## 248.48. Local-universe loss

    all X in E
    → all X

## 248.49. Scope Fidelity confusion

    Scope preserved
    → entire Claim assumed faithful

## 248.50. Lossy-projection reconstruction

    projected independent dimensions
    → reconstructed original dependency

## 248.51. Ontological Scope-role collapse

    shared safeguards
    → mandatory single Scope ontology

Diagnostic label does not establish:

- intent;
- fraud;
- negligence;
- responsibility.

---

# 249. Cross-standard compatibility

`016-SCOPE` MUST preserve boundaries established by:

- `008-ACTION`;
- `009-EVENT`;
- `010-RESULT`;
- `011-STATE`;
- `012-PROCESS`;
- `013-RELATION`;
- `014-IDENTITY`;
- `015-CONTEXT`.

Compactly:

    Scope
    → which members/cases/configurations

    Context
    → under which relevant conditions

    State
    → condition/configuration of subject

    Relation
    → semantic connection among relata

    Identity
    → whether representations refer
      to same represented thing

Therefore:

    Scope
    ≠ Context
    ≠ State
    ≠ Class
    ≠ Sample
    ≠ Evidence
    ≠ Provenance
    ≠ Quantifier
    ≠ applicability proof

The same factual information MAY participate in multiple semantic roles, but those roles MUST remain distinguishable where material.

---

# 250. Boundary concepts outside full 016 ontology

`016` uses but does not fully define:

- Universe;
- Domain;
- Quantifier;
- Population;
- Sample;
- Class;
- Evidence;
- Provenance;
- Preconditions;
- Model;
- Procedure;
- Decision;
- Verification;
- Authority;
- Risk;
- Safety;
- Extrapolation;
- Transferability;
- Applicability.

Their complete semantics belong to existing or future standards.

---

# 251. Entity Explosion Test

`016-SCOPE` DOES NOT require introducing as fundamental Core Entities:

- Scope;
- ScopeType;
- ScopeRole;
- ScopeDimension;
- ScopeConstraint;
- ScopeBoundary;
- ScopeTuple;
- ScopePartition;
- ScopeMembership;
- ScopeClosure;
- ScopeDefinition;
- ScopeMapping;
- ScopeSupport;
- ScopeConflict;
- ScopeVersion;
- ScopeInheritance;
- ScopeOverride;
- ScopeCompatibility;
- ScopeTransfer;
- ScopeFidelity;
- ScopeEpistemicStatus.

These MAY be represented through:

- Claims;
- Relations;
- Records;
- Sets;
- ranges;
- structured constraints;
- temporal/spatial structures;
- Models;
- Profiles;
- provenance;
- existing generic infrastructure.

Absence of dedicated Core Entity does not imply absence of Scope semantics.

Shared Scope safeguards do not imply that all Scope-like roles must belong to one ontological type.

---

# 252. Core invariants

### SCP-01
Scope MUST preserve the domain subset, range, membership condition or configuration to which a representation relates in a defined semantic role.

### SCP-02
Scope MUST NOT be used as an undifferentiated bucket for every restriction.

### SCP-03
Material Scope semantic role MUST remain recoverable.

### SCP-04
Scope MUST remain associated with its scoped target where ambiguity matters.

### SCP-05
Container Scope MUST NOT automatically become Scope of every contained component.

### SCP-06
Scope MAY qualify individual semantic roles/arguments and those qualifications MUST remain distinguishable where material.

### SCP-07
Joint Scope constraints MUST NOT be flattened into independent constraints when doing so creates unsupported combinations.

### SCP-08
Scope SHOULD remain interpretable relative to a universe/domain where material.

### SCP-09
Unknown universe MUST NOT be replaced by invented universe.

### SCP-10
Scope MUST remain distinguishable from Universe.

### SCP-11
Local universe MUST remain preservable.

### SCP-12
Local universe MUST NOT silently expand during transformation.

### SCP-13
Nested universes and dependent quantifiers MUST remain representable.

### SCP-14
Scope MUST remain distinguishable from Quantifier.

### SCP-15
Material quantifiers MUST remain preserved.

### SCP-16
Scope membership MUST NOT automatically establish member-level Claim truth.

### SCP-17
Universal/distributive transfer MUST occur only when Claim semantics license it.

### SCP-18
Scope containment MUST NOT itself license Claim instantiation or transfer.

### SCP-19
Generic Claims MUST NOT automatically become universal Claims.

### SCP-20
Aggregate Claims MUST NOT automatically become member-level Claims.

### SCP-21
Member observations MUST NOT automatically become population Claims.

### SCP-22
Group-level Relations MUST NOT automatically become individual-level Relations.

### SCP-23
Individual-level Relations MUST NOT automatically become population-level Relations.

### SCP-24
Material level of analysis SHOULD remain preservable.

### SCP-25
Scope MUST remain distinguishable from Context.

### SCP-26
The same condition MAY participate in Scope and Context roles without role collapse.

### SCP-27
Scope and Context MUST NOT be assumed independent.

### SCP-28
Coupled applicability constraints MUST remain representable.

### SCP-29
Scope MUST remain distinguishable from Preconditions.

### SCP-30
Scope membership MUST NOT imply satisfaction of Preconditions.

### SCP-31
Conditional propositions MUST NOT automatically become scoped unconditional propositions.

### SCP-32
Scope MUST remain distinguishable from State.

### SCP-33
Scope MUST remain distinguishable from Class.

### SCP-34
Class membership MUST NOT automatically establish applicability.

### SCP-35
Sample, eligibility, recruited, observed, analyzed, target-population and Claim Scope MUST remain distinguishable where material.

### SCP-36
Enrollment Scope MUST NOT automatically become analysis Scope.

### SCP-37
Missing-data filtering MUST NOT silently preserve broader Result Scope.

### SCP-38
Material selection mechanisms SHOULD remain preservable.

### SCP-39
Survivorship MUST NOT silently generalize to original population.

### SCP-40
Material numerator, denominator and reference population SHOULD remain preservable for quantitative Claims.

### SCP-41
Scope MUST remain distinguishable from Evidence.

### SCP-42
Evidence Scope MUST NOT automatically become Claim Scope.

### SCP-43
Claim Scope MUST NOT automatically become Evidence Scope.

### SCP-44
Evidence-selection restrictions MUST NOT automatically become phenomenon applicability restrictions.

### SCP-45
Evidence support MUST remain aligned to the Scope actually supported.

### SCP-46
Scope MUST remain distinguishable from Provenance.

### SCP-47
Scope provenance MAY exist at whole-Scope and component level.

### SCP-48
Membership provenance MUST remain preservable where material.

### SCP-49
Exception provenance MUST NOT be silently reassigned.

### SCP-50
Scope composition MUST NOT launder partial Source support into whole-Scope Source support.

### SCP-51
Declared Scope MUST NOT be treated as applicability proof.

### SCP-52
Recorded Scope MUST NOT automatically be treated as true/complete applicability.

### SCP-53
Scope epistemic status MUST remain preservable.

### SCP-54
Stated Scope MUST remain distinguishable from demonstrated Scope.

### SCP-55
Intended Scope MUST remain distinguishable from realized Scope.

### SCP-56
Designed, tested, validated, observed, permitted and actual-use Scope MUST remain distinguishable where material.

### SCP-57
Regulatory Scope MUST remain distinguishable from scientific Scope.

### SCP-58
Safety Scope MUST remain distinguishable from efficacy Scope.

### SCP-59
Normative Scope MUST remain distinguishable from empirical Scope.

### SCP-60
Scope exclusion MUST NOT automatically imply a particular reason, harm or falsity.

### SCP-61
Core MUST NOT impose one universal fixed Scope dimension list.

### SCP-62
Shared Scope safeguards MUST NOT require all Scope-like roles to belong to one ontological type.

### SCP-63
Multidimensional Scope MUST NOT be treated as Cartesian product automatically.

### SCP-64
Dependent/correlated dimensions MUST remain representable.

### SCP-65
Valid component values MUST NOT automatically imply validity of every combination.

### SCP-66
Tuple/configuration integrity MUST survive decomposition, storage and reconstruction.

### SCP-67
Validated points MUST NOT automatically generate a bounding-box validity region.

### SCP-68
Validated points MUST NOT automatically generate a convex/continuous validity region.

### SCP-69
Valid endpoints MUST NOT automatically imply valid interval.

### SCP-70
Non-contiguous Scope MUST remain representable.

### SCP-71
Scope holes/exceptions MUST remain preservable.

### SCP-72
Boolean Scope structure and grouping MUST remain preservable.

### SCP-73
Nested quantification MUST NOT be flattened when order/dependency matters.

### SCP-74
Material inclusion criteria MUST remain preservable.

### SCP-75
Material exclusion criteria MUST remain preservable.

### SCP-76
Inclusion MUST NOT automatically override exclusions.

### SCP-77
Exclusion from Scope MUST NOT automatically imply Claim falsity.

### SCP-78
Outside Scope MUST NOT automatically imply truth or falsity.

### SCP-79
Unknown Scope MUST NOT be treated as universal Scope.

### SCP-80
Unknown Scope MUST NOT be treated as empty Scope.

### SCP-81
Missing Scope MUST NOT imply universal or empty applicability.

### SCP-82
Open Scope MUST remain representable.

### SCP-83
Closed Scope requires defined closure semantics.

### SCP-84
Under open-world semantics, absence of known membership MUST NOT imply non-membership.

### SCP-85
Known members MUST NOT automatically be treated as complete extension.

### SCP-86
Closed-world reasoning requires justified closure.

### SCP-87
Closure MUST remain local to the target/dimension/domain for which it is established.

### SCP-88
Closure MUST NOT leak across dimensions.

### SCP-89
"All known" MUST remain distinguishable from "all existing."

### SCP-90
Logically empty Scope MUST remain distinguishable from unknown/no-known-member Scope.

### SCP-91
Vacuous logical truth MUST NOT automatically become empirical/practical validity.

### SCP-92
Singleton Scope MUST NOT collapse into Entity identity.

### SCP-93
Finite, continuous, discontinuous, bounded, unbounded and partially known Scope MUST remain representable where required.

### SCP-94
Intensional Scope MUST remain distinguishable from extensional membership representation.

### SCP-95
Extensional equality at one time MUST NOT automatically establish persistent semantic equivalence.

### SCP-96
Dynamic Scope SHOULD preserve temporal validity.

### SCP-97
Scope definition dependencies SHOULD remain resolvable where material.

### SCP-98
Uncertain, disputed or unresolved dependency status MUST NOT silently become certain Scope membership.

### SCP-99
Identity-dependent membership MAY remain unresolved when Identity is unresolved.

### SCP-100
Relation-dependent membership MAY remain disputed when Relation is disputed.

### SCP-101
State-dependent Scope MUST preserve relevant temporal semantics.

### SCP-102
Event-dependent Scope MUST preserve relevant Event/Relation dependencies.

### SCP-103
Measurement-dependent membership MUST preserve material Measurement uncertainty.

### SCP-104
Vague labels MUST NOT be converted into exact operational boundaries without basis.

### SCP-105
Same Scope label MUST NOT automatically imply same Scope.

### SCP-106
Relevant classification/taxonomy/definition frame SHOULD remain preservable.

### SCP-107
Vague/fuzzy Scope MUST NOT automatically become crisp Scope.

### SCP-108
Approximate boundaries MUST NOT become exact boundaries.

### SCP-109
Inclusive/exclusive boundary operators MUST remain preservable.

### SCP-110
Boundary uncertainty MUST remain representable.

### SCP-111
Membership uncertainty MUST remain representable.

### SCP-112
Component-level Scope uncertainty MUST remain representable where material.

### SCP-113
Spatial Scope MUST remain distinguishable from spatial Context.

### SCP-114
Historical spatial Scope MUST NOT silently use modern boundaries.

### SCP-115
Boundary migration MUST preserve relevant time/frame semantics.

### SCP-116
Disputed geographic membership MUST remain representable.

### SCP-117
Jurisdictional Scope MUST NOT silently transfer across jurisdictions.

### SCP-118
Jurisdiction containment MUST NOT automatically determine normative precedence.

### SCP-119
Temporal applicability MUST remain distinguishable from other temporal roles.

### SCP-120
Enactment time MUST NOT automatically become applicability time.

### SCP-121
Discontinuous temporal Scope MUST remain representable.

### SCP-122
Historical Scope MUST preserve relevant historical definitions/frames.

### SCP-123
Category drift MUST NOT silently redefine historical Scope.

### SCP-124
Population Scope MUST NOT silently generalize.

### SCP-125
Version-family membership MUST NOT establish behavioral equivalence.

### SCP-126
Validity at separated versions MUST NOT automatically imply validity at intermediate versions.

### SCP-127
Material similarity MUST NOT establish applicability equivalence.

### SCP-128
Parameter Scope MUST NOT be extrapolated without justification.

### SCP-129
Domain of definition MUST remain distinguishable from Claim Scope.

### SCP-130
Model input acceptance MUST NOT establish validation Scope.

### SCP-131
Display, operational, calibrated and validated Measurement ranges MUST remain distinguishable.

### SCP-132
Interpretive Scope MUST remain distinguishable from applicability Scope where material.

### SCP-133
Semantic/definition frame SHOULD remain recoverable where necessary for Scope interpretation.

### SCP-134
Hypothetical Scope MUST remain distinguishable from actual Scope.

### SCP-135
Future Scope MUST NOT imply demonstrated future validity.

### SCP-136
Scope intersection MUST NOT automatically license Claim composition.

### SCP-137
Scope union requires compatible Claim semantics and aligned relevant constraints.

### SCP-138
Cross-source Scope constraints MUST NOT automatically be composed into one asserted Scope.

### SCP-139
Temporal/dimensional coupling MUST survive Scope composition.

### SCP-140
Lossy Scope projection MUST remain detectable.

### SCP-141
Projection of multidimensional Scope MUST NOT permit later reconstruction as though lost dependencies were preserved.

### SCP-142
Lossy Scope projection SHOULD preserve derivation provenance where material.

### SCP-143
Decomposition/recomposition MUST NOT fabricate Scope members/configurations.

### SCP-144
Scope containment MUST NOT automatically determine validity transfer.

### SCP-145
Narrow-to-broad transfer requires justification.

### SCP-146
Broad-to-narrow transfer requires compatible Claim semantics.

### SCP-147
Scope overlap MUST NOT be treated as equivalence.

### SCP-148
Scope equivalence MUST remain distinguishable from Record, provenance, role and temporal identity.

### SCP-149
Scope similarity MUST NOT establish transferability.

### SCP-150
Scope compatibility MUST NOT establish equivalence or applicability.

### SCP-151
Scope mapping MUST NOT automatically establish equivalence.

### SCP-152
Lossy mapping MUST NOT be used as exact set mapping.

### SCP-153
Scope mismatch MUST remain detectable.

### SCP-154
Scope alignment SHOULD precede contradiction judgment where material.

### SCP-155
Different Scope MUST NOT automatically be labeled contradiction.

### SCP-156
Claim falsity, inapplicability, non-assertion and unknown applicability MUST remain distinguishable.

### SCP-157
Negation/quantifier order MUST remain preserved.

### SCP-158
Structural nesting MUST NOT automatically establish Scope inheritance.

### SCP-159
Explicit, inherited, inferred and reconstructed Scope MUST remain distinguishable.

### SCP-160
Scope MAY inherit dimension-by-dimension only where semantics justify it.

### SCP-161
Unknown/incompatible inheritance MUST NOT be treated as valid inheritance.

### SCP-162
Material heading/table/figure/footnote Scope MUST remain preservable.

### SCP-163
Evidence citation Scope MUST NOT automatically constrain or broaden author Claim Scope.

### SCP-164
Reported Scope MUST remain distinguishable from endorsed/supporting Scope.

### SCP-165
Material inherited Scope MUST travel with extracted knowledge or remain resolvably referenced.

### SCP-166
Canonicalization MUST NOT remove material Scope.

### SCP-167
Deduplication MUST NOT automatically union Scope.

### SCP-168
Identical Claim text MUST NOT imply identical scoped Claim semantics.

### SCP-169
Scope MAY participate in Claim/Record identity criteria consistently with `014`.

### SCP-170
Evidence support MAY be Scope-conditioned.

### SCP-171
Uncertainty MAY be Scope-conditioned.

### SCP-172
Risk MAY be Scope-conditioned.

### SCP-173
Verification MAY be Scope-conditioned.

### SCP-174
Conflict MAY be Scope-conditioned.

### SCP-175
Scope partitioning MUST remain representable without mandatory Core Entity proliferation.

### SCP-176
Derived Claim Scope MUST NOT exceed what premises/inference justify.

### SCP-177
Multi-premise inference MUST remain within justified joint domain.

### SCP-178
Non-overlapping required premise Scopes MUST NOT receive fabricated common Scope.

### SCP-179
Inference-specific Scope transformation MUST be explicit/justifiable.

### SCP-180
Derived Scope provenance MUST remain distinguishable from Source-stated Scope.

### SCP-181
Extrapolation beyond supported Scope MUST remain identifiable.

### SCP-182
Interpolation MUST NOT automatically establish validity.

### SCP-183
Safety-critical interpolation MUST NOT be assumed without support.

### SCP-184
Cross-Scope invariance MUST NOT imply universal invariance.

### SCP-185
Scope transferability MAY remain conditional, partial, uncertain or unknown.

### SCP-186
Scope transfer MUST remain distinguishable from Context transfer.

### SCP-187
Taxonomy, similarity, containment, mapping, inheritance or Evidence selection MUST NOT be laundered into broad applicability.

### SCP-188
Subset validity MUST NOT automatically become superset validity.

### SCP-189
Regional validity MUST NOT automatically become superregional validity.

### SCP-190
Temporal validity MUST NOT automatically expand to containing era.

### SCP-191
Version validity MUST NOT automatically expand to version family.

### SCP-192
Subpopulation validity MUST NOT automatically expand to broader population.

### SCP-193
Sample Result MUST NOT automatically become population Claim.

### SCP-194
Scope semantic role MUST NOT silently change during transformation.

### SCP-195
Limited Evidence MUST NOT create unsupported exclusivity.

### SCP-196
Finite Evidence MUST NOT create unsupported universal quantification.

### SCP-197
Existential support MUST NOT become universal support.

### SCP-198
No Evidence for Scope X MUST NOT establish non-applicability to X.

### SCP-199
Natural-language Scope ambiguity MUST remain representable.

### SCP-200
Ambiguous modifier/coordination attachment MUST NOT be silently resolved when material.

### SCP-201
Implicit Scope MUST remain distinguishable from explicit Scope.

### SCP-202
Domain defaults MUST NOT be represented as Source-stated Scope.

### SCP-203
Normalization MUST NOT invent universe, boundary, quantifier, exclusivity, precision or semantic role.

### SCP-204
Normalization MUST preserve correlated Scope dimensions.

### SCP-205
Historical categories MUST NOT silently normalize into modern exact equivalents.

### SCP-206
Translation MUST preserve materially relevant Scope semantics.

### SCP-207
Scope Fidelity MUST remain distinguishable from Scope truth.

### SCP-208
Scope Fidelity MUST remain distinguishable from overall Claim Fidelity.

### SCP-209
Scope loss, contamination, conflation, hallucination, overgeneralization, overspecification and drift MUST remain detectable failure classes.

### SCP-210
Unknown Scope MUST be preferred over unsupported Scope fabrication.

### SCP-211
Scope role drift MUST remain detectable even when extension does not change.

### SCP-212
Tuple/configuration drift MUST remain detectable.

### SCP-213
Open-world Scope MUST NOT silently become closed-world Scope.

### SCP-214
Scope definition/frame drift MUST remain detectable.

### SCP-215
Summary MUST NOT broaden, narrow or role-shift Scope without justification.

### SCP-216
Compression MUST preserve material universe, role, boundaries, tuples, coupling, uncertainty and provenance.

### SCP-217
Safety statements MUST preserve material Scope.

### SCP-218
Independent parameter ranges MUST NOT automatically define a safe multidimensional region.

### SCP-219
Uncertain safety boundaries MUST NOT become exact safe thresholds.

### SCP-220
Risk Scope MUST NOT silently generalize.

### SCP-221
Procedure Scope MUST remain recoverable.

### SCP-222
Decision-rule Scope MUST NOT silently expand.

### SCP-223
Model validity Scope MUST remain distinguishable from accepted input domain.

### SCP-224
Action Scope MUST remain compatible with `008`.

### SCP-225
Event Scope MUST remain compatible with `009`.

### SCP-226
Result Scope MUST remain compatible with `010`.

### SCP-227
State Scope MUST remain compatible with `011`.

### SCP-228
Process Scope MUST remain compatible with `012`.

### SCP-229
Relation Scope MUST remain compatible with `013`.

### SCP-230
Identity Scope MUST remain compatible with `014`.

### SCP-231
Scope/Context coupling MUST remain compatible with `015`.

### SCP-232
Meta-Scope MUST remain distinguishable from Scope of the meta-Claim.

### SCP-233
Partial verification MUST NOT become global verification.

### SCP-234
Authority/competence Scope MUST remain distinguishable from Claim applicability Scope.

### SCP-235
Retrieval/filter Scope MUST NOT become Claim semantic Scope.

### SCP-236
Presentation Scope MUST NOT become Claim applicability Scope automatically.

### SCP-237
Access-control Scope MUST remain distinguishable from knowledge applicability Scope.

### SCP-238
Validator PASS MUST NOT establish Scope truth, Claim truth, Evidence sufficiency or safety.

### SCP-239
Logically impossible Scope SHOULD remain detectable.

### SCP-240
Circular Scope references MUST NOT automatically be treated as resolved.

### SCP-241
Recursive Scope semantics MUST be sufficiently defined where recursion is used.

### SCP-242
Material Scope SHOULD remain human-interpretable offline.

### SCP-243
Material Scope qualifiers SHOULD be co-located with constrained knowledge when separation creates significant risk of offline loss or dangerous misinterpretation.

### SCP-244
Safety-critical Scope MUST NOT depend solely on opaque or fragile detached references.

### SCP-245
Carrier technology MUST NOT determine Scope semantics.

---

# 253. Stress-test framework

`016-SCOPE` MUST remain robust against at least:

1. Scope vs Universe;
2. local universe;
3. universe drift;
4. nested universe;
5. Scope vs Quantifier;
6. most/all/some/none;
7. generic vs universal;
8. member-level instantiation;
9. aggregate vs member;
10. ecological fallacy;
11. atomistic fallacy;
12. level of analysis;
13. Scope vs Context;
14. coupled Scope + Context;
15. Scope vs Preconditions;
16. conditional propositions;
17. Scope vs State;
18. Scope vs Class;
19. eligibility Scope;
20. recruited Scope;
21. observed Scope;
22. analyzed Scope;
23. target population;
24. sample Scope;
25. selection bias;
26. attrition;
27. missing data;
28. survivorship;
29. denominator loss;
30. Evidence Scope;
31. Evidence-selection Scope;
32. Scope vs Provenance;
33. membership provenance;
34. exception provenance;
35. provenance laundering;
36. stated vs demonstrated;
37. intended vs realized;
38. designed vs tested;
39. tested vs validated;
40. regulatory vs scientific;
41. safety vs efficacy;
42. normative vs empirical;
43. semantic Scope role;
44. multidimensional Scope;
45. correlated dimensions;
46. tuple Scope;
47. Cartesian-product hallucination;
48. bounding-box hallucination;
49. convex-hull hallucination;
50. endpoint interpolation;
51. non-contiguous Scope;
52. holes/exceptions;
53. Boolean Scope;
54. operator precedence;
55. nested quantifiers;
56. inclusion;
57. exclusion;
58. outside Scope;
59. unknown Scope;
60. missing Scope;
61. open Scope;
62. closed Scope;
63. open-world membership;
64. closed-world membership;
65. partial closure;
66. closure leakage;
67. all-known vs all-existing;
68. empty Scope;
69. vacuous truth;
70. singleton Scope;
71. intensional Scope;
72. extensional Scope;
73. snapshot equality;
74. dynamic Scope;
75. Identity dependency;
76. Relation dependency;
77. State dependency;
78. Event dependency;
79. Measurement dependency;
80. dependency uncertainty/dispute;
81. operational definition;
82. same-label/different-Scope;
83. taxonomy/frame;
84. vague Scope;
85. approximate boundary;
86. inclusive/exclusive boundary;
87. membership uncertainty;
88. component uncertainty;
89. spatial Scope;
90. historical geography;
91. boundary migration;
92. disputed territory;
93. jurisdiction;
94. overlapping jurisdiction;
95. temporal Scope;
96. temporal roles;
97. retroactivity;
98. discontinuous time;
99. historical Scope;
100. category drift;
101. population Scope;
102. version Scope;
103. non-contiguous versions;
104. material Scope;
105. parameter Scope;
106. domain-of-definition;
107. Model validation Scope;
108. Measurement ranges;
109. interpretive Scope;
110. semantic definition Scope;
111. hypothetical Scope;
112. future Scope;
113. intersection;
114. union;
115. cross-source composition;
116. temporal composition;
117. projection;
118. lossy projection reconstruction;
119. projection provenance;
120. decomposition/recomposition;
121. containment;
122. narrow-to-broad transfer;
123. broad-to-narrow transfer;
124. overlap;
125. equivalence;
126. similarity;
127. compatibility;
128. mapping;
129. lossy mapping;
130. mismatch;
131. contradiction alignment;
132. Scope difference vs conflict;
133. Scope vs negation;
134. negation/quantifier order;
135. inheritance;
136. explicit vs inherited;
137. dimension inheritance;
138. heading Scope;
139. table Scope;
140. figure Scope;
141. footnote Scope;
142. citation Scope;
143. quoted Scope;
144. extraction;
145. canonicalization;
146. deduplication;
147. automatic Scope union;
148. Claim Identity;
149. Scope-sensitive Evidence;
150. Scope-sensitive uncertainty;
151. Scope-sensitive risk;
152. Scope-sensitive verification;
153. Scope-sensitive conflict;
154. Scope partitioning;
155. inference Scope;
156. multi-premise inference;
157. empty intersection;
158. inference transformation;
159. derived Scope provenance;
160. extrapolation;
161. interpolation;
162. safety interpolation;
163. invariance;
164. transferability;
165. Scope vs Context transfer;
166. laundering;
167. taxonomic laundering;
168. geographic laundering;
169. temporal laundering;
170. version laundering;
171. population laundering;
172. sample laundering;
173. cross-role laundering;
174. "only";
175. "all";
176. "some";
177. no-Evidence;
178. natural-language ambiguity;
179. modifier attachment;
180. coordination ambiguity;
181. implicit subject;
182. defaults;
183. normalization;
184. historical normalization;
185. translation;
186. Scope Fidelity;
187. Scope Fidelity vs Claim Fidelity;
188. Scope loss;
189. contamination;
190. conflation;
191. hallucination;
192. overgeneralization;
193. overspecification;
194. underspecification;
195. Scope drift;
196. role drift;
197. tuple drift;
198. closure drift;
199. definition drift;
200. summary;
201. compression;
202. safety Scope;
203. multidimensional safety envelope;
204. uncertain safety boundary;
205. Risk Scope;
206. Procedure Scope;
207. Decision Scope;
208. Model Scope;
209. Action Scope;
210. Event Scope;
211. Result Scope;
212. State Scope;
213. Process Scope;
214. Relation Scope;
215. Identity Scope;
216. Context compatibility;
217. Meta-Scope;
218. verification Scope;
219. authority/competence Scope;
220. retrieval Scope;
221. presentation Scope;
222. access-control Scope;
223. impossible Scope;
224. circular Scope;
225. recursive Scope;
226. offline preservation;
227. offline qualifier co-location;
228. detached legend loss;
229. carrier neutrality;
230. machine validation;
231. Scope-role ontology collapse;
232. Entity Explosion;
233. cross-standard collision.

Stress tests do not themselves create Core Entities.

If a stress test reveals a necessary fundamental rule, that rule MUST be incorporated into normative architecture.

---

# 254. Принцип сохранения

При конфликте между удобством обобщения и честностью representation предпочтение отдаётся честности.

    unknown Scope
    > invented Scope

    local universe
    > false global universe

    open Scope
    > invented closed Scope

    partial extension
    > fabricated complete extension

    observed Scope
    > falsely universalized Claim Scope

    tested Scope
    > invented validated Scope

    Evidence Scope
    > falsely inherited Claim Scope

    sample
    > false population generalization

    aggregate Result
    > false member-level Claim

    narrow Scope
    > unsupported broad Scope

    vague boundary
    > invented exact boundary

    uncertain membership
    > invented certain membership

    correlated configuration
    > fabricated Cartesian product

    preserved dependency
    > reconstructed dependency after lossy projection

    validated points
    > fabricated continuous validity region

    Scope + Context coupling
    > false independent constraints

    historical Scope
    > modern category substitution

    specific version
    > version-family universality

    separate Source constraints
    > fabricated combined Scope

    inherited Scope
    > incompatible automatic inheritance

    Scope similarity
    > invented equivalence

    Scope compatibility
    > invented applicability

    finite Evidence
    > invented universal quantifier

    Evidence only in X
    > invented "only X"

    no Evidence outside X
    > invented non-applicability outside X

    partial verification
    > false global verification

    Scope-conditioned risk
    > misleading global risk

    high Scope Fidelity
    > false claim of overall semantic fidelity

    preserved unknown/disputed dependency
    > invented certain membership

---

# 255. Итоговая формула

В компактной форме:

    Scope
    → к каким членам,
      случаям,
      диапазонам
      или конфигурациям
      относится representation
      в определённой semantic role

    Universe
    → внутри какого domain
      Scope интерпретируется

    Quantifier
    → как proposition
      распространяется по Scope

    Context
    → при каких условиях
      representation рассматривается

    Sample
    → какие элементы
      непосредственно отобраны/наблюдались

    Evidence
    → чем representation поддерживается

И:

    Scope
    ≠ Universe

    Scope
    ≠ Quantifier

    Scope
    ≠ Context

    Scope
    ≠ Preconditions

    Scope
    ≠ State

    Scope
    ≠ Class

    Scope
    ≠ Sample

    Scope
    ≠ Evidence

    Scope
    ≠ Provenance

    Scope
    ≠ applicability proof

Также:

    x ∈ Scope
    ≠ Claim(x) automatically

    Scope containment
    ≠ Claim transfer automatically

    aggregate Claim
    ≠ member Claim

    member Evidence
    ≠ population Claim

    Sample Scope
    ≠ Population Scope automatically

    Evidence Scope
    ≠ Claim Scope automatically

    Tested Scope
    ≠ Validated Scope

    Tested Scope
    ≠ Maximum Valid Scope

    Outside Scope
    ≠ Claim false

    Unknown Scope
    ≠ Universal Scope

    Missing Scope
    ≠ Empty Scope

    Known members
    ≠ Complete extension

    No known membership
    ≠ Non-membership

    Intensional Scope
    ≠ Extensional snapshot

    Multidimensional Scope
    ≠ Cartesian product

    Valid component values
    ≠ Valid combinations

    Valid endpoints
    ≠ Valid interval

    Lossy projection
    ≠ recoverable original dependency automatically

    Scope similarity
    ≠ Scope equivalence

    Scope compatibility
    ≠ Claim applicability

    Narrow validity
    ≠ Broad validity

    Shared Scope safeguards
    ≠ one mandatory Scope ontology

    Scope Fidelity
    ≠ Scope truth
    ≠ overall Claim Fidelity

---

# 256. Центральный принцип

> **Сохранить Scope — значит сохранить не просто список объектов или диапазон, а точную семантическую границу знания: к чему оно относится, в какой роли, внутри какого universe, с каким quantifier, по каким определениям и ограничениям, для каких связанных конфигураций и при какой неопределённости; не позволяя системе превращать sample в population, aggregate в individual Claim, subset в superset, Evidence Scope в Claim Scope, open world в closed world, отдельные допустимые значения в допустимые комбинации, ограниченное знание в универсальное, отсутствие Evidence в отрицание применимости, потерянную зависимость — в восстановленную без основания, а неизвестную границу — в выдуманную точную границу.**

---

# 257. Статус

**016-SCOPE v0.1 — ACCEPTED / BASELINE**

Стандарт определяет архитектурные требования к представлению области применимости, охвата и границ знания в Энциклопедии цивилизации.

Стандарт является частью FOUNDATION и должен интерпретироваться совместно с CORE MODEL и связанными стандартами проекта.

Будущие расширения MAY уточнять:

- machine-readable Scope schema;
- formal constraint representation;
- Scope validation;
- Scope algebra;
- quantifier model;
- applicability model;
- Scope transfer model;
- domain-specific Scope profiles;

при условии сохранения инвариантов настоящего стандарта.
