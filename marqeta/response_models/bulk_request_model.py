from datetime import datetime, date
import json

class BulkRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'user_tokens' : self.user_tokens,
           'business_tokens' : self.business_tokens,
           'card_tokens' : self.card_tokens,
           'kyc_tokens' : self.kyc_tokens,
           'dda_tokens' : self.dda_tokens,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.bulk_request_model.BulkRequestModel>'