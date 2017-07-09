#!/usr/bin/env python
import sys
from functools import reduce

AlleleID=0
Type=1
Name=2
GeneID=3
GeneSymbol=4
HGNC_ID=4
ClinicalSignificance=6
ClinSigSimple=7
LastEvaluated=8
RSID=9
nsv_esv=10
RCVaccession=11
PhenotypeIDS=12
PhenotypeList=13
Origin=14
OriginSimple=15
Assembly=16
ChromosomeAccession=17
Chromosome=18
Start=19
Stop=20
ReferenceAllele=21
AlternateAllele=22
Cytogenetic=23
ReviewStatus=24
NumberSubmitters=25
Guidelines=26
TestedInGTR=27
OtherIDs=28
SubmitterCategories=29



def handler():
    varTypes = dict()

    for line in sys.stdin:
        columns = line.strip('\n').split('\t')

        if columns[Type] in varTypes:
            value = varTypes[columns[Type]]
            value += 1
            varTypes[columns[Type]] = value
        else:
            varTypes[columns[Type]] = 1


    totalNumberOfRecords = reduce(lambda x, y: x + y, varTypes.values())


    for key, value in varTypes.items():

        print(
            "{varType}\t{count}\t{ratio:4.3f}".format(
                varType = key, 
                count = value, 
                ratio = (value/totalNumberOfRecords * 100)
            )
        )

    print("Total Number of Records: ", totalNumberOfRecords)



def main(): 
    try:
        handler()
    except KeyboardInterrupt:
        sys.exit()

main()
    

