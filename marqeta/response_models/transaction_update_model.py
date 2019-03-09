from datetime import datetime

class TransactionUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

