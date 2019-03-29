from datetime import datetime, date
import json


class DigitalWalletAndroidPayProvisionRequest(object):

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
        return self.json_response.get('card_token', None)

    @property
    def device_type(self):
        return self.json_response.get('device_type', None)

    @property
    def provisioning_app_version(self):
        return self.json_response.get('provisioning_app_version', None)

    @property
    def wallet_account_id(self):
        return self.json_response.get('wallet_account_id', None)

    @property
    def device_id(self):
        return self.json_response.get('device_id', None)

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_android_pay_provision_request.DigitalWalletAndroidPayProvisionRequest>'
