# M13 — algebra basics: source-passage and rights review

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Records: `CLM-ALGEBRA_BASICS-A/B/C@1`, `EU-ALGEBRA_BASICS-A/B/C@1`, `SRC-ALGEBRA_BASICS@1`
Status: **source-passage desk review; rights HOLD; no canonical records or D/E/B assessments changed.**

## 1. Why this slice was selected

The full-corpus linkage census flags all three Evidence Use records in `algebra-basics` as generic-material descriptions. The Source record is also one of the sentence-like Source identity candidates: its current identity field reads “Алгебра — базовый язык для записи и преобразования количественных зависимостей,” which is a topical statement, not a bibliographic identity.

The Claim/EU/Source links are structurally valid and version 1. The issue is content traceability and Source identity/rights, not a broken reference.

## 2. Claim-specific passage review

Canonical Source URI:
https://openstax.org/details/books/college-algebra-2e

Bibliographic identity on the publisher's page:
Jay Abramson, *College Algebra 2e*, OpenStax, publication date 21 December 2021. The current section page also carries a 12 June 2026 copyright/update footer.

### Claim A — `CLM-ALGEBRA_BASICS-A@1`

Claim: “Алгебраические выражения состоят из чисел, переменных и операций над ними.”

Direct passage located:
- *College Algebra 2e*, §1.1 “Real Numbers: Algebra Essentials”, subsection “Evaluating Algebraic Expressions”.
- The passage defines an algebraic expression as constants and variables joined by addition, subtraction, multiplication and division, and gives examples such as (x+5), ((4/3)\pi r^3), and a radical expression.

Assessment:
- Direct support for the core definition.
- The Claim's phrase “числа” is slightly broader/less exact than the source's “constants and variables”; constants may be numbers, but variables are not numbers. Suggested wording should preserve the distinction between constants and variables.
- Proposed locator: §1.1, “Evaluating Algebraic Expressions”, definition paragraph and examples immediately following it.
- Desk-review passage status: **DIRECT, wording precision note**.

### Claim B — `CLM-ALGEBRA_BASICS-B@1`

Claim: “Уравнение задаёт условие равенства двух выражений и решается относительно неизвестных при допустимых преобразованиях.”

Direct passages located:
- §1.1, subsection “Formulas”: defines an equation as a mathematical statement that two expressions are equal; explains that solutions are values making the equation true and are found using properties of real numbers and other results.
- §2.2 “Linear Equations in One Variable”: describes solving linear equations using standard algebraic properties and checking rational-equation solutions in the original equation to avoid undefined expressions/zero denominators.

Assessment:
- Direct support for the definition and for solving in the textbook's covered equation classes.
- “Решается относительно неизвестных” is acceptable as introductory shorthand, but the statement should not imply that every equation has a solution, one solution, or a solution obtainable by unrestricted transformations. Domain restrictions and equivalence-preserving transformations matter.
- Proposed locator: §1.1 “Formulas”; §2.2 “Linear Equations in One Variable”, especially the rational-equation verification rule.
- Desk-review passage status: **DIRECT, with a mathematical boundary note**.

### Claim C — `CLM-ALGEBRA_BASICS-C@1`

Claim: “Функция связывает элементы области определения с элементами области значений по заданному правилу.”

Direct passage located:
- §3.1 “Functions and Function Notation”, “Determining Whether a Relation Represents a Function”: relation/domain/range discussion and the definition that each possible input value leads to exactly one output value.
- The same section distinguishes input/domain from output/range and explains the one-output-per-input condition.

Assessment:
- Direct support for the core definition.
- Recommended precision: explicitly state that each input in the function's domain is assigned exactly one output; outputs need not be unique across different inputs.
- Proposed locator: §3.1, “Determining Whether a Relation Represents a Function” and “Function” definition.
- Desk-review passage status: **DIRECT, with a precision note**.

## 3. Rights and permitted-use screen — blocking issue

The OpenStax page's own attribution section states:
- the book is licensed CC BY-NC-SA, requiring attribution and ShareAlike for reuse/derivatives and limiting reuse to noncommercial purposes;
- OpenStax explicitly states that the book may not be used for training large language models or otherwise ingested into large language models or generative-AI offerings without prior written permission;
- the page identifies the authors, publisher, publication date and section URL.

This is not a minor footnote. The encyclopedia's future use model and any AI-assisted/AI-facing features must be checked against the explicit restriction. This review does not grant permission and must not be interpreted as authorization to ingest, reproduce, adapt, train on, or redistribute OpenStax material within the project.

Required path before any canonical adoption:
1. obtain and retain written OpenStax permission covering the intended project use, including any AI/LLM or generative-AI use that applies; **or**
2. replace this Source with a rights-compatible source whose terms permit the intended use, then repeat the passage-level review and bibliographic/rights check.

A bibliographic citation or a public URL is not a substitute for permission.

## 4. Source identity remediation proposal

The current `source_identity` is not a title/issuer identity. If this source is retained after rights clearance, the bibliographic identity should be represented along the lines of:

- Author: Jay Abramson
- Title: *College Algebra 2e*
- Publisher: OpenStax
- Publication date: 2021-12-21
- Relevant sections: §§1.1, 2.2, 3.1
- Canonical book URI: https://openstax.org/details/books/college-algebra-2e
- Section URIs: use the exact section pages listed in the authorized Evidence Use records.

Do not make this correction until a bounded authorization covers the Source metadata and EU changes. If the source is replaced for rights reasons, do not first normalize metadata and then leave an unusable source in the chain.

## 5. Proposed Claim wording refinements (editorial proposals only)

- A: “Алгебраическое выражение — запись, состоящая из констант и переменных, соединённых арифметическими операциями.” Check the intended curriculum scope before adopting.
- B: “Уравнение — математическое утверждение о равенстве двух выражений; его решения — значения переменных, при которых равенство истинно.” Keep solving methods and domain restrictions in supporting explanation rather than implying unrestricted transformations.
- C: “Функция — соответствие, которое каждому допустимому входному значению из области определения ставит в соответствие ровно одно выходное значение из области значений.” Preserve that different inputs may share the same output.

These proposals require editorial review and are not canonical changes.

## 6. Disposition

| Item | Desk-review result |
|---|---|
| A passage support | Direct, wording precision note |
| B passage support | Direct, solution/domain boundary note |
| C passage support | Direct, function uniqueness note |
| Generic EU locators in canonical records | Still absent |
| Source identity | Sentence-like; bibliographic correction proposed |
| Rights | **HOLD — explicit OpenStax LLM/generative-AI restriction and CC BY-NC-SA conditions** |
| Canonical Claim/EU/Source changes | 0 |
| D/E/B score changes | 0 |
| Independent specialist review | 0 |
| Release/Human View clearance | 0 |

All three Claims remain **HOLD**. The passages appear to support their introductory mathematical propositions, but the evidence cannot be adopted into the project's canonical/AI-facing chain until the rights path is resolved and exact locators are recorded under a separate bounded authorization.
