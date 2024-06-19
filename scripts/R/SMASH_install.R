#!/usr/bin/env Rscript

all_packs = as.character(installed.packages()[,1])
pandoc = Sys.getenv("RSTUDIO_PANDOC")
build_vign = !is.null(pandoc) && file.exists(pandoc)

if( !("smarter" %in% all_packs) ){
	stop("Check https://github.com/pllittle/smarter for installation")
}

library(smarter)
smarter::smart_packDeps(
	cran_packs = c("Rcpp","RcppArmadillo","devtools"),
	github_packs = c("Sun-lab/SMASH"),
	pandoc = pandoc,
	build_vign = build_vign)
