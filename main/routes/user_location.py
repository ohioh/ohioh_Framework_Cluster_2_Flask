import json
from flask import request
from main import mongo
from flask_restful import Resource
from ..schemas.user_location import UserLocationSchema
from ..services.db import DbOperations
from bson.objectid import ObjectId


user_location = mongo.ohioh.user_location
db = DbOperations(collections=user_location, schema=UserLocationSchema)


class UserLocationList(Resource):
    def get(self):
        return db.find_all()

    def post(self):
        payload = request.get_json()
        return db.insert(payload)


class UserLocation(Resource):
    def get(self, user_id):
        return db.find_one(
            criteria={'user_id': user_id}
        )

    def put(self, user_id):
        payload = request.get_json()
        return db.update(
            criteria={'user_id': user_id},
            update=payload
        )

    def delete(self, user_id):
        return db.delete(
            criteria={'user_id': user_id}
        )
