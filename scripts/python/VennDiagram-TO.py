#!/usr/bin/env python3

import pandas as pd
from matplotlib_venn import venn2_unweighted
import matplotlib.pyplot as plt
import sys

## Example sys.argv inputs
# /home/davidvh/VanDenBoutLab/6767_variant_analysis/tumour_vcf/6767T_mutect2_filtered_PASS_bed.vcf
# /home/davidvh/VanDenBoutLab/6767_variant_analysis/organoid_vcf/6767O_mutect2_filtered_PASS_bed.vcf

# Define file paths 
somatic_file: str = sys.argv[1]
organoid_file: str = sys.argv[2]

# Read annotated variant list
def read_variant_list(file):
  df = pd.read_csv(file, sep="\t", header=None, engine="python", comment='#')
  df.columns = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "sample1_germline", "sample1_tumour"]
  return df

### Declare dataframes for each
somatic_df = read_variant_list(somatic_file)
organoid_df = read_variant_list(organoid_file)

## Make a venn diagram
def make_venn(somatic_df, organoid_df):
    """
    Input 2 dataframes from a VCF file and generate a venn diagram.
    """

    # Create separate sets for germline and somatic variations
    somatic_set = set(zip(somatic_df["CHROM"], somatic_df["POS"], somatic_df["REF"], somatic_df["ALT"]))
    organoid_set = set(zip(organoid_df["CHROM"], organoid_df["POS"], organoid_df["REF"], organoid_df["ALT"])) 


    ## Calculate intersections and union
    common_variants = somatic_set.intersection(organoid_set)
    unique_somatic = somatic_set.difference(organoid_set)
    unique_organoid = organoid_set.difference(somatic_set)

    # Print only common variants
    print(f"Common variants: ", common_variants)

    # Print somatic only
    # print(f"Somatic variants: ", unique_somatic)

    # Print organoid only
    # print(f"Common variants: ", unique_organoid)
    exit()
    labels = {
              "Somatic Only": len(unique_somatic),
              "Organoid Only": len(unique_organoid),
              "Both": len(common_variants)} #assert lables
    # Generate Venn diagram
    venn2_unweighted(subsets = (somatic_set, organoid_set), set_labels= labels, set_colors=("orange", "blue"), alpha=0.3)
    plt.title("Tumour vs Organoid overlapping variants (Mutect2 tumour-normal)")
    # plt.savefig("tumour-organoid-mutect2Venn.png")
    plt.show()
    # exit()
    return common_variants
    
common_vars = make_venn(somatic_df, organoid_df)

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

df_tumour_bed_intersect = pd.DataFrame(extract_variants(somatic_df, common_vars), columns=somatic_df.columns)
df_organoid_bed_intersect = pd.DataFrame(extract_variants(organoid_df, common_vars), columns=organoid_df.columns)

print("new tumour file: ", df_tumour_bed_intersect)

df_tumour_bed_intersect.to_csv('df_tumour_new.vcf', sep='\t', index=False)
df_organoid_bed_intersect.to_csv('df_organoid_new.vcf', sep='\t', index=False)

# if __name__ == '__main__':
#     read_variant_list()
#     make_venn()
#     make_csv()
