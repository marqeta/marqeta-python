from datetime import datetime

class AdviceRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

