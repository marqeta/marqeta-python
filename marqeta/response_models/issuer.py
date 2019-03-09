from datetime import datetime

class Issuer(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

