from flask_restful import Resource, Api
from flask import Blueprint
from .models import QueryHistory
from .models import db


api_bp = Blueprint('api_v1', __name__)
api = Api(api_bp)


class LookupResource(Resource):
    def get(self):
        qh = QueryHistory(name='test', result='bar')
        db.session.add(qh)
        db.session.commit()
        return {'hello': 'world'}


api.add_resource(LookupResource, '/lookup/')
