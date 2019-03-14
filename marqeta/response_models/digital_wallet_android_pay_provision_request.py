from datetime import datetime, date
import json

class DigitalWalletAndroidPayProvisionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'card_token' : self.card_token,
           'device_type' : self.device_type,
           'provisioning_app_version' : self.provisioning_app_version,
           'wallet_account_id' : self.wallet_account_id,
           'device_id' : self.device_id,
         }
        return json.dumps(dict, default=self.json_serial)

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
    def wallet_account_id(self):
        if 'wallet_account_id' in self.json_response:
            return self.json_response['wallet_account_id']

    @property
    def device_id(self):
        if 'device_id' in self.json_response:
            return self.json_response['device_id']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_android_pay_provision_request.DigitalWalletAndroidPayProvisionRequest>'