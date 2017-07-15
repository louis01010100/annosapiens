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

pd.set_option('display.width', 1280)

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

def load(rawFilePath):

    return pd.read_csv(
               rawFilePath, 
               sep = '\t',
               dtype = {'chromosome' : str},
           )

def loadPickled(pickle):
    return pd.read_pickle(pickle)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage {cmd} file.cvs".format(cmd=sys.argv[0]))
        sys.exit(1)

    # data = load(sys.argv[1])
    # data.to_pickle('data/seqgene_md.pickle')

    data = loadPickled(sys.argv[1])

    analyze(data)

