from datetime import datetime
from marqeta.response_models.account_model import AccountModel

class BalanceCacheModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def account(self):
        if 'account' in self.json_response:
            return AccountModel(self.json_response['account'])

    @property
    def balance(self):
        if 'balance' in self.json_response:
            return self.json_response['balance']

    @property
    def layers(self):
        if 'layers' in self.json_response:
            return self.json_response['layers']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

