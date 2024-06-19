#!/usr/bin/env Rscript

setwd("~/VanDenBoutLab/SNP_PCA")
library("SNPRelate")
vcf.fn<-"~/VanDenBoutLab/SNP_PCA/6767T_snp_filtered_bed.vcf"
snpgdsVCF2GDS(vcf.fn, "ccm.gds",  method="biallelic.only")
genofile <- openfn.gds("ccm.gds")
ccm_pca<-snpgdsPCA(genofile)
plot(ccm_pca$eigenvect[,1],ccm_pca$eigenvect[,2] ,col=as.numeric(substr(ccm_pca$sample, 1,3) == 'CCM')+3, pch=2)
