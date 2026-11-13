from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "si-units-basics" / "records"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]


def test_si_units_basics_slice_is_complete():
    records = _records()
    assert len(records) == 10
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {
        r["record_type"] for r in records
    }
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(sources) == 2 and len(claims) == 3 and len(evidence) == 3
    assert all(r["provenance"]["created_from"][0]["record_id"] in sources for r in claims)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence} == {
        r["record_id"] for r in claims
    }
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)


def test_si_units_nist_pinpoints_are_versioned_and_claim_specific():
    records = {r["record_id"]: r for r in _records()}
    seven = records["EU-SI-SEVEN-BASE"]
    derived = records["EU-SI-DERIVED"]
    accuracy = records["EU-SI-ACCURACY-BOUNDARY"]

    assert seven["record_version"] == "2"
    assert derived["record_version"] == "2"
    assert accuracy["record_version"] == "1"  # explicitly outside the bounded authorization

    for evidence in (seven, derived):
        assert evidence["content"]["evidence_role"] == "supports"
        assert evidence["content"]["claim_ref"]["version"] == "1"
        assert evidence["content"]["source_ref"] == {
            "record_id": "SRC-NIST-SI-UNITS",
            "version": "1",
        }
        assert evidence["provenance"]["created_from"] == [
            {"record_id": "SRC-NIST-SI-UNITS", "version": "1"}
        ]
        assert "NIST" in evidence["content"]["material"]["description"]
        assert "https://www.nist.gov/pml/owm/metric-si/si-units" in evidence["content"]["material"]["description"]

    seven_text = seven["content"]["material"]["description"]
    assert "Defining Constants" in seven_text
    assert "Base and Derived Units" in seven_text
    assert "Do not equate the seven base units with the seven defining constants." in seven_text

    derived_text = derived["content"]["material"]["description"]
    assert "Base and Derived Units" in derived_text
    assert "22 is not the total number of all possible SI derived units." in derived_text
