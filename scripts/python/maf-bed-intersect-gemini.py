#!/usr/bin/env python3

import pandas as pd
import sys
def main():
  """
  Scans a BED file and extracts matching rows from an annotated MAF file.

  Args:
      maf_file: Path to the annotated MAF file.
      bed_file: Path to the manifest BED file.
      output_file: Path to the output MAF file.
  """

  # Get input arguments
  maf_file, bed_file, output_file = sys.argv[1:]

  # Read MAF file into DataFrame
  maf_df = pd.read_csv(maf_file, sep='\t', comment = '#')  # Assuming tab-delimited MAF

  # Open BED and output files
  with open(bed_file, 'r') as bed, open(output_file, 'w') as out:
    # Write header from MAF file (assuming header is present in MAF)
    out.write(maf_df.to_csv(index=False, header=True))

    # Iterate over each line in BED file
    for line in bed:
      # Extract chromosome, start, and end positions
      chrom, start, end, gene = line.strip().split()

      # Filter MAF DataFrame for overlapping entries
      filtered_df = maf_df[(maf_df['Chromosome'] == chrom) &
                            (maf_df['Start_Position'] >= int(start)) &
                            (maf_df['Start_Position'] <= int(end))]

      # Write filtered entries to output (if any matches found)
      if not filtered_df.empty:
        out.write(filtered_df.to_csv(index=False, header=False))

  print(f"Matching MAF entries written to: {output_file}")

if __name__ == "__main__":
  main()
