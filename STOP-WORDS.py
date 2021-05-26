import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import umap
import csv
import nltk
import sklearn

df = pd.read_csv('/home/mac/Desktop/PD-LA/PDTINKERTEXT.csv', header=None, engine='python')

df = df.str.replace("[^a-zA-Z#]", ";")

df = df.apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

df = df.apply(lambda x: x.lower())

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# tokenization
tokenized_doc = news_df['clean_doc'].apply(lambda x: x.split())

# remove stop-words
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])

# de-tokenization
detokenized_doc = []
for i in range(len(news_df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

news_df['clean_doc'] = detokenized_doc
