from datetime import datetime, date
from marqeta.response_models.issuer import Issuer
from marqeta.response_models import datetime_object
import json
import re

class Fraud(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def merchant_risk_score(self):
        return self.json_response.get('merchant_risk_score', None)

    @property
    def merchant_risk_score_reason_code(self):
        return self.json_response.get('merchant_risk_score_reason_code', None)


    @property
    def transaction_risk_score(self):
        return self.json_response.get('transaction_risk_score', None)

    @property
    def transaction_risk_score_reason_code(self):
        return self.json_response.get('transaction_risk_score_reason_code', None)


    @property
    def account_risk_score(self):
        return self.json_response.get('account_risk_score', None)

    @property
    def account_risk_score_reason_code(self):
        return self.json_response.get('account_risk_score_reason_code', None)


    @property
    def issuerFraudModel(self):
        if 'issuerFraudModel' in self.json_response:
            return Issuer(self.json_response['issuerFraudModel'])

    def __repr__(self):
         return '<Marqeta.response_models.fraud.Fraud>' + self.__str__()
