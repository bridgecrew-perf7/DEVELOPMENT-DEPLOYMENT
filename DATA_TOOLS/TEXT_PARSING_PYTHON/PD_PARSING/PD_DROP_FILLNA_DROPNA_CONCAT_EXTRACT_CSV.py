#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('CSV1.csv', delimiter=';')

df.drop('column_name', axis=1, inplace=True)
# df.drop(df.columns[[0]], axis=1, inplace=True)
# df.drop(df.columns[[0,2,5]], axis=1, inplace=True)

df.dropna(how = "any", axis=0, inplace=True)
# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# df.dropna(how = "any", axis=0, inplace=True)
# df.dropna(how = "any", axis=1, inplace=True)

df = df['SomeNA'].fillna('New Data', inplace=True)

# concat dataframes and select columns
df = pd.concat(df_list, sort=True, ignore_index=True)[["Col1", "Col2", "Col3"]]

df.to_csv('CSV3.csv')
