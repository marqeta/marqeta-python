from datetime import datetime

class MoneyModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def currency(self):
        if 'currency' in self.json_response:
            return self.json_response['currency']

