import os, sys, threading

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from ..posts.facebook import FacebookPostsFetcher
from ..json_http_request import get_facebook_graph_api_response
from models.connection import db
from models.accounts.facebook import FacebookAccount
from urllib.error import HTTPError

class FacebookUpdater():
    """
    This class updates all existing Facebook Posts and the Likes count for the
    account pages
    """
    def __init__(self):
        self.accounts = FacebookAccount.all()

    def update_accounts_and_posts(self):
        with db.transaction():
            for account in self.accounts:
                t = threading.Thread(target = self.__update_account,
                        args=(account,))
                t.start()

            while(threading.active_count() > 1):
                continue

    def __update_account(self, account):
        account.fetch_and_set_likes_count()
        FacebookPostsFetcher(account = account).run()

        self.__update_posts_for_account(account)

    def __update_posts_for_account(self, account):
        for post in account.posts:
            try:
                post.comments_count = self.__update_post_comments_count(post)
                post.reactions_count = self.__update_post_reactions_count(post)
                post.save()
            except HTTPError as e:
                if e.code is 404:
                    post.delete()

                continue
            except Exception as e:
                continue

    def __update_post_comments_count(self, post):
        path = "{}/comments".format(post.facebook_post_id)
        params = { "summary": 1 }
        api_response = get_facebook_graph_api_response(path, params)

        return api_response["summary"]["total_count"]

    def __update_post_reactions_count(self, post):
        path = "{}/reactions".format(post.facebook_post_id)
        params = { "summary": 1 }
        api_response = get_facebook_graph_api_response(path, params)

        return api_response["summary"]["total_count"]

