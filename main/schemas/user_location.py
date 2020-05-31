import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class UserLocationSchema(Schema):
    location_id = ms_fields.Str()
    date_time = ms_fields.DateTime(default=datetime.datetime.now())
    splitted = ms_fields.Bool()
    accuracy = ms_fields.Float()
    location_type = ms_fields.Float()
    longitude = ms_fields.Float()
    speed = ms_fields.Int()
    arrival = ms_fields.Bool()
    
    class Meta:
        unknown = EXCLUDE


