# M13 — Unassessed Risk Content Screen — Package 31

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Queue source revision: `3c55d95dc01f29eafac3f5e6945d648e1e108854`
Queue workflow run: `43681565187`
Queue artifact: `14148283789` (`m13-review-queue-3c55d95dc01f29eafac3f5e6945d648e1e108854`)
Artifact digest: `sha256:d5b8cf2c1473d855a093db52a6d8c463ed190c4ccc9bca60ec68d2de9b3577d7`

## 1. Queue integrity and scope

- 4,834 records scanned; 1,494 Claims inventoried.
- 1,501 scored-report rows reconciled; zero Claims without a scored-report match.
- 12 candidate unassessed-risk Claims remained after exclusions.
- 697 previously screened Claim IDs excluded.
- 17 unreconciled holdout Claims excluded; 15 overlap with reviewed holdouts; 699 unique exclusions.
- 12 Claims selected; 88 nominal slots unfilled. Lane counts: 12, 0, 0, 0, 0.
- Lane 1 contains 12 unique Claim IDs, 13 Evidence Use records and 8 Source records.
- All selected IDs are unique. D/E/B values remain blank; risk flags are routing signals only.
- Queue preparation took 29.176 seconds. Human review time was not measured.

## 2. Record-chain verification

All 12 Claim records, 13 Evidence Use records and 8 Source records were fetched at the exact queue-source revision. Claim and Source content refs resolve to the intended version-1 records. Materials Science B and Risk Management C each have two Evidence Use links.

### Provenance lineage exceptions

Two ISO-based Evidence Use records have `provenance.created_from` pointing to the Claim rather than the Source:
- `EU-RISK_MANAGEMENT_BASICS-B`
- `EU-RISK_MANAGEMENT_BASICS-C`

Their content `claim_ref` and `source_ref` fields resolve correctly. The provenance lineage is inconsistent and requires authorized versioned reconciliation. The separate COSO Evidence Use for Risk Management C correctly points to the COSO Source.

## 3. Results — 12 Claims

**3 Claims have direct conceptual support in accessible, rights-compatible registered sources. 9 remain partial or on rights hold.** These are qualitative source-fit outcomes only, not D/E/B scores or publication decisions.

| Claim ID | Result | Finding and required follow-up |
|---|---|---|
| `CLM-MANUFACTURING_SYSTEMS_BASICS-B` | PARTIAL | The registered NIST Manufacturing page links to factory operations planning/control, manufacturing quality assurance and process measurement/control, but the landing page does not directly establish that measurement/control is used to improve reproducibility, quality and efficiency. Add the specific NIST process-measurement/control or manufacturing-systems-design source and pinpoint the quality/reproducibility passage. |
| `CLM-MANUFACTURING_SYSTEMS_BASICS-C` | PARTIAL | The NIST Manufacturing hub links to factory communications, interoperability, product data, systems integration and monitoring/diagnostics, but does not itself establish that digital technologies connect operations, monitoring and analysis for system management. Add a specific NIST smart-manufacturing or manufacturing-systems-integration source with an explicit data-flow/integration passage. |
| `CLM-MAPS_AND_NAVIGATION_BASICS-A` | DIRECT CONCEPTUAL SUPPORT | USGS states that a topographic map locates natural and human-made features, shows the shape of the land, distances and directions. Pinpoint the introduction to “Finding Your Way With Map and Compass,” lines 27–29. |
| `CLM-MAPS_AND_NAVIGATION_BASICS-B` | DIRECT CONCEPTUAL SUPPORT | USGS explicitly defines map scale as a ratio linking a measurement on the map to the corresponding distance on the ground and gives a 1:63,360 example. Pinpoint line 29. |
| `CLM-MAPS_AND_NAVIGATION_BASICS-C` | PARTIAL | The USGS map-and-compass page supports scale, topography and compass use, but does not establish the full dependence of a navigation conclusion on map quality, data currency and actual terrain conditions. Add a navigation/field-map source on map currency, positional accuracy and terrain verification. |
| `CLM-MATERIALS_BASICS-A` | PARTIAL — STALE/OPAQUE SOURCE | The registered NIST Metallurgy landing page has no readable content in the current fetch and does not directly establish the claimed relationship among materials, measurements, models, data and performance. Add a specific NIST Materials Science and Engineering publication or a rights-compatible materials-science textbook that explicitly covers measurement, modelling and performance. |
| `CLM-MATERIALS_BASICS-C` | PARTIAL — STALE/OPAQUE SOURCE | The registered NIST Metallurgy landing page has no readable content. NSF's current Materials Research page supports relationships among structure, properties and behaviour and mentions processing methods, but does not directly establish the complete composition/structure/processing/operating-conditions formulation. Register a specific materials-property source and pinpoint operating-condition effects. |
| `CLM-M5-MATERIALS-PERFORMANCE-D` | PARTIAL | NSF's Materials Research page supports studying material properties/behaviour and understanding failure and durability. It does not directly establish the complete assessment framework linking required function, service conditions, failure mechanisms and application-specific data. Add a specific materials selection/performance or failure-analysis source and pinpoint the service-condition and application-data requirements. |
| `CLM-MATERIALS_SCIENCE_BASICS-B` | PARTIAL — SOURCE GAP | NSF's Materials Research page names metals, ceramics, polymers and semiconductors, but does not explicitly list composites in the accessible text. The second registered NIST Materials Science and Engineering URL currently returns 404. Add a current NIST or other authoritative materials-classification source that explicitly covers all five classes and supports the application-suitability caveat. |
| `CLM-RISK_MANAGEMENT_BASICS-B` | RIGHTS HOLD — ISO | The only registered Source is ISO 31000. ISO's page expressly states that, except for material under ISO Open Data terms, ISO content may not be accessed/used to train or prompt AI systems to generate responses. Do not use ISO 31000 content in this AI-assisted evidence review without permission or a qualifying Open Data basis. Find a rights-compatible alternative that defines risk in relation to uncertainty and objectives (e.g. a government risk-management framework) and add it as a new Source/Evidence Use. |
| `CLM-RISK_MANAGEMENT_BASICS-C` | DIRECT CONCEPTUAL SUPPORT — COSO ONLY | The registered ISO Source is on RIGHTS HOLD and is not used. The separate COSO Source states that enterprise risk management should be integrated with strategy-setting and performance, supporting the Claim's core integration proposition. Pinpoint the COSO page's “Integrating with Strategy and Performance” section. Keep the scope to enterprise risk management; do not use the restricted ISO content as corroboration. |
| `CLM-STATISTICS_BASICS-B` | DIRECT CONCEPTUAL SUPPORT | NIST/SEMATECH Engineering Statistics Handbook explains that statistical methods depend on model/sampling assumptions and that sampling, measurement error and nonrepresentative data affect precision and reliability. Pinpoint the sampling-scheme, sample-size and measurement-error sections; do not imply one assumption set applies to all methods. |

