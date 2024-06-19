#!/usr/bin/env Rscript

# Load required libraries
library(vcfR)

# Define VCF file path (replace with your actual file path)
vcf_file <- "your_vcf_file.vcf"

# Read VCF data
vcf <- read.vcf(vcf_file)

# Extract genotypes (assuming samples are in separate columns after first column)
genotypes <- vcf[, 2:ncol(vcf)]  # Get all columns except the first (header)

# Calculate allele frequencies (consider error handling for missing genotypes)
allele_freqs <- colMeans(geno[!is.na(geno)])  # Calculate mean per column (assuming biallelic SNPs)


# Create a heatmap using the "pheatmap" package (install if not available)
if (!requireNamespace("pheatmap")) install.packages("pheatmap")
library(pheatmap)

# Define the color gradient for the heatmap
heatmap <- pheatmap(allele_freqs, 
                    clustering_distance_rows = "euclidean",  # Row clustering distance metric
                    clustering_method_rows = "ward.D2",    # Row clustering method
                    show_colnames = TRUE,                   # Show column names
                    annotation = names(vcf)[2:ncol(vcf)],   # Use sample names as column annotations
                    main = "Allele Frequency Heatmap")        # Heatmap title

# Customize the heatmap plot (optional)
heatmap %>%
  theme_minimal() %>%
  scale_color_gradientn(palette = "YlOrRd")  # Adjust color palette as desired

