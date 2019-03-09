from datetime import datetime

class BulkRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def user_tokens(self):
        if 'user_tokens' in self.json_response:
            return self.json_response['user_tokens']

    @property
    def business_tokens(self):
        if 'business_tokens' in self.json_response:
            return self.json_response['business_tokens']

    @property
    def card_tokens(self):
        if 'card_tokens' in self.json_response:
            return self.json_response['card_tokens']

    @property
    def kyc_tokens(self):
        if 'kyc_tokens' in self.json_response:
            return self.json_response['kyc_tokens']

    @property
    def dda_tokens(self):
        if 'dda_tokens' in self.json_response:
            return self.json_response['dda_tokens']

