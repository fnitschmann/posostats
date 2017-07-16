from .candidate import Candidate
from .connection import db
from orator import Model
from orator.orm import has_many

class Party(Model):
    __table__ = "parties"
    __fillable__ = ["full_name", "short_name"]
    __guarded__  = ["id"]

    @has_many
    def candidates(self):
        return Candidate
