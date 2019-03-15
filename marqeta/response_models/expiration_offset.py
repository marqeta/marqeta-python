from datetime import datetime, date
from marqeta.response_models.min_offset import MinOffset
import json

class ExpirationOffset(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'unit' : self.unit,
           'value' : self.value,
           'min_offset' : self.min_offset,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.expiration_offset.ExpirationOffset>'