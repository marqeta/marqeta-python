from datetime import datetime

class PushToCardDisburseRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def payment_instrument_token(self):
        if 'payment_instrument_token' in self.json_response:
            return self.json_response['payment_instrument_token']

