from datetime import datetime
from marqeta.response_models.fee_model import FeeModel

class FeeTransferRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def fees(self):
        if 'fees' in self.json_response:
            return [FeeModel(val) for val in self.json_response['fees']]

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

