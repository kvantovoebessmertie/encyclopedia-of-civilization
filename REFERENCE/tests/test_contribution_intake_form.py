from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FORM = ROOT / "CONTRIBUTIONS" / "intake-form-prototype.html"
SCRIPT = ROOT / "CONTRIBUTIONS" / "intake-form.js"
SCHEMA = ROOT / "CONTRIBUTIONS" / "contribution-submission-v1.schema.json"


def test_local_intake_form_covers_required_schema_fields():
    page = FORM.read_text(encoding="utf-8")
    script = SCRIPT.read_text(encoding="utf-8")
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    assert schema["properties"]["schema_version"]["const"] == "1.0"
    for field in schema["required"]:
        if field in {"schema_version", "sources", "proposed_relations", "risk_flags"}:
            assert field in script
        elif field == "rights_and_terms_acknowledged":
            assert 'id="rights_ack"' in page
            assert "rights_and_terms_acknowledged" in script
        elif field == "related_record_ids":
            assert 'id="related_record_ids"' in page
            assert "related_record_ids" in script
        elif field == "contributor_role":
            assert 'id="contributor_role"' in page
            assert "contributor_role" in script
        else:
            assert f'id="{field}"' in page
            assert field in script

    assert schema["properties"]["rights_and_terms_acknowledged"]["const"] is True


def test_local_intake_form_is_offline_and_has_no_contact_or_network_submission():
    page = FORM.read_text(encoding="utf-8")
    script = SCRIPT.read_text(encoding="utf-8")

    assert "default-src 'none'" in page
    assert "connect-src 'none'" in page
    assert 'script src="intake-form.js" defer' in page
    assert "<script>" not in page
    assert "fetch(" not in script
    assert "XMLHttpRequest" not in script
    assert "sendBeacon" not in script
    assert "type=\"email\"" not in page
    assert "contact_email" not in script
    assert "createObjectURL" in script
    assert "window.setTimeout(() => URL.revokeObjectURL(url), 1000)" in script
    assert "JSON.stringify(payload" in script


def test_form_submission_type_choices_match_schema():
    page = FORM.read_text(encoding="utf-8")
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    for item in schema["properties"]["submission_type"]["enum"]:
        assert f'value="{item}"' in page
    for item in schema["properties"]["contributor_role"]["enum"]:
        assert f'value="{item}"' in page
    for item in schema["properties"]["risk_flags"]["items"]["enum"]:
        assert f'value="{item}"' in page


def test_source_submission_requires_related_record_id_in_browser_form():
    script = SCRIPT.read_text(encoding="utf-8")

    # Mirror the schema's conditional minimum for source proposals so the
    # downloaded payload is not knowingly invalid before offline validation.
    assert 'if (submissionType === "source" && relatedIds.length < 1)' in script
    assert "Для предложения источника укажите минимум один ID связанной записи." in script


def test_local_form_enforces_schema_item_limits():
    script = SCRIPT.read_text(encoding="utf-8")

    assert "relatedIds.some(id => id.length > 300)" in script
    assert "(source.creators || []).length > 50" in script
    assert "(source.creators || []).some(creator => creator.length > 300)" in script
