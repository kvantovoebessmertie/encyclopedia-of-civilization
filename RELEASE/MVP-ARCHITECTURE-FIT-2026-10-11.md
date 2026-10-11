# Public MVP Architecture Fit Assessment — 2026-10-11

## Status

Initial repository inspection, based on `main` as read on 2026-10-11. This is a design assessment, not a runtime security certification. The inspected files are listed below so the conclusions can be rechecked against a later commit.

## Executive finding

**Do not start with a new web framework or database.** The repository already specifies a publication layer and portable/offline package, and it has a working first implementation of a deterministic offline edition. The smallest path is to extend the existing Publication Builder/offline pipeline into a curated, safe, reader-oriented publication, then add a separate contribution intake service.

However, the current offline HTML output is a raw technical record dump, not a suitable public reader, and it embeds record-controlled values into HTML without explicit HTML escaping. That must be treated as a release-blocking security issue before any untrusted or externally contributed content can be rendered. This assessment does not claim an exploit was executed.

## Existing capabilities and fit

| Existing asset | Observed capability | MVP fit | Gap / action |
|---|---|---|---|
| `IMPLEMENTATION/012-PUBLICATION-BUILDER.md` | Normative design for deriving publications from canonical Records; version pinning, citations, deterministic builds, offline output, security invariants | Strong architectural foundation | Implement explicit curated selection, public manifest, human-readable composition, publication eligibility checks, and release state |
| `REFERENCE/src/encyclopedia_reference/publication.py` | Produces derived entries from supplied Records and attaches Evidence Use references to Claims | Reusable base | It currently serializes supplied records without an eligibility/selection gate or full reader-oriented rendering; confirm version and relationship handling |
| `REFERENCE/build_offline_edition.py` and `REFERENCE/src/encyclopedia_reference/offline_edition.py` | Builds JSON, JSONL, SQLite, a basic HTML file, and a hash manifest without network access | Useful deterministic/offline base | Current HTML is a technical dump, not a curated reader; escape every record-derived HTML value, add manifest selection/provenance, and exclude non-approved records |
| `IMPLEMENTATION/009-PORTABLE-PACKAGE.md` | Defines portable, versioned, integrity-checkable package and partial-export semantics | Supports independence and offline distribution | Public edition must explicitly identify itself as a curated partial publication, not a complete archive |
| `IMPLEMENTATION/011-QUERY-EDIT-INTERFACE.md` | Defines query/edit semantics, history, permissions, audit, read-only behavior | Supports the conceptual access boundary | Public MVP should be read-only; contribution intake must not be implemented as direct canonical edit |
| `IMPLEMENTATION/010-STORAGE-ADAPTER.md` | Specifies storage abstraction and separation from UI/backend | Potentially useful for later service | Do not add a database just for MVP; first inspect actual implementation and operational needs |
| `REFERENCE/README.md` | Documents current reference package and existing checks | Gives implementation/test entry point | Confirm exact-head workflows after any code change |
| `.github/workflows/reference-tests.yml`, `release-gate.yml`, `offline-edition.yml` | Existing automated release layers | Reuse rather than duplicate | Add targeted publication/security tests and run all required workflows on the exact release candidate |

## Important separation of statuses

The public edition needs two different state systems:

1. **Canonical Record `publication_status`** — preserve the semantics already defined by the existing architecture.
2. **Edition membership/release state** — whether a specific version of a Record was deliberately included in a named public edition after editorial eligibility checks.

Do not infer epistemic reliability from either publication membership or a passing build. The edition manifest should carry the pinned Record IDs/versions, source revision, builder version, selection policy version, build digest, and known exclusions/limitations.

## Initial security finding

In `REFERENCE/src/encyclopedia_reference/offline_edition.py`, the current HTML builder concatenates record-derived values (including identifiers, types, and serialized content) directly into HTML strings. No explicit HTML escaping is performed at those insertion points.

**Required before public use:**
- escape text and attribute values in all HTML contexts, or use a safe template/rendering mechanism;
- never treat Record content as executable HTML;
- test adversarial strings such as `<script>`, `</pre>`, quotes, ampersands, and Unicode edge cases;
- test that output remains text and does not create new DOM elements/scripts from Record content;
- apply the same policy to any new web renderer and source metadata.

No untrusted external submissions should be rendered through this path until this issue is fixed and regression-tested.

## Recommended implementation path

### Step 1 — safe publication builder

1. Define a versioned, explicit publication manifest and curated sample selector.
2. Reuse the existing canonical Record and reference-resolution logic.
3. Add eligibility validation that is separate from technical schema/CI validation.
4. Generate reader-oriented pages: topic, Claim, source/evidence, applicability, uncertainty, Relations, review notes intended for public display, and change history.
5. Escape all untrusted content and apply a restrictive content security policy if a web-hosted renderer is used.
6. Keep the public output read-only and self-contained where practical.
7. Add tests for selection exclusion, provenance, stable IDs, escaping, broken references, determinism, and offline access.

### Step 2 — curated sample

Select a small set only after checking actual Records and their source/evidence/relation closure. Use an explicit manifest rather than a broad corpus glob. Start with non-high-consequence topics that have sufficient review evidence; high-consequence content requires the stronger existing safety review. The precise topic set is still undecided.

### Step 3 — intake as a separate service

Start with a structured form that writes to an isolated submission queue. It may use repository issues or a simple restricted store during a pilot, but must not write canonical JSON directly. Choose a provider only after privacy, licensing, abuse controls, and operational ownership are settled.

### Step 4 — deployment decision

After the safe static prototype works, decide whether static hosting is sufficient for read-only pages and whether the contribution queue needs a separate backend. Do not couple the public reader and contribution intake into one privileged service unnecessarily.

## Test matrix for the next implementation phase

- **Selection:** only manifest-approved record/version pairs are rendered; excluded and draft records remain absent.
- **Traceability:** every displayed Claim has stable identity and resolvable links to applicable evidence/source records.
- **Semantics:** Scope, Context, uncertainty, limitations, and disagreement are not dropped by composition.
- **HTML safety:** malicious-looking record text is rendered literally, not interpreted as markup or script.
- **Reproducibility:** identical pinned inputs and builder version yield equivalent output and manifest.
- **Offline:** reader navigation works without network for a self-contained edition.
- **Privacy:** no contributor contact details, internal notes, or submission queue data enter the public artifact.
- **Release integrity:** failed or partial builds cannot be marked released.
- **Human View:** representative readers understand review labels and applicability boundaries.
- **Regression:** existing Reference, Release Gate, and Offline Edition workflows pass on the exact candidate.

## Current decisions and unresolved inputs

- Public reader language: undecided.
- Pilot topic set: undecided pending record-level eligibility review.
- Hosting/domain: undecided; no production deployment is implied.
- Content license and contributor terms: must be approved before open intake.
- Submission storage and retention: undecided.
- Named editorial and urgent-correction owner: must be assigned before public contribution intake.
- No code change has yet been made to the canonical implementation or the offline builder by this workstream.
