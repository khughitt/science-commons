from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import os
import urllib.parse
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

DATASET_NAME = "cytoband-hg19"
OUTPUT_ROOT_TOKEN = "${OUTPUT_ROOT}"
RESOURCE_NAME = "cytoBand"
SOURCE_RESOURCE_PATH = Path("sources/cytoBand.txt.gz")
CYTOBANDS_RESOURCE_PATH = Path("cytobands.csv")
LOCKFILE_PATH = Path(__file__).with_name("lockfile.yaml")
DATAPACKAGE_PATH = Path(__file__).parents[1] / "datapackage.yaml"
ENTITY_PATH = Path(__file__).parents[1] / "entity.md"
REJECTED_URL_PARTS = ("latest", "current", "download/test")
FIELDNAMES = ["chrom", "start", "end", "name", "gie_stain"]
ALLOWED_STAINS = frozenset({"gneg", "gpos25", "gpos50", "gpos75", "gpos100", "acen", "gvar", "stalk"})
CHROM_ORDER = {f"chr{i}": i for i in range(1, 23)} | {"chrX": 23, "chrY": 24, "chrM": 25}


def build_dataset(
    *,
    data_dir: Path,
    lockfile_path: Path = LOCKFILE_PATH,
    datapackage_path: Path = DATAPACKAGE_PATH,
    entity_path: Path = ENTITY_PATH,
) -> None:
    lock = load_lockfile(lockfile_path)
    entry = lock["resources"][RESOURCE_NAME]
    source_path = data_dir / SOURCE_RESOURCE_PATH
    if not source_path.is_file():
        raise FileNotFoundError(f"required source file is absent: {source_path}")
    source_sha256, source_bytes = stream_sha256_and_bytes(source_path)
    if source_sha256.removeprefix("sha256:") != str(entry["sha256"]):
        raise ValueError(f"{source_path}: sha256 mismatch against lockfile")
    if source_bytes != int(entry["bytes"]):
        raise ValueError(f"{source_path}: byte count mismatch against lockfile")

    rows = parse_source_rows(source_path)
    expected_rows = entry.get("decompressed_rows")
    if expected_rows is not None and len(rows) != int(expected_rows):
        raise ValueError(f"{source_path}: expected {expected_rows} rows, observed {len(rows)}")

    cytobands_path = data_dir / CYTOBANDS_RESOURCE_PATH
    write_cytobands(cytobands_path, rows)
    cytobands_hash, cytobands_bytes = stream_sha256_and_bytes(cytobands_path)
    previous_hash = read_existing_cytobands_hash(datapackage_path)
    if previous_hash != cytobands_hash:
        write_datapackage(datapackage_path, cytobands_hash=cytobands_hash, cytobands_bytes=cytobands_bytes)
        update_entity(entity_path, row_count=len(rows))


