from datetime import datetime, date
import json

class TokenRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'account_number' : self.account_number,
           'cvv_number' : self.cvv_number,
           'exp_date' : self.exp_date,
           'zip' : self.zip,
           'postal_code' : self.postal_code,
           'is_default_account' : self.is_default_account,
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
    def cvv_number(self):
        if 'cvv_number' in self.json_response:
            return self.json_response['cvv_number']

    @property
    def exp_date(self):
        if 'exp_date' in self.json_response:
            return self.json_response['exp_date']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.json_response:
            return self.json_response['is_default_account']

    def __repr__(self):
         return '<Marqeta.response_models.token_request.TokenRequest>'