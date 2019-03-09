from datetime import datetime

class Special(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def merchant_on_boarding(self):
        if 'merchant_on_boarding' in self.json_response:
            return self.json_response['merchant_on_boarding']

