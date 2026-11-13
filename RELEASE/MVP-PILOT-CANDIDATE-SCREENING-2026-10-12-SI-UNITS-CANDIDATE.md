# MVP Pilot Candidate Screen — SI Units Basics

Date: 2026-10-12  
Branch: `mvp-public-contribution-design-2026-10-11`  
Disposition: **strong candidate for a small, low-consequence pilot; not approved or allowlisted**

## 1. Why screen this slice

The SI-units slice contains three narrowly scoped Claims. Two are factual statements about the structure of the International System of Units and have a direct official NIST source. They are a better initial pilot candidate than sources with unclear reuse terms or higher-consequence operational guidance. This screen does not approve the whole slice or the third Claim.

## 2. Candidate Claims and source fit

### `CLM-SI-SEVEN-BASE@1`

Claim: “SI consists of seven base units whose definitions are expressed through fixed values of defining constants.”

- Existing Source: `SRC-NIST-SI-UNITS@1`
- Existing Evidence Use: `EU-SI-SEVEN-BASE@1`
- Source: NIST, [SI Units](https://www.nist.gov/pml/owm/metric-si/si-units)
- Pinpoint candidate: the page's **Defining Constants** and **Base and Derived Units** sections. NIST identifies seven defining constants and the seven base SI units; the related NIST [Definitions of SI Base Units](https://www.nist.gov/si-redefinition/definitions-si-base-units) page gives the individual definitions.
- Fit: **direct**, subject to adding the pinpoint to the canonical Evidence Use and confirming the displayed claim wording does not conflate defining constants with the seven base units.

### `CLM-SI-DERIVED@1`

Claim: “In addition to seven base units, SI includes derived units; NIST notes 22 derived units with special names and symbols.”

- Existing Source: `SRC-NIST-SI-UNITS@1`
- Existing Evidence Use: `EU-SI-DERIVED@1`
- Source: NIST, [SI Units](https://www.nist.gov/pml/owm/metric-si/si-units)
- Pinpoint candidate: the page's **Base and Derived Units** section, specifically its statement that the seven base units define 22 derived units with special names and symbols. NIST's [SI Learning Hub](https://www.nist.gov/pml/owm/si-learning-hub) repeats this distinction and describes the 29-unit core set.
- Fit: **direct** for the count and distinction. The number is tied to NIST's defined category “derived units with special names and symbols”; it should not be paraphrased as the total number of derived units.

### `CLM-SI-ACCURACY-BOUNDARY@1`

- Existing Source: `SRC-BIPM-SI-BROCHURE-2026@1`
- Existing Evidence Use: `EU-SI-ACCURACY-BOUNDARY@1`
- Disposition: **HOLD / exclude from first pilot for now**. It draws a boundary between unit definitions and practical measurement accuracy/uncertainty and cites BIPM material. The exact passage-level pinpoint, rights/attribution review for the relevant BIPM material, and technical Human View review are not closed by this screen.

## 3. Rights and attribution screen

NIST's [Copyrights & Disclaimers](https://www.nist.gov/copyrights-disclaimers) page states that, except for material marked as copyrighted, information on NIST sites is public information and may be distributed or copied; appropriate byline/photo/image credits are requested.

Working disposition for this candidate:
- Use only the relevant factual text and paraphrase it; do not copy graphics or photographs.
- Preserve attribution to NIST and the exact page URL.
- Treat any separately credited/copyright-marked image, diagram, or third-party item as excluded unless its rights are separately verified.
- Record the rights basis in the pilot manifest/review log before enabling real-record preview.

This is a promising rights basis, not a blanket license for every asset on the page.

## 4. Minimum work before allowlisting

1. Add versioned, claim-specific pinpoints to the two Evidence Use records on the canonical content branch; preserve prior versions.
2. Verify exact source identity, URI, Claim wording, Evidence Use links, and schema/reference validation.
3. Check the public rendering for unit symbols, superscripts, accessibility, attribution, source navigation, and Claim-level status.
4. Conduct Human View review and record an editorial decision for each Claim independently.
5. Add only the exact approved record IDs and versions to the preview manifest. Keep `CLM-SI-ACCURACY-BOUNDARY@1` excluded until its separate review is complete.
6. Re-run Reference Tests, Release Conformance Gate, Offline Edition, security checks, and inspect the generated preview on the exact release candidate.

## 5. Decision

**Candidate shortlist: `CLM-SI-SEVEN-BASE@1` and `CLM-SI-DERIVED@1`, conditional on remediation and review.**

No canonical Claim/Source/Evidence Use records were changed by this screening note. No real-record preview allowlist was created. The reader prototype must remain synthetic-fixture-only until the exact versioned evidence pinpoints, rights/attribution, Human View, and editorial approvals are recorded.


## Bounded pinpoint correction — 2026-10-12

Under `MVP-SI-PINPOINT-001` (see `RELEASE/MVP-CORRECTION-AUTHORIZATION-SI-UNITS-2026-10-12.md`), two existing Evidence Use records have now been versioned:

- `EU-SI-SEVEN-BASE@2` records the NIST sections “Defining Constants” and “Base and Derived Units,” preserves the distinction between seven base units and seven defining constants, and adds attribution.
- `EU-SI-DERIVED@2` records “Base and Derived Units” and explicitly states that 22 refers to derived units with special names and symbols, not the total number of derived units.
- Both retain the existing Claim @1 and NIST Source @1 references. Claim wording, Source records, and the third Evidence Use were not changed.
- Regression coverage now checks exact versions, references, pinpoints, attribution, and the count boundary.

This resolves the missing section-pinpoint metadata for the two conditional candidates; it does **not** resolve publication approval. The accuracy/uncertainty Claim remains HOLD. The two candidates still require exact-head CI, rendered-page inspection, independent reader testing, and editorial sign-off before any real-record allowlist is created. The rights basis is limited to factual paraphrase and attribution of NIST information; it does not extend to third-party assets or separately copyrighted material.
