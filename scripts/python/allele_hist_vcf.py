#!/usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt

# ~/VanDenBoutLab/vcf/organoid_snp_variants.csv

def read_vcf(vcf):
    vcf = pd.read_csv(vcf, sep=",", header=None, engine="python", comment = "##", index_col=False)
    vcf = vcf.drop(index=0)
    # vcf.columns = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "sample1"]
    return vcf
vcf =read_vcf(sys.argv[1])

alleles = dict()
def make_histogram(df):
    for row in df.itertuples(index=True, name='Pandas'):
        try:
            win: str = row[3]+ ">" + row[4] # sets a moving window to check through sequence
            if (win not in alleles) and (len(win) <= 3):
                alleles[win] = 0 # initialize count to 0 if the key doesn't exist
            alleles[win] += 1 # increment count for the current window
        
        except Exception as e:
            print(f"Exception encountered {e}")

    # Build histogram
    keys = list(alleles.keys())
    values = list(alleles.values())
    plt.bar(range(len(keys)), values) # plot the histogram
    plt.title("Allele transition frequency")
    plt.xlabel("Allele transitions")
    plt.ylabel("Frequency")
    plt.xticks(range(len(keys)), keys, rotation='vertical') # set x-ticks to keys
    plt.show()
make_histogram(vcf)
