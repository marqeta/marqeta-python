from datetime import datetime, date
from marqeta.response_models.account import Account
from marqeta.response_models.risk_assessment import RiskAssessment
import json

class WalletProviderProfile(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'account' : self.account,
           'risk_assessment' : self.risk_assessment,
           'device_score' : self.device_score,
           'pan_source' : self.pan_source,
           'reason_code' : self.reason_code,
           'recommendation_reasons' : self.recommendation_reasons,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def account(self):
        if 'account' in self.json_response:
            return Account(self.json_response['account'])

    @property
    def risk_assessment(self):
        if 'risk_assessment' in self.json_response:
            return RiskAssessment(self.json_response['risk_assessment'])

    @property
    def device_score(self):
        if 'device_score' in self.json_response:
            return self.json_response['device_score']

    @property
    def pan_source(self):
        if 'pan_source' in self.json_response:
            return self.json_response['pan_source']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def recommendation_reasons(self):
        if 'recommendation_reasons' in self.json_response:
            return self.json_response['recommendation_reasons']

    def __repr__(self):
         return '<Marqeta.response_models.wallet_provider_profile.WalletProviderProfile>'