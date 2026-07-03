# cytoband-hg19 recipe

This recipe pins UCSC hg19 `cytoBand.txt.gz` and builds a deterministic
`cytobands.csv` reference artifact for `dataset:cytoband-hg19`.

Source:

```text
https://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cytoBand.txt.gz
```

Use `cytoBand.txt.gz`, not `cytoBandIdeo.txt.gz`; the latter is modified for
ideogram display. Runtime Science readers consume only the built CSV through
the datapackage hash and never fetch UCSC.

```bash
python datasets/cytoband-hg19/recipe/fetch.py
python datasets/cytoband-hg19/recipe/build.py
```
