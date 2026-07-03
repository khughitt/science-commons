"""Operator-run build of the HGNC gene crosswalk's crosswalk.csv.

Run from the dataset directory:

    uv run --with-editable ~/d/science/science --with httpx --with pyyaml python recipe/build.py

Network fetches the pinned dated HGNC release files; output is a few-MB CSV.
"""

from __future__ import annotations

import csv
import hashlib
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.gene_crosswalk import _parse_crosswalk_rows
from science_tool.commons.gene_crosswalk_build import build_rows, fetch_text

_HERE = Path(__file__).resolve().parent
_OUT = _HERE.parent
_CROSSWALK = _OUT / "crosswalk.csv"
_FIELDS = [
    "gene_key",
    "symbol",
    "entrez_id",
    "ensembl_gene_id",
    "alias_symbol",
    "prev_symbol",
    "status",
    "replacement_gene_keys",
]


def _require_text(src: dict[str, Any], key: str) -> str:
    value = src.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"sources.yaml: {key} must be a nonblank string")
    value = value.strip()
    if value.startswith("__OPERATOR_PINNED_"):
        raise ValueError(f"sources.yaml: {key} still contains an operator placeholder")
    return value


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def _sha256_resource(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return f"sha256:{hashlib.sha256(data).hexdigest()}", len(data)


def _crosswalk_resource(datapackage: dict[str, Any]) -> dict[str, Any]:
    resources = datapackage.get("resources")
    if not isinstance(resources, list):
        raise ValueError("datapackage.yaml: resources must be a list")
    for resource in resources:
        if not isinstance(resource, dict):
            raise ValueError("datapackage.yaml: each resource must be a mapping")
        if resource.get("path") == "crosswalk.csv":
            return resource
    raise ValueError("datapackage.yaml: missing crosswalk.csv resource")


def _existing_resource_hash(datapackage_path: Path) -> str:
    datapackage = yaml.safe_load(datapackage_path.read_text(encoding="utf-8"))
    if not isinstance(datapackage, dict):
        raise ValueError("datapackage.yaml: expected a mapping")
    resource = _crosswalk_resource(datapackage)
    digest = resource.get("hash")
    if not isinstance(digest, str) or not digest.strip():
        raise ValueError("datapackage.yaml: crosswalk.csv resource missing hash")
    return digest.strip()


def _existing_version(datapackage_path: Path) -> str:
    datapackage = yaml.safe_load(datapackage_path.read_text(encoding="utf-8"))
    if not isinstance(datapackage, dict):
        raise ValueError("datapackage.yaml: expected a mapping")
    version = datapackage.get("version")
    if not isinstance(version, str) or not version.strip():
        raise ValueError("datapackage.yaml: missing version")
    return version.strip()


def _update_datapackage(path: Path, *, version: str) -> None:
    datapackage = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(datapackage, dict):
        raise ValueError("datapackage.yaml: expected a mapping")
    resource = _crosswalk_resource(datapackage)
    digest, size = _sha256_resource(_CROSSWALK)
    resource["hash"] = digest
    resource["bytes"] = size

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    in_crosswalk_resource = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        newline = "\n" if line.endswith("\n") else ""
        if line.startswith("version:"):
            lines[index] = f'version: "{version}"{newline}'
        elif stripped == "- name: crosswalk":
            in_crosswalk_resource = True
        elif in_crosswalk_resource and stripped.startswith("- name:"):
            in_crosswalk_resource = False
        elif in_crosswalk_resource and stripped.startswith("hash:"):
            indent = line[: len(line) - len(line.lstrip())]
            lines[index] = f'{indent}hash: "{digest}"{newline}'
        elif in_crosswalk_resource and stripped.startswith("bytes:"):
            indent = line[: len(line) - len(line.lstrip())]
            lines[index] = f"{indent}bytes: {size}{newline}"
    path.write_text("".join(lines), encoding="utf-8")


def _replace_frontmatter_value(text: str, key: str, value: Any) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("entity.md: missing YAML frontmatter")
    value_text = f'"{value}"' if isinstance(value, str) else str(value)
    replacement = f"{key}: {value_text}"
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            break
        if line.startswith(f"{key}:"):
            newline = "\n" if line.endswith("\n") else ""
            lines[i] = f"{replacement}{newline}"
            return "".join(lines)
    raise ValueError(f"entity.md: missing frontmatter key {key!r}")


def _update_entity(path: Path, *, gene_count: int, version: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = _replace_frontmatter_value(text, "version", version)
    text = _replace_frontmatter_value(text, "updated", datetime.now(UTC).date().isoformat())
    text = _replace_frontmatter_value(text, "gene_count", gene_count)
    path.write_text(text, encoding="utf-8")


def _load_sources(path: Path) -> dict[str, str]:
    src = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(src, dict):
        raise ValueError("sources.yaml: expected a mapping")
    out = {
        "artifact_version": _require_text(src, "artifact_version"),
        "release_date": _require_text(src, "release_date"),
        "complete_set_url": _require_text(src, "complete_set_url"),
        "withdrawn_url": _require_text(src, "withdrawn_url"),
    }
    release_date = out["release_date"]
    if release_date not in out["complete_set_url"]:
        raise ValueError("sources.yaml: release_date must appear in complete_set_url")
    if release_date not in out["withdrawn_url"]:
        raise ValueError("sources.yaml: release_date must appear in withdrawn_url")
    return out


def main() -> None:
    src = _load_sources(_HERE / "sources.yaml")
    complete = fetch_text(src["complete_set_url"])
    withdrawn = fetch_text(src["withdrawn_url"])
    rows = build_rows(complete_set_text=complete, withdrawn_text=withdrawn)
    datapackage_path = _OUT / "datapackage.yaml"
    old_hash = _existing_resource_hash(datapackage_path)
    old_version = _existing_version(datapackage_path)
    _write_csv(_CROSSWALK, rows)
    new_hash, _ = _sha256_resource(_CROSSWALK)
    if new_hash == old_hash and old_version == src["artifact_version"]:
        print(f"reproduced identical crosswalk.csv ({len(rows)} rows); version/updated unchanged")
        return
    _update_datapackage(datapackage_path, version=src["artifact_version"])
    _update_entity(_OUT / "entity.md", gene_count=len(rows), version=src["artifact_version"])
    print(f"wrote {len(rows)} rows to {_CROSSWALK} (version {src['artifact_version']})")


def _self_check() -> None:
    _load_sources(_HERE / "sources.yaml")
    _parse_crosswalk_rows(
        [
            {
                "gene_key": "9606|hgnc|HGNC:5",
                "symbol": "A1BG",
                "entrez_id": "1",
                "ensembl_gene_id": "ENSG00000121410",
                "alias_symbol": "",
                "prev_symbol": "",
                "status": "approved",
                "replacement_gene_keys": "",
            }
        ]
    )


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-check"]:
        _self_check()
    else:
        main()
