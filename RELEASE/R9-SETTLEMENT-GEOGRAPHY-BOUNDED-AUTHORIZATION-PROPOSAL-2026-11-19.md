# Proposed Bounded Authorization — Settlement Geography Locator and Source Identity Closure

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Target branch: `mvp-public-contribution-design-2026-10-11`  
Status: **READY FOR OWNER APPROVAL; 3 EUS HAVE DIRECT LOCATOR CANDIDATES; NO CANONICAL CHANGE PERFORMED**

## 1. Why this authorization is needed

The R9 evidence-depth remediation addendum previously reported 7 unpinned EUs across Food Systems and Settlement Geography. A current-head re-fetch confirms the bounded Food Systems remediation has already completed at v2: both Sources, four Claims, four EUs, Context and Scope are v2 and contain claim-specific locators. This leaves **3 unpinned EUs in settlement-geography-basics**.

No active bounded authorization for `settlement-geography-basics` was found in `RELEASE/EDITORIAL-CORRECTION.json`. The Batch 9 locator research is complete, but implementation remains pending an explicit authorization.

## 2. Exact current canonical records

| Record | Current version | Proposed version | Type |
|---|---:|---:|---|
| `SRC-SETTLEMENT_GEOGRAPHY` | 1 | 2 | source |
| `CLM-SETTLEMENT_GEOGRAPHY-A` | 1 | 2 | claim |
| `CLM-SETTLEMENT_GEOGRAPHY-B` | 1 | 2 | claim |
| `CLM-SETTLEMENT_GEOGRAPHY-C` | 1 | 2 | claim |
| `EU-SETTLEMENT_GEOGRAPHY-A` | 1 | 2 | evidence_use |
| `EU-SETTLEMENT_GEOGRAPHY-B` | 1 | 2 | evidence_use |
| `EU-SETTLEMENT_GEOGRAPHY-C` | 1 | 2 | evidence_use |
| `CTX-SETTLEMENT_GEOGRAPHY` | 1 | 2 | context |
| `SCP-SETTLEMENT_GEOGRAPHY` | 1 | 2 | scope |

All nine exact records were fetched from the current branch. Claims A–C are substantively supportable as currently worded; no Claim statement change is proposed. Claims advance v1→v2 solely to align `provenance.created_from` with Source v2. Evidence Use A–C advance v1→v2 to add direct locators and point to Claim v2 / Source v2. Context and Scope advance v1→v2 only to align their `target_ref` to Claim A v2 and state the documented methodological boundary.

## 3. Proposed Source v2 identity

**Bibliographic identity:**

European Commission, FAO, UN-Habitat, ILO, OECD and World Bank (2021), *Applying the Degree of Urbanisation: A Methodological Manual to Define Cities, Towns and Rural Areas for International Comparisons*, ISBN 978-92-76-20306-3, DOI 10.2785/706535.

**Preferred canonical URI:**  
https://unhabitat.org/knowledge/publications/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas

**Stable PDF:**  
https://unhabitat.org/sites/default/files/2021/12/ks-02-20-499-en-n.pdf

**Source locator:** Abstract; Chapter 1 “Introduction”, p. 7; §§6.1–6.3, pp. 33–34.

The current Source identity attributes the publication only to UN-Habitat. The manual is jointly produced by six institutions. Source v2 must name all six co-publishers and must not imply that UN-Habitat is the sole author/publisher.

## 4. Proposed Evidence Use v2 locators

### EU A — urban/rural continuum

`material.locator`:

> *Applying the Degree of Urbanisation* (2021), Abstract; Chapter 1 “Introduction”, p. 7; §6.2 “Short description”, pp. 33–34.

Support boundary: the methodology classifies territories through a continuum and a three-class scheme; do not reduce it to a binary urban/rural split.

### EU B — harmonised criteria and three classes

`material.locator`:

> *Applying the Degree of Urbanisation* (2021), §6.1 “Terminology” and Table 6.2, p. 33; §6.2 “Short description”, pp. 33–34; §6.3 “Grid cell classification”, beginning p. 34.

Support boundary: the method uses 1 km² grid cells, population density, population size and contiguity to distinguish cities, towns/semi-dense areas and rural areas. It is a statistical classification methodology, not a universal legal definition of settlement types.

### EU C — national-definition boundary

`material.locator`:

> *Applying the Degree of Urbanisation* (2021), Abstract; Chapter 1 “Introduction”, p. 7.

Support boundary: the manual states that the harmonised method is intended to complement, not replace, national statistical-office and ministry definitions.

All three EUs should retain `evidence_role: supports`; no new Evidence Use role is required.

## 5. Proposed Context v2

Target: `CLM-SETTLEMENT_GEOGRAPHY-A@2`.

Suggested context:

> Срез описывает Degree of Urbanisation как гармонизированную статистическую методологию международного сравнения населённых территорий. Метод использует пространственные сетки и согласованные критерии плотности, численности населения и смежности для различения городов, малых городов/полуплотных территорий и сельских территорий. Методология дополняет, но не заменяет национальные определения и административно-правовые категории.

