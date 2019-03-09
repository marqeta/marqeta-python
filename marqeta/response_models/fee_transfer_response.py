from datetime import datetime
from marqeta.response_models.fee_detail import FeeDetail

class FeeTransferResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def fees(self):
        if 'fees' in self.json_response:
            return [FeeDetail(val) for val in self.json_response['fees']]

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
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

