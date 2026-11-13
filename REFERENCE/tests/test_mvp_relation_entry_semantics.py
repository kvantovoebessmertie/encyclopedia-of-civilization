from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "CONTRIBUTIONS" / "intake-form.js"


def test_default_relation_direction_is_not_treated_as_user_provided_content():
    script = SCRIPT.read_text(encoding="utf-8")

    assert 'field.dataset.field !== "direction" && field.value.trim() !== ""' in script
    assert 'key !== "direction" && raw !== ""' in script


def test_relation_fields_are_required_only_for_relation_submissions_or_started_entries():
    script = SCRIPT.read_text(encoding="utf-8")

    assert 'const requiresRelation = value("submission_type") === "relation";' in script
    assert "field.required = requiresRelation || hasRelationContent;" in script
