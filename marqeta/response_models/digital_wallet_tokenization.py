from datetime import datetime, date
from marqeta.response_models.provisioning_controls import ProvisioningControls
import json

class DigitalWalletTokenization(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'provisioning_controls' : self.provisioning_controls,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def provisioning_controls(self):
        if 'provisioning_controls' in self.json_response:
            return ProvisioningControls(self.json_response['provisioning_controls'])

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_tokenization.DigitalWalletTokenization>'