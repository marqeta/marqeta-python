from datetime import datetime, date
import json

class GatewayClearingRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'original_transaction_token' : self.original_transaction_token,
           'amount' : self.amount,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def original_transaction_token(self):
        if 'original_transaction_token' in self.json_response:
            return self.json_response['original_transaction_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    def __repr__(self):
         return '<Marqeta.response_models.gateway_clearing_request.GatewayClearingRequest>'