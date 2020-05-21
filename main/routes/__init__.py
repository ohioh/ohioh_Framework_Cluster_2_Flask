from flask import Blueprint
from .user_location import UserLocationList, UserLocation
from flask_restful import Api

from .beat import Beat

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/ohioh/api/v1')

api.add_resource(Beat, '/')
api.add_resource(UserLocationList, '/user-location')
api.add_resource(UserLocation, '/user-location/<location_id>')
