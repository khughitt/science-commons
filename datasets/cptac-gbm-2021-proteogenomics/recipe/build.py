from __future__ import annotations

import argparse
import csv
import json
import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

DATASET_NAME = "cptac-gbm-2021-proteogenomics"
MRNA_FILE = "data_mrna_seq_fpkm.txt"
PROTEIN_FILE = "data_protein_quantification.txt"
KNOWN_NON_SAMPLE_COLUMNS = frozenset({"Entrez_Gene_Id"})


@dataclass(frozen=True)
class MatrixTable:
    feature_column: str
    sample_ids: list[str]
    rows: list[dict[str, Any]]
    skipped_blank_feature_rows: int


def resolve_output_dir(output_dir: str | Path | None, env: Mapping[str, str] | None = None) -> Path:
    if output_dir:
        return Path(output_dir)
    environ = env or os.environ
    data_root = environ.get("SCIENCE_COMMONS_DATA_ROOT")
    if data_root:
        return Path(data_root) / DATASET_NAME
    raise ValueError("--output-dir is required unless SCIENCE_COMMONS_DATA_ROOT is set")


def _parse_float(value: str, *, feature_id: str, sample_id: str) -> float | None:
    if value in {"", "NA", "NaN", "nan"}:
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"Invalid numeric value for {feature_id}/{sample_id}: {value!r}") from exc


def read_matrix(path: str | Path, *, feature_column: str) -> MatrixTable:
    source = Path(path)
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError(f"{source} is missing a header row")
        if feature_column not in reader.fieldnames:
            raise ValueError(f"{source} is missing feature column {feature_column}")
        sample_ids = [name for name in reader.fieldnames if name != feature_column and name not in KNOWN_NON_SAMPLE_COLUMNS]
        if not sample_ids:
            raise ValueError(f"{source} has no sample columns")
        rows: list[dict[str, Any]] = []
        skipped_blank_feature_rows = 0
        for raw in reader:
            feature_id = str(raw.get(feature_column) or "").strip()
            if not feature_id:
                skipped_blank_feature_rows += 1
                continue
            row: dict[str, Any] = {"feature_id": feature_id}
            for sample_id in sample_ids:
                row[sample_id] = _parse_float(str(raw.get(sample_id) or ""), feature_id=feature_id, sample_id=sample_id)
            rows.append(row)
    if not rows:
        raise ValueError(f"{source} contains no feature rows")
    return MatrixTable(
        feature_column=feature_column,
        sample_ids=sample_ids,
        rows=rows,
        skipped_blank_feature_rows=skipped_blank_feature_rows,
    )


def _protein_symbol(feature_id: str) -> str:
    return feature_id.split("|", 1)[0]


def validate_aligned_samples(mrna: MatrixTable, protein: MatrixTable) -> None:
    if mrna.sample_ids != protein.sample_ids:
        raise ValueError("mRNA/protein sample order mismatch")


def _matrix_to_long(table: MatrixTable, *, value_name: str, feature_transform=lambda value: value) -> pd.DataFrame:
    records: list[dict[str, Any]] = []
    for row in table.rows:
        feature_id = feature_transform(str(row["feature_id"]))
        for sample_id in table.sample_ids:
            records.append({"feature_id": feature_id, "sample_id": sample_id, value_name: row[sample_id]})
    return pd.DataFrame.from_records(records)


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_package(output_dir: str | Path) -> dict[str, Any]:
    out = Path(output_dir)
    validation_path = out / "reports" / "validation.json"
    download_summary_path = out / "reports" / "download-summary.json"
    if not validation_path.is_file():
        raise ValueError(f"Missing validation report: {validation_path}")
    if not download_summary_path.is_file():
        raise ValueError(f"Missing download summary: {download_summary_path}")

    mrna = read_matrix(out / "_src" / "datahub" / MRNA_FILE, feature_column="Hugo_Symbol")
    protein = read_matrix(out / "_src" / "datahub" / PROTEIN_FILE, feature_column="Composite.Element.REF")
    validate_aligned_samples(mrna, protein)

    expression = _matrix_to_long(mrna, value_name="mrna_fpkm_uq")
    proteomics = _matrix_to_long(protein, value_name="protein_abundance_log2", feature_transform=_protein_symbol)
    samples = pd.DataFrame({"sample_id": mrna.sample_ids})
    matched_features = sorted(set(expression["feature_id"]) & set(proteomics["feature_id"]))

    (out / "expression").mkdir(parents=True, exist_ok=True)
    (out / "proteomics").mkdir(parents=True, exist_ok=True)
    (out / "metadata").mkdir(parents=True, exist_ok=True)
    expression.to_parquet(out / "expression" / "mrna_fpkm_uq.parquet", index=False)
    proteomics.to_parquet(out / "proteomics" / "protein_abundance_log2.parquet", index=False)
    samples.to_parquet(out / "metadata" / "samples.parquet", index=False)

    summary = {
        "sample_rows": int(len(samples)),
        "mrna_feature_rows": int(len(mrna.rows)),
        "protein_feature_rows": int(len(protein.rows)),
        "matched_feature_rows": int(len(matched_features)),
        "sample_alignment": "identical-order",
        "skipped_blank_mrna_feature_rows": int(mrna.skipped_blank_feature_rows),
        "skipped_blank_protein_feature_rows": int(protein.skipped_blank_feature_rows),
        "resources": [
            "expression/mrna_fpkm_uq.parquet",
            "proteomics/protein_abundance_log2.parquet",
            "metadata/samples.parquet",
        ],
    }
    _write_json(out / "reports" / "build-summary.json", summary)
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build CPTAC GBM aligned mRNA/protein resources.")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args(argv)
    output_dir = resolve_output_dir(args.output_dir)
    summary = build_package(output_dir)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
