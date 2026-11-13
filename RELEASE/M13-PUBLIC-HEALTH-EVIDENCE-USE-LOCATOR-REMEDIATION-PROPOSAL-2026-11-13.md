# M13 — public-health-basics Evidence Use locator remediation proposal

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Baseline: `38d121de86acc67cdf7ebdbd231733947ff245f5`
Status: noncanonical review/proposal only; no editorial authorization granted by this document.

## Purpose and boundary

The 2026-11-13 source-passage desk review examined four Claims and four linked Evidence Uses in `public-health-basics`. It found direct support for the central propositions in A, B and D, and population-level support with a residual scope gap in C. All four Evidence Uses lack reproducible claim-specific locators.

This document records proposed locator text and the remaining source-scope issue. It does **not** authorize canonical edits, new Source records, D/E/B scoring, publication, or a change to any Claim. The current `RELEASE/EDITORIAL-CORRECTION.json` does not contain a public-health-basics authorization. Do not edit canonical JSON until a bounded authorization is explicitly added and registered.

## Verified source passages

### Existing WHO Source — `SRC-PUBLIC_HEALTH_BASICS@1`

Identity: WHO European Observatory on Health Systems and Policies, “Public health”.
URI: https://eurohealthobservatory.who.int/themes/health-system-functions/public-health

Current page structure checked 2026-11-13:
- Section heading: “Public health”.
- Opening body paragraph: public health aims to improve the health of populations, keep people healthy and prevent disease.
- Immediately following body paragraph: defines the population-health orientation and enumerates surveillance of population health, response to health hazards and emergencies, health protection, health promotion and disease prevention/early detection.

### Existing CDC Source — `SRC-CDC-PUBLIC_HEALTH-2026@1`

Identity: CDC, “Introduction to Public Health”, Public Health 101 Series.
URI: https://www.cdc.gov/training-publichealth101/php/training/introduction-to-public-health.html

Current page structure checked 2026-11-13:
- “At a glance” paragraph: course overview includes core public-health functions and essential services, determinants of health and the Health Impact Pyramid.
- “Learning Objectives”: bullet 4 identifies core public-health functions and essential services; bullet 6 lists determinants of health; bullet 7 connects individual determinants to population health.

## Proposed Evidence Use descriptions — pending authorization

The following are proposed descriptions only. They preserve the existing Claim and Source references and evidence role. They do not change the canonical records.

### `EU-PUBLIC_HEALTH_BASICS-A@1`

Proposed Russian description:

> WHO European Observatory, “Public health”, section “Public health”, opening body paragraph: directly supports the proposition that public health aims to improve population health and prevent disease. The immediately following body paragraph provides corroborating detail on population-health activities. The passage supports the general purpose stated in the Claim; it is not a complete taxonomy of public-health functions.

Disposition after locator repair: source fit appears direct; retain HOLD until the authorized versioned edit, regression, independent review and publication gates are complete.

### `EU-PUBLIC_HEALTH_BASICS-B@1`

Proposed Russian description:

> WHO European Observatory, “Public health”, section “Public health”, second body paragraph: directly identifies surveillance of population health, response to health hazards and emergencies, health protection, health promotion and disease prevention, including early detection. These passages support the four activity groups summarized in the Claim. The list is illustrative, not an exhaustive taxonomy of public-health functions.

Disposition after locator repair: source fit appears direct; retain HOLD until the authorized versioned edit, regression, independent review and publication gates are complete.

### `EU-PUBLIC_HEALTH_BASICS-C@1`

Proposed Russian description, limited to what the existing linked source establishes:

> WHO European Observatory, “Public health”, section “Public health”, opening and second body paragraphs: the stated objective is improvement of the health of populations, and the listed surveillance activity explicitly concerns population health. This supports the population-level orientation of the Claim. The passage does not by itself establish a distinct community-engagement function or imply that public-health services are never delivered to individuals.

Residual source-scope issue:
- The Claim explicitly mentions both groups and communities.
- The existing WHO Observatory page establishes population-level orientation but does not explicitly name community engagement in the cited paragraphs.
- WHO’s separate “Essential public health functions” page includes the function “Community engagement and social participation” in its unified list. This is a separate source and is not represented by a canonical Source record in this slice.
- If direct support for the community-engagement wording is required, adding that WHO page as a separate versioned Source and linking it through a versioned Evidence Use requires its own bounded authorization, regression and coverage reconciliation. Do not silently treat the external page as already linked.

Disposition: HOLD. Existing source pinpoint would improve reproducibility but does not fully close the community-specific source-fit gap.

### `EU-PUBLIC_HEALTH_BASICS-D-CDC@1`

Proposed Russian description:

> CDC, “Introduction to Public Health”, section “At a glance”: the course overview explicitly includes core public-health functions, essential services and determinants of health. In “Learning Objectives”, bullets 4, 6 and 7 respectively cover recognition of core functions and essential services, identification of health determinants, and the effect of individual determinants on population health. The Claim describes the course’s coverage; it does not treat this overview as a complete technical definition of public health.

Disposition after locator repair: source fit appears direct for the attributed course-description Claim; retain HOLD until the authorized versioned edit, regression, independent review and publication gates are complete.

## Proposed bounded authorization scope

If the project owner elects to authorize remediation, the smallest safe scope is:

1. Create a named M13 authorization limited to `public-health-basics`.
2. Permit versioned updates to the four existing Evidence Use records A, B, C and D, with the descriptions above; do not change Claim wording, existing Source identities/URIs, Context, Scope, Relations or unrelated slices.
3. Treat Claim C as a partial locator repair only unless a separate WHO EPHF Source is explicitly authorized and added with exact provenance and a dedicated Evidence Use reference.
4. Strengthen only `REFERENCE/tests/test_content_public_health_basics_vertical_slice.py` to assert the required claim-specific locator content, Russian-facing descriptions, preserved exact Claim/Source references, roles and record counts. Add assertions for the explicit limitation on C.
5. Update only the public-health-basics README and required M13 audit/authorization/coverage metadata, if the schema and preflight require it.
6. Run schema/preflight, targeted regression, Reference implementation tests, Release Conformance Gate and Offline Edition on one exact final SHA. Independently verify the diff, PR base/head and unchanged `main`.

## Acceptance conditions

- No generic repeated description remains in the four authorized Evidence Uses.
- Each locator names the exact page section and paragraph/bullet set and states what proposition it supports.
- Claim C's community-engagement gap is either explicitly retained as HOLD or closed only with an authorized separate WHO EPHF Source.
- No D/E/B score is inferred from the locator edit.
- All four Claims remain HOLD until independent human review, specialist review where appropriate, Human View, source-independence, rights/attribution and editorial approval are separately evidenced.
- No change to `main`; PR #21 remains Draft/unmerged.

## Source register

- WHO European Observatory on Health Systems and Policies, “Public health”: https://eurohealthobservatory.who.int/themes/health-system-functions/public-health
- WHO, “Essential public health functions” (separate source; not currently linked by a canonical Source record in this slice): https://www.who.int/teams/primary-health-care/health-systems-resilience/essential-public-health-functions
- CDC, “Introduction to Public Health”: https://www.cdc.gov/training-publichealth101/php/training/introduction-to-public-health.html

---
This proposal is not an authorization, a canonical correction, a D/E/B assessment, independent review, or publication approval.
