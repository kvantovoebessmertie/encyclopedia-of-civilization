# Domain audit — communications, transport and infrastructure (Part I sequence 10)

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR workstream: #22  
Audited record revision: `80e4c38444fefbb3f04cc90b0a65c14ac349f285`  
Disposition: **HOLD — six slices / 60 records screened; no canonical records changed**

## Plan alignment

This is targeted first-edition Work Package 1 screening, not a new M13 batch. It follows the controlling opening-survival map's sequence 10 (communication, navigation, transport and community logistics) and the record-level candidate inventory. The purpose is to decide candidate eligibility, not to repair canonical content. Previously closed adjudications are not repeated.

## Scope

All inventory-listed records were inspected at exact version 1:
- telecommunications-basics — 9 records
- networks-basics — 9 records
- public-risk-communication-basics — 15 records
- transportation-basics — 9 records
- public-transport-basics — 9 records
- infrastructure-basics — 9 records

Total: **60 records** (19 Claims, 22 Evidence Use, 7 Sources, 6 Context, 6 Scope). The complete inventory-listed set is screened below, including the additional Evidence Use and Source records in the public-risk-communication slice.

## 1. telecommunications-basics — 9 records

Claims:
- A: telecommunications systems transmit information between remote points.
- B: telecommunications infrastructure includes equipment and connections needed to provide communications services.
- C: international technical standards help ensure compatibility among telecommunications networks and technologies.

Source: ITU-D Delegate Guide, “What is ITU?”  
https://www.itu.int/en/ITU-D/Conferences/TDAG/Pages/ITU-D-Delegate-Guide-WhatisITU.aspx

Findings:
- The current ITU page identifies ITU's role coordinating operation of networks/services and says ITU-T develops interoperable international standards. This is a reasonable conceptual match for Claim C.
- The page does not directly establish Claim A's data-transmission formulation or Claim B's infrastructure-component description with sufficient specificity.
- All three EUs use the same generic description and contain no section/passage locator.
- Context and Scope target Claim A only; do not extend them to B/C.

Decision: **HOLD.** Claim C has the strongest fit; A/B need better direct sources or tighter scope. All EUs require claim-specific pinpoint references. ITU's separate ITU-T Recommendations material is a stronger direct source for standard interoperability, but it is not the currently linked Source record.

## 2. networks-basics — 9 records

Claims:
- A: a computer network is implemented as interconnected components such as routers and communications equipment.
- B: a protocol is a set of rules, formats and procedures controlling communication between systems.
- C: Internet Protocol supports transmission of data between destinations in packet-switched networks.

Current Source: NIST CSRC Glossary — network  
https://csrc.nist.gov/glossary/term/network

Findings:
- NIST's network entry directly supports Claim A: a network is a system of interconnected components and explicitly lists routers, hubs, cabling and telecommunications controllers.
- The current Source URL does not provide the exact protocol definition needed for Claim B or the Internet Protocol definition needed for Claim C.
- NIST has separate term entries for protocol and Internet Protocol, which directly support the respective propositions, but no corresponding Source/EU records are currently present in this slice.
- All three EUs point to the single network Source and use a shared generic description. This is not adequate evidence mapping for B/C.
- Context and Scope target Claim A only.

Decision: **HOLD.** Claim A has direct support. Claims B/C require their own source records and EUs or a documented multi-source evidence structure; exact NIST term entries must not be silently treated as if they were the existing network Source.

## 3. public-risk-communication-basics — 15 records

Claims:
- A: effective risk communication supports shared understanding and risk-reduction action.
- B: risk communication should account for audience, context, accessibility and trust in message channels.
- C: unverified or misleading information can impair risk understanding and protective action.
- D: effective communication should account for audience, explain uncertainty and numbers clearly, and update as threat/knowledge changes.

Sources:
- UNDRR, “Risk communication”: https://www.undrr.org/risk-communication
- CDC, “Understanding Risk Communication”: https://www.cdc.gov/public-health-risk-communication/php/about/understanding-risk-communication.html
- CDC, “Understanding and Applying Risk Communication Principles”: https://www.cdc.gov/public-health-risk-communication/php/about/understanding-and-applying-risk-communication-principles.html

Findings:
- Claim A is directly supported by UNDRR: effective risk communication contributes to shared understanding and risk-reduction action.
- Claim B is strongly supported by CDC's audience, accessibility, community-partner and trusted-messenger principles.
- Claim C is supported by both UNDRR (rumour can erode trust and hamper solutions) and CDC (inaccurate health information can spread and mislead).
- Claim D is directly supported by CDC's explicit principles: state what is known/unknown, explain numbers clearly, address inaccurate information, use trusted partners, and communicate updates as new information becomes available.
- The slice has multiple EUs per A/B/C and a CDC EU for D, which is a materially stronger evidence structure than the generic one-source slices. However, EU descriptions still do not name exact CDC/UNDRR page sections or passages.
- Context and Scope target Claim A only; no sibling Claim inheritance is assumed.

Decision: **HOLD — strongest substantive fit in this batch.** The four Claims are well matched to the linked authorities, but the EUs need exact pinpoints and the Context/Scope coverage boundary must remain explicit. CDC material is specifically public-health risk communication; do not universalize it to every hazard, jurisdiction or audience without qualification.

