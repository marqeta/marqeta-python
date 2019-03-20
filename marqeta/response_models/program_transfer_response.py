from datetime import datetime, date
from marqeta.response_models.fee_detail import FeeDetail
from marqeta.response_models.jit_funding_api import JitFundingApi
import json

class ProgramTransferResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def fees(self):
        if 'fees' in self.json_response:
            return [FeeDetail(val) for val in self.json_response['fees']]

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def type_token(self):
        if 'type_token' in self.json_response:
            return self.json_response['type_token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

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
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def jit_funding(self):
        if 'jit_funding' in self.json_response:
            return JitFundingApi(self.json_response['jit_funding'])

    def __repr__(self):
         return '<Marqeta.response_models.program_transfer_response.ProgramTransferResponse>'