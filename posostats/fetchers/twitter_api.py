import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from config.social_networks import TWITTER_CONSUMER_KEY as con_secret
from config.social_networks import TWITTER_CONSUMER_SECRET as con_secret_key
from config.social_networks import TWITTER_ACCESS_TOKEN as token
from config.social_networks import TWITTER_ACCESS_TOKEN_SECRET as token_key
from twitter import *

def twitter_api_client():
    return Twitter(auth = OAuth(token, token_key, con_secret, con_secret_key))

def get_latest_tweets_for_user(screen_name = "self", count = 10):
    return twitter_api_client().statuses.user_timeline(screen_name = screen_name, count = count)
