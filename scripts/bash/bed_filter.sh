#!/bin/bash

for i in ./*filtered.vcf; do
    shortName="${i:2:9}"
    # echo $shortName
    bedtools intersect -a "$i" \
    -b ./'Homo_sapiens_assembly_GRCh37_Gatk_latest_CancerScreen50 (1).bed' | grep PASS > \
    ./bed-filtered/"$shortName"_filtered_bed.vcf
 done
