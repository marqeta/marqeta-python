from datetime import datetime, date
from marqeta.response_models.fee import Fee
import json

class FeeDetail(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'memo' : self.memo,
           'tags' : self.tags,
           'transaction_token' : self.transaction_token,
           'fee' : self.fee,
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
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def fee(self):
        if 'fee' in self.json_response:
            return Fee(self.json_response['fee'])

    def __repr__(self):
         return '<Marqeta.response_models.fee_detail.FeeDetail>'