from marshmallow_jsonapi import Schema, fields

class PartySchema(Schema):
    id = fields.Str(dump_only=True)
    short_name = fields.Str()
    full_name = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        type_ = "parties"
        strict = True
