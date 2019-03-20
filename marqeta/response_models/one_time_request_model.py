from datetime import datetime, date
import json

class OneTimeRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

    @property
    def password(self):
        if 'password' in self.json_response:
            return self.json_response['password']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    def __repr__(self):
         return '<Marqeta.response_models.one_time_request_model.OneTimeRequestModel>'