import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from .. import candidate, party
from ..connection import db
from ..posts import twitter
from fetchers.twitter_api import get_latest_tweets_for_user
from orator import Model
from orator.orm import belongs_to, has_many

class TwitterAccount(Model):
    __table__ = "twitter_accounts"
    __fillable__ = ["candidate_id", "followers_count", "link", "party_id",
            "screen_name"]
    __guarded__ = ["id"]

    @belongs_to
    def candidate(self):
        return candidate.Candidate

    @belongs_to
    def party(self):
        return party.Party

    @has_many
    def posts(self):
        return twitter.TwitterPost

    def fetch_and_set_followers_count(self):
        tweets = get_latest_tweets_for_user(self.screen_name, count = 1)

        self.followers_count = tweets[0]["user"]["followers_count"]
        self.save()
