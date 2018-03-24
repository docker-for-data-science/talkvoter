from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import Blueprint, abort
from sqlalchemy.sql.expression import func
from marshmallow import ValidationError
from .models import db, Talk
from .serializers import VoteSchema, TalkSchema
from .constants import VoteValue


api_bp = Blueprint('api_v1', __name__)
api = Api(api_bp)


def get_talk_or_abort(id):
    talk_obj = db.session.query(Talk).filter(Talk.id == id).first()
    if not talk_obj:
        abort(404, '`talk_id` is not in database')
    return talk_obj


class TalksListResource(Resource):

    def get(self):
        schema = TalkSchema()
        talk_objs = db.session.query(Talk)
        data = schema.dump(talk_objs, many=True).data
        return data, 200


api.add_resource(TalksListResource, '/talks/', endpoint="api.talks")


class TalkDetailResource(Resource):

    def get(self, id):
        schema = TalkSchema()
        talk_obj = get_talk_or_abort(id)
        data = schema.dump(talk_obj).data
        return data, 200


api.add_resource(TalkDetailResource, '/talks/<int:id>/', endpoint="api.talk")


class TalkRandResource(Resource):

    def get(self):
        schema = TalkSchema()
        talk_obj = db.session.query(Talk).order_by(func.random()).first()
        if not talk_obj:
            abort(404, '`talk_id` is not in database')
        data = schema.dump(talk_obj).data
        return data, 200


api.add_resource(TalkRandResource, '/talks/random/', endpoint="api.talkrand")


def validate_vote_type(value):
    if value not in [VoteValue.in_person.value, VoteValue.watch_later.value]:
        raise ValueError("Invalid object: must be watch_later or in_person")
    return value


class VoteResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'vote', type=validate_vote_type,
        required=True, help='Must be in_person | watch_later')

    def post(self, id):
        return self.get()

    def get(self, id):
        talk_obj = get_talk_or_abort(id)
        args = self.parser.parse_args()
        vote = args['vote']

        schema = VoteSchema()
        msg = ""
        try:
            serial_obj = schema.load(
                {'value': vote},
                session=db.session)
        except ValidationError as err:
            err.messages
            valid_data = err.valid_data
            data = str(err)
            print(data, valid_data)
            ret_code = 400
            msg = "Fail"
        else:
            obj = serial_obj.data
            obj.talk = talk_obj
            db.session.add(obj)
            db.session.commit()
            msg = "Success"
            ret_code = 200
        return {"message": msg}, ret_code


api.add_resource(VoteResource, '/talks/<int:id>/vote/', endpoint="api.vote")
