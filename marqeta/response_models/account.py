from datetime import datetime

class Account(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def email_address(self):
        if 'email_address' in self.json_response:
            return self.json_response['email_address']

    @property
    def score(self):
        if 'score' in self.json_response:
            return self.json_response['score']

