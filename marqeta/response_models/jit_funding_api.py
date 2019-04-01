from datetime import datetime, date
from marqeta.response_models.jit_address_verification import JitAddressVerification
import json


class JitFundingApi(object):

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
        return self.json_response.get('token', None)

    @property
    def method(self):
        return self.json_response.get('method', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def acting_user_token(self):
        return self.json_response.get('acting_user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def memo(self):
        return self.json_response.get('memo', None)

    @property
    def tags(self):
        return self.json_response.get('tags', None)

    @property
    def original_jit_funding_token(self):
        return self.json_response.get('original_jit_funding_token', None)

    @property
    def incremental_authorization_jit_funding_tokens(self):
        return self.json_response.get('incremental_authorization_jit_funding_tokens', None)

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return JitAddressVerification(self.json_response['address_verification'])

    def __repr__(self):
        return '<Marqeta.response_models.jit_funding_api.JitFundingApi>'
