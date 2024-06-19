#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns

# Read the VCF file into a DataFrame
def read_vcf_to_dataframe(file_path):
    """
    Reads a VCF file into a pandas DataFrame.

    Parameters:
    file_path (str): Path to the VCF file

    Returns:
    DataFrame: A pandas DataFrame containing the VCF data
    """
    df = pd.read_csv(file_path, sep='\t', comment='#')
    return df

# Create a density plot from the DataFrame
def create_density_plot(df, column_name):
    """
    Creates a density plot from a given column in the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the VCF data
    column_name (str): The name of the column to plot
    """
    plt.figure(figsize=(10, 6))  # Set figure size
    plt.title(f'Density Plot of {column_name}')  # Set title
    plt.xlabel(column_name)  # Set x-axis label
    plt.ylabel('Density')  # Set y-axis label
    sns.kdeplot(data=df, x=column_name)  # Create the density plot
    plt.show()

# Example usage
file_path = sys.argv[1]
df = read_vcf_to_dataframe(file_path)

# Assuming you want to plot the density of a specific column, e.g., 'GT'
create_density_plot(df, 'AF')


