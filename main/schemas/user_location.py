import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class UserLocationSchema(Schema):
    user_id = ms_fields.Str()
    location_id = ms_fields.Str()
    date_time = ms_fields.DateTime(default=datetime.datetime.now())
    splitted = ms_fields.Bool()
    accuracy = ms_fields.Int()
    location_type = ms_fields.Int()
    longitude = ms_fields.Int()
    speed = ms_fields.Int()
    arrival = ms_fields.Bool()
    
    class Meta:
        unknown = EXCLUDE


