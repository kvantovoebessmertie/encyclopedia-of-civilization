# M13 duplicate-source adjudication: NIST CSRC Network Glossary, Smithsonian History Guide, and National Academies Science Communication

Date: 2026-11-13  
Branch: m13-system-wide-depth-audit-2026-10-09  
Reviewed baseline: 4ac45d0c9e1f9cc16ae6827a9a60ec009047d176  
Scope: three shared-URI groups, six Source records and 18 linked Claims. Source, Evidence Use and Claim records were inspected directly; NIST, Smithsonian and National Academies pages were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Claims | Adjudication |
|---|---:|---:|---|
| NIST CSRC Glossary — network | 2 | 6 | One network glossary page. It supports the network definition, but the second Source identity claims network/protocol/IP while its URL contains only the network term. The three Claims in the computer-networks slice are generic editorial statements. NIST itself says to cite the underlying source publication, not the glossary website. |
| Smithsonian History of Science and Technology Research Guide | 2 | 6 | One research guide, not two independent sources and not a substantive history monograph. It is useful for source discovery but does not directly establish most historical Claims. Direct retrieval was blocked by a Smithsonian help-desk error page. |
| National Academies, Communicating Science Effectively | 2 | 6 | One 2017 report/chapter. The shared URL resolves to Chapter 2, “The Complexities of Communicating Science,” not a separately titled Chapter 4. The chapter supports much of the communication content, but several Claims need narrower wording and exact page locators. |

Totals: 6 Source records, 18 linked Claims, three shared-URI groups. Repeated Source IDs do not create independent corroboration.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed.

## 2. NIST CSRC Glossary — network — two IDs, one term page

### Source identity

Both records point to https://csrc.nist.gov/glossary/term/network:

- SRC-COMPUTER_NETWORKS_BASICS
- SRC-NETWORKS_BASICS

The first Source identity says “NIST — Computer Security Resource Center”; the second says “NIST CSRC Glossary — network/protocol/IP”. Both point to one term page for network. The page contains several context-specific network definitions and cites multiple underlying publications, including NIST SP 800-171r3, NIST SP 800-172r3, NIST SP 800-37 Rev. 2, NIST SP 800-53 Rev. 5, NIST SP 800-63-4 and NISTIR 7693.

The NIST glossary page explicitly instructs readers to understand each term-definition pair in the context of its source document. The glossary homepage says it aggregates terms from NIST standards/guidelines and CNSSI 4009-2022, that definitions are context-dependent, and that users should cite the source publication rather than the glossary website.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| CLM-COMPUTER_NETWORKS_BASICS-A — the slice introduces basic concepts and relationships for orientation in computer networks | This is a statement about the Encyclopedia slice, not an external network fact. It cannot be supported by a NIST term page. Reclassify as editorial/structural metadata or replace with a substantive network Claim through authorized review. |
| CLM-COMPUTER_NETWORKS_BASICS-B — interpretation depends on source, context and applicability boundaries | General evidence-method principle, not a computer-network fact. It belongs in a methodology standard, not a network Claim. |
| CLM-COMPUTER_NETWORKS_BASICS-C — basic knowledge does not replace specialized verification when conditions, measurements or professional judgment matter | General scope/safety boundary, not a computer-network fact. It belongs in a policy/decision record rather than a network Claim. |
| CLM-NETWORKS_BASICS-A — a computer network is interconnected components such as routers and communication equipment | Direct. The network term page defines a network as a system of interconnected components and lists routers, hubs, cabling and telecommunications controllers. Use the exact NIST definition and cite its underlying source publication, not just the glossary page. |
| CLM-NETWORKS_BASICS-B — a protocol is a set of rules, formats and procedures controlling communication between systems | Not supported by the current /term/network URI. A distinct NIST term page at https://csrc.nist.gov/glossary/term/protocol contains this definition and cites CNSSI 4009-2022, NIST SP 800-82r3 and IETF RFC 4949. Add the appropriate term/source as a separate record if authorized. |
| CLM-NETWORKS_BASICS-C — Internet Protocol transmits data from source to destinations in packet-switched networks | Not supported by the current /term/network URI. The distinct NIST term page at https://csrc.nist.gov/glossary/term/internet_protocol defines Internet Protocol in almost exactly these terms and cites CNSSI 4009-2022 and NIST SP 1800-16B/C/D. Use a separate Source/Evidence Use link and the underlying publication. |

