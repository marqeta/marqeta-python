from datetime import datetime
from marqeta.response_models.account import Account
from marqeta.response_models.risk_assessment import RiskAssessment

class WalletProviderProfile(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

