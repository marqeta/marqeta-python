from datetime import datetime

class ControlTokenRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

