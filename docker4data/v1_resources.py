from flask_restful import Resource, Api
from flask import Blueprint
from marshmallow import ValidationError
from .models import db
from .serializers import QueryHistorySchema


api_bp = Blueprint('api_v1', __name__)
api = Api(api_bp)


class LookupResource(Resource):
    def get(self):

        schema = QueryHistorySchema()

        try:
            obj = schema.load(
                {'name': 'John', 'result': 'foo'},
                session=db.session)
        except ValidationError as err:
            err.messages
            valid_data = err.valid_data
        db.session.add(obj.data)
        db.session.commit()
        return schema.dump(obj.data)


api.add_resource(LookupResource, '/lookup/')
