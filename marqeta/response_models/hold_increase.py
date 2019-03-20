from datetime import datetime, date
import json

class HoldIncrease(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

    def __repr__(self):
         return '<Marqeta.response_models.hold_increase.HoldIncrease>'