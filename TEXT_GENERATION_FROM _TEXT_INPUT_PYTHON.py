import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import csv
import nltk
import sklearn
import sys
import PIL

csv.field_size_limit(sys.maxsize)
from nltk.corpus import stopwords
stop = stopwords.words('english')

pd.set_option("display.max_colwidth", 500)

#object with axes and series
df = pd.read_csv('/home/mac/Desktop/PD-LA/PDTEXT.csv', header=None, engine='python')

count = df[0].str.split(';', expand=True).stack().value_counts().plot(kind='bar')

plt.show()
