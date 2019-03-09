from datetime import datetime

class BillingAddress(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def first_name(self):
        if 'first_name' in self.json_response:
            return self.json_response['first_name']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def address(self):
        if 'address' in self.json_response:
            return self.json_response['address']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

