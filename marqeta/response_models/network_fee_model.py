from datetime import datetime

class NetworkFeeModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def credit_debit(self):
        if 'credit_debit' in self.json_response:
            return self.json_response['credit_debit']

