from datetime import datetime, date
import json

class MinOffset(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'unit' : self.unit,
           'value' : self.value,
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

    def __repr__(self):
         return '<Marqeta.response_models.min_offset.MinOffset>'