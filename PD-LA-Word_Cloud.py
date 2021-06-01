import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud

import itertools
import umap
import csv
import nltk
import sklearn
import sys
import re
import PIL

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

csv.field_size_limit(sys.maxsize)

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

pd.set_option("display.max_colwidth", 500)

#all lowercase, only alphabetical characters, separator is ;
df = pd.read_csv('/home/mac/Desktop/PD-LA/PDTEXT.csv', header=None, engine='python')

wordcloud = WordCloud(max_words=80,margin=0).generate(df.iloc[0,0])
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
#image = wordcloud.to_image()
#image.show()
#image.save(name+'.bmp')