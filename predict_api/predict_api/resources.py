from flask_restful import Resource, Api
from flask import Blueprint, request


api_bp = Blueprint('api_v1', __name__)
api = Api(api_bp)


class PredictResource(Resource):

    def post(self):
        return self.get()

    def get(self):
        content = request.json
        print(content)
        msg = {'predict': 1, }
        ret_code = 200
        return {"message": msg}, ret_code


api.add_resource(PredictResource, '/predict/', endpoint="api.predict")
