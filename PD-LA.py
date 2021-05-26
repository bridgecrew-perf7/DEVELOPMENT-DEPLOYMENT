import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import umap
import csv
import nltk
import sklearn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

pd.set_option("display.max_colwidth", 200)

#all lowercase, only alphabetical characters, separator is;
df = pd.read_csv('/home/mac/Desktop/PD-LA/PDTINKERTEXT.csv', header=None, engine='python')
df = df[0].str.split(';', expand=True)
f = df.to_csv("Test.tab",sep=";", header=False, index=False)
df.to_csv("Test.tab",sep="\t",header=False,index=False)




print(df)
