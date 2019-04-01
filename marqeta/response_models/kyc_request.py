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
        return self.json_response.get('notes', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def manual_override(self):
        return self.json_response.get('manual_override', None)

    @property
    def reference_id(self):
        return self.json_response.get('reference_id', None)

    def __repr__(self):
        return '<Marqeta.response_models.kyc_request.KycRequest>' + self.__str__()
