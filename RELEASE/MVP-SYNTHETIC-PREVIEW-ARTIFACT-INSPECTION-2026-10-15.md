# MVP synthetic preview — artifact inspection record

Date: 2026-10-15  
Source commit: `6c261dfa4b45d11c14fa7de6bce421a146b1bdf9`  
Workflow run: https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/38776377625  
Artifact ID: `11994560411`  
Artifact: `mvp-synthetic-reader-preview-6c261dfa4b45d11c14fa7de6bce421a146b1bdf9`  
Inspection mode: static artifact inspection and manifest/hash verification; browser interaction was attempted but blocked by the execution environment.

## Results

| ID | Check | Result | Evidence / limitation |
|---|---|---|---|
| H01 | Edition identity | PASS | HTML title/banner/footer and manifest identify a private synthetic preview; they explicitly say this is not a public edition and does not establish truth or editorial approval. |
| H02 | Record boundary | PASS | Manifest declares exactly two selected synthetic IDs; HTML contains exactly two article cards, matching `DEMO-CLAIM-001` and `DEMO-SOURCE-001`. |
| H03 | Content legibility | BLOCKED | Static markup contains headings, record type/version, status labels, notices and expandable technical content. Rendered legibility, clipping and hierarchy have not been verified in a working browser. |
| H04 | Narrow viewport | BLOCKED | Browser navigation was blocked by the execution environment (`ERR_BLOCKED_BY_ADMINISTRATOR`); no mobile viewport result is claimed. |
| H05 | Search | BLOCKED | Source review confirms a local filter using `dataset.search` and a visible count, but interactive matching/no-match/repeated-query behavior could not be exercised in the browser. |
| H06 | Navigation and focus | BLOCKED | Keyboard focus order, visible focus and native disclosure interaction were not runtime-tested. |
| H07 | Untrusted text | PASS — static review only | Record-controlled content is HTML-escaped in the generated artifact; search status is assigned through `textContent`, and the search script does not use `innerHTML`. Dynamic adversarial interaction was not runtime-tested. |
| H08 | Network isolation | PASS — static review only | Artifact HTML has CSP `default-src 'none'`, `connect-src 'none'`, and no external resource URLs or image/frame/link dependencies in the inspected markup. Runtime network capture was not possible. |
| H09 | Source transparency | PASS | The displayed source record is explicitly labelled a synthetic placeholder, not a real source; the claim card says its content is synthetic and not verified for publication. |
| H10 | Console/runtime | BLOCKED | Runtime console and resource errors could not be inspected because browser navigation was blocked. |
| H11 | Manifest integrity | PASS | `index.html` SHA-256 matches manifest `8bebf7c96930b2cc64e452fb0712848fd7c8cce2f87ce0434b967403251f341a`; `search.js` SHA-256 matches manifest `3cab55efca98e7998231e235761561d4efff56fd997d3fb0e2d6312cb1e21ad1`. Manifest count (2) matches HTML article count (2). |
| H12 | Release boundary | PASS — artifact only | The artifact labels itself private/non-public and says redistribution is not allowed. This is not a review of deployment permissions or a release authorization. |

## Decision

**Overall: BLOCKED / inspection incomplete.** Static artifact identity, selection boundary, manifest hashes and several source-level security boundaries check out. H03–H06 and H10 still require an actual browser session; H07–H08 require runtime confirmation if the preview is to be accepted.

No real corpus records were included, no canonical records were changed, and no publication or deployment was authorized. This record does not qualify any real Claim or source for public release.

## Next steps

1. Re-run H03–H06 and H10 in a normal desktop browser and a narrow mobile viewport.
2. Exercise search with a match, no match, repeated queries and markup-like input; inspect console and network activity.
3. Attach observations to this record or a versioned follow-up; do not change blocked results to PASS without runtime evidence.
4. Keep the synthetic preview separate from any real-record pilot until rights, source, editorial, privacy, correction/takedown, accountable-owner and release gates are independently satisfied.
