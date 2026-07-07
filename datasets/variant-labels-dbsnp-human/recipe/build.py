from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import os
import re
import shutil
import sqlite3
import sys
import time
from collections import Counter
from contextlib import ExitStack, closing
from datetime import UTC, datetime
from pathlib import Path
from collections.abc import Iterator
from typing import Any

import yaml

# science:code
# status: exploratory
# science:end

DATASET_NAME = "variant-labels-dbsnp-human"
OUTPUT_ROOT_TOKEN = "${OUTPUT_ROOT}"
LOCKFILE_PATH = Path(__file__).with_name("lockfile.yaml")
DATAPACKAGE_PATH = Path(__file__).parents[1] / "datapackage.yaml"
SQLITE_RESOURCE = Path("rsid_mappings.sqlite")
SUMMARY_RESOURCE = Path("build-summary.yaml")
RSID_PATTERN = re.compile(r"^rs[1-9][0-9]*$")
LITERAL_ALLELE_PATTERN = re.compile(r"^[ACGTN]+$")
BATCH_SIZE = 50_000
SHARD_COUNT = 64
SHARD_IDS = tuple(f"{index:02x}" for index in range(SHARD_COUNT))
ROW_FIELDS = ("rsid", "contig", "pos0", "ref", "alt", "source_vcf", "allele_index")
SOURCE_ASSEMBLIES = {
    "GCF_000001405.40.gz": {
        "label": "GRCh38",
        "source_accession": "GCF_000001405.40",
        "registry_accession": "GCA_000001405.15",
    },
    "GCF_000001405.25.gz": {
        "label": "GRCh37",
        "source_accession": "GCF_000001405.25",
        "registry_accession": "GCA_000001405.14",
    },
}
PINNED_SOURCE_URLS = {
    "GCF_000001405.40.gz": "https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.40.gz",
    "GCF_000001405.25.gz": "https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.25.gz",
}
EXPECTED_LOCK_RESOURCES = {
    filename: {
        "url": url,
        "path": filename,
        "md5_url": f"{url}.md5",
        "md5_path": f"{filename}.md5",
    }
    for filename, url in PINNED_SOURCE_URLS.items()
}
REQUIRED_LOCK_KEYS = ("url", "path", "md5_url", "md5_path", "md5", "sha256", "bytes")
MD5_PATTERN = re.compile(r"^[0-9a-fA-F]{32}$")

AlleleRow = tuple[str, str, int, str, str, str, int]


