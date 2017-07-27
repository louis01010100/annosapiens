#!/usr/bin/env python
import vcf
import sys

def analyze(filename):
    reader = vcf.Reader(filename = filename)

    for record in reader:

        for call in record.samples:
            if call.is_variant: 
                print("{chrom}\t{pos}\t{ref}\t{alt}\t{sample}\t{gt}".format(
                        chrom = record.CHROM,
                        pos = record.POS,
                        ref = record.REF,
                        alt = record.ALT,
                        sample = call.sample, 
                        gt = call.gt_bases
                    )
                )



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {cmd} foo.vcf".format(cmd = sys.argv[0]))
        exit(1)

    filename = sys.argv[1]

    try:
        analyze(filename)
    except KeyboardInterrupt:
        exit(1)

