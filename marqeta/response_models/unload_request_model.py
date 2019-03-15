from datetime import datetime, date
import json

class UnloadRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'original_order_token' : self.original_order_token,
           'amount' : self.amount,
           'tags' : self.tags,
           'memo' : self.memo,
           'funding_source_address_token' : self.funding_source_address_token,
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
    def original_order_token(self):
        if 'original_order_token' in self.json_response:
            return self.json_response['original_order_token']

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
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.json_response:
            return self.json_response['funding_source_address_token']

    def __repr__(self):
         return '<Marqeta.response_models.unload_request_model.UnloadRequestModel>'