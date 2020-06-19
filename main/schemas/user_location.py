from datetime import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class UserLocationSchema(Schema):
    user_id = ms_fields.Str()
    user_timestamp = ms_fields.DateTime(default=datetime.now())
    splitted = ms_fields.Bool(required=False)
    location_type = ms_fields.Int(required=True)
    longitude = ms_fields.Float(required=False)
    speed = ms_fields.Int(required=False)
    arrival = ms_fields.Bool(required=True)
    
    class Meta:
        unknown = EXCLUDE


