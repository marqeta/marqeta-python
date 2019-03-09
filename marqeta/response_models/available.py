from datetime import datetime

class Available(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def uses(self):
        if 'uses' in self.json_response:
            return self.json_response['uses']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def days_remaining(self):
        if 'days_remaining' in self.json_response:
            return self.json_response['days_remaining']

