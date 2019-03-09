from datetime import datetime

class ChargebackTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def chargeback_token(self):
        if 'chargeback_token' in self.json_response:
            return self.json_response['chargeback_token']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

