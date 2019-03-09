from datetime import datetime
from marqeta.response_models.min_offset import MinOffset

class ExpirationOffset(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def unit(self):
        if 'unit' in self.json_response:
            return self.json_response['unit']

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

    @property
    def min_offset(self):
        if 'min_offset' in self.json_response:
            return MinOffset(self.json_response['min_offset'])

