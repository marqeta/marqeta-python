from datetime import datetime
from marqeta.response_models.network import Network

class CurrencyConversion(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def network(self):
        if 'network' in self.json_response:
            return Network(self.json_response['network'])

