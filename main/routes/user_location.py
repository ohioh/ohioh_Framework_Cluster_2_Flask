import json
from flask import request
from main import mongo
from flask_restful import Resource
from ..schemas.user_location import UserLocationSchema
from ..services.db import DbOperations


user_location = mongo.ohioh.user_location
db = DbOperations(collections=user_location, schema=UserLocationSchema)


class UserLocationList(Resource):
    def get(self):
        return db.find_all()

    def post(self):
        payload = request.get_json()
        return db.insert(payload)


class UserLocation(Resource):
    def get(self, location_id):
        j = location_id
        return db.find_one(
            criteria={'location_id': location_id}
        )

    def put(self, location_id):
        payload = request.get_json()
        return db.update(
            criteria={'location_id': location_id},
            updated_value=payload
        )

    def delete(self, location_id):
        return db.delete(
            criteria={'location_id': location_id}
        )
