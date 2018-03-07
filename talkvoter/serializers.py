from marshmallow_sqlalchemy import ModelSchema
import toastedmarshmallow
from .models import Vote


class VoteSchema(ModelSchema):
    class Meta:
        jit = toastedmarshmallow.Jit
        model = Vote
        fields = ['value']
