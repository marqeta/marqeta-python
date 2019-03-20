from datetime import datetime, date
import json

class DepositAccount(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def account_number(self):
        if 'account_number' in self.json_response:
            return self.json_response['account_number']

    @property
    def routing_number(self):
        if 'routing_number' in self.json_response:
            return self.json_response['routing_number']

    @property
    def allow_immediate_credit(self):
        if 'allow_immediate_credit' in self.json_response:
            return self.json_response['allow_immediate_credit']

    def __repr__(self):
         return '<Marqeta.response_models.deposit_account.DepositAccount>'