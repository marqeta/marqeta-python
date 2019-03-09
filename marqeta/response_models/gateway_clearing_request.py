from datetime import datetime

class GatewayClearingRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def original_transaction_token(self):
        if 'original_transaction_token' in self.json_response:
            return self.json_response['original_transaction_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

