#!/usr/bin/env python

import argparse
import csv
import sys
from pathlib import Path

import pandas as pd
import psycopg2

GENE_TABLE = 'gene'


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--gene-file', type=str, required=True)
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--user', type=str, required=True)
    parser.add_argument('--dbname', type=str, required=True)

    args = parser.parse_args()

    genes = load_genes(Path(args.gene_file)).rename(columns={
        'GeneID': 'gene_id',
        'end': 'stop'
    })

    genes = genes[[
        'gene_id',
        'symbol',
        'name',
        'chrom',
        'start',
        'stop',
        'strand',
        'class',
        'source',
    ]]

    conn = psycopg2.connect(
        host=args.host,
        port=args.port,
        user=args.user,
        dbname=args.dbname,
    )

    init_db(conn)

    to_db(genes, conn)


def init_db(conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute(f"DROP TABLE IF EXISTS {GENE_TABLE}")
            curs.execute(''
                         f'CREATE TABLE {GENE_TABLE} ('
                         f' gene_id text,'
                         f' symbol text,'
                         f' name text,'
                         f' chrom text,'
                         f' start integer,'
                         f' stop integer,'
                         f' strand char,'
                         f' class text,'
                         f' source text'
                         ')')


def to_db(genes, conn):

    statement = (
        ''
        f'INSERT INTO {GENE_TABLE} (gene_id, symbol, name, chrom, start, stop, strand, class, source)'
        f'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        '')

    try:
        with conn:
            for _, row in genes.iterrows():
                values = (
                    row['gene_id'],
                    row['symbol'],
                    row['name'],
                    row['chrom'],
                    row['start'],
                    row['stop'],
                    row['strand'],
                    row['class'],
                    row['source'],
                )

                with conn.cursor() as curs:
                    curs.execute(statement, values)

    finally:
        if conn:
            conn.close()


def load_genes(gene_file):

    filename = gene_file.name.strip('.txt.gz')

    genes = pd.read_csv(gene_file, header=0, sep='\t',
                        dtype=str).rename(columns={'# feature': 'feature'})

    genes = genes[lambda x: x['assembly_unit'] == 'Primary Assembly']

    genes = genes[lambda x: x['feature'] == 'gene']
    genes = genes[lambda x: x['chromosome'].notna()]
    genes.rename(columns={'chromosome': 'chrom'}, inplace=True)
    genes = genes.assign(source=filename)

    # nuclear_dna = genes[lambda x: x['chromosome'].str.contains('^\d+|X|Y$')]
    # mt_dna = genes[lambda x: x['chromosome'].str.contains('^MT$')]
    #
    # nuclear_dna['chrom'] = 'chr' + nuclear_dna['chromosome']
    # mt_dna['chrom'] = 'chrM'
    #
    # genes = pd.concat([nuclear_dna, mt_dna], sort=False, ignore_index=True)

    return genes


if __name__ == '__main__':
    main()
