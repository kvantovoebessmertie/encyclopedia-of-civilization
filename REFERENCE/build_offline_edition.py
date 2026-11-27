from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from encyclopedia_reference.offline_edition import build_offline_edition
from encyclopedia_reference.selection import build_selected_offline_edition


def load_records(root: Path) -> list[dict]:
    content = root / "CONTENT" / "vertical-slices"
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(content.glob("*/records/*.json"))]


def verify_source_commit(root: Path, requested: str, parser: argparse.ArgumentParser) -> None:
    """Require selection builds to identify the exact checked-out Git revision."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        parser.error("Selected edition builds require Git to verify the source revision.")
    if result.returncode != 0:
        parser.error(
            "Selected edition builds require --root to be inside a Git checkout "
            "so the source revision can be verified."
        )
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
        capture_output=True,
        text=True,
        check=False,
    )
    if status.returncode != 0:
        parser.error("Could not verify the selected edition working-tree state.")
    if status.stdout.strip():
        parser.error(
            "Selected edition builds require a clean Git working tree; "
            "commit or remove modified and untracked files first."
        )
    actual = result.stdout.strip()
    if not requested or requested.casefold() != actual.casefold():
        parser.error(
            f"--source-commit does not match the checked-out HEAD: "
            f"requested {requested or '<missing>'}, actual {actual}."
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a self-contained offline edition.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--edition-id", default="encyclopedia-offline")
    parser.add_argument("--selection-manifest", type=Path, help="Build only the exact approved selection in this JSON manifest.")
    parser.add_argument("--source-commit", help="Exact source commit; required with --selection-manifest.")
    args = parser.parse_args()
    if args.selection_manifest:
        verify_source_commit(args.root, args.source_commit or "", parser)
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
