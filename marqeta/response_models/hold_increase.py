from datetime import datetime

class HoldIncrease(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

