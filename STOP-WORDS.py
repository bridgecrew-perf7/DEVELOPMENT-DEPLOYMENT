import numpy as np
import pandas as pd

import csv
import nltk

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

df = pd.read_csv('/home/mac/Desktop/PD-LA/PDTINKERTEXT.csv', header=None, engine='python')

tokenized_doc = df.apply(lambda x: x.split())

tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])

detokenized_doc = []
for i in range(len(df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

df = detokenized_doc

print(df)
