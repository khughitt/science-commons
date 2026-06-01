from __future__ import annotations

import argparse
import hashlib
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
    "mondo_release": "v2026-05-05",
    "release_page": "https://github.com/monarch-initiative/mondo/releases/tag/v2026-05-05",
    "files": {
        "mondo.json": {
            "url": "https://github.com/monarch-initiative/mondo/releases/download/v2026-05-05/mondo.json",
            "sha256": "sha256:4b6ece0b965528fadbd578b98ac95f268e833f18f1827ec58d380b2ac652e95d",
            "bytes": 103231823,
        }
    },
}


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
    return lock


def _reject_mutable_url(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        raise ValueError(f"MONDO source URL must be an https://github.com release asset, got {url!r}")
    if "/releases/latest/" in parsed.path or "/raw/" in parsed.path or "/refs/heads/" in parsed.path:
        raise ValueError(f"MONDO source URL is mutable; pin a release tag asset, got {url!r}")
    if "/releases/download/v" not in parsed.path:
        raise ValueError(f"MONDO source URL must use a versioned /releases/download/v.../ asset, got {url!r}")


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
    parser = argparse.ArgumentParser(description="Fetch pinned MONDO source artifacts.")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir or resolve_commons_data_root() / "mondo" / "_src"
    lock = fetch_sources(output_dir=output_dir)
    print(f"MONDO {lock['mondo_release']} sources verified in {output_dir}")


if __name__ == "__main__":
    main()
