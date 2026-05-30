# Reactome Commons Recipe

This recipe builds the human Reactome pathway gene-set collection for commons.
Use an archived Reactome release URL. `download/current/` is discovery-only and
must not be used as `--base-url`.

```bash
cd ~/d/health/meta
rtk uv run --frozen python code/scripts/external/reactome/fetch.py --release <release> --base-url <archived-release-url>
rtk uv run --frozen python code/scripts/external/reactome/build.py
rtk uv run --frozen python code/scripts/external/reactome/build_datapackage.py
```

The fetch step writes source files and `lockfile.yaml` under
`$SCIENCE_COMMONS_DATA_ROOT/reactome/_src/`. Later runs can omit `--release` and
`--base-url`; the lockfile URLs and sha256 values are reused and verified.

The build step writes CSV resources and `build-summary.yaml` under
`$SCIENCE_COMMONS_DATA_ROOT/reactome/`. The D1 `sets.csv` member surface keeps
retained Entrez ids, while `gene_set_panel.csv` carries canonical C2 `gene_key`
and `symbol` columns for analysis.
