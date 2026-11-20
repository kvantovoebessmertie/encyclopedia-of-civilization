from __future__ import annotations

import argparse
import json
from pathlib import Path

from encyclopedia_reference.offline_edition import build_offline_edition
from encyclopedia_reference.selection import build_selected_offline_edition


def load_records(root: Path) -> list[dict]:
    content = root / "CONTENT" / "vertical-slices"
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(content.glob("*/records/*.json"))]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a self-contained offline edition.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--edition-id", default="encyclopedia-offline")
    parser.add_argument("--selection-manifest", type=Path, help="Build only the exact approved selection in this JSON manifest.")
    parser.add_argument("--source-commit", help="Exact source commit; required with --selection-manifest.")
    args = parser.parse_args()
    records = load_records(args.root)
    if not records:
        raise SystemExit("No canonical records found")
    if args.selection_manifest:
        selection = json.loads(args.selection_manifest.read_text(encoding="utf-8"))
        manifest = build_selected_offline_edition(
            records, selection, args.output,
            source_commit=args.source_commit or "",
            edition_id=args.edition_id,
        )
    else:
        manifest = build_offline_edition(records, args.output, args.edition_id)
    print(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
