from datetime import datetime

class Transit(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transaction_type(self):
        if 'transaction_type' in self.json_response:
            return self.json_response['transaction_type']

    @property
    def transportation_mode(self):
        if 'transportation_mode' in self.json_response:
            return self.json_response['transportation_mode']

