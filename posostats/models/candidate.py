from .connection import db
from orator import Model
from orator.orm import belongs_to
from .party import Party

class Candidate(Model):
    __table__ = "candidates"
    __fillable__ = ["first_name", "last_name", "party_id", "title"]
    __guarded__ = ["id"]

    @belongs_to
    def party(self):
        return Party
