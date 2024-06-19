#!/usr/bin/env python3

import pandas as pd
from matplotlib_venn import venn2_unweighted
import matplotlib.pyplot as plt
import sys

## Example sys.argv inputs
# /home/davidvh/VanDenBoutLab/6767_variant_analysis/tumour_vcf/6767T_mutect2_filtered_PASS.vcf
# /home/davidvh/VanDenBoutLab/6767_variant_analysis/dbSNP_vcf/6767O_mutect2_filtered_PASS.vcf

# Define file paths 
germline_file= "/home/davidvh/VanDenBoutLab/6767_variant_analysis/germ_vcfs/bed-filtered/germ_snps_filtered_bed.vcf"
dbSNP_file= "/mnt/d/Downloads_D/dbSNP/dbSNP_db.recode.vcf"

# Read annotated variant list
# def read_variant_list(file):
#   df = pd.read_csv(file, sep="\t", header=None, engine="python", comment='#')
#   df.columns = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "sample1_germline"]
#   return df

### Declare dataframes for each
germline_df = pd.read_csv(germline_file, sep="\t", header=None, engine="python", comment='#')
germline_df.columns = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "sample1_germline"]

dbSNP_df = pd.read_csv(dbSNP_file, sep="\t", header=None, engine="python", comment='#')
dbSNP_df.columns = ["CHROM","POS","ID","REF","ALT","QUAL","FILTER"," INFO"]

## Make a venn diagram
def make_venn(germline_df, dbSNP_df):
    """
    Input 2 dataframes from a VCF file and generate a venn diagram.
    """

    # Create separate sets for germline and germline variations
    germline_set = set(zip(germline_df["CHROM"], germline_df["POS"], germline_df["REF"], germline_df["ALT"]))
    dbSNP_set = set(zip(dbSNP_df["CHROM"], dbSNP_df["POS"], dbSNP_df["REF"], dbSNP_df["ALT"])) 


    ## Calculate intersections and union
    common_variants = germline_set.intersection(dbSNP_set)
    unique_germline = germline_set.difference(dbSNP_set)
    unique_dbSNP = dbSNP_set.difference(germline_set)

    # Print only common variants
    print(f"Common variants: ", common_variants)

    # Print germline only
    # print(f"Somatic variants: ", unique_germline)

    # Print dbSNP only
    # print(f"Common variants: ", unique_dbSNP)
    exit()
    labels = {
              "Germline Only": len(unique_germline),
              "dbSNP Only": len(unique_dbSNP),
              "Both": len(common_variants)} #assert lables
    # Generate Venn diagram
    venn2_unweighted(subsets = (germline_set, dbSNP_set), set_labels= labels, set_colors=("orange", "blue"), alpha=0.3)
    plt.title("dbSNP variants present in 6767 germline SNPs")
    plt.show()
    exit()
    return common_variants
    
common_vars = make_venn(germline_df, dbSNP_df)

matching_variants = []

def extract_variants(df_orig, tuple_set):
    """
    Extract variants from a VCF based on an imported list and write to a new VCF

    Parameters:
    df_orig: Dataframe made from original VCF
    tuple_set: Set of tuples that contain variant positions
    """
    for tuple in tuple_set:
        matching_rows = df_orig[(df_orig['CHROM'] == tuple[0]) &
                           (df_orig['POS'] == tuple[1]) &
                           (df_orig['REF'] == tuple[2]) &
                           (df_orig['ALT'] == tuple[3])]

        matching_variants.extend(matching_rows.values.tolist())
    return matching_variants

df_tumour_bed_intersect = pd.DataFrame(extract_variants(germline_df, common_vars), columns=germline_df.columns)
df_dbSNP_bed_intersect = pd.DataFrame(extract_variants(dbSNP_df, common_vars), columns=dbSNP_df.columns)

print("new tumour file: ", df_tumour_bed_intersect)

df_tumour_bed_intersect.to_csv('df_tumour_new.vcf', sep='\t', index=False)
df_dbSNP_bed_intersect.to_csv('df_dbSNP_new.vcf', sep='\t', index=False)

# if __name__ == '__main__':
#     read_variant_list()
#     make_venn()
#     make_csv()
