from datetime import datetime
from marqeta.response_models.response import Response
from marqeta.response_models.funding import Funding


class GpaReturns(object):

    def __init__(self, response):
        self.gpa_response = response

    @property
    def token(self):
        if 'token' in self.gparesponse:
            return self.gparesponse['token']

    @property
    def amount(self):
        if 'amount' in self.gparesponse:
            return self.gparesponse['amount']

    @property
    def tags(self):
        if 'tags' in self.gparesponse:
            return self.gparesponse['tags']

    @property
    def memo(self):
        if 'memo' in self.gparesponse:
            return self.gparesponse['memo']

    @property
    def created_time(self):
        if 'created_time' in self.gparesponse:
            return datetime.strptime(self.gparesponse['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.gparesponse:
            return datetime.strptime(self.gparesponse['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def transaction_token(self):
        if 'transaction_token' in self.gparesponse:
            return self.gparesponse['transaction_token']

    @property
    def state(self):
        if 'state' in self.gparesponse:
            return self.gparesponse['state']

    @property
    def gparesponse(self):
        if 'response' in self.gparesponse:
            return Response(self.gparesponse['response'])

    @property
    def funding(self):
        if 'funding' in self.gparesponse:
            return Funding(self.gparesponse['funding'])

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.gparesponse:
            return self.gparesponse['funding_source_token']

    @property
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.gparesponse:
            return self.gparesponse['funding_source_address_token']

    @property
    def original_order_token(self):
        if 'original_order_token' in self.gparesponse:
            return self.gparesponse['original_order_token']
