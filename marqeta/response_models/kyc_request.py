from datetime import datetime, date
import json

class KycRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def notes(self):
        if 'notes' in self.json_response:
            return self.json_response['notes']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def manual_override(self):
        if 'manual_override' in self.json_response:
            return self.json_response['manual_override']

    @property
    def reference_id(self):
        if 'reference_id' in self.json_response:
            return self.json_response['reference_id']

    def __repr__(self):
         return '<Marqeta.response_models.kyc_request.KycRequest>'