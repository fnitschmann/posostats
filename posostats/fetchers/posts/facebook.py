# -*- coding: utf-8 -*-
import os, sys, urllib

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from ..json_http_request import get_facebook_graph_api_response
from models.connection import db
from models.posts.facebook import FacebookPost
from utils.time import past_unix_timestamp_from_now

class FacebookPostsFetcher():
    """
    This class fetches all posts for a specific Facebook account page from a
    certain time period
    It either creates or updates them if they are present under the given post
    Faccebook ID
    """
    def __init__(self, account, since_days = 1):
        self.account = account
        self.since_days = since_days

    def api_posts_path(self):
        return "{}/posts".format(self.account.page_name)

    def api_posts_params(self):
        return {
                "limit": 100,
                "since": past_unix_timestamp_from_now(self.since_days)
                }

    def run(self):
        self.raw_api_response = get_facebook_graph_api_response(self.api_posts_path(),
                self.api_posts_params())
        self.data = self.raw_api_response["data"]

        self.__create_all_posts()

    def __create_all_posts(self):
        with db.transaction():
            for post in self.data:
                try:
                    self.__create_post(post)
                except Exception as e:
                    continue

    def __create_post(self, attributes = {}):
        facebook_account_id = self.account.id
        facebook_post_id = attributes["id"]

        post = FacebookPost.first_or_new(facebook_account_id =
                facebook_account_id, facebook_post_id = facebook_post_id)
        post.facebook_created_at = attributes["created_time"]

        self.__set_post_comments_count(post)
        self.__set_post_reactions_count(post)

        post.save()

    def __set_post_comments_count(self, post):
        path = "{}/comments".format(post.facebook_post_id)
        params = { "summary": 1 }
        api_response = get_facebook_graph_api_response(path, params)

        post.comments_count = api_response["summary"]["total_count"]

    def __set_post_reactions_count(self, post):
        path = "{}/reactions".format(post.facebook_post_id)
        params = { "summary": 1 }
        api_response = get_facebook_graph_api_response(path, params)

        post.reactions_count = api_response["summary"]["total_count"]
