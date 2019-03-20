from datetime import datetime, date
import json

class DigitalWalletTokenWalletProvider(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def wallet_provider_cardholder_wallet_account_id(self):
        if 'wallet_provider_cardholder_wallet_account_id' in self.json_response:
            return self.json_response['wallet_provider_cardholder_wallet_account_id']

    @property
    def wallet_provider_risk_assessment(self):
        if 'wallet_provider_risk_assessment' in self.json_response:
            return self.json_response['wallet_provider_risk_assessment']

    @property
    def wallet_provider_risk_assessment_version(self):
        if 'wallet_provider_risk_assessment_version' in self.json_response:
            return self.json_response['wallet_provider_risk_assessment_version']

    @property
    def wallet_provider_device_score(self):
        if 'wallet_provider_device_score' in self.json_response:
            return self.json_response['wallet_provider_device_score']

    @property
    def wallet_provider_account_score(self):
        if 'wallet_provider_account_score' in self.json_response:
            return self.json_response['wallet_provider_account_score']

    @property
    def wallet_provider_pan_source(self):
        if 'wallet_provider_pan_source' in self.json_response:
            return self.json_response['wallet_provider_pan_source']

    @property
    def wallet_provider_reason_code(self):
        if 'wallet_provider_reason_code' in self.json_response:
            return self.json_response['wallet_provider_reason_code']

    @property
    def recommendation_reasons(self):
        if 'recommendation_reasons' in self.json_response:
            return self.json_response['recommendation_reasons']

    @property
    def cardholder_wallet_account_email(self):
        if 'cardholder_wallet_account_email' in self.json_response:
            return self.json_response['cardholder_wallet_account_email']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_wallet_provider.DigitalWalletTokenWalletProvider>'