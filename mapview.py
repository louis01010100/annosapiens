#!/usr/bin/env python

import sys

#  0  #tax_id
#  1  chromosome
#  2  chr_start
#  3  chr_stop
#  4  chr_orient
#  5  contig
#  6  ctg_start
#  7  ctg_stop
#  8  ctg_orient
#  9  feature_name
# 10  feature_id
# 11  feature_type
# 12  group_label
# 13  transcript
# 14  evidence_code


chromosome=1
chrStart=2
chrStop=3
geneSymbol=9
featureId=10
featureType=11
groupLabel=12

if __name__ == '__main__':
    if len(sys.argv) != 2: 
        print("Usage: {cmd} seq_gene.md".format(cmd=sys.argv[0]))
        sys.exit(1)
    try:
        with open(sys.argv[1], 'r') as reader:
            for row in reader:
                columns = row.strip('\n').split('\t')
                
                if columns[groupLabel] == 'GRCh38.p7-Primary Assembly':
                    if columns[featureType] == 'GENE':
                        length = (int)(columns[chrStop]) - (int)(columns[chrStart]) + 1
                        print("{chr}:{start}-{stop}\t{geneId}\t{geneSymbol}\t{length}".format(
                                chr=columns[chromosome],
                                start=columns[chrStart], 
                                stop=columns[chrStop],
                                geneId=columns[featureId],
                                geneSymbol=columns[geneSymbol],
                                length=length
                            )
                        )
    except KeyboardInterrupt:
        sys.exit(1)
