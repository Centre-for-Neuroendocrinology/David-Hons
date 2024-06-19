#!/usr/bin/env Rscript

library(gdsfmt)
library(SNPRelate)

# files
# ~/VanDenBoutLab/somatic_vcf-HTCaller/bed-filtered/6767T_snp_filtered_bed.vcf

# Convert VCF
vcf.fn <- "~/VanDenBoutLab/SNP_PCA/6767OFiltered.vcf"
snpgdsVCF2GDS(vcf.fn, "~/VanDenBoutLab/SNP_PCA/6767OFiltered.vcf", method="biallelic.only")
snpgdsSummary("~/VanDenBoutLab/SNP_PCA/6767O.gds")
# head("~/VanDenBoutLab/SNP_PCA/6767O.gds")

# SNP pruning
genofile <- snpgdsOpen("~/VanDenBoutLab/SNP_PCA/6767O.gds")
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.1)
str(snpset)
snpset.id <- unlist(unname(snpset))
head(snpset.id)

# PCA analysis
pca <- snpgdsPCA(genofile, snp.id=snpset.id)
head(pca)
tab <- data.frame(sample.id = pca$sample.id, # Determine variance proportion from data
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[1],    # the second eigenvector
    stringsAsFactors = FALSE)
head(tab)

# variance proportion (%)
pc.percent <- pca$varprop*100
head(round(pc.percent, 2))

# Draw
plot(tab$EV2, tab$EV1, xlab="eigenvector 2", ylab="eigenvector 1")

