from datetime import datetime, date
from marqeta.response_models.digital_wallet_token_address_verification import DigitalWalletTokenAddressVerification
import json


class ManualEntry(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def enabled(self):
        return self.json_response.get('enabled', None)

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return DigitalWalletTokenAddressVerification(self.json_response['address_verification'])

    def __repr__(self):
        return '<Marqeta.response_models.manual_entry.ManualEntry>'
