#!/usr/bin/env python

import csv
import vcf

# "chr","pos","ref","alt","ac","clnsig","gene","diseases"


ANNOTATION_FILE = 'data/biobank_pathogenic.csv'
BIOBANK_FILE = 'data/grch37/clinvar.vcf.gz'

def to_string(record):
    return '{chrom}\t{pos}\t{ref}\t{alt}\t{ac}\t{clnsig}\t{gene}\t{diseases}'.format(
        chrom = chrom,
        pos = record['pos'],
        ref = record['ref'],
        alt = record['alt'],
        ac = record['ac'],
        clnsig = record['clnsig'],
        gene = record['gene'],
        diseases = record['diseases'],
    )


if __name__ == '__main__':

    vcf_reader = vcf.Reader(filename=BIOBANK_FILE)
    with open(ANNOTATION_FILE, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:

            chrom = row['chr'].replace('chr', '');

            # to zero-based, half-open interval
            start = int(row['pos']) - 1000
            end = start + len(row['ref']) + 1000

            print('{}\t{}\t{}'.format(row['chr'], start, end))

            # print(to_string(row))

            # for record in vcf_reader.fetch(chrom, start = start, end = end):
            #     print('{}\t{}'.format(record.POS, record.REF))




