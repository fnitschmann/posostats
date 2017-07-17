import os, sys, threading

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from ..posts.twitter import TwitterPostsFetcher
from ..twitter_api import twitter_api_client
from models.connection import db
from models.accounts.twitter import TwitterAccount
from urllib.error import HTTPError

class TwitterUpdater():
    """
    This class updates all existing Twitter Posts and the Likes count for the
    account pages
    """
    def __init__(self):
        self.accounts = TwitterAccount.all()

    def update_accounts_and_posts(self):
        with db.transaction():
            for account in self.accounts:
                t = threading.Thread(target = self.__update_account,
                        args=(account,))
                t.start()

            while(threading.active_count() > 1):
                continue

    def __update_account(self, account):
        account.fetch_and_set_followers_count()
        TwitterPostsFetcher(account = account).run()

        self.__update_posts_for_account(account)

    def __update_posts_for_account(self, account):
        for post in account.posts:
            try:
                api_data = twitter_api_client().statuses.show(_id =
                        post.twitter_post_id)

                post.favorites_count = api_data["favorite_count"]
                post.retweets_count = api_data["retweet_count"]
                post.save()
            except Exception as e:
                continue
