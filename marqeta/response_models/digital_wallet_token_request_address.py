from datetime import datetime

class DigitalWalletTokenRequestAddress(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def cardholder_name(self):
        if 'cardholder_name' in self.json_response:
            return self.json_response['cardholder_name']

    @property
    def address(self):
        if 'address' in self.json_response:
            return self.json_response['address']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

