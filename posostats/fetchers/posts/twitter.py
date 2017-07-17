# -*- coding: utf-8 -*-
import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from ..twitter_api import get_latest_tweets_for_user
from models.connection import db
from models.posts.twitter import TwitterPost

class TwitterPostsFetcher():
    """
    This class fetches all posts for a specific Twitter account page
    It either creates or updates them if they are present under the given post
    Twitter ID
    """
    def __init__(self, account, count = 10):
        self.account = account
        self.count = count

    def run(self):
        self.data = get_latest_tweets_for_user(self.account.screen_name, self.count)
        self.__create_all_posts()

    def __create_all_posts(self):
        with db.transaction():
            for post in self.data:
                try:
                    self.__create_post(post)
                except Exception as e:
                    continue

    def __create_post(self, attributes = {}):
        twitter_account_id = self.account.id
        twitter_post_id = "{}".format(attributes["id"])

        post = TwitterPost.first_or_new(twitter_account_id =
                twitter_account_id, twitter_post_id = twitter_post_id)

        post.twitter_created_at = attributes["created_at"]
        post.favorites_count = attributes["favorite_count"]
        post.retweets_count = attributes["retweet_count"]

        post.save()