### Disposition

- Two Source IDs = one NIST network term page; no independent corroboration.
- The networks-basics Source identity overstates the content of its URI: protocol and Internet Protocol have distinct term pages.
- The three computer-networks-basics Claims are generic editorial statements and should not be treated as external network facts.
- NIST’s own glossary guidance requires citation to the underlying source publication and context. A glossary page is a discovery/index resource, not a universal standalone authority.

## 3. Smithsonian History of Science and Technology Research Guide — two IDs, one research guide

### Source identity

Both records point to https://library.si.edu/research/history-science-technology:

- SRC-HISTORY_OF_SCIENCE
- SRC-HISTORY_OF_TECHNOLOGY

Both identify Smithsonian Libraries and Archives — History of Science and Technology Research Guide. They are two Source IDs for one research guide, not two independent historical sources.

Direct retrieval during this review returned a Smithsonian OCIO Help Desk error page rather than the guide content. The Source identity itself describes a research guide, not a scholarly monograph or primary historical record. Such a guide can help locate books, archives, biographies, technical collections and other research material, but its existence does not substantiate a historical interpretation.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| CLM-HISTORY_OF_SCIENCE-A — history of science studies the development of scientific fields, sources, ideas and practices over time | Partial at most. A research guide identifies relevant research resources but does not provide a field definition or historiographical argument. Add a scholarly introduction to the history of science. |
| CLM-HISTORY_OF_SCIENCE-B — historical study uses books, archives, biographies and other sources tied to periods and fields | Partial-to-direct as a resource-discovery statement. The guide is intended to surface relevant books, archives and collections, but its content could not be retrieved in this review. Use exact catalog/collection records or a research-method source for a direct Claim. |
| CLM-HISTORY_OF_SCIENCE-C — claims about causes or priority of scientific change require sources appropriate to the period and question | Not directly supported by the research-guide landing page. Add a historiography or historical-methods source; this is a methodological rule, not a fact established by a bibliography page. |
| CLM-HISTORY_OF_TECHNOLOGY-A — history of technology studies the development of technical objects, practices and knowledge over time | Partial at most. The research guide identifies a subject area and resources but does not define the discipline or support a historical synthesis. |
| CLM-HISTORY_OF_TECHNOLOGY-B — sources include materials about technology/engineering and archival/library collections | Partial-to-direct as a description of the guide’s research function. The exact page content could not be retrieved; cite actual catalog and archive collections for a fully reproducible evidence chain. |
| CLM-HISTORY_OF_TECHNOLOGY-C — an artifact alone does not prove one unique cause of invention or diffusion | Not directly supported. Add a history-of-technology methodology source on multiple causation, diffusion and contextual interpretation. |

### Disposition

- Two Source IDs = one Smithsonian research guide; no independent corroboration.
- Treat the guide as a discovery resource rather than substantive evidence for historical Claims.
- The current EUs use generic descriptions and no catalog item, archival collection, page or scholarly passage.
- Resolve the page’s current availability and identify specific primary/secondary sources for the historical Claims before treating the chain as verified.

## 4. National Academies — Communicating Science Effectively — two IDs, one book chapter

### Source identity

Both records point to https://nap.nationalacademies.org/read/23674/chapter/4:

- SRC-COMMUNICATION_BASICS
- SRC-SCIENTIFIC_COMMUNICATION_BASICS

