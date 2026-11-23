# First-edition reader shell (internal preview)

This directory contains a self-contained, dependency-free navigation prototype for the first edition's 19-chapter structure.

## Open locally

Open `index.html` in a modern browser. The shell uses only local CSS and JavaScript. It has no remote fonts, analytics, external scripts, API calls or network data dependencies.

## What works

- Two-part, 19-chapter navigation.
- Chapter and subsection outline.
- Search across chapter titles and subsection text.
- Keyboard-accessible native links and search input.
- Responsive layout for desktop and narrow screens.
- Reduced-motion support.
- Content Security Policy and no inline script.
- Explicit status for every chapter.

## What is intentionally not present

No canonical Claim records, source excerpts, health/safety procedures, recommendations, external images or user submissions are loaded. The shell states that no publication-approved articles are currently present. A chapter heading or candidate slice does not grant publication status.

This is an internal editorial navigation build, not a public edition, not a release candidate and not a substitute for the exact-version selection-aware offline builder. Do not deploy or redistribute it as an Encyclopedia release.

## Adding approved content later

Content must be rendered only from the frozen schema-1.1 exact-version selection manifest after:
- explicit INCLUDE decision and APPROVED attestation;
- exact record/type/schema pins and complete dependency closure;
- source locator and Context/Scope verification;
- item-level rights and attribution clearance;
- consequence-appropriate expert review and independent Human View;
- accountable editor and release-approver sign-off.

The navigation shell must not read all corpus records or infer approval from slice membership, historical evaluations, completion fields or CI.
