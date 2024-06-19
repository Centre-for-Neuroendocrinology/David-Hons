#!/usr/bin/env python3

import pandas as pd
from matplotlib_venn import venn2_unweighted
import matplotlib.pyplot as plt
import sys

# Read the MAF files
tumour_file = sys.argv[1]
organoid_file = sys.argv[2]

# Extract the first column from both files
data1 = pd.read_csv(tumour_file, sep=',', header=None, skiprows=2)[56].dropna().astype(str)
data2 = pd.read_csv(organoid_file, sep=',', header=None, skiprows=2)[56].dropna().astype(str)

# Convert to sets
set1 = set(data1)
set2 = set(data2)

# Plot the Venn diagram
venn2_unweighted([set1, set2], ('Tumour Variants', 'Organoid Variants'), set_colors=("orange", "blue"), alpha=0.3)

print(set2.intersection(set1))
exit()

# Show the plot
plt.title("Venn Diagram of Tumour vs Organoid COSMIC variants")
plt.show()

