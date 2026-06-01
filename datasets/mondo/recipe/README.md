# MONDO Commons Recipe

This recipe builds `dataset:mondo`, the first real `bio.reference_graph` commons dataset.

The pinned source is MONDO release `v2026-05-05`:

`https://github.com/monarch-initiative/mondo/releases/download/v2026-05-05/mondo.json`

The production recipe uses the upstream OBO Graph JSON asset directly. BioOntologies is not a production dependency in this pass because MONDO already publishes OBO Graph JSON and the recipe needs release-pinned, hash-verified bytes without introducing a ROBOT/JVM conversion step.

The recipe defaults use `resolve_commons_data_root()`, which is `/data/science-commons` unless configured. The commands below pass `~/d/science-commons-data/mondo` explicitly so the build lands in durable local storage. Alternatively, set `SCIENCE_COMMONS_DATA_ROOT=~/d/science-commons-data` before running the scripts without flags.

Run:

```bash
cd ~/d/science-commons/datasets/mondo
uv run --frozen --project ~/d/science/science python recipe/fetch.py --output-dir ~/d/science-commons-data/mondo/_src
uv run --frozen --project ~/d/science/science python recipe/build.py --source-json ~/d/science-commons-data/mondo/_src/mondo.json --output-dir ~/d/science-commons-data/mondo
uv run --frozen --project ~/d/science/science python recipe/build_datapackage.py --data-dir ~/d/science-commons-data/mondo --output-path datapackage.yaml
uv run --frozen --project ~/d/science/science python recipe/build.py --source-json ~/d/science-commons-data/mondo/_src/mondo.json --output-dir ~/d/science-commons-data/mondo --verify-entity entity.md
```

The node index includes active and deprecated MONDO terms. Deprecated terms remain addressable members; replacement targets from `IAO:0100001` are recorded in `nodes.csv.replaced_by` and are not auto-applied.

The edge table includes direct edges where either endpoint is a MONDO term plus node xrefs as `predicate=xref`. Xrefs are relations, not identity rewrites.
