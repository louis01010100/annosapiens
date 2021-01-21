#!/bin/bash

CMD="
    python src/genome/gene.py
        --gene-file /affx/louis/tfs/genomes/human/genes/GCF_000001405.39_GRCh38.p13_feature_table.txt.gz
        --host localhost
        --port 5432
        --user louis
        --dbname hg
"

echo "$CMD"

eval $CMD
