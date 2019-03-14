from datetime import datetime, date
import json

class Issuer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'success' : self.success,
           'fraud_score' : self.fraud_score,
           'fraud_rating' : self.fraud_rating,
           'rule_violations' : self.rule_violations,
           'fraud_score_reasons' : self.fraud_score_reasons,
           'recommended_action' : self.recommended_action,
           'model' : self.model,
           'message' : self.message,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def success(self):
        if 'success' in self.json_response:
            return self.json_response['success']

    @property
    def fraud_score(self):
        if 'fraud_score' in self.json_response:
            return self.json_response['fraud_score']

    @property
    def fraud_rating(self):
        if 'fraud_rating' in self.json_response:
            return self.json_response['fraud_rating']

    @property
    def rule_violations(self):
        if 'rule_violations' in self.json_response:
            return self.json_response['rule_violations']

    @property
    def fraud_score_reasons(self):
        if 'fraud_score_reasons' in self.json_response:
            return self.json_response['fraud_score_reasons']

    @property
    def recommended_action(self):
        if 'recommended_action' in self.json_response:
            return self.json_response['recommended_action']

    @property
    def model(self):
        if 'model' in self.json_response:
            return self.json_response['model']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

    def __repr__(self):
         return '<Marqeta.response_models.issuer.Issuer>'