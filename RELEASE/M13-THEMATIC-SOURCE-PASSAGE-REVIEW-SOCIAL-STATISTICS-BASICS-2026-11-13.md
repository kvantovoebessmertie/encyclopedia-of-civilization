# M13 thematic source-passage review — Social Statistics Basics — 2026-11-13

## Status and boundary

Reviewed all three Claims, their Evidence Uses, the UN Statistics Division Source, Context and Scope in `social-statistics-basics` against the M13 branch head `85d93ce8026407d0e374cfb4376e246e3908f24c`.

**Disposition: all three Claims remain HOLD.** The linked UN Statistics Division landing page is a relevant official entry point, but each Evidence Use is generic and no exact passage is identified. The review found direct support for the broad scope of official social statistics, the role of common concepts/classifications/methods in comparability, and the need to prevent misuse and document sources/methods. Claim C contains a measurement/operational-definition proposition that is not established by the cited landing page or the Fundamental Principles alone. No canonical record, score, manifest, or publication state was changed.

## Claim-by-claim findings

### CLM-SOCIAL_STATISTICS_BASICS-A@1

**Claim:** Social statistics covers data about populations, social conditions, and related aspects of societal life.

- UN Fundamental Principle 1 states that official statistics provide information about the economic, demographic, social, and environmental situation for government, the economy, and the public. This directly supports the demographic/social scope.
- The UN Statistics Division's Demographic and Social Statistics programme page is the correct institutional entry point for the domain, but it is a programme landing page rather than a precise definition of “social statistics”.
- Existing `EU-SOCIAL_STATISTICS_BASICS-A@1` only states that the source is used within its material; it contains no pinpoint or claim-specific description.
- **Disposition: HOLD.** The broad idea is supported by Principle 1, but the current Evidence Use must identify that principle and the claim should not imply an exhaustive taxonomy of all social-statistical domains.

### CLM-SOCIAL_STATISTICS_BASICS-B@1

**Claim:** Comparability of statistical data depends on definitions of indicators, classifications, and collection methodology.

- UN Fundamental Principle 9 states that international concepts, classifications, and methods promote consistency and efficiency across official statistical systems. The UN implementation guidance explains that common standards improve quality and comparability and that non-comparable statistics lose utility.
- UN Fundamental Principle 3 requires statistical agencies to present information according to scientific standards on sources, methods, and procedures to facilitate correct interpretation.
- The UN Statistics Division implementation guidance also says that concepts, definitions, classifications, data-collection and processing procedures, and quality assessments should be documented and made publicly accessible.
- Existing `EU-SOCIAL_STATISTICS_BASICS-B@1` is generic and does not cite Principle 3 or 9 or the implementation guidance.
- **Disposition: HOLD.** Strong direct support exists for common definitions/classifications/methods and transparent metadata. Exact principle/paragraph locators are missing from the current Evidence Use.

### CLM-SOCIAL_STATISTICS_BASICS-C@1

**Claim:** A statistical indicator describes an operationally defined set of observations and should not automatically be interpreted as a causal explanation.

- UN Fundamental Principle 4 explicitly addresses prevention of misuse of statistics. Principle 3 requires transparent sources, methods, and procedures to support correct interpretation.
- These principles support the caution against misuse and the need to understand how a statistic was produced. They do **not**, by themselves, define an indicator as an “operationally defined set of observations”, nor do they establish the full causal-inference distinction in the Claim.
- The current UN Statistics Division source is too broad to support the measurement-theory portion of the Claim. No linked evidence identifies a direct methodological passage on operational definitions, indicators, or causal inference.
- Existing `EU-SOCIAL_STATISTICS_BASICS-C@1` is generic.
- **Disposition: HOLD.** Split the proposition or add a source that directly defines statistical indicators and a separate source for the descriptive-versus-causal inference boundary. Do not infer causality guidance solely from a general principle against misuse.

## Cross-record findings

1. All three Evidence Uses point to their intended Claims and to the intended UN Statistics Division Source.
2. All three Evidence Use descriptions are essentially the same generic statement and do not provide claim-specific support or pinpoint locations.
3. The Source record identity is a real UN Statistics Division programme, but the landing page is not a specific standard, handbook, or definition. It should not be treated as if every claim in the slice were directly supported by that page.
4. Context and Scope are general editorial framing. They do not provide evidence for the claims.
5. The slice concerns official social statistics. Avoid silently generalizing its institutional standards to every form of social research or every non-official indicator.

## Required next steps

- For Claim A, cite UN Fundamental Principle 1 and identify the relevant Demographic and Social Statistics programme areas as context, not as a substitute for a formal definition.
- For Claim B, cite Principles 3 and 9 and the exact UN implementation-guidance passages on documentation, common concepts/classifications/methods, and comparability.
- For Claim C, either narrow it to the directly supported “statistics require context and should not be misused” statement, or add independent methodological sources defining indicators/operationalization and explaining why descriptive association does not by itself establish causation.
- Version each Evidence Use with claim-specific locators only under bounded editorial authorization, then update regression tests/manifests as required and rerun exact-head CI.
- This desk review does not authorize canonical changes, final D/E/B scores, or publication approval.

## Sources reviewed

- UN Statistics Division, Demographic and Social Statistics: https://unstats.un.org/unsd/demographic-social/
- UN Statistics Division, Fundamental Principles of Official Statistics: https://unstats.un.org/fpos
- UN Fundamental Principles implementation guidance, Principle 1 and Principle 9 sections: https://unstats.un.org/capacity-development/handbook/html/Handbook/C3/UN_Fundamental_Principles_of_Official_Statistics.htm
- UN Statistics Division, implementation guidance on concepts, definitions, classifications, sources, methods and procedures: https://unstats.un.org/unsd/methods/statorg/principles_stat_activities/principles_stat_activities.asp
- UNECE, Fundamental Principles of Official Statistics: https://unece.org/statistics/FPOS
