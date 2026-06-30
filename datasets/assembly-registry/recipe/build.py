"""Operator-run, no-FASTA build of the assembly registry resources.

Run from the dataset directory:
  uv run --with refget --with httpx --with pyyaml python recipe/build.py
Network is used only to fetch pinned seqcol level-2 records and pinned NCBI
assembly reports; output is small CSV resources.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.assembly_registry_build import (
    build_contig_rows,
    build_registry_row,
    fetch_seqcol_level2,
    validate_registry_label_bindings,
)
from science_tool.commons.assembly_report_build import build_contig_alias_rows, fetch_text, parse_assembly_report

_HERE = Path(__file__).resolve().parent
_OUT = _HERE.parent
_DATAPACKAGE = _HERE.parent / "datapackage.yaml"
_ENTITY = _HERE.parent / "entity.md"
_ASSEMBLY_FIELDS = [
    "seqcol_digest",
    "label",
    "aliases",
    "accession",
    "n_sequences",
    "naming",
    "source_collection_url",
    "source_url",
]
_CONTIG_FIELDS = ["seqcol_digest", "sequence_index", "name", "refget_digest", "length"]
_ALIAS_FIELDS = ["seqcol_digest", "refget_digest", "alias", "alias_kind", "sequence_accession"]
_RESOURCE_PATHS = ("assemblies.csv", "contigs.csv", "contig_aliases.csv")


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _require_text(src: dict[str, Any], key: str, *, label: str) -> str:
    value = src.get(key)
    if not isinstance(value, str):
        raise ValueError(f"invalid {key} for {label!r}: expected string, got {type(value).__name__}")
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"blank {key} for {label!r}")
    if cleaned.startswith("__OPERATOR_PINNED_"):
        raise ValueError(f"{key} for {label!r} still contains operator-pinning sentinel: {cleaned}")
    return cleaned


def _aliases(src: dict[str, Any], *, label: str) -> tuple[str, ...]:
    aliases = src.get("aliases")
    if aliases is None:
        return ()
    if not isinstance(aliases, list):
        raise ValueError(f"invalid aliases for {label!r}: expected list, got {type(aliases).__name__}")

    out: list[str] = []
    seen: set[str] = set()
    for alias in aliases:
        if not isinstance(alias, str):
            raise ValueError(f"invalid alias for {label!r}: expected string, got {type(alias).__name__}")
        cleaned = alias.strip()
        if not cleaned:
            raise ValueError(f"blank alias for {label!r}")
        if cleaned.startswith("__OPERATOR_PINNED_"):
            raise ValueError(f"alias for {label!r} still contains operator-pinning sentinel: {cleaned}")
        if cleaned in seen:
            raise ValueError(f"duplicate alias for {label!r}: {cleaned!r}")
        seen.add(cleaned)
        out.append(cleaned)
    return tuple(out)


def _validate_unique_seqcol_digests(rows: list[dict[str, Any]]) -> None:
    seen: dict[str, tuple[int, str]] = {}
    for row_index, row in enumerate(rows):
        digest = row.get("seqcol_digest")
        label = row.get("label")
        label_text = label if isinstance(label, str) else f"row {row_index}"
        if not isinstance(digest, str) or not digest.strip():
            raise ValueError(f"invalid seqcol_digest for assembly {label_text!r} at row {row_index}")
        if digest != digest.strip():
            raise ValueError(f"invalid seqcol_digest for assembly {label_text!r} at row {row_index}: {digest!r}")
        if digest in seen:
            previous_index, previous_label = seen[digest]
            raise ValueError(
                f"duplicate seqcol_digest/member key {digest!r}: "
                f"row {previous_index} assembly {previous_label!r} and row {row_index} assembly {label_text!r}"
            )
        seen[digest] = (row_index, label_text)


def _sha256_resource(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return "sha256:" + digest.hexdigest(), byte_count


def _update_datapackage(path: Path, *, output_dir: Path, version: str) -> None:
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    doc["version"] = version

    resources = doc.get("resources")
    if not isinstance(resources, list):
        raise ValueError(f"{path} must contain a resources list")

    wanted = {"assemblies.csv", "contigs.csv", "contig_aliases.csv"}
    seen: set[str] = set()
    for resource in resources:
        if not isinstance(resource, dict):
            raise ValueError(f"{path} contains a non-mapping resource")
        resource_path = resource.get("path")
        if resource_path in wanted:
            resource_hash, resource_bytes = _sha256_resource(output_dir / str(resource_path))
            resource["hash"] = resource_hash
            resource["bytes"] = resource_bytes
            seen.add(resource_path)

    missing = wanted - seen
    if missing:
        raise ValueError(f"{path} missing resources: {', '.join(sorted(missing))}")

    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def _replace_frontmatter_value(text: str, key: str, value: str) -> str:
    prefix = f"{key}:"
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = f"{key}: {value}"
            return "\n".join(lines) + "\n"
    raise ValueError(f"missing frontmatter key {key!r}")


def _update_entity(path: Path, *, assembly_count: int, version: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = _replace_frontmatter_value(text, "version", f'"{version}"')
    text = _replace_frontmatter_value(text, "updated", f'"{datetime.now(UTC).date().isoformat()}"')
    text = _replace_frontmatter_value(text, "assembly_count", str(assembly_count))
    path.write_text(text, encoding="utf-8")


def build_registry(
    *,
    output_dir: Path,
    sources_path: Path,
    datapackage_path: Path | None = None,
    entity_path: Path | None = None,
) -> None:
    sources = yaml.safe_load(sources_path.read_text(encoding="utf-8"))
    if not isinstance(sources, dict):
        raise ValueError(f"{sources_path} must contain a YAML mapping")

    artifact_version = _require_text(sources, "artifact_version", label=str(sources_path))
    seqcol_base_url = _require_text(sources, "seqcol_base_url", label=str(sources_path))
    assemblies = sources.get("assemblies")
    if not isinstance(assemblies, list) or not assemblies:
        raise ValueError(f"{sources_path} assemblies must be a non-empty list")

    assembly_rows: list[dict[str, Any]] = []
    contig_rows: list[dict[str, Any]] = []
    alias_rows: list[dict[str, Any]] = []

    for index, src in enumerate(assemblies):
        if not isinstance(src, dict):
            raise ValueError(f"invalid assembly at index {index}: expected mapping, got {type(src).__name__}")

        label = _require_text(src, "label", label=f"assembly {index}")
        aliases = _aliases(src, label=label)
        seqcol_digest = _require_text(src, "seqcol_digest", label=label)
        source_collection_url = _require_text(src, "source_collection_url", label=label)
        assembly_report_url = _require_text(src, "assembly_report_url", label=label)
        assembly_report_match_column = (
            _require_text(src, "assembly_report_match_column", label=label)
            if "assembly_report_match_column" in src
            else "Sequence-Name"
        )
        accession = _require_text(src, "accession", label=label)
        naming = _require_text(src, "naming", label=label)

        level2 = fetch_seqcol_level2(seqcol_digest, base_url=seqcol_base_url)
        assembly_rows.append(
            build_registry_row(
                level2=level2,
                label=label,
                aliases=aliases,
                accession=accession,
                naming=naming,
                server_digest=seqcol_digest,
                source_collection_url=source_collection_url,
                source_url=source_collection_url,
            )
        )
        assembly_contigs = build_contig_rows(level2=level2, seqcol_digest=seqcol_digest)
        contig_rows.extend(assembly_contigs)
        report_rows = parse_assembly_report(fetch_text(assembly_report_url))
        alias_rows.extend(
            build_contig_alias_rows(
                contig_rows=assembly_contigs,
                report_rows=report_rows,
                match_column=assembly_report_match_column,
            )
        )

    validate_registry_label_bindings(assembly_rows)
    _validate_unique_seqcol_digests(assembly_rows)
    assembly_rows.sort(key=lambda row: row["label"])
    contig_rows.sort(key=lambda row: (row["seqcol_digest"], int(row["sequence_index"])))
    alias_rows.sort(key=lambda row: (row["seqcol_digest"], row["refget_digest"], row["alias_kind"], row["alias"]))

    _write_csv(output_dir / "assemblies.csv", _ASSEMBLY_FIELDS, assembly_rows)
    _write_csv(output_dir / "contigs.csv", _CONTIG_FIELDS, contig_rows)
    _write_csv(output_dir / "contig_aliases.csv", _ALIAS_FIELDS, alias_rows)
    if datapackage_path is not None:
        _update_datapackage(datapackage_path, output_dir=output_dir, version=artifact_version)
    if entity_path is not None:
        _update_entity(entity_path, assembly_count=len(assembly_rows), version=artifact_version)
    print(f"wrote {len(assembly_rows)} assemblies, {len(contig_rows)} contigs, {len(alias_rows)} aliases to {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build pinned assembly registry CSV resources.")
    parser.add_argument("--output-dir", type=Path, default=_OUT, help="Directory for assemblies.csv and related outputs.")
    parser.add_argument("--sources", type=Path, default=_HERE / "sources.yaml", help="Pinned source declarations.")
    parser.add_argument("--datapackage", type=Path, default=_DATAPACKAGE, help="Path to datapackage.yaml.")
    parser.add_argument("--entity", type=Path, default=_ENTITY, help="Path to entity.md.")
    parser.add_argument("--update-datapackage", action="store_true", help="Refresh datapackage resource hashes and bytes.")
    parser.add_argument("--update-entity", action="store_true", help="Refresh entity metadata.")
    args = parser.parse_args()

    default_output = args.output_dir == _OUT
    build_registry(
        output_dir=args.output_dir,
        sources_path=args.sources,
        datapackage_path=args.datapackage if args.update_datapackage or default_output else None,
        entity_path=args.entity if args.update_entity or default_output else None,
    )


def _self_check() -> None:
    rows = [
        {"seqcol_digest": "SQ.DUP", "label": "one"},
        {"seqcol_digest": "SQ.DUP", "label": "two"},
    ]
    try:
        _validate_unique_seqcol_digests(rows)
    except ValueError as exc:
        if "duplicate seqcol_digest" not in str(exc):
            raise
    else:
        raise AssertionError("duplicate seqcol_digest was not rejected")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-check"]:
        _self_check()
    else:
        main()
