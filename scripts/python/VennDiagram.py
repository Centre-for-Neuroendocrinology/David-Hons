#!/usr/bin/env python3

import pandas as pd
from matplotlib_venn import venn3_unweighted
import matplotlib.pyplot as plt
import sys

## Example sys.argv inputs
#  /home/davidvh/VanDenBoutLab/6767_variant_analysis/germ_vcfs/3.germ_snps_indels/germ/6767_germ_snps_sorted_dedup.vcf /home/davidvh/VanDenBoutLab/6767_variant_analysis/germ_vcfs/3.germ_snps_indels/tumour/6767T_snps_indels_sorted_dedup.vcf /home/davidvh/VanDenBoutLab/6767_variant_analysis/germ_vcfs/3.germ_snps_indels/organoid/6767O_snp_indel_sorted_dedup.vcf

# Define file paths 
germline_file: str = sys.argv[1]
somatic_file: str = sys.argv[2]
organoid_file: str = sys.argv[3]

# Read annotated variant list
def read_variant_list(file):
  df = pd.read_csv(file, sep="\t", header=None, engine="python", comment='##')
  df.columns = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "sample1"]
  return df

### Declare dataframes for eac
germline_df = read_variant_list(germline_file)
somatic_df = read_variant_list(somatic_file)
organoid_df = read_variant_list(organoid_file)

## Make a venn diagram
def make_venn(germline_df, somatic_df, organoid_df):
    """
    Input 3 dataframes from the csv file and generate a venn diagram.
    """

    # Create separate sets for germline and somatic variations
    germline_set = set(zip(germline_df["CHROM"], germline_df["POS"], germline_df["REF"], germline_df["ALT"]))
    somatic_set = set(zip(somatic_df["CHROM"], somatic_df["POS"], somatic_df["REF"], somatic_df["ALT"]))
    organoid_set = set(zip(organoid_df["CHROM"], organoid_df["POS"], organoid_df["REF"], organoid_df["ALT"]))


    ## Calculate intersections and union
    common_variants = germline_set.intersection(somatic_set, organoid_set)
    unique_germline = germline_set.difference(somatic_set, organoid_set)
    unique_somatic = somatic_set.difference(germline_set, organoid_set)
    unique_organoid = organoid_set.difference(germline_set, somatic_set)
    # exit()
    labels = {"Germline Only": len(unique_germline),
              "Somatic Only": len(unique_somatic),
              "Organoid Only": len(unique_organoid),
              "Both": len(common_variants)} #assert lables
    # Generate Venn diagram
    venn3_unweighted(subsets = (germline_set, somatic_set, organoid_set), set_labels= labels, set_colors=("orange", "blue", "red"), alpha=0.3)
    plt.figure(1)
    plt.title("Intersection of HaplotypeCaller SNP/InDel Variants")
    plt.savefig("SNP-IndelVenn.png")
    plt.show()
    exit()
    return plt.show()
make_venn(germline_df, somatic_df, organoid_df)

# def make_csv(target_df):
#     target_df = pd.DataFrame(data = target_df)
#     # organoid_variants_df.columns = ("CHROM", 'POS',  "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "sample1")
#     target_df.to_csv(f"~/VanDenBoutLab/newSom.csv", index=False)
# make_csv(unique_organoid)

# if __name__ == '__main__':
#     read_variant_list()
#     make_venn()
#     make_csv()
