from __future__ import annotations

import argparse
import json
from pathlib import Path

from encyclopedia_reference.public_reader import build_public_preview


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a private, non-release reader prototype.")
    parser.add_argument(
        "--records",
        type=Path,
        default=ROOT / "REFERENCE" / "fixtures" / "public-preview-records.json",
        help="JSON file containing an array of records",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "REFERENCE" / "fixtures" / "public-preview-manifest.json",
        help="Preview-only allowlist manifest",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = json.loads(args.records.read_text(encoding="utf-8"))
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = build_public_preview(records, manifest, args.output)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
