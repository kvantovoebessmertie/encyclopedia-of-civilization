from __future__ import annotations

import hashlib
import html
import json
import tempfile
from pathlib import Path
from typing import Any

from .first_edition import validate_first_edition_chapter_map
from .selection import build_selected_offline_edition


def _canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _key(record_id: Any, version: Any) -> tuple[str, str]:
    if not isinstance(record_id, str) or not record_id.strip():
        raise ValueError("Record reference requires a non-empty record_id")
    if not isinstance(version, (str, int)) or not str(version).strip():
        raise ValueError("Record reference requires a non-empty version")
    return record_id, str(version)


def _text(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return "" if value is None else str(value)


def _safe_external_link(value: Any) -> str:
    if not isinstance(value, str) or not value.startswith(("https://", "http://")):
        return ""
    escaped = html.escape(value, quote=True)
    return f'<a href="{escaped}" rel="noreferrer noopener">{html.escape(value)}</a>'


def _require_approved_chapter_map(chapter_map: dict[str, Any]) -> None:
    if chapter_map.get("status") != "approved":
        raise ValueError("Production reader requires chapter-map status 'approved'")
    approval = chapter_map.get("approval")
    if (
        not isinstance(approval, dict)
        or approval.get("status") != "APPROVED"
        or not isinstance(approval.get("approver"), str)
        or not approval["approver"].strip()
        or not isinstance(approval.get("reference"), str)
        or not approval["reference"].strip()
    ):
        raise ValueError("Production reader requires an explicit chapter-map approval attestation")


def build_first_edition_reader(
    all_records: list[dict[str, Any]],
    selection: dict[str, Any],
    chapter_map: dict[str, Any],
    output_dir: Path,
    *,
    source_commit: str,
    edition_id: str = "encyclopedia-first-edition",
) -> dict[str, Any]:
    """Build a chapter-organized static reader from an approved exact selection.

    Selection approval and dependency closure are delegated to the schema-1.1
    selection builder. Chapter assignment is separate metadata and cannot add
    records. Only selected Claims become articles; selected non-Claim records
    may appear solely as evidence notes for their selected Claim.
    """
    if not isinstance(chapter_map, dict):
        raise ValueError("Chapter map must be an object")
    _require_approved_chapter_map(chapter_map)

    available: dict[tuple[str, str], dict[str, Any]] = {}
    for record in all_records:
        key = _key(record.get("record_id"), record.get("record_version"))
        if key in available:
            raise ValueError(f"Duplicate canonical record identity: {key}")
        available[key] = record

    # Run the authoritative selection validator before rendering anything.
    # Its temporary output is discarded; no full-corpus fallback is possible.
    with tempfile.TemporaryDirectory(prefix="first-edition-selection-check-") as temporary:
        build_selected_offline_edition(
            all_records,
            selection,
            Path(temporary) / "selected",
            source_commit=source_commit,
            edition_id=edition_id,
        )

    selected_records: list[dict[str, Any]] = []
    selected_keys: set[tuple[str, str]] = set()
    for entry in selection["records"]:
        key = _key(entry.get("record_id"), entry.get("record_version"))
        selected_keys.add(key)
        selected_records.append(available[key])

    assignments = validate_first_edition_chapter_map(selected_records, chapter_map)
    selected_by_key = {_key(r["record_id"], r["record_version"]): r for r in selected_records}
    claims_by_chapter: dict[str, list[dict[str, Any]]] = {
        chapter["chapter_id"]: [] for chapter in chapter_map["chapters"]
    }
    for key, chapter_id in assignments.items():
        claims_by_chapter[chapter_id].append(selected_by_key[key])

    evidence_by_claim: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in selected_records:
        if record.get("record_type") != "evidence_use":
            continue
        content = record.get("content", {})
        claim_ref = content.get("claim_ref") if isinstance(content, dict) else None
        claim_key = _key(
            claim_ref.get("record_id"), claim_ref.get("version", claim_ref.get("record_version"))
        ) if isinstance(claim_ref, dict) else None
        if claim_key is not None:
            evidence_by_claim.setdefault(claim_key, []).append(record)

    def evidence_html(claim: dict[str, Any]) -> str:
        claim_key = _key(claim["record_id"], claim["record_version"])
        blocks: list[str] = []
        for evidence in sorted(evidence_by_claim.get(claim_key, []), key=lambda r: r["record_id"]):
            content = evidence.get("content", {})
            source_ref = content.get("source_ref", {}) if isinstance(content, dict) else {}
            source_key = _key(
                source_ref.get("record_id"), source_ref.get("version", source_ref.get("record_version"))
            )
            source = selected_by_key[source_key]
            source_content = source.get("content", {})
            identity = source_content.get("source_identity", {}) if isinstance(source_content, dict) else {}
            external_ref = source_content.get("external_ref", {}) if isinstance(source_content, dict) else {}
            uri = external_ref.get("uri") if isinstance(external_ref, dict) else None
            material = content.get("material", {}) if isinstance(content, dict) else {}
            description = material.get("description") if isinstance(material, dict) else material
            locator = material.get("locator") if isinstance(material, dict) else None
            blocks.append(
                '<li><b>Evidence:</b> ' + html.escape(evidence["record_id"]) +
                ' · ' + html.escape(_text(content.get("evidence_role"))) +
                '<p>' + html.escape(_text(description)) + '</p>' +
                ('<p><b>Locator:</b> ' + html.escape(_text(locator)) + '</p>' if locator else '') +
                '<p><b>Source:</b> ' + html.escape(_text(identity)) + '</p>' +
                ('<p>' + _safe_external_link(uri) + '</p>' if uri else '') +
                '</li>'
            )
        return '<details><summary>Evidence and sources</summary><ul>' + ''.join(blocks) + '</ul></details>'

    chapter_sections: list[str] = []
    for chapter in chapter_map["chapters"]:
        chapter_id = html.escape(chapter["chapter_id"], quote=True)
        title = html.escape(_text(chapter.get("title") or chapter["chapter_id"]))
        articles: list[str] = []
        for claim in sorted(claims_by_chapter[chapter["chapter_id"]], key=lambda r: r["record_id"]):
            content = claim.get("content", {})
            statement = content.get("statement") if isinstance(content, dict) else None
            if not isinstance(statement, str) or not statement.strip():
                raise ValueError(f"Selected Claim has no reader statement: {claim['record_id']}")
            article_id = html.escape(claim["record_id"] + "-" + str(claim["record_version"]), quote=True)
            articles.append(
                f'<article id="{article_id}"><h3>{html.escape(claim["record_id"])}</h3>'
                f'<p class="statement">{html.escape(statement)}</p>{evidence_html(claim)}</article>'
            )
        chapter_sections.append(
            f'<section id="{chapter_id}"><h2>{title}</h2>' +
            (''.join(articles) if articles else '<p class="empty">No approved articles in this chapter.</p>') +
            '</section>'
        )

    page = (
        '<!doctype html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow">'
        '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; img-src \'none\'; connect-src \'none\'; base-uri \'none\'; form-action \'none\'; object-src \'none\'">'
        f'<title>{html.escape(edition_id)}</title>'
        '<style>body{font:1rem/1.6 system-ui,sans-serif;max-width:1000px;margin:2rem auto;padding:0 1rem;overflow-wrap:anywhere}'
        'nav{display:flex;flex-wrap:wrap;gap:.6rem}section{margin:2.5rem 0}article{border:1px solid #bbb;border-radius:.5rem;padding:1rem;margin:1rem 0}'
        '.statement{font-size:1.12rem}details{margin-top:1rem}.empty{color:#666}a{overflow-wrap:anywhere}</style>'
        '</head><body><header><h1>Энциклопедия цивилизации</h1>'
        '<p>Первая редакция · версия для чтения, собранная только из явно утверждённого набора записей.</p>'
        f'<p>Исходный коммит: <code>{html.escape(source_commit)}</code></p></header><nav>'
        + ''.join(f'<a href="#{html.escape(ch["chapter_id"], quote=True)}">{html.escape(_text(ch.get("title") or ch["chapter_id"]))}</a>' for ch in chapter_map["chapters"])
        + '</nav>' + ''.join(chapter_sections) + '</body></html>'
    )

    if output_dir.is_symlink():
        raise ValueError(f"Reader output path must not be a symbolic link: {output_dir}")
    if output_dir.exists():
        if not output_dir.is_dir():
            raise ValueError(f"Reader output path is not a directory: {output_dir}")
        if any(output_dir.iterdir()):
            raise ValueError(f"Reader output directory must be empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "index.html"
    index_path.write_text(page, encoding="utf-8")
    result = {
        "edition_id": edition_id,
        "edition_state": "approved_selection_reader",
        "source_commit": source_commit,
        "selection_schema_version": selection["schema_version"],
        "selection_manifest_sha256": hashlib.sha256(_canonical(selection)).hexdigest(),
        "chapter_map_sha256": hashlib.sha256(_canonical(chapter_map)).hexdigest(),
        "selected_record_count": len(selected_records),
        "article_count": len(assignments),
        "chapter_count": len(chapter_map["chapters"]),
        "article_identities": [
            {"record_id": rid, "record_version": version, "chapter_id": chapter_id}
            for (rid, version), chapter_id in sorted(assignments.items())
        ],
        "index_sha256": hashlib.sha256(index_path.read_bytes()).hexdigest(),
        "network_required": False,
    }
    (output_dir / "reader-manifest.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result