def parse_source_rows(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
        for row_index, line in enumerate(fh, start=1):
            stripped = line.rstrip("\n")
            if not stripped:
                continue
            cells = stripped.split("\t")
            if len(cells) != 5:
                raise ValueError(f"{path}: row {row_index}: expected 5 tab-separated fields, got {len(cells)}")
            chrom, start, end, name, gie_stain = cells
            for column, value in (("chrom", chrom), ("name", name), ("gie_stain", gie_stain)):
                if not value or value != value.strip():
                    raise ValueError(f"{path}: row {row_index}: invalid {column} {value!r}")
            if not start.isdecimal() or not end.isdecimal():
                raise ValueError(f"{path}: row {row_index}: invalid interval {start!r}-{end!r}")
            start_i = int(start)
            end_i = int(end)
            if start_i < 0 or end_i <= start_i:
                raise ValueError(f"{path}: row {row_index}: invalid interval {start!r}-{end!r}")
            if gie_stain not in ALLOWED_STAINS:
                raise ValueError(f"{path}: row {row_index}: invalid gie_stain {gie_stain!r}")
            key = (chrom, str(start_i), str(end_i), name, gie_stain)
            if key in seen:
                raise ValueError(f"{path}: row {row_index}: duplicate cytoband row {key!r}")
            seen.add(key)
            rows.append({"chrom": chrom, "start": str(start_i), "end": str(end_i), "name": name, "gie_stain": gie_stain})
    return sorted(rows, key=cytoband_sort_key)


def cytoband_sort_key(row: dict[str, str]) -> tuple[int, str, int, int, str, str]:
    chrom = row["chrom"]
    return (CHROM_ORDER.get(chrom, 10_000), chrom, int(row["start"]), int(row["end"]), row["name"], row["gie_stain"])


def write_cytobands(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def load_lockfile(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"missing lockfile: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("resources"), dict):
        raise ValueError(f"{path}: expected lockfile with resources mapping")
    entry = raw["resources"].get(RESOURCE_NAME)
    if not isinstance(entry, dict):
        raise ValueError(f"{path}: missing {RESOURCE_NAME} resource")
    for key in ("url", "sha256", "bytes", "path"):
        if key not in entry:
            raise ValueError(f"{path}: {RESOURCE_NAME} missing {key}")
    validate_explicit_url(str(entry["url"]))
    return raw


def validate_explicit_url(url: str) -> str:
    normalized = url.strip()
    if not normalized:
        raise ValueError("URL must be non-empty")
    parsed = urllib.parse.urlparse(normalized)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"URL must be an absolute http(s) URL, got {url!r}")
    lowered = normalized.lower()
    for rejected in REJECTED_URL_PARTS:
        if rejected in lowered:
            raise ValueError(f"URL contains mutable or disallowed segment {rejected!r}: {url}")
    return normalized


def write_datapackage(path: Path, *, cytobands_hash: str, cytobands_bytes: int) -> None:
    doc = {
        "name": DATASET_NAME,
        "profile": "data-package",
        "resources": [
            {
                "name": "cytobands",
                "path": CYTOBANDS_RESOURCE_PATH.as_posix(),
                "format": "csv",
                "mediatype": "text/csv",
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{CYTOBANDS_RESOURCE_PATH.as_posix()}",
                },
                "hash": cytobands_hash,
                "bytes": cytobands_bytes,
            }
        ],
    }
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def read_existing_cytobands_hash(path: Path) -> str | None:
    if not path.is_file():
        return None
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: expected datapackage mapping")
    resources = raw.get("resources")
    if not isinstance(resources, list):
        raise ValueError(f"{path}: expected resources list")
    for resource in resources:
        if isinstance(resource, dict) and resource.get("name") == "cytobands":
            value = resource.get("hash")
            if not isinstance(value, str) or not value:
                raise ValueError(f"{path}: cytobands resource missing hash")
            return value
    raise ValueError(f"{path}: missing cytobands resource")


def update_entity(path: Path, *, row_count: int) -> None:
    text = path.read_text(encoding="utf-8")
    today = datetime.now(UTC).date().isoformat()
    replacements = {
        "updated:": f'updated: "{today}"',
        "row_count:": f"row_count: {row_count}",
    }
    lines: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        replaced = False
        for prefix, new_line in replacements.items():
            if line.startswith(prefix):
                lines.append(new_line)
                seen.add(prefix)
                replaced = True
                break
        if not replaced:
            lines.append(line)
    if "row_count:" not in seen:
        insert_at = lines.index("---", 1)
        lines.insert(insert_at, f"row_count: {row_count}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def stream_sha256_and_bytes(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return f"sha256:{digest.hexdigest()}", byte_count


def resolve_commons_data_root() -> Path:
    if env := os.environ.get("SCIENCE_COMMONS_DATA_ROOT"):
        return Path(env)
    return Path("/data/science-commons")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build UCSC hg19 cytoband resources.")
    parser.add_argument("--data-dir", type=Path, help="Dataset data directory. Defaults under SCIENCE_COMMONS_DATA_ROOT.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to recipe lockfile.")
    parser.add_argument("--datapackage", type=Path, default=DATAPACKAGE_PATH, help="Path to rewrite datapackage.yaml.")
    parser.add_argument("--entity", type=Path, default=ENTITY_PATH, help="Path to rewrite entity.md.")
    args = parser.parse_args()

    data_dir = args.data_dir or resolve_commons_data_root() / DATASET_NAME
    build_dataset(data_dir=data_dir, lockfile_path=args.lockfile, datapackage_path=args.datapackage, entity_path=args.entity)
    print(f"wrote cytoband resources to {data_dir}")


if __name__ == "__main__":
    main()
