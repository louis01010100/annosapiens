#!/usr/bin/env python
import vcf
import sys


def parse(filename):
    vcfReader = vcf.Reader(filename=filename)

    for record in vcfReader:
        print(record.genotype)
        




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {cmd} vcfFilePath ".format(cmd = sys.argv[0]))
        sys.exit(1)

    try:
        parse(sys.argv[1])
    except KeyboardInterrupt:
        sys.exit(1)


