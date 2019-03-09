from datetime import datetime

class MinOffset(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def unit(self):
        if 'unit' in self.json_response:
            return self.json_response['unit']

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

