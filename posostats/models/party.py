from .connection import db
from orator import Model

class Party(Model):
    __table__ = "parties"
    __fillable__ = ["full_name", "short_name"]
    __guarded__  = ["id"]
