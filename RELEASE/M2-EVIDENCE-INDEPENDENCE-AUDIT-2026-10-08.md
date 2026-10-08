# M2 EVIDENCE INDEPENDENCE AUDIT — 2026-10-08

## Baseline

- M2 scope lock: `8e6e887e186eab40f60e8d0b2107397a7b6a3397`
- Substantive audit: `6ff368342dc6b62d2f727d5389e57c38176a0224`
- Corpus baseline: 479 vertical slices / 4619 Records / 19 Record types / 51 Relations.

## Audit rule

A second source is justified only when it materially improves at least one of:
- independent corroboration of a foundational claim;
- applicability to a broader or different context;
- terminology authority;
- interpretation of a high-reuse/high-consequence concept.

A second source is not justified merely to increase the source count.

No content correction or new Evidence Use was authored by this audit.

## Results by slice

### 1. measurement-uncertainty-basics — EVIDENCE DEBT CONFIRMED

Current state:
- 1 source: NIST Technical Note 1297.

Finding:
- Independent metrology corroboration is materially useful because the slice establishes foundational terminology that is reused across measurement, statistics, engineering and science.
- The BIPM/JCGM VIM provides an independent metrology vocabulary track for measurement uncertainty, measurand and measurement result concepts.

Recommended role:
- use BIPM/JCGM VIM as a claim-specific corroborating source;
- keep NIST as the existing primary applied measurement source;
- do not duplicate Claims solely for the second source.

### 2. statistics-basics — EVIDENCE DEBT CONFIRMED

Current state:
- 1 source: NIST/SEMATECH Engineering Statistics Handbook.

Finding:
- The current source is authoritative and semantically relevant, but it is oriented toward engineering/scientific statistical practice.
- An independent general introductory statistics source materially improves applicability and independent verification of the basic definition/data/sampling/inference layer.

Recommended role:
- use an independent general statistics source such as OpenStax for Claim A and, where materially appropriate, the data/inference boundary;
- preserve NIST for assumptions, experimental design and engineering/statistical practice;
- keep the existing Scope/Context boundary.

### 3. risk-management-basics — EVIDENCE DEBT CONFIRMED

Current state:
- 1 source: ISO 31000:2018.

Finding:
- ISO is the correct primary normative/reference source.
- Independent corroboration is materially useful for the high-reuse governance/decision-making claim because ISO 31000 is a guideline framework and the encyclopedia uses the concept across multiple domains.
- COSO ERM provides a complementary organizational-governance perspective centered on objectives and enterprise risk management.

Recommended role:
- use COSO only for a narrowly scoped corroborating Evidence Use;
- preserve ISO 31000 as the primary definition/framework source;
- do not imply that COSO and ISO are interchangeable standards.

### 4. agriculture-basics — PASS

Current state:
- 2 sources: FAO + USDA Climate Hubs.
- The dedicated regression already expects 2 sources and the USDA corroboration is claim-specific.

Finding:
- Independent evidence requirement is already satisfied.
- The USDA source adds applicability context around soil, water, climate and management.

No evidence correction required.

### 5. energy-security-basics — EVIDENCE DEBT CONFIRMED

Current state:
- 1 source: International Energy Agency — Energy Security.

Finding:
- IEA is the appropriate primary source, but a second institutional track materially improves applicability because energy security differs by fuel, system and jurisdiction.
- European Commission DG Energy provides an independent policy/operational perspective on security of supply, preparedness, diversification and crisis management.

Recommended role:
- use the European Commission source only for bounded corroboration of supply-security/preparedness concepts;
- preserve IEA as the primary cross-energy-system source;
- explicitly prevent EU-specific mechanisms from becoming universal rules.

### 6. geographic-coordinates-basics — EVIDENCE DEBT CONFIRMED

Current state:
- 1 source: USGS educational/topographic-map reference.

Finding:
- USGS adequately supports the basic educational Claims.
- An independent geospatial standards track materially improves the coordinate-system applicability boundary, especially because coordinates are ambiguous without a defined coordinate reference system.
- Open Geospatial Consortium / ISO 19111-aligned material provides the complementary CRS and coordinate-reference framework.

Recommended role:
- use OGC material for the coordinate-reference-system dimension of Claim C;
- preserve USGS as the educational latitude/longitude source;
- do not turn the slice into a technical CRS standard.

## Confirmed evidence debt summary

- measurement-uncertainty-basics: confirmed
- statistics-basics: confirmed
- risk-management-basics: confirmed
- agriculture-basics: none
- energy-security-basics: confirmed
- geographic-coordinates-basics: confirmed

**Confirmed evidence-independence debt: 5 slices.**

## Important metadata discrepancy

The fresh M2 Gap Map still describes agriculture-basics as a 9-Record / single-source slice. The actual tree is 11 Records / 2 source records and its dedicated regression already encodes that state.

This discrepancy must be reconciled before M2 CLEAN. It must not be resolved by deleting valid corroboration.

## Deferred stages

1. Human View/adversarial audit;
2. cross-domain Relation audit;
3. unified M2 Debt Map;
4. controlled correction pass;
5. re-audit;
6. exact-head Reference + Release Gate + Offline verification.

Evidence audit does not declare M2 CLEAN.
