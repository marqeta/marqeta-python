from datetime import datetime

class ReplacementAmount(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transaction_amount(self):
        if 'transaction_amount' in self.json_response:
            return self.json_response['transaction_amount']

    @property
    def settlement_amount(self):
        if 'settlement_amount' in self.json_response:
            return self.json_response['settlement_amount']

    @property
    def transaction_fee(self):
        if 'transaction_fee' in self.json_response:
            return self.json_response['transaction_fee']

    @property
    def settlement_fee(self):
        if 'settlement_fee' in self.json_response:
            return self.json_response['settlement_fee']

