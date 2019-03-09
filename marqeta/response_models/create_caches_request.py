from datetime import datetime

class CreateCachesRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transactions(self):
        if 'transactions' in self.json_response:
            return self.json_response['transactions']

