from datetime import datetime, date
from marqeta.response_models.account_model import AccountModel
import json

class BalanceCacheModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'account' : self.account,
           'balance' : self.balance,
           'layers' : self.layers,
           'user_token' : self.user_token,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.balance_cache_model.BalanceCacheModel>'