Both identify the 2017 National Academies report Communicating Science Effectively: A Research Agenda. The current URL redirects to the National Academies Press reader and displays Chapter 2, “The Complexities of Communicating Science,” beginning on book page 23. The URL segment chapter/4 is not the displayed chapter number. The Source identity names the book, not the chapter/page actually cited.

This is one report/chapter, not two independent publications. The current chapter is directly relevant to audience, goals, context, uncertainty and public engagement.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| CLM-COMMUNICATION_BASICS-A — effective communication considers goals, content, format and audience characteristics | Direct. Chapter 2, pp. 23–24, states that science communication involves goals, content, format, and individuals/organizations; audience starting points include knowledge, skills, beliefs and values. |
| CLM-COMMUNICATION_BASICS-B — context includes prior knowledge, expectations and values, so audiences can understand the same message differently | Direct for audience variation. Chapter 2, pp. 23–24, describes differences in knowledge, skills, beliefs and values and how these affect interpretation. The added limitation “this does not make every interpretation equivalent to the original meaning” is not explicit in the passage; keep it separate or add a source about faithful interpretation. |
| CLM-COMMUNICATION_BASICS-C — communication quality depends on task/audience; simplifying terms may improve accessibility but does not guarantee understanding or justify removing accuracy | Partial. Chapter 2 says science communication is more complex than translating jargon and that audience needs vary. It does not explicitly formulate the accuracy-versus-simplification rule. Add a science-writing/communication source for this boundary or narrow the Claim. |
| CLM-SCIENTIFIC_COMMUNICATION_BASICS-A — effective science communication depends on goals and audience, not only scientific content | Direct. Chapter 2, pp. 23–24, directly addresses goals, content, format, audiences and their different knowledge/values. |
| CLM-SCIENTIFIC_COMMUNICATION_BASICS-B — scientific information should be communicated in light of the context in which audiences interpret it | Direct. Chapter 2, pp. 23–24 and the section on audience needs, describes how context and prior knowledge affect understanding and use. |
| CLM-SCIENTIFIC_COMMUNICATION_BASICS-C — for complex/contested science, choice of communication form and approach is part of the task | Direct-to-partial. Chapter 2, pp. 25–28, discusses public engagement, stakeholder needs, uncertainty and context-sensitive formats. The final phrase “evaluate by evidence” is broader than the cited passage and needs a precise methodological source or narrower wording. |

### Disposition

- Two Source IDs = one National Academies report/chapter; no independent corroboration.
- Correct the bibliographic locator to Chapter 2, “The Complexities of Communicating Science,” pages 23–28 as applicable. The current URL path should not be interpreted as “Chapter 4”.
- Add page-level locators to the six EUs. The current EUs have only generic descriptions.
- Preserve the distinction between direct support for audience/context and partial support for claims about fidelity, simplification and evidence-based evaluation.

## 5. Consolidated audit decision and next actions

1. Count one source identity per shared URI: NIST network term page = 1; Smithsonian research guide = 1; National Academies report/chapter = 1.
2. Keep all 18 Claims in the audit denominator. Do not merge Source IDs solely because their URLs match.
3. For NIST network terms, add separate source records/locators for network, protocol and Internet Protocol, and prefer the underlying NIST/CNSSI/IETF publication rather than citing the glossary as if it were the source.
4. Reclassify the three computer-networks Claims as editorial/methodology boundaries or replace them with actual network propositions.
5. For history of science/technology, use the Smithsonian guide only to discover resources; attach actual primary/secondary sources and methodological works to the Claims.
6. For National Academies, preserve the exact title/year/chapter/page and add pinpoint locators; the current chapter supports most audience/context claims but not every qualifier.
7. Run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA after any authorized canonical correction.

## 6. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; main remains unchanged.

This report records source identity, page correctness, source fit and the distinction between a research guide, glossary and substantive publication. It is not a release approval or authorization to edit canonical records.
