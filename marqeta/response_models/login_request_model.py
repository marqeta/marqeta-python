from datetime import datetime, date
import json


class LoginRequestModel(object):

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
        return self.json_response.get('email', None)

    @property
    def password(self):
        return self.json_response.get('password', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.login_request_model.LoginRequestModel>'
