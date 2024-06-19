#!/usr/bin/env Rscript

library(maftools)

# laml.mcf <- system.file("6767OMutectFilteredAnnotated.maf", package = 'maftools')
laml <- read.maf(maf = "6767T_mutect2_filtered_ann.maf")
laml

plotmafSummary(maf = laml, rmOutlier = FALSE, addStat = 'mean', dashboard = TRUE, titvRaw = FALSE)

# plotVaf(maf = laml, vafCol = NULL)


