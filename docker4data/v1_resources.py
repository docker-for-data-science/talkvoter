from flask_restful import Resource, Api
from flask import Blueprint
from marshmallow import ValidationError
from webargs.flaskparser import use_args
from .models import db
from .serializers import VoteSchema
from .constants import VoteValue


api_bp = Blueprint('api_v1', __name__)
api = Api(api_bp)


class VoteResource(Resource):

    def post(self):
        return self.get()

    def get(self):
        schema = VoteSchema()
        msg = ""
        try:
            obj = schema.load(
                {'value': VoteValue.in_person.value},
                session=db.session)
        except ValidationError as err:
            err.messages
            valid_data = err.valid_data
            data = str(err)
            ret_code = 400
            msg = "Fail"
        else:
            db.session.add(obj.data)
            db.session.commit()
            data = schema.dump(obj.data)
            msg = "Success"
            ret_code = 200
        return {"message": msg}, ret_code


api.add_resource(VoteResource, '/talk/')
