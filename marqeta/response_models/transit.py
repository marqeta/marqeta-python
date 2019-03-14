from datetime import datetime, date
import json

class Transit(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'transaction_type' : self.transaction_type,
           'transportation_mode' : self.transportation_mode,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_type(self):
        if 'transaction_type' in self.json_response:
            return self.json_response['transaction_type']

    @property
    def transportation_mode(self):
        if 'transportation_mode' in self.json_response:
            return self.json_response['transportation_mode']

    def __repr__(self):
         return '<Marqeta.response_models.transit.Transit>'