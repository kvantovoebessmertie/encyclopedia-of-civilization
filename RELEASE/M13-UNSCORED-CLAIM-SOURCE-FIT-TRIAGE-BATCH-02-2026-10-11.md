# M13 Unscored Claim Source-Fit Triage — Batch 02

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **15-Claim diagnostic pass; no D/E/B scores assigned and no content JSON changed**

## Scope

This pass reviewed unscored inventory rows #203–217: compiler basics, computer architecture, computer graphics, computer networks, and computer-science algorithms. Claim statements, linked Evidence Use (EU) records and Source records were inspected. Public source pages were checked where accessible. These are source-fit and record-classification findings, not final score adjudications.

## Claim-level dispositions

| # | Claim ID | Source | Finding and next action |
|---:|---|---|---|
| 203 | `CLM-COMPILER_BASICS-A` | LLVM — Kaleidoscope Language Tutorial | LLVM's tutorial explicitly covers lexer, parser/AST and code generation. This is a good source family for the staged-compiler claim, but the EU is boilerplate and does not name the chapters. Pinpoint the lexer, parser/AST and IR-generation sections. |
| 204 | `CLM-COMPILER_BASICS-B` | LLVM — Kaleidoscope Language Tutorial | LLVM explicitly explains that an AST captures program behavior for later stages such as code generation. This is a direct fit; the EU is generic. Add the AST section locator. |
| 205 | `CLM-COMPILER_BASICS-C` | LLVM — Kaleidoscope Language Tutorial | The tutorial covers optimizer support and object-code generation as topics, but the Claim also asserts the general correctness obligation across representations. The current EU is generic and does not distinguish tutorial facts from the methodological correctness principle. Add a direct compiler-correctness source or narrow the statement; pin the relevant optimizer/object-code sections. |
| 206 | `CLM-COMPUTER_ARCHITECTURE_BASICS-A` | NIST ITL landing page | **Source identity/scope defect.** The stored `source_identity` is a descriptive sentence about computer architecture, not the title/identity of a source. The URI points to NIST's broad Information Technology Laboratory page, which is not direct support for processor instructions, memory and I/O. Replace with an actual architecture reference and claim-specific locator under an authorized Source correction plan. |
| 207 | `CLM-COMPUTER_ARCHITECTURE_BASICS-B` | Same NIST ITL landing page | The memory-versus-storage distinction is a substantive architecture claim, but the linked NIST ITL landing page does not identify a passage establishing it. Source identity is descriptive rather than bibliographic. Use a direct architecture/computer-systems reference. |
| 208 | `CLM-COMPUTER_ARCHITECTURE_BASICS-C` | Same NIST ITL landing page | The statement is a broad architecture definition, but the source locator is not a definition or technical section. Correct Source identity/locator and then reassess evidence fit. |
| 209 | `CLM-COMPUTER_GRAPHICS_BASICS-A` | Khronos — OpenGL | Khronos describes OpenGL as a graphics API for rendering 2D/3D graphics and exposing graphics-hardware capabilities. This is relevant to the Claim, but the statement also generalizes to computer graphics beyond OpenGL. The EU is generic; either narrow the scope to API-based rendering or add a broader computer-graphics source. |
| 210 | `CLM-COMPUTER_GRAPHICS_BASICS-B` | Khronos — OpenGL | Khronos directly describes OpenGL as an API controlling a rendering system. The Claim is plausible but the EU gives no pinpoint. Add the official API/renderer definition and avoid implying all graphics APIs expose identical interfaces. |
| 211 | `CLM-COMPUTER_GRAPHICS_BASICS-C` | Khronos — OpenGL | Khronos notes that hardware vendors implement the rendering system and that software implementations may provide unsupported hardware functionality. This supports some hardware/implementation dependence, but not necessarily the full universal statement about performance depending on API, hardware and implementation. Pinpoint the source and narrow or supplement as needed. |
| 212 | `CLM-COMPUTER_NETWORKS_BASICS-A` | NIST CSRC glossary — network | **Type/placement mismatch candidate.** The Claim describes the intended coverage of this local slice; a glossary definition of “network” cannot establish that the slice introduces adequate concepts and relations. Move to internal learning-design metadata or validate against an internal acceptance specification. |
| 213 | `CLM-COMPUTER_NETWORKS_BASICS-B` | NIST CSRC glossary — network | **Type/placement mismatch candidate.** The source/context/applicability rule is cross-cutting epistemic guidance, not a computer-networks fact supported by the network glossary. Move to shared methodology/policy or cite an appropriate source; review `claim_type: documented_fact`. |
| 214 | `CLM-COMPUTER_NETWORKS_BASICS-C` | NIST CSRC glossary — network | **Type/placement mismatch candidate.** The specialist-checking rule is governance/methodology and is not established by the network glossary. This is also part of the 20-slice template family in the semantic-duplicate triage report. |
| 215 | `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A` | NIST — Algorithms glossary | **Type/placement mismatch candidate.** The statement describes the local slice's learning purpose; a glossary definition of algorithm cannot establish that this slice is adequate. Reclassify as editorial/learning-design metadata or validate against an internal specification. |
| 216 | `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B` | NIST — Algorithms glossary | **Type/placement mismatch candidate.** The source/context/applicability rule is general epistemic guidance, not a domain fact established by the NIST algorithm definition. Move to shared methodology/policy or use an appropriate source. |
| 217 | `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C` | NIST — Algorithms glossary | **Type/placement mismatch candidate.** The specialist-checking rule is cross-cutting guidance, not a fact established by the NIST algorithm definition. This is part of the same 20-slice template family; do not deduplicate automatically. |

## Cross-batch observations

- The 15 reviewed Claims have Claim → EU → Source IDs that align structurally and use the `supports` role. That does not establish claim-specific evidence fit.
- All 15 EUs are generic or near-generic; none provides a claim-specific section locator.
- Three computer-architecture Claims share a Source record whose identity is descriptive rather than bibliographic and whose URI is a broad NIST ITL landing page.
- Six Claims in computer-networks and computer-science-algorithms are members of the templated slice-purpose/source-context/specialist-checking families. Their classification and source fit should be adjudicated together with the other template candidates.
- No D/E/B scores were assigned. These Claims remain unscored and in the fixed 1,494-Claim denominator.

## Public source checks used

- LLVM Kaleidoscope tutorial: https://llvm.org/docs/tutorial/index.html
- LLVM AST chapter: https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl02.html
- LLVM IR code-generation chapter: https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl03.html
- LLVM optimizer chapter: https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl04.html
- NIST Information Technology Laboratory: https://www.nist.gov/itl
- Khronos OpenGL: https://www.khronos.org/opengl/
- OpenGL concepts/API implementation: https://wikis.khronos.org/opengl/Portal%3AOpenGL_Concepts/Intro
- NIST CSRC network glossary: https://csrc.nist.gov/glossary/term/network
- NIST algorithm glossary: https://www.nist.gov/glossary-term/algorithm

## Protected-state boundary

No Claim, Evidence Use, Source or Relation JSON was changed. No identifiers were rewritten. These findings are a diagnostic source-fit pass, not final D/E/B scoring or permission to modify content. PR #21 remains open as Draft and `main` remains unchanged. M13 remains open.
