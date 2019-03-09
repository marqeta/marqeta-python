from datetime import datetime
from marqeta.response_models.transaction_model import TransactionModel

class SimulationResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transaction(self):
        if 'transaction' in self.json_response:
            return TransactionModel(self.json_response['transaction'])

    @property
    def raw_iso8583(self):
        if 'raw_iso8583' in self.json_response:
            return self.json_response['raw_iso8583']

