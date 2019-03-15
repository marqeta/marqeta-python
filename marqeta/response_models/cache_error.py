from datetime import datetime, date
import json

class CacheError(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'id' : self.id,
           'message' : self.message,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

    def __repr__(self):
         return '<Marqeta.response_models.cache_error.CacheError>'