def build_dataset(
    *,
    input_root: Path,
    output_root: Path,
    dataset_output_dir: Path | None = None,
    lockfile_path: Path = LOCKFILE_PATH,
    assembly_registry_path: Path | None = None,
    datapackage_path: Path = DATAPACKAGE_PATH,
    update_datapackage: bool = False,
) -> dict[str, Any]:
    started = time.monotonic()
    lock = load_lockfile(lockfile_path)
    assembly_registry_path = assembly_registry_path or default_assembly_registry_path(resolve_commons_data_root())
    assembly_digests = load_assembly_digests(assembly_registry_path)
    output_dir = dataset_output_dir or output_root / DATASET_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    sqlite_path = output_dir / SQLITE_RESOURCE
    tmp_sqlite_path = output_dir / f".{SQLITE_RESOURCE.name}.{os.getpid()}.tmp"
    summary_path = output_dir / SUMMARY_RESOURCE
    tmp_summary_path = output_dir / f".{SUMMARY_RESOURCE.name}.{os.getpid()}.tmp"

    source_inputs = []
    for filename in SOURCE_ASSEMBLIES:
        entry = lock_resource(lock, filename)
        source_path = input_root / str(entry["path"])
        validate_source_file(source_path, entry)
        source_inputs.append((filename, entry, source_path))

    totals: Counter[str] = Counter()
    skipped: Counter[str] = Counter()
    per_assembly: dict[str, dict[str, int]] = {
        spec["label"]: {"input_rows": 0, "retained_alleles": 0, "duplicate_alleles": 0}
        for spec in SOURCE_ASSEMBLIES.values()
    }
    source_urls: dict[str, str] = {}
    source_sha256: dict[str, str] = {}

    try:
        tmp_sqlite_path.unlink(missing_ok=True)
        with closing(sqlite3.connect(tmp_sqlite_path)) as conn:
            configure_bulk_sqlite(conn)
            create_schema(conn)
            built_at_utc = datetime.now(UTC).isoformat()
            metadata = {
                "dataset": DATASET_NAME,
                "dbsnp_build": "157",
                "built_at_utc": built_at_utc,
                "assembly_registry": str(assembly_registry_path),
            }
            conn.executemany("INSERT INTO metadata (key, value) VALUES (?, ?)", sorted(metadata.items()))

            for filename, entry, source_path in source_inputs:
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
                per_assembly[label]["duplicate_alleles"] += file_counts["duplicate_alleles"]
            create_lookup_index(conn)
            conn.execute("PRAGMA optimize")
            conn.commit()

        sqlite_bytes = tmp_sqlite_path.stat().st_size
        distinct_rsids = count_distinct_rsids(tmp_sqlite_path)
        tmp_sqlite_path.replace(sqlite_path)
    except Exception:
        tmp_sqlite_path.unlink(missing_ok=True)
        raise

    summary = {
        "dataset": DATASET_NAME,
        "dbsnp_build": 157,
        "built_at_utc": built_at_utc,
        "input_rows": totals["input_rows"],
        "retained_alleles": totals["retained_alleles"],
        "duplicate_alleles": totals["duplicate_alleles"],
        "skipped": dict(sorted(skipped.items())),
        "distinct_rsids": distinct_rsids,
        "per_assembly": per_assembly,
        "source_urls": source_urls,
        "source_sha256": source_sha256,
        "sqlite_bytes": sqlite_bytes,
        "build_seconds": round(time.monotonic() - started, 3),
    }
    write_yaml_atomic(summary_path, tmp_summary_path, summary)

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
        """
    )


def configure_bulk_sqlite(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA journal_mode = OFF;
        PRAGMA synchronous = OFF;
        PRAGMA temp_store = MEMORY;
        PRAGMA cache_size = -200000;
        PRAGMA locking_mode = EXCLUSIVE;
        """
    )


def create_lookup_index(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE INDEX rsid_alleles_lookup ON rsid_alleles (rsid, seqcol_digest)")


def shard_ids(*, shard_count: int = SHARD_COUNT) -> tuple[str, ...]:
    width = max(2, len(f"{shard_count - 1:x}"))
    return tuple(f"{index:0{width}x}" for index in range(shard_count))


def shard_id_for_rsid(rsid: str, *, shard_count: int = SHARD_COUNT) -> str:
    normalized = rsid.lower()
    if not RSID_PATTERN.fullmatch(normalized):
        raise ValueError(f"invalid rsID for sharding: {rsid!r}")
    width = max(2, len(f"{shard_count - 1:x}"))
    return f"{int(normalized[2:]) % shard_count:0{width}x}"


def split_archive_to_shards(
    *,
    archive_path: Path,
    source_vcf: str,
    output_dir: Path,
    shard_count: int = SHARD_COUNT,
    lockfile_path: Path | None = None,
    marker_path: Path | None = None,
) -> dict[str, Any]:
    if lockfile_path is not None:
        lock = load_lockfile(lockfile_path)
        validate_source_file(archive_path, lock_resource(lock, source_vcf, lockfile_path=lockfile_path))

    ids = shard_ids(shard_count=shard_count)
    summary_path = output_dir / "split-summary.yaml"
    shard_paths = [output_dir / f"shard-{shard_id}.tsv.gz" for shard_id in ids]
    if output_dir.exists():
        missing = [path for path in [summary_path, *shard_paths] if not path.is_file()]
        if not missing:
            summary = _read_yaml(summary_path)
            if marker_path is not None:
                write_marker(marker_path, summary)
            return summary
        missing_text = ", ".join(str(path) for path in missing[:5])
        raise FileExistsError(f"{output_dir}: incomplete split directory; missing {missing_text}")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = output_dir.with_name(f".{output_dir.name}.{os.getpid()}.tmp")
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True)

    counts: Counter[str] = Counter()
    skipped: Counter[str] = Counter()
    emitted_by_shard: Counter[str] = Counter()
    try:
        with ExitStack() as stack:
            writers = {
                shard_id: stack.enter_context(gzip.open(tmp_dir / f"shard-{shard_id}.tsv.gz", "wt", encoding="utf-8"))
                for shard_id in ids
            }
            for row in iter_vcf_allele_rows(path=archive_path, source_vcf=source_vcf, skipped=skipped, counts=counts):
                shard_id = shard_id_for_rsid(row[0], shard_count=shard_count)
                writers[shard_id].write("\t".join(str(value) for value in row))
                writers[shard_id].write("\n")
                emitted_by_shard[shard_id] += 1

        summary = {
            "source_vcf": source_vcf,
            "archive_path": str(archive_path),
            "shard_count": shard_count,
            "input_rows": counts["input_rows"],
            "emitted_alleles": sum(emitted_by_shard.values()),
            "skipped": dict(sorted(skipped.items())),
            "emitted_by_shard": {shard_id: emitted_by_shard[shard_id] for shard_id in ids},
        }
        (tmp_dir / "split-summary.yaml").write_text(yaml.safe_dump(summary, sort_keys=False), encoding="utf-8")
        tmp_dir.rename(output_dir)
        if marker_path is not None:
            write_marker(marker_path, summary)
        return summary
    except Exception:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise


