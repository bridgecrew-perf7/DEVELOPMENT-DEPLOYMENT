### IMPORT LIBRARIES ###

import gensim
from gensim.models import Word2Vec

input = open("/home/rechner/Desktop/IN.csv", "r")
data = input.read()

### CBOW ###

model1 = gensim.models.Word2Vec(data, min_count = 1, window = 5)

print(model1.n_similarity("modern", "world"))


### SKIP ###

model2 = gensim.models.Word2Vec(data, min_count = 1, window = 5, sg = 1)

print(model2.n_similarity("modern", "world"))
