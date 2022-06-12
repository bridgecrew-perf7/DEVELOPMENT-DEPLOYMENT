import json
from collections import Counter
from itertools import combinations
from pathlib import Path

from tqdm import tqdm

from joblib import Parallel, delayed

def read_data(f):
    first_tweet_user = 1111155555555555555
    tweets = Path(f).read_text().split('\n')
    tweets = [t for t in tweets if t != '']
    if len(tweets) == 0:
        return
    tweets = [json.loads(t) for t in tweets]
    rt = [t['retweeted_status']['user']['screen_name'].lower() for t in tweets if 'retweeted_status' in t and t['id'] > first_tweet_user]
    return rt

rts = Parallel(n_jobs=8)(delayed(read_data)(f) for f in tqdm(list(Path('/mnt/data/datasets/twitter/tweets-maassen/').glob('*.json'))))

c = Counter()
for names in tqdm(rts):
    if names is None or 'user' not in names:
        continue
    c.update(set(names))

len(c.keys())

c.most_common(21)

import pandas as pd

df = pd.DataFrame([{'name': x[0], 'value': x[1] / c['user']} for x in c.most_common(101)[1:]])

df.to_csv('data.csv', )
