# M13 — Unassessed Risk Content Screen — Package 20

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Queue source revision: `9448f860b043844ed4adb0f0eb67f7060569a171`
Queue workflow run: `43678619500`
Queue artifact: `14147855414` (`m13-review-queue-9448f860b043844ed4adb0f0eb67f7060569a171`)
Artifact SHA-256: `24d45fb7158020d72b887ec0fccfa7d976b62610988fdb35f9683efef2f4b439`

## 1. Fresh queue and selection integrity

Package 20 is exactly Lane 1 of the queue generated on the branch HEAD containing the final Package 19 review report. It was not selected from an older artifact.

- 4,834 records scanned; 1,494 Claims inventoried.
- 477 previously screened Claim IDs excluded.
- 17 unreconciled holdout Claims excluded; 15 overlap with the reviewed holdout set; 479 unique exclusions across those two sets.
- 232 candidates remained in the unassessed-risk screening queue.
- 100 Claims selected in five lanes of 20; all selected IDs are unique; no unfilled slots.
- All 20 Package 19 Claim IDs are present in the 477 previously-screened exclusion set. None appears in the 100 selected Claims.
- Lane 1 contains 20 unique Claims and 22 Evidence Use links. The artifact contains 100 evidence packets overall.

## 2. Chain verification and review boundary

The 20 Claim records, 22 linked Evidence Use records, and 10 referenced Source records were inspected at version 1. The two additional Evidence Use links provide a second source chain for each Rehabilitation Claim. Every inspected Evidence Use `claim_ref` and `source_ref` resolves to the expected version-1 record; Claim provenance points to the corresponding Source.

The two Rehabilitation sources are separate WHO publications (Q&A and fact sheet), but they are not independent institutions. Their evidentiary independence should not be overstated.

All 20 Claims remain `UNASSESSED` in the risk queue. No D/E/B score was assigned or inferred. No canonical Claim, Evidence Use, Source, Context, Scope, Relation, or risk metadata was changed. Existing `published` / `complete` fields are not treated as new publication authorization.

## 3. Results

**6 Claims have direct conceptual support in the registered source material, subject to exact locator capture. 14 Claims remain partial because the registered source is a broad hub, a broken URL, incomplete for part of the statement, or subject to an AI-use rights restriction.**

