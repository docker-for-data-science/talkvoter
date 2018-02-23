from flask_restful import Resource, Api
from flask import Blueprint


api_bp = Blueprint('api_v1', __name__)
api = Api(api_bp)


class LookupResource(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(LookupResource, '/lookup/')
