import importlib, os, schemas, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from app import db

class ApplicationRecord(db.Model):
    @classmethod
    def schema(cls):
        schema_classname = cls.__name__ + "Schema"
        klass = getattr(importlib.import_module("schemas"), schema_classname)

        return klass()

