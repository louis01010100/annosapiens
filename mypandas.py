#!/usr/bin/env python

# #tax_id
# 0  chromosome
# 1  chr_start
# 2  chr_stop
# 3  chr_orient
# 4  contig
# 5  ctg_start
# 6  ctg_stop
# 7  ctg_orient
# 8  feature_name
# 9  feature_id
# 10 feature_type
# 11 group_label
# 12 transcript
# 13 evidence_code

import pandas as pd
import sys

pd.set_option('display.width', 160) # default 80

def analyze(data):

    primaryAssemblyGenes = data[
        (data['group_label'] == 'GRCh38.p7-Primary Assembly') & 
        (data['feature_type'] == 'GENE') & 
        (data['chr_stop'] - data['chr_start'] < 100)
    ]

    print(
        primaryAssemblyGenes[ [
                    'chromosome', 
                    'chr_start', 
                    'chr_stop', 
                    'feature_name', 
                    'feature_type', 
                    'group_label', 
                ]
            ]
    )

# def load(rawFilePath):
#
#     return pd.read_csv(
#                rawFilePath, 
#                sep = '\t',
#                dtype = {'chromosome' : str},
#            )
#

def load(pickle):
    return pd.read_pickle(pickle)



seq_gene_md_dst = 'data/seq_gene_md.pickle'
seq_gene_q_dst = 'data/seq_gene_q.pickle'

def sql():

    store = pd.HDFStore('data/store.h5')

    seq_gene_md = store['seq_gene_md'] 
    seq_gene_q = store['seq_gene_q'] 

   primary_gene_md = seq_gene_md[
                (seq_gene_md['group_label'] == 'GRCh38.p7-Primary Assembly') & 
                (seq_gene_md['feature_type'] == 'GENE' )
            ][ 
                [ 
                    'chromosome', 
                    'chr_start', 
                    'chr_stop', 
                    'feature_id', 
                    'feature_name', 
                    'feature_type', 
                    'group_label',
                ] 
            ]

    primary_gene_q = seq_gene_q[
                [ 
                    '#feature_id', 
                    'feature_name', 
                    'alt_symbols', 
                    'description', 
                ] 
            ]

    target = primary_gene_md.merge(primary_gene_q, left_on = 'feature_id', right_on = '#feature_id')

    print(target.head(10))
    


    store.close();


if __name__ == '__main__':
    # sql()
    pd.test()
