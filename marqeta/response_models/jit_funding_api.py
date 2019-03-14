from datetime import datetime, date
from marqeta.response_models.jit_address_verification import JitAddressVerification
import json

class JitFundingApi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'method' : self.method,
           'user_token' : self.user_token,
           'acting_user_token' : self.acting_user_token,
           'business_token' : self.business_token,
           'amount' : self.amount,
           'memo' : self.memo,
           'tags' : self.tags,
           'original_jit_funding_token' : self.original_jit_funding_token,
           'incremental_authorization_jit_funding_tokens' : self.incremental_authorization_jit_funding_tokens,
           'address_verification' : self.address_verification,
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
    def method(self):
        if 'method' in self.json_response:
            return self.json_response['method']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def acting_user_token(self):
        if 'acting_user_token' in self.json_response:
            return self.json_response['acting_user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def original_jit_funding_token(self):
        if 'original_jit_funding_token' in self.json_response:
            return self.json_response['original_jit_funding_token']

    @property
    def incremental_authorization_jit_funding_tokens(self):
        if 'incremental_authorization_jit_funding_tokens' in self.json_response:
            return self.json_response['incremental_authorization_jit_funding_tokens']

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return JitAddressVerification(self.json_response['address_verification'])

    def __repr__(self):
         return '<Marqeta.response_models.jit_funding_api.JitFundingApi>'