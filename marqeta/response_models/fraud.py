from datetime import datetime
from marqeta.response_models.issuer import Issuer

class Fraud(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def merchant_risk_score(self):
        if 'merchant_risk_score' in self.json_response:
            return self.json_response['merchant_risk_score']

    @property
    def merchant_risk_score_reason_code(self):
        if 'merchant_risk_score_reason_code' in self.json_response:
            return self.json_response['merchant_risk_score_reason_code']

    @property
    def transaction_risk_score(self):
        if 'transaction_risk_score' in self.json_response:
            return self.json_response['transaction_risk_score']

    @property
    def transaction_risk_score_reason_code(self):
        if 'transaction_risk_score_reason_code' in self.json_response:
            return self.json_response['transaction_risk_score_reason_code']

    @property
    def account_risk_score(self):
        if 'account_risk_score' in self.json_response:
            return self.json_response['account_risk_score']

    @property
    def account_risk_score_reason_code(self):
        if 'account_risk_score_reason_code' in self.json_response:
            return self.json_response['account_risk_score_reason_code']

    @property
    def issuerFraudModel(self):
        if 'issuerFraudModel' in self.json_response:
            return Issuer(self.json_response['issuerFraudModel'])

