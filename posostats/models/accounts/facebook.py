from .. import candidate, party
from ..connection import db
from ..posts import facebook
from orator import Model
from orator.orm import belongs_to, has_many

class FacebookAccount(Model):
    __table__ = "facebook_accounts"
    __fillable__ = ["candidate_id", "link", "page_name", "party_id"]
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