## 4. Cross-record, rights and source-quality findings

1. Two Evidence Use records for Risk Management B/C have self-referential Claim entries in `provenance.created_from`; the content Claim/Source refs resolve. Reconcile the provenance only through an authorized versioned correction.
2. ISO 31000 is a RIGHTS HOLD for this AI-assisted evidence workflow. ISO's official page states that, outside ISO Open Data terms, ISO content may not be used for machine learning, AI prompting or AI-generated responses. No ISO content was used to support either Claim in this screen.
3. Risk Management C has a separate COSO Evidence Use and Source. COSO's public page supports integration of ERM with strategy-setting and performance; this is the only evidence used for the direct conceptual-support result.
4. The NIST Manufacturing landing page is a topic hub, not a technical manufacturing-systems specification. Its links to subtopics are not a substitute for the content of those subtopics.
5. The NIST Metallurgy site root has no readable content in the current fetch. Do not infer detailed materials-science propositions from the domain name or institutional identity.
6. The NSF Materials Research page supports some materials classes and properties, but does not explicitly establish every class in the Claim or the full application-specific selection framework.
7. The USGS map-and-compass fact sheet directly supports topographic-map content and scale, but not map freshness, accuracy or field-condition verification.
8. All generic `publication_status=published` and `completion_status=complete` values remain distinct from M13 risk assessment. All 12 Claims remain `UNASSESSED`.

## 5. Decision

- 12 Claim records, 13 Evidence Use records and 8 Source records inspected.
- 3 Claims: direct conceptual support (Maps A/B, Risk Management C via COSO, Statistics B).
- 9 Claims: partial support or rights hold.
- Two provenance-lineage inconsistencies recorded (Risk Management B/C ISO Evidence Use records).
- One rights hold recorded (ISO 31000 source); no ISO content used as evidence.
- No D/E/B scores assigned or inferred.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation or risk metadata modified.
- No publication, release or public-pilot approval granted.
- Package 31 closes only the current 12-Claim risk-priority queue. It does not close M13 or certify the remaining unassessed inventory as low risk.

## 6. Source references reviewed

- NIST Manufacturing: https://www.nist.gov/manufacturing
- USGS — Finding Your Way With Map and Compass: https://www.usgs.gov/educational-resources/finding-your-way-map-and-compass
- NIST Metallurgy: https://www.metallurgy.nist.gov/
- NSF Materials Research: https://www.nsf.gov/focus-areas/materials
- NIST Materials Science and Engineering: https://www.nist.gov/materials-science-and-engineering
- ISO 31000 page — inspected only to identify the explicit AI-use restriction; not used as evidence: https://www.iso.org/iso-31000-risk-management.html
- COSO Enterprise Risk Management: https://www.coso.org/enterprise-risk-management
- NIST/SEMATECH Engineering Statistics Handbook: https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook
