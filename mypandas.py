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

def analyze(dataFilePath):
    data = pd.read_csv(
               dataFilePath, 
               delimiter ='\t',
               nrows=1000,
           )

    primaryAssemblyGenes = data[
        (data['group_label'] == 'GRCh38.p7-Primary Assembly') & 
        (data['feature_type'] == 'GENE')
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
            ].head(10)
    )

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage {cmd} file.cvs".format(cmd=sys.argv[0]))
        sys.exit(1)

    analyze(sys.argv[1])

