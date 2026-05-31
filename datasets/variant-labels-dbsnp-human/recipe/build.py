from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import os
import re
import sqlite3
import time
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

# science:code
# status: exploratory
# science:end

DATASET_NAME = "variant-labels-dbsnp-human"
OUTPUT_ROOT_TOKEN = "${OUTPUT_ROOT}"
LOCKFILE_PATH = Path(__file__).with_name("lockfile.yaml")
DATAPACKAGE_PATH = Path(__file__).parents[1] / "datapackage.yaml"
COMMONS_ROOT = Path(__file__).parents[3]
ASSEMBLY_REGISTRY_PATH = COMMONS_ROOT / "datasets" / "assembly-registry" / "assemblies.csv"
SQLITE_RESOURCE = Path("rsid_mappings.sqlite")
SUMMARY_RESOURCE = Path("build-summary.yaml")
RSID_PATTERN = re.compile(r"^rs[1-9][0-9]*$")
LITERAL_ALLELE_PATTERN = re.compile(r"^[ACGTN]+$")
SOURCE_ASSEMBLIES = {
    "GCF_000001405.40.gz": {"label": "GRCh38", "accession": "GCF_000001405.40"},
    "GCF_000001405.25.gz": {"label": "GRCh37", "accession": "GCF_000001405.25"},
}


