# Co-ocurrence, PPMI and PCA

import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix, dok_matrix
from scipy.sparse.linalg import svds
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

embd_n = 1001

idx2token = [x[0] for x in list(c.most_common(embd_n)) if x[0] != 'user']
token2idx = {k: v for v, k in enumerate(idx2token)}
n = len(idx2token)

xs, ys, data = [], [], []
for x in tqdm(rts):
    if x is None or 'user' not in x:
        continue
    s = set(x)
    s = [t for t in s if t in token2idx]
    for (c1, c2) in combinations(s, 2):
        c1 = token2idx[c1]
        c2 = token2idx[c2]
        xs.append(c1)
        xs.append(c2)
        ys.append(c2)
        ys.append(c1)
        data.append(1/len(s))
        data.append(1/len(s))

num_yes = 0
num_no = 0

for x in tqdm(rts):
    if x is None:
        continue
    if 'user' in x:
        num_yes += 1
    else:
        num_no +=1

num_no

num_yes

num_no / len(rts)

m = coo_matrix((data, (xs, ys)), (n, n), dtype=np.float32)

m = m.tocsr()

def calc_pmi(counts, cds):
    """
    Calculates e^PMI; PMI without the log().
    """

    sum_w = np.array(counts.sum(axis=1))[:, 0]
    sum_c = np.array(counts.sum(axis=0))[0, :]
    if cds != 1:
        sum_c = sum_c ** cds
    sum_total = sum_c.sum()
    sum_w = np.reciprocal(sum_w)
    sum_c = np.reciprocal(sum_c)

    pmi = csr_matrix(counts)
    pmi = multiply_by_rows(pmi, sum_w)
    pmi = multiply_by_columns(pmi, sum_c)
    pmi = pmi * sum_total
    return pmi

def multiply_by_rows(matrix, row_coefs):
    normalizer = dok_matrix((len(row_coefs), len(row_coefs)))
    normalizer.setdiag(row_coefs)
    return normalizer.tocsr().dot(matrix)


def multiply_by_columns(matrix, col_coefs):
    normalizer = dok_matrix((len(col_coefs), len(col_coefs)))
    normalizer.setdiag(col_coefs)
    return matrix.dot(normalizer.tocsr())

mm = calc_pmi(m, 0.75)

res = MinMaxScaler().fit_transform(mm.todense())

vis_n = 100

res_vis = res[:vis_n, :]

res_vis.shape

res_vis = PCA(n_components=2).fit_transform(res_vis)
res_vis = MinMaxScaler().fit_transform(res_vis)

from adjustText import adjust_text

from matplotlib import rcParams
rcParams['font.family'] = 'arial'

fig, ax = plt.subplots(figsize=(20, 20))

fig.patch.set_visible(False)
ax.axis('off')

sc = ax.scatter(res_vis[:, 0], res_vis[:, 1], color='black')

texts = [plt.text(res_vis[i][0] + 0.015 * 0, res_vis[i][1] - 0.009 * 0, idx2token[i], weight='regular', size='12') for i in range(vis_n)]
adjust_text(texts, weight='regular', size='12')

fig.savefig("200.svg")
