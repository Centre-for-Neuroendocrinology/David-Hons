#!/usr/bin/env python3

import csv

def dbSNP_scanner(dbSNP_file_path):
    """
    Generator function to scan through a GATK VCF file and yield lines where the dbSNP_ID column is not empty.
    
    Parameters:
    - dbSNP_file_path: Path to the VCF file
    
    Yields:
    A dictionary representing each line where the dbSNP_ID column is not empty.
    """
    with open(dbSNP_file_path, mode='r') as dbSNP_file:
        reader = csv.DictReader(dbSNP_file)
    
    for row in reader:
        yield {key: value for key, value in row.items()}

# Example usage
dbSNP_file_path = '/mnt/d/Downloads_D/dbsnp/dbSNP_db.recode.vcf'
dbSNP_scanner(dbSNP_file_path)
# Use dictionary generate from dbSNP VCF to scan through VCF

VCF_file 

for entry in dbSNP_scanner(dbSNP_file_path):
        
    for row in reader:
            # Check if the dbSNP_ID field is not empty
            if row['dbSNP_ID']:
                yield {key: value for key, value in row.items()}
    print(entry)