## 4. transportation-basics — 9 records

Claims:
- A: transport systems move people and goods between places.
- B: a transport system includes infrastructure, vehicles, rules and organizational processes.
- C: transport safety and efficiency depend on operating conditions, infrastructure, rules and participant behaviour.

Current Source: U.S. Department of Transportation, “About DOT”  
https://www.transportation.gov/mission/about-dot

Findings:
- The current page states DOT's mission to move people and goods and advance safety/infrastructure. It offers conceptual support for Claim A.
- The current page does not directly substantiate the full system decomposition in Claim B or the multi-factor safety/efficiency proposition in Claim C.
- A current DOT strategic/agency source describes roads, railways, pipelines, airways and seaways and coordination with public/private partners, but that is not the Source presently linked in this slice.
- All three EUs are generic and lack pinpoint passages.
- Context and Scope target Claim A only.

Decision: **HOLD.** Claim A is supportable from the current Source; B/C need specific DOT or transport-systems sources and pinpoint EUs. Do not treat a department mission statement as full evidence for a systems model or safety analysis.

## 5. public-transport-basics — 9 records

Claims:
- A: public transport provides shared mobility services within and between communities.
- B: public-transport systems can include buses, rail and other shared modes in organized networks.
- C: planning depends on demand, network design, accessibility, capacity, operating conditions and resources.

Critical integrity finding:
- The actual Claim record IDs are hyphenated (for example, `CLM-PUBLIC_TRANSPORT_BASICS-A`), but the Claim refs embedded in all three EUs use underscore-form IDs (for example, `CLM_PUBLIC_TRANSPORT_BASICS_A`). The Context and Scope target refs also use underscore-form IDs. These do not resolve to the actual record IDs enumerated in the controlling inventory.
- The EUs' Source refs use `SRC_PUBLIC_TRANSPORT_BASICS`, while the actual Source record ID is `SRC-PUBLIC_TRANSPORT_BASICS`. This is a broken Claim/EU/Source chain.
- The Source URL stored in the record redirects to a generic World Bank development-topics page rather than the stated Urban Transport brief: https://www.worldbank.org/en/topic/transport/brief/urban-transport
- The EUs are generic and do not identify any source passages.

Decision: **HOLD — referential integrity failure.** All three EU Claim refs, all three EU Source refs, and Context/Scope target refs need a separately authorized, versioned correction. The current World Bank URL must be replaced or re-verified against a stable, relevant source. No silent normalization or canonical correction is performed in this audit.

## 6. infrastructure-basics — 9 records

Claims:
- A: infrastructure includes physical and organizational systems needed for society to function.
- B: infrastructure systems may include transport, energy, water, healthcare, communications and supply chains.
- C: infrastructure reliability depends on interconnections among systems, not only individual assets.

Current Source: NIST, “Infrastructure”  
https://www.nist.gov/infrastructure

Findings:
- NIST directly defines infrastructure as basic physical and organizational structures needed for a society or enterprise and lists roads, bridges, dams, rail, ports, hospitals, power, food systems, communications and supply chains. This strongly supports Claims A and B.
- Claim C's interdependency/reliability proposition is not directly established by the current NIST landing page. NIST SP 1190 Vol. II discusses internal/external infrastructure dependencies and cascading effects, but it is not the Source linked in the slice and must be added only through authorized versioned evidence work.
- All three EUs use a generic NIST description without claim-specific locators.
- Context and Scope target Claim A only.

Decision: **HOLD.** Claims A/B have direct conceptual support; Claim C needs a source specifically on infrastructure interdependencies and resilience. All EUs require exact locators.

## Cross-slice and record-integrity findings

1. No new Relation is created merely because telecommunications, networks, public-risk communication, transport and infrastructure are related. Any relation requires a specific pair of Claims and a justified semantic relation.
2. No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was edited.
3. No INCLUDE decision, public allowlist, preview or publication status was changed.
4. All inspected records are version 1; local Claim/EU/Source references were checked. Public-transport-basics contains the explicit broken-reference defect described above.
5. The NIST CSRC glossary itself warns that term definitions are aggregated from different source publications and should be understood in their originating contexts; cite the originating NIST publication where practical, not merely the glossary page.
6. High-consequence operational instructions are not introduced by this educational batch; these records remain explanatory and HOLD.

## Group disposition

| Slice | Records | Finding | Decision |
|---|---:|---|---|
| telecommunications-basics | 9 | Claim C strongest; A/B weakly sourced; generic EUs | HOLD |
| networks-basics | 9 | Claim A supported; B/C need separate direct NIST entries | HOLD |
| public-risk-communication-basics | 15 | A-D substantively supported; pinpoints/context boundary open | HOLD |
| transportation-basics | 9 | Claim A supported; B/C under-supported by current Source | HOLD |
| public-transport-basics | 9 | Broken record refs and redirected Source URL | HOLD |
| infrastructure-basics | 9 | A/B supported; C needs interdependency source | HOLD |
| **Total** | **60** | **No public INCLUDE decisions** | **HOLD** |

Next step within Work Package 1: consolidate these six screens into the record-level candidate register, preserve all HOLDs, then continue the opening-section sequence only where candidate selection still requires targeted evidence. Do not launch a new M13 batch or rewrite canonical records.
