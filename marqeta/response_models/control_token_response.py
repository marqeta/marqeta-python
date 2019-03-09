from datetime import datetime

class ControlTokenResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def control_token(self):
        if 'control_token' in self.json_response:
            return self.json_response['control_token']

