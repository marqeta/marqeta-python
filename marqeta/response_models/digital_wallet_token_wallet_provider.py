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
        return self.json_response.get('wallet_provider_cardholder_wallet_account_id', None)

    @property
    def wallet_provider_risk_assessment(self):
        return self.json_response.get('wallet_provider_risk_assessment', None)

    @property
    def wallet_provider_risk_assessment_version(self):
        return self.json_response.get('wallet_provider_risk_assessment_version', None)

    @property
    def wallet_provider_device_score(self):
        return self.json_response.get('wallet_provider_device_score', None)

    @property
    def wallet_provider_account_score(self):
        return self.json_response.get('wallet_provider_account_score', None)

    @property
    def wallet_provider_pan_source(self):
        return self.json_response.get('wallet_provider_pan_source', None)

    @property
    def wallet_provider_reason_code(self):
        return self.json_response.get('wallet_provider_reason_code', None)

    @property
    def recommendation_reasons(self):
        return self.json_response.get('recommendation_reasons', None)

    @property
    def cardholder_wallet_account_email(self):
        return self.json_response.get('cardholder_wallet_account_email', None)

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_token_wallet_provider.DigitalWalletTokenWalletProvider>'
