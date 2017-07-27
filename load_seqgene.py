#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys

seq_gene_md_src = 'data/seq_gene.md'
seq_gene_q_src = 'data/seq_gene.q'

repository = 'data/store.h5'


if __name__ == '__main__':

    store = pd.HDFStore('data/store.h5')

    print('store seq_gene.md to {dst}'.format(dst = repository))
    store['seq_gene_md'] = pd.read_csv(
            seq_gene_md_src, 
            sep='\t', 
            dtype={'chromosome' : str},
        )

    print('store seq_gene.q to {dst}'.format(dst = repository))
    store['seq_gene_q'] = pd.read_csv(
            seq_gene_q_src, 
            sep='\t',
        )

    store.close()

