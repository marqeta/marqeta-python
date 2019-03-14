from datetime import datetime, date
import json

class PinRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'control_token' : self.control_token,
           'pin' : self.pin,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def control_token(self):
        if 'control_token' in self.json_response:
            return self.json_response['control_token']

    @property
    def pin(self):
        if 'pin' in self.json_response:
            return self.json_response['pin']

    def __repr__(self):
         return '<Marqeta.response_models.pin_request.PinRequest>'