# Air Quality / Power Systems — Focused Cross-Slice Evidence Review

- **Agent:** chief-engineer
- **Task:** Focused WP1 evidence and endpoint-fit review of `REL-CROSS-AIR-POWER-SYSTEMS@2`
- **Date (UTC):** 2026-11-20
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** f31f556017aee81b355333b8c4f87307b37969b8
- **Status:** VERIFIED — exact records and official EPA pages inspected; report-only; no canonical changes

## 1. Request and acceptance criteria

Continue WP1 with a bounded review of an existing semantic-HOLD Relation. Test whether authoritative evidence establishes a direct air-quality / electric-power connection; distinguish external mechanism evidence from what the current canonical endpoints actually state. Preserve all canonical records and HOLD unless exact owner authorization exists.

## 2. Scope

- **In scope:** `REL-CROSS-AIR-POWER-SYSTEMS@2`, its two Claims, Evidence Use and Source records, its target-specific Context, and relevant official EPA source pages.
- **Out of scope:** canonical mutation, new Source/Evidence Use records, locator insertion, Relation/Context versioning, candidate promotion, rights clearance, and release/merge actions.
- **Dependencies:** PR #22 current branch HEAD and the WP1 semantic-HOLD checkpoint.

## 3. Work performed

Fetched the exact Relation, Context, both participant Claims, both Evidence Use records and both Source records at the starting HEAD. Inspected the existing EPA AirData source and three directly relevant official EPA pages: Electric Power Sector Basics, Power Sector Data, and Power Plants and Neighboring Communities. Compared what these sources establish with the precise wording of the two current Claims.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `reports/agent-work/chief-engineer/air-quality-power-systems-relation-evidence-review-2026-11-20.md` | Added report-only evidence review | Record the direct external bridge and the remaining endpoint/evidence limitations |

## 5. Exact canonical graph

At starting HEAD `f31f556017aee81b355333b8c4f87307b37969b8`:

- `REL-CROSS-AIR-POWER-SYSTEMS@2`
  - `relation_type`: `air_quality_and_energy_systems_link`
  - participants: `CLM-AIR_QUALITY_BASICS-A@1` and `CLM-POWER_SYSTEMS_BASICS-A@1`
  - both roles are currently `linked_record`
  - frame: `CTX-REL-CROSS-AIR-POWER-SYSTEMS@1`, whose target_ref points to Relation @2.
- `CLM-AIR_QUALITY_BASICS-A@1`: “Мониторинг качества атмосферного воздуха включает измерение концентраций загрязняющих веществ на пунктах наблюдения.”
  - `EU-AIR_QUALITY_BASICS-A@1` references `SRC-AIR_QUALITY_BASICS@1` (US EPA — AirData Basic Information), but its material description is generic and has no pinpoint locator.
- `CLM-POWER_SYSTEMS_BASICS-A@1`: “Электроэнергетическая система объединяет производство, передачу, распределение и нагрузку.”
  - `EU-POWER_SYSTEMS_BASICS-A@1` references `SRC-POWER_SYSTEMS_BASICS@1` (NREL — *The North American Electric Power System: The Grid*), but its material description is generic and has no pinpoint locator.

The two Claims currently describe ambient-air monitoring and the functional components of an electricity system. Neither Claim explicitly states the emissions / atmospheric-impact mechanism.

## 6. External primary-source findings

### 6.1 EPA AirData: ambient monitoring and emissions are distinct but connected data domains

Official locator: https://www.epa.gov/outdoor-air-quality-data/airdata-basic-information

Pinpoints inspected:
- Lines 14–21: AirData provides outdoor-monitor data and monitored hourly, daily and annual concentration data.
- Lines 63–65: EPA lists Power Sector Emissions, Operations, and Environmental Data as including power-plant emissions and operating data plus ambient data used to track environmental changes.
- Lines 78–79: EPA explicitly distinguishes ambient monitoring concentrations measured at more than 4,000 stations from emissions data associated with sources such as power plants.

**Assessment:** this is particularly useful because the existing canonical Air Quality Source is this same EPA AirData page. It provides an explicit data-domain bridge while carefully distinguishing source emissions from ambient concentration measurements. It does not say that a monitor measures a particular plant's emissions directly.

### 6.2 EPA Electric Power Sector Basics: generation-related pollution mechanism

Official locator: https://www.epa.gov/power-sector/electric-power-sector-basics

Pinpoints inspected:
- Lines 37–43: the power sector includes interconnected generators and a range of technologies; some power plants burn fuels, while wind, hydro and solar PV do not use the same combustion process.
- Lines 60–61: coal and natural gas are identified as key drivers of the power sector's overall pollution emissions.
- Lines 62–67: fossil-fuel-fired power plants are described as a leading source of air pollution; coal combustion emits SO2 and NOx, NOx contributes to ground-level ozone and fine particulate matter, and other combustion pollutants include mercury.
- Lines 70–79: EPA identifies pollution-control technologies and fuel/efficiency measures that reduce emissions.

**Assessment:** establishes a direct, technically credible mechanism from a subset of electricity generation (especially fossil-fuel combustion) to air pollutants. It does not support a blanket statement that all electricity generation, transmission, distribution or load has the same emissions profile. EPA expressly distinguishes non-combustion generation technologies.

### 6.3 EPA Power Sector Data: direct emissions measurement and quality information

