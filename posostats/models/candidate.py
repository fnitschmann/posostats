from . import party
from .accounts import facebook, twitter
from .connection import db
from orator import Model
from orator.orm import belongs_to, has_one

class Candidate(Model):
    __table__ = "candidates"
    __fillable__ = ["first_name", "last_name", "party_id", "title"]
    __guarded__ = ["id"]

    @belongs_to
    def party(self):
        return party.Party

    @has_one
    def facebook_account(self):
        return facebook.FacebookAccount

    @has_one
    def twitter_account(self):
        return twitter.TwitterAccount
