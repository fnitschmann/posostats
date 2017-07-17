from . import candidate
from .accounts import facebook, twitter
from .connection import db
from orator import Model
from orator.orm import has_many, has_one

class Party(Model):
    __table__ = "parties"
    __fillable__ = ["full_name", "short_name"]
    __guarded__  = ["id"]

    @has_many
    def candidates(self):
        return candidate.Candidate

    @has_one
    def facebook_account(self):
        return facebook.FacebookAccount

    @has_one
    def twitter_account(self):
        return twitter.TwitterAccount
