from datetime import datetime
from marqeta.response_models.cache_error import CacheError

class CreateCachesResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

