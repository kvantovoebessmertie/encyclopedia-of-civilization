from __future__ import annotations

import hashlib
import html
import json
from pathlib import Path
from typing import Any


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _display_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def _semantic_html(record: dict[str, Any]) -> str:
    """Render a cautious human-readable summary while preserving raw record data."""
    record_type = str(record.get("record_type", "unknown")).casefold()
    content = record.get("content", {})
    if not isinstance(content, dict):
        content = {}
    parts: list[str] = ['<section class="semantic"><h3>Reader view</h3>']

    def field(label: str, value: Any) -> None:
        if value is None or value == "":
            return
        parts.append(
            '<p><b>' + html.escape(label) + ':</b> '
            + html.escape(_display_value(value)) + '</p>'
        )

    if record_type == "claim":
        statement = content.get("statement")
        if isinstance(statement, str) and statement.strip():
            parts.append('<p class="statement">' + html.escape(statement) + '</p>')
        field("Claim type", content.get("claim_type"))
    elif record_type == "source":
        field("Source", content.get("source_identity"))
        external_ref = content.get("external_ref")
        uri = external_ref.get("uri") if isinstance(external_ref, dict) else None
        if isinstance(uri, str) and uri.startswith(("https://", "http://")):
            safe_uri = html.escape(uri, quote=True)
            parts.append(
                '<p><b>Source link:</b> <a href="' + safe_uri
                + '" rel="noreferrer">' + html.escape(uri) + '</a></p>'
            )
        else:
            field("External reference", external_ref)
    elif record_type == "evidence_use":
        field("Evidence role", content.get("evidence_role"))
        field("Claim reference", content.get("claim_ref"))
        field("Source reference", content.get("source_ref"))
        material = content.get("material")
        if isinstance(material, dict):
            field("Evidence description", material.get("description"))
        else:
            field("Evidence material", material)
    elif record_type == "relation":
        for key in sorted(content):
            field(key.replace("_", " ").capitalize(), content[key])
    else:
        summary = content.get("statement") or content.get("description") or content.get("label")
        if summary:
            field("Summary", summary)

    if len(parts) == 1:
        parts.append('<p>No reader summary is available for this record type.</p>')
    parts.append('</section>')
    return "".join(parts)


