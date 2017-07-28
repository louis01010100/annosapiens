#!/usr/bin/env python
import vcf
import sys

def analyze(filename):
    reader = vcf.Reader(filename = filename)

    for record in reader:
        for call in filter(lambda call : call.is_variant, record.samples):
            print("{chrom}\t{pos}\t{ref}\t{alt}\t{sample}\t{gt}".format(
                    chrom = record.CHROM,
                    pos = record.POS,
                    ref = record.REF,
                    alt = record.ALT,
                    sample = call.sample, 
                    gt = call.gt_bases,
                )
            )

def clinvar_to_bed(filename):
    reader = vcf.Reader(filename = filename)

    for record in reader:
        record.INFO['GENEINFO'].split('|')
        print("{chrom}\t{pos}\t{ref}\t{alt}\t{info}".format(
                chrom = record.CHROM,
                pos = record.POS,
                ref = record.REF,
                alt = record.ALT,
                info = record.INFO['GENEINFO'],
            )
        )



clinvar_file_path = 'data/clinvar.vcf.gz'
biobank_file_path = '../biobank/chrY.100k-merged.20170412.vcf.gz'


if __name__ == '__main__':
    try:
        #analyze(biobank_file_path)
        clinvar_to_bed(clinvar_file_path)
    except KeyboardInterrupt:
        exit(1)