def build_shard_sqlite(
    *,
    rows_path: Path,
    sqlite_path: Path,
    summary_path: Path,
    seqcol_digest: str,
    shard_id: str,
    source_vcf: str,
) -> dict[str, Any]:
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_sqlite_path = sqlite_path.with_name(f".{sqlite_path.name}.{os.getpid()}.tmp")
    tmp_summary_path = summary_path.with_name(f".{summary_path.name}.{os.getpid()}.tmp")
    counts: Counter[str] = Counter()
    batch: list[tuple[str, str, str, int, str, str, str, int]] = []
    started = time.monotonic()
    try:
        tmp_sqlite_path.unlink(missing_ok=True)
        with closing(sqlite3.connect(tmp_sqlite_path)) as conn:
            configure_bulk_sqlite(conn)
            create_schema(conn)
            conn.executemany(
                "INSERT INTO metadata (key, value) VALUES (?, ?)",
                sorted(
                    {
                        "dataset": DATASET_NAME,
                        "source_vcf": source_vcf,
                        "shard_id": shard_id,
                    }.items()
                ),
            )
            with gzip.open(rows_path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    fields = line.rstrip("\n").split("\t")
                    if len(fields) != len(ROW_FIELDS):
                        raise ValueError(f"{rows_path}: expected {len(ROW_FIELDS)} tab-separated fields")
                    rsid, contig, pos0_text, ref, alt, row_source_vcf, allele_index_text = fields
                    if row_source_vcf != source_vcf:
                        raise ValueError(f"{rows_path}: row source {row_source_vcf!r} != {source_vcf!r}")
                    batch.append(
                        (
                            rsid,
                            seqcol_digest,
                            contig,
                            int(pos0_text),
                            ref,
                            alt,
                            row_source_vcf,
                            int(allele_index_text),
                        )
                    )
                    if len(batch) >= BATCH_SIZE:
                        flush_insert_batch(conn, batch, counts)
            flush_insert_batch(conn, batch, counts)
            conn.commit()
        sqlite_bytes = tmp_sqlite_path.stat().st_size
        tmp_sqlite_path.replace(sqlite_path)

        summary = {
            "source_vcf": source_vcf,
            "shard_id": shard_id,
            "seqcol_digest": seqcol_digest,
            "retained_alleles": counts["retained_alleles"],
            "duplicate_alleles": counts["duplicate_alleles"],
            "sqlite_bytes": sqlite_bytes,
            "build_seconds": round(time.monotonic() - started, 3),
        }
        write_yaml_atomic(summary_path, tmp_summary_path, summary)
        return summary
    except Exception:
        tmp_sqlite_path.unlink(missing_ok=True)
        tmp_summary_path.unlink(missing_ok=True)
        raise


def merge_shard_sqlites(
    *,
    shard_paths: list[Path],
    split_summary_paths: list[Path],
    shard_summary_paths: list[Path],
    output_dir: Path,
    datapackage_path: Path | None = None,
    source_metadata: dict[str, dict[str, str]] | None = None,
) -> dict[str, Any]:
    started = time.monotonic()
    output_dir.mkdir(parents=True, exist_ok=True)
    sqlite_path = output_dir / SQLITE_RESOURCE
    summary_path = output_dir / SUMMARY_RESOURCE
    tmp_sqlite_path = output_dir / f".{SQLITE_RESOURCE.name}.{os.getpid()}.tmp"
    tmp_summary_path = output_dir / f".{SUMMARY_RESOURCE.name}.{os.getpid()}.tmp"
    split_summaries = [_read_yaml(path) for path in split_summary_paths]
    shard_summaries = [_read_yaml(path) for path in shard_summary_paths]
    source_metadata = source_metadata or {}
    built_at_utc = datetime.now(UTC).isoformat()

    try:
        tmp_sqlite_path.unlink(missing_ok=True)
        with closing(sqlite3.connect(tmp_sqlite_path)) as conn:
            configure_bulk_sqlite(conn)
            create_schema(conn)
            conn.executemany(
                "INSERT INTO metadata (key, value) VALUES (?, ?)",
                sorted(
                    {
                        "dataset": DATASET_NAME,
                        "dbsnp_build": "157",
                        "built_at_utc": built_at_utc,
                    }.items()
                ),
            )
            for shard_path in shard_paths:
                conn.execute("ATTACH DATABASE ? AS shard", (str(shard_path),))
                try:
                    cursor = conn.execute(
                        """
                    INSERT OR IGNORE INTO rsid_alleles
                    SELECT rsid, seqcol_digest, contig, pos0, ref, alt, source_vcf, allele_index
                    FROM shard.rsid_alleles
                    """
                    )
                    cursor.close()
                    conn.commit()
                finally:
                    conn.execute("DETACH DATABASE shard")
            create_lookup_index(conn)
            conn.execute("PRAGMA optimize")
            conn.commit()

        sqlite_bytes = tmp_sqlite_path.stat().st_size
        distinct_rsids = count_distinct_rsids(tmp_sqlite_path)
        retained_alleles = count_rows(tmp_sqlite_path)
        tmp_sqlite_path.replace(sqlite_path)

        per_assembly = _per_assembly_summary(split_summaries, shard_summaries)
        skipped: Counter[str] = Counter()
        input_rows = 0
        for summary in split_summaries:
            input_rows += int(summary.get("input_rows", 0))
            skipped.update({str(key): int(value) for key, value in dict(summary.get("skipped", {})).items()})
        duplicate_alleles = sum(int(summary.get("duplicate_alleles", 0)) for summary in shard_summaries)
        summary = {
            "dataset": DATASET_NAME,
            "dbsnp_build": 157,
            "built_at_utc": built_at_utc,
            "input_rows": input_rows,
            "retained_alleles": retained_alleles,
            "duplicate_alleles": duplicate_alleles,
            "skipped": dict(sorted(skipped.items())),
            "distinct_rsids": distinct_rsids,
            "per_assembly": per_assembly,
            "source_urls": {name: str(values.get("url", "")) for name, values in sorted(source_metadata.items())},
            "source_sha256": {name: str(values.get("sha256", "")) for name, values in sorted(source_metadata.items())},
            "sqlite_bytes": sqlite_bytes,
            "build_seconds": round(time.monotonic() - started, 3),
        }
        write_yaml_atomic(summary_path, tmp_summary_path, summary)
        if datapackage_path is not None:
            write_datapackage(datapackage_path, output_dir=output_dir)
        return summary
    except Exception:
        tmp_sqlite_path.unlink(missing_ok=True)
        tmp_summary_path.unlink(missing_ok=True)
        raise


def iter_vcf_allele_rows(
    *,
    path: Path,
    source_vcf: str,
    skipped: Counter[str],
    counts: Counter[str],
) -> Iterator[AlleleRow]:
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
            rsids = [part.lower() for part in id_text.split(";") if RSID_PATTERN.fullmatch(part.lower())]
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
                    yield (rsid, chrom, pos0, ref, alt, source_vcf, allele_index)


def ingest_vcf(
    *,
    conn: sqlite3.Connection,
    path: Path,
    source_vcf: str,
    seqcol_digest: str,
    skipped: Counter[str],
) -> Counter[str]:
    counts: Counter[str] = Counter()
    batch: list[tuple[str, str, str, int, str, str, str, int]] = []
    for rsid, chrom, pos0, ref, alt, row_source_vcf, allele_index in iter_vcf_allele_rows(
        path=path,
        source_vcf=source_vcf,
        skipped=skipped,
        counts=counts,
    ):
        batch.append((rsid, seqcol_digest, chrom, pos0, ref, alt, row_source_vcf, allele_index))
        if len(batch) >= BATCH_SIZE:
            flush_insert_batch(conn, batch, counts)
    flush_insert_batch(conn, batch, counts)
    return counts


def flush_insert_batch(
    conn: sqlite3.Connection,
    batch: list[tuple[str, str, str, int, str, str, str, int]],
    counts: Counter[str],
) -> None:
    if not batch:
        return
    before = conn.total_changes
    conn.executemany(
        """
        INSERT OR IGNORE INTO rsid_alleles
        (rsid, seqcol_digest, contig, pos0, ref, alt, source_vcf, allele_index)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        batch,
    )
    inserted = conn.total_changes - before
    counts["retained_alleles"] += inserted
    counts["duplicate_alleles"] += len(batch) - inserted
    batch.clear()


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
    if set(raw["resources"]) != set(EXPECTED_LOCK_RESOURCES):
        expected = ", ".join(EXPECTED_LOCK_RESOURCES)
        raise ValueError(f"{path}: lockfile must contain exactly these resources: {expected}")
    for filename in SOURCE_ASSEMBLIES:
        lock_resource(raw, filename, lockfile_path=path)
    return raw


def lock_resource(lock: dict[str, Any], filename: str, *, lockfile_path: Path | None = None) -> dict[str, Any]:
    entry = lock["resources"].get(filename)
    label = str(lockfile_path) if lockfile_path is not None else "lockfile"
    if not isinstance(entry, dict):
        raise ValueError(f"{label}: missing resource {filename!r}")
    for key in REQUIRED_LOCK_KEYS:
        if key not in entry:
            raise ValueError(f"{label}: resource {filename!r} missing {key}")
    if "/latest_release/" in str(entry["url"]).lower():
        raise ValueError(f"dbSNP latest_release URLs are mutable: {entry['url']}")
    expected = EXPECTED_LOCK_RESOURCES[filename]
    for key in ("url", "path", "md5_url", "md5_path"):
        if str(entry[key]) != expected[key]:
            raise ValueError(f"{label}: resource {filename!r} {key} must be {expected[key]!r}")
    if not MD5_PATTERN.fullmatch(str(entry["md5"])):
        raise ValueError(f"{label}: resource {filename!r} md5 must be a 32-character hex digest")
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
                registry_accession = spec["registry_accession"]
                if row["label"] == label and row["accession"] == registry_accession:
                    digest = row["seqcol_digest"].strip()
                    if not digest:
                        raise ValueError(f"{path}: blank seqcol_digest for {label}")
                    if label in by_label:
                        raise ValueError(f"{path}: duplicate registry row for {label} {registry_accession}")
                    by_label[label] = digest
    missing = sorted({spec["label"] for spec in SOURCE_ASSEMBLIES.values()} - set(by_label))
    if missing:
        raise ValueError(f"{path}: missing assembly registry rows for {', '.join(missing)}")
    return by_label


def count_distinct_rsids(sqlite_path: Path) -> int:
    with closing(sqlite3.connect(sqlite_path)) as conn:
        row = conn.execute("SELECT COUNT(DISTINCT rsid) FROM rsid_alleles").fetchone()
    return int(row[0])


def count_rows(sqlite_path: Path) -> int:
    with closing(sqlite3.connect(sqlite_path)) as conn:
        row = conn.execute("SELECT COUNT(*) FROM rsid_alleles").fetchone()
    return int(row[0])


def _read_yaml(path: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: expected YAML mapping")
    return raw


def _source_label(source_vcf: str) -> str:
    spec = SOURCE_ASSEMBLIES.get(source_vcf)
    if spec is None:
        return source_vcf
    return spec["label"]


def _per_assembly_summary(
    split_summaries: list[dict[str, Any]],
    shard_summaries: list[dict[str, Any]],
) -> dict[str, dict[str, int]]:
    per_assembly: dict[str, dict[str, int]] = {}
    for summary in split_summaries:
        label = _source_label(str(summary["source_vcf"]))
        per_assembly.setdefault(label, {"input_rows": 0, "retained_alleles": 0, "duplicate_alleles": 0})
        per_assembly[label]["input_rows"] += int(summary.get("input_rows", 0))
    for summary in shard_summaries:
        label = _source_label(str(summary["source_vcf"]))
        per_assembly.setdefault(label, {"input_rows": 0, "retained_alleles": 0, "duplicate_alleles": 0})
        per_assembly[label]["retained_alleles"] += int(summary.get("retained_alleles", 0))
        per_assembly[label]["duplicate_alleles"] += int(summary.get("duplicate_alleles", 0))
    return per_assembly


def source_metadata_from_lockfile(path: Path) -> dict[str, dict[str, str]]:
    lock = load_lockfile(path)
    return {
        name: {
            "url": str(entry["url"]),
            "sha256": str(entry["sha256"]),
        }
        for name, entry in lock["resources"].items()
    }


def seqcol_digest_for_source(source_vcf: str, assembly_registry_path: Path) -> str:
    spec = SOURCE_ASSEMBLIES[source_vcf]
    return load_assembly_digests(assembly_registry_path)[spec["label"]]


def write_marker(path: Path, summary: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"ok": True, "summary": summary}, sort_keys=False), encoding="utf-8")


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


def write_yaml_atomic(path: Path, tmp_path: Path, value: dict[str, Any]) -> None:
    try:
        tmp_path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
        tmp_path.replace(path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def stream_hash_and_bytes(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return f"sha256:{digest.hexdigest()}", byte_count


def resolve_commons_data_root() -> Path:
    try:
        from science_tool.commons.config import resolve_commons_data_root as resolve_science_commons_data_root
    except ImportError:
        resolve_science_commons_data_root = None
    if resolve_science_commons_data_root is not None:
        return resolve_science_commons_data_root()
    if env := os.environ.get("SCIENCE_COMMONS_DATA_ROOT"):
        return Path(env)
    return Path("/data/science-commons")


def default_assembly_registry_path(commons_data_root: Path) -> Path:
    return commons_data_root / "assembly-registry" / "assemblies.csv"


def _run_shard_command(argv: list[str]) -> bool:
    parser = argparse.ArgumentParser(description="Build dbSNP rsID shard artifacts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    split_parser = subparsers.add_parser("split-archive", help="Split one VCF archive into deterministic rsID row shards.")
    split_parser.add_argument("--archive", type=Path, required=True)
    split_parser.add_argument("--source-vcf", required=True)
    split_parser.add_argument("--output-dir", type=Path, required=True)
    split_parser.add_argument("--lockfile", type=Path)
    split_parser.add_argument("--marker", type=Path)
    split_parser.add_argument("--shard-count", type=int, default=SHARD_COUNT)

    shard_parser = subparsers.add_parser("build-shard", help="Build one shard SQLite from split rows.")
    shard_parser.add_argument("--rows", type=Path, required=True)
    shard_parser.add_argument("--sqlite", type=Path, required=True)
    shard_parser.add_argument("--summary", type=Path, required=True)
    shard_parser.add_argument("--source-vcf", required=True)
    shard_parser.add_argument("--shard-id", required=True)
    shard_parser.add_argument("--seqcol-digest")
    shard_parser.add_argument("--assembly-registry", type=Path)

    merge_parser = subparsers.add_parser("merge-shards", help="Merge shard SQLite files into the final dataset artifact.")
    merge_parser.add_argument("--shard-sqlite", type=Path, action="append", required=True)
    merge_parser.add_argument("--split-summary", type=Path, action="append", required=True)
    merge_parser.add_argument("--shard-summary", type=Path, action="append", required=True)
    merge_parser.add_argument("--output-dir", type=Path, required=True)
    merge_parser.add_argument("--lockfile", type=Path, required=True)
    merge_parser.add_argument("--datapackage", type=Path)
    merge_parser.add_argument("--update-datapackage", action="store_true")

    if not argv or argv[0] not in {"split-archive", "build-shard", "merge-shards"}:
        return False
    args = parser.parse_args(argv)
    if args.command == "split-archive":
        summary = split_archive_to_shards(
            archive_path=args.archive,
            source_vcf=args.source_vcf,
            output_dir=args.output_dir,
            shard_count=args.shard_count,
            lockfile_path=args.lockfile,
            marker_path=args.marker,
        )
        print(f"split {summary['emitted_alleles']} alleles from {args.source_vcf} into {args.output_dir}")
        return True
    if args.command == "build-shard":
        seqcol_digest = args.seqcol_digest
        if seqcol_digest is None:
            if args.assembly_registry is None:
                raise ValueError("--assembly-registry is required when --seqcol-digest is not provided")
            seqcol_digest = seqcol_digest_for_source(args.source_vcf, args.assembly_registry)
        summary = build_shard_sqlite(
            rows_path=args.rows,
            sqlite_path=args.sqlite,
            summary_path=args.summary,
            seqcol_digest=seqcol_digest,
            shard_id=args.shard_id,
            source_vcf=args.source_vcf,
        )
        print(f"built shard {args.source_vcf} {args.shard_id}: {summary['retained_alleles']} alleles")
        return True
    if args.command == "merge-shards":
        summary = merge_shard_sqlites(
            shard_paths=args.shard_sqlite,
            split_summary_paths=args.split_summary,
            shard_summary_paths=args.shard_summary,
            output_dir=args.output_dir,
            datapackage_path=args.datapackage if args.update_datapackage else None,
            source_metadata=source_metadata_from_lockfile(args.lockfile),
        )
        print(f"merged {summary['retained_alleles']} retained dbSNP alleles into {args.output_dir}")
        return True
    raise AssertionError(f"unhandled command: {args.command}")


def main() -> None:
    if _run_shard_command(sys.argv[1:]):
        return

    parser = argparse.ArgumentParser(description="Build dbSNP rsID to small-allele SQLite mappings.")
    parser.add_argument("--input-root", type=Path, help="Directory containing locked dbSNP .gz archives.")
    parser.add_argument("--output-root", type=Path, help="Commons output root. Dataset directory is created below it.")
    parser.add_argument("--dataset-output-dir", type=Path, help="Exact dataset output directory passed by science commons dataset build.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to recipe lockfile.")
    parser.add_argument(
        "--assembly-registry",
        type=Path,
        help="Path to assembly-registry assemblies.csv.",
    )
    parser.add_argument("--datapackage", type=Path, default=DATAPACKAGE_PATH, help="Path to datapackage.yaml.")
    parser.add_argument("--update-datapackage", action="store_true", help="Rewrite datapackage hashes and bytes.")
    args = parser.parse_args()

    commons_root = resolve_commons_data_root()
    input_root = args.input_root or commons_root / DATASET_NAME / "_src"
    output_root = args.output_root or commons_root
    effective_output_dir = args.dataset_output_dir or output_root / DATASET_NAME
    summary = build_dataset(
        input_root=input_root,
        output_root=output_root,
        dataset_output_dir=args.dataset_output_dir,
        lockfile_path=args.lockfile,
        assembly_registry_path=args.assembly_registry or default_assembly_registry_path(commons_root),
        datapackage_path=args.datapackage,
        update_datapackage=args.update_datapackage,
    )
    print(
        "wrote "
        f"{summary['retained_alleles']} retained dbSNP alleles "
        f"for {summary['distinct_rsids']} rsIDs to {effective_output_dir}"
    )


if __name__ == "__main__":
    main()
