# Offline Edition

Build the complete corpus into a self-contained local edition:

    pip install -e "REFERENCE[test]"
    python REFERENCE/build_offline_edition.py --output offline-edition

Generated files include a static `index.html`, canonical `records.json`, deterministic `records.jsonl`, `records.sqlite3`, and `edition-manifest.json`.

`--edition-id` (default `encyclopedia-offline`) must be an ASCII identifier matching `[A-Za-z0-9][A-Za-z0-9._-]{0,127}`. Other values are rejected before any output is written.

The generated representations require no network connection. The static HTML contains no external resources.

Packaging and integrity do not establish the truth of the underlying knowledge.
