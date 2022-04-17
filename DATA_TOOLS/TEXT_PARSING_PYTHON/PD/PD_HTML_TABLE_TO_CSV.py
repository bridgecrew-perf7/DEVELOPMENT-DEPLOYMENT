#!/usr/bin/env python3

import pandas as pd

# linux bash cat to one file
# OPTIONAL get with html selenium driver page source / selenium-stealth

# infile
in_filename = './merged.html'

# get df list from html table parsing
df_list = pd.read_html(in_filename)

# concat entire list
df = pd.concat(df_list, sort=True, ignore_index=True)[["Col1", "Col2", "Col3"]].dropna(axis=0, how='all')

# save to file
df.to_csv('selected_cols.csv')
