# GRCh37 to GRCh38 assembly liftover recipe

This recipe pins the UCSC `hg19ToHg38.over.chain.gz` liftover chain and builds
a single `compatibility_relations.csv` resource linking explicit GRCh37 and
GRCh38 seqcol digests.

Fetch the pinned chain:

```bash
rtk python datasets/assembly-liftover-grch37-grch38/recipe/fetch.py
```

The default URL is:

```text
https://hgdownload.soe.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz
```

The fetch step writes the chain under
`$SCIENCE_COMMONS_DATA_ROOT/assembly-liftover-grch37-grch38/chains/` and writes
`recipe/lockfile.yaml` with the explicit URL, SHA-256 digest, and byte count.
URLs containing `latest`, `current`, or `download/test` are rejected.

Build the compatibility relation and update `datapackage.yaml`:

```bash
rtk python datasets/assembly-liftover-grch37-grch38/recipe/build.py \
  --source-seqcol <GRCh37 seqcol digest> \
  --target-seqcol <GRCh38 seqcol digest>
```

`build.py` fails if the lockfile is missing, the locked URL is not explicit, the
source and target seqcol digests are equal, or the pinned chain file is absent
from the dataset data directory.
