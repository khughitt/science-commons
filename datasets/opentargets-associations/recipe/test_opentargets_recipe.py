from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from fetch import LOCKFILE, _reject_mutable_url


def test_lockfile_has_31_files():
    assert len(LOCKFILE["files"]) == 31
    assert LOCKFILE["release"] == "25.12"


def test_lockfile_yaml_matches_constant():
    lock_path = Path(__file__).with_name("lockfile.yaml")
    on_disk = yaml.safe_load(lock_path.read_text(encoding="utf-8"))
    assert on_disk["files"].keys() == LOCKFILE["files"].keys()
    assert on_disk["release"] == LOCKFILE["release"]


def test_reject_mutable_url_accepts_pinned_2512():
    _reject_mutable_url(
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/"
        "association_overall_direct/part-00000-aaa1c63d-a07c-4486-af49-f58da5ca71d5-c000.snappy.parquet"
    )


@pytest.mark.parametrize(
    "url",
    [
        "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/disease/disease.parquet",
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/disease/disease.parquet",
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/master/output/disease/disease.parquet",
        "https://example.com/25.12/output/disease/disease.parquet",
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/disease/disease.csv",
    ],
)
def test_reject_mutable_url_rejects(url):
    with pytest.raises(ValueError):
        _reject_mutable_url(url)
