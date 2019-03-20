from datetime import datetime, date
import json

class DigitalWalletTokenRequestAddress(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_request_address.DigitalWalletTokenRequestAddress>'