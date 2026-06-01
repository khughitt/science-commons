from __future__ import annotations

import argparse
import hashlib
import json
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

LOCKFILE = {
    "go_release": "2026-05-19",
    "release_archive": "https://release.geneontology.org/2026-05-19/",
    "files": {
        "go.json": {
            "url": "https://release.geneontology.org/2026-05-19/ontology/go.json",
            "sha256": "sha256:d901e4924cec804e0fbec209b88dd07547ca5503f81712c435200d3c9df7744b",
            "bytes": 82502353,
        }
    },
}

_RELEASE_PATH_RE = re.compile(r"^/\d{4}-\d{2}-\d{2}/ontology/go\.json$")
_PURL_PATH_RE = re.compile(r"^/obo/go/releases/\d{4}-\d{2}-\d{2}/go\.json$")


def fetch_sources(*, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    lock_path = Path(__file__).with_name("lockfile.yaml")
    if not lock_path.exists():
        lock_path.write_text(yaml.safe_dump(LOCKFILE, sort_keys=False), encoding="utf-8")
    lock = yaml.safe_load(lock_path.read_text(encoding="utf-8"))
    for filename, entry in lock["files"].items():
        url = str(entry["url"])
        _reject_mutable_url(url)
        path = output_dir / filename
        if not path.exists():
            _download(url, path)
        digest, byte_count = _hash_file(path)
        if digest != entry["sha256"] or byte_count != entry["bytes"]:
            raise ValueError(f"{path}: hash/bytes mismatch against lockfile")
        _verify_meta_version(path, str(lock["go_release"]))
    return lock


def _reject_mutable_url(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        raise ValueError(f"GO source URL must be https, got {url!r}")
    if parsed.netloc == "release.geneontology.org" and _RELEASE_PATH_RE.match(parsed.path):
        return
    if parsed.netloc == "purl.obolibrary.org" and _PURL_PATH_RE.match(parsed.path):
        return
    raise ValueError(
        "GO source URL must be a dated release.geneontology.org/<YYYY-MM-DD>/ontology/go.json "
        f"or purl.obolibrary.org/obo/go/releases/<YYYY-MM-DD>/go.json asset; "
        f"current/, snapshot/, latest/, and undated /obo/go.json are rejected, got {url!r}"
    )


def _verify_meta_version(path: Path, go_release: str) -> None:
    doc = json.loads(path.read_text(encoding="utf-8"))
    version = doc["graphs"][0]["meta"]["version"]
    if go_release not in str(version):
        raise ValueError(
            f"{path}: graphs[0].meta.version {version!r} does not contain pinned release {go_release!r}"
        )


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
    parser = argparse.ArgumentParser(description="Fetch pinned GO source artifacts.")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir or resolve_commons_data_root() / "go" / "_src"
    lock = fetch_sources(output_dir=output_dir)
    print(f"GO {lock['go_release']} sources verified in {output_dir}")


if __name__ == "__main__":
    main()
