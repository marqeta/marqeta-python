from datetime import datetime, date
from marqeta.response_models.network import Network
import json

class CurrencyConversion(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network(self):
        if 'network' in self.json_response:
            return Network(self.json_response['network'])

    def __repr__(self):
         return '<Marqeta.response_models.currency_conversion.CurrencyConversion>'