from datetime import datetime, date
from marqeta.response_models.response import Response
from marqeta.response_models.funding import Funding
import json

class GpaReturns(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'amount' : self.amount,
           'tags' : self.tags,
           'memo' : self.memo,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'transaction_token' : self.transaction_token,
           'state' : self.state,
           'response' : self.response,
           'funding' : self.funding,
           'funding_source_token' : self.funding_source_token,
           'funding_source_address_token' : self.funding_source_address_token,
           'original_order_token' : self.original_order_token,
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
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

    @property
    def funding(self):
        if 'funding' in self.json_response:
            return Funding(self.json_response['funding'])

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.json_response:
            return self.json_response['funding_source_token']

    @property
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.json_response:
            return self.json_response['funding_source_address_token']

    @property
    def original_order_token(self):
        if 'original_order_token' in self.json_response:
            return self.json_response['original_order_token']

    def __repr__(self):
         return '<Marqeta.response_models.gpa_returns.GpaReturns>'