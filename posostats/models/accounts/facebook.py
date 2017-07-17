import os, sys, threading

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from .. import candidate, party
from ..connection import db
from ..posts import facebook
from fetchers.json_http_request import get_facebook_graph_api_response
from orator import Model
from orator.orm import belongs_to, has_many

class FacebookAccount(Model):
    __table__ = "facebook_accounts"
    __fillable__ = ["candidate_id", "link", "likes_count", "page_name", "party_id"]
    __guarded__ = ["id"]

    @belongs_to
    def candidate(self):
        return candidate.Candidate

    @belongs_to
    def party(self):
        return party.Party

    @has_many
    def posts(self):
        return facebook.FacebookPost

    def fetch_and_set_likes_count(self):
        params = { "fields": "fan_count" }
        api_response = get_facebook_graph_api_response(self.page_name, params)

        self.likes_count = api_response["fan_count"]
        self.save()
