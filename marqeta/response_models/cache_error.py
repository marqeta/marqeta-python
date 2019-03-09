from datetime import datetime

class CacheError(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

