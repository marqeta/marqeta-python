from datetime import datetime

class ClientAccessTokenRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def application_token(self):
        if 'application_token' in self.json_response:
            return self.json_response['application_token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

