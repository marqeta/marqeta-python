from datetime import datetime

class LoadVelocityModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def description(self):
        if 'description' in self.json_response:
            return self.json_response['description']

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def layers(self):
        if 'layers' in self.json_response:
            return self.json_response['layers']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def days(self):
        if 'days' in self.json_response:
            return self.json_response['days']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

