from datetime import datetime

class TokenUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def exp_date(self):
        if 'exp_date' in self.json_response:
            return self.json_response['exp_date']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.json_response:
            return self.json_response['is_default_account']

