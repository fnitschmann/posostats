from .application_record import ApplicationRecord
from orator.orm import has_many, has_one

class Party(ApplicationRecord):
    __table__ = "parties"
    __fillable__ = ["full_name", "short_name"]
