from datetime import datetime, date
import json

class DigitalWalletApplePayProvisionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def device_type(self):
        if 'device_type' in self.json_response:
            return self.json_response['device_type']

    @property
    def provisioning_app_version(self):
        if 'provisioning_app_version' in self.json_response:
            return self.json_response['provisioning_app_version']

    @property
    def certificates(self):
        if 'certificates' in self.json_response:
            return self.json_response['certificates']

    @property
    def nonce(self):
        if 'nonce' in self.json_response:
            return self.json_response['nonce']

    @property
    def nonce_signature(self):
        if 'nonce_signature' in self.json_response:
            return self.json_response['nonce_signature']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_apple_pay_provision_request.DigitalWalletApplePayProvisionRequest>'