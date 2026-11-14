# M13 Batch 13 — source-fit triage (rows 624–626): graph theory

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; MIT OCW directly supports the core definitions, but application examples and claim-specific Evidence Use pinpoints remain incomplete**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON remains unchanged.

## Source trail and public-source pinpoints

All three Claims reference `SRC-GRAPH_THEORY_BASICS@1`, identified as MIT OpenCourseWare, *Mathematics for Computer Science*, Fall 2010.

- Chapter 5: Graph Theory: https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/resources/mit6_042jf10_chap05/
- Chapter 6: Directed Graphs, listed in the same course readings index: https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/resources/readings/
- Course description establishes the source as an undergraduate discrete-mathematics course with elementary graph theory and applied methods.

The Chapter 5 reading defines a graph as vertices/nodes plus edges, and explains that edges represent relationships between pairs of objects. It distinguishes symmetric relationships in simple graphs from one-way relationships handled in Chapter 6. These section-level locations directly support the conceptual definition and directed/undirected distinction. The stored Evidence Use records, however, contain only generic statements and no page/section pinpoints.

## 1. `CLM-GRAPH_THEORY_BASICS-A` — provisional **D2 / E3 / B2**

**Claim:** “Граф представляет объекты и отношения между ними через вершины и рёбра.”

**Assessment:** This is a clear introductory definition but does not explain graph variants, edge weights, multiplicity, or formal notation (D2). MIT OCW Chapter 5 directly explains vertices/nodes and edges and their use to represent relationships between objects, so the core proposition is strongly supported (E3). The claim is appropriately general for an introduction, though it should not be read as a complete definition covering every graph formalism (B2).

**Disposition:** Retain provisionally. Add a pinpoint to Chapter 5, section “Definitions” / “Simple Graphs,” and update Evidence Use with a claim-specific summary.

## 2. `CLM-GRAPH_THEORY_BASICS-B` — provisional **D2 / E3 / B2**

**Claim:** “Ориентированные и неориентированные графы позволяют различать направленные и ненаправленные отношения.”

**Assessment:** The statement captures the core distinction but does not explain ordered pairs, edge direction, or consequences for reachability (D2). MIT OCW Chapter 5 defines undirected edges as unordered pairs representing symmetric relationships; Chapter 6 is specifically devoted to directed graphs and one-way relationships. This is a strong direct fit (E3). Preserve the distinction that “directed/undirected” is a property of the model, not an inherent property of every real-world relationship independent of how it is represented (B2).

**Disposition:** Retain provisionally. Evidence Use should reference both Chapter 5's simple-graph definition and Chapter 6's directed-graph definitions.

## 3. `CLM-GRAPH_THEORY_BASICS-C` — provisional **D2 / E2 / B2**

**Claim:** “Графовые модели применяются к маршрутизации, расписаниям, сетям и другим задачам, но результат зависит от того, какие объекты и связи включены в модель.”

**Assessment:** This claim usefully notes modelling choices but does not explain how graph structure or algorithm assumptions affect results (D2). MIT's course resources include communication networks, directed graphs, and relations/scheduling, supporting several application areas. However, the stored source record points only to Chapter 5, and its Evidence Use contains no pinpoint for routing, scheduling, or networks; the complete list of examples is not directly established by the stored locator alone (E2). The modelling-boundary clause is sensible but should be presented as a general methodological caution, not a theorem proven by the introductory definition chapter (B2).

**Disposition:** Retain provisionally, but either add relevant course sources/chapters (directed graphs, relations and scheduling, communication networks) to the source chain or narrow the examples to those directly supported by Chapter 5. Add a specific explanation that the selected vertices, edges, directionality and other modelling assumptions constrain what the model can answer.

## Batch accounting

- Individual Claims reviewed in this note: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