## 6. Proposed Scope v2

Target: `CLM-SETTLEMENT_GEOGRAPHY-A@2`.

Suggested scope:

> Срез ограничен методологией Degree of Urbanisation в редакции совместного руководства 2021 года и её применением для международного статистического сравнения. Он не определяет универсальный юридический статус города или села, не заменяет национальные определения и не задаёт административные границы, планировочные нормы или правила предоставления услуг.

## 7. Rights boundary — mandatory decision

The official PDF identifies **CC BY-NC-SA 3.0 IGO**. This is a non-commercial licence with ShareAlike requirements for adaptations. It does not clear commercial reuse or automatically establish compatibility with the project's eventual distribution licence. The publication excludes third-party cover photography and maps from the blanket copyright grant.

Official publication page and PDF:
- https://unhabitat.org/knowledge/publications/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas
- https://unhabitat.org/sites/default/files/2021/12/ks-02-20-499-en-n.pdf

The proposed canonical records store bibliographic identity, factual paraphrase and locators only; they do not reproduce manual text, maps, diagrams, photographs or tables. Even so, the project owner must decide whether the non-commercial/ShareAlike source is compatible with the planned Encyclopedia distribution and licensing model before source use is approved.

## 8. Exact proposed allowed changes

If approved, authorization should allow only:
1. `SRC-SETTLEMENT_GEOGRAPHY` v1→v2: correct joint bibliographic identity, stable official URI, DOI and publication locators.
2. `CLM-SETTLEMENT_GEOGRAPHY-A/B/C` v1→v2 without changing statement or claim_type, solely to align `provenance.created_from` to Source v2.
3. `EU-SETTLEMENT_GEOGRAPHY-A/B/C` v1→v2: exact locators above, concise support limits, current Claim v2 and Source v2 references.
4. `CTX-SETTLEMENT_GEOGRAPHY` and `SCP-SETTLEMENT_GEOGRAPHY` v1→v2: update only target_ref to Claim A v2 and use the boundaries in §§5–6.
5. Update only the settlement-geography README, R9 evidence-depth addendum, exact-version register and rights/attribution screen.

## 9. Explicit prohibited changes

- No Claim statement or claim_type changes.
- No publication_status or completion_status changes.
- No INCLUDE/EXCLUDE decision or first-edition allowlist changes; the slice remains HOLD.
- No new Source, Claim, EU or Relation IDs.
- No change to any other slice or relation.
- No reproduction/translation of manual text, maps, photographs, diagrams, tables or page layout.
- No validator, storage, recovery, package or release-gate changes.
- No merge, deployment or release approval.

## 10. Release conditions

After implementation, re-fetch all nine exact records and verify:
- Claim→EU→Source references resolve to the exact current versions;
- Context and Scope target Claim A v2;
- all three EU locators are non-empty and claim-specific;
- source identity includes all six co-publishers;
- the rights/attribution screen preserves CC BY-NC-SA 3.0 IGO and the third-party map/photo exclusion;
- all records remain HOLD.

Then run affected-slice tests and exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests on one frozen final HEAD. Technical PASS does not establish factual truth, rights clearance or release eligibility.

**Owner decision required:** approve or reject this exact nine-record scope and separately decide whether the CC BY-NC-SA 3.0 IGO source is compatible with the project's distribution/licensing model.


## Source-rights alternative — Eurostat 2026 CC BY 4.0 — 2026-11-19

A new source alternative has been verified and is preferred over the joint 2021 manual for the proposed text-only locator remediation: Eurostat, *Review and implementation of the degree of urbanisation*, 2026 edition. The report provides direct locators for Claims A–C in §§1.2 and 2.1 (printed pp. 6–7), including the urban–rural continuum, Level 1/Level 2 classes, the population-grid method, international comparability and the boundary that the methodology complements rather than replaces national definitions.

The report's front matter explicitly licenses EU-owned content under CC BY 4.0, with attribution and indication of changes. Third-party cover photo, most maps, other photos and administrative-boundary content are excluded. The proposed use is factual paraphrase and text locators only; no visual assets are proposed. The report identifies itself as a Eurostat Statistical Report and states that it is not representative of the European Commission's official position. Preserve that source-status boundary.

Preferred source identity, locators and the exact nine-record v1→v2 scope are in `R9-SETTLEMENT-GEOGRAPHY-EUROSTAT-CC-BY-4-0-SOURCE-ALTERNATIVE-2026-11-19.md`. This alternative supersedes the joint 2021 manual as the preferred implementation route if the owner approves. The earlier joint-manual option remains documented as a fallback but is CC BY-NC-SA 3.0 IGO and does not clear commercial reuse.

No authorization is granted by this addendum. The nine canonical records remain v1 and HOLD; no JSON was changed.
