from datetime import datetime

class PinRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def control_token(self):
        if 'control_token' in self.json_response:
            return self.json_response['control_token']

    @property
    def pin(self):
        if 'pin' in self.json_response:
            return self.json_response['pin']

