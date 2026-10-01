from __future__ import annotations

import argparse
import json
from pathlib import Path

from encyclopedia_reference.offline_edition import build_offline_edition


def load_records(root: Path) -> list[dict]:
    content = root / "CONTENT" / "vertical-slices"
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(content.glob("*/records/*.json"))]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a self-contained offline edition.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--edition-id", default="encyclopedia-offline")
    args = parser.parse_args()
    records = load_records(args.root)
    if not records:
        raise SystemExit("No canonical records found")
    print(json.dumps(build_offline_edition(records, args.output, args.edition_id), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
