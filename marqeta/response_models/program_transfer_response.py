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

        return self.json_response.get('token', None)

    @property
    def type_token(self):

        return self.json_response.get('type_token', None)

    @property
    def user_token(self):

        return self.json_response.get('user_token', None)

    @property
    def business_token(self):

        return self.json_response.get('business_token', None)

    @property
    def transaction_token(self):

        return self.json_response.get('transaction_token', None)

    @property
    def currency_code(self):

        return self.json_response.get('currency_code', None)

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
    def created_time(self):

        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def jit_funding(self):

        if 'jit_funding' in self.json_response:
            return JitFundingApi(self.json_response['jit_funding'])

    def __repr__(self):
        return '<Marqeta.response_models.program_transfer_response.ProgramTransferResponse>'
