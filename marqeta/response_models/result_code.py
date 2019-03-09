from datetime import datetime

class ResultCode(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def code(self):
        if 'code' in self.json_response:
            return self.json_response['code']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

