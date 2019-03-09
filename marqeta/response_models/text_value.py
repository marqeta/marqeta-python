from datetime import datetime

class TextValue(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

