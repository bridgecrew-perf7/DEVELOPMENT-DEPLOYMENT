#!/usr/bin/env python3

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_csv('File1.csv', delimiter=';')
df2 = pd.read_csv('File2.csv', delimiter=',')

# Merge the two dataframes
df3 = pd.merge(df1, df2, on='email')

# Write it to a new CSV file
df3.to_csv('merged.csv')
