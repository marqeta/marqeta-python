from datetime import datetime

class Gpa(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def trigger_amount(self):
        if 'trigger_amount' in self.json_response:
            return self.json_response['trigger_amount']

    @property
    def reload_amount(self):
        if 'reload_amount' in self.json_response:
            return self.json_response['reload_amount']

