from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"web-systems-basics"/"records"
def test_web_systems_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==11
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    assert len(sources)==2
    for claim in [r for r in records if r["record_type"]=="claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources


def test_web_systems_evidence_uses_have_claim_specific_pinpoints():
    records = {
        record["record_id"]: record
        for record in (
            json.loads(path.read_text(encoding="utf-8"))
            for path in SLICE.glob("*.json")
        )
    }
    expected = {
        "EU-WEB_SYSTEMS_BASICS-A": (
            "CLM-WEB_SYSTEMS_BASICS-A",
            ("Clients and servers", "The other parts of the toolbox"),
            "высокоуровневую",
        ),
        "EU-WEB_SYSTEMS_BASICS-B": (
            "CLM-WEB_SYSTEMS_BASICS-B",
            ("HTTP basics", "прикладного уровня"),
            "HTML",
        ),
        "EU-WEB_SYSTEMS_BASICS-C": (
            "CLM-WEB_SYSTEMS_BASICS-C",
            ("DNS explained", "IP-адресом"),
            "не гарантирует",
        ),
    }
    for evidence_id, (claim_id, markers, boundary) in expected.items():
        evidence = records[evidence_id]
        assert evidence["record_version"] == "2"
        assert evidence["content"]["claim_ref"] == {
            "record_id": claim_id,
            "version": "1",
        }
        assert evidence["content"]["source_ref"] == {
            "record_id": "SRC-WEB_SYSTEMS_BASICS",
            "version": "1",
        }
        description = evidence["content"]["material"]["description"]
        for marker in markers:
            assert marker.casefold() in description.casefold()
        assert boundary.casefold() in description.casefold()


def test_web_systems_claim_a_has_separate_browser_rendering_evidence():
    records = {
        record["record_id"]: record
        for record in (
            json.loads(path.read_text(encoding="utf-8"))
            for path in SLICE.glob("*.json")
        )
    }
    source = records["SRC-MDN-HOW-BROWSERS-LOAD-WEBSITES"]
    evidence = records["EU-WEB_SYSTEMS_BASICS-A-RENDERING"]
    assert source["record_type"] == "source"
    assert source["content"]["source_identity"] == "MDN — How browsers load websites"
    assert source["content"]["external_ref"]["uri"] == (
        "https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/"
        "Web_standards/How_browsers_load_websites"
    )
    assert evidence["record_type"] == "evidence_use"
    assert evidence["record_version"] == "1"
    assert evidence["content"]["claim_ref"] == {
        "record_id": "CLM-WEB_SYSTEMS_BASICS-A",
        "version": "1",
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": "SRC-MDN-HOW-BROWSERS-LOAD-WEBSITES",
        "version": "1",
    }
    description = evidence["content"]["material"]["description"]
    for marker in ("Web page rendering", "Handling HTML", "Parsing CSS and rendering the page"):
        assert marker.casefold() in description.casefold()
    assert "упрощённое описание" in description.casefold()
    assert "могут обрабатывать этапы по-разному" in description.casefold()
