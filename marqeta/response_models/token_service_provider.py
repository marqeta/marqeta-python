from datetime import datetime

class TokenServiceProvider(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token_reference_id(self):
        if 'token_reference_id' in self.json_response:
            return self.json_response['token_reference_id']

    @property
    def pan_reference_id(self):
        if 'pan_reference_id' in self.json_response:
            return self.json_response['pan_reference_id']

    @property
    def correlation_id(self):
        if 'correlation_id' in self.json_response:
            return self.json_response['correlation_id']

    @property
    def token_requestor_id(self):
        if 'token_requestor_id' in self.json_response:
            return self.json_response['token_requestor_id']

    @property
    def token_requestor_name(self):
        if 'token_requestor_name' in self.json_response:
            return self.json_response['token_requestor_name']

    @property
    def token_type(self):
        if 'token_type' in self.json_response:
            return self.json_response['token_type']

    @property
    def token_pan(self):
        if 'token_pan' in self.json_response:
            return self.json_response['token_pan']

    @property
    def token_expiration(self):
        if 'token_expiration' in self.json_response:
            return self.json_response['token_expiration']

    @property
    def token_score(self):
        if 'token_score' in self.json_response:
            return self.json_response['token_score']

    @property
    def token_assurance_level(self):
        if 'token_assurance_level' in self.json_response:
            return self.json_response['token_assurance_level']

    @property
    def token_eligibility_decision(self):
        if 'token_eligibility_decision' in self.json_response:
            return self.json_response['token_eligibility_decision']

