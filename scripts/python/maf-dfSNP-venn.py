#!/usr/bin/env python3

import pandas as pd
from matplotlib_venn import venn2_unweighted
import matplotlib.pyplot as plt
import sys

# Read the MAF files
germline_file = "/home/davidvh/VanDenBoutLab/6767_variant_analysis/germ_vcfs/bed-filtered/germ_snps_filtered_bed.vcf"
db_SNP_file = "tumour_dbSNP.vcf"

# Extract the first column from both files
data1 = pd.read_csv(germline_file, sep='\t', header=None, comment='#')[1]
print("germline POS", data1)
data2 = pd.read_csv(db_SNP_file, sep='\t', header=None)[6].dropna().astype(str)
print("dbSNP pos", data2)

# Convert to sets
set1 = set(data1)
set2 = set(data2)

# Plot the Venn diagram
venn2_unweighted([set1, set2], ('Germline Variants', 'dbSNP Variants'), set_colors=("orange", "blue"), alpha=0.3)

# print(set2.intersection(set1))
# exit()

# Show the plot
plt.title("Venn Diagram of Germline vs dbSNP") 
plt.show()

