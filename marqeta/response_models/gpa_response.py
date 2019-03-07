from datetime import datetime
from marqeta.response_models.fee_detail import FeeDetail
from marqeta.response_models.response import Response as Res
from marqeta.response_models.funding import Funding


class GpaResponse(object):

    def __init__(self, response):
        self.gpa_response = response

    @property
    def token(self):
        if 'token' in self.gpa_response:
            return self.gpa_response['token']

    @property
    def amount(self):
        if 'amount' in self.gpa_response:
            return self.gpa_response['amount']

    @property
    def tags(self):
        if 'tags' in self.gpa_response:
            return self.gpa_response['tags']

    @property
    def memo(self):
        if 'memo' in self.gpa_response:
            return self.gpa_response['memo']

    @property
    def fees(self):
        if 'fees' in self.gpa_response:
            return FeeDetail(self.gpa_response['fees'])

    @property
    def created_time(self):
        if 'created_time' in self.gpa_response:
            return datetime.strptime(self.gpa_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.gpa_response:
            return datetime.strptime(self.gpa_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def transaction_token(self):
        if 'transaction_token' in self.gpa_response:
            return self.gpa_response['transaction_token']

    @property
    def state(self):
        if 'state' in self.gpa_response:
            return self.gpa_response['state']

    @property
    def response(self):
        if 'response' in self.gpa_response:
            return Res(self.gpa_response['response'])

    @property
    def funding(self):
        if 'funding' in self.gpa_response:
            return Funding(self.gpa_response['funding'])

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.gpa_response:
            return self.gpa_response['funding_source_token']

    @property
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.gpa_response:
            return self.gpa_response['funding_source_address_token']

    @property
    def user_token(self):
        if 'user_token' in self.gpa_response:
            return self.gpa_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.gpa_response:
            return self.gpa_response['business_token']

    @property
    def currency_code(self):
        if 'currency_code' in self.gpa_response:
            return self.gpa_response['currency_code']

    @property
    def gateway_token(self):
        if 'gateway_token' in self.gpa_response:
            return self.gpa_response['gateway_token']

    @property
    def gateway_message(self):
        if 'gateway_message' in self.gpa_response:
            return self.gpa_response['gateway_message']
