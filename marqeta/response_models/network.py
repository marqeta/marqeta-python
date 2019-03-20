from datetime import datetime, date
import json

class Network(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def original_amount(self):
        if 'original_amount' in self.json_response:
            return self.json_response['original_amount']

    @property
    def conversion_rate(self):
        if 'conversion_rate' in self.json_response:
            return self.json_response['conversion_rate']

    @property
    def original_currency_code(self):
        if 'original_currency_code' in self.json_response:
            return self.json_response['original_currency_code']

    def __repr__(self):
         return '<Marqeta.response_models.network.Network>'