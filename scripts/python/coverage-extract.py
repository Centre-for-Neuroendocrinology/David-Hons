#!/usr/bin/env python3

from pysam import VariantFile
import sys

# ~/VanDenBoutLab/somatic_vcf-HTCaller/bed-filtered/6767O_snp_filtered_bed.vcf

input_vcf = sys.argv[1]

def coverage_extract(vcf):
    # Open the VCF file
    vcf_file =  VariantFile(filename=vcf, mode="r")

    # Filter variants based on coverage
    filtered_variants = [variant for variant in vcf_file if variant.info['DP'] >= 100]

    # Print the number of filtered variants
    print(f"Number of filtered variants: {len(filtered_variants)}")

    # (Optional) Write the filtered variants to a new VCF file
    with  VariantFile('filtered.vcf', 'w', header=vcf_file.header) as output_vcf:
        for variant in filtered_variants:
            output_vcf.write(variant)
coverage_extract(input_vcf)
