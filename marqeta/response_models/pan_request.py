from datetime import datetime, date
import json

class PanRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'pan' : self.pan,
           'cvv_number' : self.cvv_number,
           'expiration' : self.expiration,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pan(self):
        if 'pan' in self.json_response:
            return self.json_response['pan']

    @property
    def cvv_number(self):
        if 'cvv_number' in self.json_response:
            return self.json_response['cvv_number']

    @property
    def expiration(self):
        if 'expiration' in self.json_response:
            return self.json_response['expiration']

    def __repr__(self):
         return '<Marqeta.response_models.pan_request.PanRequest>'