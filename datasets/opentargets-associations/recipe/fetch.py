from __future__ import annotations

import argparse
import hashlib
import re
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.config import resolve_commons_data_root

# science:code
# status: exploratory
# science:end

_PLATFORM_PREFIX = "/pub/databases/opentargets/platform/"
_VERSION_RE = re.compile(r"^\d+\.\d+$")
_MUTABLE_SEGMENTS = frozenset({"latest", "master", "snapshot"})


def _load_lockfile() -> dict[str, Any]:
    lock_path = Path(__file__).with_name("lockfile.yaml")
    return yaml.safe_load(lock_path.read_text(encoding="utf-8"))


LOCKFILE = _load_lockfile()


def _reject_mutable_url(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        raise ValueError(f"Open Targets source URL must be https, got {url!r}")
    if parsed.netloc != "ftp.ebi.ac.uk":
        raise ValueError(f"Open Targets source URL must be on ftp.ebi.ac.uk, got {url!r}")
    if not parsed.path.startswith(_PLATFORM_PREFIX):
        raise ValueError(f"Open Targets source URL must be under {_PLATFORM_PREFIX!r}, got {url!r}")
    version = parsed.path[len(_PLATFORM_PREFIX):].split("/", 1)[0]
    if version in _MUTABLE_SEGMENTS or not _VERSION_RE.fullmatch(version):
        raise ValueError(
            "Open Targets source URL must pin a dated platform/<MAJOR.MINOR>/ release "
            f"(not latest/master/snapshot), got version segment {version!r} in {url!r}"
        )
    if "/output/" not in parsed.path or not parsed.path.endswith(".parquet"):
        raise ValueError(f"Open Targets source URL must be a .parquet under /output/, got {url!r}")


def fetch_sources(*, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    lock = LOCKFILE
    for rel_path, entry in lock["files"].items():
        url = str(entry["url"])
        _reject_mutable_url(url)
        path = output_dir / rel_path
        if not path.exists():
            _download(url, path)
        digest, byte_count = _hash_file(path)
        if digest != entry["sha256"] or byte_count != entry["bytes"]:
            raise ValueError(
                f"{path}: hash/bytes mismatch against lockfile "
                f"(got {digest}/{byte_count}, want {entry['sha256']}/{entry['bytes']})"
            )
    return lock


def _download(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    with urllib.request.urlopen(url) as response, tmp_path.open("wb") as fh:
        for chunk in iter(lambda: response.read(1024 * 1024), b""):
            fh.write(chunk)
    tmp_path.replace(output_path)


def _hash_file(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return f"sha256:{digest.hexdigest()}", byte_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch pinned Open Targets 25.12 source parquet.")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir or resolve_commons_data_root() / "opentargets-associations" / "_src"
    lock = fetch_sources(output_dir=output_dir)
    print(f"Open Targets {lock['release']} sources verified ({len(lock['files'])} files) in {output_dir}")


if __name__ == "__main__":
    main()
