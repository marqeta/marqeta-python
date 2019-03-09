from datetime import datetime

class Track1Data(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def cvv(self):
        if 'cvv' in self.json_response:
            return self.json_response['cvv']

    @property
    def atc(self):
        if 'atc' in self.json_response:
            return self.json_response['atc']

