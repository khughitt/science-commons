from __future__ import annotations

import gzip
import sqlite3
from pathlib import Path

import yaml

import build


def _write_vcf_gz(path: Path) -> None:
    with gzip.open(path, "wt", encoding="utf-8") as fh:
        fh.write("##fileformat=VCFv4.2\n")
        fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
        fh.write("1\t10\trs1\tA\tG\t.\t.\t.\n")
        fh.write("2\t20\trs2\tC\tT\t.\t.\t.\n")


def _write_datapackage(path: Path) -> None:
    path.write_text(
        yaml.safe_dump(
            {
                "name": "variant-labels-dbsnp-human",
                "profile": "data-package",
                "resources": [
                    {
                        "name": "rsid_mappings",
                        "path": "rsid_mappings.sqlite",
                        "format": "sqlite",
                        "mediatype": "application/vnd.sqlite3",
                        "source": {
                            "type": "local",
                            "ref": "${OUTPUT_ROOT}/variant-labels-dbsnp-human/rsid_mappings.sqlite",
                        },
                        "hash": "sha256:" + "0" * 64,
                        "bytes": 0,
                    },
                    {
                        "name": "build_summary",
                        "path": "build-summary.yaml",
                        "format": "yaml",
                        "mediatype": "application/x-yaml",
                        "source": {
                            "type": "local",
                            "ref": "${OUTPUT_ROOT}/variant-labels-dbsnp-human/build-summary.yaml",
                        },
                        "hash": "sha256:" + "0" * 64,
                        "bytes": 0,
                    },
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )


def test_split_archive_to_shards_reuses_complete_existing_split(tmp_path: Path) -> None:
    archive = tmp_path / "GCF_000001405.40.gz"
    _write_vcf_gz(archive)
    split_dir = tmp_path / "splits" / "GCF_000001405.40"

    first = build.split_archive_to_shards(
        archive_path=archive,
        source_vcf=archive.name,
        output_dir=split_dir,
        shard_count=4,
    )
    second = build.split_archive_to_shards(
        archive_path=archive,
        source_vcf=archive.name,
        output_dir=split_dir,
        shard_count=4,
    )

    assert first == second
    assert (split_dir / "shard-01.tsv.gz").is_file()
    assert (split_dir / "shard-02.tsv.gz").is_file()
    assert (split_dir / "split-summary.yaml").is_file()
    with gzip.open(split_dir / "shard-01.tsv.gz", "rt", encoding="utf-8") as fh:
        assert "rs1\t1\t9\tA\tG\tGCF_000001405.40.gz\t1\n" in fh.read()


def test_build_shards_and_merge_final_sqlite(tmp_path: Path) -> None:
    archive = tmp_path / "GCF_000001405.40.gz"
    _write_vcf_gz(archive)
    split_dir = tmp_path / "splits" / "GCF_000001405.40"
    build.split_archive_to_shards(
        archive_path=archive,
        source_vcf=archive.name,
        output_dir=split_dir,
        shard_count=4,
    )

    shard_paths: list[Path] = []
    shard_summary_paths: list[Path] = []
    for shard_id in ("00", "01", "02", "03"):
        shard_sqlite = tmp_path / "shards" / "GCF_000001405.40" / f"shard-{shard_id}.sqlite"
        shard_summary = shard_sqlite.with_suffix(".summary.yaml")
        build.build_shard_sqlite(
            rows_path=split_dir / f"shard-{shard_id}.tsv.gz",
            sqlite_path=shard_sqlite,
            summary_path=shard_summary,
            seqcol_digest="digest-grch38",
            shard_id=shard_id,
            source_vcf=archive.name,
        )
        shard_paths.append(shard_sqlite)
        shard_summary_paths.append(shard_summary)

    datapackage = tmp_path / "datapackage.yaml"
    _write_datapackage(datapackage)
    output_dir = tmp_path / "final"
    merged = build.merge_shard_sqlites(
        shard_paths=shard_paths,
        split_summary_paths=[split_dir / "split-summary.yaml"],
        shard_summary_paths=shard_summary_paths,
        output_dir=output_dir,
        datapackage_path=datapackage,
        source_metadata={archive.name: {"url": "https://example.test/archive.gz", "sha256": "sha256:" + "a" * 64}},
    )

    assert merged["retained_alleles"] == 2
    assert merged["distinct_rsids"] == 2
    assert (output_dir / "rsid_mappings.sqlite").is_file()
    assert (output_dir / "build-summary.yaml").is_file()
    with sqlite3.connect(output_dir / "rsid_mappings.sqlite") as conn:
        rows = conn.execute("SELECT rsid, seqcol_digest, contig, pos0, ref, alt FROM rsid_alleles ORDER BY rsid").fetchall()
    assert rows == [
        ("rs1", "digest-grch38", "1", 9, "A", "G"),
        ("rs2", "digest-grch38", "2", 19, "C", "T"),
    ]
    refreshed = yaml.safe_load(datapackage.read_text(encoding="utf-8"))
    assert refreshed["resources"][0]["bytes"] > 0
    assert refreshed["resources"][1]["bytes"] > 0


def test_snakefile_does_not_manage_tracked_datapackage_as_output() -> None:
    text = Path(__file__).with_name("Snakefile").read_text(encoding="utf-8")

    assert "datapackage=DATAPACKAGE" not in text
    assert "rule write_lockfile" not in text
    assert "output:\n        lockfile=LOCKFILE" not in text
