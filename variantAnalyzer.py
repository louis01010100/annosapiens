#!/usr/bin/env python

import vcf
import sys

# NGS20140601A
def analyze(filename):
    vcf_reader = vcf.Reader(filename=filename)

    for record in vcf_reader:
        maf = {}
        for key, value in zip(record.ALT, map(lambda x: "{:7.5f}".format(x), record.aaf)):
            if key :
                maf[key.sequence] = value
            else :
                maf['.'] = value

        print("{}\t{}\t{}\t{}".format(record.CHROM, record.POS, record.REF, maf))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {cmd} foo.vcf'.format(cmd = sys.argv[0]))
        exit(1)
    filename = sys.argv[1]

    try: 
        analyze(filename)

    except KeyboardInterrupt:
        exit(1)
