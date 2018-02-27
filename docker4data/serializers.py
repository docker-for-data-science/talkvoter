from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pprint
import toastedmarshmallow
from .models import QueryHistory


class QueryHistorySchema(ModelSchema):
    class Meta:
        jit = toastedmarshmallow.Jit
        model = QueryHistory
        fields = ['name']


# class QueryHistorySchema(Schema):
#
#     title = fields.Str()
#
#     class Meta:
#         jit = toastedmarshmallow.Jit
#     name = fields.Str()
