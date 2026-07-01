from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any
from urllib import request

import pandas as pd

GDC_API_BASE = "https://api.gdc.cancer.gov"
GDC_DATA_BASE = f"{GDC_API_BASE}/data"
DEFAULT_TIMEOUT_SECONDS = 60
PAGE_SIZE = 1000
PROJECT_ID = "MMRF-COMMPASS"

FILE_FIELDS = [
    "file_id",
    "file_name",
    "data_category",
    "data_type",
    "data_format",
    "experimental_strategy",
    "access",
    "file_size",
    "md5sum",
    "cases.case_id",
    "cases.submitter_id",
    "cases.samples.submitter_id",
    "cases.samples.sample_type",
]

CASE_FIELDS = [
    "case_id",
    "submitter_id",
    "diagnoses.days_to_recurrence",
    "diagnoses.progression_or_recurrence",
    "diagnoses.days_to_last_follow_up",
    "demographic.vital_status",
    "demographic.days_to_death",
]

PROGRESSION_EVENT_STATUSES = {"yes", "progression", "recurrence", "true", "1"}
PROGRESSION_CENSORED_STATUSES = {"no", "false", "0"}
SURVIVAL_FIELDS = ["vital_status", "days_to_death"]


def build_file_filter() -> dict[str, Any]:
    return {
        "op": "and",
        "content": [
            {"op": "in", "content": {"field": "cases.project.project_id", "value": [PROJECT_ID]}},
            {"op": "in", "content": {"field": "access", "value": ["open"]}},
            {"op": "in", "content": {"field": "data_type", "value": ["Gene Expression Quantification"]}},
            {"op": "in", "content": {"field": "experimental_strategy", "value": ["RNA-Seq"]}},
            {"op": "in", "content": {"field": "data_format", "value": ["TSV"]}},
        ],
    }


def _project_case_filter() -> dict[str, Any]:
    return {"op": "in", "content": {"field": "project.project_id", "value": [PROJECT_ID]}}


