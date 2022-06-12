import nest_asyncio
import twint
from pathlib import Path
import twitter
import json


nest_asyncio.apply()
config = twint.Config()

config.Username = 'user'
c.Proxy_host = 'tor'
c.Store_csv = True
c.Output = 'followers.csv'

twint.run.Followers(c)

followers = Path('followers.csv').read_text().split()[1:]

api = twitter.Api(
    '', '', '', '', sleep_on_rate_limit=True)

def get_tweets(api=None, screen_name=None):

    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    if len(timeline) == 0:
        return []

    print(len(timeline))
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline

for f in followers:
    if Path(f'./INFILE{f}.json').is_file():
        continue

    print(f)
    try:
        timeline = get_tweets(api=api, screen_name=f)
        with open(f'./OUTFILE{f}.json', 'w+') as f:
            for tweet in timeline:
                f.write(json.dumps(tweet._json))
                f.write('\n')

    except Exception as e:
        print(e)
