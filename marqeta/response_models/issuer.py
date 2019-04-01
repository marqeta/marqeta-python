from datetime import datetime, date
import json


class Issuer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def success(self):
        return self.json_response.get('success', None)

    @property
    def fraud_score(self):
        return self.json_response.get('fraud_score', None)

    @property
    def fraud_rating(self):
        return self.json_response.get('fraud_rating', None)

    @property
    def rule_violations(self):
        return self.json_response.get('rule_violations', None)

    @property
    def fraud_score_reasons(self):
        return self.json_response.get('fraud_score_reasons', None)

    @property
    def recommended_action(self):
        return self.json_response.get('recommended_action', None)

    @property
    def model(self):
        return self.json_response.get('model', None)

    @property
    def message(self):
        return self.json_response.get('message', None)

    def __repr__(self):
        return '<Marqeta.response_models.issuer.Issuer>' + self.__str__()
