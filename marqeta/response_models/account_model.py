from datetime import datetime

class AccountModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def code(self):
        if 'code' in self.json_response:
            return self.json_response['code']

    @property
    def description(self):
        if 'description' in self.json_response:
            return self.json_response['description']

