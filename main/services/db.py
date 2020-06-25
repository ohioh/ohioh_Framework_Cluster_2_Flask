from flask import make_response
from main.resources.message_templates import error_message
from bson.objectid import ObjectId
from datetime import datetime

class DbOperations:
    def __init__(self, collections, schema):
        self.collections = collections
        self.schema = schema

    def insert(self, payload):
        payload = self.schema().dump(payload)
        inserted_id = self.collections.insert_one(payload).inserted_id
        
        self.update(
            criteria={ '_id': ObjectId(inserted_id) },
            update={
                'user_timestamp': datetime.now().isoformat()
                }
        )
        return f"{str(inserted_id)} added"

    def find_one(self, criteria):
        record = self.collections.find_one(criteria)
        result = self.schema().load(record) if record is not None else error_message(criteria, 'Record not found')
        return make_response(result)

    def find_all(self):
        cursor = self.collections.find()
        result = self.schema().load(cursor, many=True)

        for each in result:
            each['user_timestamp'] = str(each['user_timestamp'])
            
        return result

    def update(self, criteria, update):
        new_value = { "$set": update }
        result = self.collections.update_one(criteria, new_value, upsert=True).modified_count
        return result

    def delete(self, criteria):
        result = self.collections.delete_one(criteria)
        return result.deleted_count
