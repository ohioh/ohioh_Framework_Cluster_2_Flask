import os
from flask_restful import Resource

class Beat(Resource):
    def get(self):
        return 'the app UserLocation is running on {}'.format(os.getenv("FLASK_RUN_PORT"))


