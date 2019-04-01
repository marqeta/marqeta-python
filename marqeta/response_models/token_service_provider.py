from datetime import datetime, date
import json


class TokenServiceProvider(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token_reference_id(self):
        return self.json_response.get('token_reference_id', None)

    @property
    def pan_reference_id(self):
        return self.json_response.get('pan_reference_id', None)

    @property
    def correlation_id(self):
        return self.json_response.get('correlation_id', None)

    @property
    def token_requestor_id(self):
        return self.json_response.get('token_requestor_id', None)

    @property
    def token_requestor_name(self):
        return self.json_response.get('token_requestor_name', None)

    @property
    def token_type(self):
        return self.json_response.get('token_type', None)

    @property
    def token_pan(self):
        return self.json_response.get('token_pan', None)

    @property
    def token_expiration(self):
        return self.json_response.get('token_expiration', None)

    @property
    def token_score(self):
        return self.json_response.get('token_score', None)

    @property
    def token_assurance_level(self):
        return self.json_response.get('token_assurance_level', None)

    @property
    def token_eligibility_decision(self):
        return self.json_response.get('token_eligibility_decision', None)

    def __repr__(self):
        return '<Marqeta.response_models.token_service_provider.TokenServiceProvider>' + self.__str__()
