import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from app import db
from orator.orm import has_many, has_one

class Party(db.Model):
    __table__ = "parties"
    __fillable__ = ["full_name", "short_name"]
