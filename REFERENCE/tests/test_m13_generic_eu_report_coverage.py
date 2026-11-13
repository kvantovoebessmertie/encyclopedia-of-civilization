from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "m13_generic_eu_report_coverage.py"
SPEC = importlib.util.spec_from_file_location("m13_generic_eu_report_coverage", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def test_coverage_maps_generic_eus_and_marks_report_mentions_as_unverified(tmp_path: Path):
    findings = tmp_path / "findings.csv"
    worksheet = tmp_path / "worksheet.csv"
    release = tmp_path / "RELEASE"
    release.mkdir()

    write_csv(
        findings,
        ["path", "record_id", "record_type", "finding", "severity", "detail"],
        [
            {
                "path": "slice/records/EU-FOO-A.json",
                "record_id": "EU-FOO-A",
                "record_type": "evidence_use",
                "finding": "generic_material_description",
                "severity": "medium",
                "detail": "generic",
            },
            {
                "path": "slice/records/EU-BAR-A.json",
                "record_id": "EU-BAR-A",
                "record_type": "evidence_use",
                "finding": "generic_material_description",
                "severity": "medium",
                "detail": "generic",
            },
            {
                "path": "slice/records/SRC-FOO.json",
                "record_id": "SRC-FOO",
                "record_type": "source",
                "finding": "source_identity_sentence_candidate",
                "severity": "medium",
                "detail": "not an EU",
            },
        ],
    )
    write_csv(
        worksheet,
        ["record_id", "evidence_use_ids", "source_ids", "slice"],
        [
            {
                "record_id": "CLM-FOO-A",
                "evidence_use_ids": "EU-FOO-A",
                "source_ids": "SRC-FOO",
                "slice": "foo",
            },
            {
                "record_id": "CLM-BAR-A",
                "evidence_use_ids": "EU-BAR-A",
                "source_ids": "SRC-BAR",
                "slice": "bar",
            },
        ],
    )
    (release / "M13-FOO-SOURCE-PASSAGE-REVIEW.md").write_text(
        "Reviewed CLM-FOO-A at a source passage.\n", encoding="utf-8"
    )
    (release / "M13-HANDOFF.md").write_text(
        "CLM-BAR-A appears only in a handoff.\n", encoding="utf-8"
    )

    result = MODULE.build_coverage(findings, worksheet, release)

    assert result["generic_evidence_use_candidates"] == 2
    assert result["mapped_candidates"] == 2
    assert result["candidates_with_any_m13_report_mention"] == 2
    assert result["candidates_with_source_review_filename_mention"] == 1
    assert result["candidates_without_any_report_mention"] == 0

    foo = next(item for item in result["candidates"] if item["claim_id"] == "CLM-FOO-A")
    bar = next(item for item in result["candidates"] if item["claim_id"] == "CLM-BAR-A")
    assert foo["source_review_report_mentions"] == ["M13-FOO-SOURCE-PASSAGE-REVIEW.md"]
    assert bar["source_review_report_mentions"] == []
    assert foo["human_confirmation_required"] is True
    assert bar["human_confirmation_required"] is True


def test_exact_claim_id_matching_does_not_match_longer_identifiers(tmp_path: Path):
    findings = tmp_path / "findings.csv"
    worksheet = tmp_path / "worksheet.csv"
    release = tmp_path / "RELEASE"
    release.mkdir()

    write_csv(
        findings,
        ["path", "record_id", "record_type", "finding", "severity", "detail"],
        [{
            "path": "slice/EU-FOO.json",
            "record_id": "EU-FOO",
            "record_type": "evidence_use",
            "finding": "generic_material_description",
            "severity": "medium",
            "detail": "generic",
        }],
    )
    write_csv(
        worksheet,
        ["record_id", "evidence_use_ids", "source_ids", "slice"],
        [{
            "record_id": "CLM-FOO-A",
            "evidence_use_ids": "EU-FOO",
            "source_ids": "SRC-FOO",
            "slice": "foo",
        }],
    )
    (release / "M13-OTHER-REVIEW.md").write_text(
        "CLM-FOO-AB was reviewed, not CLM-FOO-A.\n", encoding="utf-8"
    )

    result = MODULE.build_coverage(findings, worksheet, release)

    assert result["candidates_with_any_m13_report_mention"] == 0
    assert result["candidates_without_any_report_mention"] == 1


def test_unmapped_generic_eu_is_reported_not_silently_dropped(tmp_path: Path):
    findings = tmp_path / "findings.csv"
    worksheet = tmp_path / "worksheet.csv"
    release = tmp_path / "RELEASE"
    release.mkdir()

    write_csv(
        findings,
        ["path", "record_id", "record_type", "finding", "severity", "detail"],
        [{
            "path": "slice/EU-ORPHAN.json",
            "record_id": "EU-ORPHAN",
            "record_type": "evidence_use",
            "finding": "generic_material_description",
            "severity": "medium",
            "detail": "generic",
        }],
    )
    write_csv(worksheet, ["record_id", "evidence_use_ids", "source_ids", "slice"], [])

    result = MODULE.build_coverage(findings, worksheet, release)

    assert result["generic_evidence_use_candidates"] == 1
    assert result["mapped_candidates"] == 0
    assert result["unmapped_evidence_use_ids"] == ["EU-ORPHAN"]


def test_corpus_mode_discovers_generic_eus_without_external_artifacts(tmp_path: Path):
    content = tmp_path / "CONTENT"
    slice_records = content / "vertical-slices" / "education-science-basics" / "records"
    slice_records.mkdir(parents=True)
    release = tmp_path / "RELEASE"
    release.mkdir()

    generic_description = (
        "IES — Common Guidelines используется для представления утверждения "
        "без вывода за пределы указанного материала."
    )
    (slice_records / "EU-EDUCATION_SCIENCE_BASICS-A.json").write_text(
        json.dumps(
            {
                "record_id": "EU-EDUCATION_SCIENCE_BASICS-A",
                "record_type": "evidence_use",
                "content": {
                    "claim_ref": {"record_id": "CLM-EDUCATION_SCIENCE_BASICS-A"},
                    "source_ref": {"record_id": "SRC-IES-COMMON-GUIDELINES-2013"},
                    "material": {"description": generic_description},
                },
            }
        ),
        encoding="utf-8",
    )
    (slice_records / "EU-EDUCATION_SCIENCE_BASICS-B.json").write_text(
        __import__("json").dumps(
            {
                "record_id": "EU-EDUCATION_SCIENCE_BASICS-B",
                "record_type": "evidence_use",
                "content": {
                    "claim_ref": {"record_id": "CLM-EDUCATION_SCIENCE_BASICS-B"},
                    "source_ref": {"record_id": "SRC-IES-COMMON-GUIDELINES-2013"},
                    "material": {"description": "Specific passage, page 12."},
                },
            }
        ),
        encoding="utf-8",
    )
    (release / "M13-EDUCATION-SCIENCE-SOURCE-PASSAGE-REVIEW.md").write_text(
        "CLM-EDUCATION_SCIENCE_BASICS-A\n", encoding="utf-8"
    )

    result = MODULE.build_coverage_from_corpus(content, release)

    assert result["generic_evidence_use_candidates"] == 1
    assert result["mapped_candidates"] == 1
    candidate = result["candidates"][0]
    assert candidate["claim_id"] == "CLM-EDUCATION_SCIENCE_BASICS-A"
    assert candidate["evidence_use_id"] == "EU-EDUCATION_SCIENCE_BASICS-A"
    assert candidate["source_ids"] == ["SRC-IES-COMMON-GUIDELINES-2013"]
    assert candidate["slice"] == "education-science-basics"
    assert candidate["source_review_report_mentions"] == [
        "M13-EDUCATION-SCIENCE-SOURCE-PASSAGE-REVIEW.md"
    ]
