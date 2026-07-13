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


def _write_shard_sqlite(path: Path, rsid_index: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        build.create_schema(conn)
        conn.execute(
            """
            INSERT INTO rsid_alleles
            (rsid, seqcol_digest, contig, pos0, ref, alt, source_vcf, allele_index)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                f"rs{rsid_index}",
                "digest-grch38",
                "1",
                rsid_index,
                "A",
                "G",
                "GCF_000001405.40.gz",
                1,
            ),
        )


def _write_yaml(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


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


def test_publish_sharded_dataset_writes_manifest_without_final_sqlite(tmp_path: Path) -> None:
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
        shard_sqlite = tmp_path / "_work" / "shards" / "GCF_000001405.40" / f"shard-{shard_id}.sqlite"
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
    output_dir = tmp_path
    summary = build.publish_sharded_dataset(
        shard_paths=shard_paths,
        split_summary_paths=[split_dir / "split-summary.yaml"],
        shard_summary_paths=shard_summary_paths,
        output_dir=output_dir,
        datapackage_path=datapackage,
        source_metadata={archive.name: {"url": "https://example.test/archive.gz", "sha256": "sha256:" + "a" * 64}},
    )

    manifest = yaml.safe_load((output_dir / "rsid-shards.yaml").read_text(encoding="utf-8"))
    refreshed = yaml.safe_load(datapackage.read_text(encoding="utf-8"))

    assert summary["retained_alleles"] == 2
    assert summary["shard_count"] == 4
    assert not (output_dir / "rsid_mappings.sqlite").exists()
    assert manifest["dataset"] == "variant-labels-dbsnp-human"
    assert manifest["shard_count"] == 4
    assert manifest["shards"][0]["path"].startswith("_work/shards/GCF_000001405.40/")
    assert refreshed["resources"][0]["name"] == "rsid_shards"
    assert refreshed["resources"][0]["path"] == "rsid-shards.yaml"
    assert refreshed["resources"][0]["bytes"] > 0
    assert refreshed["resources"][1]["bytes"] > 0


def test_merge_shard_sqlites_handles_more_than_sqlite_attach_limit(tmp_path: Path) -> None:
    split_summary = tmp_path / "splits" / "GCF_000001405.40" / "split-summary.yaml"
    _write_yaml(
        split_summary,
        {
            "source_vcf": "GCF_000001405.40.gz",
            "input_rows": 12,
            "skipped": {},
        },
    )

    shard_paths: list[Path] = []
    shard_summary_paths: list[Path] = []
    for index in range(12):
        shard_id = f"{index:02x}"
        shard_sqlite = tmp_path / "shards" / "GCF_000001405.40" / f"shard-{shard_id}.sqlite"
        shard_summary = shard_sqlite.with_suffix(".summary.yaml")
        _write_shard_sqlite(shard_sqlite, index + 1)
        _write_yaml(
            shard_summary,
            {
                "source_vcf": "GCF_000001405.40.gz",
                "shard_id": shard_id,
                "retained_alleles": 1,
                "duplicate_alleles": 0,
            },
        )
        shard_paths.append(shard_sqlite)
        shard_summary_paths.append(shard_summary)

    output_dir = tmp_path / "final"
    merged = build.merge_shard_sqlites(
        shard_paths=shard_paths,
        split_summary_paths=[split_summary],
        shard_summary_paths=shard_summary_paths,
        output_dir=output_dir,
    )

    assert merged["retained_alleles"] == 12
    assert merged["distinct_rsids"] == 12


def test_merge_shard_sqlites_resumes_recorded_temp_progress(tmp_path: Path) -> None:
    split_summary = tmp_path / "splits" / "GCF_000001405.40" / "split-summary.yaml"
    _write_yaml(
        split_summary,
        {
            "source_vcf": "GCF_000001405.40.gz",
            "input_rows": 2,
            "skipped": {},
        },
    )

    shard_paths: list[Path] = []
    shard_summary_paths: list[Path] = []
    for index in range(2):
        shard_id = f"{index:02x}"
        shard_sqlite = tmp_path / "shards" / "GCF_000001405.40" / f"shard-{shard_id}.sqlite"
        shard_summary = shard_sqlite.with_suffix(".summary.yaml")
        _write_shard_sqlite(shard_sqlite, index + 1)
        _write_yaml(
            shard_summary,
            {
                "source_vcf": "GCF_000001405.40.gz",
                "shard_id": shard_id,
                "retained_alleles": 1,
                "duplicate_alleles": 0,
            },
        )
        shard_paths.append(shard_sqlite)
        shard_summary_paths.append(shard_summary)

    output_dir = tmp_path / "final"
    output_dir.mkdir()
    temp_sqlite = output_dir / ".rsid_mappings.sqlite.merge.tmp"
    with sqlite3.connect(temp_sqlite) as conn:
        build.create_schema(conn)
        conn.execute(
            "INSERT INTO metadata (key, value) VALUES (?, ?)",
            ("dataset", "variant-labels-dbsnp-human"),
        )
        conn.execute(
            """
            INSERT INTO rsid_alleles
            (rsid, seqcol_digest, contig, pos0, ref, alt, source_vcf, allele_index)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("rs1", "digest-grch38", "1", 1, "A", "G", "GCF_000001405.40.gz", 1),
        )
    _write_yaml(
        output_dir / ".rsid_mappings.sqlite.merge-progress.yaml",
        {
            "version": 1,
            "completed_shards": [shard_paths[0].as_posix()],
        },
    )

    merged = build.merge_shard_sqlites(
        shard_paths=shard_paths,
        split_summary_paths=[split_summary],
        shard_summary_paths=shard_summary_paths,
        output_dir=output_dir,
    )

    assert merged["retained_alleles"] == 2
    assert merged["distinct_rsids"] == 2
    assert not temp_sqlite.exists()
    assert not (output_dir / ".rsid_mappings.sqlite.merge-progress.yaml").exists()


def test_load_assembly_digests_uses_current_registry_accessions(tmp_path: Path) -> None:
    registry = tmp_path / "assemblies.csv"
    registry.write_text(
        "\n".join(
            [
                "seqcol_digest,label,accession",
                "digest-grch37,GRCh37,GCA_000001405.14",
                "digest-grch38,GRCh38,GCA_000001405.15",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    assert build.load_assembly_digests(registry) == {
        "GRCh37": "digest-grch37",
        "GRCh38": "digest-grch38",
    }


def test_snakefile_does_not_manage_tracked_datapackage_as_output() -> None:
    text = Path(__file__).with_name("Snakefile").read_text(encoding="utf-8")

    assert "datapackage=DATAPACKAGE" not in text
    assert "rule write_lockfile" not in text
    assert "output:\n        lockfile=LOCKFILE" not in text
