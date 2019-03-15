from datetime import datetime, date
import json

class DigitalWalletTokenAddressVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'validate' : self.validate,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def validate(self):
        if 'validate' in self.json_response:
            return self.json_response['validate']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_address_verification.DigitalWalletTokenAddressVerification>'