def build_public_preview(
    records: list[dict[str, Any]],
    manifest: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    """Build a read-only, explicitly non-release preview from an exact allowlist.

    This prototype intentionally supports preview state only. It is not a
    publication eligibility adjudicator and cannot create a released edition.
    """
    required = (
        "edition_id",
        "edition_state",
        "source_revision",
        "builder_version",
        "selection_policy_version",
        "records",
    )
    missing = [key for key in required if key not in manifest]
    if missing:
        raise ValueError("Manifest missing required fields: " + ", ".join(missing))
    if manifest["edition_state"] != "preview":
        raise ValueError("Prototype builder supports preview state only")
    if not all(isinstance(manifest[key], str) and manifest[key].strip() for key in (
        "edition_id", "source_revision", "builder_version", "selection_policy_version"
    )):
        raise ValueError("Edition identity and version fields must be non-empty strings")
    selections = manifest["records"]
    if not isinstance(selections, list) or not selections:
        raise ValueError("Preview manifest must contain an explicit non-empty record allowlist")

    records_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for record in records:
        key = (record.get("record_id"), record.get("record_version"))
        if not all(isinstance(part, str) and part for part in key):
            raise ValueError("Input record has invalid identity")
        if key in records_by_key:
            raise ValueError(f"Duplicate input record identity: {key[0]} @ {key[1]}")
        records_by_key[key] = record

    selected: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for item in selections:
        if not isinstance(item, dict):
            raise ValueError("Each manifest record selection must be an object")
        record_id = item.get("record_id")
        version = item.get("record_version")
        key = (record_id, version)
        if not all(isinstance(part, str) and part for part in key):
            raise ValueError("Manifest record selection has invalid identity")
        if key in seen:
            raise ValueError(f"Duplicate manifest selection: {record_id} @ {version}")
        seen.add(key)
        if item.get("review_state") != "preview_only":
            raise ValueError("Prototype selections must be marked preview_only")
        note = item.get("preview_note")
        if not isinstance(note, str) or not note.strip():
            raise ValueError("Every preview-only selection requires a visible preview_note")
        record = records_by_key.get(key)
        if record is None:
            raise ValueError(f"Selected record/version not found: {record_id} @ {version}")
        selected.append(record)

    selected.sort(key=lambda record: (record["record_id"], record["record_version"]))
    output_dir.mkdir(parents=True, exist_ok=True)

    cards: list[str] = []
    for index, record in enumerate(selected):
        item = next(
            item for item in selections
            if item["record_id"] == record["record_id"]
            and item["record_version"] == record["record_version"]
        )
        record_id = html.escape(record["record_id"], quote=True)
        record_version = html.escape(record["record_version"], quote=True)
        record_type = html.escape(str(record.get("record_type", "unknown")), quote=True)
        canonical_status = html.escape(str(record.get("publication_status", "unknown")), quote=True)
        preview_note = html.escape(item["preview_note"], quote=True)
        content = html.escape(
            json.dumps(record.get("content", {}), ensure_ascii=False, indent=2, sort_keys=True),
            quote=True,
        )
        search_text = html.escape(
            " ".join((record["record_id"], record["record_version"], str(record.get("record_type", "")),
                      _canonical(record.get("content", {})))).casefold(),
            quote=True,
        )
        semantic = _semantic_html(record)
        cards.append(
            f'<article id="record-{index}" data-search="{search_text}">'
            f'<h2>{record_id}</h2>'
            f'<p><b>Type:</b> {record_type} · <b>Version:</b> {record_version}</p>'
            f'<p><b>Canonical publication_status:</b> {canonical_status} '
            f'<span>(not a truth rating)</span></p>'
            f'<p class="notice">{preview_note}</p>'
            f'{semantic}'
            f'<details><summary>Record content (technical view)</summary><pre>{content}</pre></details>'
            f'</article>'
        )

    edition_id = html.escape(manifest["edition_id"], quote=True)
    source_revision = html.escape(manifest["source_revision"], quote=True)
    builder_version = html.escape(manifest["builder_version"], quote=True)
    policy_version = html.escape(manifest["selection_policy_version"], quote=True)
    page = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow">'
        '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; script-src \'self\'; style-src \'unsafe-inline\'; connect-src \'none\'; img-src \'none\'; base-uri \'none\'; form-action \'none\'; object-src \'none\'">'
        '<title>Encyclopedia — private preview</title>'
        '<style>body{font-family:system-ui,sans-serif;max-width:980px;margin:2rem auto;padding:0 1rem;line-height:1.55}'
        '.banner{border:2px solid #8a5a00;padding:1rem;margin-bottom:1.5rem}'
        'article{border:1px solid #bbb;border-radius:.6rem;padding:1rem;margin:1rem 0;overflow-wrap:anywhere}'
        '.notice{background:#fff3cd;padding:.7rem}pre{white-space:pre-wrap;overflow-wrap:anywhere}'
        'input{font:inherit;padding:.65rem;width:min(100%,34rem)}summary{cursor:pointer}'
        '</style></head><body>'
        '<header class="banner"><h1>Private prototype — not a public edition</h1>'
        '<p>This preview is for interface and security testing only. Inclusion here is not editorial approval, '
        'and technical validation does not establish that a Claim is true. Do not redistribute as an edition.</p>'
        f'<p><b>Edition:</b> {edition_id} · <b>Source revision:</b> {source_revision}</p></header>'
        '<label for="q">Search this preview</label><br><input id="q" type="search" autocomplete="off" '
        'placeholder="Search visible records"><p id="count" aria-live="polite"></p>'
        + "".join(cards)
        + '<script src="search.js" defer></script>'
        f'<footer><p>Builder {builder_version} · Selection policy {policy_version} · State: preview</p></footer>'
        '</body></html>'
    )
    search_script = (
        '"use strict";\n'
        'const q = document.getElementById("q");\n'
        'const cards = [...document.querySelectorAll("article[data-search]")];\n'
        'const count = document.getElementById("count");\n'
        'function filter() {\n'
        '  const term = q.value.trim().toLocaleLowerCase();\n'
        '  let shown = 0;\n'
        '  for (const card of cards) {\n'
        '    const match = card.dataset.search.includes(term);\n'
        '    card.hidden = !match;\n'
        '    if (match) shown++;\n'
        '  }\n'
        '  count.textContent = shown + " of " + cards.length + " records shown";\n'
        '}\n'
        'q.addEventListener("input", filter);\n'
        'filter();\n'
    )
    search_path = output_dir / "search.js"
    search_path.write_text(search_script, encoding="utf-8")
    index_path = output_dir / "index.html"
    index_path.write_text(page, encoding="utf-8")
    output_manifest = {
        "edition_id": manifest["edition_id"],
        "edition_state": "preview",
        "source_revision": manifest["source_revision"],
        "builder_version": manifest["builder_version"],
        "selection_policy_version": manifest["selection_policy_version"],
        "selected_records": [
            {"record_id": record["record_id"], "record_version": record["record_version"]}
            for record in selected
        ],
        "record_count": len(selected),
        "network_required": False,
        "redistribution_allowed": False,
        "index_sha256": hashlib.sha256(index_path.read_bytes()).hexdigest(),
        "search_js_sha256": hashlib.sha256(search_path.read_bytes()).hexdigest(),
        "epistemic_boundary": "preview membership and technical validation do not establish truth",
    }
    (output_dir / "preview-manifest.json").write_text(
        json.dumps(output_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return output_manifest