| Claim ID | Existing evidence chain | Review result | Required follow-up / best locator |
|---|---|---|---|
| `CLM-PROGRAMMING_LANGUAGES_BASICS-B` | `EU-PROGRAMMING_LANGUAGES_BASICS-B` → `SRC-PROGRAMMING_LANGUAGES_BASICS` (NIST ITL) | PARTIAL | The registered NIST ITL landing page does not establish interpreter versus compiler execution. Candidate: Charlie Murphy, *A Practical Introduction to Programming Language Design*, “Why Build an Interpreter?”; the section distinguishes direct interpretation from compilation to another language, and explains that real implementations may combine interpreters, bytecode and JIT compilation: `https://www.cs.montana.edu/users/murphy/books/pl-design/foundations/why-interpreter.html`. The Claim should avoid implying that a language itself is exclusively interpreted or compiled. |
| `CLM-PROGRAMMING_LANGUAGES_BASICS-C` | `EU-PROGRAMMING_LANGUAGES_BASICS-C` → same NIST ITL Source | PARTIAL | The registered source is too broad for computation models and abstraction mechanisms. Candidate: Murphy, *A Practical Introduction to Programming Language Design*, “The Paradigm Branches,” which compares imperative, functional, declarative and object-oriented models and explains the different abstractions they make available: `https://www.cs.montana.edu/users/murphy/books/pl-design/foundations/paradigms.html`. Add this as a specific Source and locator. |
| `CLM-PUBLIC_ADMINISTRATION_BASICS-A` | `EU-PUBLIC_ADMINISTRATION_BASICS-A` → `SRC-PUBLIC_ADMINISTRATION_BASICS` (OECD Public Governance) | PARTIAL | The registered OECD `/gov/` page is a broad public-governance hub, not a pinpoint definition of public administration or public-service delivery. Add an OECD Government at a Glance 2025 chapter/section on public services and public employment, or a specific OECD public-governance definition, with exact section and scope. |
| `CLM-PUBLIC_ADMINISTRATION_BASICS-B` | `EU-PUBLIC_ADMINISTRATION_BASICS-B` → same OECD Source | PARTIAL | The broad OECD hub does not establish the legal/administrative authority and procedure clause. Add a specific public-administration or administrative-law source that identifies statutory mandates, delegated authority, due process and procedural requirements. Avoid implying that all jurisdictions use identical administrative structures. |
| `CLM-PUBLIC_FINANCE_BASICS-B` | `EU-PUBLIC_FINANCE_BASICS-B` → `SRC-PUBLIC_FINANCE_BASICS` (IMF Fiscal Policies) | DIRECT CONCEPTUAL SUPPORT | The registered IMF “Fiscal Policies” overview explicitly states that fiscal policy affects macroeconomic stability, growth and income distribution. Record the exact “Overview” locator (paragraph 1). |
| `CLM-PUBLIC_POLICY_BASICS-B` | `EU-PUBLIC_POLICY_BASICS-B` → `SRC-PUBLIC_POLICY_BASICS` (OECD Government at a Glance 2025) | DIRECT CONCEPTUAL SUPPORT | OECD, *Government at a Glance 2025*, section 5.2 “Public policy evaluation,” states that evaluations provide evidence on what works, why, for whom and under what circumstances. Record section 5.2, paragraph 1. |
| `CLM-PUBLIC_POLICY_BASICS-C` | `EU-PUBLIC_POLICY_BASICS-C` → same OECD Source | PARTIAL | OECD section 5.2 supports evaluation of effectiveness, informed decision-making and delivery of intended outcomes, but the registered passage does not establish the full monitoring clause or identifying unintended consequences. Add an evaluation-method source that explicitly covers comparison against objectives, monitoring indicators and intended/unintended effects, or narrow the Claim to the OECD-supported proposition. |
| `CLM-QUALITY_MANAGEMENT_BASICS-A` | `EU-QUALITY_MANAGEMENT_BASICS-A` → `SRC-QUALITY_MANAGEMENT_BASICS` (ISO Quality Management Principles) | PARTIAL — RIGHTS HOLD | The registered ISO source is subject to ISO's explicit AI/ML-use restriction, including use in prompts and generated responses, absent written permission. Do not use this content in the AI-assisted evidence workflow without written permission. Candidate replacement: NIST, “About the Baldrige Excellence Framework,” which describes an organization-wide management framework and results: `https://www.nist.gov/baldrige/about-baldrige-excellence-framework`. The Claim should be scoped to the replacement source's actual framework, not presented as an ISO definition. |
| `CLM-QUALITY_MANAGEMENT_BASICS-B` | `EU-QUALITY_MANAGEMENT_BASICS-B` → same ISO Source | PARTIAL — RIGHTS HOLD | Same ISO AI-use restriction. Candidate replacement: NIST Baldrige, sections on systems perspective, leadership, workforce, operations, measurement/analysis and results. This is not a substitute for ISO's seven named principles; either obtain permission or reframe the Claim around the NIST framework. |
| `CLM-QUALITY_MANAGEMENT_BASICS-C` | `EU-QUALITY_MANAGEMENT_BASICS-C` → same ISO Source | PARTIAL — RIGHTS HOLD | Same ISO AI-use restriction. Candidate replacement: NIST Baldrige Organizational Profile and Results criteria, which address organizational context, processes, performance measures and results. Add a separate source for applicable legal/contractual requirements if those remain in the Claim. |
| `CLM-QUANTUM_MECHANICS_BASICS-A` | `EU-QUANTUM_MECHANICS_BASICS-A` → `SRC-QUANTUM_MECHANICS_BASICS` (NIST Quantum Information Science) | PARTIAL — SOURCE URL FAILURE | The registered URI `https://www.nist.gov/topics/quantum-information-science` returns 404. No content from that URL can support the Claim until a working canonical source is identified. Candidate: MIT OpenCourseWare 8.04 Quantum Physics I, introductory lectures on quantum states, wave functions and probability/Born rule; add an accessible current course/source and exact lecture locator. |
| `CLM-QUANTUM_MECHANICS_BASICS-B` | `EU-QUANTUM_MECHANICS_BASICS-B` → same NIST Source | PARTIAL — SOURCE URL FAILURE | The NIST URI returns 404 and cannot support the classical/quantum distinction. Candidate MIT OCW 8.04 lectures on superposition, states and measurement, or another open university text with exact locators. State the specific non-classical property (e.g. superposition or entanglement) rather than leaving “different from classical description” unbounded. |
| `CLM-QUANTUM_MECHANICS_BASICS-C` | `EU-QUANTUM_MECHANICS_BASICS-C` → same NIST Source | PARTIAL — SOURCE URL FAILURE | The NIST URI returns 404. Candidate MIT OCW 8.04 lectures on observables, measurement and the Born rule, with an exact locator for how predictions depend on the state and measured observable. Clarify whether the Claim is about formal quantum measurement or a general epistemic warning. |
| `CLM-RATIOS_AND_PERCENTAGES-A` | `EU-RATIOS_AND_PERCENTAGES-A` → `SRC-RATIOS_AND_PERCENTAGES` (NIST SP 811, Chapter 7) | DIRECT CONCEPTUAL SUPPORT | NIST Guide to the SI, Chapter 7, section 7.10 (paragraph 1) describes dimension-one quantities defined as ratios of two mutually comparable quantities; section 7.14 provides the detailed convention. Record the exact ratio locator and retain the Claim's condition that division must be defined. |
| `CLM-RATIOS_AND_PERCENTAGES-B` | `EU-RATIOS_AND_PERCENTAGES-B` → same NIST SP 811 Source | DIRECT CONCEPTUAL SUPPORT | NIST Guide to the SI, Chapter 7, section 7.10.2, states that the percent symbol represents the number 0.01 and provides a numerical example. Thus 25 % corresponds to 25 × 0.01 = 0.25. Record section 7.10.2. |
| `CLM-RECORDS_MANAGEMENT_BASICS-A` | `EU-RECORDS_MANAGEMENT_BASICS-A` → `SRC-RECORDS_MANAGEMENT_BASICS` (NARA Records Management 101) | PARTIAL | The registered NARA page is a training hub. It links to “Records Management Fundamentals,” “What is a Federal Record?” and “Permanent and Temporary Records,” but does not itself provide the complete definition of what constitutes a record and all handling/disposition requirements. Add the linked NARA lessons as exact Source records and locators. |
| `CLM-RECORDS_MANAGEMENT_BASICS-B` | `EU-RECORDS_MANAGEMENT_BASICS-B` → same NARA Source | PARTIAL | The NARA hub links to the “Permanent and Temporary Records, Non-Records and Personal Files” tip sheet but does not itself define the retention distinctions. Add that tip sheet as a separate Source and cite the exact definitions. |
| `CLM-RECORDS_MANAGEMENT_BASICS-C` | `EU-RECORDS_MANAGEMENT_BASICS-C` → same NARA Source | PARTIAL | NARA page lines 76–78 explicitly state that General Records Schedules provide disposition authority for common federal records and that agency-specific schedules cover mission records. This directly supports the disposition-authority clause. The lifecycle clause points to a separate “Records Lifecycle” resource but is not explained in the registered page; add the linked lifecycle source and locator before treating the whole Claim as directly supported. |
| `CLM_REHABILITATION_BASICS_B` | `EU_REHABILITATION_BASICS_B` → `SRC_REHABILITATION_BASICS`; plus `EU_P9_REHABILITATION_BASICS_B` → `SRC_WHO_REHABILITATION_FACTSHEET` | DIRECT CONCEPTUAL SUPPORT | WHO “Rehabilitation” Q&A, “What would my rehabilitation look like?” (paragraphs 1–2), explicitly lists exercises/training, assistive products, environmental modifications, education/advice and medicines, with interventions chosen for the person's situation and goals. The WHO fact sheet is a second publication from the same institution, not an independent institutional source. |
| `CLM_REHABILITATION_BASICS_C` | `EU_REHABILITATION_BASICS_C` → `SRC_REHABILITATION_BASICS`; plus `EU_P9_REHABILITATION_BASICS_C` → `SRC_WHO_REHABILITATION_FACTSHEET` | DIRECT CONCEPTUAL SUPPORT | WHO “Rehabilitation” Q&A, “What would my rehabilitation look like?” (paragraph 1), states that a rehabilitation professional assesses the person's situation, defines goals with them, and designs intervention type, intensity and duration to fit that situation. This supports the Claim's boundary that general information does not determine an individual programme. |

