from datetime import datetime

class TranLogAttributeRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

