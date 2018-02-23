from marshmallow_sqlalchemy import ModelSchema
from .models import QueryHistory


class QueryHistorySchema(ModelSchema):
    class Meta:
        model = QueryHistory