## 4. Cross-record, source and rights findings

1. `SRC-QUALITY_MANAGEMENT_BASICS` points to ISO Quality Management Principles. ISO's site-wide notice explicitly restricts use of ISO content for AI/ML, including prompts and generated responses, absent written permission. This source is on RIGHTS HOLD for this AI-assisted workflow. NIST Baldrige is a candidate alternative but is not equivalent to ISO's seven named principles.
2. `SRC-QUANTUM_MECHANICS_BASICS` points to a NIST URL that currently returns 404. Treat it as an unavailable source, not as evidence. A working canonical URL and precise quantum-mechanics reference are required.
3. `SRC-PROGRAMMING_LANGUAGES_BASICS` identifies the NIST ITL home page, which is not a specific programming-language source. Replace/supplement with exact sections on syntax/semantics, implementation, interpretation/compilation and programming paradigms.
4. `SRC-PUBLIC_ADMINISTRATION_BASICS` identifies the OECD public-governance hub, not a specific definition or administrative-law source.
5. `SRC-RECORDS_MANAGEMENT_BASICS` is a useful NARA training hub, but the Claim-level evidence requires its linked Federal Record, Permanent and Temporary Records, Records Schedule and Records Lifecycle materials as separate precise sources.
6. `SRC-RATIOS_AND_PERCENTAGES` uses a descriptive identity rather than the full publication title, “NIST Guide to the SI, Chapter 7: Rules and Style Conventions for Expressing Values of Quantities.”
7. The two Rehabilitation chains use two WHO publications. They are distinct documents but not independent institutions; retain that qualification in any evidence-independence assessment.
8. All Evidence Use descriptions are generic and omit exact passage locators. A structurally valid Claim → Evidence Use → Source chain does not by itself establish complete substantive support.

## 5. Decision

- 20 Claim → Evidence Use → Source chains structurally resolve.
- 6 Claims have direct conceptual support in registered sources, subject to exact locator capture.
- 14 Claims remain partial and require exact sources/locators, wording or scope clarification, or rights clearance.
- The three Quality Management Claims are on RIGHTS HOLD for AI-assisted use of the registered ISO content absent written permission.
- No D/E/B scores assigned.
- No canonical records modified.
- No publication, release, or public-pilot approval granted.
- Package 20 closes only this 20-Claim screening pass. The next package must come from a newly generated queue after this commit, not from the current artifact.
