from .. import candidate, party
from ..connection import db
from ..posts import twitter
from orator import Model
from orator.orm import belongs_to, has_many

class TwitterAccount(Model):
    __table__ = "twitter_accounts"
    __fillable__ = ["candidate_id", "link", "party_id", "screen_name"]
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
