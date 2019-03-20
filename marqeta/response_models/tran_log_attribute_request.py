from datetime import datetime, date
import json

class TranLogAttributeRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def attribute_name(self):
        if 'attribute_name' in self.json_response:
            return self.json_response['attribute_name']

    @property
    def attribute_value(self):
        if 'attribute_value' in self.json_response:
            return self.json_response['attribute_value']

    def __repr__(self):
         return '<Marqeta.response_models.tran_log_attribute_request.TranLogAttributeRequest>'