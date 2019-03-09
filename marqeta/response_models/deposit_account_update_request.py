from datetime import datetime

class DepositAccountUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def allow_immediate_credit(self):
        if 'allow_immediate_credit' in self.json_response:
            return self.json_response['allow_immediate_credit']

