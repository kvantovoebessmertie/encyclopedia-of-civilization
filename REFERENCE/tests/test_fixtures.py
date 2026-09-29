from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "REFERENCE" / "fixtures"
SCHEMA = ROOT.parent / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def test_fixture_manifest_is_complete():
    manifest = json.loads((FIXTURES / "manifest.json").read_text(encoding="utf-8"))
    for item in manifest["fixtures"]:
        assert (FIXTURES / item["file"]).exists()


def test_fixtures_match_expected_status():
    manifest = json.loads((FIXTURES / "manifest.json").read_text(encoding="utf-8"))
    validator = Validator(SCHEMA)
    for item in manifest["fixtures"]:
        record = json.loads((FIXTURES / item["file"]).read_text(encoding="utf-8"))
        result = validator.validate(record)
        assert result.status == item["expected_status"], item["fixture_id"]
