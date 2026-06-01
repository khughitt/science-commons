# GO Commons Recipe

This recipe builds `dataset:go`, a `bio.reference_graph` commons dataset sourced
from the Gene Ontology.

The pinned source is GO release `2026-05-19`:

`https://release.geneontology.org/2026-05-19/ontology/go.json`

The production recipe uses the upstream OBO Graph JSON asset directly. The recipe
needs release-pinned, hash-verified bytes without introducing a ROBOT/JVM
conversion step, and GO already publishes OBO Graph JSON.

## Allowed vs. discovery-only URLs

Only a **dated** release asset may be pinned:

- `https://release.geneontology.org/<YYYY-MM-DD>/ontology/go.json`, or
- the equivalent PURL `https://purl.obolibrary.org/obo/go/releases/<YYYY-MM-DD>/go.json`

The undated `https://purl.obolibrary.org/obo/go.json`, and any URL containing
`current/`, `snapshot/`, or `latest/`, are **discovery-only** and must never be
pinned. `fetch.py` rejects them: the dated `YYYY-MM-DD` segment is mandatory, and
the lockfile sha256 plus a `graphs[0].meta.version` cross-check are the integrity
backstops.

## Operator rebuild flow

The recipe defaults use `resolve_commons_data_root()`, which is
`/data/science-commons` unless configured. The commands below pass
`~/d/science-commons-data/go` explicitly so the build lands in durable local
storage. Alternatively, set `SCIENCE_COMMONS_DATA_ROOT=~/d/science-commons-data`
before running the scripts without flags.

```bash
cd ~/d/science
uv run --frozen --project science python ~/d/science-commons/datasets/go/recipe/fetch.py --output-dir ~/d/science-commons-data/go/_src
uv run --frozen --project science python ~/d/science-commons/datasets/go/recipe/build.py --source-json ~/d/science-commons-data/go/_src/go.json --output-dir ~/d/science-commons-data/go
uv run --frozen --project science python ~/d/science-commons/datasets/go/recipe/build_datapackage.py --data-dir ~/d/science-commons-data/go
```

The node index includes active and deprecated GO terms. Deprecated terms remain
addressable members; replacement targets from `IAO:0100001` are recorded in
`nodes.csv.replaced_by` and are not auto-applied.

The edge table includes direct edges where either endpoint is a GO term plus node
xrefs as `predicate=xref`. Xrefs are relations, not identity rewrites.
