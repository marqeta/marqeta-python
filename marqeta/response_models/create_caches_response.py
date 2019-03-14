from datetime import datetime, date
from marqeta.response_models.cache_error import CacheError
import json

class CreateCachesResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created' : self.created,
           'already_exists' : self.already_exists,
           'errors' : self.errors,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created(self):
        if 'created' in self.json_response:
            return self.json_response['created']

    @property
    def already_exists(self):
        if 'already_exists' in self.json_response:
            return self.json_response['already_exists']

    @property
    def errors(self):
        if 'errors' in self.json_response:
            return [CacheError(val) for val in self.json_response['errors']]

    def __repr__(self):
         return '<Marqeta.response_models.create_caches_response.CreateCachesResponse>'