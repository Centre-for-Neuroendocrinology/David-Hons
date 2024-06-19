#!/usr/bin/env Rscript

library(vcfR)
library(dplyr)

# open the file
vcf_file <- read.vcfR("~/VanDenBoutLab/clonal_subgrouping/6767SomaticAnnotatedPASS_BED_SNPs.vcf")
allele_freqs <- extract.gt(vcf_file, element = 'AF', as.numeric = TRUE)
print(allele_freqs[, 0])

# Create a distance matrix using Euclidean distance
distance_matrix <- dist(allele_freqs[, 1])
# print(distance_matrix)

# Perform hierarchical clustering based on Ward's method
cluster <- hclust(distance_matrix, method = "ward.D2")

# Cut the dendrogram trees
cut_height <- 0.1
clusters <- cutree(cluster, h = cut_height)

plot(cluster, 
xlim = c(0, 5000),
main = "Hierarchical clustering of SNPs based on Allele Frequency")
# dev.off()

