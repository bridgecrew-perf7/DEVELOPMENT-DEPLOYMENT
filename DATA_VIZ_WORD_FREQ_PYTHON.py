import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import csv
import nltk
import sklearn
import sys
import PIL

#nltk.download('stopwords')
csv.field_size_limit(sys.maxsize)

from nltk.corpus import stopwords
stop = stopwords.words('english')

pd.set_option("display.max_colwidth", 500)

df = pd.read_csv('/home/mac/Desktop/PANDAS-ML/IN.csv', header=None, engine='python')

series = df[0].str.split(';', expand=True).stack().value_counts(normalize=True)

series.plot(kind="bar")

#plt.show()
print(df)
print(series)
