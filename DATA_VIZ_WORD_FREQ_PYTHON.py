import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import csv
import sys

csv.field_size_limit(sys.maxsize)

pd.set_option("display.max_colwidth", 500)

#get the 1-dim df
df = pd.read_csv('/home/mac/Desktop/PANDAS-ML/IN.csv', header=None, engine='python')

#split and count
col = df[0].str.split(';', expand=True).stack().value_counts(normalize=True)

col.plot(kind="bar")

plt.show()
#print(df)