def build_dataset(
    *,
    input_root: Path,
    output_root: Path,
    lockfile_path: Path = LOCKFILE_PATH,
    assembly_registry_path: Path = ASSEMBLY_REGISTRY_PATH,
    datapackage_path: Path = DATAPACKAGE_PATH,
    update_datapackage: bool = False,
) -> dict[str, Any]:
    started = time.monotonic()
    lock = load_lockfile(lockfile_path)
    assembly_digests = load_assembly_digests(assembly_registry_path)
    output_dir = output_root / DATASET_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    sqlite_path = output_dir / SQLITE_RESOURCE
    summary_path = output_dir / SUMMARY_RESOURCE
    sqlite_path.unlink(missing_ok=True)

    totals: Counter[str] = Counter()
    skipped: Counter[str] = Counter()
    per_assembly: dict[str, dict[str, int]] = {
        spec["label"]: {"input_rows": 0, "retained_alleles": 0}
        for spec in SOURCE_ASSEMBLIES.values()
    }
    source_urls: dict[str, str] = {}
    source_sha256: dict[str, str] = {}

    with sqlite3.connect(sqlite_path) as conn:
        create_schema(conn)
        metadata = {
            "dataset": DATASET_NAME,
            "dbsnp_build": "157",
            "built_at_utc": datetime.now(UTC).isoformat(),
            "assembly_registry": str(assembly_registry_path),
        }
        conn.executemany("INSERT INTO metadata (key, value) VALUES (?, ?)", sorted(metadata.items()))

        for filename in SOURCE_ASSEMBLIES:
            entry = lock_resource(lock, filename)
            source_path = input_root / str(entry["path"])
            validate_source_file(source_path, entry)
            spec = SOURCE_ASSEMBLIES[filename]
            label = spec["label"]
            seqcol_digest = assembly_digests[label]
            source_urls[filename] = str(entry["url"])
            source_sha256[filename] = str(entry["sha256"])
            file_counts = ingest_vcf(
                conn=conn,
                path=source_path,
                source_vcf=filename,
                seqcol_digest=seqcol_digest,
                skipped=skipped,
            )
            totals.update(file_counts)
            per_assembly[label]["input_rows"] += file_counts["input_rows"]
            per_assembly[label]["retained_alleles"] += file_counts["retained_alleles"]

    sqlite_bytes = sqlite_path.stat().st_size
    distinct_rsids = count_distinct_rsids(sqlite_path)
    summary = {
        "dataset": DATASET_NAME,
        "dbsnp_build": 157,
        "input_rows": totals["input_rows"],
        "retained_alleles": totals["retained_alleles"],
        "skipped": dict(sorted(skipped.items())),
        "distinct_rsids": distinct_rsids,
        "per_assembly": per_assembly,
        "source_urls": source_urls,
        "source_sha256": source_sha256,
        "sqlite_bytes": sqlite_bytes,
        "build_seconds": round(time.monotonic() - started, 3),
    }
    summary_path.write_text(yaml.safe_dump(summary, sort_keys=False), encoding="utf-8")

    if update_datapackage:
        write_datapackage(datapackage_path, output_dir=output_dir)
    return summary


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE rsid_alleles (
          rsid TEXT NOT NULL,
          seqcol_digest TEXT NOT NULL,
          contig TEXT NOT NULL,
          pos0 INTEGER NOT NULL,
          ref TEXT NOT NULL,
          alt TEXT NOT NULL,
          source_vcf TEXT NOT NULL,
          allele_index INTEGER NOT NULL,
          PRIMARY KEY (rsid, seqcol_digest, contig, pos0, ref, alt, source_vcf, allele_index)
        );
        CREATE INDEX rsid_alleles_lookup ON rsid_alleles (rsid, seqcol_digest);
        """
    )


def ingest_vcf(
    *,
    conn: sqlite3.Connection,
    path: Path,
    source_vcf: str,
    seqcol_digest: str,
    skipped: Counter[str],
) -> Counter[str]:
    counts: Counter[str] = Counter()
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if not line or line.startswith("#"):
                continue
            counts["input_rows"] += 1
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 5:
                skipped["malformed_row"] += 1
                continue
            chrom, pos_text, id_text, ref_text, alt_text = fields[:5]
            rsids = [part for part in id_text.split(";") if RSID_PATTERN.fullmatch(part)]
            if not rsids:
                skipped["no_rsid"] += 1
                continue
            if not pos_text:
                skipped["missing_pos"] += 1
                continue
            try:
                pos0 = int(pos_text) - 1
            except ValueError:
                skipped["invalid_pos"] += 1
                continue
            if pos0 < 0:
                skipped["invalid_pos"] += 1
                continue
            ref = ref_text.upper()
            if not is_literal_allele(ref):
                skipped["non_literal_ref"] += 1
                continue
            alts = alt_text.split(",")
            for allele_index, alt_text_part in enumerate(alts, start=1):
                alt = alt_text_part.upper()
                if not alt:
                    skipped["missing_alt"] += 1
                    continue
                if is_symbolic_or_breakend(alt):
                    skipped["symbolic_or_breakend_alt"] += 1
                    continue
                if not is_literal_allele(alt):
                    skipped["non_literal_alt"] += 1
                    continue
                for rsid in rsids:
                    cursor = conn.execute(
                        """
                        INSERT OR IGNORE INTO rsid_alleles
                        (rsid, seqcol_digest, contig, pos0, ref, alt, source_vcf, allele_index)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (rsid, seqcol_digest, chrom, pos0, ref, alt, source_vcf, allele_index),
                    )
                    counts["retained_alleles"] += cursor.rowcount
    return counts


def is_literal_allele(value: str) -> bool:
    return bool(value) and bool(LITERAL_ALLELE_PATTERN.fullmatch(value))


def is_symbolic_or_breakend(value: str) -> bool:
    return value in {".", "*"} or value.startswith("<") or "[" in value or "]" in value


def load_lockfile(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"missing lockfile: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("resources"), dict):
        raise ValueError(f"{path}: expected lockfile with resources mapping")
    for filename in SOURCE_ASSEMBLIES:
        lock_resource(raw, filename)
    return raw


def lock_resource(lock: dict[str, Any], filename: str) -> dict[str, Any]:
    entry = lock["resources"].get(filename)
    if not isinstance(entry, dict):
        raise ValueError(f"lockfile missing resource {filename!r}")
    for key in ("url", "path", "sha256", "bytes"):
        if key not in entry:
            raise ValueError(f"lockfile resource {filename!r} missing {key}")
    if "/latest_release/" in str(entry["url"]).lower():
        raise ValueError(f"dbSNP latest_release URLs are mutable: {entry['url']}")
    return entry


def validate_source_file(path: Path, entry: dict[str, Any]) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"missing source archive: {path}")
    sha256, byte_count = stream_hash_and_bytes(path)
    if sha256 != str(entry["sha256"]):
        raise ValueError(f"{path}: sha256 mismatch against lockfile")
    if byte_count != int(entry["bytes"]):
        raise ValueError(f"{path}: byte count mismatch against lockfile")


