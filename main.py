import tweepy
import os
import time
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status('Twitterつぶやき投稿!!')

keyword = 'javascript'
tweet_count = 3
tweets = tweepy.Cursor(api.user_timeline, id="tm_3tomato111").items(tweet_count)

for tweet in tweets:
    if not 'RT @' in tweet.text[:4]:
        try:
            print('Tweet liked')
            tweet.favorite()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break