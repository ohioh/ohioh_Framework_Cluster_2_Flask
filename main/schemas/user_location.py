from datetime import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class UserLocationSchema(Schema):
    user_id = ms_fields.Str()
    user_timestamp = ms_fields.DateTime(default=datetime.now())
    splitted = ms_fields.Bool(default=True)
    location_type = ms_fields.Int(default=0)
    longitude = ms_fields.Float(default=0.0)
    speed = ms_fields.Int(default=0)
    arrival = ms_fields.Bool(default=False)
    
    class Meta:
        unknown = EXCLUDE


