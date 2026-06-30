from __future__ import annotations

import hashlib
import urllib.request
from pathlib import Path
from typing import Any

import fetch


class _FakeResponse:
    def __init__(self, body: bytes, *, status: int = 200, headers: dict[str, str] | None = None) -> None:
        self._body = body
        self._offset = 0
        self.status = status
        self.headers = headers or {}

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, *_exc: object) -> None:
        return None

    def read(self, size: int = -1) -> bytes:
        if self._offset >= len(self._body):
            return b""
        if size < 0:
            size = len(self._body) - self._offset
        chunk = self._body[self._offset : self._offset + size]
        self._offset += len(chunk)
        return chunk


def _md5(value: bytes) -> str:
    return hashlib.md5(value).hexdigest()


def test_download_resumes_existing_temp_file(monkeypatch: Any, tmp_path: Path) -> None:
    output_path = tmp_path / "archive.gz"
    tmp_path_partial = output_path.with_suffix(output_path.suffix + ".tmp")
    tmp_path_partial.write_bytes(b"partial-")
    requests: list[urllib.request.Request] = []

    def fake_urlopen(request: urllib.request.Request) -> _FakeResponse:
        requests.append(request)
        assert request.get_header("Range") == "bytes=8-"
        return _FakeResponse(b"tail", status=206)

    monkeypatch.setattr(fetch.urllib.request, "urlopen", fake_urlopen)

    sha256, byte_count = fetch._download("https://example.test/archive.gz", output_path)

    assert output_path.read_bytes() == b"partial-tail"
    assert not tmp_path_partial.exists()
    assert byte_count == len(b"partial-tail")
    assert sha256 == "sha256:" + hashlib.sha256(b"partial-tail").hexdigest()
    assert len(requests) == 1


def test_download_promotes_complete_temp_file_after_range_416(monkeypatch: Any, tmp_path: Path) -> None:
    output_path = tmp_path / "archive.gz"
    tmp_path_complete = output_path.with_suffix(output_path.suffix + ".tmp")
    tmp_path_complete.write_bytes(b"complete")
    requests: list[urllib.request.Request] = []

    def fake_urlopen(request: urllib.request.Request) -> _FakeResponse:
        requests.append(request)
        if request.get_method() == "HEAD":
            return _FakeResponse(b"", headers={"Content-Length": "8"})
        raise fetch.urllib.error.HTTPError(request.full_url, 416, "Requested Range Not Satisfiable", {}, None)

    monkeypatch.setattr(fetch.urllib.request, "urlopen", fake_urlopen)

    sha256, byte_count = fetch._download("https://example.test/archive.gz", output_path)

    assert output_path.read_bytes() == b"complete"
    assert not tmp_path_complete.exists()
    assert byte_count == len(b"complete")
    assert sha256 == "sha256:" + hashlib.sha256(b"complete").hexdigest()
    assert [request.get_method() for request in requests] == ["GET", "HEAD"]


def test_refresh_lockfile_can_require_existing_sources(monkeypatch: Any, tmp_path: Path) -> None:
    archive_bytes = {
        "GCF_000001405.40.gz": b"grch38",
        "GCF_000001405.25.gz": b"grch37",
    }
    for name, content in archive_bytes.items():
        (tmp_path / name).write_bytes(content)
        (tmp_path / f"{name}.md5").write_text(f"{_md5(content)}  {name}\n", encoding="utf-8")

    def fail_download(url: str, output_path: Path) -> tuple[str, int]:
        raise AssertionError(f"unexpected download of {url} to {output_path}")

    monkeypatch.setattr(fetch, "_download", fail_download)

    lock = fetch.fetch_sources(
        output_dir=tmp_path,
        lockfile_path=tmp_path / "lockfile.yaml",
        refresh_lockfile=True,
        require_existing=True,
    )

    assert set(lock["resources"]) == {"GCF_000001405.40.gz", "GCF_000001405.25.gz"}
    for name, content in archive_bytes.items():
        entry = lock["resources"][name]
        assert entry["md5"] == _md5(content)
        assert entry["sha256"] == "sha256:" + hashlib.sha256(content).hexdigest()
        assert entry["bytes"] == len(content)