def _exactly_one(items: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(items, list) or len(items) != 1:
        raise ValueError(f"Expected exactly one linked {label}; found {0 if not isinstance(items, list) else len(items)}")
    item = items[0]
    if not isinstance(item, Mapping):
        raise ValueError(f"Expected linked {label} to be an object")
    return item


def normalize_file_hit(hit: Mapping[str, Any]) -> dict[str, Any]:
    case = _exactly_one(hit.get("cases"), "case")
    sample = _exactly_one(case.get("samples"), "sample")
    file_id = hit.get("file_id")
    if not file_id:
        raise ValueError("File hit is missing file_id")
    file_id = str(file_id)

    return {
        "file_id": file_id,
        "file_name": hit.get("file_name"),
        "data_category": hit.get("data_category"),
        "data_type": hit.get("data_type"),
        "data_format": hit.get("data_format"),
        "experimental_strategy": hit.get("experimental_strategy"),
        "access": hit.get("access"),
        "file_size": hit.get("file_size"),
        "md5sum": hit.get("md5sum"),
        "case_id": case.get("case_id") or case.get("id"),
        "case_submitter_id": case.get("submitter_id"),
        "sample_submitter_id": sample.get("submitter_id"),
        "sample_type": sample.get("sample_type"),
        "gdc_download_url": f"{GDC_DATA_BASE}/{file_id}",
    }


def validate_manifest_count(rows: Iterable[Mapping[str, Any]], expected_total: int) -> None:
    materialized = list(rows)
    file_ids = [row.get("file_id") for row in materialized]
    duplicates = sorted({file_id for file_id in file_ids if file_id and file_ids.count(file_id) > 1})
    if duplicates:
        raise ValueError(f"Manifest contains duplicate file_id values: {', '.join(map(str, duplicates))}")
    if len(materialized) != expected_total:
        raise ValueError(f"Normalized manifest count {len(materialized)} does not match independent manifest count {expected_total}")


def _one_diagnosis(case: Mapping[str, Any]) -> Mapping[str, Any]:
    diagnoses = case.get("diagnoses")
    if not isinstance(diagnoses, list) or len(diagnoses) != 1:
        case_id = case.get("case_id") or case.get("submitter_id") or "<unknown>"
        raise ValueError(f"Case {case_id} must have exactly one diagnosis for endpoint discovery")
    diagnosis = diagnoses[0]
    if not isinstance(diagnosis, Mapping):
        raise ValueError("Diagnosis must be an object")
    return diagnosis


def _flatten_case_endpoint_fields(case: Mapping[str, Any]) -> dict[str, Any]:
    diagnosis = _one_diagnosis(case)
    demographic = case.get("demographic") if isinstance(case.get("demographic"), Mapping) else {}
    flattened = {
        "case_id": case.get("case_id"),
        "case_submitter_id": case.get("submitter_id"),
        **dict(diagnosis),
    }
    for field in ("vital_status", "days_to_death"):
        flattened[field] = demographic.get(field)
    return flattened


def _has_value(value: Any) -> bool:
    return value is not None and value != ""


def _is_usable_progression_outcome(row: Mapping[str, Any]) -> bool:
    status = str(row.get("progression_or_recurrence") or "").strip().lower()
    if status in PROGRESSION_EVENT_STATUSES:
        return _has_value(row.get("days_to_recurrence"))
    if status in PROGRESSION_CENSORED_STATUSES:
        return _has_value(row.get("days_to_last_follow_up"))
    return False


def _progression_fields_for_usable_outcomes(flattened_cases: Iterable[Mapping[str, Any]]) -> list[str]:
    has_event_time = False
    has_usable_status = False
    for row in flattened_cases:
        status = str(row.get("progression_or_recurrence") or "").strip().lower()
        if status in PROGRESSION_EVENT_STATUSES and _has_value(row.get("days_to_recurrence")):
            has_event_time = True
            has_usable_status = True
        elif status in PROGRESSION_CENSORED_STATUSES and _has_value(row.get("days_to_last_follow_up")):
            has_usable_status = True

    fields: list[str] = []
    if has_event_time:
        fields.append("days_to_recurrence")
    if has_usable_status:
        fields.append("progression_or_recurrence")
    return fields


def discover_endpoint_fields(cases: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    flattened_cases = [_flatten_case_endpoint_fields(case) for case in cases]
    progression_fields = _progression_fields_for_usable_outcomes(flattened_cases)
    survival_fields = [field for field in SURVIVAL_FIELDS if any(_has_value(row.get(field)) for row in flattened_cases)]
    usable_progression_outcome_count = sum(1 for row in flattened_cases if _is_usable_progression_outcome(row))

    if usable_progression_outcome_count:
        status = "progression-ready"
    elif survival_fields:
        status = "survival-only"
    else:
        status = "missing-endpoint"

    return {
        "status": status,
        "progression_fields": progression_fields,
        "survival_fields": survival_fields,
        "usable_progression_outcome_count": usable_progression_outcome_count,
        "flattened_cases": flattened_cases,
    }


class LiveGdcClient:
    def __init__(self, api_base: str = GDC_API_BASE, timeout: int = DEFAULT_TIMEOUT_SECONDS, page_size: int = PAGE_SIZE) -> None:
        self.api_base = api_base.rstrip("/")
        self.timeout = timeout
        self.page_size = page_size

    def get_status(self) -> dict[str, Any]:
        return self._get_json(f"{self.api_base}/status")

    def count_files(self, file_filter: Mapping[str, Any]) -> int:
        payload = self._post_json(
            f"{self.api_base}/files",
            {
                "filters": file_filter,
                "fields": "file_id",
                "format": "JSON",
                "size": 0,
            },
        )
        return int(payload["data"]["pagination"]["total"])

    def iter_files(self, file_filter: Mapping[str, Any]) -> Iterable[dict[str, Any]]:
        yield from self._iter_endpoint(
            "files",
            filters=file_filter,
            fields=FILE_FIELDS,
            expand=None,
        )

    def iter_cases(self) -> Iterable[dict[str, Any]]:
        yield from self._iter_endpoint(
            "cases",
            filters=_project_case_filter(),
            fields=CASE_FIELDS,
            expand=["diagnoses", "demographic"],
        )

    def _iter_endpoint(
        self,
        endpoint: str,
        *,
        filters: Mapping[str, Any],
        fields: list[str],
        expand: list[str] | None,
    ) -> Iterable[dict[str, Any]]:
        offset = 0
        while True:
            payload: dict[str, Any] = {
                "filters": filters,
                "fields": ",".join(fields),
                "format": "JSON",
                "size": self.page_size,
                "from": offset,
            }
            if expand:
                payload["expand"] = ",".join(expand)
            page = self._post_json(f"{self.api_base}/{endpoint}", payload)
            data = page["data"]
            hits = data.get("hits", [])
            pagination = data["pagination"]
            page_count = int(pagination["count"])
            total = int(pagination["total"])
            if not hits and offset < total:
                raise ValueError(f"GDC returned empty {endpoint} page before total was reached")
            yield from hits
            offset += page_count
            if offset >= total:
                break

    def _get_json(self, url: str) -> dict[str, Any]:
        with request.urlopen(url, timeout=self.timeout) as response:
            return json.loads(response.read().decode("utf-8"))

    def _post_json(self, url: str, payload: Mapping[str, Any]) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        req = request.Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
        with request.urlopen(req, timeout=self.timeout) as response:
            return json.loads(response.read().decode("utf-8"))


class StaticGdcClient:
    def __init__(
        self,
        *,
        status_payload: Mapping[str, Any],
        file_total: int,
        file_pages: list[Mapping[str, Any]],
        case_pages: list[Mapping[str, Any]],
    ) -> None:
        self.status_payload = dict(status_payload)
        self.file_total = file_total
        self.file_pages = file_pages
        self.case_pages = case_pages

    def get_status(self) -> dict[str, Any]:
        return self.status_payload

    def count_files(self, file_filter: Mapping[str, Any]) -> int:
        _ = file_filter
        return self.file_total

    def iter_files(self, file_filter: Mapping[str, Any]) -> Iterable[dict[str, Any]]:
        _ = file_filter
        for page in self.file_pages:
            yield from page["data"]["hits"]

    def iter_cases(self) -> Iterable[dict[str, Any]]:
        for page in self.case_pages:
            yield from page["data"]["hits"]


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_dry_run(output_dir: str | Path, client: LiveGdcClient | StaticGdcClient | None = None) -> dict[str, Any]:
    out = Path(output_dir)
    manifest_dir = out / "manifest"
    reports_dir = out / "reports"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    gdc_client = client or LiveGdcClient()
    file_filter = build_file_filter()
    status_payload = gdc_client.get_status()
    file_rows = [normalize_file_hit(hit) for hit in gdc_client.iter_files(file_filter)]
    independent_file_total = gdc_client.count_files(file_filter)
    validate_manifest_count(file_rows, expected_total=independent_file_total)
    cases = list(gdc_client.iter_cases())
    manifest_case_ids = {row["case_id"] for row in file_rows}
    manifest_cases = [case for case in cases if case.get("case_id") in manifest_case_ids]
    missing_case_ids = sorted(manifest_case_ids - {case.get("case_id") for case in manifest_cases})
    endpoint_report = discover_endpoint_fields(manifest_cases)

    pd.DataFrame(file_rows).to_parquet(manifest_dir / "files.parquet", index=False)
    _write_json(manifest_dir / "cases.json", cases)
    _write_json(manifest_dir / "query.json", file_filter)

    promotable = endpoint_report["status"] == "progression-ready" and not missing_case_ids
    validation = {
        "file_filter": file_filter,
        "file_count": len(file_rows),
        "independent_file_total": independent_file_total,
        "case_count": len(manifest_cases),
        "project_case_count": len(cases),
        "missing_manifest_case_ids": missing_case_ids,
        "endpoint_status": endpoint_report["status"],
        "progression_fields": endpoint_report["progression_fields"],
        "survival_fields": endpoint_report["survival_fields"],
        "usable_progression_outcome_count": endpoint_report["usable_progression_outcome_count"],
        "gdc_data_release": status_payload.get("data_release"),
        "gdc_status": status_payload,
        "promotable": promotable,
    }
    _write_json(reports_dir / "validation.json", validation)

    if missing_case_ids:
        raise ValueError(f"GDC case query is missing manifest cases: {', '.join(missing_case_ids)}")
    if endpoint_report["status"] == "survival-only":
        raise ValueError("GDC cases expose only overall-survival endpoints; progression endpoint is required")
    if endpoint_report["status"] == "missing-endpoint":
        raise ValueError("GDC cases are missing a usable progression endpoint")

    return {
        "endpoint_status": endpoint_report["status"],
        "file_count": len(file_rows),
        "case_count": len(manifest_cases),
        "promotable": promotable,
        "validation_path": str(reports_dir / "validation.json"),
    }


def _iter_manifest_rows(manifest_rows: Iterable[Mapping[str, Any]] | pd.DataFrame) -> Iterable[Mapping[str, Any]]:
    if isinstance(manifest_rows, pd.DataFrame):
        yield from manifest_rows.to_dict(orient="records")
    else:
        yield from manifest_rows


def download_expression_files(
    manifest_rows: Iterable[Mapping[str, Any]] | pd.DataFrame,
    output_dir: str | Path,
    *,
    timeout: int = DEFAULT_TIMEOUT_SECONDS,
) -> list[Path]:
    expression_dir = Path(output_dir) / "expression"
    expression_dir.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []

    for row in _iter_manifest_rows(manifest_rows):
        file_id = str(row.get("file_id") or "")
        url = str(row.get("gdc_download_url") or "")
        if not file_id or not url:
            raise ValueError("Manifest row must include file_id and gdc_download_url")
        target = expression_dir / f"{file_id}.tsv"
        expected_md5 = row.get("md5sum")
        expected_size = row.get("file_size")

        hasher = hashlib.md5()
        total_bytes = 0
        with request.urlopen(url, timeout=timeout) as response, target.open("wb") as handle:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                total_bytes += len(chunk)
                hasher.update(chunk)
                handle.write(chunk)

        if expected_size is not None and int(expected_size) != total_bytes:
            raise ValueError(f"Downloaded size mismatch for {file_id}: expected {expected_size}, got {total_bytes}")
        if expected_md5 and str(expected_md5).lower() != hasher.hexdigest():
            raise ValueError(f"Downloaded md5 mismatch for {file_id}")
        downloaded.append(target)

    return downloaded


def resolve_output_dir(output_dir: str | Path | None, env: Mapping[str, str] | None = None) -> Path:
    if output_dir:
        return Path(output_dir)
    environ = env or os.environ
    data_root = environ.get("SCIENCE_COMMONS_DATA_ROOT")
    if data_root:
        return Path(data_root) / "mmrf-commpass"
    raise ValueError("--output-dir is required unless SCIENCE_COMMONS_DATA_ROOT is set")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dry-run the MMRF-COMMPASS GDC manifest query.")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--download-expression", action="store_true")
    args = parser.parse_args(argv)

    output_dir = resolve_output_dir(args.output_dir)
    report = write_dry_run(output_dir)
    if args.download_expression:
        manifest = pd.read_parquet(output_dir / "manifest" / "files.parquet")
        download_expression_files(manifest, output_dir)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
