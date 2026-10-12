# Bounded Editorial Authorization — SI Units Evidence Pinpoints

Date: 2026-10-12  
Finding: `MVP-SI-PINPOINT-001`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: **AUTHORIZED FOR A NARROW EVIDENCE-USE METADATA CORRECTION ONLY**

## Purpose

Record exact NIST section pinpoints and attribution in two existing Evidence Use records so the SI pilot candidates can be reviewed against a traceable source location. This authorization is not an approval to publish the slice.

## Allowed changes

1. Version `EU-SI-SEVEN-BASE@1` to `@2`, preserving the existing Claim and Source identities/versions, and identify the NIST sections **“Defining Constants”** and **“Base and Derived Units”** relevant to the seven-base-unit statement.
2. Version `EU-SI-DERIVED@1` to `@2`, preserving the existing Claim and Source identities/versions, and identify **“Base and Derived Units”** as the pinpoint for NIST’s category of 22 derived units with special names and symbols.
3. State explicitly that 22 is not the total number of all derived units.
4. Add regression tests for exact versions, claim/source reference integrity, section pinpoints, and the count boundary.
5. Update the SI candidate-screen documentation to distinguish completed pinpoint metadata from remaining Human View/editorial release gates.

## Excluded from scope

- No Claim wording, Claim version, Source record, Scope/Context record, or Relation is to be changed.
- `EU-SI-ACCURACY-BOUNDARY` and its BIPM source remain on HOLD and must not be altered under this authorization.
- No real-record preview allowlist, release manifest, deployment, or hosted intake is authorized.
- No third-party images, diagrams, or graphics are to be copied.

## Source and rights boundary

Source: NIST, [SI Units](https://www.nist.gov/pml/owm/metric-si/si-units). Relevant sections: **“Defining Constants”** and **“Base and Derived Units.”** NIST’s [Copyrights and Disclaimers](https://www.nist.gov/copyrights-disclaimers) states that information on NIST sites is public information unless marked copyrighted and requests appropriate attribution. This correction uses factual paraphrase with source attribution only; the rights basis does not extend to third-party assets or material separately marked copyrighted.

## Acceptance and remaining holds

- Validate the exact versioned Claim/Source references and pinpoints in Reference tests.
- Run Reference Tests, Release Conformance Gate, and Offline Edition on the exact candidate head.
- Inspect the rendered preview and conduct independent reader testing; this desk review alone is not Human View approval.
- Keep both candidate Claims conditional. Do not add a real-record allowlist until editorial review and release gates are complete.