Official locator: https://www.epa.gov/power-sector/power-sector-data

Pinpoints inspected:
- Lines 5–6: EPA collects continuously monitored CO2, NOx, SO2 and mercury emissions data from electric generating units, alongside operations, facility, monitoring-plan and QA-test information.
- Lines 14–23: EPA describes the EPA–EIA data crosswalk and eGRID, which combines emissions and generation data to calculate annual emissions and rates at multiple aggregation levels.

**Assessment:** supplies an operational evidence path between electricity generation and quantified emissions. These are emissions data at generating units, not ambient-air concentration measurements at community monitoring stations.

### 6.4 EPA Power Plants and Neighboring Communities: spatial exposure relevance and limits

Official locator: https://www.epa.gov/power-sector/power-plants-and-neighboring-communities

Pinpoints inspected:
- Lines 27–29: fossil-fuel power-plant emissions include SO2, NOx, particulate matter and other pollutants; the tool identifies potentially exposed communities but explicitly does not evaluate air-quality impacts or quantify population health risk.
- Lines 32–36: the tool covers grid-supplying fossil-fuel plants, emissions and generation information, and nearby/downwind communities.
- Lines 47–48: EPA notes that air pollution can travel long distances, so impacts may occur far from the emitting plant.

**Assessment:** supports spatial relevance and long-range transport as reasons why energy-system emissions matter to air quality beyond the plant boundary. The EPA tool's explicit limitation must be preserved: its mapping does not itself quantify ambient concentration or health risk.

## 7. Adjudication

**Finding:** a direct external cross-domain mechanism is now established. The earlier “no demonstrated mechanism found” description is too strong and should be refined to “official EPA evidence establishes a fossil-fuel generation → pollutant emissions → atmospheric transport / air-quality relevance pathway; canonical endpoint fit and evidence linkage remain incomplete.”

However:
- The current Air Quality Claim describes monitoring ambient concentrations, not effects of power-sector emissions.
- The current Power Systems Claim describes system components, not fuel mix, generating technologies, emissions, or environmental impacts.
- The existing Evidence Use records contain no pinpoint locators for the mechanism above.
- Ambient monitoring, source emissions monitoring, emissions inventories, atmospheric transport, and modeled exposure are distinct evidence types and must not be collapsed.
- The EPA material is U.S.-specific in several of the pages reviewed; do not generalize its regulatory or fleet statistics globally.
- The source supports a bounded relation about fossil-fuel electricity generation and air-quality impacts, not a universal assertion that all grid components or all electricity sources pollute ambient air.

**Disposition:** keep `REL-CROSS-AIR-POWER-SYSTEMS@2` and affected slices on **HOLD**. Upgrade the research finding from “no mechanism” to “direct external bridge identified; endpoint-fit and canonical evidence linkage required.” Do not promote the Relation, change its type/participants, or add locators/provenance without bounded owner authorization and independent semantic review.

## 8. Rights and reuse boundary

This report uses official source identities, URLs, pinpoint locators and independently worded factual summaries only. It proposes no reproduction of EPA text, charts, maps, images, datasets, or other expressive assets. Public accessibility is not treated as a blanket project-level reuse licence. Any future reproduction or dataset inclusion requires item-level rights and terms review under WP2.

No R-01–R-10 owner decision is closed by this review.

## 9. Commands and verification

| Check | Result | Exact SHA / URL | Notes |
|---|---|---|---|
| Exact canonical graph inspection | VERIFIED | `f31f556017aee81b355333b8c4f87307b37969b8` | Relation, Context, Claims, EU and Source records fetched from PR branch |
| EPA primary-source review | VERIFIED | Official EPA URLs and line ranges in §6 | Four official pages inspected |
| Canonical changes | NONE | N/A | Report-only scope |
| CI | NOT RUN | Documentation-only change | Do not claim CI PASS |

No local tests were run. No CI PASS is claimed for this report-only review.

## 10. Unresolved issues, risks, and not done

- No independent air-quality or power-systems subject-matter reviewer was engaged.
- No new Source or Evidence Use record was created.
- No pinpoint locator was added to either existing Evidence Use.
- No Relation or Context version was created.
- No candidate disposition, rights permission, project licence, or release approval was changed.
- No PR merge, main-branch change, allowlist, or publication action was performed.

## 11. Recommendation and acceptance

- **Recommendation:** retain Relation @2 on HOLD; preserve the new finding as a source-backed research update. If the owner later authorizes remediation, define the intended relation narrowly around fossil-fuel electricity generation, emissions, and air-quality impacts, and use precise source/emissions versus ambient-monitoring distinctions.
- **Acceptance status:** CONDITIONAL — evidence review complete; canonical evidence integration, endpoint-fit review, rights review and independent expert review remain open.
- **Reason:** direct external evidence exists, but current Claims and Evidence Use do not yet encode the mechanism or its limits.

## 12. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/air-quality-power-systems-relation-evidence-review-2026-11-20.md`
- **Next owner/action:** if canonical integration is desired, issue a bounded authorization naming exact Source/Evidence Use/Relation fields and versions; then request independent air-quality/power-systems review.

## 13. Integrity statement

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope changed.
- No candidate disposition, INCLUDE/EXCLUDE, HOLD, allowlist, licence, permission, or publication state changed.
- PR #22 remains Draft and unmerged; `main` is untouched.
