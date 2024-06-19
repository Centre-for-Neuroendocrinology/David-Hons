#!/usr/bin/env Rscript

library(vcfR)
library(ggplot2)
library(dplyr)
library(tidyverse)

# PASS - BED filtered
tumour_file <- read.vcfR("/home/davidvh/VanDenBoutLab/6767_variant_analysis/tumour_vcf/6767T_mutect2_filtered_PASS_bed.vcf")
organoid_file <- read.vcfR("/home/davidvh/VanDenBoutLab/6767_variant_analysis/organoid_vcf/6767O_mutect2_filtered_PASS_bed.vcf")

# BED-filtered Intersect
# tumour_file <- read.vcfR("df_tumour_bed_intersect.vcf")
# organoid_file <- read.vcfR("df_organoid_bed_intersect.vcf")

# High coverage
# tumour_file <- read.vcfR("/home/davidvh/VanDenBoutLab/6767_variant_analysis/venn_diagrams/coverage-extract/6767T_HTC_snp_filtered_bed_cov100.vcf")
# organoid_file <- read.vcfR("/home/davidvh/VanDenBoutLab/6767_variant_analysis/venn_diagrams/coverage-extract/6767O_HTC_snp_filtered_bed_cov100.vcf")

# BED-filtered w/intersect
# tumour_file <- read.vcfR("/home/davidvh/VanDenBoutLab/6767_variant_analysis/tumour_vcf/6767T_mutect2_filtered_bed.vcf")
# organoid_file <- read.vcfR("/home/davidvh/VanDenBoutLab/6767_variant_analysis/organoid_vcf/6767O_mutect2_filtered_bed.vcf")

# Read VCF files
tumour_tidy <- vcfR2tidy(tumour_file)
organoid_tidy <- vcfR2tidy(organoid_file)

# Merge CHROM and POS columns into a single key
tumour_tidy$fix$key <- paste(tumour_tidy$fix$CHROM, tumour_tidy$fix$POS, tumour_tidy$fix$REF, tumour_tidy$fix$ALT)
organoid_tidy$fix$key <- paste(organoid_tidy$fix$CHROM, organoid_tidy$fix$POS, organoid_tidy$fix$REF, organoid_tidy$fix$ALT)

# Create a new dataframe containing only key, allele frequency, and sample name
tumour_all_af <- data.frame(tumour_tidy$fix$key, tumour_tidy$gt$gt_AF, tumour_tidy$gt$Indiv, tumour_tidy$gt$gt_DP)
colnames(tumour_all_af) <- c("key", "Tumour_AF", "sample", "coverage")
organoid_all_af <- data.frame(organoid_tidy$fix$key, organoid_tidy$gt$gt_AF, organoid_tidy$gt$Indiv, organoid_tidy$gt$gt_DP)
colnames(organoid_all_af) <- c("key", "Organoid_AF", "sample", "coverage")

# Filter by sample name (exclude germline)
tumour_af <- tumour_all_af %>%
	filter(sample == "Sample1_tumour")
organoid_af <- organoid_all_af %>%
	filter(sample == "Sample1_organoid")

# Merge data frames, remove NAs, and set AF to numeric
plot_data <- merge(tumour_af, organoid_af, by = "key")
plot_data <- na.omit(plot_data)
plot_data$Organoid_AF <- as.numeric(plot_data$Organoid_AF)
plot_data$Tumour_AF <- as.numeric(plot_data$Tumour_AF)

# Generate Density Plot
# png(filename="organoid-tumourAF-density.png")
ggplot(plot_data, aes(x = Organoid_AF, y = Tumour_AF)) +
  geom_point(alpha = 0.8) + 
  geom_density_2d_filled(show.legend=FALSE, alpha = 0.5) +
  xlim(0, 1) +
  ylim(0, 0.25) +
  theme_minimal() + # Optional: Use a minimal theme
  labs(title = "Density Scatterplot of Organoid vs Tumour Allele Frequency",
       x = "Organoid Allele Frequency",
       y = "Tumour Allele Frequency")
# dev.off()
