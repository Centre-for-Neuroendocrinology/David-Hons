#!/usr/bin/env Rscript

# Dependencies
req_packs = c("usethis","rmarkdown","Rcpp",
	"RcppArmadillo","devtools","BiocManager",
	"smarter")

for(pack in req_packs){
	
	chk_pack = tryCatch(find.package(pack),
		error = function(ee){NULL})
	
	if( !is.null(chk_pack) ){
		library(package = pack,character.only = TRUE)
		next
	}
	
	bb = NULL
	
	if( pack %in% "smarter" ){
		bb = tryCatch(install_github("pllittle/smarter",
			dependencies = TRUE),
			error = function(ee){"error"})
	} else {
		bb = tryCatch(install.packages(pkgs = pack,
			dependencies = TRUE),
			error = function(ee){"error"})
	}
	
	if( !is.null(bb) && bb == "error" )
		stop(sprintf("Error for package = %s",pack))
}
