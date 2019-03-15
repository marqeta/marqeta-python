from datetime import datetime, date
from marqeta.response_models.issuer import Issuer
import json

class Fraud(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'merchant_risk_score' : self.merchant_risk_score,
           'merchant_risk_score_reason_code' : self.merchant_risk_score_reason_code,
           'transaction_risk_score' : self.transaction_risk_score,
           'transaction_risk_score_reason_code' : self.transaction_risk_score_reason_code,
           'account_risk_score' : self.account_risk_score,
           'account_risk_score_reason_code' : self.account_risk_score_reason_code,
           'issuerFraudModel' : self.issuerFraudModel,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.fraud.Fraud>'