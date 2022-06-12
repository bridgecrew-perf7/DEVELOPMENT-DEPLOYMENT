import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import csv
import sys
import PIL

csv.field_size_limit(sys.maxsize)

pd.set_option("display.max_colwidth", 600)


df = pd.read_csv("./IN.csv", header=None, engine='python', delimiter=None)


col = df[0].str.split(' ', expand=True).stack().value_counts(normalize=True)


col.plot(kind="bar")

plt.show()
