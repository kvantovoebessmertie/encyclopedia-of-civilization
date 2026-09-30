from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import zipfile
from typing import Any


SECRET_PATTERNS = (
    re.compile(r"(?i)[\"\']?(api[_-]?key|secret|password|token)[\"\']?\s*[:=]\s*[\"\']?[^\s\"\']{8,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)gh[pousr]_[A-Za-z0-9_]{20,}"),
)


@dataclass(frozen=True)
class OperationalFinding:
    code: str
    severity: str
    message: str
    subject: str | None = None


def digest_bytes(data: bytes) -> str:
    return "sha256:" + sha256(data).hexdigest()


def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def manifest_for_files(root: Path) -> dict[str, Any]:
    root = root.resolve()
    files = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        files[rel] = digest_file(path)
    return {"algorithm": "sha256", "files": files}


def verify_manifest(root: Path, manifest: dict[str, Any]) -> list[OperationalFinding]:
    findings = []
    expected = manifest.get("files", {})
    if not isinstance(expected, dict):
        return [OperationalFinding("OPS-MANIFEST-INVALID", "error", "manifest.files должен быть объект")]
    for rel, expected_digest in expected.items():
        path = (root / rel).resolve()
        if root.resolve() not in path.parents:
            findings.append(OperationalFinding("OPS-PATH-TRAVERSAL", "error", "manifest path выходит за root", rel))
            continue
        if not path.is_file():
            findings.append(OperationalFinding("OPS-FILE-MISSING", "error", "файл из manifest отсутствует", rel))
            continue
        actual = digest_file(path)
        if actual != expected_digest:
            findings.append(OperationalFinding("OPS-INTEGRITY-MISMATCH", "error", "digest не совпадает", rel))
    return findings


def scan_secrets(root: Path) -> list[OperationalFinding]:
    findings = []
    root = root.resolve()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(OperationalFinding("OPS-SECRET-EXPOSURE", "error", "в artifact обнаружен потенциальный secret", path.relative_to(root).as_posix()))
                break
    return findings


def validate_archive(path: Path, destination: Path | None = None) -> list[OperationalFinding]:
    findings = []
    root = (destination or Path("/tmp/encyclopedia-archive-check")).resolve()
    try:
        with zipfile.ZipFile(path) as archive:
            if archive.testzip() is not None:
                findings.append(OperationalFinding("OPS-ARCHIVE-CORRUPT", "error", "zip integrity check failed"))
            for info in archive.infolist():
                target = (root / info.filename).resolve()
                if root not in target.parents and target != root:
                    findings.append(OperationalFinding("OPS-PATH-TRAVERSAL", "error", "archive entry выходит за extraction root", info.filename))
                if info.filename.startswith("/") or info.filename.startswith("\\"):
                    findings.append(OperationalFinding("OPS-ABSOLUTE-PATH", "error", "absolute archive path запрещён", info.filename))
    except (OSError, zipfile.BadZipFile) as exc:
        findings.append(OperationalFinding("OPS-ARCHIVE-INVALID", "error", str(exc)))
    return findings


def authorize(actor_roles: set[str], required_role: str) -> bool:
    return required_role in actor_roles or "administrator" in actor_roles


def validate_dependency_lock(lock: dict[str, Any]) -> list[OperationalFinding]:
    findings = []
    deps = lock.get("dependencies")
    if not isinstance(deps, list):
        return [OperationalFinding("OPS-DEPENDENCY-LOCK-MISSING", "error", "dependencies lock отсутствует")]
    for dep in deps:
        if not isinstance(dep, dict) or not dep.get("name") or not dep.get("version") or not dep.get("digest"):
            findings.append(OperationalFinding("OPS-DEPENDENCY-UNPINNED", "error", "dependency должна иметь name/version/digest"))
    return findings


def validate_change_record(change: dict[str, Any]) -> list[OperationalFinding]:
    required = ("change_id", "reason", "components", "actor", "from_version", "to_version", "test_result", "rollback_plan")
    return [
        OperationalFinding("OPS-CHANGE-INCOMPLETE", "error", f"отсутствует обязательное поле {key}")
        for key in required if key not in change
    ]


def validate_rollback(current: dict[str, Any], target: dict[str, Any]) -> list[OperationalFinding]:
    findings = []
    if current.get("record_id") != target.get("record_id"):
        findings.append(OperationalFinding("OPS-ROLLBACK-IDENTITY", "error", "rollback меняет record identity"))
    if current.get("record_version") == target.get("record_version"):
        findings.append(OperationalFinding("OPS-ROLLBACK-NOOP", "error", "rollback target совпадает с current version"))
    if target.get("history_deleted") is True:
        findings.append(OperationalFinding("OPS-ROLLBACK-HISTORY-LOSS", "error", "rollback не должен удалять history"))
    return findings


def operational_registry() -> dict[str, str]:
    return {
        "OPS-BACKUP-IDENTITY": "O01",
        "OPS-BACKUP-RESTORE": "O02",
        "OPS-PACKAGE-INTEGRITY": "O03",
        "OPS-INTEGRITY-CORRUPTION": "O04",
        "OPS-AUTHORIZATION": "O05",
        "OPS-LEAST-PRIVILEGE": "O06",
        "OPS-SECRET-EXPOSURE": "O07",
        "OPS-DEPENDENCY-UNPINNED": "O08",
        "OPS-CHANGE-INCOMPLETE": "O09",
        "OPS-ROLLBACK-HISTORY-LOSS": "O10",
        "OPS-UPDATE-MIGRATION": "O11",
        "OPS-INCIDENT-NONINFERENCE": "O12",
        "OPS-ARCHIVE-INVALID": "O13",
        "OPS-RECOVERY-CLEAN-ENV": "O14",
        "OPS-RECOVERY-DIGEST": "O15",
        "OPS-BACKEND-FAILURE": "O16",
        "OPS-INDEX-LOSS": "O17",
        "OPS-PACKAGE-CORRUPTION": "O18",
        "OPS-BACKUP-CORRUPTION": "O19",
        "OPS-STORAGE-NODE-LOSS": "O20",
        "OPS-DEPENDENCY-COMPROMISE": "O21",
        "OPS-MALICIOUS-PACKAGE": "O22",
        "OPS-PATH-TRAVERSAL": "O23",
        "OPS-MASS-IMPORT": "O24",
        "OPS-MASS-EXPORT": "O25",
        "OPS-OFFLINE-DURATION": "O26",
        "OPS-LARGE-RECOVERY": "O27",
        "OPS-REPEATED-RECOVERY": "O28",
        "OPS-PARTIAL-UPDATE": "O29",
        "OPS-ROLLBACK-RECOVERY": "O30",
    }
