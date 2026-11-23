# Offline Edition

Build the complete corpus into a self-contained local edition:

    pip install -e "REFERENCE[test]"
    python REFERENCE/build_offline_edition.py --output offline-edition

Generated files include a static \`index.html\`, canonical \`records.json\`, deterministic \`records.jsonl\`, \`records.sqlite3\`, and \`edition-manifest.json\`.

The generated representations require no network connection. The static HTML contains no external resources.

## Edition identifier contract

\`--edition-id\` is an identifier, not free-form display text. It must be 1–128 ASCII characters, start with an ASCII letter or digit, and contain only ASCII letters, digits, dots (\`.\`), underscores (\`_\`) or hyphens (\`-\`). The same validation is applied by the command-line interface and the Python build function. Invalid values are rejected before the output directory or any output file is created. The HTML renderer also escapes the identifier as defense in depth.

Existing identifiers such as \`encyclopedia-offline\`, \`encyclopedia-4686-09\`, \`full-corpus-offline-v1\` and \`same\` satisfy this contract.

Packaging and integrity do not establish the truth of the underlying knowledge.
