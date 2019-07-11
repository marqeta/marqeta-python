from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class DigitalWalletApplePayProvisionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime_object('created_time', self.json_response)


    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime_object('last_modified_time', self.json_response)


    @property
    def card_token(self):
        return self.json_response.get('card_token', None)


    @property
    def encrypted_pass_data(self):
        return self.json_response.get('encrypted_pass_data', None)


    @property
    def activation_data(self):
        return self.json_response.get('activation_data', None)


    @property
    def ephemeral_public_key(self):
        return self.json_response.get('ephemeral_public_key', None)


    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_apple_pay_provision_response.DigitalWalletApplePayProvisionResponse>' + self.__str__()
