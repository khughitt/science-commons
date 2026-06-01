# Open Targets Associations Commons Recipe

This recipe builds `dataset:opentargets-associations`, a `bio.reference_graph`
commons dataset: the first **association graph** in the reference-graph family
(after `dataset:mondo` and `dataset:go`).

Pinned source: **Open Targets Platform 25.12** (`25.12.0`, 2025-12-04, CC0 1.0).
Members are the participating targets (`ENSEMBL:ENSG…`) and diseases
(`EFO:…`/`MONDO:…`/…); edges are `subject=target, predicate=associated_with,
object=disease`, carrying the 0–1 overall score.

## Source files (pinned)

`lockfile.yaml` pins 31 immutable parquet files under
`https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/`:
the `target/` index (10 parts), the single `disease/disease.parquet`, and
`association_overall_direct/` (20 parts). `fetch.py` rejects any non-dated /
`latest/` / `master/` / `snapshot/` URL; the per-file sha256 + bytes are the
integrity backstop.

## edge_resource is omitted (design §8)

25.12 has 4,492,971 overall-direct associations (≫ the ~2 M threshold), so this
dataset is on the **omit-`edge_resource`** branch: the full edge set lives only
in the canonical `graph.jsonl` (`graph_format: jsonl_edges`, existence-checked by
`commons validate`). No `edges.csv` is written or registered. RG2 therefore
returns node-only payloads for this dataset (incident-association resolution is a
later increment). Because validate cannot count an omitted edge resource,
`build.py` self-verifies: `edge_count == graph.jsonl` line count, every endpoint
present in `nodes.csv`, and no orphan members.

The overall score lives only in `graph.jsonl` (the RG edge contract has no score
field). A scored query reads `graph.jsonl` directly.

## Operator rebuild flow

The recipe defaults use `resolve_commons_data_root()` (`/data/science-commons`
unless configured); the commands below pass `~/d/science-commons-data/opentargets-associations`
explicitly so the build lands in durable local storage.

```bash
cd ~/d/science
uv run --frozen --project science python ~/d/science-commons/datasets/opentargets-associations/recipe/fetch.py --output-dir ~/d/science-commons-data/opentargets-associations/_src
uv run --frozen --project science python ~/d/science-commons/datasets/opentargets-associations/recipe/build.py --source-dir ~/d/science-commons-data/opentargets-associations/_src --output-dir ~/d/science-commons-data/opentargets-associations --verify-entity ~/d/science-commons/datasets/opentargets-associations/entity.md
uv run --frozen --project science python ~/d/science-commons/datasets/opentargets-associations/recipe/build_datapackage.py --data-dir ~/d/science-commons-data/opentargets-associations
```