def load_assembly_digests(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise FileNotFoundError(f"missing assembly registry: {path}")
    required = {"seqcol_digest", "label", "accession"}
    by_label: dict[str, str] = {}
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise ValueError(f"{path}: expected columns including {sorted(required)}")
        for row in reader:
            for spec in SOURCE_ASSEMBLIES.values():
                label = spec["label"]
                accession = spec["accession"]
                if row["label"] == label and row["accession"] == accession:
                    digest = row["seqcol_digest"].strip()
                    if not digest:
                        raise ValueError(f"{path}: blank seqcol_digest for {label}")
                    if label in by_label:
                        raise ValueError(f"{path}: duplicate registry row for {label} {accession}")
                    by_label[label] = digest
    missing = sorted({spec["label"] for spec in SOURCE_ASSEMBLIES.values()} - set(by_label))
    if missing:
        raise ValueError(f"{path}: missing assembly registry rows for {', '.join(missing)}")
    return by_label


def count_distinct_rsids(sqlite_path: Path) -> int:
    with sqlite3.connect(sqlite_path) as conn:
        row = conn.execute("SELECT COUNT(DISTINCT rsid) FROM rsid_alleles").fetchone()
    return int(row[0])


def write_datapackage(path: Path, *, output_dir: Path) -> None:
    sqlite_hash, sqlite_bytes = stream_hash_and_bytes(output_dir / SQLITE_RESOURCE)
    summary_hash, summary_bytes = stream_hash_and_bytes(output_dir / SUMMARY_RESOURCE)
    doc = {
        "name": DATASET_NAME,
        "profile": "data-package",
        "resources": [
            {
                "name": "rsid_mappings",
                "path": SQLITE_RESOURCE.as_posix(),
                "format": "sqlite",
                "mediatype": "application/vnd.sqlite3",
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{SQLITE_RESOURCE.as_posix()}",
                },
                "hash": sqlite_hash,
                "bytes": sqlite_bytes,
            },
            {
                "name": "build_summary",
                "path": SUMMARY_RESOURCE.as_posix(),
                "format": "yaml",
                "mediatype": "application/x-yaml",
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{SUMMARY_RESOURCE.as_posix()}",
                },
                "hash": summary_hash,
                "bytes": summary_bytes,
            },
        ],
    }
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def stream_hash_and_bytes(path: Path) -> tuple[str, int]:
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
    parser = argparse.ArgumentParser(description="Build dbSNP rsID to small-allele SQLite mappings.")
    parser.add_argument("--input-root", type=Path, help="Directory containing locked dbSNP .gz archives.")
    parser.add_argument("--output-root", type=Path, help="Commons output root. Dataset directory is created below it.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to recipe lockfile.")
    parser.add_argument(
        "--assembly-registry",
        type=Path,
        default=ASSEMBLY_REGISTRY_PATH,
        help="Path to assembly-registry assemblies.csv.",
    )
    parser.add_argument("--datapackage", type=Path, default=DATAPACKAGE_PATH, help="Path to datapackage.yaml.")
    parser.add_argument("--update-datapackage", action="store_true", help="Rewrite datapackage hashes and bytes.")
    args = parser.parse_args()

    commons_root = resolve_commons_data_root()
    input_root = args.input_root or commons_root / DATASET_NAME / "_src"
    output_root = args.output_root or commons_root
    summary = build_dataset(
        input_root=input_root,
        output_root=output_root,
        lockfile_path=args.lockfile,
        assembly_registry_path=args.assembly_registry,
        datapackage_path=args.datapackage,
        update_datapackage=args.update_datapackage,
    )
    print(
        "wrote "
        f"{summary['retained_alleles']} retained dbSNP alleles "
        f"for {summary['distinct_rsids']} rsIDs to {output_root / DATASET_NAME}"
    )


if __name__ == "__main__":
    main()
