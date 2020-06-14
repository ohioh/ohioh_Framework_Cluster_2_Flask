from flask import make_response
from main.resources.message_templates import error_message
from bson.objectid import ObjectId


class DbOperations:
    def __init__(self, collections, schema):
        self.collections = collections
        self.schema = schema

    def insert(self, payload):
        payload = self.schema().load(payload)
        inserted_id = self.collections.insert_one(payload).inserted_id
        return str(inserted_id)

    def find_one(self, criteria):
        record = self.collections.find_one(criteria)
        result = self.schema().dump(record) if record is not None else error_message(criteria, 'Record not found')
        return make_response(result)

    def find_all(self):
        cursor = self.collections.find()
        result = self.schema(many=True).dumps(cursor)
        return make_response(result)

    def update(self, criteria, update):
        new_value = { "$set": update }
        result = self.collections.update_one(criteria, new_value, upsert=True).modified_count
        return result

    def delete(self, criteria):
        result = self.collections.delete_one(criteria)
        return result.deleted_count
