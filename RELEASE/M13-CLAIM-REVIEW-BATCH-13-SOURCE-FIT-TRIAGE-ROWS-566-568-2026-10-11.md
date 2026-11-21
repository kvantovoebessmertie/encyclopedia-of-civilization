# M13 Batch 13 — source-fit review checkpoint (rows 566–568)

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **partial review; Batch 13 not complete**

Scores use the M13 rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). No canonical records changed.

## 1. `CLM-FORMAL_METHODS_BASICS-A` — **D1 / E1 / B2**

**Claim:** Formal methods use mathematically rigorous techniques for specifying, designing, and verifying software and hardware systems.

**Source check:** NASA Langley’s “What is Formal Methods?” states this almost verbatim and explains that formal specifications are well-formed statements in mathematical logic, with verification performed by rigorous deductions (https://shemesh.larc.nasa.gov/fm/fm-what.html, “What is Formal Methods?”, paragraphs 1–2). The claim is well supported in substance.

**Assessment:** This is a definition, not yet an explanation of how specifications or verification work (D1). The stored EU says only that the source is used within the context and limitations and provides no passage locator (E1). The claim scopes the domain to software and hardware but omits that the techniques and tools vary by application (B2).

**Disposition:** Add a pinpoint to the NASA definition and, if the introductory scope allows, a short distinction between formal specification and formal verification.

## 2. `CLM-FORMAL_METHODS_BASICS-B` — **D2 / E1 / B2**

**Claim:** Model checking and theorem proving can check system properties relative to a formal specification.

**Source check:** NASA explains formal verification against formal specifications and mentions the theorem prover as one example (same page, paragraphs 1 and 3). It does not explicitly establish the combined wording about “model checking and theorem proving” as two methods in this particular sentence. The EU is generic and does not distinguish which method the source supports (E1).

**Assessment:** The claim describes the purpose of verification relative to a specification (D2). It risks implying the methods are interchangeable or exhaustive; the source itself says there is no single best formal method and that techniques vary by application domain and lifecycle phase (B2).

**Disposition:** Narrow the claim to the source’s explicit description or add a technical source that separately explains model checking and theorem proving. Add a pinpoint and preserve the distinction between methods.

## 3. `CLM-FORMAL_METHODS_BASICS-C` — **D3 / E1 / B3**

**Claim:** Full formal verification of large systems is limited by state-space complexity, so abstractions and restricted verification scope are often used in practice.

**Source check:** NASA states that examining the entire state space is rarely done in practice because of the enormous complexity of real systems, then lists approaches including abstracting high-level designs, focusing on critical components, reducing variable ranges, hierarchical analysis, and automation (same page, paragraphs 1–2). This closely supports the claim.

**Assessment:** The claim identifies a concrete limitation and explains practical responses (D3). “Often” and the restriction to large systems avoid suggesting that full-state verification is impossible in every case (B3). The stored EU remains generic and does not identify the source passage (E1).

**Disposition:** Strongest of the three claims; retain provisionally after adding the exact NASA paragraph locator. Do not broaden it to claim that all formal verification is necessarily incomplete.

## Checkpoint totals

- New Claims reviewed in this checkpoint: **3**.
- Batch 13 total with provisional D/E/B review recorded: **21 of 100**.
- Remaining candidates without individual D/E/B review: **79**.
- Canonical records changed: **0**.
- Batch 13 complete: **NO**.
