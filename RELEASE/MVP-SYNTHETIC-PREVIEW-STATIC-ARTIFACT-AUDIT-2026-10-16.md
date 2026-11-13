# MVP synthetic reader — static artifact audit

Date: 2026-10-16  
Branch: `mvp-reader-prototype-2026-10-11`  
Source commit: `6a0ba5be7581e2b85aa3626c81dab40bba294898`  
Workflow artifact: `mvp-synthetic-reader-preview-6a0ba5be7581e2b85aa3626c81dab40bba294898`  
Artifact ID: `11995067588`

## Scope and limitation

This report records static inspection of the exact generated artifact ZIP and a Node-based behavioral test of the bundled search script. It is **not** the required full human visual/browser inspection and does not authorize release.

## Artifact integrity

| File | SHA-256 | Manifest match |
|---|---|---|
| `index.html` | `8bebf7c96930b2cc64e452fb0712848fd7c8cce2f87ce0434b967403251f341a` | PASS |
| `search.js` | `3cab55efca98e7998231e235761561d4efff56fd997d3fb0e2d6312cb1e21ad1` | PASS |

Manifest reports `record_count: 2`, `network_required: false`, `redistribution_allowed: false`, and `source_revision: synthetic-fixture-only`. The two selected records are `DEMO-CLAIM-001@1.0` and `DEMO-SOURCE-001@1.0`.

## Static checks

| Check | Result | Evidence |
|---|---|---|
| Edition boundary | PASS | Visible banner says private prototype, not public edition; synthetic-only source revision is explicit |
| Record boundary | PASS | Artifact contains exactly two synthetic demo records; no canonical corpus records found |
| Search script structure | PASS | Uses local DOM only; no fetch/XHR or network API calls |
| Content Security Policy | PASS (static) | `default-src 'none'`, `connect-src 'none'`, `img-src 'none'`, `base-uri 'none'`, `form-action 'none'`, `object-src 'none'`; script source limited to self |
| Third-party dependencies | PASS (static) | No remote script, stylesheet, image, font, or other asset reference found in the HTML |
| Search behavior | PASS (Node mock-DOM test) | Default shows 2/2; matching query shows 1/2; no-match shows 0/2; whitespace resets to 2/2 |
| Manifest hashes | PASS | SHA-256 of the extracted HTML and JS match the manifest |
| Mobile layout / clipping | BLOCKED | Chromium headless screenshot attempt timed out in this environment; visual layout was not certified |
| Keyboard navigation / visible focus | BLOCKED | Not verified in a functioning browser session |
| Runtime console and real DOM behavior | BLOCKED | Mock-DOM test does not replace an actual browser runtime test |
| Injection behavior under adversarial record content | PARTIAL | This fixture is synthetic and contains no adversarial payload; no end-to-end hostile fixture test was performed |
| Publication / deployment boundary | PASS (static) | Artifact labels itself preview-only; no publish or deploy action is represented by this artifact |

## Decision

**Static artifact checks: PASS with limitations. Full human inspection: NOT COMPLETE.**

The browser screenshot attempt failed to complete, so this report does not mark mobile legibility, visual hierarchy, keyboard interaction, or browser console checks as passed. The existing `MVP-SYNTHETIC-PREVIEW-HUMAN-INSPECTION-CHECKLIST-2026-10-14.md` remains the controlling checklist and must not be marked complete from this report alone.

This artifact contains synthetic fixture data only. It is not a public edition and does not qualify real Claims, Sources, Evidence Use records, or other corpus material for release.
