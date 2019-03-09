from datetime import datetime

class PanRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def pan(self):
        if 'pan' in self.json_response:
            return self.json_response['pan']

    @property
    def cvv_number(self):
        if 'cvv_number' in self.json_response:
            return self.json_response['cvv_number']

    @property
    def expiration(self):
        if 'expiration' in self.json_response:
            return self.json_response['expiration']

