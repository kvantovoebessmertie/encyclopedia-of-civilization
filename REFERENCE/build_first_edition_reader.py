from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from encyclopedia_reference.first_edition_reader import build_first_edition_reader
from encyclopedia_reference.selection import build_selected_offline_edition


def load_records(root: Path) -> list[dict]:
    content = root / "CONTENT" / "vertical-slices"
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(content.glob("*/records/*.json"))]


def verify_source_commit(root: Path, requested: str, parser: argparse.ArgumentParser) -> None:
    try:
        head = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        parser.error("First-edition reader builds require Git to verify the source revision.")
    if head.returncode != 0:
        parser.error("The selected --root must be inside a Git checkout.")
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
        capture_output=True, text=True, check=False,
    )
    if status.returncode != 0 or status.stdout.strip():
        parser.error("First-edition reader builds require a clean Git working tree.")
    actual = head.stdout.strip()
    if not requested or requested.casefold() != actual.casefold():
        parser.error(f"--source-commit does not match checked-out HEAD: requested {requested!r}, actual {actual!r}.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a chapter-organized reader from an approved schema-1.1 first-edition selection."
    )
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--selection-manifest", type=Path, required=True)
    parser.add_argument("--chapter-map", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--edition-id", default="encyclopedia-first-edition")
    args = parser.parse_args()

    verify_source_commit(args.root, args.source_commit, parser)
    records = load_records(args.root)
    if not records:
        raise SystemExit("No canonical records found")
    selection = json.loads(args.selection_manifest.read_text(encoding="utf-8"))
    chapter_map = json.loads(args.chapter_map.read_text(encoding="utf-8"))
    manifest = build_first_edition_reader(
        records, selection, chapter_map, args.output,
        source_commit=args.source_commit,
        edition_id=args.edition_id,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
